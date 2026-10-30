import os
import json, os, sys, textwrap, glob
from data4 import E, X
from data5 import M, GOALS, RULES, HINTS
import data6  # noqa: F401  (adds ladder, Parsons and debugging exercises to E and M)
from data7 import DRILLS  # drill bank: same-pattern repetition
import data8  # noqa: F401  (search drills, Methods and Errors exercises)
from data9 import EDGE  # edge-case tests with their own hint
from data6 import NOTE_P
from themes import THEMES, BYSLUG, GROUP
import re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # the repo
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
for e in E:  # guard: every prerequisite must exist, every exercise sits in exactly one group (themes.py)
    missing = [p for p in e["pre"] if p not in byid]
    if missing: sys.exit(f"{e['id']}: unknown prerequisite(s) {missing}")
    if e["id"] not in GROUP: sys.exit(f"{e['id']}: not listed in any group of internal/tools/generator/themes.py")
    e["theme"], e["group"] = GROUP[e["id"]][0]["slug"], GROUP[e["id"]][1]["slug"]
for i_ in GROUP:
    if i_ not in byid: sys.exit(f"themes.py lists {i_}, which no data file defines")
def fname(e): return f'{e["id"]}-{e["slug"]}'
def kind(e):
    if e.get("paper"): return "paper"
    if e.get("task") == "parsons": return "arrange the lines"
    if e.get("task") == "debug": return "fix the bugs"
    return "write code"
def stars(n): return {1: "easy", 2: "medium", 3: "hard"}[n]
def rlinks(e, base="../cookbook/"):
    return ", ".join(f"[{RECIPES[r][0]}]({base}{RECIPES[r][1]}.md)" for r in e["recipes"]) or "—"
def plinks(e, base=""):
    return ", ".join(f"[{p}]({base}{fname(byid[p])}.md)" for p in e["pre"]) or "—"

for d in ["course/exercises", "course/answer-keys", "internal/solutions", "internal/tools/starters", "internal/tests/Practice.Tests"]: os.makedirs(f"{ROOT}/{d}", exist_ok=True)
for old in glob.glob(f"{ROOT}/internal/solutions/*.cs") + glob.glob(f"{ROOT}/internal/tools/starters/*.cs"): os.remove(old)
# Course order = the groups of themes.py, in order. Each `pre` must come earlier.
ORDER = [byid[i_] for x_ in THEMES for g_ in x_["groups"] for i_ in g_["ids"]]
POS = {e["id"]: i for i, e in enumerate(ORDER)}
for e in ORDER:
    late = [p for p in e["pre"] if POS[p] > POS[e["id"]]]
    if late: sys.exit(f"{e['id']}: its prerequisite(s) {late} come later in the course order (themes.py)")
TH_LIST = {x["slug"]: [e for e in ORDER if e["theme"] == x["slug"]] for x in THEMES}
def where(e):
    th, gr = GROUP[e["id"]]; lst = TH_LIST[th["slug"]]; gl = [x for x in lst if x["group"] == gr["slug"]]
    return th, gr, lst.index(e) + 1, len(lst), gl.index(e) + 1, len(gl)
def gpage(th, gr): return f"{th['slug']}-{gr['slug']}"   # one page per group: themes/loops-count.md -> /themes/loops-count
def gref(th, gr, up="../"): return f"{up}themes/{gpage(th, gr)}.md"
def neighbours(e):
    """Previous/Next inside the theme, in course order; at the ends, the theme pages."""
    th = GROUP[e["id"]][0]; lst = TH_LIST[th["slug"]]; i = lst.index(e); k = THEMES.index(th)
    prev = (f"{lst[i-1]['id']} · {lst[i-1]['title']}", f"{fname(lst[i-1])}.md") if i else (th["title"], f"../themes/{th['slug']}.md")
    if i < len(lst) - 1: nxt = (f"{lst[i+1]['id']} · {lst[i+1]['title']}", f"{fname(lst[i+1])}.md")
    elif k < len(THEMES) - 1: nxt = (f"Next theme: {THEMES[k+1]['title']}", f"../themes/{THEMES[k+1]['slug']}.md")
    else: nxt = ("Roadmap", "../ROADMAP.md")
    return prev, nxt
def nav(e):
    (pt, pl), (nt, nl) = neighbours(e); th = GROUP[e["id"]][0]
    return f"Previous: [{pt}]({pl}) · [{th['title']}](../themes/{th['slug']}.md) · Next: [{nt}]({nl})"
