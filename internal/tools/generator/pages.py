# Pages built from the themes (exec'd by gen.py: uses ORDER, byid, fname, stars, kind, rlinks, RECIPES, DRILLS, X, THEMES, GROUP).
# exercises/README.md (overview), themes/<slug>.md, ROADMAP.md, docs/progress-checklist.md, diagrams/roadmap.d2, docs/README.md.
from learn import TRACKER, PARTS as MSL, MODULE, CERT, SERIES, EPISODES, EPISODE_ORDER, DROPPED, THUMBS, NOTES, CERT_SOURCES, VIDEOS, TOUR, THEORY, path_url, module_url, episode_url, modules_md, episodes_md
assert set(THEORY) == {x["slug"] for x in THEMES}, "learn.py THEORY must list every theme exactly once"
TH_EX = {x["slug"]: [e for e in ORDER if e["theme"] == x["slug"]] for x in THEMES}
NUM = {x["slug"]: i for i, x in enumerate(THEMES, 1)}
PARTS = list(dict.fromkeys(x["part"] for x in THEMES))  # roadmap groups, aligned with the 6 Microsoft Learn parts
def mdlinks(items): return " · ".join(f"[{a}]({b})" for a, b in items)
def gex(g_): return [byid[i_] for i_ in g_["ids"]]
def recipe_link(r, up="../"): return f"[Recipe {int(r)} · {RECIPES[r][0]}]({up}cookbook/{RECIPES[r][1]}.md)"
def ex_row(e, up="../exercises/"):
    return f"| {e['id']} | [{e['title']}]({up}{fname(e)}.md) | {kind(e)} | {e['level']} | {stars(e['stars'])} |"

# ---------- exercises/README.md: overview of all themes ----------
out = ["[Home](../../README.md) › Exercises", "", "# Exercises", "",
       f"{len(ORDER)} small exercises in {len(THEMES)} themes. Each theme is split into small groups of the **same pattern**. Do them in order: each exercise adds **one** new difficulty.", "",
       "Start one with `./ex start A04`, check it with `./ex check`. New here? Read [Getting started](../docs/getting-started.md) first.", "",
       "<ExercisesOverview />", "", '<div class="gh-only">', "",
       "| # | Theme | Groups | Exercises |", "| ---: | --- | --- | ---: |"]
for x in THEMES:
    out.append(f"| {NUM[x['slug']]} | [{x['title']}](../themes/{x['slug']}.md) | " + ", ".join(f"[{g_['title']}](../themes/{gpage(x, g_)}.md) ({len(g_['ids'])})" for g_ in x["groups"]) + f" | {len(TH_EX[x['slug']])} |")
out += ["", "</div>", "",
        "## Levels", "", "- **Guided**: small steps, the hints help a lot.", "- **Independent**: the same idea, alone.", "- **Challenge**: a new problem; combine recipes.", "",
        "## Drill sets (same pattern, many times)", "",
        "Want to practise one pattern today? Do **one set**, in order. The exercises change only small details, so you see the **same pattern** again and again.", "",
        "<DrillSets />", "", '<div class="gh-only">', "",
        "| Drill | Recipe | Exercises, in order |", "| --- | --- | --- |"]
for name, r, ids in DRILLS:
    for i in ids: assert i in byid, f"drill set lists unknown exercise {i}"
    assert [POS[i] for i in ids] == sorted(POS[i] for i in ids), f"drill set {name!r} is not in course order"
    out.append(f"| {name} | [{RECIPES[r][0]}](../cookbook/{RECIPES[r][1]}.md) | " + ", ".join(f"[{i}]({fname(byid[i])}.md)" for i in ids) + " |")
out += ["", "</div>", "", "## Extra challenges", "", "Bigger problems for later, once their theme feels easy.", "", "| Problem | Theme | Do first |", "| --- | --- | --- |"]
for x in X:
    if x["source"].startswith("Project"):
        out.append(f"| [{x['source']}: {x['title']}]({x['url']}) | {BYSLUG[x['theme']]['title']} | {x['pre']} |")
