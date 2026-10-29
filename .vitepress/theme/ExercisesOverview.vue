<script setup lang="ts">
// All themes with their completion, from the browser store.
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load } from './progress'
import { inline } from './inline'

onMounted(load)
const rows = computed(() => course.themes.map((t, i) => {
  const list = course.exercises.filter((e) => e.theme === t.slug)
  return { ...t, num: i + 1, total: list.length, n: list.filter((e) => done.value[e.id]).length }
}))
const total = computed(() => Object.keys(done.value).length)
const next = computed(() => course.exercises.find((e) => !done.value[e.id]))
</script>

<template>
  <div class="overview">
    <div class="total">
      <div><strong>{{ total }} of {{ course.exercises.length }}</strong> exercises done</div>
      <div class="bar big" role="img" :aria-label="`${total} of ${course.exercises.length} done`">
        <span :style="{ width: (100 * total / course.exercises.length) + '%' }"></span></div>
      <div v-if="next" class="next">Next: <a :href="withBase(next.link)">{{ next.id }} {{ next.title }}</a></div>
    </div>
    <table>
      <thead><tr><th>#</th><th>Theme</th><th>Done</th><th class="barcol">Progress</th></tr></thead>
      <tbody>
        <tr v-for="r in rows" :key="r.slug">
          <td class="num">{{ r.num }}</td>
          <td><a :href="withBase(r.link)">{{ r.title }}</a><div class="sum" v-html="inline(r.summary)"></div></td>
          <td class="n">{{ r.n }} / {{ r.total }}</td>
          <td class="barcol"><div class="bar" role="img" :aria-label="`${r.n} of ${r.total} done`">
            <span :style="{ width: (r.total ? 100 * r.n / r.total : 0) + '%' }"></span></div></td>
        </tr>
      </tbody>
    </table>
    <p class="note">Ticks are saved in this browser. The real check is <code>./ex check</code> in your copy of the course. Sync them on <a :href="withBase('/progress')">My progress</a>.</p>
  </div>
</template>

<style scoped>
.total { border: 1px solid var(--vp-c-divider); border-radius: 10px; padding: 14px 16px; margin: 16px 0; }
.next { margin-top: 8px; }
.overview table { display: table; width: 100%; }
.overview td, .overview th { padding: 8px 12px; vertical-align: top; }
.num, .n { white-space: nowrap; color: var(--vp-c-text-2); }
.sum { font-size: 13px; color: var(--vp-c-text-2); line-height: 1.4; }
.barcol { width: 30%; }
.bar { height: 8px; background: var(--vp-c-default-soft); border-radius: 4px; overflow: hidden; margin-top: 8px; }
.bar.big { height: 10px; }
.bar span { display: block; height: 100%; background: var(--vp-c-brand-1); }
.note { font-size: 14px; color: var(--vp-c-text-2); }
</style>