def fm_link(l): return "/" + l.replace("../", "").replace(".md", "") if l.startswith("../") else "/exercises/" + l.replace(".md", "")
tests = []
for e in E:
    paper = e.get("paper", False)
    src = "Custom"
    if e.get("teacher"): src += f" · teacher topic: {e['teacher']}"
    if e.get("euler"): src += f" · prepares [Project Euler #{e['euler']}](https://projecteuler.net/problem={e['euler']})"
    th, gr, pos, of, gpos, gof = where(e); (pt, pl), (nt, nl) = neighbours(e)
    L = ["---", f"prev:\n  text: {json.dumps(pt, ensure_ascii=False)}\n  link: {fm_link(pl)}", f"next:\n  text: {json.dumps(nt, ensure_ascii=False)}\n  link: {fm_link(nl)}", "---", "",
         f"[Home](../../README.md) › [Exercises](README.md) › [{th['title']}](../themes/{th['slug']}.md) › [{gr['title']}]({gref(th, gr)}) › " + e["id"], "", f"# {e['id']} · {e['title']}", "",
         "<ExerciseHeader />", "", '<div class="gh-only">', "",
         f"**{th['title']} › {gr['title']}** · exercise {gpos} of {gof} in this group ({pos} of {of} in the theme)", "",
         "| Level | Effort | Kind | Recipes | Do these first |", "| --- | --- | --- | --- | --- |",
         f"| {e['level']} | {stars(e['stars'])} | {kind(e)} | {rlinks(e)} | {plinks(e)} |", "", "</div>", ""]
    if src != "Custom": L += [f"Source: {src.replace('Custom · ', '')}.", ""]
    L += ["## Goal", "", GOALS.get(e["id"], e["goal"]), ""]
    if paper:
        L += ["## Start and check", "", "This one is on **paper**: no code to write. When you are done, compare with the answer key (link at the bottom).", ""]
    else:
        L += ["## Start and check", "", "```bash", f"./ex start {e['id']}     # creates practice/{cls(e)}.cs (never overwrites your work)", f"./ex check {e['id']}     # tests your code with the examples below", "```", "",
              f"On Windows, type `.\\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).", ""]
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
    if e["id"] in EDGE:
        if e["id"] in M: checked = [f"`{c[0]}({', '.join(cslit(a) for a in c[1])})` {'prints nothing' if c[2] == '' else ('prints ' + ' '.join(chr(96) + l + chr(96) for l in c[2].rstrip(chr(10)).split(chr(10))) if isinstance(c[2], str) and chr(10) in c[2] else 'gives ' + shown(c[2]))}" for c in EDGE[e["id"]]]
        else: checked = ["input " + (", ".join(f"`{x}`" if x else "*(empty)*" for x in c[0])) + " prints " + ", ".join(f"`{x}`" for x in c[1]) for c in EDGE[e["id"]]]
        L += ["`./ex check` tests these too: " + "; ".join(checked) + ".", ""]
    L += ["## Rules", ""] + [f"- {x}" for x in RULES.get(e["id"], e["constraints"])] + ["- No LINQ and no ready-made helpers: you write every step yourself.", ""]
    L += ["## Before coding", "", ("Fill the [reading worksheet](../docs/reading-an-exercise.md#the-template): what goes in? what comes out? a tiny example by hand?" if not e["recipes"] else "Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?"), ""]
    L += ["## Hints (open one at a time)", ""]
    for i, h in enumerate(HINTS.get(e["id"], e["hints"]), 1):
        L += [f"<details><summary>Hint {i}</summary>", "", h, "", "</details>", ""]
    L += ["## Mastery check", "", "Solve this variation **alone**, on another day:", "", e["mastery"], ""]
    sol = f"../answer-keys/{fname(e)}.md" if paper else f"../../internal/solutions/{cls(e)}.cs"
    L += ["## Solution", "", f"Only after a real try: [open the solution for {e['id']}]({sol}). Your solution can be different and still correct!", "",
          "---", "", '<div class="gh-only">', "", nav(e), "", "</div>", ""]
    open(f"{ROOT}/course/exercises/{fname(e)}.md","w").write("\n".join(L))
    if paper:
        open(f"{ROOT}/course/answer-keys/{fname(e)}.md","w").write(f"[Home](../../README.md) › [Solutions](README.md) › {e['id']}\n\n# Answer key · {e['id']} {e['title']}\n\n{e['answer']}\n\n[Back to the exercise](../exercises/{fname(e)}.md)\n")
    else:
        open(f"{ROOT}/internal/solutions/{cls(e)}.cs", "w").write(cs_file(e, starter=False))
        open(f"{ROOT}/internal/tools/starters/{cls(e)}.cs", "w").write(cs_file(e, starter=True))
        if e["id"] not in M: tests += e["examples"]
# single source for the checker (internal/tools/checker) and CI
def jcase(name, args, exp): return {"method": name, "args": args, "expected": exp}
cj = [{"id": e["id"], "name": fname(e), "class": cls(e), "title": e["title"], "paper": bool(e.get("paper")),
       "kind": "paper" if e.get("paper") else ("method" if e["id"] in M else "output"),
       "methods": [parse_sig(sig)[1] for sig, _, _ in M[e["id"]]["methods"]] if e["id"] in M else [],
       "cases": [jcase(*c) for c in M[e["id"]]["cases"]] if e["id"] in M else [],
       "edge_tests": len(EDGE.get(e["id"], [])),
       "checkHint": e.get("check_hint", ""),
       "theme": BYSLUG[e["theme"]]["title"], "themeOrder": [x["slug"] for x in THEMES].index(e["theme"]) + 1, "group": GROUP[e["id"]][1]["title"], "drills": [n for n, _, ids in DRILLS if e["id"] in ids],
       "examples": [{"input": inp, "expected": [o for o in out if o.strip()]} for inp, out in (e["examples"] or [])]}
      for e in ORDER]
