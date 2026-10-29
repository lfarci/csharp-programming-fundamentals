// Checks the website sync code: round trip, and the exact format ./ex progress prints.
import assert from 'node:assert/strict'
import { encode, decode } from '../site/.vitepress/theme/sync-code.ts'

assert.equal(encode(['A01', 'A02', 'A03', 'A04', 'A07', 'B01', 'B02', 'B03', 'L11']), 'CPF1:A1-4,7;B1-3;L11')
assert.deepEqual(decode('CPF1:A1-4,7;B1-3;L11'), ['A01', 'A02', 'A03', 'A04', 'A07', 'B01', 'B02', 'B03', 'L11'])
assert.deepEqual(decode(' cpf1:l11 '), ['L11'])
assert.equal(encode([]), 'CPF1:')
assert.deepEqual(decode('CPF1:'), [])
assert.throws(() => decode('hello'))
const ids = ['A10', 'A11', 'A09', 'G01', 'S01']
assert.deepEqual(decode(encode(ids)), [...ids].sort())
console.log('OK: website sync code (encode, decode, same format as ./ex progress)')
