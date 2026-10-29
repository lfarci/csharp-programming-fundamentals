# Pages built from the themes (exec'd by gen.py: uses ORDER, byid, fname, stars, rlinks, RECIPES, DRILLS, X, THEMES).
# exercises/README.md (overview), themes/<slug>.md, ROADMAP.md, docs/progress-checklist.md, diagrams/roadmap.d2.
TH_EX = {x["slug"]: [e for e in ORDER if e["theme"] == x["slug"]] for x in THEMES}
NUM = {x["slug"]: i for i, x in enumerate(THEMES, 1)}
PARTS = ["Before loops", "Loops", "After loops"]
def kind(e):
    if e.get("paper"): return "paper"
    if e.get("task") == "parsons": return "arrange the lines"
    if e.get("task") == "debug": return "fix the bugs"
    return "write code"
def mdlinks(items): return " · ".join(f"[{a}]({b})" for a, b in items)

# ---------- exercises/README.md: overview of all themes ----------
out = ["[Home](../README.md) › Exercises", "", "# Exercises", "",
       f"{len(ORDER)} small exercises in {len(THEMES)} themes. Do the themes in order; inside a theme, do the exercises from top to bottom. Each one adds **one** new difficulty.", "",
       "Start one with `./ex start A04`, check it with `./ex check`. New here? Read [Getting started](../docs/getting-started.md) first.", "",
       "<ExercisesOverview />", "", '<div class="gh-only">', "",
       "| # | Theme | What you practise | Exercises |", "| ---: | --- | --- | ---: |"]
for x in THEMES:
    out.append(f"| {NUM[x['slug']]} | [{x['title']}](../themes/{x['slug']}.md) | {x['summary']} | {len(TH_EX[x['slug']])} |")
out += ["", "</div>", "",
        "## Levels", "", "- **Guided**: small steps, the hints help a lot.", "- **Independent**: the same idea, alone.", "- **Challenge**: a new problem; combine recipes.", "",
        "## Drill sets (same pattern, many times)", "",
        "Want to practise one pattern today? Do **one row**, in order. The exercises change only small details, so you see the **same pattern** again and again.", "",
        "| Drill | Recipe | Exercises, in order |", "| --- | --- | --- |"]
for name, r, ids in DRILLS:
    for i in ids: assert i in byid, f"drill set lists unknown exercise {i}"
    out.append(f"| {name} | [{RECIPES[r][0]}](../cookbook/{RECIPES[r][1]}.md) | " + ", ".join(f"[{i}]({fname(byid[i])}.md)" for i in ids) + " |")
out += ["", "## Extra challenges", "", "Bigger problems for later, once their theme feels easy.", "", "| Problem | Theme | Do first |", "| --- | --- | --- |"]
for x in X:
    if x["source"].startswith("Project"):
        out.append(f"| [{x['source']}: {x['title']}]({x['url']}) | {BYSLUG[x['theme']]['title']} | {x['pre']} |")
out += ["", "## When you are stuck", "", "1. Read the recipe again in the [cookbook](../cookbook/README.md).", "2. Solve a smaller example on paper with a trace table.",
        "3. Open **one** hint. Wait. Try again.", "4. Still stuck? Do the exercise listed in *Do these first*.", ""]
open(f"{ROOT}/exercises/README.md", "w").write("\n".join(out))
if os.path.exists(f"{ROOT}/exercises/dependency-graph.md"): os.remove(f"{ROOT}/exercises/dependency-graph.md")

# ---------- themes/<slug>.md ----------
os.makedirs(f"{ROOT}/themes", exist_ok=True)
for old in glob.glob(f"{ROOT}/themes/*.md"): os.remove(old)
for k, x in enumerate(THEMES):
    s = x["slug"]; L = [f"[Home](../README.md) › [Roadmap](../ROADMAP.md) › Theme {k+1} of {len(THEMES)}", "", f"# {x['title']}", "", x["summary"], "",
                        "## After this theme you can", ""] + [f"- {o}" for o in x["objectives"]] + ["",
         "## Exercises", "", "Do them from top to bottom. Tick each one when `./ex check` says DONE.", "",
         f'<ThemeExercises theme="{s}" />', "", '<div class="gh-only">', "", "| ID | Exercise | Kind | Level | Effort |", "| --- | --- | --- | --- | --- |"]
    for e in TH_EX[s]:
        L.append(f"| {e['id']} | [{e['title']}](../exercises/{fname(e)}.md) | {kind(e)} | {e['level']} | {stars(e['stars'])} |")
    L += ["", "</div>", "", "## What to learn", "", f"- **C#:** {x['learn']}"]
    if x["recipes"]: L.append("- **Recipes:** " + ", ".join(f"[{RECIPES[r][0]}](../cookbook/{RECIPES[r][1]}.md)" for r in x["recipes"]))
    L.append(f"- **Book (optional):** *The C# Player's Guide*, {x['book']}.")
    if x["docs"]: L.append("- **Microsoft docs:** " + mdlinks(x["docs"]))
    L += ["", "## Ready for the next theme when", "", f"{x['ready'][0].upper()}{x['ready'][1:]}", "", "---", ""]
    nav_ = []
    if k: nav_.append(f"Previous: [{THEMES[k-1]['title']}]({THEMES[k-1]['slug']}.md)")
    nav_.append("[Roadmap](../ROADMAP.md)")
    if k < len(THEMES) - 1: nav_.append(f"Next: [{THEMES[k+1]['title']}]({THEMES[k+1]['slug']}.md)")
    L += [" · ".join(nav_), ""]
    open(f"{ROOT}/themes/{s}.md", "w").write("\n".join(L))

