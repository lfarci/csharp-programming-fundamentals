# Pages built from the themes (exec'd by gen.py: uses ORDER, byid, fname, stars, rlinks, RECIPES, DRILLS, X, THEMES).
# exercises/README.md (overview), themes/<slug>.md, ROADMAP.md, docs/progress-checklist.md, diagrams/roadmap.d2.
from learn import TRACKER, PARTS as MSL, MODULE, CERT, SERIES, EPISODES, EPISODE_ORDER, DROPPED, VIDEOS, TOUR, THEORY, path_url, module_url, episode_url, modules_md, episodes_md
assert set(THEORY) == {x["slug"] for x in THEMES}, "learn.py THEORY must list every theme exactly once"
TH_EX = {x["slug"]: [e for e in ORDER if e["theme"] == x["slug"]] for x in THEMES}
NUM = {x["slug"]: i for i, x in enumerate(THEMES, 1)}
PARTS = list(dict.fromkeys(x["part"] for x in THEMES))  # roadmap groups, aligned with the 6 Microsoft Learn parts
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
    L += ["", '<div class="learn-box">', "", f"**Learn the theory on Microsoft Learn** ([Part {th['part']}: {MSL[th['part']][0]}]({path_url(th['part'])}))", "",
          "- **Modules:** " + modules_md(th["modules"]),
          f"- **Video ({SERIES[0]}):** " + episodes_md(th["episodes"])]
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
     "The course is a path of themes, grouped like the 6 parts of [Microsoft Learn](learn/microsoft-learn.md) *Get started with C#*. Do a Microsoft Learn part, then its themes here, **in order, at your own pace**. Move on when the \"ready\" check of a theme works without help.", "",
     '<div class="gh-only">', "",
     "![The roadmap: " + "; ".join(f"{part}: " + ", ".join(x["title"] for x in THEMES if x["part"] == part) for part in PARTS) + "](diagrams/roadmap.svg)", "", "</div>", "",
     "Before the first theme, read [How to read an exercise](docs/reading-an-exercise.md). You will use it for every exercise.", "",
     "<RoadmapPath />", "", '<div class="gh-only">', ""]
R += ["| # | Part | Theme | What you learn | Exercises |", "| --- | --- | --- | --- | --- |"]
for x in THEMES:
    R.append(f"| {NUM[x['slug']]} | {x['part']} | [{x['title']}](themes/{x['slug']}.md) | {x['summary']} | {len(TH_EX[x['slug']])} |")
R.append("")
R += ["</div>", "", "## After the roadmap", "", "Objects and classes come next in most courses. There are no exercises for them here yet: follow your course or Microsoft Learn, and come back to the [cookbook](cookbook/README.md) when a method needs a loop.", "",
      "---", "", "[Home](README.md) · Next: [Getting started](docs/getting-started.md)", ""]
open(f"{ROOT}/ROADMAP.md", "w").write("\n".join(R))

# ---------- diagrams/roadmap.d2 (rendered to SVG by tools/diagrams.sh) ----------
D = ["# Generated by tools/generator (themes.py). Render: tools/diagrams.sh", "...@_style", "direction: down", ""]
for p_i, part in enumerate(PARTS):
    xs = [x for x in THEMES if x["part"] == part]
    # long parts wrap onto rows of 4 so the picture stays readable on a phone
    # a grid of equal cards, 4 per row, read left to right; numbers give the order
    D += [f'part{p_i}: "{part}" {{', "  class: part", f"  grid-rows: {(len(xs) + 3) // 4}", "  grid-columns: 4", "  grid-gap: 24", ""]
    for x in xs:
        name = x["title"].replace("Loops: ", ""); name = name[:1].upper() + name[1:]
        D.append(f'  t{NUM[x["slug"]]}: "{NUM[x["slug"]]}. {name}" {{class: step; width: 270; height: 64}}')
    D += ["}", ""]
D += [f"part{i} -> part{i + 1}" for i in range(len(PARTS) - 1)] + [""]
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


# ---------- learn/: the theory comes from Microsoft Learn ----------
os.makedirs(f"{ROOT}/learn", exist_ok=True)
for old in glob.glob(f"{ROOT}/learn/*.md"): os.remove(old)
def theme_link(x, up="../"): return f"[{x['title']}]({up}themes/{x['slug']}.md)"
USED = {}  # module slug -> themes that practise it
for x in THEMES:
    for m_ in THEORY[x["slug"]]["modules"]: USED.setdefault(m_, []).append(x)
EP_USED = {}
for x in THEMES:
    for e_ in THEORY[x["slug"]]["episodes"]: EP_USED.setdefault(e_, []).append(x)

LG = ["[Home](../README.md) › Learn", "", "# Learn the theory", "",
      "This course is for **practice**: exercises, recipes and a checker. The **theory** comes from **Microsoft Learn**, free: six short learning paths and a video series. Read or watch the matching part, then do the exercises of the theme.", "",
      "<LearnCards />", "", '<div class="gh-only">', "",
      "- [Microsoft Learn modules](microsoft-learn.md): the main companion, the 6 parts and the free certification.",
      f"- [Videos](videos.md): the {SERIES[0]} episodes for each theme.",
      f"- [Extra exercises](quest-tracker.md): more practice in the {TRACKER['title']}.", "", "</div>", "",
      "## What to learn before each theme", "",
      "| # | Theme | Microsoft Learn | Video |", "| ---: | --- | --- | --- |"]
for x in THEMES:
    th = THEORY[x["slug"]]
    LG.append(f"| {NUM[x['slug']]} | {theme_link(x)} | [Part {th['part']}]({path_url(th['part'])}): [{MODULE[th['modules'][0]][1]}]({module_url(th['modules'][0])}) | {episodes_md(th['episodes'][:1])} |")
