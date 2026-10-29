# AGENTS.md

A C# loop **rescue course** for one true beginner (a university student, Programming Fundamentals, struggling with loops). Every page is read by her, so every change is judged by one question: *does this make the next step easier for a struggling beginner?*

Deeper reference, reached only when the branch fires:

- Writing or reviewing learner text → [docs/writing-guide.md](docs/writing-guide.md) (teaching, plain-language and accessibility rules, with sources).
- Adding or changing an exercise → skill [.agents/skills/add-exercise](.agents/skills/add-exercise/SKILL.md).
- Reviewing the repo → skill [.agents/skills/review-content](.agents/skills/review-content/SKILL.md).

## Map

- `ROADMAP.md`: two tracks aligned to university weeks (W1 Hello World, W2 variables, W3 conditions, W4 loops, W5 files, W6 arrays, 2–6 Nov no class, W7 exceptions, W8 recap, W9 collections, W10 methods, W11–12 objects). It also holds the dated "you are here" callout and the catch-up plan: update both when the date moves on.
- `cookbook/`: 12 loop **recipes** + decision diagram + `combining-recipes.md`.
- `exercises/`, `solutions/`, `docs/progress-checklist.md`: **generated**. Never hand-edit them.
- `tools/generator/`: the single source of truth for every exercise (`data1.py` → `data4.py`, chained imports; `gen.py` renders).
- `docs/`: learner guides (getting started, reading an exercise, problem solving, practice, glossary) + the writing guide.
- `practice/`: the one console project she codes in. `Program.cs` stays a neutral placeholder, never a solution.

## Pedagogy (the rubric)

- **One new difficulty** per exercise: everything else in it is covered by its `pre` exercises. Levels fade the help: 🟢 Guided → 🔵 Independent → 🟣 Challenge.
- **Order holds**: each `pre` sits at the same roadmap step or earlier, and every plan (roadmap sessions, README start, recap) lists an exercise only after its `pre`.
- **Hand-written loops**: no LINQ, no `Math.Pow`, no `Array.Reverse`/`string.Join`/`.Contains` shortcuts. Solutions use only what the exercise's roadmap step has taught.
- **Hints** in `<details>`, smallest nudge first; Guided exercises carry at least 2. Every exercise has a **mastery check** (a new variation, alone, another day).
- **Solutions separate**: exercise pages link to `solutions/` only at the bottom.
- **The book** (*The C# Player's Guide*, 5th ed.) is a **parallel reading track**: name the level to read beside a roadmap step. Its challenges stay out of exercise lists, recipe mini-exercises and plans.
- **One home per meaning**: the session shape and coach questions live in `docs/how-to-practice.md`, check commands in this file; other pages link there.
- **Plain English**: short sentences, "you", common words, concrete numbers; new words go to `docs/glossary.md`. Swap academic words for plain ones: *turn* (iteration), *start value* (initialization), *small job* (responsibility), *a sentence that stays true* (invariant). She knows basic Git (clone, pull, commit, push): use it without explaining it, and keep CI, generator and agent detail here and in `CONTRIBUTING.md`.
- **Accessible**: alt text on images, `accTitle` + `accDescr` on every Mermaid diagram, meaning never in colour or emoji alone, descriptive link text, headings in order.
- **Navigation**: every page opens with a breadcrumb (`🏠 Home › …`) and ends with Previous/Next or Back links.

## Formats

**Exercise** (rendered by `gen.py`): breadcrumb, `# ID · Title`, a header table (Level, Difficulty, Roadmap step, Recipes, Do these first, Source), then 🎯 Goal, 🧪 Examples, ⚠️ Edge cases, 📏 Rules, 🗺️ Before coding, 💡 Hints, ✅ Mastery check, 🔑 Solution, Previous/Next.

**IDs**: one family letter + two digits, ordered by difficulty. B basics, C conditions, L loop mechanics, A accumulators, G 2D drawings, D digits, S state, P search & primes, M combine, R arrays, T text, F files, E exceptions, K collections, N methods. Family order and the step it maps to live in `FAM` in `gen.py`. `paper=True` makes a paper exercise with an answer key in `solutions/ID.md`.

**Examples are tests**: each `(inputs, outputs)` pair becomes a case in `solutions/tests.json`. Output lines match as *line endings*, because prompts printed with `Console.Write` share the line; keep printed results on their own `WriteLine`.

**Recipe** (`cookbook/NN-name.md`): breadcrumb, `# Recipe N · Name — tagline`, one-line quote, then 🔎 Recognize it, 🧠 The idea (diagram), 📝 Template, 🔬 Trace table, ⚠️ Common mistakes, 🏋️ Mini exercises (linked IDs), ➡️ Next.

**Mermaid**: `flowchart TD` for decisions, `LR` for sequences; labels in `"quotes"` with `<br/>`; write `#lt;` / `#gt;` for `<` / `>`; first two lines `accTitle:` and `accDescr:` (a full text version of the diagram).

## Checks

`tools/verify.sh` runs every check, the same set the CI workflow runs; green before every merge.

| Check | Local | Gotcha |
| --- | --- | --- |
| Generator in sync | `python3 tools/generator/gen.py` then `git diff` | Edit data, regenerate, commit both. |
| Solutions | `python3 tools/check-solutions.py [ID…]` | Needs .NET 10 (file-based `dotnet build x.cs`); each run gets a temp working dir, so F01's `numbers.txt` stays out of the repo. |
| Practice | `dotnet build practice` | Targets net8.0 with `RollForward=Major`. |
| Mermaid | `tools/check-mermaid.sh` | Renders through mermaid-cli + Chrome (`--no-sandbox`). |
| Markdown lint | `npx markdownlint-cli2` | Config `.markdownlint-cli2.jsonc`; a heading ending in `C#` trips MD020, so reword it. |
| Links | `python3 tools/check-links.py [--external]`, `lychee --config lychee.toml .` | doi.org and publishers answer 403 to bots: accepted. |
| Spelling | `npx cspell "**/*.md"` | British and US spellings both allowed; add real words to `cspell.json`. |

## Shipping

Branch, PR, wait for green checks (`gh pr checks --watch`), then merge. `main` is never force-pushed.
