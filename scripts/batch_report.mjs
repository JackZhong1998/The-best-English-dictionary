#!/usr/bin/env node
// Read-only editorial and asset inventory. Notes are qualitative; never infer
// an issue count from their wording. Future review records may add numeric
// issue_count / correction_count or issues[] / corrections[].
import fs from 'node:fs'
import path from 'node:path'

const root = path.resolve(import.meta.dirname, '..')
const asJson = process.argv.includes('--json')
const catalog = JSON.parse(fs.readFileSync(path.join(root, 'content/catalog.json'), 'utf8'))
if (!Array.isArray(catalog.entries)) throw new Error('Catalog entries must be an array')

function recordedCount(record, numericKey, arrayKey) {
  if (Number.isSafeInteger(record?.[numericKey]) && record[numericKey] >= 0) return record[numericKey]
  if (Array.isArray(record?.[arrayKey])) return record[arrayKey].length
  return null
}

function assetInventory(word) {
  const file = path.join(root, 'content/words', `${word}.json`)
  if (!fs.existsSync(file)) return { json: 'missing', audio: 'unknown', filesPresent: 0, filesExpected: 0 }
  let entry
  try { entry = JSON.parse(fs.readFileSync(file, 'utf8')) } catch {
    return { json: 'invalid', audio: 'unknown', filesPresent: 0, filesExpected: 0 }
  }
  if (entry.word !== word || !Array.isArray(entry.senses) || !entry.senses.length) {
    return { json: 'invalid', audio: 'unknown', filesPresent: 0, filesExpected: 0 }
  }
  const names = ['word']
  if (word === 'increase') names.push('noun')
  for (const sense of entry.senses) {
    if (!Array.isArray(sense.usages)) return { json: 'invalid', audio: 'unknown', filesPresent: 0, filesExpected: 0 }
    for (const [usageIndex, usage] of sense.usages.entries()) {
      if (!Array.isArray(usage.examples)) return { json: 'invalid', audio: 'unknown', filesPresent: 0, filesExpected: 0 }
      for (const [exampleIndex] of usage.examples.entries()) {
        names.push(`s${sense.id}-u${usageIndex + 1}-e${exampleIndex + 1}`)
      }
    }
  }
  const filesPresent = names.filter(name => {
    const audioFile = path.join(root, 'public/audio', word, `${name}.mp3`)
    return fs.existsSync(audioFile) && fs.statSync(audioFile).size >= 1000
  }).length
  return {
    json: 'readable',
    audio: filesPresent === 0 ? 'on_demand' : filesPresent === names.length ? 'complete' : 'partial',
    filesPresent,
    filesExpected: names.length,
  }
}

const batches = [...new Set(catalog.entries.map(item => item.batch))].sort((a, b) => a - b)
const report = batches.map(batch => {
  const entries = catalog.entries.filter(item => item.batch === batch)
  const statuses = { basic: 0, draft: 0, reviewed: 0, published: 0 }
  const reviews = { accepted: 0, rejected: 0, issue_count: null, correction_count: null,
    issues_with_count: 0, corrections_with_count: 0,
    issues_unrecorded: 0, corrections_unrecorded: 0 }
  const assets = { json_readable: 0, json_missing: 0, json_invalid: 0,
    audio_complete: 0, audio_partial: 0, audio_on_demand: 0, audio_unknown: 0,
    audio_files_present: 0, audio_files_expected: 0 }

  for (const item of entries) {
    if (!(item.status in statuses)) throw new Error(`${item.word}: unknown status ${item.status}`)
    statuses[item.status]++
    for (const review of item.review_records ?? []) {
      if (review.decision === 'accept') reviews.accepted++
      if (review.decision === 'reject') reviews.rejected++
      const issues = recordedCount(review, 'issue_count', 'issues')
      const corrections = recordedCount(review, 'correction_count', 'corrections')
      if (issues === null) reviews.issues_unrecorded++
      else { reviews.issue_count = (reviews.issue_count ?? 0) + issues; reviews.issues_with_count++ }
      if (corrections === null) reviews.corrections_unrecorded++
      else { reviews.correction_count = (reviews.correction_count ?? 0) + corrections; reviews.corrections_with_count++ }
    }
    if (item.status !== 'published') continue
    const inventory = assetInventory(item.word)
    assets[`json_${inventory.json}`]++
    assets[`audio_${inventory.audio}`]++
    assets.audio_files_present += inventory.filesPresent
    assets.audio_files_expected += inventory.filesExpected
  }
  return { batch, headwords: entries.length, statuses, reviews, assets }
})

if (asJson) {
  console.log(JSON.stringify({ generated_at: new Date().toISOString(), batches: report }, null, 2))
} else {
  const countLabel = (total, withCount, withoutCount) => {
    if (withCount === 0) return withoutCount ? `not recorded (${withoutCount} reviews)` : 'not applicable (no reviews)'
    return `${total} recorded (${withCount} reviews with count, ${withoutCount} without)`
  }
  for (const row of report) {
    const { statuses: s, reviews: r, assets: a } = row
    console.log(`Batch ${row.batch} (${row.headwords} words): ${s.basic} basic, ${s.draft} draft, ${s.reviewed} reviewed, ${s.published} published`)
    console.log(`  Reviews: ${r.accepted} accepted, ${r.rejected} rejected; issues ${countLabel(r.issue_count, r.issues_with_count, r.issues_unrecorded)}; corrections ${countLabel(r.correction_count, r.corrections_with_count, r.corrections_unrecorded)}`)
    console.log(`  Published JSON: ${a.json_readable} readable, ${a.json_missing} missing, ${a.json_invalid} invalid`)
    console.log(`  Audio: ${a.audio_complete} complete, ${a.audio_partial} partial, ${a.audio_on_demand} on demand, ${a.audio_unknown} unknown (${a.audio_files_present}/${a.audio_files_expected} expected files present)`)
  }
}
