"""Vercel Function: resolve published dictionary audio and cache generated US speech.

GET /api/audio?word=run                         (headword)
GET /api/audio?word=run&senseId=1&usageId=1&exampleId=2

The request never carries TTS text. Only a published lexeme can resolve to audio.

Required environment: DATABASE_URL, R2_ACCOUNT_ID, R2_BUCKET,
R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, AUDIO_VISITOR_SALT.
Optional limits: AUDIO_VISITOR_DAILY_LIMIT (5), AUDIO_GLOBAL_DAILY_LIMIT (100),
AUDIO_STORAGE_MAX_BYTES (8000000000).
"""

from __future__ import annotations

import asyncio
import hashlib
import hmac
import json
import os
import re
import tempfile
import time
import uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

VOICE = "en-US-JennyNeural"
RATE = "+0%"
PITCH = "+0Hz"
VOLUME = "+0%"
WORD_RE = re.compile(r"^[a-z][a-z'-]{0,63}$")
MAX_TEXT = 500


class AudioError(Exception):
    def __init__(self, status: int, code: str, retry_after: int | None = None):
        super().__init__(code)
        self.status = status
        self.code = code
        self.retry_after = retry_after


def parse_locator(query: str) -> tuple[str, tuple[int, int, int] | None]:
    values = parse_qs(query, keep_blank_values=True)
    allowed = {"word", "senseId", "usageId", "exampleId"}
    if not values or any(key not in allowed or len(items) != 1 for key, items in values.items()):
        raise AudioError(400, "invalid_locator")
    word = values.get("word", [""])[0].lower()
    if not WORD_RE.fullmatch(word):
        raise AudioError(400, "invalid_locator")
    keys = ("senseId", "usageId", "exampleId")
    if not any(key in values for key in keys):
        return word, None
    if not all(key in values for key in keys):
        raise AudioError(400, "invalid_locator")
    numbers = []
    for key in keys:
        raw = values[key][0]
        if not re.fullmatch(r"[1-9][0-9]{0,3}", raw):
            raise AudioError(400, "invalid_locator")
        numbers.append(int(raw))
    return word, tuple(numbers)


def resolve_text(entry: dict, word: str, locator: tuple[int, int, int] | None) -> str:
    if entry.get("word") != word:
        raise AudioError(404, "not_found")
    if locator is None:
        text = word
    else:
        sense_id, usage_id, example_id = locator
        try:
            senses = entry["senses"]
            sense = next(s for s in senses if s["id"] == sense_id)
            text = sense["usages"][usage_id - 1]["examples"][example_id - 1]["en"]
        except (KeyError, IndexError, StopIteration, TypeError):
            raise AudioError(404, "not_found") from None
    if not isinstance(text, str) or not text.strip() or len(text) > MAX_TEXT:
        raise AudioError(404, "not_found")
    return text.strip()


def clip_key(text: str) -> str:
    settings = json.dumps(
        {"text": text, "voice": VOICE, "rate": RATE, "pitch": PITCH, "volume": VOLUME},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    )
    return hashlib.sha256(settings.encode("utf-8")).hexdigest()


def visitor_hash(ip: str, user_agent: str, secret: str) -> str:
    # A daily HMAC avoids keeping raw IP addresses and prevents clients from
    # choosing an arbitrary quota identity through a cookie or query parameter.
    today = datetime.now(timezone.utc).date().isoformat()
    message = f"{today}\n{ip}\n{user_agent}".encode("utf-8")
    return hmac.new(secret.encode("utf-8"), message, hashlib.sha256).hexdigest()


