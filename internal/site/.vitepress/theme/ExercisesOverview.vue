<script setup lang="ts">
// All themes as numbered cards with their completion, from the browser store (same style as the roadmap).
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load } from './progress'
import ProgressSummary from './ProgressSummary.vue'

onMounted(load)
const rows = computed(() => course.themes.map((t, i) => {
  const list = course.exercises.filter((e) => e.theme === t.slug)
  const groups = t.groups.map((g) => { const gl = list.filter((e) => e.group === g.slug); return { ...g, total: gl.length, n: gl.filter((e) => done.value[e.id]).length } })
  return { ...t, num: i + 1, groups, total: list.length, n: list.filter((e) => done.value[e.id]).length }
}))
</script>

<template>
  <div class="overview">
    <ProgressSummary sync />
    <ol class="grid">
      <li v-for="r in rows" :key="r.slug" class="cpf-card item">
        <span class="cpf-num" :class="{ on: r.total && r.n === r.total }" aria-hidden="true">{{ r.num }}</span>
        <span class="body">
          <a class="title" :href="withBase(r.link)">{{ r.title }}</a>
          <span class="meta"><span class="n">{{ r.n }} / {{ r.total }}</span>
            <span class="cpf-bar" role="img" :aria-label="`${r.n} of ${r.total} done`"><span :style="{ width: (r.total ? 100 * r.n / r.total : 0) + '%' }"></span></span></span>
          <span class="groups"><a v-for="g in r.groups" :key="g.slug" :href="withBase(g.link)">{{ g.title }} <span class="gn">{{ g.n }}/{{ g.total }}</span></a></span>
        </span>
      </li>
    </ol>
    <p class="note">Ticks are saved in this browser. The real check is <code>./ex check</code> in your copy of the course.</p>
  </div>
</template>

<style scoped>
.grid { list-style: none; padding: 0; margin: 0; display: grid; gap: 12px; }
.grid li { margin: 0; }
.item { display: flex; gap: 14px; align-items: flex-start; }
.title { text-decoration: none !important; }
.title:hover { color: var(--vp-c-brand-1) !important; }
.groups { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
.groups a { font-size: 13px; border: 1px solid var(--vp-c-divider); border-radius: 12px; padding: 2px 10px; text-decoration: none; color: var(--vp-c-text-2); }
.groups a:hover { border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); }
.gn { color: var(--vp-c-text-3); font-size: 12px; }
.body { flex: 1; min-width: 0; }
.title { display: block; font-weight: 600; font-size: 15px; color: var(--vp-c-text-1); line-height: 1.35; }
.meta { display: flex; align-items: center; gap: 10px; margin-top: 6px; font-size: 13px; color: var(--vp-c-text-3); }
.n { white-space: nowrap; min-width: 44px; }
.meta .cpf-bar { flex: 1; }
.note { font-size: 14px; color: var(--vp-c-text-2); }
</style>
