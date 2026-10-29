---
name: add-exercise
description: Add, change or renumber an exercise in this repo (exercise page, solution, example tests, inventory). Use whenever exercises/, solutions/ or tools/generator data change.
---

Every exercise lives in one `ex(...)` call in `tools/generator/data*.py`. The pages are output.

1. **Place it.** Pick the family letter and the roadmap step (see `FAM` in `gen.py`). Name the **one new difficulty** it adds. Choose `pre` so that everything else is already practised, at the same step or earlier. Done when you can say the new difficulty in one sentence and every `pre` exists.
2. **Number it.** Take the next free number in the family; renumbering an existing ID means updating every mention (`rg "\bX07\b"`) in ROADMAP, cookbook mini exercises, docs and other `pre` lists.
3. **Write the `ex(...)` call** in the data file of its family, after its `pre`: `id, slug, title, level, stars, step, recipes, pre, goal, examples, edge, constraints, hints, mastery, code` (`paper=True` + `answer` for a paper exercise; optional `note`, `teacher`, `euler`). Follow the plain-language rules in `docs/writing-guide.md`: goal in one or two short sentences, hints from smallest nudge to near-solution, at least 2 for Guided, a mastery check that is a *new variation*.
4. **Make examples real tests.** 2–4 examples, including one edge case (0, 1, empty). Print results with `Console.WriteLine` on their own line so they match as line endings.
5. **Write the solution** in `code`: beginner style, only what its step teaches, a hand-written loop.
6. **Regenerate and check.** `python3 tools/generator/gen.py && python3 tools/check-solutions.py <ID>`, then `tools/verify.sh`. Done when every check is green.
7. **Link it in.** Add the ID to its ROADMAP step's **Exercises** line and, when it trains a recipe, to that recipe's 🏋️ Mini exercises.
