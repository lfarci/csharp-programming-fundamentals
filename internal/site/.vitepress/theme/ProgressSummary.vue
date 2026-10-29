<script setup lang="ts">
// The progress card (total, bar, next exercise). Same look as the roadmap cards.
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load } from './progress'

defineProps<{ sync?: boolean }>()
onMounted(load)
const total = computed(() => course.exercises.filter((e) => done.value[e.id]).length)
const all = course.exercises.length
const next = computed(() => course.exercises.find((e) => !done.value[e.id]))
</script>

<template>
  <div class="cpf-card summary">
    <div class="cpf-kicker">Your progress</div>
    <div class="big"><strong>{{ total }} of {{ all }}</strong> exercises done</div>
    <div class="cpf-bar thick" role="img" :aria-label="`${total} of ${all} done`"><span :style="{ width: (100 * total / all) + '%' }"></span></div>
    <div class="row">
      <a v-if="next" class="cpf-button" :href="withBase(next.link)">Next: {{ next.id }} {{ next.title }}</a>
      <span v-else>Everything is done. Well done.</span>
      <a v-if="sync" class="side" :href="withBase('/progress')">Sync with the terminal, backup</a>
    </div>
  </div>
</template>

<style scoped>
.summary { margin: 16px 0 24px; padding: 18px 20px; }
.big { font-size: 20px; margin: 2px 0 10px; color: var(--vp-c-text-1); }
.row { display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center; margin-top: 14px; font-size: 14px; }
.side { font-size: 14px; }
</style>
