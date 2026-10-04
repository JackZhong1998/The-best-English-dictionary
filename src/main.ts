import './style.css'

type Pair = { phrase: string; translation: string }
type Example = { en: string; zh: string }
type Usage = { usage_label: string; collocations: Pair[]; examples: Example[] }
type Sense = {
  id: number; part_of_speech: string; en_definition: string; zh_definition: string
  usages: Usage[]; synonyms: string[]; antonyms: string[]; confusables: string[]
}
type Entry = {
  word: string; phonetic: string; syllables: string[]; pos: string[]
  core_meanings: string[]; etymology: string; semantic_shift: string; senses: Sense[]
}
type WordSummary = { word: string; basic_zh: string; exam_levels: string[]; status: 'basic' | 'published' }
type SearchResult = { items: WordSummary[]; total: number; limit: number; offset: number; has_more: boolean }
type EntryResult = WordSummary & { version: number; reviewed_at: string | null; entry: Entry | null }
type AudioLocator = { word: string; senseId?: number; usageId?: number; exampleId?: number }

const app = document.querySelector<HTMLDivElement>('#app')!
const base = import.meta.env.BASE_URL
const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')
const preGeneratedWords = new Set(['ability', 'accept', 'access', 'achieve', 'active', 'activity', 'advantage', 'affect', 'afford', 'agree', 'break', 'call', 'case', 'change', 'charge', 'come', 'cut', 'draw', 'drive', 'fall', 'get', 'go', 'hold', 'keep', 'leave', 'light', 'line', 'make', 'matter', 'move', 'order', 'pass', 'play', 'point', 'put', 'right', 'run', 'set', 'take', 'turn'])
let currentAudio: HTMLAudioElement | null = null
let searchSequence = 0
let currentQuery = ''
let currentLetter = ''
let currentOffset = 0
let currentItems: WordSummary[] = []
const pageSize = 25

