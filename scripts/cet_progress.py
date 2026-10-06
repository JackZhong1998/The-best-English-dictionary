"""Report how much of the combined CET transcription has full entries."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    with (ROOT / "content/wordlists/cet2016_simple.tsv").open(encoding="utf-8", newline="") as source:
        source_words = {row["word"] for row in csv.DictReader(source, delimiter="\t")}
    catalog = json.loads((ROOT / "content/catalog.json").read_text(encoding="utf-8"))
    published = {item["word"] for item in catalog["entries"] if item["status"] == "published"}
    pending = source_words - published
    print(f"Simple source spellings: {len(source_words)}")
    print(f"Published source spellings: {len(source_words & published)}")
    print(f"Pending simple spellings: {len(pending)}")
    print(f"Published pilot words outside simple transcription: {', '.join(sorted(published - source_words)) or 'none'}")
    print("Unresolved compact variants:", sum(1 for _ in (ROOT / "content/wordlists/cet2016_unresolved.tsv").open(encoding="utf-8")) - 1)
    print("Case-sensitive spellings for review:", sum(1 for _ in (ROOT / "content/wordlists/cet2016_case_review.tsv").open(encoding="utf-8")) - 1)


if __name__ == "__main__":
    main()
