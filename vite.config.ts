import { defineConfig } from 'vite'

export default defineConfig({
  base: process.env.GITHUB_PAGES === '1' ? '/The-best-English-dictionary/' : '/',
  build: { outDir: 'dist' },
})
