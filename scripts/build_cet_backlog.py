"""Inventory the licensed CET-4/CET-6 transcription without copying definitions.

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
    summary = {
        "source": "content/sources/cet2016-word-list.txt",
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "source_rows": len(lines),
        "simple_unique_spellings": len(words),
        "unresolved_variant_tokens": len(unresolved),
        "unresolved_source_rows": len({row for row, _, _ in unresolved}),
        "note": "Combined CET-4/CET-6 transcription; grade labels are not yet verified. Complex variants remain queued for editorial normalization.",
    }
    (OUTPUT / "cet2016_inventory.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