out += ["", "## When you are stuck", "", "1. Read the recipe again in the [cookbook](../cookbook/README.md).", "2. Solve a smaller example on paper with a trace table.",
        "3. Open **one** hint. Wait. Try again.", "4. Still stuck? Do the exercise listed in *Do these first*.", ""]
open(f"{ROOT}/course/exercises/README.md", "w").write("\n".join(out))
if os.path.exists(f"{ROOT}/course/exercises/dependency-graph.md"): os.remove(f"{ROOT}/course/exercises/dependency-graph.md")

# ---------- the "Learn the theory" card: Watch one video, Read one module, Then practise ----------
def learn_card(x):
    th = THEORY[x["slug"]]; ep, mo = th["episodes"][0], th["modules"][0]; first = TH_EX[x["slug"]][0]
    return {"watch": {"title": EPISODES[ep][0], "minutes": EPISODES[ep][1], "link": f"/learn/videos/{ep}"},
            "read": {"title": MODULE[mo][1], "part": MODULE[mo][0], "url": module_url(mo)},
            "first": {"id": first["id"], "title": first["title"], "link": f"/exercises/{fname(first)}"},
            "path": {"num": th["part"], "title": MSL[th["part"]][0], "url": path_url(th["part"])},
            "more": {"modules": [{"title": MODULE[m_][1], "part": MODULE[m_][0], "url": module_url(m_)} for m_ in th["modules"][1:]],
                     "videos": [{"title": EPISODES[e_][0], "link": f"/learn/videos/{e_}"} for e_ in th["episodes"][1:]],
                     "docs": [{"title": a_, "url": b_} for a_, b_ in x["docs"]]}}
LEARN = {x["slug"]: learn_card(x) for x in THEMES}

