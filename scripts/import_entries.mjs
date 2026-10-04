#!/usr/bin/env node
// Idempotent catalog → Neon import. Run with --dry-run before applying db/schema.sql.
import { readFile } from 'node:fs/promises'
import { resolve } from 'node:path'

const root = resolve(import.meta.dirname, '..')
const dryRun = process.argv.includes('--dry-run')
const batchFlag = process.argv.indexOf('--batch')
const batch = batchFlag < 0 ? null : Number(process.argv[batchFlag + 1])
if (batchFlag >= 0 && (!Number.isSafeInteger(batch) || batch < 1)) {
  throw new Error('--batch requires a positive integer')
}
const raw = JSON.parse(await readFile(resolve(root, 'content/catalog.json'), 'utf8'))
const catalog = Array.isArray(raw) ? raw : raw.entries
if (!Array.isArray(catalog)) throw new Error('content/catalog.json must contain an entries array')

const seen = new Set()
const records = []
for (const candidate of catalog) {
  if (!candidate || typeof candidate !== 'object') throw new Error('Invalid catalog record')
  const word = candidate.word
  if (typeof word !== 'string' || !/^[a-z][a-z'-]{0,63}$/.test(word)) {
    throw new Error(`Invalid word in catalog: ${String(word)}`)
  }
  if (seen.has(word)) throw new Error(`Duplicate catalog word: ${word}`)
  seen.add(word)
  if (batch !== null && candidate.batch !== batch) continue
  if (!['basic', 'draft', 'reviewed', 'published'].includes(candidate.status)) continue
  const publicStatus = candidate.status === 'published' ? 'published' : 'basic'

  const basicZh = candidate.basic_zh
  const levels = candidate.exam_categories ?? candidate.exam_levels
  if (typeof basicZh !== 'string' || !basicZh.trim()) throw new Error(`${word}: missing basic_zh`)
  if (!Array.isArray(levels) || !levels.every(level => typeof level === 'string' && level.trim())) {
    throw new Error(`${word}: invalid exam_categories`)
  }
  const version = candidate.content_version ?? candidate.version ?? 1
  if (!Number.isSafeInteger(version) || version < 0 ||
      (candidate.status === 'published' && version === 0)) {
    throw new Error(`${word}: invalid content_version`)
  }

  let entry = null
  if (publicStatus === 'published') {
    entry = JSON.parse(await readFile(resolve(root, `content/words/${word}.json`), 'utf8'))
    if (entry.word !== word || !Array.isArray(entry.senses) || !entry.senses.length) {
      throw new Error(`${word}: published JSON is incomplete or mismatched`)
    }
  }

  const reviewRecords = candidate.review_records ?? []
  if (!Array.isArray(reviewRecords)) throw new Error(`${word}: invalid review_records`)
  const approvedReview = [...reviewRecords].reverse().find(record =>
    ['accept', 'approved', 'accepted', 'published'].includes(record?.decision))
  const reviewedAt = approvedReview?.date ?? candidate.reviewed_at ?? null
  if (reviewedAt !== null && !Number.isFinite(Date.parse(reviewedAt))) {
    throw new Error(`${word}: invalid reviewed_at`)
  }
  const sourceId = typeof candidate.source === 'string' ? candidate.source : raw.source?.id ?? null
  const sourceUrl = candidate.source_url ?? (typeof candidate.source === 'object' ? candidate.source?.url : null) ?? null
  records.push({ word, basicZh: basicZh.trim(), levels, status: publicStatus,
    entry, sourceId, sourceUrl, version, reviewedAt, reviewRecords })
}
if (!records.length) throw new Error(batch === null ? 'No public records' : `No public records in batch ${batch}`)

console.log(`Validated ${records.length} public words${batch === null ? '' : ` in batch ${batch}`} (${records.filter(r => r.status === 'published').length} published, ${records.filter(r => r.status === 'basic').length} basic).`)
if (dryRun) process.exit(0)
if (!process.env.DATABASE_URL) throw new Error('DATABASE_URL is required to import entries')

const { neon } = await import('@neondatabase/serverless')
const sql = neon(process.env.DATABASE_URL)
for (const record of records) {
  const levels = record.levels.join('|')
  const entryJson = JSON.stringify(record.entry)
  const reviewJson = JSON.stringify(record.reviewRecords)
  await sql`INSERT INTO lexemes
      (word, exam_levels, basic_zh, status, entry, source_id, source_url, version, reviewed_at, review_records)
    VALUES (${record.word}, string_to_array(${levels}, '|'), ${record.basicZh},
      ${record.status}, CASE WHEN ${record.status} = 'basic' THEN NULL ELSE ${entryJson}::jsonb END,
      ${record.sourceId}, ${record.sourceUrl}, ${record.version}, ${record.reviewedAt}::timestamptz,
      ${reviewJson}::jsonb)
    ON CONFLICT (word) DO UPDATE SET
      exam_levels = EXCLUDED.exam_levels,
      basic_zh = EXCLUDED.basic_zh,
      status = EXCLUDED.status,
      entry = EXCLUDED.entry,
      source_id = EXCLUDED.source_id,
      source_url = EXCLUDED.source_url,
      version = EXCLUDED.version,
      reviewed_at = EXCLUDED.reviewed_at,
      review_records = EXCLUDED.review_records`
}
console.log(`Imported ${records.length} words.`)
