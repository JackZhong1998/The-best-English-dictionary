-- Apply this once to a Neon Postgres database before importing content.
CREATE TABLE IF NOT EXISTS lexemes (
  word TEXT PRIMARY KEY CHECK (word ~ '^[a-z][a-z''-]*$'),
  exam_levels TEXT[] NOT NULL DEFAULT '{}',
  basic_zh TEXT NOT NULL CHECK (length(trim(basic_zh)) > 0),
  status TEXT NOT NULL CHECK (status IN ('basic', 'published')),
  entry JSONB,
  source_id TEXT,
  source_url TEXT,
  version INTEGER NOT NULL DEFAULT 0 CHECK (version >= 0),
  reviewed_at TIMESTAMPTZ,
  review_records JSONB NOT NULL DEFAULT '[]'::jsonb,
  CHECK (
    (status = 'basic' AND entry IS NULL) OR
    (status = 'published' AND entry IS NOT NULL)
  )
);

CREATE INDEX IF NOT EXISTS lexemes_word_prefix_idx
  ON lexemes (word text_pattern_ops);