# ---------- themes/<slug>.md ----------
os.makedirs(f"{ROOT}/course/themes", exist_ok=True)
for old in glob.glob(f"{ROOT}/course/themes/*.md"): os.remove(old)
for k, x in enumerate(THEMES):
    s = x["slug"]; c = LEARN[s]
    L = [f"[Home](../../README.md) › [Roadmap](../ROADMAP.md) › Theme {k+1} of {len(THEMES)}", "", f"# {x['title']}", "", x["summary"], "",
         f'<LearnCard theme="{s}" />', "", '<div class="gh-only">', "", "**Before you start:**", "",
         f"1. **Watch:** [{c['watch']['title']}](../learn/videos/{THEORY[s]['episodes'][0]}.md) ({c['watch']['minutes']} min)",
         f"2. **Read:** [{c['read']['title']}]({c['read']['url']}) (Microsoft Learn, Part {c['read']['part']})",
         f"3. **Then practise:** [{c['first']['id']} · {c['first']['title']}](../exercises/{fname(TH_EX[s][0])}.md)", "",
         "<details><summary>More on Microsoft Learn</summary>", ""]
    if c["more"]["modules"]: L.append("- **Modules:** " + modules_md(THEORY[s]["modules"][1:]))
    if c["more"]["videos"]: L.append("- **Videos:** " + " · ".join(f"[{EPISODES[e_][0]}](../learn/videos/{e_}.md)" for e_ in THEORY[s]["episodes"][1:]))
    if x["docs"]: L.append("- **Reference:** " + mdlinks(x["docs"]))
    L += ["", "</details>", "", "</div>", "",
          "## After this theme you can", ""] + [f"- {o}" for o in x["objectives"]] + ["",
          "## The groups", "", "Do the groups in order, and the exercises of a group from top to bottom. Tick each one when `./ex check` says DONE.", "",
          f'<ThemeGroups theme="{s}" />', "", '<div class="gh-only">', ""]
    L += [f"{i_}. [{g_['title']}]({gpage(x, g_)}.md): {g_['about']} ({len(g_['ids'])} exercises)" for i_, g_ in enumerate(x["groups"], 1)] + ["", "</div>", ""]
    L += ["## Ready for the next theme when", "", f"{x['ready'][0].upper()}{x['ready'][1:]}", "", "---", ""]
    nav_ = []
    if k: nav_.append(f"Previous: [{THEMES[k-1]['title']}]({THEMES[k-1]['slug']}.md)")
    nav_.append("[Roadmap](../ROADMAP.md)")
    if k < len(THEMES) - 1: nav_.append(f"Next: [{THEMES[k+1]['title']}]({THEMES[k+1]['slug']}.md)")
    L += [" · ".join(nav_), ""]
    open(f"{ROOT}/course/themes/{s}.md", "w").write("\n".join(L))
    # one page per group: the table of its exercises, the lesson, Previous/Next group
    G = x["groups"]
    for i_, g_ in enumerate(G):
        if i_: pv = (f"{G[i_-1]['title']}", f"{gpage(x, G[i_-1])}.md")
        else: pv = (x["title"], f"{s}.md")
        if i_ < len(G) - 1: nx = (f"{G[i_+1]['title']}", f"{gpage(x, G[i_+1])}.md")
        elif k < len(THEMES) - 1: nx = (f"Next theme: {THEMES[k+1]['title']}", f"{THEMES[k+1]['slug']}.md")
        else: nx = ("Roadmap", "../ROADMAP.md")
        fm = lambda t_, l_: f"  text: {json.dumps(t_, ensure_ascii=False)}\n  link: /themes/{l_[:-3]}" if not l_.startswith("..") else f"  text: {json.dumps(t_, ensure_ascii=False)}\n  link: /ROADMAP"
        P = ["---", "prev:\n" + fm(*pv), "next:\n" + fm(*nx), "---", "",
             f"[Home](../../README.md) › [Roadmap](../ROADMAP.md) › [{x['title']}]({s}.md) › Group {i_+1} of {len(G)}", "",
             f"# {x['title']} · {g_['title']}", "", g_["about"] + (f" Lesson: {recipe_link(g_['recipe'])}." if g_["recipe"] else ""), ""]
        if i_ == 0: P += [f'<LearnCard theme="{s}" />', ""]
        P += ["Do the exercises from top to bottom. Tick each one when `./ex check` says DONE.", "",
              f'<ThemeExercises theme="{s}" group="{g_["slug"]}" />', "", '<div class="gh-only">', "",
              "| ID | Exercise | Kind | Level | Effort |", "| --- | --- | --- | --- | --- |"] + [ex_row(e) for e in gex(g_)] + ["", "</div>", "", "---", "",
              " · ".join([f"Previous: [{pv[0]}]({pv[1]})"] + ([f"[{x['title']}]({s}.md)"] if i_ else []) + [f"Next: [{nx[0]}]({nx[1]})"]), ""]
        open(f"{ROOT}/course/themes/{gpage(x, g_)}.md", "w").write("\n".join(P))


# ---------- ROADMAP.md ----------
R = ["[Home](../README.md) › Roadmap", "", "# Roadmap", "",
     "The course is a path of themes, grouped like the 6 parts of [Microsoft Learn](learn/microsoft-learn.md) *Get started with C#*. Do a Microsoft Learn part, then its theme here, **in order, at your own pace**. Move on when the \"ready\" check of a theme works without help.", "",
     '<div class="gh-only">', "",
     "![The roadmap: " + "; ".join(f"{part}: " + ", ".join(f"{x['title']} (" + ", ".join(g_["title"] for g_ in x["groups"]) + ")" for x in THEMES if x["part"] == part) for part in PARTS) + "](diagrams/roadmap.svg)", "", "</div>", "",
     "Before the first theme, read [How to read an exercise](docs/reading-an-exercise.md). You will use it for every exercise.", "",
     "<RoadmapPath />", "", '<div class="gh-only">', ""]
R += ["| # | Part | Theme | Groups | Exercises |", "| --- | --- | --- | --- | --- |"]
for x in THEMES:
    R.append(f"| {NUM[x['slug']]} | {x['part']} | [{x['title']}](themes/{x['slug']}.md) | " + ", ".join(f"[{g_['title']}](themes/{gpage(x, g_)}.md)" for g_ in x["groups"]) + f" | {len(TH_EX[x['slug']])} |")
