# AGENTS.md

A C# loop **rescue course** for one true beginner (a university student, Programming Fundamentals, struggling with loops). Every page is read by her, so every change is judged by one question: *does this make the next step easier for a struggling beginner?*

Deeper reference, reached only when the branch fires:

- Who the learner is → [docs/learner-persona.md](docs/learner-persona.md). Read it before writing any learner page.
- Writing or reviewing learner text → [docs/writing-guide.md](docs/writing-guide.md) (teaching rules, the 6-step lesson format, exercise types, plain-language and accessibility rules, with sources).
- Adding or changing an exercise → skill [.agents/skills/add-exercise](.agents/skills/add-exercise/SKILL.md).
- Reviewing the repo → skill [.agents/skills/review-content](.agents/skills/review-content/SKILL.md).

## Map

- `ROADMAP.md`: two tracks aligned to university weeks (W1 Hello World, W2 variables, W3 conditions, W4 loops, W5 files, W6 arrays, 2–6 Nov no class, W7 exceptions, W8 recap, W9 collections, W10 methods, W11–12 objects). It also holds the dated "you are here" callout and the catch-up plan: update both when the date moves on.
- `cookbook/`: 12 loop **recipes** + decision diagram + `combining-recipes.md`.
- `exercises/`, `solutions/*.cs`, `tools/starters/`, `tools/exercises.json`, `tests/Practice.Tests/Generated.cs`, `docs/progress-checklist.md`: **generated**. Never hand-edit them.
- `tools/generator/`: the single source of truth for every exercise (`data1.py` → `data4.py` statements, chained imports; `data5.py` the method each exercise asks for; `data6.py` ladder, 🧩 Parsons and 🐞 debugging exercises; `data7.py` the drill bank and `DRILLS` (drill-set table in `exercises/README.md`); `gen.py` renders).
- `docs/`: learner guides (getting started, reading an exercise, problem solving, practice, glossary) + the writing guide.
- `practice/`: **her** project. `./ex start` copies a starter here and never overwrites; nothing else writes here. `Program.cs` and `Practice.csproj` are plumbing she never edits (they run the current exercise via `tools/ex/Runner.cs`).
- `./ex` (`ex`, `ex.cmd` → `tools/ex`): start, check, run, next, list. `tests/Practice.Tests`: xUnit v3 tests behind `./ex check`, also visible in Test Explorer (`CSharpFundamentals.sln`).

## Pedagogy (the rubric)

