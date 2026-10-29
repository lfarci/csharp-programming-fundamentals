<script setup lang="ts">
// The groups of a theme as numbered cards with their completion (Roadmap look). Each card opens its group page;
// the card keeps the group slug as id, so old links like /themes/loops#count still land on it.
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load } from './progress'

const props = defineProps<{ theme: string }>()
onMounted(load)
const t = computed(() => course.themes.find((x) => x.slug === props.theme)!)
const num = computed(() => course.themes.findIndex((x) => x.slug === props.theme) + 1)
const rows = computed(() => t.value.groups.map((g, i) => {
  const list = course.exercises.filter((e) => e.theme === props.theme && e.group === g.slug)
  return { ...g, num: `${num.value}.${i + 1}`, total: list.length, n: list.filter((e) => done.value[e.id]).length }
}))
</script>

<template>
  <ol class="groups">
    <li v-for="g in rows" :key="g.slug" :id="g.slug">
      <a class="cpf-card cpf-link item" :href="withBase(g.link)">
        <span class="cpf-num" :class="{ on: g.total && g.n === g.total }" aria-hidden="true">{{ g.num }}</span>
        <span class="body"><span class="title">{{ g.title }}</span>
          <span class="about">{{ g.total }} exercises</span>
          <span class="meta"><span class="n">{{ g.n }} / {{ g.total }}</span>
            <span class="cpf-bar" role="img" :aria-label="`${g.n} of ${g.total} done`"><span :style="{ width: (g.total ? 100 * g.n / g.total : 0) + '%' }"></span></span></span></span>
      </a>
    </li>
  </ol>
</template>

<style scoped>
.groups { list-style: none; padding: 0; margin: 12px 0 8px; display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; }
.groups li { margin: 0; }
.item { display: flex; gap: 12px; align-items: center; height: 100%; padding: 10px 14px; }
.cpf-num { width: 40px; height: 40px; font-size: 13px; }
.body { flex: 1; min-width: 0; }
.title { display: block; font-weight: 600; font-size: 15px; color: var(--vp-c-text-1); }
.meta { display: flex; align-items: center; gap: 8px; margin-top: 4px; font-size: 12px; color: var(--vp-c-text-3); }
.about { display: block; font-size: 12px; color: var(--vp-c-text-2); }
.n { white-space: nowrap; }
.meta .cpf-bar { flex: 1; }
</style>