R.append("")
R += ["</div>", "", "## After the roadmap", "", "Objects and classes come next in most courses. There are no exercises for them here yet: follow your course or Microsoft Learn, and come back to the [cookbook](cookbook/README.md) when a method needs a loop.", "",
      "---", "", "[Home](../README.md) · Next: [Getting started](docs/getting-started.md)", ""]
open(f"{ROOT}/course/ROADMAP.md", "w").write("\n".join(R))

# ---------- diagrams/roadmap.d2 (rendered to SVG by internal/tools/diagrams.sh) ----------
D = ["# Generated by internal/tools/generator (themes.py). Render: internal/tools/diagrams.sh", "...@_style", "direction: down", ""]
for p_i, part in enumerate(PARTS):
    xs = [x for x in THEMES if x["part"] == part]
    D += [f'part{p_i}: "{part}" {{', "  class: part", ""]
    for x in xs:
        gs = x["groups"]; cols = min(3, len(gs))
        D += [f'  t{NUM[x["slug"]]}: "{NUM[x["slug"]]}. {x["title"]}" {{', "    class: part", f"    grid-rows: {(len(gs) + cols - 1) // cols}", f"    grid-columns: {cols}", "    grid-gap: 16"]
        for j_, g_ in enumerate(gs, 1):
            D.append(f'    g{j_}: "{NUM[x["slug"]]}.{j_} {g_["title"]}" {{class: step; width: 230; height: 56}}')
        D += ["  }"]
    D += ["}", ""]
D += [f"part{i} -> part{i + 1}" for i in range(len(PARTS) - 1)] + [""]
os.makedirs(f"{ROOT}/course/diagrams", exist_ok=True)
open(f"{ROOT}/course/diagrams/roadmap.d2", "w").write("\n".join(D))

# ---------- progress checklist (paper) ----------
pc = ["[Home](../../README.md) › Progress checklist", "", "# My progress checklist (paper)", "",
      "Print this page if you like paper. Tick a box when it is true **without help**. (On the website, use [My progress](../progress.md) instead.)", "",
      "**Solved** = `./ex check` says DONE. **Mastered** = you also solved the mastery check alone, on another day.", ""]
for x in THEMES:
    pc += [f"## {x['title']}", ""]
    for g_ in x["groups"]:
        pc += [f"### {x['title']}: {g_['title']}", ""]
        for e in gex(g_):
            pc += [f"- [ ] [{e['id']} · {e['title']}](../exercises/{fname(e)}.md) solved", "  - [ ] mastered (another day, alone)"]
        pc.append("")
pc += ["---", "", "[Home](../../README.md) · [All exercises](../exercises/README.md)", ""]
open(f"{ROOT}/course/docs/progress-checklist.md", "w").write("\n".join(pc))

# ---------- docs/README.md: the study skills index ----------
SKILLS = [("How to read an exercise", "reading-an-exercise", "Find what goes in, what comes out, and a tiny example, before you code."),
          ("Solving a problem", "problem-solving", "Turn a problem into small steps you can write."),
          ("How to practice", "how-to-practice", "The shape of one practice session, and what to ask yourself."),
          ("Glossary", "glossary", "Every new word of the course, in plain English."),
          ("Progress checklist (paper)", "progress-checklist", "Every exercise as a box to tick on paper.")]
SK = ["[Home](../../README.md) › Study skills", "", "# Study skills", "", "How to work, not what to code: read these once, and come back when you are stuck.", "",
      "<CardList list=\"skills\" />", "", '<div class="gh-only">', ""] + [f"{i_}. [{a_}]({b_}.md): {c_}" for i_, (a_, b_, c_) in enumerate(SKILLS, 1)] + ["", "</div>", "",
      "---", "", "[Home](../../README.md) · Next: [How to read an exercise](reading-an-exercise.md)", ""]
open(f"{ROOT}/course/docs/README.md", "w").write("\n".join(SK))
RECIPE_CARDS = []
for r, (name, f_) in RECIPES.items():
    m_ = re.search(r"^# Recipe \d+ · [^—\n]+— (.+)$", open(f"{ROOT}/course/cookbook/{f_}.md", encoding="utf-8").read(), re.M)
    RECIPE_CARDS.append({"num": int(r), "title": name, "text": m_.group(1).strip() if m_ else "", "link": f"/cookbook/{f_}"})

