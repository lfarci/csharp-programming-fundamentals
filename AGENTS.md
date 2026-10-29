# AGENTS.md

A C# loop **rescue course** for one true beginner (a university student, Programming Fundamentals, struggling with loops). Every page is read by her, so every change is judged by one question: *does this make the next step easier for a struggling beginner?*

Deeper reference, reached only when the branch fires:

- Who the learner is → [docs/learner-persona.md](docs/learner-persona.md). Read it before writing any learner page.
- Writing or reviewing learner text → [docs/writing-guide.md](docs/writing-guide.md) (teaching rules, the 6-step lesson format, exercise types, plain-language and accessibility rules, with sources).
- Adding or changing an exercise → skill [.agents/skills/add-exercise](.agents/skills/add-exercise/SKILL.md).
- Reviewing the repo → skill [.agents/skills/review-content](.agents/skills/review-content/SKILL.md).

## Map

- **Themes** are the units of the path (15, in three parts: before loops, loops, after loops). `tools/generator/themes.py` is the only place they are defined (slug, title, summary, objectives, what to learn, book level, ready-when). Always say *theme*, never *step* or *week*. `ROADMAP.md` (a visual path), `themes/<slug>.md` (one page per theme, with a tick table), `exercises/README.md` (overview) and `diagrams/roadmap.d2` are **generated** by `tools/generator/pages.py`.
- `cookbook/`: 12 loop **recipes**, the decision diagram, `combining-recipes.md`, and the theory pages (`which-loop.md`, `the-maths.md`). Theory goes here, never in the roadmap.
- `learn/` (**generated** by `pages.py` from `tools/generator/learn.py`): the **Learn** section. This course is for practice; the theory comes from existing resources: *The C# Player's Guide* (main companion), Microsoft Learn (modules, the *C# for Beginners* videos, the Foundational C# path) and the C# Quest Tracker (<https://lfarci.github.io/csharp-quest-tracker/>) for the book's own challenges. `learn.py` maps every theme to book levels, modules and videos, and also feeds the *Learn the theory* box on each theme page. Rules: only add a resource you opened (check it returns 200), take book level names from the official table of contents (the free sample PDF), link instead of copying, and never reproduce the book's text or challenges.
- **Affiliate link**: `.vitepress/theme/affiliate.ts`, `BOOK_AFFILIATE_URL`. Empty by default, so "Buy the book" goes to the official site. Only the owner fills it in with a real link from an affiliate program (never invent an ID); the disclosure note under the button appears only when it is set.
- `diagrams/`: every diagram, as a D2 source (`x.d2`) and its committed SVG (`x.svg`), all sharing `_style.d2`. Pages embed the SVG as a Markdown image whose alt text is the full text version, so it works on GitHub and the site. Render with `tools/diagrams.sh`; no Mermaid.
- `exercises/`, `solutions/*.cs`, `tools/starters/`, `tools/exercises.json`, `tests/Practice.Tests/Exercises/*Tests.cs`, `docs/progress-checklist.md`: **generated**. Never hand-edit them.
- `tools/generator/`: the single source of truth for every exercise (`data1.py` → `data4.py` statements, chained imports; `data5.py` the method each exercise asks for; `data6.py` ladder, Parsons and debugging exercises; `data7.py` the drill bank and `DRILLS` (drill-set table in `exercises/README.md`); `gen.py` renders, `pages.py` the theme pages).
- `docs/`: learner guides (getting started, reading an exercise, problem solving, practice, glossary) + the writing guide.
- `practice/`: **her** project. `./ex start` copies a starter here and never overwrites; nothing else writes here. `Program.cs` and `Practice.csproj` are plumbing she never edits (they run the current exercise via `tools/ex/Runner.cs`).
- `./ex` (`ex`, `ex.cmd` → `tools/ex`): start, check, run, next, list, progress, done. `./ex check` saves passed exercises in `practice/.done`; `./ex progress` writes `practice/PROGRESS.md` (both gitignored, inspired by [C# Quest Tracker](https://github.com/lfarci/csharp-quest-tracker)).
- `.vitepress/`: the website (VitePress, <https://lfarci.github.io/csharp-programming-fundamentals/>). It is built from the repo Markdown itself (`README.md` → folder index), so never copy a page into it. **The site home is `home.md`** (a VitePress home: what the course is, what is in it, how it works, where to go, the VS Code demo video), **separate from the root `README.md`**, which stays short and useful on GitHub (badges, quick start, link to the site). Repo-only things (Codespaces badge, GIF) stay out of `home.md`. Vue components in `.vitepress/theme/` (`ThemeExercises`, `ExercisesOverview`, `RoadmapPath`, `MarkDone`, `ProgressPage`) show live progress; their GitHub fallback sits in a `<div class="gh-only">`, hidden on the site. `course.json` (sidebar, "Mark as done", progress) is **generated** by `gen.py`. `progress.md` is the one site-only page. Relative links to non-page files (`.cs`, tools, agent notes) become GitHub links at build time. Preview: `npm ci && npm run docs:dev`; build: `npm run docs:build` (fails on dead links). Progress lives in the browser (localStorage key `csharp-programming-fundamentals:progress:v1`); `./ex progress` prints a sync code (`CPF1:A1-4,7;L11`) that the site imports, format in `.vitepress/theme/sync-code.ts` and `SyncCode` in `tools/ex/Program.cs` (keep both in step, `tools/check-site-sync.ts` tests it). `site-tests/progress.spec.ts` (Playwright, `npm run test:site`; `SITE_URL=<live url>` to test the deployed site) ticks Mark as done, reloads, checks the counts and imports a sync code in a real browser.
- `tests/Practice.Tests`: xUnit v3. **One plain test file per exercise** (`Exercises/<Class>Tests.cs`, one `[Fact]` per example with literal inputs and expected values, `DisplayName` in words) plus the small shared helper `Expect.cs` (`Returns`, `Prints`, `Output`: friendly messages, 5 s time limit). A test file is compiled only when `practice/<Class>.cs` exists (MSBuild target `OnlyStartedExercises`), so exercises not started yet never break the build. `-p:ExerciseProject=` points the tests at `solutions/` in CI. Tests are also visible in Test Explorer (`CSharpFundamentals.sln`).

## Pedagogy (the rubric)

- **One new difficulty** per exercise: everything else in it is covered by its `pre` exercises. Levels fade the help: Guided → Independent → Challenge.
- **Read before write**: every new recipe gets predict → trace → complete (or arrange) before a blank file, and a debugging task that plants one of its common mistakes.
- **Drills over challenges**: to add practice, add a same-pattern **drill** (`drill()` in `tools/generator/data7.py`) that changes only the target, never a clever combined challenge. Add its ID to the right `DRILLS` row, in difficulty order. A recipe needs 5–12 drills.
- **Simple ideas**: goal in 1–2 short sentences; she will come back to it often. The examples table comes from `cases`, so it always matches the method. One new difficulty only.
- **Her files**: learners write only in `practice/` (`practice/*_*.cs` is gitignored). Never ship a file matching that pattern.
- **Objectives first**: every theme (in `themes.py`) starts with objectives using checkable verbs (trace, write, find the bug); its exercises must train exactly those.
- **No weeks**: no week numbers, dates, "you are here" or catch-up plans anywhere. The path is an order of themes, not a calendar.
- **Order holds**: each `pre` sits in the same theme or an earlier one (one known exception: F01 waits for R01, because `File.ReadAllLines` returns an array), and every list (theme pages, README start, recap) lists an exercise only after its `pre`.
- **Hand-written loops**: no LINQ, no `Math.Pow`, no `Array.Reverse`/`string.Join`/`.Contains` shortcuts. Solutions use only what the exercise's theme and earlier themes have taught (the Files theme builds text with `+=`; `List<T>` waits for the Collections theme).
- **Hints** in `<details>`, smallest nudge first; Guided exercises carry at least 2. Every exercise has a **mastery check**: a *new variation* solved alone another day ("do it again" is not a variation).
- **Solutions separate**: exercise pages link to `solutions/` only at the bottom.
- **The book** (*The C# Player's Guide*, 5th ed.) is a **parallel reading track**: name the level to read beside a theme (`book` in `themes.py`). Its challenges stay out of exercise lists, recipe mini-exercises and plans.
- **One home per meaning**: the session shape and coach questions live in `docs/how-to-practice.md`, check commands in this file; other pages link there.
- **Plain English**: short sentences, "you", common words, concrete numbers; **every new word goes to `docs/glossary.md`** (one row, alphabetical, plain definition, link to where it is taught); review the glossary whenever a page adds a term. Swap academic words for plain ones: *turn* (iteration), *start value* (initialization), *small job* (responsibility), *a sentence that stays true* (invariant). She knows basic Git (clone, pull, commit, push): use it without explaining it, and keep CI, generator and agent detail here and in `CONTRIBUTING.md`.
- **Visual identity (the Roadmap is the reference)**: numbered circle, white card with a thin border and 12px radius, thin progress bar, one blue accent (`#3451b2`), no shadows except on hover. The shared classes live in `.vitepress/theme/custom.css` (`cpf-card`, `cpf-link`, `cpf-num`, `cpf-bar`, `cpf-kicker`, `cpf-button`); use them in every new component (overview, theme table, progress, Learn cards, home) instead of new styles. Logo and favicon: `public/logo.svg` (a loop arrow), with `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-192/512.png` rendered from it.
- **Progress lives under Exercises**: the Exercises overview opens with the progress card; `/progress` (sync code import, backup) is linked from there and from the Exercises sidebar group, not from Start here.
- **One topic per page, short and visual**: a page answers one question. Lead with a picture, a table or a worked example, then a few short sentences. If a page grows a second topic, split it and link.
- **No emoji**: none in pages, headings, diagram labels, code, test names or `./ex` output. Status is a word: OK, NOT YET, DONE, FAIL. The verify step `No emoji` enforces it.
- **Accessible**: alt text on images, a full text version as the alt text of every diagram (and the same facts in the text nearby), meaning never in colour alone, descriptive link text, headings in order.
- **Navigation**: every page opens with a breadcrumb (`Home › …`) and ends with Previous/Next or Back links.

## Formats

**Exercise** (rendered by `gen.py`): breadcrumb, `# ID · Title`, a header table (Level, Difficulty, Theme, Recipes, Do these first, Source), then Goal, Examples, Edge cases, Rules, Before coding, Hints, Mastery check, Solution, Previous/Next.

**IDs**: one family letter + two digits, ordered by difficulty. B basics, C conditions, L loop mechanics, A accumulators, G 2D drawings, D digits, S state, P search & primes, M combine, R arrays, T text, F files, E exceptions, K collections, N methods. Each `ex(...)` names its `theme=` (a slug from `themes.py`); IDs and file names never change, so sync codes and tests stay valid. `paper=True` makes a paper exercise with an answer key in `solutions/ID.md`. `task="parsons"` (starter = the solution lines, shuffled and commented) and `task="debug"` (starter = compiling code with 1–2 planted bugs) use a starter string that begins with `NOTE_P` (`//! `), kept as is. Give each of them a `check_hint` (in `CHECK`, `tools/generator/data7.py`): `./ex check` shows it instead of the generic hints. `sort="G001"` places a bridge exercise elsewhere in the path than its ID (L09 sits just before G01).

**Exercise shape**: one file, one `public static class ID_PascalName` in namespace `Practice`.

- *Method exercise* (entry in `data5.M`): she fills in the method(s); its parameters are the input, `return` the result. The page shows `GOALS` and a call → result table; the tests call the method by reflection with `cases`. Drawings are `void` methods whose printed text is compared. Add a case the `TODO` starter fails (CI checks this).
- *Program exercise* (no entry): input loops, menus, files. She writes `public static void Run()`; the tests feed the example input and match printed lines as *line endings* (prompts from `Console.Write` share the line), so results go on their own `WriteLine`.
- Methods are allowed from the first theme, framed as "input = parameters, result = return"; unit-test vocabulary stays behind `./ex check` until the Methods theme.

**Recipe** (`cookbook/NN-name.md`): breadcrumb, `# Recipe N · Name — tagline`, one-line quote, a "how this page works" line, then the 6 lesson steps of `docs/writing-guide.md#2-lesson-format`: 1 · Goal (one sentence), 2 · Predict (working example, answer in `<details>`), 3 · Trace it (table of the *same* example), 4 · The pattern (numbered **subgoal labels**, then Recognize it, The idea with diagram, Template as `###`), 5 · Complete it (blanks `____` or lines to arrange, answer in `<details>`), 6 · Your turn (linked IDs, then ### Debug it with one bug and the answer in `<details>`, then ### Common mistakes), Next.

**Diagram** (`diagrams/x.d2`): import the shared style (`...@_style`), use its classes (`step`, `ask` for questions, `end`, `note`, `part`), `direction: down` for decisions and `right` for sequences, short labels. Do not name a node `steps` (a D2 keyword). Run `tools/diagrams.sh`, commit the `.d2` and the `.svg`, embed the SVG with a full text alt.

## Checks

`tools/verify.sh` runs the same checks as CI (`.github/workflows/checks.yml`, one job per row below); all green before every merge.

| Check | Local | Gotcha |
| --- | --- | --- |
| Generator in sync | `python3 tools/generator/gen.py` then `git diff` | Edit data, regenerate, commit both. |
| Exercises | `tools/check-exercises.sh` | One exercise builds alone with `-p:OnlyExercise=<Class>` (what `./ex check` uses). Every exercise has a test file; reference solutions pass every test (via `-p:ExerciseProject=solutions/Solutions.csproj`), every starter compiles and fails at least one example, `./ex` runs. Projects target net8.0 with `RollForward=Major`; `global.json` opts `dotnet test` into Microsoft.Testing.Platform (needed on .NET 10 SDK); `./ex` runs the test exe directly, so it works on any SDK. |
| ./ex end to end | `tools/check-ex.sh` (called by check-exercises) | Fresh copy of the repo: start, NOT YET, DONE, a broken other file does not block, progress, done, next. |
| Website | `npm ci && npm run docs:build && node tools/check-site-sync.ts` | Workflow `site.yml` builds on PRs, deploys to GitHub Pages on main. Dead links fail the build. Then `npm run test:site` (Playwright, Chromium) tests the ticks. |
| No emoji | `python3 tools/check-no-emoji.py` | Every tracked text file. Use words. |
| Diagrams | `tools/diagrams.sh --check` | Needs D2 v0.9.0 (the release tarball, as in `checks.yml`). Fails if an SVG is missing or differs from its source. |
| Markdown lint | `npx markdownlint-cli2` | Config `.markdownlint-cli2.jsonc`; a heading ending in `C#` trips MD020, so reword it. |
| Links | `python3 tools/check-links.py [--external]`, `lychee --config lychee.toml .` | doi.org and publishers answer 403 to bots: accepted. |
| Spelling | `npx cspell "**/*.md"` | British and US spellings both allowed; add real words to `cspell.json`. |

## Shipping

Branch, PR, wait for green checks (`gh pr checks --watch`), then merge. `main` is never force-pushed.
