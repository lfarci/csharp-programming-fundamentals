<script setup lang="ts">
// The header card of an exercise page: where you are (theme > group, exercise N of M), level, recipe,
// what to do first, and the "Mark as done" tick. Same look as the roadmap cards.
import { computed, onMounted } from 'vue'
import { useRoute, withBase } from 'vitepress'
import course from '../course.json'
import { done, load, setDone, storageOk } from './progress'

const route = useRoute()
const ex = computed(() => course.exercises.find((e) => route.path.replace(/\.html$/, '').endsWith(e.link)))
const theme = computed(() => course.themes.find((t) => t.slug === ex.value?.theme))
const group = computed(() => theme.value?.groups.find((g) => g.slug === ex.value?.group))
onMounted(load)
</script>

<template>
  <div v-if="ex && theme && group" class="cpf-card ex-head">
    <div class="top">
      <span class="cpf-kicker"><a :href="withBase(theme.link)">{{ theme.title }}</a> › <a :href="withBase(group.link)">{{ group.title }}</a></span>
      <span class="pos">Exercise {{ ex.pos }} of {{ ex.of }}</span>
    </div>
    <span class="cpf-bar" aria-hidden="true"><span :style="{ width: (100 * ex.pos / ex.of) + '%' }"></span></span>
    <dl class="facts">
      <div><dt>Level</dt><dd><span class="badge">{{ ex.level }}</span> {{ ex.effort }}</dd></div>
      <div><dt>Kind</dt><dd>{{ ex.kind }}</dd></div>
      <div v-if="ex.recipes.length"><dt>Lesson</dt><dd><template v-for="(r, i) in ex.recipes" :key="r.link"><span v-if="i">, </span><a :href="withBase(r.link)">{{ r.title }}</a></template></dd></div>
      <div v-if="ex.pre.length"><dt>Do first</dt><dd><template v-for="(p, i) in ex.pre" :key="p.id"><span v-if="i">, </span><a :href="withBase(p.link)">{{ p.id }}</a></template></dd></div>
    </dl>
    <div class="done">
      <label>
        <input type="checkbox" :checked="!!done[ex.id]" @change="setDone(ex.id, ($event.target as HTMLInputElement).checked)" />
        Mark {{ ex.id }} as done
      </label>
      <span v-if="done[ex.id]" class="when">(done on {{ done[ex.id] }})</span>
      <span class="note">
        <template v-if="ex.paper">Tick it when your answer matches the answer key.</template>
        <template v-else>Tick it when <code>./ex check {{ ex.id }}</code> says DONE.</template>
        Saved in this browser. <a :href="withBase('/progress')">My progress</a>
      </span>
      <p v-if="!storageOk" class="warn">Progress cannot be saved in this browser. Export a backup from My progress.</p>
    </div>
  </div>
</template>

<style scoped>
.ex-head { margin: 16px 0 24px; padding: 14px 18px; }
.top { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 6px 16px; align-items: baseline; margin-bottom: 8px; }
.cpf-kicker a { color: inherit; text-decoration: none; }
.cpf-kicker a:hover { text-decoration: underline; }
.pos { font-size: 14px; font-weight: 600; color: var(--vp-c-text-2); }
.facts { display: flex; flex-wrap: wrap; gap: 8px 28px; margin: 12px 0 0; }
.facts div { margin: 0; }
.facts dt { font-size: 12px; color: var(--vp-c-text-3); margin: 0; }
.facts dd { margin: 0; font-size: 14px; }
.badge { font-size: 12px; background: var(--vp-c-default-soft); border-radius: 10px; padding: 1px 10px; }
.done { margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--vp-c-divider); display: flex; flex-wrap: wrap; gap: 4px 12px; align-items: baseline; }
.done label { font-weight: 600; cursor: pointer; }
.done input { margin-right: 6px; transform: scale(1.2); accent-color: var(--vp-c-brand-1); }
.when { color: var(--vp-c-text-2); font-size: 14px; }
.note { font-size: 13px; color: var(--vp-c-text-2); }
.warn { color: var(--vp-c-danger-1); margin: 4px 0 0; }
</style>
