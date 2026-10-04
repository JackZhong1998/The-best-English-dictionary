-- Run after db/schema.sql. Audio metadata and approximate anonymous quotas.
-- Report with SELECT * FROM audio_generation_daily ORDER BY day_utc DESC;
-- Failure reasons: SELECT * FROM audio_generation_failures_daily ORDER BY day_utc DESC;
CREATE TABLE IF NOT EXISTS audio_cache (
  cache_key TEXT PRIMARY KEY,
  object_key TEXT NOT NULL,
  state TEXT NOT NULL CHECK (state IN ('pending', 'ready')),
  byte_size BIGINT NOT NULL DEFAULT 0 CHECK (byte_size >= 0),
  lease_token UUID,
  lease_until TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS audio_cache_ready_idx ON audio_cache (state);

CREATE TABLE IF NOT EXISTS audio_visitor_daily (
  day DATE NOT NULL,
  visitor_hash TEXT NOT NULL,
  generated INTEGER NOT NULL CHECK (generated >= 0),
  PRIMARY KEY (day, visitor_hash)
);

CREATE TABLE IF NOT EXISTS audio_global_daily (
  day DATE PRIMARY KEY,
  generated INTEGER NOT NULL CHECK (generated >= 0)
);

-- One durable result per claimed lease. Never store source text, IP, or user agent.
CREATE TABLE IF NOT EXISTS audio_generation_events (
  lease_token UUID PRIMARY KEY,
  cache_key TEXT NOT NULL,
  outcome TEXT NOT NULL CHECK (outcome IN ('success', 'failure', 'recovered')),
  reason TEXT NOT NULL,
  duration_ms INTEGER NOT NULL CHECK (duration_ms >= 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS audio_generation_events_created_idx
  ON audio_generation_events (created_at);

CREATE OR REPLACE VIEW audio_generation_daily AS
SELECT
  (created_at AT TIME ZONE 'UTC')::date AS day_utc,
  count(*) FILTER (WHERE outcome = 'success') AS succeeded,
  count(*) FILTER (WHERE outcome = 'failure') AS failed,
  count(*) FILTER (WHERE outcome = 'recovered') AS recovered,
  count(*) FILTER (WHERE outcome IN ('success', 'failure')) AS attempted,
  round(
    count(*) FILTER (WHERE outcome = 'failure')::numeric /
      nullif(count(*) FILTER (WHERE outcome IN ('success', 'failure')), 0),
    4
  ) AS failure_rate
FROM audio_generation_events
GROUP BY (created_at AT TIME ZONE 'UTC')::date;

CREATE OR REPLACE VIEW audio_generation_failures_daily AS
SELECT
  (created_at AT TIME ZONE 'UTC')::date AS day_utc,
  reason,
  count(*) AS failures
FROM audio_generation_events
WHERE outcome = 'failure'
GROUP BY (created_at AT TIME ZONE 'UTC')::date, reason;
