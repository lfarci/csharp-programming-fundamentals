import os
import json, os, sys, textwrap, glob
from data4 import E, X
from data5 import M, GOALS, RULES, HINTS
import data6  # noqa: F401  (adds ladder, Parsons and debugging exercises to E and M)
from data7 import DRILLS  # drill bank: same-pattern repetition
from data6 import NOTE_P
import re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RECIPES = {"01":("Counter loop","01-counter-loop"),"02":("Accumulator","02-accumulator"),"03":("Conditional accumulator","03-conditional-accumulator"),
"04":("Min/max","04-min-max"),"05":("Flag/search","05-flag-search"),"06":("Digit extraction","06-digit-extraction"),"07":("State update","07-state-update"),
"08":("Nested grid","08-nested-grid"),"09":("Input validation","09-input-validation"),"10":("Sentinel loop","10-sentinel-loop"),
"11":("Array traversal","11-array-traversal"),"12":("Build a string","12-string-building")}

def plain(t):  # markdown → plain text for code comments
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return t.replace("**", "").replace("`", "")
def pascal(slug): return "".join(w[:1].upper() + w[1:] for w in slug.split("-"))
def cls(e): return f'{e["id"]}_{pascal(e["slug"])}'
def ind(code, n):
    pad = " " * n
    return "\n".join((pad + l) if l.strip() else "" for l in code.rstrip("\n").split("\n"))
def parse_sig(sig):
    m = re.match(r"public static (\S+) (\w+)\((.*)\)", sig)
    ps = [p.strip().split() for p in m.group(3).split(",") if p.strip()]
    return m.group(1), m.group(2), ps
TYPE = {"int": "an int (whole number)", "long": "a long (big whole number)", "double": "a double (decimal number)",
        "bool": "a bool (true or false)", "string": "a string (text)", "char": "a char (one character)", "int[]": "an int[] (array of whole numbers)"}
def cslit(v):
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, list): return "new int[] { " + ", ".join(map(str, v)) + " }" if v else "new int[0]"
    if isinstance(v, str): return '"' + v.replace("\n", "\\n") + '"' if len(v) != 1 else "'" + v + "'"
    return str(v)
def shown(v):
    if isinstance(v, str) and "\n" in v: return "prints:<br>" + "<br>".join("`" + l.replace(" ", " ") + "`" for l in v.rstrip("\n").split("\n"))
    if isinstance(v, str): return f'`"{v}"`'
    if isinstance(v, float): return f"`{v:.4f}`…"
    return f"`{cslit(v)}`"
def method_job(e):
    """Plain-words description of the method(s) to write (page + starter)."""
    out = []
    for sig, _, _ in M[e["id"]]["methods"]:
        ret, name, ps = parse_sig(sig)
        ins = ", ".join(f"{p[1]}, {TYPE[p[0]]}" for p in ps) or "nothing"
        res = "the lines it writes with Console.Write / Console.WriteLine (no return)" if ret == "void" else f"{TYPE[ret]}, given back with return"
        out.append((name, sig, ins, res))
    return out