class PostgresRepository:
    def __init__(self, database_url: str):
        import psycopg

        self.database_url = database_url
        self.psycopg = psycopg

    def lookup_entry(self, word: str) -> dict | None:
        with self.psycopg.connect(self.database_url, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT entry FROM lexemes WHERE word = %s AND status = 'published' AND entry IS NOT NULL",
                    (word,),
                )
                row = cur.fetchone()
        if not row:
            return None
        return json.loads(row[0]) if isinstance(row[0], str) else row[0]

    def claim_clip(
        self, key: str, object_key: str, visitor: str, visitor_limit: int,
        global_limit: int, storage_limit: int,
    ) -> tuple[str, str | None, str | None]:
        """Atomically return ready/pending/claimed/limited and the lease token.

        Counts are charged only to the request that owns a new generation lease.
        A crashed worker's lease expires and can be reclaimed.
        """
        token = str(uuid.uuid4())
        with self.psycopg.connect(self.database_url, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO audio_cache(cache_key, object_key, state) VALUES (%s, %s, 'pending') "
                    "ON CONFLICT (cache_key) DO NOTHING",
                    (key, object_key),
                )
                cur.execute(
                    "SELECT state, object_key, lease_until FROM audio_cache WHERE cache_key = %s FOR UPDATE",
                    (key,),
                )
                state, stored_key, lease_until = cur.fetchone()
                if state == "ready":
                    return "ready", stored_key, None
                if lease_until and lease_until > datetime.now(timezone.utc):
                    return "pending", None, None
                # Serialize quota checks across keys. This also prevents two
                # requests from both claiming the final global allowance.
                cur.execute("SELECT pg_advisory_xact_lock(830401)")
                cur.execute("SELECT COALESCE(SUM(byte_size), 0) FROM audio_cache WHERE state = 'ready'")
                if cur.fetchone()[0] >= storage_limit:
                    conn.rollback()
                    return "storage_limit", None, None
                cur.execute(
                    "INSERT INTO audio_global_daily(day, generated) VALUES (CURRENT_DATE, 1) "
                    "ON CONFLICT (day) DO UPDATE SET generated = audio_global_daily.generated + 1 "
                    "WHERE audio_global_daily.generated < %s RETURNING generated",
                    (global_limit,),
                )
                if cur.fetchone() is None:
                    conn.rollback()
                    return "global_limit", None, None
                cur.execute(
                    "INSERT INTO audio_visitor_daily(day, visitor_hash, generated) "
                    "VALUES (CURRENT_DATE, %s, 1) "
                    "ON CONFLICT (day, visitor_hash) DO UPDATE "
                    "SET generated = audio_visitor_daily.generated + 1 "
                    "WHERE audio_visitor_daily.generated < %s RETURNING generated",
                    (visitor, visitor_limit),
                )
                if cur.fetchone() is None:
                    conn.rollback()
                    return "daily_limit", None, None
                cur.execute(
                    "UPDATE audio_cache SET state = 'pending', object_key = %s, lease_token = %s, "
                    "lease_until = now() + interval '45 seconds', updated_at = now() "
                    "WHERE cache_key = %s",
                    (object_key, token, key),
                )
        return "claimed", object_key, token

    def complete(self, key: str, token: str, size: int, outcome: str, duration_ms: int) -> None:
        with self.psycopg.connect(self.database_url, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE audio_cache SET state = 'ready', byte_size = %s, "
                    "lease_token = NULL, lease_until = NULL, updated_at = now() "
                    "WHERE cache_key = %s AND lease_token = %s",
                    (size, key, token),
                )
                if cur.rowcount != 1:
                    raise AudioError(503, "lease_expired", retry_after=2)

                cur.execute(
                    "INSERT INTO audio_generation_events"
                    "(lease_token, cache_key, outcome, reason, duration_ms) "
                    "VALUES (%s, %s, %s, %s, %s) ON CONFLICT (lease_token) DO NOTHING",
                    (token, key, outcome,
                     "generated" if outcome == "success" else "object_already_present", duration_ms),
                )

    def release(self, key: str, token: str, reason: str, duration_ms: int) -> None:
        with self.psycopg.connect(self.database_url, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE audio_cache SET lease_token = NULL, lease_until = NULL, updated_at = now() "
                    "WHERE cache_key = %s AND lease_token = %s AND state = 'pending'",
                    (key, token),
                )
                cur.execute(
                    "INSERT INTO audio_generation_events"
                    "(lease_token, cache_key, outcome, reason, duration_ms) "
                    "VALUES (%s, %s, 'failure', %s, %s) "
                    "ON CONFLICT (lease_token) DO NOTHING",
                    (token, key, reason, duration_ms),
                )

    def invalidate(self, key: str) -> None:
        with self.psycopg.connect(self.database_url, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE audio_cache SET state = 'pending', byte_size = 0, "
                            "lease_token = NULL, lease_until = NULL WHERE cache_key = %s AND state = 'ready'", (key,))


class R2Storage:
    def __init__(self):
        import boto3
        from botocore.config import Config

        account = os.environ["R2_ACCOUNT_ID"]
        self.bucket = os.environ["R2_BUCKET"]
        self.client = boto3.client(
            "s3", endpoint_url=f"https://{account}.r2.cloudflarestorage.com",
            aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
            region_name="auto", config=Config(signature_version="s3v4"),
        )

    def exists(self, object_key: str) -> int | None:
        from botocore.exceptions import ClientError

        try:
            response = self.client.head_object(Bucket=self.bucket, Key=object_key)
            return int(response["ContentLength"])
        except ClientError as exc:
            if exc.response.get("ResponseMetadata", {}).get("HTTPStatusCode") == 404:
                return None
            raise

    def upload(self, object_key: str, data: bytes) -> None:
        self.client.put_object(
            Bucket=self.bucket, Key=object_key, Body=data, ContentType="audio/mpeg",
            CacheControl="public, max-age=31536000, immutable",
        )

    def url(self, object_key: str) -> str:
        return self.client.generate_presigned_url(
            "get_object", Params={"Bucket": self.bucket, "Key": object_key}, ExpiresIn=3600,
        )


