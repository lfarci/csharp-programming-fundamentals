---
name: review-content
description: Review the whole course repo for a struggling beginner and fix what you find. Use when asked to review, audit, polish or improve the content.
---

A **pass** reads every learner page against the rubric in `AGENTS.md` and `docs/writing-guide.md`. Repeat passes until one finds nothing meaningful.

1. **Run the checks first:** `tools/verify.sh --external` (it includes `tools/check-structure.py`). Every red line is an issue.
   Then open the site at 1440 px as the learner: roadmap, exercises overview, a theme page, an exercise page, the sidebar. Compare the components with each other.
2. **Read every page as the persona** in `docs/learner-persona.md`, in learner order: README → getting started → roadmap → cookbook → exercises (via generator data) → docs → solutions. For each page, hunt these issue kinds and log each with file and line:
   - *jump*: an exercise adds two new difficulties, or a plan lists an exercise before its `pre`;
   - *mismatch*: an example, trace table or comment that disagrees with the code;
   - *shortcut*: LINQ or a helper doing the loop; a challenge copied from a book or course listed as an exercise;
   - *scaffold gap*: Guided with fewer than 2 hints, missing edge case or mastery check;
   - *format drift*: a page that leaves the exercise or recipe format in `AGENTS.md` (recipes: all 6 lesson steps, in order, predict and trace on the same code);
   - *persona*: a page that assumes more than [the persona](../../../docs/learner-persona.md) knows in that theme, or a theme without objectives;
   - *vocabulary and weeks*: the word "step" for a theme, week numbers, dates or catch-up plans; a new term missing from the glossary; a page covering two topics;
   - *visual identity*: a component or page that leaves the Roadmap look (`cpf-*` classes in `custom.css`) or adds a second accent colour; a list of pages or exercises shown as a plain table on the site where a comparable list uses cards (roadmap, overview, group cards, drill sets, cookbook and study-skills indexes, exercise header);
   - *Learn section*: a theme missing from `tools/generator/learn.py`, an outside link that no longer returns 200, text copied from Microsoft Learn, or any reference to the content of *The C# Player's Guide* (copyrighted: no chapters, levels or challenges);
   - *order*: the theme table, Previous/Next and the drill-set row disagree, or a Guided drill comes after a Challenge in the same group;
   - *balance*: a theme with 1 or 2 exercises next to one with 15+, a group above 14; merge or split groups in `themes.py`;
   - *where am I*: an exercise page that does not show its theme, group and *Exercise N of M*, or a sidebar that lists exercises;
   - *long title*: a title over 24 characters, or one that repeats the kind ("(paper)", "Fix the bugs:");
   - *noisy theory box*: a theme page offering more than one video and one module up front (the rest belongs under *More*);
   - *near-duplicate*: an exercise or mastery check that repeats its neighbour without a new variation;
   - *thin drill*: a recipe whose `DRILLS` row has fewer than 5 exercises, or a drill that changes more than one thing from its neighbour;
   - *no retrieval*: a new recipe without predict, complete-it or debugging practice;
   - *plain-language*: long sentences, jargon not in the glossary, Git words on learner pages;
   - *emoji*: any emoji or symbol standing for a word (pages, test names, `./ex` output); write the word;
   - *access*: missing alt text, `accTitle`/`accDescr`, colour-only meaning, "click here" links, skipped heading levels;
   - *navigation*: missing breadcrumb or Previous/Next, dead ends, a stale "you are here";
   - *duplicate*: one meaning written in two places that can drift apart.
   Done when every page is read and the log names a kind for each issue.
3. **Fix** each logged issue at its source (generator data for exercises).
4. **Re-verify** with `tools/verify.sh --external`. Done when it ends with `ALL CHECKS PASSED`.
5. **Sharpen the rules.** A new kind of issue, or one that keeps coming back, becomes a line in `AGENTS.md` or the writing guide.
6. **Report** the pass: issue count per kind and the main fixes.