def cs_file(e, starter):
    """One exercise = one file = one static class holding the method(s) to write."""
    c = cls(e); spec = M.get(e["id"])
    H = [f"{e['id']} · {e['title']}", f"Exercise page: exercises/{fname(e)}.md"]
    if starter:
        goal = plain(GOALS[e["id"]] if spec else e["goal"]).split("\n")[0]
        H += [""] + textwrap.wrap("Goal: " + goal, 90) + [""]
        if e.get("task") == "parsons":
            H += ["YOUR JOB: the right lines are already in the method, but mixed up.", "Put them in order and remove the // in front of them."]
        elif e.get("task") == "debug":
            H += ["YOUR JOB: the method below compiles, but it has bugs.", "Run the check, read what fails, trace it on paper, then fix it."]
        if spec and not e.get("task"):
            H += ["YOUR JOB: write the method" + ("s" if len(spec["methods"]) > 1 else "") + " below, where it says TODO."]
            for name, sig, ins, res in method_job(e):
                H += [f"  {name}", f"    input  (parameters): {ins}", f"    result ({'prints' if sig.split()[2] == 'void' else 'return'}){' ' if sig.split()[2] == 'void' else ''}    : {res}"]
        elif not spec:
            H += ["YOUR JOB: write the whole program inside Run(), where it says TODO.",
                  "Use Console.ReadLine() to read and Console.WriteLine() to print, as usual."]
        H += ["", f"Check your code:  ./ex check {e['id']}     (Windows: .\\ex check {e['id']})",
              f"Try it yourself:  ./ex run {e['id']}"]
    body = []
    if spec:
        for i, (sig, code, todo) in enumerate(spec["methods"]):
            if not starter: inner = code
            elif todo.startswith(NOTE_P): inner = "// " + todo[len(NOTE_P):]
            else: inner = ("// TODO: write your code here.\n" + todo).rstrip()
            body += ([""] if i else []) + [sig, "{", ind(inner, 4), "}"]
    else:
        inner = "// TODO: write your code here." if starter else e["code"]
        body += ["public static void Run()", "{", ind(inner, 4), "}"]
    L = ["namespace Practice", "{"] + ["    // " + h if h else "    //" for h in H] + [f"    public static class {c}", "    {", ind("\n".join(body), 8), "    }", "}", ""]
    return "\n".join(L)

byid = {e["id"]: e for e in E}
for e in E:  # guard: every prerequisite must exist
    missing = [p for p in e["pre"] if p not in byid]
    if missing: sys.exit(f"{e['id']}: unknown prerequisite(s) {missing}")
def fname(e): return f'{e["id"]}-{e["slug"]}'
def stars(n): return {1: "easy", 2: "medium", 3: "hard"}[n]
def rlinks(e, base="../cookbook/"):
    return ", ".join(f"[{RECIPES[r][0]}]({base}{RECIPES[r][1]}.md)" for r in e["recipes"]) or "—"
def plinks(e, base=""):
    return ", ".join(f"[{p}]({base}{fname(byid[p])}.md)" for p in e["pre"]) or "—"

for d in ["exercises", "solutions", "tools/starters", "tests/Practice.Tests"]: os.makedirs(f"{ROOT}/{d}", exist_ok=True)
for old in glob.glob(f"{ROOT}/solutions/*.cs") + glob.glob(f"{ROOT}/tools/starters/*.cs"): os.remove(old)
FAMORDER = "BCLAGDSPMRTFEKN"
def skey(e): k = e.get("sort", e["id"]); return (FAMORDER.index(k[0]), k)
ORDER = sorted(E, key=skey)
POS = {e["id"]: i for i, e in enumerate(ORDER)}
def nav(e):
    i = POS[e["id"]]; parts = []
    if i > 0: parts.append(f"Previous: [{ORDER[i-1]['id']} · {ORDER[i-1]['title']}]({fname(ORDER[i-1])}.md)")
    parts.append("[All exercises](README.md)")
    if i < len(ORDER) - 1: parts.append(f"Next: [{ORDER[i+1]['id']} · {ORDER[i+1]['title']}]({fname(ORDER[i+1])}.md)")
    return " · ".join(parts)
