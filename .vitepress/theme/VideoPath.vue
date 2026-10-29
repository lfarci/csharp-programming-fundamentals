<script setup lang="ts">
// The kept Absolute Beginners episodes as roadmap-style numbered cards, grouped like the roadmap.
import { withBase } from 'vitepress'
import course from '../course.json'
const groups = (course as any).videos as { group: string; episodes: { num: number; title: string; minutes: number; url: string; themes: { title: string; link: string }[] }[] }[]
</script>

<template>
  <div class="path">
    <section v-for="g in groups" :key="g.group">
      <div class="cpf-kicker part-kicker">{{ g.group.split(': ')[0] }}</div>
      <h2 :id="'videos-' + g.group.split(': ')[1].toLowerCase().replace(/ /g, '-')" class="part-name">{{ g.group.split(': ')[1] }}</h2>
      <ol class="steps">
        <li v-for="e in g.episodes" :key="e.url">
          <span class="cpf-num" aria-hidden="true">{{ e.num }}</span>
          <div class="cpf-card card">
            <a class="title" :href="e.url" target="_blank" rel="noopener">{{ e.title }}</a>
            <span class="meta">Video, {{ e.minutes }} min</span>
            <span class="then">Then practise:
              <template v-for="(t, i) in e.themes" :key="t.link"><a class="theme" :href="withBase(t.link)">{{ t.title }}</a><span v-if="i < e.themes.length - 1">, </span></template>
            </span>
          </div>
        </li>
      </ol>
    </section>
  </div>
</template>

<style scoped>
.part-kicker { margin-top: 32px; }
.part-name { border-top: none; margin: 2px 0 10px; padding-top: 0; font-size: 20px; color: var(--vp-c-brand-1); }
.steps { list-style: none; padding: 0; margin: 0; }
.steps > li { position: relative; padding-left: 52px; margin: 0 0 12px; }
.steps > li::before { content: ''; position: absolute; left: 17px; top: 46px; bottom: -14px; width: 2px; background: var(--vp-c-divider); }
.steps > li:last-child::before { display: none; }
.steps .cpf-num { position: absolute; left: 0; top: 10px; }
.card { padding: 12px 16px; }
.title { display: block; font-weight: 600; font-size: 16px; text-decoration: none; color: var(--vp-c-text-1); }
.title:hover { color: var(--vp-c-brand-1); }
.meta { display: block; font-size: 13px; color: var(--vp-c-text-3); margin-top: 2px; }
.then { display: block; font-size: 14px; color: var(--vp-c-text-2); margin-top: 6px; }
.theme { font-weight: 600; }
</style>
