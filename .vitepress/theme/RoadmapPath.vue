<script setup lang="ts">
// The roadmap as a vertical path of theme cards, with progress from the browser store.
import { computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, load } from './progress'
import { inline } from './inline'

onMounted(load)
const parts = computed(() => {
  const out: { name: string; themes: any[] }[] = []
  course.themes.forEach((t, i) => {
    const list = course.exercises.filter((e) => e.theme === t.slug)
    const row = { ...t, num: i + 1, total: list.length, n: list.filter((e) => done.value[e.id]).length }
    const last = out[out.length - 1]
    if (last && last.name === t.part) last.themes.push(row)
    else out.push({ name: t.part, themes: [row] })
  })
  return out
})
</script>

<template>
  <div class="path">
    <section v-for="p in parts" :key="p.name" class="part">
      <div class="cpf-kicker part-kicker">{{ p.name.split(': ')[0] }}</div>
      <h2 :id="p.name.split(': ')[1].toLowerCase().replace(/ /g, '-')" class="part-name">{{ p.name.split(': ')[1] }}</h2>
      <ol class="steps">
        <li v-for="t in p.themes" :key="t.slug" :class="{ complete: t.total && t.n === t.total }">
          <span class="dot" aria-hidden="true">{{ t.num }}</span>
          <a class="card" :href="withBase(t.link)">
            <span class="title">{{ t.title }}</span>
            <span class="sum" v-html="inline(t.summary)"></span>
            <span class="meta">{{ t.n }} of {{ t.total }} exercise{{ t.total === 1 ? '' : 's' }} done
              <span class="bar" aria-hidden="true"><span :style="{ width: (t.total ? 100 * t.n / t.total : 0) + '%' }"></span></span>
            </span>
          </a>
        </li>
      </ol>
    </section>
  </div>
</template>

<style scoped>
.part-kicker { margin-top: 32px; }
.part-name { border-top: none; margin: 2px 0 10px; padding-top: 0; font-size: 20px; color: var(--vp-c-brand-1); }
.steps { list-style: none; padding: 0; margin: 0; position: relative; }
.steps li { position: relative; padding-left: 52px; margin: 0 0 12px; }
.steps li::before { content: ''; position: absolute; left: 17px; top: 36px; bottom: -14px; width: 2px; background: var(--vp-c-divider); }
.steps li:last-child::before { display: none; }
.dot { position: absolute; left: 0; top: 10px; width: 36px; height: 36px; border-radius: 50%; border: 2px solid var(--vp-c-brand-1);
  background: var(--vp-c-bg); color: var(--vp-c-brand-1); font-weight: 700; display: flex; align-items: center; justify-content: center; font-size: 14px; }
.complete .dot { background: var(--vp-c-brand-1); color: #fff; }
.card { display: block; border: 1px solid var(--vp-c-divider); border-radius: 12px; padding: 12px 16px; text-decoration: none !important; color: inherit !important; transition: border-color .2s, box-shadow .2s; }
.card:hover { border-color: var(--vp-c-brand-1); box-shadow: 0 4px 16px rgba(52, 81, 178, .10); }
.title { display: block; font-weight: 600; font-size: 16px; color: var(--vp-c-text-1); }
.sum { display: block; font-size: 14px; color: var(--vp-c-text-2); margin-top: 2px; }
.meta { display: flex; align-items: center; gap: 12px; font-size: 13px; color: var(--vp-c-text-3); margin-top: 8px; }
.bar { flex: 0 0 120px; height: 6px; border-radius: 3px; background: var(--vp-c-default-soft); overflow: hidden; }
.bar span { display: block; height: 100%; background: var(--vp-c-brand-1); }
</style>