json.dump(cj, open(f"{ROOT}/internal/tools/exercises.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
# data for the website (internal/site/.vitepress): sidebar, "Mark as done", progress page
os.makedirs(f"{ROOT}/internal/site/.vitepress", exist_ok=True)
def site_ex(e):
    th, gr, pos, of, gpos, gof = where(e)
    return {"id": e["id"], "title": e["title"], "link": f"/exercises/{fname(e)}", "theme": e["theme"], "group": e["group"],
            "level": e["level"], "effort": stars(e["stars"]), "kind": kind(e), "paper": bool(e.get("paper")), "pos": gpos, "of": gof,
            "recipes": [{"title": RECIPES[r][0], "link": f"/cookbook/{RECIPES[r][1]}"} for r in e["recipes"]],
            "pre": [{"id": p, "link": f"/exercises/{fname(byid[p])}"} for p in e["pre"]],
            "drills": [n for n, _, ids in DRILLS if e["id"] in ids]}
site = {"exercises": [site_ex(e) for e in ORDER],
        "drillSets": [{"name": n, "recipe": r, "ids": ids} for n, r, ids in DRILLS],
        "themes": [{"slug": x["slug"], "title": x["title"], "part": x["part"], "summary": x["summary"], "link": f"/themes/{x['slug']}",
                    "groups": [{"slug": g_["slug"], "title": g_["title"], "link": f"/themes/{x['slug']}-{g_['slug']}"} for g_ in x["groups"]]} for x in THEMES]}
json.dump(site, open(f"{ROOT}/internal/site/.vitepress/course.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

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
         f"// Your code:     practice/{c}.cs", f"// Run them:      ./ex check {e['id']}", "//", "// Generated from internal/tools/generator (edit the exercise there, not here).",
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
        for j, (name, args, exp, why) in enumerate(EDGE.get(e["id"], []), 1):
            ret, _, ps = sigs[name]
            call = f"{c}.{name}({', '.join(lit(a, p[0]) for a, p in zip(args, ps))})"
            shown_call = f"{name}({', '.join(show(a, p[0]) for a, p in zip(args, ps))})"
            if ret == "void":
                lines_ = exp.rstrip("\n").split("\n") if exp else []
                what = "prints nothing" if not lines_ else (f'prints "{lines_[0]}"' if len(lines_) == 1 else f"prints {len(lines_)} lines")
                out += [f'        [Fact(DisplayName = "{e["id"]} example {len(M[e["id"]]["cases"]) + j}: edge case, {attr(shown_call)} {attr(what)}")]', f"        public void Edge{j}() => Expect.Prints("]
                if len(lines_) <= 1: out[-1] += f'{cs_str((lines_[0] + chr(10)) if lines_ else "")}, () => {call}, hint: {cs_str(why)});'
                else: out += ['            """'] + ["            " + l.rstrip() for l in lines_] + [f'            """, () => {call}, hint: {cs_str(why)});']
            else:
                out += [f'        [Fact(DisplayName = "{e["id"]} example {len(M[e["id"]]["cases"]) + j}: edge case, {attr(shown_call)} returns {attr(show(exp, ret))}")]',
                        f"        public void Edge{j}() => Expect.Returns({lit(exp, ret)}, () => {call}, hint: {cs_str(why)});"]
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
        for j, (inp, want, why) in enumerate(EDGE.get(e["id"], []), 1):
            shown_in = ", ".join(x if x else "(empty)" for x in inp)
            out += [f'        [Fact(DisplayName = "{e["id"]} example {len(e["examples"]) + j}: edge case, input {attr(shown_in)} prints {attr(chr(34) + want[-1] + chr(34))}")]',
                    f"        public void Edge{j}() => Expect.Output(",
                    f"            input: [{', '.join(cs_str(x) for x in inp)}],",
                    f"            lines: [{', '.join(cs_str(x) for x in want)}],",
                    f"            run: () => {c}.Run(), hint: {cs_str(why)});", ""]
    if out[-1] == "": out.pop()
    return "\n".join(out + ["    }", "}", ""])
TD = f"{ROOT}/internal/tests/Practice.Tests/Exercises"
os.makedirs(TD, exist_ok=True)
for old in glob.glob(f"{TD}/*.cs"): os.remove(old)
for e in ORDER:
    if not e.get("paper"): open(f"{TD}/{cls(e)}Tests.cs", "w").write(test_file(e))

exec(open(os.path.join(os.path.dirname(__file__), 'pages.py'), encoding='utf-8').read())
print("generated", len(E), "exercises,", len(tests), "example runs,", sum(len(m["cases"]) for m in M.values()), "method cases,", sum(map(len, EDGE.values())), "edge cases")
