import fs from 'node:fs'
import path from 'node:path'

const root = path.resolve(import.meta.dirname, '..')
const source = path.join(root, 'content', 'words')
const target = path.join(root, 'public', 'data')
fs.mkdirSync(path.join(target, 'words'), { recursive: true })

const catalogFile = path.join(root, 'content', 'catalog.json')
const fallbackEntries = fs.readdirSync(source).filter((name) => name.endsWith('.json')).map((name) => {
  const entry = JSON.parse(fs.readFileSync(path.join(source, name), 'utf8'))
  return { word: entry.word, exam_categories: [], status: 'published', basic_zh: entry.core_meanings.join('、') }
})
const catalog = fs.existsSync(catalogFile)
  ? JSON.parse(fs.readFileSync(catalogFile, 'utf8'))
  : { version: 1, entries: fallbackEntries }

const publicEntries = catalog.entries
  .filter((item) => ['basic', 'draft', 'review', 'published'].includes(item.status))
  .map((item) => ({ ...item, status: item.status === 'published' ? 'published' : 'basic' }))
fs.writeFileSync(path.join(target, 'catalog.json'), JSON.stringify({ version: catalog.version, entries: publicEntries }))
for (const item of publicEntries) {
  if (item.status !== 'published') continue
  const filename = `${item.word}.json`
  fs.copyFileSync(path.join(source, filename), path.join(target, 'words', filename))
}
console.log(`Exported ${publicEntries.length} public catalog records`)