# ---------- learn/: the theory comes from Microsoft Learn ----------
os.makedirs(f"{ROOT}/course/learn", exist_ok=True)
for old in glob.glob(f"{ROOT}/course/learn/*.md"): os.remove(old)
def theme_link(x, up="../"): return f"[{x['title']}]({up}themes/{x['slug']}.md)"
USED = {}  # module slug -> themes that practise it
for x in THEMES:
    for m_ in THEORY[x["slug"]]["modules"]: USED.setdefault(m_, []).append(x)
EP_USED = {}
for x in THEMES:
    for e_ in THEORY[x["slug"]]["episodes"]: EP_USED.setdefault(e_, []).append(x)

def ep_page(e_, up=""): return f"{up}videos/{e_}.md"
def ex_links(x, n=3, up="../"): return ", ".join(f"[{e['id']}]({up}exercises/{fname(e)}.md)" for e in TH_EX[x["slug"]][:n])

# Overview: one row per theme: theme -> Microsoft Learn -> video -> exercises (LearnFlow component)
LG = ["[Home](../../README.md) › Learn", "", "# How it fits together", "",
      "This course is for **practice**. The **theory** comes from **Microsoft Learn**, free. For each theme, follow the line from left to right: learn the idea on Microsoft Learn, watch the video, then practise here.", "",
      "<LearnFlow />", "", '<div class="gh-only">', ""]
for x in THEMES:
    th = THEORY[x["slug"]]; m0 = th["modules"][0]; e0 = th["episodes"][0]
    LG.append(f"- **{NUM[x['slug']]}. {theme_link(x)}**: learn [{MODULE[m0][1]}]({module_url(m0)}) (Part {MODULE[m0][0]}), watch [{EPISODES[e0][0]}]({ep_page(e0)}), then practise {ex_links(x)}")
LG += ["", "</div>", "", "Next: the [Microsoft Learn modules](microsoft-learn.md), the [videos](videos.md), the [certification](certification.md) and [extra exercises](quest-tracker.md).", "",
       "---", "", "[Home](../../README.md) · Next: [Microsoft Learn modules](microsoft-learn.md)", ""]
open(f"{ROOT}/course/learn/README.md", "w").write("\n".join(LG))

LM = ["[Home](../../README.md) › [Learn](README.md) › Microsoft Learn modules", "", "# Microsoft Learn modules", "",
      "Microsoft Learn teaches C# for free in **6 parts** (learning paths). Each part has short **modules**: you read a little, then try the code. This course follows the same order: after a module, do the themes listed under it.", "",
      "<MsLearnPath />", "", '<div class="gh-only">', ""]
for n, (title, ms) in MSL.items():
    LM += [f"**Part {n}: [{title}]({path_url(n)})**", ""]
    for t_, slug_ in ms:
        after = ", ".join(theme_link(x) for x in USED.get(slug_, [])) or "no exercises here"
        LM.append(f"- [{t_}]({module_url(slug_)}). Then: {after}")
    LM.append("")
LM += ["</div>", "",
       f"Prefer videos? See [Videos](videos.md). Want a certificate? See [Certification](certification.md).", "",
       "## The docs", "", f"[{TOUR[0]}]({TOUR[1]}): the official overview of the language, for later.", "",
       "---", "", "[Learn](README.md) · Next: [Videos](videos.md)", ""]
open(f"{ROOT}/course/learn/microsoft-learn.md", "w").write("\n".join(LM))

# Videos: kept episodes only, grouped like the roadmap (by the group of the first theme that uses them)
FIRST = {e_: EP_USED[e_][0] for e_ in EPISODE_ORDER}
VG = []
for part in PARTS:
    eps_ = sorted([e_ for e_ in EPISODE_ORDER if FIRST[e_]["part"] == part], key=lambda e_: (NUM[FIRST[e_]["slug"]], EPISODE_ORDER.index(e_)))
    if eps_: VG.append((part, eps_))
