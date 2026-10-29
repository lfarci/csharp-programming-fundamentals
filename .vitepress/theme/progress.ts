// Progress in the browser (localStorage), like csharp-quest-tracker: one versioned key,
// a backup you can export, and an import that only adds. The real check is ./ex check.
import { ref } from 'vue'
import course from '../course.json'
import { decode } from './sync-code'
export { encode, decode } from './sync-code'

export const KEY = 'csharp-programming-fundamentals:progress:v1'
export type Done = Record<string, string> // exercise ID -> date (YYYY-MM-DD)
const known = new Set(course.exercises.map((e) => e.id))

export const done = ref<Done>({})
export const storageOk = ref(true)

export function load() {
  if (typeof window === 'undefined') return
  try {
    const raw = window.localStorage.getItem(KEY)
    const data = raw ? JSON.parse(raw) : { done: {} }
    done.value = Object.fromEntries(Object.entries(data.done ?? {}).filter(([id]) => known.has(id))) as Done
  } catch {
    storageOk.value = false
  }
}

function save() {
  try {
    window.localStorage.setItem(KEY, JSON.stringify({ schemaVersion: 1, done: done.value }))
    storageOk.value = true
  } catch {
    storageOk.value = false
  }
}

const today = () => new Date().toISOString().slice(0, 10)

export function setDone(id: string, value: boolean) {
  const next = { ...done.value }
  if (value) next[id] = next[id] ?? today()
  else delete next[id]
  done.value = next
  save()
}

/** Import a sync code or a JSON backup. Only adds exercises; returns how many were new. */
export function importText(text: string): { added: number; unknown: string[] } {
  const t = text.trim()
  let ids: string[]
  let dates: Done = {}
  if (t.startsWith('{')) {
    const data = JSON.parse(t)
    dates = data.done ?? {}
    ids = Object.keys(dates)
  } else ids = decode(t)
  const unknown = ids.filter((id) => !known.has(id))
  const next = { ...done.value }
  let added = 0
  for (const id of ids)
    if (known.has(id) && !next[id]) {
      next[id] = dates[id] || today()
      added++
    }
  done.value = next
  save()
  return { added, unknown }
}

export function exportJson(): string {
  return JSON.stringify({ schemaVersion: 1, exportedAt: new Date().toISOString(), done: done.value }, null, 1)
}