class EdgeSynthesizer:
    def synthesize(self, text: str) -> bytes:
        import edge_tts

        async def run(path: Path) -> None:
            communicate = edge_tts.Communicate(
                text, VOICE, rate=RATE, pitch=PITCH, volume=VOLUME,
            )
            await asyncio.wait_for(communicate.save(str(path)), timeout=25)

        with tempfile.TemporaryDirectory(prefix="dictionary-audio-") as directory:
            path = Path(directory) / "clip.mp3"
            asyncio.run(run(path))
            data = path.read_bytes()
        if len(data) < 1000:
            raise AudioError(503, "generation_failed", retry_after=3)
        return data


class AudioService:
    def __init__(self, repository, storage, synthesizer, visitor_limit=5,
                 global_limit=100, storage_limit=8_000_000_000):
        self.repository = repository
        self.storage = storage
        self.synthesizer = synthesizer
        self.visitor_limit = visitor_limit
        self.global_limit = global_limit
        self.storage_limit = storage_limit

    def fetch(self, word: str, locator: tuple[int, int, int] | None, visitor: str) -> tuple[int, dict]:
        entry = self.repository.lookup_entry(word)
        if entry is None:
            raise AudioError(404, "not_found")
        text = resolve_text(entry, word, locator)
        key = clip_key(text)
        object_key = f"audio/v1/{key}.mp3"
        for _ in range(2):
            state, stored_key, token = self.repository.claim_clip(
                key, object_key, visitor, self.visitor_limit,
                self.global_limit, self.storage_limit,
            )
            if state == "ready":
                if self.storage.exists(stored_key) is not None:
                    return 200, {"status": "ready", "url": self.storage.url(stored_key), "cached": True}
                self.repository.invalidate(key)
                continue
            if state == "pending":
                return 202, {"status": "generating", "retryAfter": 2}
            if state in {"daily_limit", "global_limit", "storage_limit"}:
                raise AudioError(429, state, retry_after=86400 if state != "storage_limit" else None)
            if state == "claimed":
                started = time.monotonic()
                stage = "storage_check"
                try:
                    size = self.storage.exists(object_key)
                    outcome = "recovered" if size is not None else "success"
                    if size is None:
                        stage = "tts"
                        data = self.synthesizer.synthesize(text)
                        stage = "storage_upload"
                        self.storage.upload(object_key, data)
                        size = len(data)
                    stage = "database_finalize"
                    self.repository.complete(
                        key, token, size, outcome, int((time.monotonic() - started) * 1000),
                    )
                except Exception as exc:
                    if stage == "tts":
                        if isinstance(exc, (TimeoutError, asyncio.TimeoutError)):
                            reason = "tts_timeout"
                        elif isinstance(exc, AudioError) and exc.code == "generation_failed":
                            reason = "tts_empty_audio"
                        else:
                            reason = "tts_error"
                    elif stage.startswith("storage_"):
                        reason = "storage_error"
                    elif isinstance(exc, AudioError) and exc.code == "lease_expired":
                        reason = "lease_expired"
                    else:
                        reason = "database_error"
                    try:
                        self.repository.release(
                            key, token, reason, int((time.monotonic() - started) * 1000),
                        )
                    except Exception:
                        pass
                    raise
                return 200, {"status": "ready", "url": self.storage.url(object_key), "cached": False}
        raise AudioError(503, "unavailable", retry_after=2)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            word, locator = parse_locator(urlsplit(self.path).query)
            salt = os.environ["AUDIO_VISITOR_SALT"]
            # Vercel sets x-forwarded-for; clients may spoof its first element,
            # so this is deliberately an approximate anonymous limit.
            ip = self.headers.get("x-vercel-forwarded-for") or self.headers.get("x-forwarded-for", "unknown")
            user_agent = self.headers.get("user-agent", "")[:200]
            visitor = visitor_hash(ip[:200], user_agent, salt)
            service = AudioService(
                PostgresRepository(os.environ["DATABASE_URL"]), R2Storage(), EdgeSynthesizer(),
                visitor_limit=int(os.getenv("AUDIO_VISITOR_DAILY_LIMIT", "5")),
                global_limit=int(os.getenv("AUDIO_GLOBAL_DAILY_LIMIT", "100")),
                storage_limit=int(os.getenv("AUDIO_STORAGE_MAX_BYTES", "8000000000")),
            )
            status, payload = service.fetch(word, locator, visitor)
        except AudioError as exc:
            status, payload = exc.status, {"error": exc.code}
            if exc.retry_after:
                payload["retryAfter"] = exc.retry_after
        except Exception:
            # Never expose credentials, database errors, or the source text.
            status, payload = 503, {"error": "unavailable", "retryAfter": 3}
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        if "retryAfter" in payload:
            self.send_header("Retry-After", str(payload["retryAfter"]))
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
