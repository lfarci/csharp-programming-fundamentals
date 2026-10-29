# Pages built from the themes (exec'd by gen.py: uses ORDER, byid, fname, stars, rlinks, RECIPES, DRILLS, X, THEMES).
# exercises/README.md (overview), themes/<slug>.md, ROADMAP.md, docs/progress-checklist.md, diagrams/roadmap.d2.
from learn import BOOK, LEVELS, TRACKER, PATHS, CERT, VIDEOS, TOUR, THEORY, level_text
assert set(THEORY) == {x["slug"] for x in THEMES}, "learn.py THEORY must list every theme exactly once"
for _t in THEORY.values():
    for _n in _t["levels"]: assert _n in LEVELS, f"book level {_n} has no verified name in learn.py LEVELS"
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
    th = THEORY[s]
    L += ["", '<div class="learn-box">', "", "**Learn the theory** (before or beside the exercises)", "",
          f"- **Book:** [*{BOOK['title']}*](../learn/players-guide.md), {level_text(th['levels'])}"]
    L.append("- **Microsoft Learn:** " + mdlinks(th["modules"]))
    if th["videos"]: L.append("- **Video:** " + mdlinks(th["videos"]))
    if x["docs"]: L.append("- **Reference:** " + mdlinks(x["docs"]))
    L += ["", "</div>"]
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


# ---------- learn/: the theory comes from existing resources ----------
os.makedirs(f"{ROOT}/learn", exist_ok=True)
def theme_link(x, up="../"): return f"[{x['title']}]({up}themes/{x['slug']}.md)"
LG = ["[Home](../README.md) › Learn", "", "# Learn the theory", "",
     "This course is for **practice**: exercises, recipes and a checker. The **theory** comes from two free or well-known resources. Read or watch the matching part, then do the exercises of the theme.", "",
     "<LearnCards />", "", '<div class="gh-only">', "",
     f"- [The book: *{BOOK['title']}*](players-guide.md): the main theory companion.",
     "- [Microsoft Learn](microsoft-learn.md): free modules and videos from Microsoft.",
     f"- [Extra exercises: the {TRACKER['title']}](quest-tracker.md): track the book's own challenges.", "", "</div>", "",
     "## What to read before each theme", "",
     "| # | Theme | Book level | Microsoft Learn |", "| ---: | --- | --- | --- |"]
for x in THEMES:
    th = THEORY[x["slug"]]
    LG.append(f"| {NUM[x['slug']]} | {theme_link(x)} | {', '.join(str(n) for n in th['levels'])} | {mdlinks(th['modules'][:1])} |")
LG += ["", "Each theme page has a *Learn the theory* box with all the links.", "", "---", "", "[Home](../README.md) · Next: [The book](players-guide.md)", ""]
open(f"{ROOT}/learn/README.md", "w").write("\n".join(LG))

LB = ["[Home](../README.md) › [Learn](README.md) › The book", "", f"# The book: {BOOK['title']}", "",
     f"*{BOOK['title']}* ({BOOK['edition']}), by {BOOK['author']}, teaches C# from zero, in short **levels**. It is the theory companion of this course: we do not copy it, we point to the right level.", "",
     "<BuyBook />", "", '<div class="gh-only">', "", f"[Official site]({BOOK['url']}) · [Free sample (PDF)]({BOOK['sample']})", "", "</div>", "",
     "## How to use it with this course", "",
     "1. Open the theme you are on.", "2. Read the book level in its *Learn the theory* box.", "3. Do the exercises of the theme here.",
     f"4. Want more? Do the book's own challenges and tick them in the [{TRACKER['title']}](quest-tracker.md).", "",
     "## Book levels for each theme", "", "| # | Theme | Read |", "| ---: | --- | --- |"]
for x in THEMES:
    LB.append(f"| {NUM[x['slug']]} | {theme_link(x)} | {level_text(THEORY[x['slug']]['levels'])} |")
LB += ["", f"Level names come from the table of contents of the {BOOK['edition']}. Levels 1 and 2 (what C# is, installing an IDE) are covered by [Getting started](../docs/getting-started.md).", "",
      "---", "", "[Learn](README.md) · Next: [Microsoft Learn](microsoft-learn.md)", ""]
open(f"{ROOT}/learn/players-guide.md", "w").write("\n".join(LB))

LM = ["[Home](../README.md) › [Learn](README.md) › Microsoft Learn", "", "# Microsoft Learn", "",
     "Microsoft has free C# lessons for beginners: short **modules** you read and try in the browser, and a **video** series. Use them for the theory; use this course to practise.", "",
     "## The free path", "", f"[{CERT[0]}]({CERT[1]}) groups six learning paths. You can follow them without the exam:", ""]
for i, (t_, u) in enumerate(PATHS, 1): LM.append(f"{i}. [{t_}]({u})")
LM += ["", "## Videos", "", f"[{VIDEOS[0]}]({VIDEOS[1]}): each video is 15 to 30 minutes.", "",
      "## The docs", "", f"[{TOUR[0]}]({TOUR[1]}): the official overview, with small tutorials.", "",
      "## Which module before which theme", "", "| # | Theme | Module | Video |", "| ---: | --- | --- | --- |"]
for x in THEMES:
    th = THEORY[x["slug"]]
    LM.append(f"| {NUM[x['slug']]} | {theme_link(x)} | {mdlinks(th['modules'])} | {mdlinks(th['videos']) or '-'} |")
LM += ["", "---", "", "[The book](players-guide.md) · Next: [Extra exercises](quest-tracker.md)", ""]
open(f"{ROOT}/learn/microsoft-learn.md", "w").write("\n".join(LM))

LQ = ["[Home](../README.md) › [Learn](README.md) › Extra exercises", "", f"# Extra exercises: the {TRACKER['title']}", "",
     f"The book has its own challenges at the end of each level. The [{TRACKER['title']}]({TRACKER['url']}) is a free website to tick them, earn XP and level up, like a game.", "",
     "## How it works", "",
     "- Open the tracker in your browser. No account.", "- Tick a challenge when you finish it. Your XP and level go up.",
     "- Progress is saved in this browser. Use **Settings** to export a backup and import it on another computer.", "",
     "## When to use it", "",
     "Finish the exercises of a theme here first. Then, for more practice, do the book's challenges of the same level and track them there.", "",
     f"[Open the {TRACKER['title']}]({TRACKER['url']}) · [Source code]({TRACKER['repo']})", "",
     "---", "", "[Microsoft Learn](microsoft-learn.md) · [Learn](README.md)", ""]
open(f"{ROOT}/learn/quest-tracker.md", "w").write("\n".join(LQ))
