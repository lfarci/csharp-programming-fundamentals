import json, os, sys
from data4 import E, X
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RECIPES = {"01":("Counter loop","01-counter-loop"),"02":("Accumulator","02-accumulator"),"03":("Conditional accumulator","03-conditional-accumulator"),
"04":("Min/max","04-min-max"),"05":("Flag/search","05-flag-search"),"06":("Digit extraction","06-digit-extraction"),"07":("State update","07-state-update"),
"08":("Nested grid","08-nested-grid"),"09":("Input validation","09-input-validation"),"10":("Sentinel loop","10-sentinel-loop"),
"11":("Array traversal","11-array-traversal"),"12":("Build a string","12-string-building")}
byid = {e["id"]: e for e in E}
def fname(e): return f'{e["id"]}-{e["slug"]}'
def stars(n): return "⭐"*n
def rlinks(e, base="../cookbook/"):
    return ", ".join(f"[{RECIPES[r][0]}]({base}{RECIPES[r][1]}.md)" for r in e["recipes"]) or "—"
def plinks(e, base=""):
    return ", ".join(f"[{p}]({base}{fname(byid[p])}.md)" for p in e["pre"]) or "—"

os.makedirs(f"{ROOT}/exercises", exist_ok=True); os.makedirs(f"{ROOT}/solutions", exist_ok=True)
FAMORDER = "BCLAGDSPMRTFEKN"
ORDER = sorted(E, key=lambda e: (FAMORDER.index(e["id"][0]), e["id"]))
POS = {e["id"]: i for i, e in enumerate(ORDER)}
def nav(e):
    i = POS[e["id"]]; parts = []
    if i > 0: parts.append(f"⬅️ Previous: [{ORDER[i-1]['id']} · {ORDER[i-1]['title']}]({fname(ORDER[i-1])}.md)")
    parts.append("📚 [All exercises](README.md)")
    if i < len(ORDER) - 1: parts.append(f"Next: [{ORDER[i+1]['id']} · {ORDER[i+1]['title']}]({fname(ORDER[i+1])}.md) ➡️")
    return " · ".join(parts)
tests = []
for e in E:
    paper = e.get("paper", False)
    src = "Custom"
    if e.get("teacher"): src += f" · teacher topic: {e['teacher']}"
    if e.get("euler"): src += f" · prepares [Project Euler #{e['euler']}](https://projecteuler.net/problem={e['euler']})"
    L = ["🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › " + e["id"], "", f"# {e['id']} · {e['title']}", "",
         f"| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |", "| --- | --- | --- | --- | --- | --- |",
         f"| {e['level']} | {stars(e['stars'])} | {e['step']} | {rlinks(e)} | {plinks(e)} | {src} |", "",
         "## 🎯 Goal", "", e["goal"], ""]
    if e["examples"]:
        L += ["## 🧪 Examples", "", "The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.", ""]
        for i, (inp, out) in enumerate(e["examples"], 1):
            shown_in = ", ".join(f"`{x}`" if x else "*(empty)*" for x in inp)
            L += [f"**Example {i}** — input: {shown_in}", "", "```text"] + (out if any(out) else ["(nothing is printed)"]) + ["```", ""]
    if e.get("note"): L += [f"> ℹ️ {e['note']}", ""]
    L += ["## ⚠️ Edge cases to test", ""] + [f"- {x}" for x in e["edge"]] + [""]
    L += ["## 📏 Rules", ""] + [f"- {x}" for x in e["constraints"]] + ["- No LINQ and no ready-made helpers: you write every step yourself.", ""]
    L += ["## 🗺️ Before coding", "", ("Fill the [reading worksheet](../docs/reading-an-exercise.md#4-the-worksheet-copy-it): what goes in? what comes out? a tiny example by hand?" if not e["recipes"] else "Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?"), ""]
    L += ["## 💡 Hints (open one at a time)", ""]
    for i, h in enumerate(e["hints"], 1):
        L += [f"<details><summary>Hint {i}</summary>", "", h, "", "</details>", ""]
    L += ["## ✅ Mastery check", "", "Solve this variation **alone**, on another day:", "", e["mastery"], ""]
    sol = f"../solutions/{fname(e)}.{'md' if paper else 'cs'}"
    L += ["## 🔑 Solution", "", f"Only after a real try: [open the solution for {e['id']}]({sol}). Your solution can be different and still correct!", "",
          "---", "", nav(e), ""]
    open(f"{ROOT}/exercises/{fname(e)}.md","w").write("\n".join(L))
    if paper:
        open(f"{ROOT}/solutions/{fname(e)}.md","w").write(f"🏠 [Home](../README.md) › 🔑 [Solutions](README.md) › {e['id']}\n\n# Answer key · {e['id']} {e['title']}\n\n{e['answer']}\n\n⬅️ [Back to the exercise](../exercises/{fname(e)}.md)\n")
    else:
        head = f"// {e['id']} · {e['title']}\n// Exercise: exercises/{fname(e)}.md\n// Run: dotnet run solutions/{fname(e)}.cs   (.NET 10+), or paste into practice/Program.cs\n\n"
        open(f"{ROOT}/solutions/{fname(e)}.cs","w").write(head + e["code"])
        for inp, out in e["examples"]:
            tests.append({"file": f"{fname(e)}.cs", "input": inp, "expected": [o for o in out if o.strip()]})
