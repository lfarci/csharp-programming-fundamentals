// Website built from the repo Markdown (single source). Preview: npm run docs:dev
import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'
import course from './course.json' with { type: 'json' }

const REPO = 'https://github.com/lfarci/csharp-programming-fundamentals'
const ROOT = path.resolve(__dirname, '..')
// Not part of the site (machinery, agent notes). Links to them go to GitHub.
const EXCLUDE = ['README.md', 'node_modules/**', 'diagrams/**', 'public/**', 'tools/**', 'tests/**', '.agents/**', '.github/**', 'AGENTS.md', 'CLAUDE.md',
  'practice/PROGRESS.md', 'docs/writing-guide.md', 'docs/learner-persona.md']
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
      let rel = path.posix.normalize(path.posix.join(path.posix.dirname(env.relativePath), decodeURI(file)))
      // The repo README is the GitHub front page; on the site, "Home" is home.md (the site root).
      if (rel === 'README.md') {
        t.attrSet('href', '/' + (hash ? '#' + hash : ''))
        return base ? base(tokens, idx, opts, env, self) : self.renderToken(tokens, idx, opts)
      }
      const abs = path.join(ROOT, rel)
      if (fs.existsSync(abs) && fs.statSync(abs).isDirectory()) {
        if (fs.existsSync(path.join(abs, 'README.md')) && !excluded(rel + '/README.md')) {
          t.attrSet('href', file.replace(/\/?$/, '/index.md') + (hash ? '#' + hash : ''))
        } else t.attrSet('href', `${REPO}/tree/main/${rel}`)
      } else if (!rel.endsWith('.md') || excluded(rel)) {
        t.attrSet('href', `${REPO}/blob/main/${rel}${hash ? '#' + hash : ''}`)
      } else if (/(^|\/)README\.md$/.test(rel)) {
        // README.md pages are rewritten to index.md
        t.attrSet('href', file.replace(/README\.md$/, 'index.md') + (hash ? '#' + hash : ''))
      }
    }
    return base ? base(tokens, idx, opts, env, self) : self.renderToken(tokens, idx, opts)
  }
}

// Sidebar: themes and their groups only, never one link per exercise (tools/check-structure.py checks it).
// Exercises are reached from the theme page tables and the Previous/Next links of each exercise page.
const themeItems = course.themes.map((t, i) => ({
  text: `${i + 1}. ${t.title}`, collapsed: true, link: t.link,
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
  srcDir: '.',
  srcExclude: EXCLUDE,
  rewrites: { 'home.md': 'index.md', ':dir/README.md': ':dir/index.md' },
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
      { text: 'Cookbook', link: '/cookbook/' },
      { text: 'Exercises', link: '/exercises/' },
      { text: 'Study skills', link: '/docs/' },
    ],
    search: { provider: 'local' },
    outline: { level: [2, 3], label: 'On this page' },
    socialLinks: [{ icon: 'github', link: REPO }],
    editLink: { pattern: `${REPO}/edit/main/:path`, text: 'Edit this page on GitHub' },
    footer: { message: 'The real check is ./ex check in your own copy of the course. This site does not run C#.' },
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
        ...fs.readdirSync(path.join(ROOT, 'cookbook')).filter((f) => /^\d\d-.*\.md$/.test(f)).sort()
          .map((f) => ({ text: fs.readFileSync(path.join(ROOT, 'cookbook', f), 'utf8').match(/^# Recipe \d+ · ([^—\n]+)/m)?.[1].trim() ?? f,
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
