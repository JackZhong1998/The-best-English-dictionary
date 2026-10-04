"""Focused regression check for revising a published entry."""

import json
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from scripts import content_pipeline as pipeline


class PublishedRevisionTest(unittest.TestCase):
    def test_reviewed_revision_keeps_old_entry_visible_and_can_resume(self):
        fixture = json.loads((Path(__file__).resolve().parents[1] / "content" / "words" / "case.json").read_text(encoding="utf-8"))
        old_paths = pipeline.CATALOG, pipeline.WORDS, pipeline.DRAFTS
        try:
            with tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                pipeline.CATALOG = root / "catalog.json"
                pipeline.WORDS = root / "words"
                pipeline.DRAFTS = root / "drafts"
                pipeline.WORDS.mkdir()
                published = pipeline.WORDS / "case.json"
                published.write_text(json.dumps(fixture, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                original_bytes = published.read_bytes()
                previous_review = {"date": "2026-01-01", "reviewer": "previous-reviewer", "decision": "accept", "notes": "old version", "sha256": "old"}
                pipeline.save_catalog({"entries": [{
                    "word": "case", "batch": 1, "status": "published", "content_version": 1,
                    "author": "original-author", "risk_flags": [], "review_records": [previous_review],
                }]})
                candidate = json.loads(json.dumps(fixture))
                candidate["senses"][0]["usages"][0]["examples"][0]["zh"] = "这是一个特殊的情况。"
                input_file = root / "candidate.json"
                input_file.write_text(json.dumps(candidate, ensure_ascii=False), encoding="utf-8")
                pipeline.stage(Namespace(word="case", file=str(input_file), author="new-author", risk=[]))
                item = pipeline.load_catalog()["entries"][0]
                self.assertEqual(item["status"], "published")
                self.assertEqual(item["content_version"], 1)
                self.assertEqual(item["review_records"], [previous_review])
                self.assertEqual(published.read_bytes(), original_bytes)
                with self.assertRaises(SystemExit):
                    pipeline.review(Namespace(word="case", reviewer="new-author", decision="accept", notes="self", issues_found=None, corrections=None))

                pipeline.review(Namespace(word="case", reviewer="independent-reviewer", decision="accept", notes="checked", issues_found=1, corrections=0))
                # A draft changed after review cannot replace the published entry.
                altered = json.loads((pipeline.DRAFTS / "case.json").read_text(encoding="utf-8"))
                altered["senses"][0]["usages"][0]["examples"][0]["zh"] = "未经审核的改动。"
                (pipeline.DRAFTS / "case.json").write_text(json.dumps(altered, ensure_ascii=False), encoding="utf-8")
                with self.assertRaises(SystemExit):
                    pipeline.publish(Namespace(word="case"))
                self.assertEqual(published.read_bytes(), original_bytes)

                # Restaging retains review history for audit but requires new review.
                pipeline.stage(Namespace(word="case", file=str(input_file), author="new-author", risk=[]))
                self.assertEqual(len(pipeline.load_catalog()["entries"][0]["revision"]["review_records"]), 1)
                pipeline.review(Namespace(word="case", reviewer="independent-reviewer", decision="accept", notes="rechecked", issues_found=0, corrections=1))
                # Simulate an interruption after replacing the file but before
                # saving the catalog; rerunning publish must finish safely.
                published.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                pipeline.publish(Namespace(word="case"))
                item = pipeline.load_catalog()["entries"][0]
                self.assertEqual(item["status"], "published")
                self.assertEqual(item["content_version"], 2)
                self.assertNotIn("revision", item)
                self.assertEqual(item["review_records"][0], previous_review)
                self.assertEqual(len(item["review_records"]), 3)
                self.assertNotIn("issue_count", item["review_records"][0])
                self.assertEqual(item["review_records"][1]["issue_count"], 1)
                self.assertEqual(item["review_records"][2]["correction_count"], 1)
                self.assertEqual(json.loads(published.read_text(encoding="utf-8")), candidate)
        finally:
            pipeline.CATALOG, pipeline.WORDS, pipeline.DRAFTS = old_paths


if __name__ == "__main__":
    unittest.main()