json.dump(tests, open(f"{ROOT}/solutions/tests.json","w"), indent=1)

# ---------- inventory ----------
FAM = [("B","Basics: input → compute → output","Step 1–2"),("C","Conditions","Step 3"),("L","Loop mechanics","Step 4a"),
("A","Accumulators","Step 4b"),("G","2D drawings (nested loops)","Step 4c"),("D","Digits","Step 4d"),("S","Changing state","Step 4d"),
("P","Search & primes","Step 4d"),("M","Combine (mixed)","Step 4"),("R","Arrays","Step 6"),("T","Text","Step 6"),
("F","Files","Step 5"),("E","Exceptions","Step 7"),("K","Collections","Step 9"),("N","Methods","Step 10")]
lvl_icon = {"Guided":"🟢 Guided","Independent":"🔵 Independent","Challenge":"🟣 Challenge"}
out = ["🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 Exercises", "", "# 📚 Exercise inventory", "", "✅ Track what you have done with the [progress checklist](../docs/progress-checklist.md).", "",
"One table for **every** exercise: our own original exercises, a few Project Euler milestones and the teacher's topics.",
"Each custom exercise adds **one** new difficulty. Pick the next one whose prerequisites you have done.", "",
"- 🟢 **Guided** — small steps, hints help a lot.  🔵 **Independent** — same idea, alone.  🟣 **Challenge** — new problem, combine recipes.",
"- ⭐ to ⭐⭐⭐ = effort for a true beginner.",
"- Solutions are in [`solutions/`](../solutions/README.md). Try first, look later.",
"- 📖 *The C# Player's Guide* is a **parallel track**, not part of this list: read the book level named in each [roadmap](../ROADMAP.md) step alongside it. Its challenges are tracked in [C# Quest Tracker](https://lfarci.github.io/csharp-quest-tracker/).",
"- 🔎 Before any exercise, read it with [How to read an exercise](../docs/reading-an-exercise.md).", ""]
from collections import Counter
cnt = Counter(); lv = Counter(e["level"] for e in E)
for x in X: cnt[x["source"].split(" L")[0].split(" #")[0]] += 1
out += ["## Counts", "", "| Source | Exercises |", "| --- | ---: |", f"| Custom (this repo) | {len(E)} |"]
for k in ["Project Euler","Teacher topic"]: out.append(f"| {k} | {cnt[k]} |")
out += [f"| **Total** | **{len(E)+len(X)}** |", "",
        f"Custom by level: 🟢 {lv['Guided']} guided · 🔵 {lv['Independent']} independent · 🟣 {lv['Challenge']} challenge.", ""]
out += ["## Map of the families", "", "```mermaid", "flowchart LR", "    accTitle: Map of the exercise families", "    accDescr: Basics lead to conditions, then loop mechanics. Loop mechanics lead to accumulators, state and exceptions. Accumulators lead to 2D drawings, digits, search and primes, combine, and arrays. Digits lead to combine, which leads to methods. Arrays lead to text, files and collections."]
out += ['    B["B · Basics"] --> C["C · Conditions"] --> L["L · Loop mechanics"]',
        '    L --> A["A · Accumulators"]', '    A --> G["G · 2D drawings"]', '    A --> D["D · Digits"]', '    L --> S["S · State"]',
        '    A --> P["P · Search & primes"]', '    D --> M["M · Combine: Armstrong"]', '    A --> M',
        '    A --> R["R · Arrays"] --> T["T · Text"]', '    R --> F["F · Files"]', '    L --> E["E · Exceptions"]',
        '    R --> K["K · Collections"]', '    M --> N["N · Methods"]', "```", "",
        "Full exercise-by-exercise graph: [dependency-graph.md](dependency-graph.md).", ""]
