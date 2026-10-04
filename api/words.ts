import { neon } from '@neondatabase/serverless'

type WordRow = {
  word: string
  basic_zh: string
  exam_levels: string[]
  status: 'basic' | 'published'
}

const json = (body: unknown, status = 200) => Response.json(body, {
  status,
  headers: { 'Cache-Control': status === 200 ? 'public, s-maxage=60, stale-while-revalidate=300' : 'no-store' },
})

export async function GET(request: Request) {
  const url = new URL(request.url)
  const query = (url.searchParams.get('query') ?? '').trim().toLowerCase()
  const letter = (url.searchParams.get('letter') ?? '').trim().toLowerCase()
  const rawLimit = url.searchParams.get('limit') ?? '25'
  const rawOffset = url.searchParams.get('offset') ?? '0'

  if ((query && !/^[a-z][a-z'-]{0,63}$/.test(query)) ||
      (letter && !/^[a-z]$/.test(letter)) ||
      !/^\d+$/.test(rawLimit) || !/^\d+$/.test(rawOffset)) {
    return json({ error: 'Invalid search parameters' }, 400)
  }
  const limit = Number(rawLimit)
  const offset = Number(rawOffset)
  if (!Number.isSafeInteger(limit) || limit < 1 || limit > 100 ||
      !Number.isSafeInteger(offset) || offset < 0 || offset > 100000) {
    return json({ error: 'Invalid pagination parameters' }, 400)
  }
  if (!process.env.DATABASE_URL) return json({ error: 'Dictionary database is not configured' }, 503)

  try {
    const sql = neon(process.env.DATABASE_URL)
    const queryPrefix = query ? `${query}%` : '%'
    const letterPrefix = letter ? `${letter}%` : '%'
    const [items, counts] = await Promise.all([
      sql`SELECT word, basic_zh, exam_levels, status
          FROM lexemes
          WHERE status IN ('basic', 'published')
            AND word LIKE ${queryPrefix} AND word LIKE ${letterPrefix}
          ORDER BY word ASC LIMIT ${limit} OFFSET ${offset}`,
      sql`SELECT count(*)::integer AS total
          FROM lexemes
          WHERE status IN ('basic', 'published')
            AND word LIKE ${queryPrefix} AND word LIKE ${letterPrefix}`,
    ])
    const total = Number(counts[0]?.total ?? 0)
    return json({ items: items as WordRow[], total, limit, offset, has_more: offset + items.length < total })
  } catch (error) {
    console.error('Word search failed', error)
    return json({ error: 'Dictionary search is temporarily unavailable' }, 503)
  }
}
