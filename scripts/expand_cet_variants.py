"""Create a review queue for compact spellings in the CET transcription.

The generated spellings are *candidates*, not approved headwords. A human or
editorial agent must check them before adding them to the catalog.
"""

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content/wordlists/cet2016_unresolved.tsv"
OUTPUT = ROOT / "content/wordlists/cet2016_variant_candidates.tsv"
SUPERSCRIPTS = str.maketrans("", "", "¹²³⁴⁵⁶⁷⁸⁹⁰")
OPTIONAL = re.compile(r"\(([^()]*)\)")
HEADWORD = re.compile(r"^[a-z][a-z'\-]*$")
# The transcription's shorthand is not reliable enough to expand these by rule.
MANUAL_ONLY = {"(d'état)", "Celsius/-cius", "sober/-re"}


def optionals(value):
    """Expand parenthesized optional letters, such as color(u)r."""
    match = OPTIONAL.search(value)
    if not match:
        return [value]
    start, end = match.span()
    return optionals(value[:start] + value[end:]) + optionals(value[:start] + match.group(1) + value[end:])


def candidates(token):
    if token in MANUAL_ONLY:
        return []
    parts = token.translate(SUPERSCRIPTS).split("/")
    base = optionals(parts[0])
    words = list(base)
    for part in parts[1:]:
        if part.startswith("-"):
            suffix = part[1:]
            if not suffix:
                continue
            words.extend(word[:-len(suffix)] + suffix for word in base if len(word) > len(suffix))
        else:
            words.extend(optionals(part))
    return sorted({word.lower().rstrip(".") for word in words
                   if HEADWORD.fullmatch(word.lower().rstrip("."))})


def main():
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(("source_row", "token", "candidate", "review_status"))
        count = 0
        manual = 0
        for row in rows:
            expanded = candidates(row["token"])
            if not expanded:
                writer.writerow((row["source_row"], row["token"], "", "manual"))
                manual += 1
            for word in expanded:
                writer.writerow((row["source_row"], row["token"], word, "pending"))
                count += 1
    print(f"Queued {count} spelling candidates and {manual} manual-only tokens from {len(rows)} unresolved tokens; all require review.")


if __name__ == "__main__":
    main()
