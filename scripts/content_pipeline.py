"""Resumable, local editorial pipeline. No model or network API is called.

Codex agents author candidate JSON separately. This CLI records their work,
requires an independent reviewer for the 100-word pilot, and publishes only
entries that pass the structural gate. Existing 30 published entries are
grandfathered with an explicit empty review history.
"""

import argparse
import csv
import datetime as dt
import hashlib
import json
import shutil
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "content" / "catalog.json"
SOURCE = ROOT / "content" / "pilot_cet4.tsv"
WORDS = ROOT / "content" / "words"
DRAFTS = ROOT / "content" / "drafts"
BATCH_SIZE = 25
ORIGINAL_WORDS = {
    "break", "call", "case", "change", "charge", "come", "cut", "draw", "drive", "fall",
    "get", "go", "hold", "keep", "leave", "light", "line", "make", "matter", "move",
    "order", "pass", "play", "point", "put", "right", "run", "set", "take", "turn",
}
HEAD_KEYS = {"word", "phonetic", "syllables", "pos", "core_meanings", "etymology", "semantic_shift", "senses"}
SENSE_KEYS = {"id", "part_of_speech", "en_definition", "zh_definition", "usages", "synonyms", "antonyms", "confusables"}


def today():
    return dt.date.today().isoformat()


