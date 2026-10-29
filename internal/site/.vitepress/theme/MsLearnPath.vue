<script setup lang="ts">
// The 6 Microsoft Learn parts as roadmap-style numbered cards, each module with the themes to do after it.
import { withBase } from 'vitepress'
import course from '../course.json'
const parts = (course as any).mslearn as { num: number; title: string; url: string; modules: { title: string; url: string; themes: { title: string; link: string }[] }[] }[]
</script>

<template>
  <ol class="steps">
    <li v-for="p in parts" :key="p.num">
      <span class="cpf-num" aria-hidden="true">{{ p.num }}</span>
      <div class="cpf-card card">
        <div class="cpf-kicker">Microsoft Learn, Part {{ p.num }}</div>
        <a class="title" :href="p.url" target="_blank" rel="noopener">{{ p.title }}</a>
        <ul class="mods">
          <li v-for="m in p.modules" :key="m.url">
            <a :href="m.url" target="_blank" rel="noopener">{{ m.title }}</a>
            <span v-if="m.themes.length" class="then">Then:
              <template v-for="(t, i) in m.themes" :key="t.link"><a class="theme" :href="withBase(t.link)">{{ t.title }}</a><span v-if="i < m.themes.length - 1">, </span></template>
            </span>
          </li>
        </ul>
      </div>
    </li>
  </ol>
</template>

<style scoped>
.steps { list-style: none; padding: 0; margin: 16px 0; }
.steps > li { position: relative; padding-left: 52px; margin: 0 0 12px; }
.steps > li::before { content: ''; position: absolute; left: 17px; top: 46px; bottom: -14px; width: 2px; background: var(--vp-c-divider); }
.steps > li:last-child::before { display: none; }
.steps .cpf-num { position: absolute; left: 0; top: 12px; }
.card { padding: 14px 18px; }
.title { display: block; font-weight: 600; font-size: 17px; margin: 2px 0 8px; text-decoration: none; color: var(--vp-c-text-1); }
.title:hover { color: var(--vp-c-brand-1); }
.mods { margin: 0; padding-left: 18px; font-size: 14px; }
.mods li { margin: 6px 0; }
.then { display: block; color: var(--vp-c-text-2); font-size: 13px; }
.theme { font-weight: 600; }
</style>
