import { neon } from '@neondatabase/serverless'

const json = (body: unknown, status = 200) => Response.json(body, {
  status,
  headers: { 'Cache-Control': status === 200 ? 'public, s-maxage=300, stale-while-revalidate=3600' : 'no-store' },
})

export async function GET(request: Request) {
  let word: string
  try {
    word = decodeURIComponent(new URL(request.url).pathname.split('/').pop() ?? '').toLowerCase()
  } catch {
    return json({ error: 'Invalid word' }, 400)
  }
  if (!/^[a-z][a-z'-]{0,63}$/.test(word)) return json({ error: 'Invalid word' }, 400)
  if (!process.env.DATABASE_URL) return json({ error: 'Dictionary database is not configured' }, 503)

  try {
    const sql = neon(process.env.DATABASE_URL)
    const rows = await sql`SELECT word, basic_zh, exam_levels, status, entry,
                                 source_id, source_url, version, reviewed_at, review_records
                          FROM lexemes WHERE word = ${word} AND status IN ('basic', 'published')
                          LIMIT 1`
    if (!rows.length) return json({ error: 'Word not found' }, 404)
    return json(rows[0])
  } catch (error) {
    console.error('Entry lookup failed', error)
    return json({ error: 'Dictionary entry is temporarily unavailable' }, 503)
  }
}
