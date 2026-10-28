#!/usr/bin/env python3
"""Run every solution in solutions/ with the example inputs from the exercises
and check that the expected lines appear in the output, in order.

Needs the .NET 10 SDK (file-based apps: `dotnet run file.cs`).
Usage: python3 tools/check-solutions.py [ID-prefix ...]
"""
import json, os, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOL = os.path.join(ROOT, "solutions")
tests = json.load(open(os.path.join(SOL, "tests.json")))
if len(sys.argv) > 1:
    tests = [t for t in tests if any(t["file"].startswith(p) for p in sys.argv[1:])]
env = dict(os.environ, DOTNET_CLI_TELEMETRY_OPTOUT="1", DOTNET_NOLOGO="1", DOTNET_SYSTEM_GLOBALIZATION_INVARIANT="1")
dotnet = shutil.which("dotnet") or os.path.expanduser("~/.dotnet/dotnet")

# build each file once (sequentially warms the cache), then run the tests
for f in sorted({t["file"] for t in tests}):
    r = subprocess.run([dotnet, "build", os.path.join(SOL, f)], capture_output=True, text=True, env=env)
    if r.returncode != 0:
        print(f"BUILD FAIL {f}\n{r.stdout[-2000:]}"); sys.exit(1)

def run(t):
    with tempfile.TemporaryDirectory() as d:  # files written by solutions (F01) go here
        r = subprocess.run([dotnet, "run", "--no-build", os.path.join(SOL, t["file"])], input="\n".join(t["input"]) + "\n",
                           capture_output=True, text=True, env=env, cwd=d, timeout=60)
    lines = [l.rstrip() for l in r.stdout.splitlines()]
    pos = 0
    for exp in t["expected"]:
        while pos < len(lines) and exp.rstrip() not in lines[pos]:
            pos += 1
        if pos == len(lines):
            return f"FAIL {t['file']} input={t['input']} missing {exp!r}\n--- output ---\n{r.stdout}{r.stderr}"
        pos += 1
    return None

with ThreadPoolExecutor(4) as pool:
    fails = [x for x in pool.map(run, tests) if x]
for f in fails: print(f)
print(f"{len(tests) - len(fails)}/{len(tests)} example runs OK")
sys.exit(1 if fails else 0)
