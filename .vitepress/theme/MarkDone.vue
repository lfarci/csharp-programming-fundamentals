<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useRoute, withBase } from 'vitepress'
import course from '../course.json'
import { done, load, setDone, storageOk } from './progress'

const route = useRoute()
const ex = computed(() => course.exercises.find((e) => route.path.endsWith(e.link)))
onMounted(load)
</script>

<template>
  <div v-if="ex" class="mark-done">
    <label>
      <input type="checkbox" :checked="!!done[ex.id]" @change="setDone(ex.id, ($event.target as HTMLInputElement).checked)" />
      Mark {{ ex.id }} as done
    </label>
    <span v-if="done[ex.id]" class="when">(done on {{ done[ex.id] }})</span>
    <p class="note">
      <template v-if="ex.paper">Paper exercise: tick it when your answer matches the answer key.</template>
      <template v-else>Tick it when <code>./ex check {{ ex.id }}</code> says DONE in your copy of the course. This site does not run C#.</template>
      Saved in this browser only. See <a :href="withBase('/progress')">My progress</a>.
    </p>
    <p v-if="!storageOk" class="warn">Progress cannot be saved in this browser. Export a backup from My progress.</p>
  </div>
</template>

<style scoped>
.mark-done { border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 10px 14px; margin: 0 0 20px; }
.mark-done label { font-weight: 600; cursor: pointer; }
.mark-done input { margin-right: 6px; transform: scale(1.2); }
.when { margin-left: 8px; color: var(--vp-c-text-2); }
.note { margin: 6px 0 0; font-size: 14px; color: var(--vp-c-text-2); }
.warn { color: var(--vp-c-danger-1); }
</style>
