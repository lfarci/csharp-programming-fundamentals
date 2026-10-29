<script setup lang="ts">
// The exercises of one theme (or one group of it), with a done tick from the browser store (same as "Mark as done").
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load, setDone } from './progress'

const props = defineProps<{ theme: string; group?: string }>()
onMounted(load)
const list = computed(() => course.exercises.filter((e) => e.theme === props.theme && (!props.group || e.group === props.group)))
const n = computed(() => list.value.filter((e) => done.value[e.id]).length)
</script>

<template>
  <div class="theme-ex cpf-card" :data-group="group || null">
    <div class="head">
      <p class="count"><strong>{{ n }} of {{ list.length }}</strong> done</p>
      <span class="cpf-bar" aria-hidden="true"><span :style="{ width: (list.length ? 100 * n / list.length : 0) + '%' }"></span></span>
    </div>
    <ol class="rows">
      <li v-for="e in list" :key="e.id" :class="{ isdone: done[e.id] }">
        <input type="checkbox" :checked="!!done[e.id]" :aria-label="`Mark ${e.id} as done`"
          @change="setDone(e.id, ($event.target as HTMLInputElement).checked)" />
        <a :href="withBase(e.link)">{{ e.title }}</a>
        <span class="id">{{ e.id }}</span>
        <span v-if="e.kind !== 'write code'" class="tag">{{ e.kind }}</span>
        <span class="level">{{ e.level }}</span>
      </li>
    </ol>
  </div>
</template>

<style scoped>
.theme-ex { padding: 0; overflow: hidden; margin: 16px 0; }
.head { display: flex; align-items: center; gap: 16px; padding: 14px 18px; border-bottom: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft); }
.count { margin: 0; white-space: nowrap; color: var(--vp-c-text-2); font-size: 14px; }
.head .cpf-bar { flex: 1; }
.rows { list-style: none; padding: 0; margin: 0; }
.rows li { display: flex; align-items: center; gap: 12px; padding: 9px 18px; margin: 0; border-top: 1px solid var(--vp-c-divider); font-size: 15px; }
.rows li:first-child { border-top: none; }
.rows input { width: 16px; height: 16px; accent-color: var(--vp-c-brand-1); cursor: pointer; flex: none; }
.rows a { font-weight: 500; text-decoration: none; }
.rows a:hover { text-decoration: underline; }
.isdone a { color: var(--vp-c-text-2); text-decoration: line-through; text-decoration-color: var(--vp-c-text-3); }
.id { font-family: var(--vp-font-family-mono); font-size: 12px; color: var(--vp-c-text-3); }
.tag { font-size: 12px; padding: 0 6px; border: 1px solid var(--vp-c-divider); border-radius: 4px; color: var(--vp-c-text-2); }
.level { margin-left: auto; font-size: 12px; color: var(--vp-c-text-2); background: var(--vp-c-default-soft); border-radius: 10px; padding: 1px 10px; white-space: nowrap; }
@media (max-width: 640px) { .id { display: none; } }
</style>
