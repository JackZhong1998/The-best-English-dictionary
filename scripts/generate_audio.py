"""Generate US English audio for every headword and example with edge-tts.

Install edge-tts separately, then run: python3 scripts/generate_audio.py
Existing nonempty MP3 files are skipped, so interrupted runs can resume.
"""

import asyncio
import hashlib
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
VOICE = 'en-US-JennyNeural'
CONCURRENCY = 3
MANIFEST = ROOT / 'content' / 'audio_manifest.json'
RATE = '+0%'
PITCH = '+0Hz'
VOLUME = '+0%'


def clip_digest(text):
    payload = '\0'.join((VOICE, RATE, PITCH, VOLUME, text))
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def clip_name(target):
    return target.relative_to(ROOT / 'public' / 'audio').as_posix()


def jobs():
    for file in sorted((ROOT / 'content' / 'words').glob('*.json')):
        entry = json.loads(file.read_text(encoding='utf-8'))
        word = entry['word']
        # The isolated spelling is ambiguous: context makes each stress pattern clear.
        yield ('to increase' if word == 'increase' else word), ROOT / 'public' / 'audio' / word / 'word.mp3'
        if word == 'increase':
            yield 'an increase', ROOT / 'public' / 'audio' / word / 'noun.mp3'
        for sense in entry['senses']:
            for usage_index, usage in enumerate(sense['usages'], 1):
                for example_index, example in enumerate(usage['examples'], 1):
                    name = f's{sense["id"]}-u{usage_index}-e{example_index}.mp3'
                    yield example['en'], ROOT / 'public' / 'audio' / word / name


async def generate(text, target, semaphore, previous_digest):
    digest = clip_digest(text)
    if target.exists() and target.stat().st_size > 1000 and previous_digest == digest:
        return 'skipped', digest
    async with semaphore:
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_suffix('.tmp')
        for attempt in range(3):
            try:
                await asyncio.wait_for(edge_tts.Communicate(text, VOICE).save(str(temporary)), timeout=25)
                if temporary.stat().st_size < 1000:
                    raise ValueError('empty audio')
                temporary.replace(target)
                return 'created', digest
            except Exception:
                temporary.unlink(missing_ok=True)
                if attempt == 2:
                    raise
                await asyncio.sleep(2 ** attempt)


async def main():
    previous = json.loads(MANIFEST.read_text(encoding='utf-8')) if MANIFEST.exists() else {}
    semaphore = asyncio.Semaphore(CONCURRENCY)
    clips = list(jobs())
    tasks = [generate(text, target, semaphore, previous.get(clip_name(target))) for text, target in clips]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    failures = [result for result in results if isinstance(result, Exception)]
    current = {clip_name(target): result[1] for (_, target), result in zip(clips, results)
               if not isinstance(result, Exception)}
    temporary = MANIFEST.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(current, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    temporary.replace(MANIFEST)
    created = sum(result[0] == 'created' for result in results if not isinstance(result, Exception))
    skipped = sum(result[0] == 'skipped' for result in results if not isinstance(result, Exception))
    print(f'{len(tasks)} files: {created} created, {skipped} skipped, {len(failures)} failed')
    if failures:
        for error in failures[:10]:
            print(f'  {type(error).__name__}: {error}')
        raise SystemExit(1)


if __name__ == '__main__':
    asyncio.run(main())