const esc = (value: string) => value.replace(/[&<>"']/g, (character) => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character]!)
const normalize = (value: string) => value.trim().toLowerCase()
const wordHref = (word: string) => base === '/' ? `/word/${encodeURIComponent(word)}` : `${base}?word=${encodeURIComponent(word)}`
const staticAudioPath = (word: string, name: string) => `${base}audio/${word}/${name}.mp3`
const getWordFromUrl = () => {
  const pathMatch = location.pathname.match(/\/word\/([^/]+)\/?$/i)
  let raw = new URLSearchParams(location.search).get('word') || ''
  if (pathMatch?.[1]) {
    try { raw = decodeURIComponent(pathMatch[1]) } catch { return '' }
  }
  const word = normalize(raw)
  return /^[a-z][a-z'-]{0,63}$/.test(word) ? word : ''
}

function shell(content: string): string {
  return `<div class="site-shell"><header class="site-header">
    <a class="brand" href="${base}" aria-label="词义之间，返回首页"><span class="brand-mark" aria-hidden="true">a<span>·</span>z</span><span class="brand-text"><strong>词义之间</strong><small>学懂一个词的每一种常见意思</small></span></a>
    <a class="header-link" href="${base}">词库 <span aria-hidden="true">↗</span></a>
  </header><main>${content}</main><footer class="site-footer"><span>词义之间</span><span>为中文学习者写的英汉多义词典 · 按考试词表逐批更新</span></footer></div>`
}

async function fallbackCatalog(): Promise<WordSummary[]> {
  const response = await fetch(`${base}data/catalog.json`)
  if (!response.ok) throw new Error('词库暂时无法加载')
  const catalog = await response.json() as { entries: Array<{ word: string; basic_zh: string; exam_categories?: string[]; status: string }> }
  return catalog.entries.filter((item) => item.status === 'basic' || item.status === 'published')
    .map((item) => ({ word: item.word, basic_zh: item.basic_zh, exam_levels: item.exam_categories || [], status: item.status as WordSummary['status'] }))
}

async function searchWords(query: string, letter: string, offset: number): Promise<SearchResult> {
  const params = new URLSearchParams({ query, letter, limit: String(pageSize), offset: String(offset) })
  try {
    const response = await fetch(`/api/words?${params}`)
    if (!response.ok) throw new Error('API unavailable')
    return await response.json() as SearchResult
  } catch {
    const all = await fallbackCatalog()
    const filtered = all.filter((item) => item.word.startsWith(normalize(query)) && (!letter || item.word[0]?.toUpperCase() === letter)).sort((a, b) => a.word.localeCompare(b.word))
    return { items: filtered.slice(offset, offset + pageSize), total: filtered.length, limit: pageSize, offset, has_more: offset + pageSize < filtered.length }
  }
}

async function fetchEntry(word: string): Promise<EntryResult | null> {
  try {
    const response = await fetch(`/api/entries/${encodeURIComponent(word)}`)
    if (response.status === 404) return null
    if (!response.ok) throw new Error('API unavailable')
    return await response.json() as EntryResult
  } catch {
    const item = (await fallbackCatalog()).find((candidate) => candidate.word === word)
    if (!item) return null
    let entry: Entry | null = null
    if (item.status === 'published') {
      const response = await fetch(`${base}data/words/${encodeURIComponent(word)}.json`)
      if (response.ok) entry = await response.json() as Entry
    }
    return { ...item, version: 1, reviewed_at: null, entry }
  }
}

function renderHome(): void {
  app.innerHTML = shell(`<section class="hero"><div class="hero-copy"><p class="eyebrow">EXPLORE THE DICTIONARY <span class="eyebrow-line"></span> 英汉双解</p>
    <h1>一个单词，<br /><em>不止一种意思。</em></h1><p class="hero-desc">先查基础词义，再阅读精修的义项、例句和辨析。词库按四级、六级、考研逐批扩充。</p></div>
    <div class="hero-card" aria-hidden="true"><span class="hero-card-num">FROM WORD TO MEANING</span><span class="hero-card-word">run</span><span class="hero-card-phonetic">/rʌn/</span><div class="hero-card-rule"></div><span>跑 · 运行 · 经营 · 流动</span><span class="hero-card-bottom">一个词 · 多种生活场景 <span>↗</span></span></div></section>
    <section class="browse" aria-labelledby="browse-title"><div class="section-heading"><div><p class="eyebrow">A–Z / 词库</p><h2 id="browse-title">从一个词开始</h2></div><span class="entry-count" id="entry-count">载入中</span></div>
    <label class="search-box"><span class="search-icon" aria-hidden="true">⌕</span><span class="sr-only">搜索英文单词</span><input id="word-search" type="search" placeholder="搜索英文单词，例如 take" autocomplete="off" spellcheck="false" /><span class="search-hint">EN</span></label>
    <div class="alphabet" role="group" aria-label="按首字母浏览"><button type="button" data-letter="" class="active">全部</button>${letters.map((letter) => `<button type="button" data-letter="${letter}">${letter}</button>`).join('')}</div>
    <div id="word-list" aria-live="polite"></div><button class="load-more" id="load-more" type="button" hidden>加载更多单词</button></section>`)
  const input = document.querySelector<HTMLInputElement>('#word-search')!
  let timer: number | undefined
  input.addEventListener('input', () => { window.clearTimeout(timer); timer = window.setTimeout(() => { currentQuery = input.value; void loadWords(true) }, 180) })
  document.querySelectorAll<HTMLButtonElement>('[data-letter]').forEach((button) => button.addEventListener('click', () => {
    currentLetter = button.dataset.letter || ''
    document.querySelectorAll('[data-letter]').forEach((item) => item.classList.toggle('active', item === button))
    void loadWords(true)
  }))
  document.querySelector<HTMLButtonElement>('#load-more')!.addEventListener('click', () => void loadWords(false))
  void loadWords(true)
}

async function loadWords(reset: boolean): Promise<void> {
  const sequence = ++searchSequence
  if (reset) { currentOffset = 0; currentItems = []; document.querySelector('#word-list')!.innerHTML = '<div class="empty-state">正在查找单词…</div>' }
  try {
    const result = await searchWords(currentQuery, currentLetter, currentOffset)
    if (sequence !== searchSequence) return
    currentItems = [...currentItems, ...result.items]
    currentOffset += result.items.length
    document.querySelector('#entry-count')!.textContent = `找到 ${result.total} 个词`
    document.querySelector('#word-list')!.innerHTML = renderGroups(currentItems)
    document.querySelector<HTMLButtonElement>('#load-more')!.hidden = !result.has_more
  } catch {
    if (sequence === searchSequence) document.querySelector('#word-list')!.innerHTML = '<div class="empty-state">词库暂时无法加载，请稍后重试。</div>'
  }
}

function renderGroups(items: WordSummary[]): string {
  if (!items.length) return '<div class="empty-state"><strong>暂时没有找到这个词</strong><p>可以换一个英文词试试。</p></div>'
  const groups = letters.map((letter) => ({ letter, words: items.filter((item) => item.word[0]?.toUpperCase() === letter) })).filter((group) => group.words.length)
  return groups.map(({ letter, words }) => `<section class="letter-group" aria-label="${letter} 开头的词"><div class="letter-title"><span>${letter}</span><i></i><small>${words.length} WORD${words.length > 1 ? 'S' : ''}</small></div><div class="word-grid">${words.map((item) => `<a class="word-card" href="${wordHref(item.word)}"><span class="word-card-top"><strong>${esc(item.word)}</strong><span class="card-arrow" aria-hidden="true">↗</span></span><span class="word-card-phonetic">${esc(item.exam_levels.join(' · ') || '英语词汇')}</span><span class="word-card-meanings">${esc(item.basic_zh)}</span><span class="word-card-bottom">${item.status === 'published' ? '查看完整词条' : '基础释义 · 精修中'} <span aria-hidden="true">→</span></span></a>`).join('')}</div></section>`).join('')
}

function playButton(locator: AudioLocator, label: string, extraClass = ''): string {
  const attrs = [`data-word="${esc(locator.word)}"`]
  for (const field of ['senseId', 'usageId', 'exampleId'] as const) if (locator[field] !== undefined) attrs.push(`data-${field.toLowerCase()}="${locator[field]}"`)
  return `<button class="audio-button ${extraClass}" type="button" ${attrs.join(' ')} aria-label="${esc(label)}" title="${esc(label)}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4Zm12-1.5a6 6 0 0 1 0 9m2.5-12a10 10 0 0 1 0 15"/></svg></button>`
}

function metaList(title: string, values: string[]): string {
  return `<div><span>${title}</span><p>${values.length ? esc(values.join('、')) : '这个意思没有直接对应的反义词。'}</p></div>`
}

function learningNotes(entry: Entry): string {
  const split = entry.syllables.length > 1 ? entry.syllables.join(' · ') : `${entry.word}（单音节）`
  return `<section class="learning-notes" aria-label="词形与词义线索"><div><h2>音节拆分</h2><p class="syllable-split" lang="en">${esc(split)}</p><small>按美式发音分节；单音节词保留完整拼写。</small></div>
    <div><h2>词源</h2><p>${esc(entry.etymology || '暂无可靠资料。')}</p></div><div><h2>词义迁移</h2><p>${esc(entry.semantic_shift || '暂无可靠说明。')}</p></div></section>`
}

function renderBasic(result: EntryResult): void {
  app.innerHTML = shell(`<div class="entry-layout"><nav class="breadcrumb" aria-label="面包屑"><a href="${base}">词库</a><span>/</span><span>${esc(result.word)}</span></nav>
    <section class="entry-hero"><div><p class="eyebrow">${esc(result.exam_levels.join(' · ') || '英语词汇')}</p><h1>${esc(result.word)}</h1><p class="entry-pos">基础释义 · 精修中</p></div><div class="entry-hero-side"><span class="entry-hero-side-label">BASIC MEANING / 基础释义</span><div class="meaning-chips"><span>${esc(result.basic_zh)}</span></div></div></section>
    <div class="entry-columns"><div class="entry-main"><div class="reading-note"><span aria-hidden="true">✳</span><p>这个词已经收入词库。多义项、例句和辨析正在分批制作，完成复核后会在这里显示。</p></div><a class="header-link" href="${base}">← 返回词库</a></div></div></div>`)
}

function renderEntry(result: EntryResult): void {
  const entry = result.entry!
  app.innerHTML = shell(`<div class="entry-layout"><nav class="breadcrumb" aria-label="面包屑"><a href="${base}">词库</a><span>/</span><span>${esc(entry.word)}</span></nav>
    <section class="entry-hero"><div><p class="eyebrow">${esc(result.exam_levels.join(' · ') || '精修词条')}</p><h1>${esc(entry.word)}</h1><div class="pronunciation"><span>${esc(entry.phonetic)}</span>${playButton({ word: entry.word }, `播放 ${entry.word} 的美式发音`, 'word-audio')}<span class="pronunciation-label">美音</span></div><p class="entry-pos">${esc(entry.pos.join(' · '))}</p></div><div class="entry-hero-side"><span class="entry-hero-side-label">CORE MEANINGS / 核心词义</span><div class="meaning-chips">${entry.core_meanings.map((meaning) => `<span>${esc(meaning)}</span>`).join('')}</div></div></section>
    <div class="entry-columns"><aside class="entry-sidebar"><div class="toc"><p class="eyebrow">ON THIS PAGE</p><h2>义项目录 <span>${entry.senses.length}</span></h2><ol>${entry.senses.map((sense) => `<li><button type="button" data-jump="sense-${sense.id}"><span>${String(sense.id).padStart(2, '0')}</span>${esc(sense.usages[0]?.usage_label || sense.zh_definition)}</button></li>`).join('')}</ol></div></aside>
    <div class="entry-main"><div class="reading-note"><span aria-hidden="true">✳</span><p>从最常见的意思读起。点击目录或义项标题，逐个展开学习。</p></div>${learningNotes(entry)}
    <div class="senses">${entry.senses.map((sense, senseIndex) => `<details class="sense" id="sense-${sense.id}" ${senseIndex === 0 ? 'open' : ''}><summary><span class="sense-number">${String(sense.id).padStart(2, '0')}</span><span class="sense-summary"><small>${esc(sense.part_of_speech)} · MEANING</small><strong>${esc(sense.usages[0]?.usage_label || sense.zh_definition)}</strong><span>${esc(sense.en_definition)}</span></span><span class="expand-icon" aria-hidden="true">+</span></summary><div class="sense-body"><div class="definition"><span>英文释义 / DEFINITION</span><p class="en-definition">${esc(sense.en_definition)}</p><p class="zh-definition">${esc(sense.zh_definition)}</p></div>${sense.usages.map((usage, usageIndex) => `<section class="usage"><h3>${esc(usage.usage_label)}</h3><div class="usage-label">常见搭配 / COLLOCATIONS</div><div class="collocations">${usage.collocations.map((item) => `<div><strong>${esc(item.phrase)}</strong><span>${esc(item.translation)}</span></div>`).join('')}</div><div class="usage-label example-label">简单例句 / EXAMPLES</div><div class="examples">${usage.examples.map((example, exampleIndex) => `<div class="example"><div class="example-main">${playButton({ word: entry.word, senseId: sense.id, usageId: usageIndex + 1, exampleId: exampleIndex + 1 }, `播放例句 ${example.en}`)}<div><p lang="en">${esc(example.en)}</p><span>${esc(example.zh)}</span></div></div><span class="example-index">${String(exampleIndex + 1).padStart(2, '0')}</span></div>`).join('')}</div></section>`).join('')}<div class="related-words"><h3>近义词 / 反义词 / 易混淆词辨析</h3>${metaList('近义词', sense.synonyms)}${metaList('反义词', sense.antonyms)}${metaList('易混淆词', sense.confusables)}</div></div></details>`).join('')}</div><nav class="entry-pagination" aria-label="词库导航"><a href="${base}"><span>← 返回词库</span><strong>继续查词</strong></a></nav></div></div></div>`)
  document.querySelectorAll<HTMLButtonElement>('[data-jump]').forEach((button) => button.addEventListener('click', () => {
    const details = document.getElementById(button.dataset.jump!) as HTMLDetailsElement
    details.open = true
    details.scrollIntoView({ behavior: 'smooth', block: 'start' })
    history.replaceState(null, '', `${wordHref(entry.word)}#${details.id}`)
  }))
  document.querySelectorAll<HTMLButtonElement>('[data-word]').forEach((button) => button.addEventListener('click', () => void playAudio(button)))
  if (location.hash.startsWith('#sense-')) {
    const details = document.getElementById(location.hash.slice(1)) as HTMLDetailsElement | null
    if (details) { details.open = true; requestAnimationFrame(() => details.scrollIntoView()) }
  }
}

async function resolveAudio(button: HTMLButtonElement): Promise<string> {
  const word = button.dataset.word!
  const senseId = button.dataset.senseid
  const usageId = button.dataset.usageid
  const exampleId = button.dataset.exampleid
  if (preGeneratedWords.has(word)) return staticAudioPath(word, senseId ? `s${senseId}-u${usageId}-e${exampleId}` : 'word')
  const params = new URLSearchParams({ word })
  if (senseId) { params.set('senseId', senseId); params.set('usageId', usageId!); params.set('exampleId', exampleId!) }
  for (let attempt = 0; attempt < 12; attempt++) {
    const response = await fetch(`/api/audio?${params}`)
    const result = await response.json() as { status?: string; url?: string; retryAfter?: number; error?: string }
    if (response.ok && result.status === 'ready' && result.url) return result.url
    if (response.status === 202) {
      if (attempt === 0) announce('正在生成美式发音，请稍候…')
      await new Promise((resolve) => window.setTimeout(resolve, Math.min(result.retryAfter || 2, 5) * 1000))
      continue
    }
    if (response.status === 429) throw new Error('今日新发音额度已用完，已有音频仍可播放')
    throw new Error(result.error === 'unavailable' ? '发音暂时不可用，请稍后再试' : '发音暂时无法生成')
  }
  throw new Error('发音仍在生成，请稍后再试')
}

async function playAudio(button: HTMLButtonElement): Promise<void> {
  if (currentAudio) { currentAudio.pause(); currentAudio = null }
  document.querySelectorAll('.audio-button').forEach((item) => item.classList.remove('playing'))
  button.classList.add('playing')
  button.setAttribute('aria-busy', 'true')
  const originalTitle = button.title
  button.title = '正在准备发音…'
  if (!preGeneratedWords.has(button.dataset.word!)) announce('正在准备美式发音…')
  try {
    const url = await resolveAudio(button)
    const player = new Audio(url)
    currentAudio = player
    player.addEventListener('ended', () => button.classList.remove('playing'), { once: true })
    player.addEventListener('error', () => button.classList.remove('playing'), { once: true })
    await player.play()
    button.title = originalTitle
  } catch (error) {
    button.classList.remove('playing')
    button.title = error instanceof Error ? error.message : '发音暂时无法播放'
    announce(button.title)
  } finally {
    button.removeAttribute('aria-busy')
  }
}

function announce(message: string): void {
  let node = document.querySelector<HTMLDivElement>('#audio-status')
  if (!node) { node = document.createElement('div'); node.id = 'audio-status'; node.setAttribute('role', 'status'); node.className = 'audio-status'; document.body.append(node) }
  node.textContent = message
  window.setTimeout(() => { if (node?.textContent === message) node.textContent = '' }, 5000)
}

async function init(): Promise<void> {
  const word = getWordFromUrl()
  if (!word) { renderHome(); return }
  app.innerHTML = shell('<div class="entry-layout"><p class="loading-entry">正在加载词条…</p></div>')
  try {
    const result = await fetchEntry(word)
    if (!result) { app.innerHTML = shell(`<div class="entry-layout"><div class="empty-state"><strong>暂时没有收录 ${esc(word)}</strong><p>词库仍在逐批扩充。</p><a href="${base}">返回词库</a></div></div>`); return }
    document.title = `${result.word} · 词义之间`
    if (result.status === 'published' && result.entry) renderEntry(result)
    else renderBasic(result)
  } catch {
    app.innerHTML = shell('<div class="entry-layout"><div class="empty-state">词条暂时无法加载，请稍后重试。</div></div>')
  }
}

void init()