tests = []
for e in E:
    paper = e.get("paper", False)
    src = "Custom"
    if e.get("teacher"): src += f" · teacher topic: {e['teacher']}"
    if e.get("euler"): src += f" · prepares [Project Euler #{e['euler']}](https://projecteuler.net/problem={e['euler']})"
    L = ["[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › " + e["id"], "", f"# {e['id']} · {e['title']}", "",
         f"| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |", "| --- | --- | --- | --- | --- | --- |",
         f"| {e['level']} | {stars(e['stars'])} | {e['step']} | {rlinks(e)} | {plinks(e)} | {src} |", "",
         "## Goal", "", GOALS.get(e["id"], e["goal"]), ""]
    if paper:
        L += ["## Start and check", "", "This one is on **paper**: no code to write. When you are done, compare with the answer key (link at the bottom).", ""]
    else:
        L += ["## Start and check", "", "```bash", f"./ex start {e['id']}     # creates practice/{cls(e)}.cs (never overwrites your work)", f"./ex check {e['id']}     # tests your code with the examples below", "```", "",
              f"On Windows, type `.\\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).", ""]
        if e.get("task") == "parsons":
            L += ["**Your job:** the file already holds **all** the lines you need, mixed up and turned into comments (`//`). Put them in order and remove the `//`. No new code to invent: this trains *reading* the pattern.", ""]
        elif e.get("task") == "debug":
            L += ["**Your job:** the file already holds code that compiles but gives wrong answers. Run `./ex check`, read which example fails, trace that example on paper, then fix the bug. Change as little as you can.", ""]
        elif e["id"] in M:
            L += ["**Your job:** fill in " + ("these methods" if len(M[e["id"]]["methods"]) > 1 else "this method") + " in the file. The *parameters* are its input; " + ("what it **prints** is its result (it has no `return`)." if all(parse_sig(s_)[0] == "void" for s_, _, _ in M[e["id"]]["methods"]) else "what you `return` is its result."), ""]
            for name, sig, ins, res in method_job(e):
                L += [f"- `{sig.replace('public static ', '')}`: input = {ins}; result = {res}."]
            L += [""]
        else:
            L += ["**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.", ""]
    if e["id"] in M:
        L += ["## Examples", "", "Your method must give these results. `./ex check` tests all of them.", "", "| Call | Result |", "| --- | --- |"]
        for name, args, exp in M[e["id"]]["cases"]:
            L.append(f"| `{name}({', '.join(cslit(a) for a in args)})` | {shown(exp)} |")
        L += [""]
    elif e["examples"]:
        L += ["## Examples", "", "The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.", ""]
        for i, (inp, out) in enumerate(e["examples"], 1):
            shown_in = ", ".join(f"`{x}`" if x else "*(empty)*" for x in inp)
            L += [f"**Example {i}** — input: {shown_in}", "", "```text"] + (out if any(out) else ["(nothing is printed)"]) + ["```", ""]
    if e.get("note"): L += [f"> {e['note']}", ""]
    L += ["## Edge cases to test", ""] + [f"- {x}" for x in e["edge"]] + [""]
    L += ["## Rules", ""] + [f"- {x}" for x in RULES.get(e["id"], e["constraints"])] + ["- No LINQ and no ready-made helpers: you write every step yourself.", ""]
    L += ["## Before coding", "", ("Fill the [reading worksheet](../docs/reading-an-exercise.md#4-the-worksheet-copy-it): what goes in? what comes out? a tiny example by hand?" if not e["recipes"] else "Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?"), ""]
    L += ["## Hints (open one at a time)", ""]
    for i, h in enumerate(HINTS.get(e["id"], e["hints"]), 1):
        L += [f"<details><summary>Hint {i}</summary>", "", h, "", "</details>", ""]
    L += ["## Mastery check", "", "Solve this variation **alone**, on another day:", "", e["mastery"], ""]
    sol = f"../solutions/{fname(e)}.md" if paper else f"../solutions/{cls(e)}.cs"
    L += ["## Solution", "", f"Only after a real try: [open the solution for {e['id']}]({sol}). Your solution can be different and still correct!", "",
          "---", "", nav(e), ""]
    open(f"{ROOT}/exercises/{fname(e)}.md","w").write("\n".join(L))
    if paper:
        open(f"{ROOT}/solutions/{fname(e)}.md","w").write(f"[Home](../README.md) › [Solutions](README.md) › {e['id']}\n\n# Answer key · {e['id']} {e['title']}\n\n{e['answer']}\n\n[Back to the exercise](../exercises/{fname(e)}.md)\n")
    else:
        open(f"{ROOT}/solutions/{cls(e)}.cs", "w").write(cs_file(e, starter=False))
        open(f"{ROOT}/tools/starters/{cls(e)}.cs", "w").write(cs_file(e, starter=True))
        if e["id"] not in M: tests += e["examples"]
