// Website built from the repo Markdown (single source). Preview: npm run docs:dev
import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'
import course from './course.json' with { type: 'json' }

const REPO = 'https://github.com/lfarci/csharp-programming-fundamentals'
// The repo: README.md (start here), practice/ (the learner's code), course/ (the site pages), internal/ (machinery).
const REPO_ROOT = path.resolve(__dirname, '../../..')
const SRC = path.join(REPO_ROOT, 'course')
// Not part of the site (agent notes, diagram sources, static files). Links to them go to GitHub.
const EXCLUDE = ['README.md', 'diagrams/**', 'public/**', 'docs/writing-guide.md', 'docs/learner-persona.md']
// The pages live in course/, the npm packages in internal/node_modules: resolve bare imports
// from a page (vue, the theme's packages) as if they came from internal/.
const fromInternal = {
  name: 'resolve-from-internal',
  enforce: 'pre' as const,
  async resolveId(this: any, id: string, importer?: string) {
    if (!importer || !importer.startsWith(SRC + path.sep) || /^[./\0]|^[a-z]:/i.test(id) || id.startsWith('@theme') || id.startsWith('@siteData')) return null
    return this.resolve(id, path.join(__dirname, 'config.mts'), { skipSelf: true })
  },
}
const excluded = (rel: string) =>
  EXCLUDE.some((g) => (g.endsWith('/**') ? rel.startsWith(g.slice(0, -2)) : rel === g))

// Relative links to files that are not site pages (.cs solutions, excluded pages, folders) open on GitHub.
function githubLinks(md: any) {
  const base = md.renderer.rules.link_open
  md.renderer.rules.link_open = (tokens: any, idx: number, opts: any, env: any, self: any) => {
    const t = tokens[idx]
    const href: string = t.attrGet('href') || ''
    if (href && !/^[a-z]+:|^#|^\//i.test(href) && env.relativePath) {
      const [file, hash] = href.split('#')
      // rel: path inside course/ (the site); repo: path from the repo root (for GitHub links).
      const rel = path.posix.normalize(path.posix.join(path.posix.dirname(env.relativePath), decodeURI(file)))
      const repo = path.posix.normalize(path.posix.join('course', rel))
      // The repo README is the GitHub front page; on the site, "Home" is home.md (the site root).
      if (repo === 'README.md') {
        t.attrSet('href', '/' + (hash ? '#' + hash : ''))
        return base ? base(tokens, idx, opts, env, self) : self.renderToken(tokens, idx, opts)
      }
      const abs = path.join(REPO_ROOT, repo)
      if (repo.startsWith('../')) throw new Error(`${env.relativePath}: link ${href} leaves the repo`)
      if (rel.startsWith('../')) {
        // Outside course/ (practice/, internal/, AGENTS.md...): not a site page, open it on GitHub.
        const kind = fs.existsSync(abs) && fs.statSync(abs).isDirectory() ? 'tree' : 'blob'
        t.attrSet('href', `${REPO}/${kind}/main/${repo}${hash ? '#' + hash : ''}`)
      } else if (fs.existsSync(abs) && fs.statSync(abs).isDirectory()) {
        if (fs.existsSync(path.join(abs, 'README.md')) && !excluded(rel + '/README.md')) {
          t.attrSet('href', file.replace(/\/?$/, '/index.md') + (hash ? '#' + hash : ''))
        } else t.attrSet('href', `${REPO}/tree/main/${repo}`)
      } else if (!rel.endsWith('.md') || excluded(rel)) {
        t.attrSet('href', `${REPO}/blob/main/${repo}${hash ? '#' + hash : ''}`)
      } else if (/(^|\/)README\.md$/.test(rel)) {
        // README.md pages are rewritten to index.md
        t.attrSet('href', file.replace(/README\.md$/, 'index.md') + (hash ? '#' + hash : ''))
      }
    }
    return base ? base(tokens, idx, opts, env, self) : self.renderToken(tokens, idx, opts)
  }
}

// Sidebar: themes and their groups only, never one link per exercise (internal/tools/check-structure.py checks it).
// Exercises are reached from the theme page tables and the Previous/Next links of each exercise page.
const themeItems = course.themes.map((t, i) => ({
  text: t.title, collapsed: true, link: t.link,
  items: t.groups.map((g) => ({ text: g.title, link: g.link })),
}))

