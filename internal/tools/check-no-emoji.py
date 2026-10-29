"""Fails if a tracked text file contains an emoji. Rule: plain words only (see AGENTS.md)."""
import re, subprocess, sys
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\u2300-\u23FF\u25A0-\u25FF\uFE0F]")
files = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.split()
bad = []
for f in files:
    if not re.search(r"\.(md|cs|py|sh|json|jsonc|yml|cmd|tape)$|^ex$", f): continue
    for n, line in enumerate(open(f, encoding="utf-8", errors="ignore"), 1):
        if EMOJI.search(line): bad.append(f"{f}:{n}: {line.strip()[:80]}")
for b in bad: print("FAIL:", b)
print("OK: no emoji in tracked files" if not bad else f"FAIL: {len(bad)} line(s) with emoji. Use plain words.")
sys.exit(1 if bad else 0)
