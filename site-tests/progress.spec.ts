import { test, expect } from '@playwright/test'

// Each test starts with an empty browser store (Playwright gives every test a fresh context).

test('Mark as done on an exercise page survives a reload and shows on its theme and overview', async ({ page }) => {
  await page.goto('exercises/A04-factorial')
  const tick = page.getByLabel('Mark A04 as done')
  await expect(tick).not.toBeChecked()
  await tick.check()
  await page.reload()
  await expect(page.getByLabel('Mark A04 as done')).toBeChecked()

  await page.goto('themes/loops-running-result')
  await expect(page.locator('.theme-ex .count')).toHaveText(/1 of 22 done/)
  await expect(page.locator('.theme-ex').getByLabel('Mark A04 as done')).toBeChecked()

  await page.goto('exercises/')
  await expect(page.locator('.overview .summary')).toContainText('1 of 96')
  await expect(page.locator('.overview li', { hasText: 'Loops: keep a running result' })).toContainText('1 / 22')

  await page.goto('progress')
  await expect(page.locator('.progress .big')).toContainText('1 of 96')
})

test('Ticking in a theme table updates the count, and unticking removes it', async ({ page }) => {
  await page.goto('themes/conditions')
  const box = page.locator('.theme-ex').getByLabel('Mark C01 as done')
  await box.check()
  await expect(page.locator('.theme-ex .count')).toHaveText(/1 of 4 done/)
  await page.reload()
  await expect(page.locator('.theme-ex').getByLabel('Mark C01 as done')).toBeChecked()
  await page.locator('.theme-ex').getByLabel('Mark C01 as done').uncheck()
  await expect(page.locator('.theme-ex .count')).toHaveText(/0 of 4 done/)
})

test('Importing a sync code from ./ex progress marks those exercises as done', async ({ page }) => {
  await page.goto('progress')
  await page.getByLabel('Sync code or JSON backup').fill('CPF1:A1-4;L11')
  await page.getByRole('button', { name: 'Import' }).click()
  await expect(page.getByRole('status')).toContainText('5 new exercise(s)')
  await expect(page.locator('.progress .big')).toContainText('5 of 96')
  await page.reload()
  await expect(page.locator('.progress .big')).toContainText('5 of 96')
  await expect(page.locator('.progress p', { hasText: 'Your sync code for this browser' }).locator('code')).toHaveText('CPF1:A1-4;L11')

  await page.goto('exercises/L11-count-from-a-to-b')
  await expect(page.getByLabel('Mark L11 as done')).toBeChecked()
})

test('A wrong code is refused with a clear message', async ({ page }) => {
  await page.goto('progress')
  await page.getByLabel('Sync code or JSON backup').fill('hello')
  await page.getByRole('button', { name: 'Import' }).click()
  await expect(page.getByRole('status')).toContainText('Not imported')
  await expect(page.locator('.progress .big')).toContainText('0 of 96')
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
  await expect(page.locator('.flow .steps > li')).toHaveCount(15)
  await expect(page.locator('.flow .steps > li').first().locator('a')).toHaveCount(4)
})