out += ["## Custom exercises", ""]
for f, name, step in FAM:
    rows = [e for e in E if e["id"].startswith(f)]
    out += [f"### {f} · {name} ({step})", "", "| ID | Exercise | Level | ⭐ | Recipes | Before | Source |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for e in rows:
        s = "Custom"
        if e.get("teacher"): s += f" · teacher: {e['teacher']}"
        if e.get("euler"): s += f" → PE #{e['euler']}"
        if e.get("paper"): s += " · 📝 paper"
        out.append(f"| {e['id']} | [{e['title']}]({fname(e)}.md) | {lvl_icon[e['level']]} | {stars(e['stars'])} | {rlinks(e)} | {', '.join(e['pre']) or '—'} | {s} |")
    out.append("")
out += ["## Project Euler (milestones, not daily homework)", "", "| ID | Problem | Roadmap step | Skills | Do first | ⭐ |", "| --- | --- | --- | --- | --- | --- |"]
for x in X:
    if x["source"].startswith("Project"):
        out.append(f"| {x['id']} | [{x['source']}: {x['title']}]({x['url']}) | {x['step']} | {x['skills']} | {x['pre']} | {stars(x['stars'])} |")
out += ["", "Tip: always start with a small version (below 10, up to 100) where you can check the answer by hand.", "",
        "## Teacher topics", "", "Exact statements are not copied here. Use them as **assessments** once the prerequisites are done.", "",
        "| ID | Topic | Matching exercises | Recipes | Note |", "| --- | --- | --- | --- | --- |"]
for x in X:
    if x["source"].startswith("Teacher"):
        out.append(f"| {x['id']} | {x['title']} | {x['pre']} | {x['skills']} | {x['note']} |")
out += ["", "## When stuck", "", "1. Go back to the recipe in the [cookbook](../cookbook/README.md).", "2. Solve a smaller example on paper and fill a trace table.",
        "3. Use the unstuck techniques in [How to read an exercise](../docs/reading-an-exercise.md#5-when-you-are-stuck).", "4. Open **one** hint. Wait. Try again.", "5. Still stuck? Do the exercise listed in *Before*.", "", "See also [How to practice](../docs/how-to-practice.md)."]
open(f"{ROOT}/exercises/README.md","w").write("\n".join(out)+"\n")

# ---------- progress checklist ----------
pc = ["🏠 [Home](../README.md) › ✅ Progress checklist", "", "# ✅ My progress checklist", "",
      "Print this page, or copy it into a notes file. Tick a box when it is true **without help**.", "",
      "For each exercise: **Solved** = it works and matches the examples. **Mastered** = you also solved the mastery check alone, on another day.", ""]
for f_, name, step in FAM:
    rows = [e for e in ORDER if e["id"].startswith(f_)]
    if not rows: continue
    pc += [f"## {f_} · {name} ({step})", ""]
    for e in rows:
        pc += [f"- [ ] [{e['id']} · {e['title']}](../exercises/{fname(e)}.md) solved", "  - [ ] mastered (another day, alone)"]
    pc.append("")
pc += ["## Milestones", "", "- [ ] I can trace a loop on paper (L01, L02).", "- [ ] I can solve factorial, Fibonacci and Armstrong from a blank file.",
       "- [ ] I can explain every line of my code to someone else.", ""]
open(f"{ROOT}/docs/progress-checklist.md","w").write("\n".join(pc))

# ---------- dependency graph ----------
g = ["🏠 [Home](../README.md) › 📚 [Exercises](README.md) › Dependency graph", "", "# 🕸️ Exercise dependency graph", "", "An arrow `X → Y` means: do X before Y. Colours: green = guided, blue = independent, purple = challenge. Thick border = teacher topic. The same information is in the [inventory](README.md) tables, as text.", ""]
def graph(ids, title):
    s = [f"## {title}", "", "```mermaid", "flowchart LR", f"    accTitle: {title}", "    accDescr: Each box is one exercise. An arrow from X to Y means do X before Y. The same order is written as text in the Before column of the inventory.",
         "    classDef guided fill:#d8f5d0,stroke:#2e7d32", "    classDef indep fill:#d6e8ff,stroke:#1565c0", "    classDef chall fill:#ead9ff,stroke:#6a1b9a",
         "    classDef teacher stroke-width:4px"]
    for i in ids:
        e = byid[i]; cls = {"Guided":"guided","Independent":"indep","Challenge":"chall"}[e["level"]]
        s.append(f'    {i}["{i}<br/>{e["title"].replace(chr(34),"")}"]:::{cls}')
        if e.get("teacher"): s.append(f"    class {i} teacher")
    for i in ids:
        for p in byid[i]["pre"]:
            if p in ids: s.append(f"    {p} --> {i}")
    return s + ["```", ""]
loopids = [e["id"] for e in E if e["id"][0] in "LADSPMG"]
g += graph(loopids, "Loops: from counting to Armstrong (step 4)")
g += graph([e["id"] for e in E if e["id"][0] in "BC"] + ["L01","L03"], "Before loops (steps 1–3)")
g += graph([e["id"] for e in E if e["id"][0] in "RTFEKN"] + ["A01","A02","C02","L05","L07","M02"], "After loops (steps 5–10)")
open(f"{ROOT}/exercises/dependency-graph.md","w").write("\n".join(g))
print("generated", len(E), "exercises,", len(tests), "tests")