# ---------- ROADMAP.md ----------
R = ["[Home](README.md) › Roadmap", "", "# Roadmap", "",
     "The course is a path of themes. Go through them **in order, at your own pace**. Move on when the \"ready\" check of a theme works without help.", "",
     '<div class="gh-only">', "",
     "![The roadmap: three parts in order. Before loops: Hello World, Variables and expressions, Conditions. Loops: repeat and count, keep a running result, draw in 2D, take digits apart, remember changing values, search, combine recipes. After loops: Arrays and text, Files, Exceptions, Collections, Methods.](diagrams/roadmap.svg)", "", "</div>", "",
     "Before the first theme, read [How to read an exercise](docs/reading-an-exercise.md). You will use it for every exercise.", "",
     "<RoadmapPath />", "", '<div class="gh-only">', ""]
R += ["| # | Part | Theme | What you learn | Exercises |", "| --- | --- | --- | --- | --- |"]
for x in THEMES:
    R.append(f"| {NUM[x['slug']]} | {x['part']} | [{x['title']}](themes/{x['slug']}.md) | {x['summary']} | {len(TH_EX[x['slug']])} |")
R.append("")
R += ["</div>", "", "## After the roadmap", "", "Objects and classes come next in most courses. There are no exercises for them here yet: follow your course or the book, and come back to the [cookbook](cookbook/README.md) when a method needs a loop.", "",
      "---", "", "[Home](README.md) · Next: [Getting started](docs/getting-started.md)", ""]
open(f"{ROOT}/ROADMAP.md", "w").write("\n".join(R))

# ---------- diagrams/roadmap.d2 (rendered to SVG by tools/diagrams.sh) ----------
D = ["# Generated by tools/generator (themes.py). Render: tools/diagrams.sh", "...@_style", "direction: down", ""]
for p_i, part in enumerate(PARTS):
    xs = [x for x in THEMES if x["part"] == part]
    # long parts wrap onto rows of 4 so the picture stays readable on a phone
    # a grid of equal cards, 4 per row, read left to right; numbers give the order
    D += [f"part{p_i}: {part} {{", "  class: part", f"  grid-rows: {(len(xs) + 3) // 4}", "  grid-columns: 4", "  grid-gap: 24", ""]
    for x in xs:
        name = x["title"].replace("Loops: ", ""); name = name[:1].upper() + name[1:]
        D.append(f'  t{NUM[x["slug"]]}: "{NUM[x["slug"]]}. {name}" {{class: step; width: 270; height: 64}}')
    D += ["}", ""]
D += ["part0 -> part1", "part1 -> part2", ""]
os.makedirs(f"{ROOT}/diagrams", exist_ok=True)
open(f"{ROOT}/diagrams/roadmap.d2", "w").write("\n".join(D))

# ---------- progress checklist (paper) ----------
pc = ["[Home](../README.md) › Progress checklist", "", "# My progress checklist (paper)", "",
      "Print this page if you like paper. Tick a box when it is true **without help**. (On the website, use [My progress](../progress.md) instead.)", "",
      "**Solved** = `./ex check` says DONE. **Mastered** = you also solved the mastery check alone, on another day.", ""]
for x in THEMES:
    pc += [f"## {x['title']}", ""]
    for e in TH_EX[x["slug"]]:
        pc += [f"- [ ] [{e['id']} · {e['title']}](../exercises/{fname(e)}.md) solved", "  - [ ] mastered (another day, alone)"]
    pc.append("")
pc += ["---", "", "[Home](../README.md) · [All exercises](../exercises/README.md)", ""]
open(f"{ROOT}/docs/progress-checklist.md", "w").write("\n".join(pc))