- **One new difficulty** per exercise: everything else in it is covered by its `pre` exercises. Levels fade the help: 🟢 Guided → 🔵 Independent → 🟣 Challenge.
- **Read before write**: every new recipe gets predict → trace → complete (or 🧩 arrange) before a blank file, and a 🐞 debugging task that plants one of its common mistakes.
- **Drills over challenges**: to add practice, add a same-pattern **drill** (`drill()` in `tools/generator/data7.py`) that changes only the target, never a clever combined challenge. Add its ID to the right `DRILLS` row, in difficulty order. A recipe needs 5–12 drills.
- **Simple ideas**: goal in 1–2 short sentences; she will come back to it often. The examples table comes from `cases`, so it always matches the method. One new difficulty only.
- **Her files**: learners write only in `practice/` (`practice/*_*.cs` is gitignored). Never ship a file matching that pattern.
- **Objectives first**: every ROADMAP step starts with a 🎯 objectives line using checkable verbs (trace, write, find the bug); its exercises must train exactly those.
- **Order holds**: each `pre` sits at the same roadmap step or earlier (one known exception: F01 waits for R01, because `File.ReadAllLines` returns an array), and every plan (roadmap sessions, README start, recap) lists an exercise only after its `pre`.
- **Hand-written loops**: no LINQ, no `Math.Pow`, no `Array.Reverse`/`string.Join`/`.Contains` shortcuts. Solutions use only what the exercise's roadmap step has taught (files at step 5 build text with `+=`; `List<T>` waits for step 9).
- **Hints** in `<details>`, smallest nudge first; Guided exercises carry at least 2. Every exercise has a **mastery check**: a *new variation* solved alone another day ("do it again" is not a variation).
- **Solutions separate**: exercise pages link to `solutions/` only at the bottom.
- **The book** (*The C# Player's Guide*, 5th ed.) is a **parallel reading track**: name the level to read beside a roadmap step. Its challenges stay out of exercise lists, recipe mini-exercises and plans.
- **One home per meaning**: the session shape and coach questions live in `docs/how-to-practice.md`, check commands in this file; other pages link there.
- **Plain English**: short sentences, "you", common words, concrete numbers; new words go to `docs/glossary.md`. Swap academic words for plain ones: *turn* (iteration), *start value* (initialization), *small job* (responsibility), *a sentence that stays true* (invariant). She knows basic Git (clone, pull, commit, push): use it without explaining it, and keep CI, generator and agent detail here and in `CONTRIBUTING.md`.
- **Accessible**: alt text on images, `accTitle` + `accDescr` on every Mermaid diagram, meaning never in colour or emoji alone, descriptive link text, headings in order.
- **Navigation**: every page opens with a breadcrumb (`🏠 Home › …`) and ends with Previous/Next or Back links.

## Formats

**Exercise** (rendered by `gen.py`): breadcrumb, `# ID · Title`, a header table (Level, Difficulty, Roadmap step, Recipes, Do these first, Source), then 🎯 Goal, 🧪 Examples, ⚠️ Edge cases, 📏 Rules, 🗺️ Before coding, 💡 Hints, ✅ Mastery check, 🔑 Solution, Previous/Next.

**IDs**: one family letter + two digits, ordered by difficulty. B basics, C conditions, L loop mechanics, A accumulators, G 2D drawings, D digits, S state, P search & primes, M combine, R arrays, T text, F files, E exceptions, K collections, N methods. Family order and the step it maps to live in `FAM` in `gen.py`. `paper=True` makes a paper exercise with an answer key in `solutions/ID.md`. `task="parsons"` (starter = the solution lines, shuffled and commented) and `task="debug"` (starter = compiling code with 1–2 planted bugs) use a starter string that begins with `NOTE_P` (`//! `), kept as is. `sort="G001"` places a bridge exercise elsewhere in the path than its ID (L09 sits just before G01).

**Exercise shape**: one file, one `public static class ID_PascalName` in namespace `Practice`.

- *Method exercise* (entry in `data5.M`): she fills in the method(s); its parameters are the input, `return` the result. The page shows `GOALS` and a call → result table; the tests call the method by reflection with `cases`. Drawings are `void` methods whose printed text is compared. Add a case the `TODO` starter fails (CI checks this).
- *Program exercise* (no entry): input loops, menus, files. She writes `public static void Run()`; the tests feed the example input and match printed lines as *line endings* (prompts from `Console.Write` share the line), so results go on their own `WriteLine`.
- Methods are allowed from week 1, framed as "input = parameters, result = return"; unit-test vocabulary stays behind `./ex check` until week 10.

**Recipe** (`cookbook/NN-name.md`): breadcrumb, `# Recipe N · Name — tagline`, one-line quote, a 🧭 "how this page works" line, then the 6 lesson steps of `docs/writing-guide.md#2-lesson-format`: 🎯 1 · Goal (one sentence), 🔮 2 · Predict (working example, answer in `<details>`), 🔬 3 · Trace it (table of the *same* example), 🧩 4 · The pattern (numbered **subgoal labels**, then 🔎 Recognize it, 🧠 The idea with diagram, 📝 Template as `###`), ✍️ 5 · Complete it (blanks `____` or lines to arrange, answer in `<details>`), 🏋️ 6 · Your turn (linked IDs, then ### 🐞 Debug it with one bug and the answer in `<details>`, then ### ⚠️ Common mistakes), ➡️ Next.

**Mermaid**: `flowchart TD` for decisions, `LR` for sequences; labels in `"quotes"` with `<br/>`; write `#lt;` / `#gt;` for `<` / `>`; first two lines `accTitle:` and `accDescr:` (a full text version of the diagram).

## Checks

`tools/verify.sh` runs the same checks as CI (`.github/workflows/checks.yml`, one job per row below); all green before every merge.

| Check | Local | Gotcha |
| --- | --- | --- |
| Generator in sync | `python3 tools/generator/gen.py` then `git diff` | Edit data, regenerate, commit both. |
| Exercises | `tools/check-exercises.sh` | One exercise builds alone with `-p:OnlyExercise=<Class>` (what `./ex check` uses). Reference solutions pass every test (via `EXERCISE_ASSEMBLY`), every starter compiles and fails at least one example, `./ex` runs. Projects target net8.0 with `RollForward=Major`; `global.json` opts `dotnet test` into Microsoft.Testing.Platform (needed on .NET 10 SDK); `./ex` runs the test exe directly, so it works on any SDK. |
| Mermaid | `tools/check-mermaid.sh` | Renders through mermaid-cli + Chrome (`--no-sandbox`). |
| Markdown lint | `npx markdownlint-cli2` | Config `.markdownlint-cli2.jsonc`; a heading ending in `C#` trips MD020, so reword it. |
| Links | `python3 tools/check-links.py [--external]`, `lychee --config lychee.toml .` | doi.org and publishers answer 403 to bots: accepted. |
| Spelling | `npx cspell "**/*.md"` | British and US spellings both allowed; add real words to `cspell.json`. |

## Shipping

Branch, PR, wait for green checks (`gh pr checks --watch`), then merge. `main` is never force-pushed.
