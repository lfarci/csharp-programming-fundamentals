#!/usr/bin/env python3
"""The repo root stays small: README.md, the ./ex tool, practice/ (the learner's code), course/ (what she reads),
internal/ (machinery) and the few files tools need at the root. Anything else fails: put it in course/ or internal/."""
import os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALLOWED = {
    "README.md", "ex", "ex.cmd", "practice", "course", "internal",       # what the learner sees
    "AGENTS.md", "CLAUDE.md",                                            # agent notes (found by agents at the root)
    "global.json", "CSharpFundamentals.sln",                             # dotnet needs them at the root
    ".github", ".gitignore", ".vscode", ".devcontainer", ".agents",      # GitHub, VS Code, Codespaces, agent skills
}
tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
extra = sorted({p.split("/")[0] for p in tracked} - ALLOWED)
for e in extra: print(f"FAIL: {e} is at the repo root. Move it into course/ (learner pages) or internal/ (machinery), or allow it in internal/tools/check-root.py.")
print("OK: the repo root only has the allowed entries" if not extra else f"FAIL: {len(extra)} unexpected root entr{'y' if len(extra) == 1 else 'ies'}")
sys.exit(1 if extra else 0)
