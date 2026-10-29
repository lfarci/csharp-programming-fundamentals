<script setup lang="ts">
import ProgressSummary from './ProgressSummary.vue'
import { computed, onMounted, ref } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'
import { done, encode, exportJson, importText, load, setDone, storageOk } from './progress'

onMounted(load)
const all = course.exercises
const count = computed(() => all.filter((e) => done.value[e.id]).length)
const themes = computed(() => course.themes.map((t) => {
  const list = all.filter((e) => e.theme === t.slug)
  return { theme: t.title, link: t.link, list, n: list.filter((e) => done.value[e.id]).length }
}))
const drills = computed(() => course.drillSets.map((d) => ({ ...d, n: d.ids.filter((id) => done.value[id]).length })))
const next = computed(() => all.find((e) => !done.value[e.id]))
const byId = Object.fromEntries(all.map((e) => [e.id, e]))
const code = computed(() => encode(Object.keys(done.value)))
const input = ref('')
const message = ref('')

function doImport() {
  try {
    const r = importText(input.value)
    message.value = `Imported: ${r.added} new exercise(s) marked as done.` + (r.unknown.length ? ` Unknown IDs ignored: ${r.unknown.join(', ')}.` : '')
    input.value = ''
  } catch (e: any) {
    message.value = 'Not imported: ' + e.message
  }
}
function download() {
  const a = document.createElement('a')
  a.href = URL.createObjectURL(new Blob([exportJson()], { type: 'application/json' }))
  a.download = `csharp-fundamentals-progress-${new Date().toISOString().slice(0, 10)}.json`
  a.click()
  setTimeout(() => URL.revokeObjectURL(a.href), 1000)
}
function copy() { navigator.clipboard?.writeText(code.value); message.value = 'Sync code copied.' }
</script>

<template>
  <div class="progress">
    <ProgressSummary />
    <p v-if="!storageOk" class="warn">This browser does not let the site save progress. Export a backup before you close the tab.</p>

    <h2 id="sync-with-the-terminal">Sync with the terminal</h2>
    <div class="cpf-card box">
    <p>In your copy of the course, run <code>./ex progress</code>. Its last line is a <strong>sync code</strong> like <code>CPF1:A1-4,7;L3</code>.
      Paste it here to mark the exercises that passed <code>./ex check</code>. Import only adds: it never removes a tick.</p>
    <textarea v-model="input" rows="3" placeholder="CPF1:... or a JSON backup" aria-label="Sync code or JSON backup"></textarea>
    <p><button @click="doImport" :disabled="!input.trim()">Import</button></p>
    <p v-if="message" role="status">{{ message }}</p>
    </div>

    <h2 id="by-theme">By theme</h2>
    <div class="themes">
      <div v-for="(s, i) in themes" :key="s.theme" class="cpf-card th">
        <div class="th-head">
          <span class="cpf-num" :class="{ on: s.n === s.list.length }" aria-hidden="true">{{ i + 1 }}</span>
          <a class="th-title" :href="withBase(s.link)">{{ s.theme }}</a>
          <span class="th-n">{{ s.n }} of {{ s.list.length }}</span>
        </div>
        <span class="cpf-bar" aria-hidden="true"><span :style="{ width: (100 * s.n / s.list.length) + '%' }"></span></span>
        <div class="chips"><span v-for="e in s.list" :key="e.id" class="chip" :class="{ on: done[e.id] }">
          <a :href="withBase(e.link)" :title="e.title">{{ e.id }}</a>{{ done[e.id] ? ' done' : '' }}</span></div>
      </div>
    </div>

    <h2 id="by-drill-set">By drill set</h2>
    <table>
      <thead><tr><th>Drill set</th><th>Done</th><th>Exercises</th></tr></thead>
      <tbody>
        <tr v-for="d in drills" :key="d.name">
          <td>{{ d.name }}</td><td>{{ d.n }} of {{ d.ids.length }}</td>
          <td><span v-for="id in d.ids" :key="id" class="chip" :class="{ on: done[id] }">
            <a :href="withBase(byId[id].link)" :title="byId[id].title">{{ id }}</a>{{ done[id] ? ' done' : '' }}</span></td>
        </tr>
      </tbody>
    </table>

    <h2 id="backup">Backup</h2>
    <div class="cpf-card box">
    <p>Your sync code for this browser: <code>{{ code }}</code> <button @click="copy">Copy</button></p>
    <p><button @click="download">Download a JSON backup</button> Use it to move your progress to another browser (Import above accepts it).</p>
    <p class="note">Progress is saved in this browser only (localStorage). The real check is always <code>./ex check</code> in your own copy: the site does not run C#.</p>
    <details><summary>Clear all ticks</summary>
      <p><button @click="Object.keys(done).forEach((id) => setDone(id, false))">Yes, clear every tick in this browser</button></p>
    </details>
    </div>
  </div>
</template>

<style scoped>
.box { padding: 4px 18px 12px; }
.themes { display: grid; gap: 12px; }
.th-head { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
.th-title { font-weight: 600; text-decoration: none; }
.th-n { margin-left: auto; font-size: 13px; color: var(--vp-c-text-3); white-space: nowrap; }
.chips { margin-top: 10px; }
.chip { display: inline-block; margin: 2px 6px 2px 0; padding: 0 6px; border: 1px solid var(--vp-c-divider); border-radius: 4px; font-size: 13px; }
.chip a { text-decoration: none; }
.chip.on { background: var(--vp-c-brand-soft); border-color: var(--vp-c-brand-1); font-weight: 600; }
textarea { width: 100%; font-family: var(--vp-font-family-mono); border: 1px solid var(--vp-c-divider); border-radius: 6px; padding: 8px; }
button { border: 1px solid var(--vp-c-brand-1); color: var(--vp-c-brand-1); border-radius: 20px; padding: 3px 14px; margin-right: 8px; font-weight: 600; font-size: 14px; }
button:hover:not(:disabled) { background: var(--vp-c-brand-soft); }
button:disabled { opacity: .5; }
.warn { color: var(--vp-c-danger-1); }
.note { color: var(--vp-c-text-2); }
</style>
