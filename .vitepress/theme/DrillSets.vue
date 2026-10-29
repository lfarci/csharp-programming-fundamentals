<script setup lang="ts">
// The drill sets as numbered cards: one recipe, its exercises in order, with done ticks (Roadmap look).
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load } from './progress'

onMounted(load)
const files: Record<string, string> = Object.fromEntries((course as any).recipes.map((r: any) => [String(r.num).padStart(2, '0'), r.link]))
const sets = computed(() => course.drillSets.map((d, i) => {
  const list = d.ids.map((id) => course.exercises.find((e) => e.id === id)!)
  return { ...d, num: i + 1, list, n: list.filter((e) => done.value[e.id]).length, recipeLink: files[d.recipe] }
}))
</script>

<template>
  <ol class="sets">
    <li v-for="s in sets" :key="s.name" class="cpf-card set">
      <span class="cpf-num" :class="{ on: s.n === s.list.length }" aria-hidden="true">{{ s.num }}</span>
      <div class="body">
        <div class="head"><span class="title">{{ s.name }}</span>
          <a class="recipe" :href="withBase(s.recipeLink)">Lesson: recipe {{ Number(s.recipe) }}</a>
          <span class="n">{{ s.n }} / {{ s.list.length }}</span></div>
        <ol class="chips">
          <li v-for="e in s.list" :key="e.id"><a :href="withBase(e.link)" :class="{ on: done[e.id] }" :title="e.title">{{ e.id }}<span class="sr"> {{ e.title }}{{ done[e.id] ? ', done' : '' }}</span></a></li>
        </ol>
      </div>
    </li>
  </ol>
</template>

<style scoped>
.sets { list-style: none; padding: 0; margin: 16px 0; display: grid; gap: 10px; }
.set { display: flex; gap: 14px; align-items: flex-start; margin: 0; }
.body { flex: 1; min-width: 0; }
.head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px; }
.title { font-weight: 600; font-size: 15px; color: var(--vp-c-text-1); }
.recipe { font-size: 13px; }
.n { margin-left: auto; font-size: 13px; color: var(--vp-c-text-3); }
.chips { list-style: none; padding: 0; margin: 8px 0 0; display: flex; flex-wrap: wrap; gap: 6px; }
.chips li { margin: 0; }
.chips a { display: inline-block; font-family: var(--vp-font-family-mono); font-size: 12px; padding: 2px 8px; border: 1px solid var(--vp-c-divider); border-radius: 10px; text-decoration: none; color: var(--vp-c-text-1); }
.chips a:hover { border-color: var(--vp-c-brand-1); }
.chips a.on { background: var(--vp-c-brand-1); border-color: var(--vp-c-brand-1); color: #fff; }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
</style>
