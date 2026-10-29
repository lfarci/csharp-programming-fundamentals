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
  return { ...t, num: i + 1, total: list.length, n: list.filter((e) => done.value[e.id]).length }
}))
</script>

<template>
  <div class="overview">
    <ProgressSummary sync />
    <ol class="grid">
      <li v-for="r in rows" :key="r.slug">
        <a class="cpf-card cpf-link item" :href="withBase(r.link)">
          <span class="cpf-num" :class="{ on: r.total && r.n === r.total }" aria-hidden="true">{{ r.num }}</span>
          <span class="body">
            <span class="title">{{ r.title }}</span>
            <span class="meta"><span class="n">{{ r.n }} / {{ r.total }}</span>
              <span class="cpf-bar" role="img" :aria-label="`${r.n} of ${r.total} done`"><span :style="{ width: (r.total ? 100 * r.n / r.total : 0) + '%' }"></span></span></span>
          </span>
        </a>
      </li>
    </ol>
    <p class="note">Ticks are saved in this browser. The real check is <code>./ex check</code> in your copy of the course.</p>
  </div>
</template>

<style scoped>
.grid { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 12px; }
.grid li { margin: 0; }
.item { display: flex; gap: 14px; align-items: center; height: 100%; }
.body { flex: 1; min-width: 0; }
.title { display: block; font-weight: 600; font-size: 15px; color: var(--vp-c-text-1); line-height: 1.35; }
.meta { display: flex; align-items: center; gap: 10px; margin-top: 6px; font-size: 13px; color: var(--vp-c-text-3); }
.n { white-space: nowrap; min-width: 44px; }
.meta .cpf-bar { flex: 1; }
.note { font-size: 14px; color: var(--vp-c-text-2); }
</style>
