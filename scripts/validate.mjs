import fs from 'node:fs'
import path from 'node:path'

const root = path.resolve(import.meta.dirname, '..')
const legacyWords = new Set(['break', 'call', 'case', 'change', 'charge', 'come', 'cut', 'draw', 'drive', 'fall', 'get', 'go', 'hold', 'keep', 'leave', 'light', 'line', 'make', 'matter', 'move', 'order', 'pass', 'play', 'point', 'put', 'right', 'run', 'set', 'take', 'turn'])
const preGeneratedWords = new Set([...legacyWords, 'ability', 'accept', 'access', 'achieve', 'active', 'activity', 'advantage', 'affect', 'afford', 'agree'])
const errors = []
const seenExamples = new Map()
const requireAudio = !process.argv.includes('--content-only')
const catalog = JSON.parse(fs.readFileSync(path.join(root, 'content', 'catalog.json'), 'utf8'))
const records = catalog.entries
if (!Array.isArray(records)) throw new Error('Catalog entries must be an array')
if (records.length < 100) errors.push('Pilot catalog must contain at least 100 headwords')
const seenWords = new Set()
for (const item of records) {
  if (!item || typeof item.word !== 'string' || !/^[a-z][a-z'-]*$/.test(item.word)) { errors.push('Catalog has invalid headword'); continue }
  if (seenWords.has(item.word)) errors.push(`Catalog duplicate: ${item.word}`)
  seenWords.add(item.word)
  if (!['basic', 'draft', 'reviewed', 'published'].includes(item.status)) errors.push(`${item.word}: invalid editorial status`)
  if (typeof item.basic_zh !== 'string' || !item.basic_zh.trim()) errors.push(`${item.word}: missing basic_zh`)
  if (!Array.isArray(item.exam_categories) || !item.exam_categories.length) errors.push(`${item.word}: missing exam category`)
  if (!Array.isArray(item.review_records)) errors.push(`${item.word}: missing review history`)
  if (item.status === 'published' && !(item.content_version > 0)) errors.push(`${item.word}: missing published version`)
}
const words = records.filter((item) => item.status === 'published').map((item) => item.word).sort()
for (const word of legacyWords) if (!words.includes(word)) errors.push(`${word}: legacy entry is not published`)
const keys = (object, expected, where) => {
  if (!object || typeof object !== 'object' || Array.isArray(object)) return errors.push(`${where}: expected object`)
  const actual = Object.keys(object).sort().join(',')
  if (actual !== [...expected].sort().join(',')) errors.push(`${where}: incorrect keys: ${actual}`)
}
const string = (value, where, allowEmpty = false) => {
  if (typeof value !== 'string' || (!allowEmpty && !value.trim())) errors.push(`${where}: expected ${allowEmpty ? 'string' : 'nonempty string'}`)
}
const array = (value, where, min = 0) => {
  if (!Array.isArray(value) || value.length < min) { errors.push(`${where}: expected array with at least ${min} items`); return [] }
  return value
}
const audio = (word, name) => {
  if (!requireAudio || !preGeneratedWords.has(word)) return
  const file = path.join(root, 'public', 'audio', word, `${name}.mp3`)
  if (!fs.existsSync(file) || fs.statSync(file).size < 1000) errors.push(`${word}: missing or empty audio ${name}.mp3`)
}

const files = fs.readdirSync(path.join(root, 'content', 'words')).filter((file) => file.endsWith('.json')).sort()
if (files.join(',') !== words.map((word) => `${word}.json`).sort().join(',')) errors.push('Published JSON files do not match catalog')
for (const word of words) {
  const file = path.join(root, 'content', 'words', `${word}.json`)
  if (!fs.existsSync(file)) continue
  let entry
  try { entry = JSON.parse(fs.readFileSync(file, 'utf8')) } catch (error) { errors.push(`${word}: invalid JSON: ${error}`); continue }
  keys(entry, ['word', 'phonetic', 'syllables', 'pos', 'core_meanings', 'etymology', 'semantic_shift', 'senses'], word)
  if (entry.word !== word) errors.push(`${word}: word field mismatch`)
  string(entry.phonetic, `${word}.phonetic`)
  if (typeof entry.phonetic === 'string' && !/^\/.+\/$/.test(entry.phonetic)) errors.push(`${word}: phonetic must be between slashes`)
  for (const item of array(entry.syllables, `${word}.syllables`, 1)) string(item, `${word}.syllables item`)
  if (Array.isArray(entry.syllables) && entry.syllables.join('').toLowerCase() !== word) errors.push(`${word}: syllables must reconstruct the headword`)
  for (const item of array(entry.pos, `${word}.pos`, 1)) string(item, `${word}.pos item`)
  for (const item of array(entry.core_meanings, `${word}.core_meanings`, 1)) string(item, `${word}.core_meanings item`)
  string(entry.etymology, `${word}.etymology`)
  string(entry.semantic_shift, `${word}.semantic_shift`)
  const senses = array(entry.senses, `${word}.senses`, 1)
  if (legacyWords.has(word) && !senses.some((sense) => Array.isArray(sense.antonyms) && sense.antonyms.length)) errors.push(`${word}: no antonym comparison in any sense`)
  for (const [senseIndex, sense] of senses.entries()) {
    const where = `${word}.senses[${senseIndex}]`
    keys(sense, ['id', 'part_of_speech', 'en_definition', 'zh_definition', 'usages', 'synonyms', 'antonyms', 'confusables'], where)
    if (sense.id !== senseIndex + 1) errors.push(`${where}: IDs must start at 1 and follow array order`)
    string(sense.part_of_speech, `${where}.part_of_speech`)
    string(sense.en_definition, `${where}.en_definition`)
    string(sense.zh_definition, `${where}.zh_definition`)
    if (!entry.pos?.includes(sense.part_of_speech)) errors.push(`${where}: part of speech missing from word header`)
    for (const field of ['synonyms', 'antonyms', 'confusables']) {
      for (const item of array(sense[field], `${where}.${field}`, field === 'antonyms' ? 0 : 1)) {
        string(item, `${where}.${field} item`)
        if (typeof item === 'string' && ((field !== 'confusables' && !item.includes('：')) || item.trim().length < 8)) errors.push(`${where}.${field}: add a useful explanation`)
      }
    }
    for (const [usageIndex, usage] of array(sense.usages, `${where}.usages`, 1).entries()) {
      const usageWhere = `${where}.usages[${usageIndex}]`
      keys(usage, ['usage_label', 'collocations', 'examples'], usageWhere)
      string(usage.usage_label, `${usageWhere}.usage_label`)
      for (const [index, collocation] of array(usage.collocations, `${usageWhere}.collocations`, 2).entries()) {
        keys(collocation, ['phrase', 'translation'], `${usageWhere}.collocations[${index}]`)
        string(collocation.phrase, `${usageWhere}.collocations[${index}].phrase`)
        string(collocation.translation, `${usageWhere}.collocations[${index}].translation`)
      }
      for (const [index, example] of array(usage.examples, `${usageWhere}.examples`, 2).entries()) {
        const exampleWhere = `${usageWhere}.examples[${index}]`
        keys(example, ['en', 'zh'], exampleWhere)
        string(example.en, `${exampleWhere}.en`)
        string(example.zh, `${exampleWhere}.zh`)
        if (typeof example.en === 'string') {
          const count = example.en.trim().split(/\s+/).length
          if (count > 16) errors.push(`${exampleWhere}: example has ${count} words (maximum 16)`)
          const normalized = example.en.toLowerCase().replace(/[^a-z ]/g, '').trim()
          if (seenExamples.has(normalized)) errors.push(`${exampleWhere}: duplicate of ${seenExamples.get(normalized)}`)
          else seenExamples.set(normalized, exampleWhere)
        }
        audio(word, `s${sense.id}-u${usageIndex + 1}-e${index + 1}`)
      }
    }
  }
  audio(word, 'word')
}

if (errors.length) {
  console.error(`Validation failed (${errors.length} problems):\n${errors.join('\n')}`)
  process.exitCode = 1
} else console.log(`Validated ${records.length} catalog words, ${words.length} published entries, ${seenExamples.size} distinct examples${requireAudio ? ', and all required pre-generated audio files' : ''}.`)