LG += ["", "Each theme page has a *Learn the theory* box with all its modules and videos.", "", "---", "", "[Home](../README.md) · Next: [Microsoft Learn modules](microsoft-learn.md)", ""]
open(f"{ROOT}/learn/README.md", "w").write("\n".join(LG))

LM = ["[Home](../README.md) › [Learn](README.md) › Microsoft Learn modules", "", "# Microsoft Learn modules", "",
      "Microsoft Learn teaches C# for free in **6 parts** (learning paths). Each part has short **modules**: you read a little, then try the code. This course follows the same order: after a module, do the themes listed under it.", "",
      "<MsLearnPath />", "", '<div class="gh-only">', ""]
for n, (title, ms) in MSL.items():
    LM += [f"**Part {n}: [{title}]({path_url(n)})**", ""]
    for t_, slug_ in ms:
        after = ", ".join(theme_link(x) for x in USED.get(slug_, [])) or "no exercises here"
        LM.append(f"- [{t_}]({module_url(slug_)}). Then: {after}")
    LM.append("")
LM += ["</div>", "",
       f"Prefer videos? See [Videos](videos.md): the {SERIES[0]} episodes for each theme.", "",
       "## The free certification", "",
       f"[{CERT[0]}]({CERT[1]}) is a **free** certification by freeCodeCamp and Microsoft. It is made of the same 6 parts above, you finish the 6 parts on Microsoft Learn (a trophy for each), link them to your freeCodeCamp account, then take an exam of 80 questions in one session (pass with 70%). Both accounts are free.", "",
       "You do not need it for this course. If you want it, this course is the practice: do the themes after each part, then take the exam.", "",
       "## The docs", "", f"[{TOUR[0]}]({TOUR[1]}): the official overview of the language, for later.", "",
       "---", "", "[Learn](README.md) · Next: [Videos](videos.md)", ""]
open(f"{ROOT}/learn/microsoft-learn.md", "w").write("\n".join(LM))

# Videos: kept episodes only, grouped like the roadmap (by the group of the first theme that uses them)
FIRST = {e_: EP_USED[e_][0] for e_ in EPISODE_ORDER}
VG = []
for part in PARTS:
    eps_ = sorted([e_ for e_ in EPISODE_ORDER if FIRST[e_]["part"] == part], key=lambda e_: (NUM[FIRST[e_]["slug"]], EPISODE_ORDER.index(e_)))
    if eps_: VG.append((part, eps_))
LV = ["[Home](../README.md) › [Learn](README.md) › Videos", "", f"# Videos: {SERIES[0]}", "",
      f"[{SERIES[0]}]({SERIES[1]}) is a free video series on Microsoft Learn by Bob Tabor. It explains each idea slowly. Watch an episode, then do the themes under it. Only the episodes about the fundamentals are listed here.", "",
      "<VideoPath />", "", '<div class="gh-only">', ""]
k_ = 0
for part, eps_ in VG:
    LV += [f"{part.split(': ')[0]}: **{part.split(': ')[1]}**", ""]
    for e_ in eps_:
        k_ += 1; t_, mins = EPISODES[e_]
        LV.append(f"- **{k_}** [{t_}]({episode_url(e_)}) ({mins} min). Then: " + ", ".join(theme_link(x) for x in EP_USED[e_]))
    LV.append("")
LV += ["</div>", "", f"More videos, optional: [{VIDEOS[0]}]({VIDEOS[1]}).", "", "---", "", "[Microsoft Learn modules](microsoft-learn.md) · Next: [Extra exercises](quest-tracker.md)", ""]
open(f"{ROOT}/learn/videos.md", "w").write("\n".join(LV))

LQ = ["[Home](../README.md) › [Learn](README.md) › Extra exercises", "", f"# Extra exercises: the {TRACKER['title']}", "",
      f"Want more practice once a theme feels easy? The [{TRACKER['title']}]({TRACKER['url']}) is a free website where you tick challenges, earn XP and level up, like a game. It follows the challenges of the book [The C# Player's Guide](https://csharpplayersguide.com/).", "",
      "## How it works", "",
      "- Open the tracker in your browser. No account.", "- Tick a challenge when you finish it. Your XP goes up.",
      "- Progress is saved in this browser. Use **Settings** to export a backup and import it on another computer.", "",
      f"[Open the {TRACKER['title']}]({TRACKER['url']}) · [Source code]({TRACKER['repo']})", "",
      "---", "", "[Videos](videos.md) · [Learn](README.md)", ""]
open(f"{ROOT}/learn/quest-tracker.md", "w").write("\n".join(LQ))

# ---------- .vitepress/course.json: add the Microsoft Learn path (MsLearnPath component) ----------
_site = json.load(open(f"{ROOT}/.vitepress/course.json", encoding="utf-8"))
_site["mslearn"] = [{"num": n, "title": title, "url": path_url(n),
                     "modules": [{"title": t_, "url": module_url(sl), "themes": [{"title": x["title"], "link": f"/themes/{x['slug']}"} for x in USED.get(sl, [])]} for t_, sl in ms]}
                    for n, (title, ms) in MSL.items()]
_n = iter(range(1, 100))
_site["videos"] = [{"group": part, "episodes": [{"num": next(_n), "title": EPISODES[e_][0], "minutes": EPISODES[e_][1], "url": episode_url(e_),
                     "themes": [{"title": x["title"], "link": f"/themes/{x['slug']}"} for x in EP_USED[e_]]} for e_ in eps_]} for part, eps_ in VG]
json.dump(_site, open(f"{ROOT}/.vitepress/course.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