export default defineConfig({
  title: 'C# Fundamentals',
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/csharp-programming-fundamentals/favicon.svg' }],
    ['link', { rel: 'icon', type: 'image/x-icon', href: '/csharp-programming-fundamentals/favicon.ico', sizes: '16x16 32x32 48x48' }],
    ['link', { rel: 'apple-touch-icon', href: '/csharp-programming-fundamentals/apple-touch-icon.png' }],
    ['meta', { name: 'theme-color', content: '#3451b2' }],
  ],
  description: 'Loops, step by step: recipes, exercises and drills for beginners.',
  base: '/csharp-programming-fundamentals/',
  srcDir: SRC,
  vite: { plugins: [fromInternal] },
  cacheDir: path.join(__dirname, 'cache'),
  outDir: path.join(__dirname, 'dist'),
  srcExclude: EXCLUDE,
  // answer-keys/ keeps its old URL /solutions/ (the .cs solutions are in internal/solutions/).
  rewrites: { 'home.md': 'index.md', 'answer-keys/README.md': 'solutions/index.md', 'answer-keys/:page.md': 'solutions/:page.md', ':dir/README.md': ':dir/index.md' },
  cleanUrls: true,
  lastUpdated: false,
  ignoreDeadLinks: false,
  markdown: { config: githubLinks },
  themeConfig: {
    logo: { src: '/logo.svg', alt: '' },
    nav: [
      { text: 'Start here', link: '/docs/getting-started' },
      { text: 'Roadmap', link: '/ROADMAP' },
      { text: 'Learn', link: '/learn/' },
    ],
    // Only 3 top links: Cookbook, Exercises, Projects and Study skills are in the sidebar, the home cards and the home footer.
    search: { provider: 'local' },
    outline: { level: [2, 3], label: 'On this page' },
    socialLinks: [{ icon: 'github', link: REPO }],
    editLink: { pattern: `${REPO}/edit/main/course/:path`, text: 'Edit this page on GitHub' },
    footer: { message: '<a href="/csharp-programming-fundamentals/cookbook/">Cookbook</a> · <a href="/csharp-programming-fundamentals/exercises/">Exercises</a> · <a href="/csharp-programming-fundamentals/projects/">Projects</a> · <a href="/csharp-programming-fundamentals/docs/">Study skills</a>', copyright: 'The real check is ./ex check in your own copy of the course. This site does not run C#.' },
    sidebar: [
      { text: 'Start here', items: [
        { text: 'Home', link: '/' },
        { text: 'Getting started', link: '/docs/getting-started' },
        { text: 'Roadmap', link: '/ROADMAP' },
      ] },
      { text: 'Learn', items: [
        { text: 'Overview', link: '/learn/' },
        { text: 'Microsoft Learn modules', link: '/learn/microsoft-learn' },
        { text: 'Videos', link: '/learn/videos' },
        { text: 'Certification', link: '/learn/certification' },
        { text: 'Extra exercises', link: '/learn/quest-tracker' },
      ] },
      { text: 'Cookbook', collapsed: true, items: [
        { text: 'All recipes', link: '/cookbook/' },
        { text: 'Which loop should I use?', link: '/cookbook/which-loop' },
        ...fs.readdirSync(path.join(SRC, 'cookbook')).filter((f) => /^\d\d-.*\.md$/.test(f)).sort()
          .map((f) => ({ text: fs.readFileSync(path.join(SRC, 'cookbook', f), 'utf8').match(/^# Recipe \d+ · ([^—\n]+)/m)?.[1].trim() ?? f,
            link: `/cookbook/${f.replace(/\.md$/, '')}` })),
        { text: 'Combining recipes', link: '/cookbook/combining-recipes' },
        { text: 'The maths', link: '/cookbook/the-maths' },
      ] },
      { text: 'Exercises', items: [
        { text: 'All exercises', link: '/exercises/' },
        { text: 'My progress', link: '/progress' },
        { text: 'Drill sets', link: '/exercises/#drill-sets-same-pattern-many-times' },
        ...themeItems,
      ] },
      { text: 'Projects', collapsed: true, items: [
        { text: 'All projects', link: '/projects/' },
        ...(course as any).projects.groups.flatMap((g: any) => g.items.map((p: any) => ({ text: p.title, link: p.link }))),
      ] },
      { text: 'Study skills', items: [
        { text: 'All study skills', link: '/docs/' },
        { text: 'How to read an exercise', link: '/docs/reading-an-exercise' },
        { text: 'Solving a problem', link: '/docs/problem-solving' },
        { text: 'How to practice', link: '/docs/how-to-practice' },
        { text: 'Glossary', link: '/docs/glossary' },
      ] },
    ],
  },
})
