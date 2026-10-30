import { test, expect } from '@playwright/test'
import { readFileSync } from 'node:fs'

// The number of exercises comes from the generator, so adding an exercise does not break these tests.
const ALL = JSON.parse(readFileSync(new URL('../../tools/exercises.json', import.meta.url), 'utf8'))
const TOTAL = ALL.length
const LOOPS = ALL.filter((e: { theme: string }) => e.theme === 'Loops').length

// Each test starts with an empty browser store (Playwright gives every test a fresh context).

test('Mark as done on an exercise page survives a reload and shows on its theme and overview', async ({ page }) => {
  await page.goto('exercises/A04-factorial')
  const tick = page.getByLabel('Mark A04 as done')
  await expect(tick).not.toBeChecked()
  await tick.check()
  await page.reload()
  await expect(page.getByLabel('Mark A04 as done')).toBeChecked()

  await page.goto('themes/loops')
  await expect(page.locator('.groups li', { hasText: 'Add up' })).toContainText('1 / 12')
  await page.locator('.groups a', { hasText: 'Add up' }).click()
  await expect(page).toHaveURL(/themes\/loops-add-up$/)
  await expect(page.locator('.theme-ex[data-group="add-up"] .count')).toHaveText(/1 of 12 done/)
  await expect(page.locator('.theme-ex').getByLabel('Mark A04 as done')).toBeChecked()

  await page.goto('exercises/')
  await expect(page.locator('.overview .summary')).toContainText(`1 of ${TOTAL}`)
  await expect(page.locator('.overview li.item', { hasText: 'Loops' })).toContainText(`1 / ${LOOPS}`)

  await page.goto('progress')
  await expect(page.locator('.progress .big')).toContainText(`1 of ${TOTAL}`)
})

test('Ticking in a theme table updates the count, and unticking removes it', async ({ page }) => {
  await page.goto('themes/basics-conditions')
  const box = page.locator('.theme-ex').getByLabel('Mark C01 as done')
  await box.check()
  await expect(page.locator('.theme-ex[data-group="conditions"] .count')).toHaveText(/1 of 4 done/)
  await page.reload()
  await expect(page.locator('.theme-ex').getByLabel('Mark C01 as done')).toBeChecked()
  await page.locator('.theme-ex').getByLabel('Mark C01 as done').uncheck()
  await expect(page.locator('.theme-ex[data-group="conditions"] .count')).toHaveText(/0 of 4 done/)
})

test('Importing a sync code from ./ex progress marks those exercises as done', async ({ page }) => {
  await page.goto('progress')
  await page.getByLabel('Sync code or JSON backup').fill('CPF1:A1-4;L11')
  await page.getByRole('button', { name: 'Import' }).click()
  await expect(page.getByRole('status')).toContainText('5 new exercise(s)')
  await expect(page.locator('.progress .big')).toContainText(`5 of ${TOTAL}`)
  await page.reload()
  await expect(page.locator('.progress .big')).toContainText(`5 of ${TOTAL}`)
  await expect(page.locator('.progress p', { hasText: 'Your sync code for this browser' }).locator('code')).toHaveText('CPF1:A1-4;L11')

  await page.goto('exercises/L11-count-from-a-to-b')
  await expect(page.getByLabel('Mark L11 as done')).toBeChecked()
})

test('A wrong code is refused with a clear message', async ({ page }) => {
  await page.goto('progress')
  await page.getByLabel('Sync code or JSON backup').fill('hello')
  await page.getByRole('button', { name: 'Import' }).click()
  await expect(page.getByRole('status')).toContainText('Not imported')
  await expect(page.locator('.progress .big')).toContainText(`0 of ${TOTAL}`)
})

test('The home page has the logo, the favicon and a playable demo video', async ({ page, request }) => {
  await page.goto('')
  await expect(page.locator('.VPNavBarTitle img.logo')).toBeVisible()
  const icon = await page.locator('link[rel="icon"][type="image/svg+xml"]').getAttribute('href')
  expect((await request.get(icon!)).status()).toBe(200)
  const video = await page.locator('.home-demo video source').getAttribute('src')
  expect((await request.get(video!)).status()).toBe(200)
})

test('The Microsoft Learn page lists the 6 parts with their themes', async ({ page }) => {
  await page.goto('learn/microsoft-learn')
  await expect(page.locator('.steps > li')).toHaveCount(6)
  await expect(page.getByRole('link', { name: 'Add logic to C# console applications' })).toHaveAttribute('href', /get-started-c-sharp-part-3/)
  await expect(page.locator('.steps .theme').first()).toBeVisible()
})

test('The Videos gallery lists only the kept episodes, and each opens its own page', async ({ page }) => {
  await page.goto('learn/videos')
  await expect(page.locator('.gallery li')).toHaveCount(13)
  await expect(page.getByText('Working with LINQ')).toHaveCount(0)
  await page.locator('.gallery a', { hasText: 'for Iteration Statement' }).click()
  await expect(page).toHaveURL(/learn\/videos\/for-iteration-statement/)
  await expect(page.getByRole('link', { name: 'Watch on Microsoft Learn' })).toHaveAttribute('href', /csharp-fundamentals-for-absolute-beginners\/for-iteration-statement/)
  await expect(page.getByRole('heading', { name: 'Practise after this' })).toBeVisible()
})

test('The Learn overview links every theme to a module, a video and its exercises', async ({ page }) => {
  await page.goto('learn/')
  await expect(page.locator('.flow .steps > li')).toHaveCount(4)
  await expect(page.locator('.flow .steps > li').first().locator('a')).toHaveCount(4)
})

