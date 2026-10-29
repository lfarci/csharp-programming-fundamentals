<script setup lang="ts">
// "How it fits together": for each theme, Microsoft Learn module -> video -> exercises, in the roadmap style.
import { computed } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
type Row = { num: number; title: string; link: string; group: string; part: number; module: string; moduleUrl: string; video: string; videoPage: string; exercises: number; first: { id: string; link: string } }
const groups = computed(() => {
  const out: { name: string; rows: Row[] }[] = []
  for (const r of (course as any).flow as Row[]) {
    const last = out[out.length - 1]
    if (last && last.name === r.group) last.rows.push(r); else out.push({ name: r.group, rows: [r] })
  }
  return out
})
</script>

<template>
  <div class="flow">
    <div class="legend" aria-hidden="true"><span>Theme</span><span>1. Learn</span><span>2. Watch</span><span>3. Practise</span></div>
    <section v-for="g in groups" :key="g.name">
      <div class="cpf-kicker part-kicker">{{ g.name.split(': ')[0] }}</div>
      <h2 :id="'flow-' + g.name.split(': ')[1].toLowerCase().replace(/ /g, '-')" class="part-name">{{ g.name.split(': ')[1] }}</h2>
      <ol class="steps">
        <li v-for="r in g.rows" :key="r.link">
          <span class="cpf-num" aria-hidden="true">{{ r.num }}</span>
          <div class="cpf-card row">
            <a class="cell theme" :href="withBase(r.link)">{{ r.title }}</a>
            <span class="arrow" aria-hidden="true">&rarr;</span>
            <a class="cell" :href="r.moduleUrl" target="_blank" rel="noopener"><span class="lab">Microsoft Learn, Part {{ r.part }}</span>{{ r.module }}</a>
            <span class="arrow" aria-hidden="true">&rarr;</span>
            <a class="cell" :href="withBase(r.videoPage)"><span class="lab">Video</span>{{ r.video }}</a>
            <span class="arrow" aria-hidden="true">&rarr;</span>
            <a class="cell" :href="withBase(r.first.link)"><span class="lab">{{ r.exercises }} exercise{{ r.exercises === 1 ? '' : 's' }}</span>Start with {{ r.first.id }}</a>
          </div>
        </li>
      </ol>
    </section>
  </div>
</template>

<style scoped>
.legend { display: grid; grid-template-columns: 1.1fr 1.4fr 1.2fr 0.9fr; gap: 28px; padding-left: 70px; font-size: 12px; font-weight: 600; color: var(--vp-c-text-3); text-transform: uppercase; letter-spacing: .05em; }
.part-kicker { margin-top: 28px; }
.part-name { border-top: none; margin: 2px 0 10px; padding-top: 0; font-size: 20px; color: var(--vp-c-brand-1); }
.steps { list-style: none; padding: 0; margin: 0; }
.steps > li { position: relative; padding-left: 52px; margin: 0 0 10px; }
.steps > li::before { content: ''; position: absolute; left: 17px; top: 46px; bottom: -12px; width: 2px; background: var(--vp-c-divider); }
.steps > li:last-child::before { display: none; }
.steps .cpf-num { position: absolute; left: 0; top: 12px; }
.row { display: grid; grid-template-columns: 1.1fr auto 1.4fr auto 1.2fr auto 0.9fr; gap: 8px; align-items: center; padding: 10px 14px; }
.cell { font-size: 13px; line-height: 1.35; text-decoration: none; color: var(--vp-c-text-1); }
.cell:hover { color: var(--vp-c-brand-1); }
.cell.theme { font-weight: 600; font-size: 15px; }
.lab { display: block; font-size: 11px; color: var(--vp-c-text-3); }
.arrow { color: var(--vp-c-brand-1); }
@media (max-width: 760px) { .legend { display: none; } .row { grid-template-columns: 1fr; } .arrow { display: none; } }
</style>
