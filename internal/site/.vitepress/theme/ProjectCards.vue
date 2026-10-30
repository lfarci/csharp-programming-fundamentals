<script setup lang="ts">
// The projects overview: one section per group (games, real-world, fun), Roadmap-style cards with level, effort and themes.
import { withBase } from 'vitepress'
import course from '../course.json'

type Item = { title: string; text: string; level: string; effort: string; themes: string[]; link: string }
const groups = (course as any).projects.groups as { slug: string; title: string; text: string; items: Item[] }[]
const dots: Record<string, number> = { Easy: 1, Medium: 2, Hard: 3 }
</script>

<template>
  <section v-for="g in groups" :key="g.slug" class="pgroup" :data-group="g.slug">
    <h2 :id="g.slug" class="ptitle">{{ g.title }}</h2>
    <p class="ptext">{{ g.text }}</p>
    <ul class="cards">
      <li v-for="p in g.items" :key="p.link">
        <a class="cpf-card cpf-link item" :href="withBase(p.link)">
          <span class="title">{{ p.title }}</span>
          <span class="text">{{ p.text }}</span>
          <span class="meta">
            <span class="level" :title="`Level: ${p.level}`">
              <span v-for="n in 3" :key="n" class="dot" :class="{ on: n <= dots[p.level] }" aria-hidden="true"></span>
              {{ p.level }}
            </span>
            <span class="effort">{{ p.effort }}</span>
          </span>
          <span class="themes"><span v-for="t in p.themes" :key="t" class="tag">{{ t }}</span></span>
        </a>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.pgroup { margin-top: 28px; }
.ptitle { border-top: none !important; margin-top: 0 !important; padding-top: 0 !important; }
.ptext { color: var(--vp-c-text-2); margin: 4px 0 0; }
.cards { list-style: none; padding: 0 !important; margin: 12px 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }
.cards li { margin: 0 !important; }
.item { display: flex; flex-direction: column; gap: 6px; height: 100%; }
.title { font-weight: 600; font-size: 16px; color: var(--vp-c-text-1); }
.text { font-size: 14px; color: var(--vp-c-text-2); line-height: 1.45; flex: 1; }
.meta { display: flex; justify-content: space-between; gap: 8px; font-size: 13px; color: var(--vp-c-text-2); }
.level { display: inline-flex; align-items: center; gap: 3px; flex: none; white-space: nowrap; }
.dot { flex: 0 0 auto; box-sizing: border-box; width: 10px; height: 10px; min-width: 10px; aspect-ratio: 1; border-radius: 50%; border: 2px solid var(--vp-c-brand-1); }
.dot.on { background: var(--vp-c-brand-1); }
.level { margin-right: 6px; }
.themes { display: flex; flex-wrap: wrap; gap: 4px; }
.tag { font-size: 12px; padding: 1px 8px; border-radius: 10px; background: var(--vp-c-brand-soft); color: var(--vp-c-brand-1); }
</style>
