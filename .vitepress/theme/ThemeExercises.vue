<script setup lang="ts">
// The exercises of one theme, with a done tick from the browser store (same as "Mark as done").
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load, setDone } from './progress'

const props = defineProps<{ theme: string }>()
onMounted(load)
const list = computed(() => course.exercises.filter((e) => e.theme === props.theme))
const n = computed(() => list.value.filter((e) => done.value[e.id]).length)
</script>

<template>
  <div class="theme-ex">
    <p class="count"><strong>{{ n }} of {{ list.length }}</strong> done</p>
    <table>
      <thead><tr><th>Done</th><th>ID</th><th>Exercise</th><th>Level</th></tr></thead>
      <tbody>
        <tr v-for="e in list" :key="e.id" :class="{ isdone: done[e.id] }">
          <td><input type="checkbox" :checked="!!done[e.id]" :aria-label="`Mark ${e.id} as done`"
              @change="setDone(e.id, ($event.target as HTMLInputElement).checked)" /></td>
          <td class="id">{{ e.id }}</td>
          <td><a :href="withBase(e.link)">{{ e.title }}</a><span v-if="e.paper" class="tag">paper</span></td>
          <td>{{ e.level }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.count { margin: 0 0 8px; color: var(--vp-c-text-2); }
.theme-ex table { display: table; width: 100%; margin: 0; }
.theme-ex td, .theme-ex th { padding: 6px 12px; }
.theme-ex input { transform: scale(1.2); cursor: pointer; }
.id { font-family: var(--vp-font-family-mono); font-size: 13px; color: var(--vp-c-text-2); }
.isdone a { color: var(--vp-c-text-2); }
.tag { margin-left: 8px; font-size: 12px; padding: 0 6px; border: 1px solid var(--vp-c-divider); border-radius: 4px; color: var(--vp-c-text-2); }
</style>
