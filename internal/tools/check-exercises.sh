#!/usr/bin/env bash
# Checks every exercise with its own test file (internal/tests/Practice.Tests/Exercises/<Exercise>Tests.cs):
# 1. Every non-paper exercise has a test file, and the reference solutions (internal/solutions/) pass ALL tests.
# 2. Every starter (internal/tools/starters/) compiles, and each exercise fails at least one test before any code is written.
# 3. One exercise builds alone, even when another practice file is broken (what ./ex check uses).
# 4. The ./ex tool works: list, start, check (NOT YET, then OK), progress.
set -euo pipefail
cd "$(dirname "$0")/../.."  # the repo root
root=$PWD
tmp=$(mktemp -d)
q=(-nologo -v q -clp:NoSummary)
run_tests() { dotnet "$1/Practice.Tests.dll" -noLogo -noColor -xml "$2" > "$2.log" 2>&1 || true; }

echo "Every exercise has a test file"
python3 - <<'PY'
import json, os, sys
missing = [e["id"] for e in json.load(open("internal/tools/exercises.json"))
           if e["kind"] != "paper" and not os.path.exists(f"internal/tests/Practice.Tests/Exercises/{e['class']}Tests.cs")]
if missing: sys.exit("FAIL: no test file for " + ", ".join(missing))
print("OK: every exercise has its test file")
PY

echo "Reference solutions pass every test"
dotnet build internal/tests/Practice.Tests "${q[@]}" -p:ExerciseProject="$root/internal/solutions/Solutions.csproj" -o "$tmp/sol"
run_tests "$tmp/sol" "$tmp/sol.xml"
python3 - "$tmp/sol.xml" <<'PY'
import json, sys, xml.etree.ElementTree as T
tests = list(T.parse(sys.argv[1]).getroot().iter("test"))
bad = [t.get("name") for t in tests if t.get("result") != "Pass"]
want = sum(len(e["cases"]) or len(e["examples"]) for e in json.load(open("internal/tools/exercises.json")) if e["kind"] != "paper")
if bad: sys.exit("FAIL: the reference solution does not pass:\n  " + "\n  ".join(bad))
if len(tests) != want: sys.exit(f"FAIL: {len(tests)} tests ran, {want} expected (a test file is missing or not compiled)")
print(f"OK: reference solutions pass all {len(tests)} tests")
PY

echo "Starters compile and fail before any code is written"
mkdir -p "$tmp/repo/internal/tools/ex"
cp -r practice "$tmp/repo/practice"; rm -rf "$tmp/repo/practice"/{bin,obj} "$tmp/repo/practice"/*_*.cs
cp internal/tools/ex/Runner.cs "$tmp/repo/internal/tools/ex/"
cp internal/tools/starters/*.cs "$tmp/repo/practice/"
dotnet build internal/tests/Practice.Tests "${q[@]}" -p:ExerciseProject="$tmp/repo/practice/Practice.csproj" -o "$tmp/start"
run_tests "$tmp/start" "$tmp/start.xml"
python3 - "$tmp/start.xml" <<'PY'
import sys, xml.etree.ElementTree as T, collections
res = collections.defaultdict(list)
for t in T.parse(sys.argv[1]).getroot().iter("test"):
    res[t.get("type")].append(t.get("result"))
weak = [c for c, r in res.items() if all(x == "Pass" for x in r)]
if weak: sys.exit("FAIL: these starters already pass all tests (add a case the starter fails): " + ", ".join(weak))
print(f"OK: {len(res)} starters compile and fail before the learner writes code")
PY

echo "One exercise at a time"
echo "int broken = ;" > "$tmp/repo/practice/A01_Sum1ToN.cs"
dotnet build internal/tests/Practice.Tests "${q[@]}" -p:ExerciseProject="$tmp/repo/practice/Practice.csproj" -p:OnlyExercise=A04_Factorial -o "$tmp/only" > "$tmp/only.log" 2>&1 || { cat "$tmp/only.log"; echo "FAIL: a broken file in another exercise blocks ./ex check"; exit 1; }
echo "OK: a broken file in another exercise does not block ./ex check"

# restore the normal build of the test project (the builds above changed its project reference)
dotnet build internal/tests/Practice.Tests "${q[@]}" > /dev/null

echo "./ex"
internal/tools/check-ex.sh
