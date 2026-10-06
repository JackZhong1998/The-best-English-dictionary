"""Inventory an MIT-labeled third-party CET transcription without definitions.

Simple standalone spellings become a resumable backlog. Compact variant
notations stay in a separate review file rather than being silently guessed.
The source row numbers make every extracted spelling traceable.
"""

import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content/sources/cet2016-word-list.txt"
OUTPUT = ROOT / "content/wordlists"
HOMOGRAPH_NUMBERS = str.maketrans("¹²³⁴⁵⁶⁷⁸⁹", "123456789")
SIMPLE = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*[1-9]?")


def inventory(lines):
    words = defaultdict(lambda: {"rows": set(), "forms": set()})
    unresolved = []
    for row, line in enumerate(lines, 1):
        for token in line.split():
            candidate = token.translate(HOMOGRAPH_NUMBERS)
            if SIMPLE.fullmatch(candidate):
                canonical = re.sub(r"[1-9]$", "", candidate).lower()
                words[canonical]["rows"].add(row)
                words[canonical]["forms"].add(token)
            else:
                unresolved.append((row, token, line))
    return words, unresolved


def main():
    source_bytes = SOURCE.read_bytes()
    lines = source_bytes.decode("utf-8-sig").splitlines()
    words, unresolved = inventory(lines)
    OUTPUT.mkdir(exist_ok=True)
    with (OUTPUT / "cet2016_simple.tsv").open("w", encoding="utf-8", newline="") as out:
        writer = csv.writer(out, delimiter="\t")
        writer.writerow(("word", "source_rows", "source_forms"))
        for word, evidence in sorted(words.items()):
            writer.writerow((word, ",".join(map(str, sorted(evidence["rows"]))), ",".join(sorted(evidence["forms"]))))
    with (OUTPUT / "cet2016_unresolved.tsv").open("w", encoding="utf-8", newline="") as out:
        writer = csv.writer(out, delimiter="\t")
        writer.writerow(("source_row", "token", "source_line"))
        writer.writerows(unresolved)
    case_review = [(word, ",".join(map(str, sorted(evidence["rows"]))), ",".join(sorted(evidence["forms"])))
                   for word, evidence in sorted(words.items())
                   if any(any(letter.isupper() for letter in form) for form in evidence["forms"])]
    with (OUTPUT / "cet2016_case_review.tsv").open("w", encoding="utf-8", newline="") as out:
        writer = csv.writer(out, delimiter="\t")
        writer.writerow(("lowercase_key", "source_rows", "source_forms"))
        writer.writerows(case_review)
    summary = {
        "source": "content/sources/cet2016-word-list.txt",
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "source_rows": len(lines),
        "simple_unique_spellings": len(words),
        "unresolved_variant_tokens": len(unresolved),
        "unresolved_source_rows": len({row for row, _, _ in unresolved}),
        "case_sensitive_spellings_for_review": len(case_review),
        "note": "Combined third-party transcription; original syllabus reuse rights and per-word grade labels are unverified. Complex and case-sensitive forms remain queued for editorial normalization.",
    }
    (OUTPUT / "cet2016_inventory.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