VNUM = {e_: i for i, e_ in enumerate([e_ for _, es in VG for e_ in es], 1)}
ORDERED = [e_ for _, es in VG for e_ in es]
LV = ["[Home](../../README.md) › [Learn](README.md) › Videos", "", "# Videos", "",
      f"[{SERIES[0]}]({SERIES[1]}) is a free video series on Microsoft Learn by Bob Tabor. Pick the video of your theme: its page says what to watch for and what to practise after. Only the episodes about the fundamentals are here.", "",
      "<VideoGallery />", "", '<div class="gh-only">', ""]
for part, eps_ in VG:
    LV += [f"{part.split(': ')[0]}: **{part.split(': ')[1]}**", ""]
    for e_ in eps_:
        LV.append(f"- **{VNUM[e_]}** [{EPISODES[e_][0]}]({ep_page(e_)}) ({EPISODES[e_][1]} min)")
    LV.append("")
LV += ["</div>", "", f"More videos, optional: [{VIDEOS[0]}]({VIDEOS[1]}).", "", "---", "", "[Microsoft Learn modules](microsoft-learn.md) · Next: [Certification](certification.md)", ""]
open(f"{ROOT}/course/learn/videos.md", "w").write("\n".join(LV))

# One page per kept episode
os.makedirs(f"{ROOT}/course/learn/videos", exist_ok=True)
for old in glob.glob(f"{ROOT}/course/learn/videos/*.md"): os.remove(old)
for i, e_ in enumerate(ORDERED):
    t_, mins = EPISODES[e_]; watch, words = NOTES[e_]
    P = ["---", "prev: false", "next: false", "---", "", f"[Home](../../../README.md) › [Learn](../README.md) › [Videos](../videos.md) › Video {VNUM[e_]}", "", f"# {t_}", "",
         f"*{SERIES[0]}*, on Microsoft Learn. {mins} minutes.", ""]
    if THUMBS[e_]: P += [f"[![Picture from the video: {t_}. Open the video on Microsoft Learn.]({THUMBS[e_]})]({episode_url(e_)})", ""]
    P += [f'<p><a class="cpf-button" href="{episode_url(e_)}">Watch on Microsoft Learn</a></p>', "",
          "## Watch for", ""] + [f"- {w}" for w in watch] + ["",
          "## Key words", "", ", ".join(f"*{w}*" for w in words) + ". See the [glossary](../../docs/glossary.md).", "",
          "## Practise after this", ""]
    for x in EP_USED[e_]:
        P.append(f"- {theme_link(x, '../../')}: start with {ex_links(x, 3, '../../')}")
    P += ["", "---", ""]
    nav_ = []
    if i: nav_.append(f"Previous: [{EPISODES[ORDERED[i-1]][0]}]({ORDERED[i-1]}.md)")
    nav_.append("[All videos](../videos.md)")
    if i < len(ORDERED) - 1: nav_.append(f"Next: [{EPISODES[ORDERED[i+1]][0]}]({ORDERED[i+1]}.md)")
    P += [" · ".join(nav_), ""]
    open(f"{ROOT}/course/learn/videos/{e_}.md", "w").write("\n".join(P))

# Certification
LC = ["[Home](../../README.md) › [Learn](README.md) › Certification", "", "# The free certification", "",
      f'<div class="cpf-card cert"><p class="cpf-kicker">Free, by freeCodeCamp and Microsoft</p><p class="cert-title">{CERT[0]}</p><p><a class="cpf-button" href="{CERT[1]}">Open it on freeCodeCamp</a></p></div>', "",
      "## What it is", "",
      f"A **free** certification you can put on your CV or LinkedIn. The training is the **6 parts** of Microsoft Learn *Get started with C#* (about 35 hours), the same parts this course follows. The exam is on freeCodeCamp.", "",
      "## How to take it", "",
      f"1. Open [{CERT[0]}]({CERT[1]}) on freeCodeCamp. It lists the 6 courses and their modules.",
      "2. Do each module on Microsoft Learn, then answer its short comprehension question on freeCodeCamp.",
      "3. At the end of each part, Microsoft Learn gives you a **trophy**. Link your Microsoft Learn account to freeCodeCamp and verify the trophy there.",
      "4. With the 6 trophies, take the **exam**: 80 multiple-choice questions, in one session.",
      "5. Pass, and you get your certification.", "",
      "Both websites are free. Rules can change: read the steps on freeCodeCamp before you start.", "",
      "## How this course helps", "",
      "- After each Microsoft Learn part, do its themes here: the [roadmap](../ROADMAP.md) is grouped the same way.",
      "- The exercises make you **write** the loops, conditions and methods the exam asks about.",
      "- `./ex check` tells you at once if your code works, so you practise more in less time.", "",
      "## Sources", ""] + [f"- [{a}]({b})" for a, b in CERT_SOURCES] + ["",
      "---", "", "[Videos](videos.md) · Next: [Extra exercises](quest-tracker.md)", ""]
