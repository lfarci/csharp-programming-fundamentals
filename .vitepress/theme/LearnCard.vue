<script setup lang="ts">
// "Before you start" card of a theme page: one video to watch, one module to read, then the first exercise.
// Everything else stays collapsed under "More on Microsoft Learn". Data: course.json `learn` (tools/generator/learn.py).
import { computed } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'

const props = defineProps<{ theme: string }>()
const c = computed(() => (course as any).learn[props.theme])
const hasMore = computed(() => c.value.more.modules.length + c.value.more.videos.length + c.value.more.docs.length > 0)
</script>

<template>
  <section class="cpf-card learn-card" aria-label="Before you start">
    <div class="cpf-kicker">Before you start</div>
    <ol class="steps">
      <li>
        <span class="cpf-num" aria-hidden="true">1</span>
        <span class="body"><span class="verb">Watch</span>
          <a :href="withBase(c.watch.link)">{{ c.watch.title }}</a>
          <span class="meta">Video, {{ c.watch.minutes }} min</span></span>
      </li>
      <li>
        <span class="cpf-num" aria-hidden="true">2</span>
        <span class="body"><span class="verb">Read</span>
          <a :href="c.read.url">{{ c.read.title }}</a>
          <span class="meta">Microsoft Learn, Part {{ c.read.part }}</span></span>
      </li>
      <li>
        <span class="cpf-num on" aria-hidden="true">3</span>
        <span class="body"><span class="verb">Then practise</span>
          <a class="cpf-button" :href="withBase(c.first.link)">Start {{ c.first.id }} · {{ c.first.title }}</a></span>
      </li>
    </ol>
    <details v-if="hasMore" class="more">
      <summary>More on Microsoft Learn</summary>
      <ul>
        <li v-for="m in c.more.modules" :key="m.url"><a :href="m.url">{{ m.title }}</a> <span class="meta">Part {{ m.part }}</span></li>
        <li v-for="v in c.more.videos" :key="v.link"><a :href="withBase(v.link)">{{ v.title }}</a> <span class="meta">Video</span></li>
        <li v-for="d in c.more.docs" :key="d.url"><a :href="d.url">{{ d.title }}</a> <span class="meta">Reference</span></li>
      </ul>
    </details>
  </section>
</template>

<style scoped>
.learn-card { margin: 20px 0 8px; padding: 16px 20px; }
.steps { list-style: none; padding: 0; margin: 10px 0 0; display: grid; gap: 12px; }
.steps li { display: flex; gap: 14px; align-items: center; margin: 0; }
.body { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 10px; }
.verb { font-weight: 700; color: var(--vp-c-text-1); min-width: 110px; }
.body a:not(.cpf-button) { font-weight: 500; }
.meta { font-size: 13px; color: var(--vp-c-text-3); }
.more { margin-top: 14px; border-top: 1px solid var(--vp-c-divider); padding-top: 10px; font-size: 14px; }
.more summary { cursor: pointer; color: var(--vp-c-text-2); font-weight: 500; }
.more ul { margin: 8px 0 0; padding-left: 18px; }
.more li { margin: 4px 0; }
</style>
