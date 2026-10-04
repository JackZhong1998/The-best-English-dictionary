"""Generate US English audio for every headword and example with edge-tts.

Install edge-tts separately, then run: python3 scripts/generate_audio.py
Existing nonempty MP3 files are skipped, so interrupted runs can resume.
"""

import asyncio
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
VOICE = 'en-US-JennyNeural'
CONCURRENCY = 3


def jobs():
    for file in sorted((ROOT / 'content' / 'words').glob('*.json')):
        entry = json.loads(file.read_text(encoding='utf-8'))
        word = entry['word']
        yield word, ROOT / 'public' / 'audio' / word / 'word.mp3'
        for sense in entry['senses']:
            for usage_index, usage in enumerate(sense['usages'], 1):
                for example_index, example in enumerate(usage['examples'], 1):
                    name = f's{sense["id"]}-u{usage_index}-e{example_index}.mp3'
                    yield example['en'], ROOT / 'public' / 'audio' / word / name


async def generate(text, target, semaphore):
    if target.exists() and target.stat().st_size > 1000:
        return 'skipped'
    async with semaphore:
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_suffix('.tmp')
        for attempt in range(3):
            try:
                await asyncio.wait_for(edge_tts.Communicate(text, VOICE).save(str(temporary)), timeout=25)
                if temporary.stat().st_size < 1000:
                    raise ValueError('empty audio')
                temporary.replace(target)
                return 'created'
            except Exception:
                temporary.unlink(missing_ok=True)
                if attempt == 2:
                    raise
                await asyncio.sleep(2 ** attempt)


async def main():
    semaphore = asyncio.Semaphore(CONCURRENCY)
    tasks = [generate(text, target, semaphore) for text, target in jobs()]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    failures = [result for result in results if isinstance(result, Exception)]
    print(f'{len(tasks)} files: {results.count("created")} created, {results.count("skipped")} skipped, {len(failures)} failed')
    if failures:
        for error in failures[:10]:
            print(f'  {type(error).__name__}: {error}')
        raise SystemExit(1)


if __name__ == '__main__':
    asyncio.run(main())