open(f"{ROOT}/course/learn/certification.md", "w").write("\n".join(LC))

LQ = ["[Home](../../README.md) › [Learn](README.md) › Extra exercises", "", f"# Extra exercises: the {TRACKER['title']}", "",
      f"Finished a theme and want more? The **{TRACKER['title']}** is a free website: tick challenges as you solve them, earn XP and level up, like a game.", "",
      f"[![The {TRACKER['title']}: your level, your XP, how many challenges are done, and a searchable list of challenges.](../docs/assets/quest-tracker.jpg)]({TRACKER['url']})", "",
      f'<p><a class="cpf-button" href="{TRACKER["url"]}">Open the {TRACKER["title"]}</a></p>', "",
      "## What it offers", "",
      "- A dashboard with your level, your XP and your progress bar.", "- A list of challenges you can search and filter (all, done, remaining).",
      "- No account: progress stays in your browser. **Settings** exports a backup to move it to another computer.", "",
      "It follows the challenges of the book [The C# Player's Guide](https://csharpplayersguide.com/).", "",
      f"[Source code]({TRACKER['repo']})", "",
      "---", "", "[Certification](certification.md) · [Learn](README.md)", ""]
open(f"{ROOT}/course/learn/quest-tracker.md", "w").write("\n".join(LQ))

# ---------- internal/site/.vitepress/course.json: Microsoft Learn data for the Learn components ----------
_site = json.load(open(f"{ROOT}/internal/site/.vitepress/course.json", encoding="utf-8"))
_site["mslearn"] = [{"num": n, "title": title, "url": path_url(n),
                     "modules": [{"title": t_, "url": module_url(sl), "themes": [{"title": x["title"], "link": f"/themes/{x['slug']}"} for x in USED.get(sl, [])]} for t_, sl in ms]}
                    for n, (title, ms) in MSL.items()]
_site["videos"] = [{"group": part, "episodes": [{"num": VNUM[e_], "title": EPISODES[e_][0], "minutes": EPISODES[e_][1], "page": f"/learn/videos/{e_}", "thumb": THUMBS[e_],
                     "themes": [x["title"] for x in EP_USED[e_]]} for e_ in eps_]} for part, eps_ in VG]
_site["flow"] = [{"num": NUM[x["slug"]], "title": x["title"], "link": f"/themes/{x['slug']}", "group": x["part"],
                  "part": MODULE[THEORY[x["slug"]]["modules"][0]][0], "module": MODULE[THEORY[x["slug"]]["modules"][0]][1], "moduleUrl": module_url(THEORY[x["slug"]]["modules"][0]),
                  "video": EPISODES[THEORY[x["slug"]]["episodes"][0]][0], "videoPage": f"/learn/videos/{THEORY[x['slug']]['episodes'][0]}",
                  "exercises": len(TH_EX[x["slug"]]), "first": {"id": TH_EX[x["slug"]][0]["id"], "link": f"/exercises/{fname(TH_EX[x['slug']][0])}"}} for x in THEMES]
_site["learn"] = LEARN
_site["recipes"] = RECIPE_CARDS
_site["skills"] = [{"num": i_, "title": a_, "text": c_, "link": f"/docs/{b_}"} for i_, (a_, b_, c_) in enumerate(SKILLS, 1)]
json.dump(_site, open(f"{ROOT}/internal/site/.vitepress/course.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
