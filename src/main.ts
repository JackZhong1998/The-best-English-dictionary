import './style.css'

type Pair = { phrase: string; translation: string }
type Example = { en: string; zh: string }
type Usage = { usage_label: string; collocations: Pair[]; examples: Example[] }
type Sense = {
  id: number
  part_of_speech: string
  en_definition: string
  zh_definition: string
  usages: Usage[]
  synonyms: string[]
  antonyms: string[]
  confusables: string[]
}
type Entry = {
  word: string
  phonetic: string
  syllables: string[]
  pos: string[]
  core_meanings: string[]
  etymology: string
  semantic_shift: string
  senses: Sense[]
}

const modules = import.meta.glob('../content/words/*.json', { eager: true, import: 'default' }) as Record<string, Entry>
const entries = Object.values(modules).sort((a, b) => a.word.localeCompare(b.word))
const byWord = new Map(entries.map((entry) => [entry.word, entry]))
const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')
const app = document.querySelector<HTMLDivElement>('#app')!
const base = import.meta.env.BASE_URL
let currentAudio: HTMLAudioElement | null = null

const esc = (value: string) => value.replace(/[&<>"']/g, (character) => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character]!)
const wordHref = (word: string) => `${base}?word=${encodeURIComponent(word)}`
const audioPath = (word: string, name: string) => `${base}audio/${word}/${name}.mp3`
const strip = (value: string) => value.trim().toLowerCase()

function shell(content: string): string {
  return `
    <div class="site-shell">
      <header class="site-header">
        <a class="brand" href="${base}" aria-label="词义之间，返回首页">
          <span class="brand-mark" aria-hidden="true">a<span>·</span>z</span>
          <span class="brand-text"><strong>词义之间</strong><small>学懂一个词的每一种常见意思</small></span>
        </a>
        <a class="header-link" href="${base}">词库 <span aria-hidden="true">↗</span></a>
      </header>
      <main>${content}</main>
      <footer class="site-footer"><span>词义之间</span><span>为中文学习者写的英汉多义词典 · 首批 ${entries.length} 词</span></footer>
    </div>`
}

function renderHome(query = '', activeLetter = ''): void {
  const normalized = strip(query)
  const found = entries.filter((entry) => entry.word.includes(normalized) && (!activeLetter || entry.word[0].toUpperCase() === activeLetter))
  const groups = letters.map((letter) => ({ letter, words: found.filter((entry) => entry.word[0].toUpperCase() === letter) })).filter((group) => group.words.length)
  app.innerHTML = shell(`
    <section class="hero">
      <div class="hero-copy"><p class="eyebrow">A BETTER WAY TO LEARN WORDS <span class="eyebrow-line"></span> 英汉双解</p>
        <h1>一个单词，<br /><em>不止一种意思。</em></h1>
        <p class="hero-desc">把常见义项分开，配上简单的英文释义、贴近日常的例句与搭配。慢慢读，真正学懂。</p>
      </div>
      <div class="hero-card" aria-hidden="true"><span class="hero-card-num">01 / 30</span><span class="hero-card-word">run</span><span class="hero-card-phonetic">/rʌn/</span><div class="hero-card-rule"></div><span>跑 · 运行 · 经营 · 流动</span><span class="hero-card-bottom">一个词 · 多种生活场景 <span>↗</span></span></div>
    </section>
    <section class="browse" aria-labelledby="browse-title">
      <div class="section-heading"><div><p class="eyebrow">EXPLORE THE DICTIONARY</p><h2 id="browse-title">从一个词开始</h2></div><span class="entry-count">收录 ${entries.length} 个多义词</span></div>
      <label class="search-box"><span class="search-icon" aria-hidden="true">⌕</span><span class="sr-only">搜索英文单词</span><input id="word-search" type="search" placeholder="搜索英文单词，例如 take" value="${esc(query)}" autocomplete="off" spellcheck="false" /><span class="search-hint">EN</span></label>
      <div class="alphabet" role="group" aria-label="按首字母浏览">
        <button type="button" data-letter="" class="${activeLetter ? '' : 'active'}">全部</button>
        ${letters.map((letter) => `<button type="button" data-letter="${letter}" class="${activeLetter === letter ? 'active' : ''}" ${entries.some((entry) => entry.word[0].toUpperCase() === letter) ? '' : 'disabled'}>${letter}</button>`).join('')}
      </div>
      <div id="word-list" aria-live="polite">${renderGroups(groups, query)}</div>
    </section>`)

  const search = document.querySelector<HTMLInputElement>('#word-search')!
  search.addEventListener('input', () => updateHome(search.value, activeLetter))
  document.querySelectorAll<HTMLButtonElement>('[data-letter]').forEach((button) => button.addEventListener('click', () => {
    activeLetter = button.dataset.letter || ''
    document.querySelectorAll('[data-letter]').forEach((item) => item.classList.toggle('active', item === button))
    updateHome(search.value, activeLetter)
  }))
}

function renderGroups(groups: { letter: string; words: Entry[] }[], query: string): string {
  if (!groups.length) return `<div class="empty-state"><strong>暂时没有找到这个词</strong><p>目前收录 30 个高频多义词，可以换个英文单词试试。</p></div>`
  return groups.map(({ letter, words }) => `<section class="letter-group" aria-label="${letter} 开头的词"><div class="letter-title"><span>${letter}</span><i></i><small>${words.length} WORD${words.length > 1 ? 'S' : ''}</small></div><div class="word-grid">${words.map((entry) => `<a class="word-card" href="${wordHref(entry.word)}"><span class="word-card-top"><strong>${esc(entry.word)}</strong><span class="card-arrow" aria-hidden="true">↗</span></span><span class="word-card-phonetic">${esc(entry.phonetic)} <span class="word-card-pos">${esc(entry.pos.join(' / '))}</span></span><span class="word-card-meanings">${esc(entry.core_meanings.slice(0, 4).join(' · '))}</span><span class="word-card-bottom">${entry.senses.length} 个常见义项 <span aria-hidden="true">→</span></span></a>`).join('')}</div></section>`).join('')
}

function updateHome(query: string, activeLetter: string): void {
  const normalized = strip(query)
  const found = entries.filter((entry) => entry.word.includes(normalized) && (!activeLetter || entry.word[0].toUpperCase() === activeLetter))
  const groups = letters.map((letter) => ({ letter, words: found.filter((entry) => entry.word[0].toUpperCase() === letter) })).filter((group) => group.words.length)
  document.querySelector('#word-list')!.innerHTML = renderGroups(groups, query)
}

function playButton(path: string, label: string, extraClass = ''): string {
  return `<button class="audio-button ${extraClass}" type="button" data-audio="${esc(path)}" aria-label="${esc(label)}" title="${esc(label)}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4Zm12-1.5a6 6 0 0 1 0 9m2.5-12a10 10 0 0 1 0 15"/></svg></button>`
}

function metaList(title: string, values: string[]): string {
  return `<div><span>${title}</span><p>${values.length ? esc(values.join('、')) : '—'}</p></div>`
}

function renderEntry(entry: Entry): void {
  const currentIndex = entries.findIndex((item) => item.word === entry.word)
  const previous = entries[currentIndex - 1]
  const next = entries[currentIndex + 1]
  app.innerHTML = shell(`
    <div class="entry-layout"><nav class="breadcrumb" aria-label="面包屑"><a href="${base}">词库</a><span>/</span><span>${esc(entry.word)}</span></nav>
      <section class="entry-hero"><div><p class="eyebrow">WORD ${String(currentIndex + 1).padStart(2, '0')} / ${entries.length}</p><h1>${esc(entry.word)}</h1><div class="pronunciation"><span>${esc(entry.phonetic)}</span>${playButton(audioPath(entry.word, 'word'), `播放 ${entry.word} 的美式发音`, 'word-audio')}<span class="pronunciation-label">美音</span></div><p class="entry-pos">${esc(entry.pos.join(' · '))}</p></div><div class="entry-hero-side"><span class="entry-hero-side-label">CORE MEANINGS / 核心词义</span><div class="meaning-chips">${entry.core_meanings.map((meaning) => `<span>${esc(meaning)}</span>`).join('')}</div></div></section>
      <div class="entry-columns"><aside class="entry-sidebar"><div class="toc"><p class="eyebrow">ON THIS PAGE</p><h2>义项目录 <span>${entry.senses.length}</span></h2><ol>${entry.senses.map((sense) => `<li><button type="button" data-jump="sense-${sense.id}"><span>${String(sense.id).padStart(2, '0')}</span>${esc(sense.usages[0]?.usage_label || sense.zh_definition)}</button></li>`).join('')}</ol></div></aside>
      <div class="entry-main"><div class="reading-note"><span aria-hidden="true">✳</span><p>从最常见的意思读起。点击目录或义项标题，逐个展开学习。</p></div>${entry.semantic_shift ? `<div class="semantic-note"><strong>词义怎样延伸？</strong><p>${esc(entry.semantic_shift)}</p></div>` : ''}
      <div class="senses">${entry.senses.map((sense, senseIndex) => `<details class="sense" id="sense-${sense.id}" ${senseIndex === 0 ? 'open' : ''}><summary><span class="sense-number">${String(sense.id).padStart(2, '0')}</span><span class="sense-summary"><small>${esc(sense.part_of_speech)} · MEANING</small><strong>${esc(sense.usages[0]?.usage_label || sense.zh_definition)}</strong><span>${esc(sense.en_definition)}</span></span><span class="expand-icon" aria-hidden="true">+</span></summary><div class="sense-body"><div class="definition"><span>英文释义 / DEFINITION</span><p class="en-definition">${esc(sense.en_definition)}</p><p class="zh-definition">${esc(sense.zh_definition)}</p></div>${sense.usages.map((usage, usageIndex) => `<section class="usage"><h3>${esc(usage.usage_label)}</h3><div class="usage-label">常见搭配 / COLLOCATIONS</div><div class="collocations">${usage.collocations.map((item) => `<div><strong>${esc(item.phrase)}</strong><span>${esc(item.translation)}</span></div>`).join('')}</div><div class="usage-label example-label">简单例句 / EXAMPLES</div><div class="examples">${usage.examples.map((example, exampleIndex) => `<div class="example"><div class="example-main">${playButton(audioPath(entry.word, `s${sense.id}-u${usageIndex + 1}-e${exampleIndex + 1}`), `播放例句 ${example.en}`)}<div><p lang="en">${esc(example.en)}</p><span>${esc(example.zh)}</span></div></div><span class="example-index">${String(exampleIndex + 1).padStart(2, '0')}</span></div>`).join('')}</div></section>`).join('')}<div class="related-words">${metaList('近义词', sense.synonyms)}${metaList('反义词', sense.antonyms)}${metaList('易混淆词', sense.confusables)}</div></div></details>`).join('')}</div>
      <nav class="entry-pagination" aria-label="相邻词条">${previous ? `<a href="${wordHref(previous.word)}"><span>← 上一个词</span><strong>${esc(previous.word)}</strong></a>` : '<span></span>'}${next ? `<a href="${wordHref(next.word)}"><span>下一个词 →</span><strong>${esc(next.word)}</strong></a>` : '<span></span>'}</nav></div></div></div>`)

  document.querySelectorAll<HTMLButtonElement>('[data-jump]').forEach((button) => button.addEventListener('click', () => {
    const details = document.getElementById(button.dataset.jump!) as HTMLDetailsElement
    details.open = true
    details.scrollIntoView({ behavior: 'smooth', block: 'start' })
    history.replaceState(null, '', `${wordHref(entry.word)}#${details.id}`)
  }))
  document.querySelectorAll<HTMLButtonElement>('[data-audio]').forEach((button) => button.addEventListener('click', async () => {
    try {
      if (currentAudio) { currentAudio.pause(); currentAudio = null }
      document.querySelectorAll('.audio-button').forEach((item) => item.classList.remove('playing'))
      const player = new Audio(button.dataset.audio)
      currentAudio = player
      button.classList.add('playing')
      player.addEventListener('ended', () => button.classList.remove('playing'), { once: true })
      player.addEventListener('error', () => button.classList.remove('playing'), { once: true })
      await player.play()
    } catch {
      button.classList.remove('playing')
      button.title = '音频暂时无法播放'
    }
  }))
  if (location.hash.startsWith('#sense-')) {
    const details = document.getElementById(location.hash.slice(1)) as HTMLDetailsElement | null
    if (details) { details.open = true; requestAnimationFrame(() => details.scrollIntoView()) }
  }
}

function init(): void {
  const word = strip(new URLSearchParams(location.search).get('word') || '')
  const entry = byWord.get(word)
  if (entry) renderEntry(entry)
  else renderHome(word)
}

init()
