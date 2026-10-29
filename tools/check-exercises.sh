#!/usr/bin/env bash
# 1. Reference solutions pass every example (method cases + program runs).
# 2. Every starter compiles, and no starter already passes all its examples (else the tests are too weak).
# 3. One exercise builds alone, even when another practice file is broken.
# 4. The ./ex tool builds and lists the exercises.
set -euo pipefail
cd "$(dirname "$0")/.."
tmp=$(mktemp -d)
q=(-nologo -v q -clp:NoSummary)

dotnet build tests/Practice.Tests "${q[@]}"
tests="dotnet tests/Practice.Tests/bin/Debug/net8.0/Practice.Tests.dll -noLogo -noColor"

echo "▶ Reference solutions"
dotnet build solutions "${q[@]}" -o "$tmp/solutions"
EXERCISE_ASSEMBLY="$tmp/solutions/Solutions.dll" $tests -xml "$tmp/solutions.xml" > "$tmp/solutions.log" 2>&1 || { grep -E "\[FAIL\]" -A6 "$tmp/solutions.log"; echo "❌ some reference solutions fail their examples"; exit 1; }
grep -E "Total:" "$tmp/solutions.log"
if grep -q 'result="Skip"' "$tmp/solutions.xml"; then echo "❌ some exercises have no reference solution"; exit 1; fi
echo "✅ reference solutions pass every example"

echo "▶ Starters"
mkdir -p "$tmp/repo/tools/ex"
cp -r practice "$tmp/repo/practice"; rm -rf "$tmp/repo/practice"/{bin,obj}
cp tools/ex/Runner.cs "$tmp/repo/tools/ex/"
cp tools/starters/*.cs "$tmp/repo/practice/"
dotnet build "$tmp/repo/practice" "${q[@]}" -o "$tmp/starters"
EXERCISE_ASSEMBLY="$tmp/starters/Practice.dll" $tests -xml "$tmp/starters.xml" > /dev/null 2>&1 || true
python3 - "$tmp/starters.xml" <<'PY'
import sys, xml.etree.ElementTree as T, collections
res = collections.defaultdict(list)
for t in T.parse(sys.argv[1]).getroot().iter("test"):
    res[t.get("type")].append(t.get("result"))
weak = [c for c, r in res.items() if all(x == "Pass" for x in r)]
if weak:
    sys.exit("❌ these starters already pass all examples (add a case the TODO version fails): " + ", ".join(weak))
print(f"✅ {len(res)} starters compile and none passes before the learner writes code")
PY

echo "▶ One exercise at a time"
echo "int broken = ;" > "$tmp/repo/practice/A01_Sum1ToN.cs"
dotnet build "$tmp/repo/practice" "${q[@]}" -p:OnlyExercise=A04_Factorial -o "$tmp/only" > "$tmp/only.log" 2>&1 || { cat "$tmp/only.log"; echo "❌ a broken file in another exercise blocks ./ex check"; exit 1; }
echo "✅ a broken file in another exercise does not block ./ex check"

echo "▶ ./ex"
dotnet build tools/ex "${q[@]}"
dotnet run --project tools/ex --no-build -- list > /dev/null
echo "✅ ./ex works"
