// Pure functions, shared format with ./ex progress (tools/ex/Program.cs, SyncCode). Tested by tools/check-site-sync.ts.
// Sync code: "CPF1:A1-4,7;B1-3" = A01..A04, A07, B01..B03. ./ex progress prints the same format.
export function encode(ids: string[]): string {
  const fam: Record<string, number[]> = {}
  for (const id of [...ids].sort()) (fam[id[0]] ??= []).push(Number(id.slice(1)))
  const parts = Object.entries(fam).map(([f, ns]) => {
    const out: string[] = []
    for (let i = 0; i < ns.length; i++) {
      let j = i
      while (j + 1 < ns.length && ns[j + 1] === ns[j] + 1) j++
      out.push(j > i ? `${ns[i]}-${ns[j]}` : `${ns[i]}`)
      i = j
    }
    return f + out.join(',')
  })
  return 'CPF1:' + parts.join(';')
}

export function decode(code: string): string[] {
  const m = code.trim().match(/^CPF1:(.*)$/i)
  if (!m) throw new Error('This is not a sync code. It starts with CPF1:')
  const ids: string[] = []
  for (const part of m[1].split(';').map((p) => p.trim()).filter(Boolean)) {
    const f = part[0].toUpperCase()
    for (const r of part.slice(1).split(',')) {
      const [a, b] = r.split('-').map(Number)
      if (!Number.isInteger(a) || (b !== undefined && !Number.isInteger(b))) throw new Error(`Cannot read "${part}".`)
      for (let n = a; n <= (b ?? a); n++) ids.push(f + String(n).padStart(2, '0'))
    }
  }
  return ids
}

