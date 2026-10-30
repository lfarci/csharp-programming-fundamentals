#!/usr/bin/env python3
"""Small prose mistakes the reviews kept finding in the course pages: a doubled word ("the the"),
a space before a full stop or comma, and an unclosed `code span`. Code blocks and code spans are skipped."""
import glob, re, sys, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CHECKS = [("doubled word", re.compile(r"\b([A-Za-z]{2,}) \1\b", re.I)),
          ("space before . or ,", re.compile(r"[A-Za-z)] [.,](\s|$)"))]
bad = []
for f in sorted(glob.glob("course/**/*.md", recursive=True) + ["README.md", "practice/README.md"]):
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), open(f, encoding="utf-8").read(), flags=re.S)
    for n, line in enumerate(text.split("\n"), 1):
        if line.count("`") % 2: bad.append(f"{f}:{n}: unclosed `code span`")
        plain = re.sub(r"`[^`]*`", "X", line)
        bad += [f"{f}:{n}: {name}: {plain.strip()[:100]}" for name, rx in CHECKS if rx.search(plain)]
print("\n".join(bad) if bad else "OK: no doubled words, stray spaces before punctuation or unclosed code spans")
sys.exit(1 if bad else 0)
