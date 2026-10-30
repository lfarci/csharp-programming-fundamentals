#!/usr/bin/env bash
# End-to-end test of ./ex, the way the learner uses it, on a fresh copy of the repo:
# start -> check fails (NOT YET) -> write the solution -> check passes (DONE) -> progress -> next.
set -euo pipefail
cd "$(dirname "$0")/../.."  # the repo root
tmp=$(mktemp -d)
git ls-files -z | xargs -0 -I{} cp --parents {} "$tmp"
cd "$tmp"
# a git repo, like a real clone (./ex check warns about changes outside practice/)
git init -q && echo out.txt >> .git/info/exclude && git add -A && git -c user.name=check -c user.email=check@example.com commit -qm "fresh clone"
fail() { echo "FAIL: $1"; echo "--- output:"; cat out.txt; exit 1; }

mkdir -p tests/Practice.Tests/obj tools/ex/bin && touch tests/Practice.Tests/obj/x tools/ex/bin/x  # build output left by the old layout
./ex list > out.txt                      || fail "./ex list"
test ! -e tests && test ! -e tools       || fail "./ex did not remove the old build folders tests/ and tools/"
grep -q "L11  Count from a to b" out.txt  || fail "./ex list does not show L11"

./ex start L11 > out.txt                 || fail "./ex start L11"
test -f practice/L11_CountFromAToB.cs    || fail "./ex start did not create the file"
./ex start L11 > out.txt                 || fail "./ex start L11 (again)"
grep -q "kept as it is" out.txt          || fail "./ex start must never overwrite"

if ./ex check > out.txt; then fail "./ex check must fail before any code is written"; fi
grep -q "NOT YET  example 1 of 4" out.txt || fail "./ex check does not say NOT YET"
grep -q "Hint:" out.txt                   || fail "./ex check gives no hint"

cp internal/solutions/L11_CountFromAToB.cs practice/  # the learner writes the code
./ex check > out.txt                      || fail "./ex check must pass with the solution"
grep -q "DONE: all 4 examples are OK" out.txt || fail "./ex check does not say DONE"
grep -q "^L11 " practice/.done            || fail "./ex check did not save L11 as done"

grep -q "WARNING" out.txt && fail "./ex check warns although only practice/ changed"
echo "a mistake" >> course/docs/glossary.md   # the learner edits a course page by mistake
./ex check L11 > out.txt                  || fail "a changed course file must not make ./ex check fail"
grep -q "WARNING: 1 file outside practice/ changed" out.txt || fail "./ex check does not warn about a change outside practice/"
grep -q "course/docs/glossary.md" out.txt  || fail "the warning does not name the changed file"
grep -q "git restore <path>" out.txt      || fail "the warning does not say how to undo"
git restore course/docs/glossary.md

./ex start A01 > out.txt && echo "int broken = ;" > practice/A01_Sum1ToN.cs
./ex check L11 > out.txt                  || fail "a broken A01 must not block ./ex check L11"
if ./ex check A01 > out.txt; then fail "./ex check A01 must fail on a compile error"; fi
grep -q "does not compile" out.txt        || fail "compile errors are not explained"
rm practice/A01_Sum1ToN.cs

./ex progress > out.txt                   || fail "./ex progress"
grep -q "Progress: 1 of" out.txt          || fail "./ex progress does not count L11"
grep -q "x L11" out.txt                   || fail "./ex progress does not mark L11 in its drill set"
grep -q "CPF1:L11$" out.txt               || fail "./ex progress does not print the sync code CPF1:L11"
test -f practice/PROGRESS.md              || fail "./ex progress did not write practice/PROGRESS.md"

./ex done L01 > out.txt                   || fail "./ex done L01 (paper)"
./ex next > out.txt                       || fail "./ex next"
grep -q "^Started " out.txt              || fail "./ex next did not start an exercise"
echo "OK: ./ex start, check (NOT YET, then DONE), progress, done and next work"