def content_digest(entry):
    return hashlib.sha256(json.dumps(entry, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def file_digest(data):
    return hashlib.sha256(data).hexdigest()


def nonnegative_int(value):
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("count must be a nonnegative integer")
    return number


def save_catalog(catalog):
    temp = CATALOG.with_suffix(".json.tmp")
    temp.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(CATALOG)


def load_catalog():
    if not CATALOG.exists():
        raise SystemExit("No catalog. Run bootstrap first.")
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def record(catalog, word):
    found = next((item for item in catalog["entries"] if item["word"] == word), None)
    if found is None:
        raise SystemExit(f"Unknown headword: {word}")
    return found


def basic_rows(file=SOURCE, expected_count=100):
    lines = file.read_text(encoding="utf-8").splitlines()
    if lines[0] != "word\tbasic_zh":
        raise SystemExit("Invalid pilot TSV header")
    rows = []
    for line in lines[1:]:
        word, gloss = line.split("\t", 1)
        if not re.fullmatch(r"[a-z]+(?:[-'][a-z]+)*", word) or not gloss.strip():
            raise SystemExit(f"Invalid pilot row: {line}")
        rows.append((word, gloss))
    if len(rows) != expected_count or len(set(w for w, _ in rows)) != expected_count:
        raise SystemExit(f"Wordlist must contain {expected_count} unique headwords")
    return rows


def bootstrap(_args):
    if CATALOG.exists():
        raise SystemExit("Catalog exists. Bootstrap is intentionally non-destructive.")
    rows = basic_rows()
    entries = []
    for index, (word, gloss) in enumerate(rows):
        existing = word in ORIGINAL_WORDS
        entries.append({
            "word": word,
            "exam_categories": ["CET4-level candidate"],
            "status": "published" if existing else "basic",
            "basic_zh": gloss,
            "content_version": 1 if existing else 0,
            "batch": index // BATCH_SIZE + 1,
            "source": "independent_editorial_selection_v1",
            "source_file": "content/pilot_cet4.tsv",
            "author": "legacy_editorial" if existing else None,
            "risk_flags": [],
            "review_records": [],
        })
    if sum(item["status"] == "published" for item in entries) != 30:
        raise SystemExit("Expected exactly 30 existing published entries")
    save_catalog({
        "schema_version": 1,
        "batch_size": BATCH_SIZE,
        "source": {
            "id": "independent_editorial_selection_v1",
            "description": "100 common English headwords independently selected as a CET4-level pilot; not an official exam syllabus or a copied wordlist.",
            "gloss_policy": "Chinese basic glosses are newly written editorial summaries, not copied dictionary definitions.",
            "file": "content/pilot_cet4.tsv",
        },
        "entries": entries,
    })
    print("Bootstrapped 100 headwords: 30 published, 70 basic, four batches of 25.")


def validate_candidate(entry, word):
    problems = []
    if set(entry) != HEAD_KEYS or entry.get("word") != word:
        problems.append("headword/schema mismatch")
    for field in ("phonetic", "etymology", "semantic_shift"):
        if not isinstance(entry.get(field), str):
            problems.append(f"{field} must be a string")
    if not isinstance(entry.get("syllables"), list) or not all(isinstance(part, str) for part in entry["syllables"]) or "".join(entry["syllables"]) != word:
        problems.append("syllables must reconstruct headword")
    if not isinstance(entry.get("pos"), list) or not entry["pos"]:
        problems.append("missing part of speech")
    if not isinstance(entry.get("core_meanings"), list) or not entry["core_meanings"]:
        problems.append("missing core meanings")
    senses = entry.get("senses")
    if not isinstance(senses, list) or not senses:
        problems.append("missing senses")
        return problems
    if isinstance(entry.get("pos"), list):
        declared = set(entry["pos"])
        covered = {sense.get("part_of_speech") for sense in senses if isinstance(sense, dict)}
        if declared != covered:
            problems.append("parts of speech do not match the senses")
    for index, sense in enumerate(senses, 1):
        if not isinstance(sense, dict) or set(sense) != SENSE_KEYS or sense.get("id") != index:
            problems.append(f"sense {index}: schema/id mismatch")
            continue
        for field in ("part_of_speech", "en_definition", "zh_definition"):
            if not isinstance(sense[field], str) or not sense[field].strip():
                problems.append(f"sense {index}: missing {field}")
        for field in ("synonyms", "antonyms", "confusables"):
            items = sense[field]
            if not isinstance(items, list):
                problems.append(f"sense {index}: {field} must be an array")
                continue
            if field != "antonyms" and not items:
                problems.append(f"sense {index}: missing {field} comparison")
            for item in items:
                if not isinstance(item, str) or len(item.strip()) < 8 or (field != "confusables" and "：" not in item):
                    problems.append(f"sense {index}: {field} needs a useful explanation")
        usages = sense.get("usages")
        if not isinstance(usages, list) or not usages:
            problems.append(f"sense {index}: missing usages")
            continue
        for usage in usages:
            if not isinstance(usage, dict) or set(usage) != {"usage_label", "collocations", "examples"}:
                problems.append(f"sense {index}: usage schema mismatch")
                continue
            if not isinstance(usage["collocations"], list) or not isinstance(usage["examples"], list) or len(usage["collocations"]) < 2 or len(usage["examples"]) < 2:
                problems.append(f"sense {index}: need two collocations and examples")
                continue
            for collocation in usage["collocations"]:
                if not isinstance(collocation, dict) or not collocation.get("phrase") or not collocation.get("translation"):
                    problems.append(f"sense {index}: invalid collocation")
            for example in usage["examples"]:
                if not isinstance(example, dict) or not isinstance(example.get("en"), str) or not isinstance(example.get("zh"), str) or not example["en"].strip() or not example["zh"].strip() or len(example["en"].split()) > 16:
                    problems.append(f"sense {index}: invalid example")
    return problems


def status(_args):
    catalog = load_catalog()
    for batch in sorted({item["batch"] for item in catalog["entries"]}):
        items = [item for item in catalog["entries"] if item["batch"] == batch]
        counts = {state: sum(item["status"] == state for item in items) for state in ("basic", "draft", "reviewed", "published")}
        print(f"Batch {batch}: {counts}")
    print("Next basic headwords:", ", ".join(item["word"] for item in catalog["entries"] if item["status"] == "basic") or "none")
    revisions = [item for item in catalog["entries"] if item.get("revision")]
    print("Published entries with pending revisions:", ", ".join(f"{item['word']} ({item['revision']['status']})" for item in revisions) or "none")


def extend(args):
    """Append an independently authored 25-word CET4/CET6/postgraduate batch."""
    catalog = load_catalog()
    rows = basic_rows(Path(args.file), BATCH_SIZE)
    source_evidence = {}
    if args.source_id == "cet2016_mit_transcription":
        if args.category != "CET4_CET6":
            raise SystemExit("Combined CET transcription cannot support a single-level CET4 or CET6 label")
        source_index = ROOT / "content/wordlists/cet2016_simple.tsv"
        with source_index.open(encoding="utf-8", newline="") as handle:
            source_evidence = {line["word"]: [int(row) for row in line["source_rows"].split(",")]
                               for line in csv.DictReader(handle, delimiter="\t")}
        missing = [word for word, _ in rows if word not in source_evidence]
        if missing:
            raise SystemExit("Words missing from CET transcription: " + ", ".join(missing))
    known = {item["word"] for item in catalog["entries"]}
    duplicates = [word for word, _ in rows if word in known]
    if duplicates:
        raise SystemExit("Existing headwords: " + ", ".join(duplicates))
    next_batch = max(item["batch"] for item in catalog["entries"]) + 1
    source_path = ROOT / "content" / "wordlists" / f"batch-{next_batch}.tsv"
    source_path.parent.mkdir(exist_ok=True)
    shutil.copyfile(args.file, source_path)
    for word, gloss in rows:
        catalog["entries"].append({
            "word": word,
            "exam_categories": ["CET4/CET6-syllabus candidate" if args.category == "CET4_CET6" else f"{args.category}-level candidate"],
            "status": "basic",
            "basic_zh": gloss,
            "content_version": 0,
            "batch": next_batch,
            "source": args.source_id,
            "source_file": str(source_path.relative_to(ROOT)),
            "source_rows": source_evidence.get(word, []),
            "author": None,
            "risk_flags": [],
            "review_records": [],
        })
    save_catalog(catalog)
    print(f"Added batch {next_batch}: {BATCH_SIZE} {args.category}-level candidate headwords.")


def review_required(catalog, item):
    if item["batch"] <= 4 or item["risk_flags"]:
        return True
    cohort = [entry["word"] for entry in catalog["entries"] if entry["batch"] == item["batch"]]
    sample = sorted(cohort, key=lambda word: hashlib.sha256(word.encode()).hexdigest())[:3]
    return item["word"] in sample


def stage(args):
    catalog = load_catalog()
    item = record(catalog, args.word)
    candidate = json.loads(Path(args.file).read_text(encoding="utf-8"))
    problems = validate_candidate(candidate, args.word)
    if problems:
        raise SystemExit("Candidate failed: " + "; ".join(problems))
    if item["status"] == "published":
        published = WORDS / f"{args.word}.json"
        if not published.exists():
            raise SystemExit("Published entry file is missing")
        previous = item.get("revision") or {}
        revision = {
            "status": "draft",
            "author": args.author,
            "risk_flags": args.risk or [],
            "base_version": item["content_version"],
            "base_sha256": file_digest(published.read_bytes()),
            "review_records": previous.get("review_records", []),
        }
        DRAFTS.mkdir(exist_ok=True)
        (DRAFTS / f"{args.word}.json").write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        item["revision"] = revision
        save_catalog(catalog)
        print(f"Staged revision of published {args.word} v{item['content_version']}; independent review required.")
        return
    DRAFTS.mkdir(exist_ok=True)
    target = DRAFTS / f"{args.word}.json"
    target.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    item["status"] = "draft"
    item["author"] = args.author
    item["risk_flags"] = args.risk or []
    # Retain prior decisions for audit. Their hashes cannot approve a new draft.
    save_catalog(catalog)
    print(f"Staged {args.word}; independent review {'required' if review_required(catalog, item) else 'sampled for other words in this batch'}.")


def review(args):
    catalog = load_catalog()
    item = record(catalog, args.word)
    revision = item.get("revision") if item["status"] == "published" else None
    if revision:
        if revision["status"] != "draft":
            raise SystemExit("Restage the changed revision before reviewing it again")
        author = revision["author"]
    elif item["status"] == "draft":
        author = item["author"]
    else:
        raise SystemExit("Only staged drafts can be reviewed")
    if args.reviewer == author:
        raise SystemExit("Reviewer must differ from author")
    candidate = json.loads((DRAFTS / f"{args.word}.json").read_text(encoding="utf-8"))
    problems = validate_candidate(candidate, args.word)
    if problems:
        raise SystemExit("Draft no longer passes validation: " + "; ".join(problems))
    digest = content_digest(candidate)
    review_record = {"date": today(), "reviewer": args.reviewer, "decision": args.decision, "notes": args.notes, "sha256": digest}
    if args.issues_found is not None:
        review_record["issue_count"] = args.issues_found
    if args.corrections is not None:
        review_record["correction_count"] = args.corrections
    if revision:
        revision["review_records"].append(review_record)
        if args.decision == "accept":
            revision["status"] = "reviewed"
    else:
        item["review_records"].append(review_record)
        if args.decision == "accept":
            item["status"] = "reviewed"
    save_catalog(catalog)
    print(f"Recorded {args.decision} review for {args.word}.")


def publish(args):
    catalog = load_catalog()
    item = record(catalog, args.word)
    if item["status"] == "published" and item.get("revision"):
        revision = item["revision"]
        if revision["status"] != "reviewed" or not revision["review_records"]:
            raise SystemExit("Published-entry revisions require an accepted independent review")
        latest = revision["review_records"][-1]
        if latest["decision"] != "accept" or latest["reviewer"] == revision["author"]:
            raise SystemExit("Revision needs an independent accepted review")
        if revision["base_version"] != item["content_version"]:
            raise SystemExit("Published version changed; restage the revision")
        source = DRAFTS / f"{args.word}.json"
        candidate = json.loads(source.read_text(encoding="utf-8"))
        problems = validate_candidate(candidate, args.word)
        if problems:
            raise SystemExit("Draft failed validation: " + "; ".join(problems))
        if latest["sha256"] != content_digest(candidate):
            raise SystemExit("Revision changed after review; restage and review again")
        rendered = (json.dumps(candidate, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        target = WORDS / f"{args.word}.json"
        current_digest = file_digest(target.read_bytes())
        if current_digest == revision["base_sha256"]:
            temporary = target.with_suffix(".json.tmp")
            temporary.write_bytes(rendered)
            temporary.replace(target)
        elif current_digest != file_digest(rendered):
            raise SystemExit("Published file changed outside this revision; restage")
        # If the file already matches rendered, the last publish was interrupted
        # after file replacement. Finalize the catalog without replacing again.
        item["content_version"] = revision["base_version"] + 1
        item["author"] = revision["author"]
        item["risk_flags"] = revision["risk_flags"]
        item["review_records"].extend(revision["review_records"])
        del item["revision"]
        save_catalog(catalog)
        print(f"Published revised {args.word} v{item['content_version']}.")
        return
    if item["status"] not in ("draft", "reviewed"):
        raise SystemExit("Only staged or reviewed candidates can be published")
    if review_required(catalog, item) and item["status"] != "reviewed":
        raise SystemExit("Independent review is required for this word")
    source = DRAFTS / f"{args.word}.json"
    candidate = json.loads(source.read_text(encoding="utf-8"))
    problems = validate_candidate(candidate, args.word)
    if problems:
        raise SystemExit("Draft failed validation: " + "; ".join(problems))
    digest = content_digest(candidate)
    latest = item["review_records"][-1] if item["review_records"] else None
    if latest and latest["decision"] == "reject":
        raise SystemExit("Rejected draft needs a new accepted review")
    if latest and latest["sha256"] != digest:
        raise SystemExit("Draft changed after its last review; review the current draft")
    if item["status"] == "reviewed" and (not latest or latest["decision"] != "accept" or latest["reviewer"] == item["author"]):
        raise SystemExit("Independent accepted review is required")
    shutil.copyfile(source, WORDS / f"{args.word}.json")
    item["status"] = "published"
    item["content_version"] += 1
    save_catalog(catalog)
    print(f"Published {args.word} v{item['content_version']}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("bootstrap").set_defaults(func=bootstrap)
    commands.add_parser("status").set_defaults(func=status)
    extended = commands.add_parser("extend")
    extended.add_argument("file", help="TSV with word and original basic_zh columns, exactly 25 rows")
    extended.add_argument("--category", choices=("CET4", "CET6", "CET4_CET6", "postgraduate"), required=True)
    extended.add_argument("--source-id", choices=("independent_editorial_selection_v1", "cet2016_mit_transcription"),
                          default="independent_editorial_selection_v1")
    extended.set_defaults(func=extend)
    staged = commands.add_parser("stage")
    staged.add_argument("word")
    staged.add_argument("file")
    staged.add_argument("--author", required=True)
    staged.add_argument("--risk", action="append", choices=("multiple_pronunciations", "multiple_etymologies", "phrasal_verb"))
    staged.set_defaults(func=stage)
    reviewed = commands.add_parser("review")
    reviewed.add_argument("word")
    reviewed.add_argument("--reviewer", required=True)
    reviewed.add_argument("--decision", choices=("accept", "reject"), required=True)
    reviewed.add_argument("--notes", required=True)
    reviewed.add_argument("--issues-found", type=nonnegative_int, help="Number of issues found in this review")
    reviewed.add_argument("--corrections", type=nonnegative_int, help="Number of corrections completed in this review")
    reviewed.set_defaults(func=review)
    published = commands.add_parser("publish")
    published.add_argument("word")
    published.set_defaults(func=publish)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
