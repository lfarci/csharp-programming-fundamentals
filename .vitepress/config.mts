// Website built from the repo Markdown (single source). Preview: npm run docs:dev
import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import fs from 'node:fs'
import path from 'node:path'
import course from './course.json' with { type: 'json' }

const REPO = 'https://github.com/lfarci/csharp-programming-fundamentals'
const ROOT = path.resolve(__dirname, '..')
// Not part of the site (machinery, agent notes). Links to them go to GitHub.
const EXCLUDE = ['node_modules/**', 'tools/**', 'tests/**', '.agents/**', '.github/**', 'AGENTS.md', 'CLAUDE.md',
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

// Sidebar: exercises grouped by roadmap step, in course order.
const steps: Record<string, any[]> = {}
for (const e of course.exercises) (steps[e.step] ??= []).push({ text: `${e.id} ${e.title}`, link: e.link })

export default withMermaid(defineConfig({
  title: 'C# Programming Fundamentals',
  description: 'Loops, step by step: recipes, exercises and drills for beginners.',
  base: '/csharp-programming-fundamentals/',
  srcDir: '.',
  srcExclude: EXCLUDE,
  rewrites: { 'README.md': 'index.md', ':dir/README.md': ':dir/index.md' },
  cleanUrls: true,
  lastUpdated: false,
  ignoreDeadLinks: false,
  markdown: { config: githubLinks },
  themeConfig: {
    nav: [
      { text: 'Start here', link: '/docs/getting-started' },
      { text: 'Roadmap', link: '/ROADMAP' },
      { text: 'Exercises', link: '/exercises/' },
      { text: 'My progress', link: '/progress' },
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
        { text: 'How to read an exercise', link: '/docs/reading-an-exercise' },
        { text: 'Problem solving', link: '/docs/problem-solving' },
        { text: 'Glossary', link: '/docs/glossary' },
      ] },
      { text: 'Roadmap', items: [{ text: 'The plan, week by week', link: '/ROADMAP' }, { text: 'My progress', link: '/progress' }] },
      { text: 'Drill sets', items: [{ text: 'Same pattern, many times', link: '/exercises/#drill-sets-same-pattern-many-times' }] },
      { text: 'Exercises', collapsed: false, items: [
        { text: 'All exercises', link: '/exercises/' },
        ...Object.entries(steps).map(([s, items]) => ({ text: `Step ${s}`, collapsed: true, items })),
      ] },
      { text: 'Cookbook', collapsed: true, items: [
        { text: 'All recipes', link: '/cookbook/' },
        ...fs.readdirSync(path.join(ROOT, 'cookbook')).filter((f) => f !== 'README.md' && f.endsWith('.md')).sort()
          .map((f) => ({ text: fs.readFileSync(path.join(ROOT, 'cookbook', f), 'utf8').match(/^# (.+)$/m)?.[1] ?? f,
            link: `/cookbook/${f.replace(/\.md$/, '')}` })),
      ] },
      { text: 'How to practice', items: [
        { text: 'How to practice', link: '/docs/how-to-practice' },
        { text: 'Progress checklist (paper)', link: '/docs/progress-checklist' },
      ] },
    ],
  },
  mermaid: {},
}))
