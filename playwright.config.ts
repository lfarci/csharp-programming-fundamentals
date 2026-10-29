// Browser tests for the website (progress ticks, import). Local: npm run docs:build && npm run test:site
// Live site: SITE_URL=https://lfarci.github.io/csharp-programming-fundamentals npm run test:site
import { defineConfig } from '@playwright/test'

const live = process.env.SITE_URL
export default defineConfig({
  testDir: 'site-tests',
  timeout: 30_000,
  retries: live ? 2 : 0,
  reporter: [['list']],
  use: { baseURL: (live ?? 'http://localhost:4173/csharp-programming-fundamentals') + '/', browserName: 'chromium' },
  webServer: live ? undefined : {
    command: 'npx vitepress preview --port 4173',
    url: 'http://localhost:4173/csharp-programming-fundamentals/',
    reuseExistingServer: !process.env.CI,
  },
})