test('An exercise page says where you are, and Previous/Next stay inside the theme', async ({ page }) => {
  await page.goto('exercises/L11-count-from-a-to-b')
  await expect(page.locator('.ex-head .cpf-kicker')).toHaveText('Loops › Count')
  await expect(page.locator('.ex-head .pos')).toHaveText('Exercise 4 of 13')
  await expect(page.locator('.VPDocFooter .pager-link.prev')).toContainText('L03')
  await expect(page.locator('.VPDocFooter .pager-link.next')).toContainText('L12')
})

test('The sidebar shows themes and groups, never one link per exercise', async ({ page }) => {
  await page.goto('themes/loops')
  await expect(page.locator('.VPSidebar a[href*="/exercises/"][href$="-"], .VPSidebar a[href*="/exercises/A"], .VPSidebar a[href*="/exercises/L"]')).toHaveCount(0)
  await expect(page.locator('.VPSidebar').getByRole('link', { name: 'Draw shapes' })).toHaveCount(1)
})

test('The Learn the theory card has one video, one module and the first exercise', async ({ page }) => {
  await page.goto('themes/loops')
  const card = page.locator('.learn-card')
  await expect(card.locator('.steps > li')).toHaveCount(3)
  await expect(card.getByRole('link', { name: 'Start L01 · Trace a loop' })).toHaveAttribute('href', /exercises\/L01-trace-a-loop/)
})

test('Each group has its own page: theme cards link to it, old anchors still land on the card, Previous/Next go to the next group', async ({ page }) => {
  await page.goto('themes/loops')
  await expect(page.locator('.groups li')).toHaveCount(9)
  await expect(page.locator('.theme-ex')).toHaveCount(0)
  await expect(page.locator('#count a')).toHaveAttribute('href', /\/themes\/loops-count$/)
  await page.goto('themes/loops-count')
  await expect(page.locator('h1')).toHaveText(/Loops · Count/)
  await expect(page.locator('.VPDocFooter .pager-link.next')).toContainText('Add up')
  await expect(page.locator('.VPSidebar').getByRole('link', { name: 'Count', exact: true })).toHaveAttribute('href', /loops-count/)
  await page.goto('exercises/L11-count-from-a-to-b')
  await expect(page.locator('.ex-head .cpf-kicker a', { hasText: 'Count' })).toHaveAttribute('href', /\/themes\/loops-count$/)
})

test('Themes and groups show their names only, without a number', async ({ page }) => {
  await page.goto('themes/loops')
  await expect(page.locator('.VPSidebar').getByText('Loops', { exact: true })).toBeVisible()
  await expect(page.locator('.VPSidebar').getByText(/^\d+\.\s/)).toHaveCount(0)
  await expect(page.locator('.groups .cpf-num').first()).toHaveText('')
  await page.goto('exercises/')
  await expect(page.locator('.overview .cpf-num').first()).toHaveText('')
})

test('Completion tables have no row-number column, only the exercise and its ID', async ({ page }) => {
  await page.goto('themes/loops-add-up')
  const row = page.locator('.theme-ex .rows li').first()
  await expect(row.locator('.pos')).toHaveCount(0)
  await expect(row.locator('.id')).toHaveText(/^[A-Z]\d\d$/)
  await expect(row).not.toContainText(/^\s*1\s/)
})

test('The navbar has only Start here, Roadmap and Learn; the other sections are on the home page and in the sidebar', async ({ page }) => {
  await page.goto('./')
  const nav = (await page.locator('.VPNavBarMenu > :not(.visually-hidden)').allTextContents()).map((t) => t.trim())
  expect(nav).toEqual(['Start here', 'Roadmap', 'Learn'])
  for (const [text, href] of [['Cookbook', 'cookbook/'], ['Exercises', 'exercises/'], ['Projects', 'projects/'], ['Study skills', 'docs/']]) {
    await expect(page.locator(`.VPFooter a[href$="/${href}"]`)).toHaveText(text)
    await expect(page.locator(`.VPFeatures a[href$="/${href}"]`).first()).toBeVisible()
  }
  await page.goto('./docs/getting-started')
  for (const s of ['Cookbook', 'Exercises', 'Projects', 'Study skills']) await expect(page.locator('.VPSidebar .VPSidebarItem.level-0 > .item', { hasText: s }).first()).toBeVisible()
})

test('The projects overview groups 10 project cards with level, effort and themes, and the level dots are round', async ({ page }) => {
  for (const width of [1280, 390]) {
    await page.setViewportSize({ width, height: 900 })
    await page.goto('./projects/')
    for (const d of await page.locator('.pgroup .dot').all()) {
      const b = (await d.boundingBox())!
      expect(Math.abs(b.width - b.height), `dot ${b.width}x${b.height} at width ${width}`).toBeLessThan(0.5)
    }
  }
  await page.setViewportSize({ width: 1280, height: 900 })
  await expect(page.locator('.pgroup h2')).toHaveText(['Terminal games', 'Learn something real', 'Just for fun'])
  const cards = page.locator('.pgroup .item')
  await expect(cards).toHaveCount(10)
  for (const c of await cards.all()) {
    await expect(c.locator('.level')).toHaveText(/Easy|Medium|Hard/)
    await expect(c.locator('.effort')).toContainText('hours')
    expect(await c.locator('.tag').count()).toBeGreaterThan(0)
  }
  await cards.filter({ hasText: 'Hangman' }).click()
  await expect(page.locator('h1')).toHaveText('Hangman')
  for (const h of ['A sample run', 'What you will learn', 'Milestones', 'Stretch goals', 'Hints (open one at a time)']) await expect(page.locator('h2', { hasText: h })).toBeVisible()
  expect(await page.locator('h2:has-text("Milestones") + p + ol > li').count()).toBeGreaterThanOrEqual(5)
  expect(await page.locator('h2:has-text("Stretch goals") + p + ul > li').count()).toBeGreaterThanOrEqual(4)
})
