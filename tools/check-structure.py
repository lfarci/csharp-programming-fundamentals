#!/usr/bin/env python3
"""Course structure rules that a review keeps finding by hand. Fails (exit 1) on an error, prints warnings.

- every exercise title is short (at most 24 characters) and does not repeat its kind ("(paper)", "Fix the bugs:");
- every exercise sits in exactly one theme group and appears in its theme page table (reachable);
- inside a group the level never goes back (Guided, then Independent, then Challenge);
- every drill set lists its exercises in course order;
- theme size balance: every theme has at least 3 exercises, every group 2 to 14 (warning above that);
- the website sidebar lists themes and groups only, never one link per exercise.
"""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "generator"))
from themes import THEMES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_TITLE, LEVELS = 24, ["Guided", "Independent", "Challenge"]
site = json.load(open(f"{ROOT}/.vitepress/course.json", encoding="utf-8"))
ex = {e["id"]: e for e in site["exercises"]}
errors, warnings = [], []

for e in site["exercises"]:
    if len(e["title"]) > MAX_TITLE: errors.append(f"{e['id']}: title {e['title']!r} is longer than {MAX_TITLE} characters")
    if re.search(r"\(paper\)|^Fix the bugs|^Arrange the lines", e["title"]): errors.append(f"{e['id']}: the title repeats the kind ({e['title']!r}); the badge shows it")
    page = f"{ROOT}/themes/{e['theme']}.md"
    if f"{e['link'].split('/')[-1]}.md" not in open(page, encoding="utf-8").read(): errors.append(f"{e['id']}: not linked from {os.path.relpath(page, ROOT)}")

for x in THEMES:
    n = sum(len(g["ids"]) for g in x["groups"])
    if n < 3: errors.append(f"theme {x['slug']}: only {n} exercise(s); merge it into a neighbour")
    for g in x["groups"]:
        lv = [LEVELS.index(ex[i]["level"]) for i in g["ids"]]
        for a, b in zip(g["ids"], g["ids"][1:]):
            if LEVELS.index(ex[b]["level"]) < LEVELS.index(ex[a]["level"]):
                errors.append(f"group {x['slug']}/{g['slug']}: {b} ({ex[b]['level']}) comes after {a} ({ex[a]['level']}); levels must not go back")
        if len(g["ids"]) < 2: errors.append(f"group {x['slug']}/{g['slug']}: a group needs at least 2 exercises")
        if len(g["ids"]) > 14: warnings.append(f"group {x['slug']}/{g['slug']}: {len(g['ids'])} exercises; consider splitting it (14 at most)")

pos = {e["id"]: i for i, e in enumerate(site["exercises"])}
for d in site["drillSets"]:
    if [pos[i] for i in d["ids"]] != sorted(pos[i] for i in d["ids"]): errors.append(f"drill set {d['name']!r} is not in course order")

cfg = open(f"{ROOT}/.vitepress/config.mts", encoding="utf-8").read()
if re.search(r"course\.exercises|/exercises/[A-Z]\d\d", cfg): errors.append(".vitepress/config.mts: the sidebar must not list exercises (themes and groups only)")

for w in warnings: print("WARN:", w)
for m in errors: print("FAIL:", m)
if errors: sys.exit(1)
print(f"OK: structure ({len(ex)} exercises, {len(THEMES)} themes, {sum(len(x['groups']) for x in THEMES)} groups)")
