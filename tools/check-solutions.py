#!/usr/bin/env python3
"""Build every solution once and run it with the examples from tests.json.

Each expected line must appear, in order, at the END of an output line
(prompts such as "N: " are printed with Console.Write, so they share the line).

Usage: python3 tools/check-solutions.py [ID prefix ...]   e.g. A0 M01
"""
import json, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOL = os.path.join(ROOT, "solutions")
tests = json.load(open(os.path.join(SOL, "tests.json")))
only = sys.argv[1:]
if only:
    tests = [t for t in tests if any(t["file"].startswith(p) for p in only)]

def matches(out_lines, expected):
    i = 0
    for line in out_lines:
        if i < len(expected) and line.rstrip().endswith(expected[i].rstrip()):
            i += 1
    return i == len(expected)

build = tempfile.mkdtemp(prefix="cpf-sol-")
built, fails = {}, 0
for t in tests:
    f = t["file"]
    if f not in built:
        out = os.path.join(build, f[:-3])
        r = subprocess.run(["dotnet", "build", os.path.join(SOL, f), "-o", out, "-nologo", "-v", "q"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f"❌ {f}: does not compile\n{r.stdout[-2000:]}{r.stderr[-2000:]}")
            built[f] = None; fails += 1; continue
        dll = [x for x in os.listdir(out) if x.endswith(".dll") and x[:-4] == f[:-3]]
        built[f] = os.path.join(out, dll[0]) if dll else None
    if not built[f]:
        continue
    work = tempfile.mkdtemp(prefix="cpf-run-")   # files like numbers.txt land here
    r = subprocess.run(["dotnet", built[f]], input="\n".join(t["input"]) + "\n",
                       capture_output=True, text=True, cwd=work, timeout=30)
    lines = r.stdout.splitlines()
    if r.returncode != 0 or not matches(lines, t["expected"]):
        fails += 1
        print(f"❌ {f} input={t['input']}\n   expected={t['expected']}\n   got={lines}\n   {r.stderr[-500:]}")
print(f"{'✅' if not fails else '❌'} {len(tests)} example runs over {len(built)} solutions, {fails} failure(s)")
sys.exit(1 if fails else 0)
