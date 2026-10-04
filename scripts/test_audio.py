"""Run with: python3 -m unittest scripts.test_audio"""

import unittest

from api.audio import AudioError, AudioService, clip_key, parse_locator, resolve_text


ENTRY = {
    "word": "run",
    "senses": [{"id": 3, "usages": [{"examples": [
        {"en": "She runs the shop.", "zh": "她经营那家店。"},
        {"en": "He runs a small team.", "zh": "他管理一个小团队。"},
    ]}]}],
}


class FakeRepository:
    def __init__(self, entry=ENTRY):
        self.entry = entry
        self.state = "absent"
        self.claims = 0
        self.events = []

    def lookup_entry(self, word):
        return self.entry if word == "run" else None

    def lookup_ready_clip(self, key):
        return f"audio/v1/{key}.mp3" if self.state == "ready" else None

    def claim_clip(self, key, object_key, visitor, visitor_limit, global_limit, storage_limit):
        self.claims += 1
        if self.state == "ready":
            return "ready", object_key, None
        if self.state == "pending":
            return "pending", None, None
        self.state = "pending"
        return "claimed", object_key, "test-lease"

    def complete(self, key, token, size, outcome, duration_ms):
        assert token == "test-lease" and size > 1000
        self.state = "ready"
        self.events.append((outcome, "generated" if outcome == "success" else "object_already_present"))

    def release(self, key, token, reason, duration_ms):
        self.state = "absent"
        self.events.append(("failure", reason))

    def invalidate(self, key):
        self.state = "absent"


class FakeStorage:
    def __init__(self):
        self.files = {}

    def exists(self, key):
        return len(self.files[key]) if key in self.files else None

    def upload(self, key, data):
        self.files[key] = data

    def url(self, key):
        return "https://example.invalid/" + key


class FakeSynth:
    def __init__(self):
        self.calls = []

    def synthesize(self, text):
        self.calls.append(text)
        return b"a" * 1500


class AudioTests(unittest.TestCase):
    def test_locator_rejects_arbitrary_text_and_partial_positions(self):
        for query in ("word=run&text=secret", "word=run&senseId=3",
                      "word=run&senseId=3&usageId=1&exampleId=0", "word=run&word=go"):
            with self.subTest(query=query), self.assertRaises(AudioError):
                parse_locator(query)
        self.assertEqual(parse_locator("word=RUN&senseId=3&usageId=1&exampleId=2"),
                         ("run", (3, 1, 2)))

    def test_only_stored_example_is_spoken(self):
        self.assertEqual(resolve_text(ENTRY, "run", (3, 1, 2)), "He runs a small team.")
        for locator in ((2, 1, 1), (3, 2, 1), (3, 1, 3)):
            with self.subTest(locator=locator), self.assertRaises(AudioError):
                resolve_text(ENTRY, "run", locator)

    def test_key_is_content_addressed(self):
        self.assertEqual(clip_key("run"), clip_key("run"))
        self.assertNotEqual(clip_key("run"), clip_key("Run"))

    def test_generation_then_cache_hit(self):
        repository, storage, synth = FakeRepository(), FakeStorage(), FakeSynth()
        service = AudioService(repository, storage, synth)
        first_status, first = service.fetch("run", (3, 1, 1), "visitor")
        second_status, second = service.fetch("run", (3, 1, 1), "visitor")
        self.assertEqual((first_status, second_status), (200, 200))
        self.assertEqual((first["cached"], second["cached"]), (False, True))
        self.assertEqual(synth.calls, ["She runs the shop."])
        self.assertEqual(repository.events, [("success", "generated")])

    def test_paused_generation_keeps_cached_audio_available(self):
        repository, storage, synth = FakeRepository(), FakeStorage(), FakeSynth()
        key = f"audio/v1/{clip_key('run')}.mp3"
        storage.files[key] = b"a" * 1500
        repository.state = "ready"
        status, response = AudioService(repository, storage, synth, generation_enabled=False).fetch("run", None, "visitor")
        self.assertEqual((status, response["cached"]), (200, True))
        self.assertEqual(repository.claims, 0)
        self.assertEqual(synth.calls, [])
        repository.state = "absent"
        with self.assertRaises(AudioError):
            AudioService(repository, storage, synth, generation_enabled=False).fetch("run", None, "visitor")

    def test_active_lease_is_pending(self):
        repository = FakeRepository()
        repository.state = "pending"
        status, body = AudioService(repository, FakeStorage(), FakeSynth()).fetch("run", None, "visitor")
        self.assertEqual((status, body["status"]), (202, "generating"))

    def test_failed_generation_releases_lease_for_retry(self):
        class FailingSynth:
            def synthesize(self, text):
                raise RuntimeError("temporary TTS failure")

        repository = FakeRepository()
        with self.assertRaises(RuntimeError):
            AudioService(repository, FakeStorage(), FailingSynth()).fetch("run", None, "visitor")
        self.assertEqual(repository.state, "absent")
        self.assertEqual(repository.events, [("failure", "tts_error")])

        status, _ = AudioService(repository, FakeStorage(), FakeSynth()).fetch("run", None, "visitor")
        self.assertEqual(status, 200)
        self.assertEqual(repository.events[-1], ("success", "generated"))

    def test_storage_failure_has_reason_and_releases_lease(self):
        class FailingStorage(FakeStorage):
            def upload(self, key, data):
                raise RuntimeError("R2 unavailable")

        repository = FakeRepository()
        with self.assertRaises(RuntimeError):
            AudioService(repository, FailingStorage(), FakeSynth()).fetch("run", None, "visitor")
        self.assertEqual(repository.state, "absent")
        self.assertEqual(repository.events, [("failure", "storage_error")])

    def test_deleted_cached_object_can_be_rebuilt(self):
        repository, storage, synth = FakeRepository(), FakeStorage(), FakeSynth()
        repository.state = "ready"
        status, response = AudioService(repository, storage, synth).fetch("run", None, "visitor")
        self.assertEqual(status, 200)
        self.assertFalse(response["cached"])
        self.assertEqual(synth.calls, ["run"])
        self.assertEqual(repository.events, [("success", "generated")])

    def test_existing_object_recovered_without_synthesizing(self):
        repository, storage, synth = FakeRepository(), FakeStorage(), FakeSynth()
        storage.files[f"audio/v1/{clip_key('run')}.mp3"] = b"a" * 1500
        status, response = AudioService(repository, storage, synth).fetch("run", None, "visitor")
        self.assertEqual(status, 200)
        self.assertFalse(response["cached"])
        self.assertEqual(synth.calls, [])
        self.assertEqual(repository.events, [("recovered", "object_already_present")])

    def test_unpublished_or_unknown_word_fails(self):
        with self.assertRaises(AudioError) as caught:
            AudioService(FakeRepository(None), FakeStorage(), FakeSynth()).fetch("run", None, "visitor")
        self.assertEqual(caught.exception.status, 404)


if __name__ == "__main__":
    unittest.main()