# single source for the checker (tools/checker) and CI
def jcase(name, args, exp): return {"method": name, "args": args, "expected": exp}
cj = [{"id": e["id"], "name": fname(e), "class": cls(e), "title": e["title"], "paper": bool(e.get("paper")),
       "kind": "paper" if e.get("paper") else ("method" if e["id"] in M else "output"),
       "methods": [parse_sig(sig)[1] for sig, _, _ in M[e["id"]]["methods"]] if e["id"] in M else [],
       "cases": [jcase(*c) for c in M[e["id"]]["cases"]] if e["id"] in M else [],
       "checkHint": e.get("check_hint", ""),
       "step": e["step"], "drills": [n for n, _, ids in DRILLS if e["id"] in ids],
       "examples": [{"input": inp, "expected": [o for o in out if o.strip()]} for inp, out in (e["examples"] or [])]}
      for e in ORDER]
json.dump(cj, open(f"{ROOT}/tools/exercises.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
# data for the website (.vitepress): sidebar, "Mark as done", progress page
os.makedirs(f"{ROOT}/.vitepress", exist_ok=True)
site = {"exercises": [{"id": e["id"], "title": e["title"], "link": f"/exercises/{fname(e)}", "step": e["step"],
                       "level": e["level"], "paper": bool(e.get("paper")),
                       "drills": [n for n, _, ids in DRILLS if e["id"] in ids]} for e in ORDER],
        "drillSets": [{"name": n, "recipe": r, "ids": ids} for n, r, ids in DRILLS]}
json.dump(site, open(f"{ROOT}/.vitepress/course.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# ---------- tests: one plain xUnit file per exercise ----------
def cs_str(v): return '"' + v.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'
def lit(v, t):
    if t == "long": return f"{v}L"
    if t == "double": return repr(float(v))
    if t == "bool": return "true" if v else "false"
    if t == "string": return cs_str(v)
    if t == "char": return "'" + v.replace("\\", "\\\\").replace("'", "\\'") + "'"
    if t == "int[]": return "new[] { " + ", ".join(map(str, v)) + " }" if v else "new int[0]"
    return str(v)
def show(v, t):  # for the test name
    if t == "int[]": return "[" + ", ".join(map(str, v)) + "]"
    if t == "string": return '"' + v + '"'
    if t == "char": return "'" + v + "'"
    if t == "bool": return "true" if v else "false"
    return str(v)
def attr(t): return t.replace("\\", "\\\\").replace('"', '\\"')
def test_file(e):
    c = cls(e); out = [f"// Tests for {e['id']} · {e['title']}", f"// Exercise page: exercises/{fname(e)}.md",
         f"// Your code:     practice/{c}.cs", f"// Run them:      ./ex check {e['id']}", "//", "// Generated from tools/generator (edit the exercise there, not here).",
         "namespace Practice.Tests", "{", f"    public class {c}Tests", "    {"]
    hint = e.get("check_hint")
    if hint: out += [f"        const string Hint = {cs_str(hint)};", ""]
    hp = ", hint: Hint" if hint else ""
    k = 0
    if e["id"] in M:
        sigs = {parse_sig(sg)[1]: parse_sig(sg) for sg, _, _ in M[e["id"]]["methods"]}
        for name, args, exp in M[e["id"]]["cases"]:
            k += 1; ret, _, ps = sigs[name]
            call = f"{c}.{name}({', '.join(lit(a, p[0]) for a, p in zip(args, ps))})"
            shown_call = f"{name}({', '.join(show(a, p[0]) for a, p in zip(args, ps))})"
            if ret == "void":
                lines_ = exp.rstrip("\n").split("\n") if exp.strip("\n") else []
                what = "prints nothing but a line break" if not lines_ else (f'prints "{lines_[0]}"' if len(lines_) == 1 else f"prints {len(lines_)} lines")
                out += [f'        [Fact(DisplayName = "{e["id"]} example {k}: {attr(shown_call)} {attr(what)}")]', f"        public void Example{k}() => Expect.Prints("]
                if not lines_ or len(lines_) == 1:
                    out[-1] += f'{cs_str(lines_[0] if lines_ else "")}, () => {call}{hp});'
                else:
                    out += ['            """'] + ["            " + l.rstrip() for l in lines_] + [f'            """, () => {call}{hp});']
            else:
                out += [f'        [Fact(DisplayName = "{e["id"]} example {k}: {attr(shown_call)} returns {attr(show(exp, ret))}")]',
                        f"        public void Example{k}() => Expect.Returns({lit(exp, ret)}, () => {call}{hp});"]
            out.append("")
    else:
        for inp, outl in e["examples"]:
            k += 1; want = [o for o in outl if o.strip()]
            shown_in = ", ".join(x if x else "(empty)" for x in inp) or "no input"
            out += [f'        [Fact(DisplayName = "{e["id"]} example {k}: input {attr(shown_in)} prints {attr(chr(34) + want[-1] + chr(34)) if want else "nothing"}")]',
                    f"        public void Example{k}() => Expect.Output(",
                    f"            input: [{', '.join(cs_str(x) for x in inp)}],",
                    f"            lines: [{', '.join(cs_str(x) for x in want)}],",
                    f"            run: () => {c}.Run(){hp});", ""]
    if out[-1] == "": out.pop()
    return "\n".join(out + ["    }", "}", ""])
TD = f"{ROOT}/tests/Practice.Tests/Exercises"
os.makedirs(TD, exist_ok=True)
for old in glob.glob(f"{TD}/*.cs"): os.remove(old)
for e in ORDER:
    if not e.get("paper"): open(f"{TD}/{cls(e)}Tests.cs", "w").write(test_file(e))

# ---------- inventory ----------
FAM = [("B","Basics: input → compute → output","Step 1–2"),("C","Conditions","Step 3"),("L","Loop mechanics","Step 4a"),
("A","Accumulators","Step 4b"),("G","2D drawings (nested loops)","Step 4c"),("D","Digits","Step 4d"),("S","Changing state","Step 4d"),
("P","Search & primes","Step 4d"),("M","Combine (mixed)","Step 4"),("R","Arrays","Step 6"),("T","Text","Step 6"),
("F","Files","Step 5"),("E","Exceptions","Step 7"),("K","Collections","Step 9"),("N","Methods","Step 10")]
lvl_icon = {"Guided":"Guided","Independent":"Independent","Challenge":"Challenge"}
out = ["[Home](../README.md) › [Roadmap](../ROADMAP.md) › Exercises", "", "# Exercise inventory", "", "Track what you have done with the [progress checklist](../docs/progress-checklist.md).", "",
"One table for **every** exercise: our own original exercises, a few Project Euler milestones and the teacher's topics.",
"Each custom exercise adds **one** new difficulty. Pick the next one whose prerequisites you have done.", "",
"- **Guided** — small steps, hints help a lot.  **Independent** — same idea, alone.  **Challenge** — new problem, combine recipes.",
"- Effort for a true beginner: easy, medium or hard.",
"- Solutions are in [`solutions/`](../solutions/README.md). Try first, look later.",
"- *The C# Player's Guide* is a **parallel track**, not part of this list: read the book level named in each [roadmap](../ROADMAP.md) step alongside it. Its challenges are tracked in [C# Quest Tracker](https://lfarci.github.io/csharp-quest-tracker/).",
"- Before any exercise, read it with [How to read an exercise](../docs/reading-an-exercise.md).", ""]
from collections import Counter
cnt = Counter(); lv = Counter(e["level"] for e in E)
for x in X: cnt[x["source"].split(" L")[0].split(" #")[0]] += 1
out += ["## Counts", "", "| Source | Exercises |", "| --- | ---: |", f"| Custom (this repo) | {len(E)} |"]
for k in ["Project Euler","Teacher topic"]: out.append(f"| {k} | {cnt[k]} |")
out += [f"| **Total** | **{len(E)+len(X)}** |", "",
        f"Custom by level: {lv['Guided']} guided · {lv['Independent']} independent · {lv['Challenge']} challenge.", ""]
out += ["## Map of the families", "", "```mermaid", "flowchart LR", "    accTitle: Map of the exercise families", "    accDescr: Basics lead to conditions, then loop mechanics. Loop mechanics lead to accumulators, state and exceptions. Accumulators lead to 2D drawings, digits, search and primes, combine, and arrays. Digits lead to combine, which leads to methods. Arrays lead to text, files and collections."]
out += ['    B["B · Basics"] --> C["C · Conditions"] --> L["L · Loop mechanics"]',
        '    L --> A["A · Accumulators"]', '    A --> G["G · 2D drawings"]', '    A --> D["D · Digits"]', '    L --> S["S · State"]',
        '    A --> P["P · Search & primes"]', '    D --> M["M · Combine: Armstrong"]', '    A --> M',
        '    A --> R["R · Arrays"] --> T["T · Text"]', '    R --> F["F · Files"]', '    L --> E["E · Exceptions"]',
        '    R --> K["K · Collections"]', '    M --> N["N · Methods"]', "```", "",
        "See the full [graph of every exercise and its prerequisites](dependency-graph.md).", ""]
out += ["## Drill sets (same pattern, many times)", "",
        "Want to practise one pattern today? Do the exercises of **one row**, in order, in one or two short sessions. They change only small details, so your brain sees the **same pattern** again and again. Check each one with `./ex check` before the next.", "",
        "| Drill | Recipe | Exercises, in order |", "| --- | --- | --- |"]
for name, r, ids in DRILLS:
    for i in ids: assert i in byid, f"drill set lists unknown exercise {i}"
    out.append(f"| {name} | [{RECIPES[r][0]}](../cookbook/{RECIPES[r][1]}.md) | " + " → ".join(f"[{i}]({fname(byid[i])}.md)" for i in ids) + " |")
out += ["", "Tip: if one feels hard, do the one before it again. If one feels easy, skip ahead. See [How to practice](../docs/how-to-practice.md#drill-sets).", ""]
out += ["## Custom exercises", ""]
for f, name, step in FAM:
    rows = [e for e in ORDER if e["id"].startswith(f)]
    out += [f"### {f} · {name} ({step})", "", "| ID | Exercise | Level | Effort | Recipes | Before | Source |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for e in rows:
        s = "Custom"
        if e.get("teacher"): s += f" · teacher: {e['teacher']}"
        if e.get("euler"): s += f" → PE #{e['euler']}"
        if e.get("paper"): s += " · paper"
        if e.get("task") == "parsons": s += " · arrange the lines"
        if e.get("task") == "debug": s += " · fix the bugs"
        out.append(f"| {e['id']} | [{e['title']}]({fname(e)}.md) | {lvl_icon[e['level']]} | {stars(e['stars'])} | {rlinks(e)} | {', '.join(e['pre']) or '—'} | {s} |")
    out.append("")
out += ["## Project Euler (milestones, not daily homework)", "", "| ID | Problem | Roadmap step | Skills | Do first | Effort |", "| --- | --- | --- | --- | --- | --- |"]
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
pc = ["[Home](../README.md) › Progress checklist", "", "# My progress checklist", "",
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
       "- [ ] I can explain every line of my code to someone else.", "", "---", "", "[Home](../README.md) · [All exercises](../exercises/README.md)", ""]
open(f"{ROOT}/docs/progress-checklist.md","w").write("\n".join(pc))

# ---------- dependency graph ----------
g = ["[Home](../README.md) › [Exercises](README.md) › Dependency graph", "", "# Exercise dependency graph", "", "An arrow `X → Y` means: do X before Y. Colours: green = guided, blue = independent, purple = challenge. Thick border = teacher topic. The same information is in the [inventory](README.md) tables, as text.", ""]
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
g += ["---", "", "[All exercises](README.md) · [Roadmap](../ROADMAP.md)", ""]
open(f"{ROOT}/exercises/dependency-graph.md","w").write("\n".join(g))
print("generated", len(E), "exercises,", len(tests), "example runs,", sum(len(m["cases"]) for m in M.values()), "method cases")
