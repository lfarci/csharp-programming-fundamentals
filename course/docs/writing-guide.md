[Home](../../README.md) › Writing guide (for coaches and agents)

# Writing guide

How we write for a **struggling beginner**. Every rule below comes from a source listed at the end; numbers in brackets, like (2), point to that list. [AGENTS.md](../../AGENTS.md) turns these rules into the review rubric.

## 1. Teaching rules (how people learn to program)

| Rule | Why | Source |
| --- | --- | --- |
| **One new difficulty per exercise.** Everything else in it is already known. | Working memory is small. Two new ideas at once overload it. | Cognitive load theory (1, 2) |
| **Worked example first, then fade the help.** Recipe page (full example) → Guided (hints do most of the steps) → Independent → Challenge. | Beginners learn more from studied examples than from solving alone; help is removed step by step. | Worked examples, fading (3, 2) |
| **Read code before writing code.** Predict, trace, then modify, then make. Paper exercises (L01, L02, S01) come first. | Reading and tracing are separate skills that come before writing. | PRIMM (4), theory of instruction (5) |
| **Name the plan.** Recipes have a name, trigger words and a template. | Novices lack "plans"; naming them makes them reusable. | Theory of instruction (5) |
| **Arrange-the-lines tasks are welcome** for a new recipe (give the lines, mixed up). | Lower load than a blank page, same thinking. | Parsons problems (6) |
| **Hints one at a time, solutions far away.** | Minimal guidance does not work for novices, but too much help removes the thinking. | (2) |
| **Mastery = a new variation, alone, another day.** | Spaced, independent retrieval shows real learning. | (5) |
| **Write for one person.** Check every page against the [learner persona](learner-persona.md). | A concrete learner keeps lessons at the right level and pace. | Learner personas (15, 21) |
| **Start each theme with objectives** that use verbs you can check ("trace", "write", "find the bug"), not "understand". | Objectives decide the exercises, and the exercises check the objectives. | SMART objectives, backward design (15, 20) |
| **Ask for a prediction before running code**, and write it down. | Watching a demo without predicting does not help learning. | (23 tip 4), PRIMM (17) |
| **Label the subgoals** of a pattern with short reusable names. | Labels show novices what two problems have in common. | (19, 23 tip 6) |
| **Give at least two examples per pattern**, in different contexts. | Learners then see the structure, not the surface. | Worked examples (18) |
| **Practise debugging on purpose** with small, planted bugs and real failing checks. | Novices spend most of their time fixing mistakes, and textbooks leave this out. | (23 tips 3, 9), RPF principles (16) |
| **Check understanding often**, with small tasks that each target a known misconception. | Formative assessment finds mistakes before they settle. | (22), RPF "challenge misconceptions" (16) |
| **Drill a recurrent skill many times.** Each recipe has a drill set: 5–12 *near* variations that change only the target (sum odds vs sum evens, count by 3 vs by 5). | Part-task practice of a recurrent sub-skill, with high repetition and quick feedback, makes it automatic. | Part-task practice (26), deliberate practice (27) |
| **Balance the path, and say where she is.** Themes of similar weight, groups of 2 to 14 exercises, short titles, and on every exercise page *theme › group, exercise N of M*. Levels never go back inside a group. | A long flat list hides the pattern and makes progress feel slow; a visible position lowers anxiety. | COGA (9) |
| **Vary and space the drills.** Short sessions of several same-pattern drills, then mix in older sets. Not one giant exercise. | Deliberate practice is not rote: vary, distribute and break it into parts. | (27) |
| **Label loop subgoals the same way in every drill.** | Subgoal labels help most for loops. | (28) |
| **One topic per page.** A page answers one question; a second topic gets its own page and a link. | Short, focused pages are easier to scan and come back to. | COGA (9) |
| **Show, then tell.** Lead with a diagram, a table, an annotated example or a template; then a few short sentences. | Pictures plus words beat words alone. | Multimedia principle (2) |
| **One word for one thing.** The path is made of **themes**, split into **groups** of the same pattern (never "steps" or "weeks"); IDs never change. Every new word gets a glossary row. | Consistent terms lower load; a glossary helps readers with cognitive disabilities. | COGA (9) |
| **No calendar.** No week numbers, dates or catch-up plans; the roadmap is a path of themes. Theory (which loop, the maths) lives in the cookbook. | Dated plans go stale and make a learner who is behind feel late. | Learner personas (15) |
| **Theory comes from Microsoft Learn.** Link the module and video for each theme; never copy its text and never reference the content of a copyrighted book. | One trusted, free source keeps the theory consistent and the course legal. | Course policy |
| **No "just" or "simply"**, and never imply that some people are born programmers. | There is no "geek gene": skill comes from practice. | (23 tip 1), (15) |

## 2. Lesson format

Every cookbook recipe follows the same **6 steps**, in this order. Same order on every page means less to think about (COGA (9)).

| # | Step | What it holds | Why | Source |
| ---: | --- | --- | --- | --- |
| 1 | **Goal** | One concrete goal, in one sentence. | One new difficulty at a time. | (1, 20) |
| 2 | **Predict** | A small **working** example. She predicts the output; the answer is in `<details>`. | Read before write; predictions make running code useful. | PRIMM (4, 17), (23 tip 4) |
| 3 | **Trace it** | A trace table of the same example. | Tracing is its own skill, and comes before writing. | (5), RPF "read and explore code first" (16) |
| 4 | **The pattern** | Labelled subgoals, trigger words, the idea (with a diagram and its text), the template. | Subgoal labels help transfer to new problems. | (18, 19, 23 tip 6) |
| 5 | **Complete it** | A **partly written** variation: fill in the blanks, or arrange the lines (Parsons). Answer in `<details>`. | Fading: less help, same thinking. | (3, 6, 18), (23 tip 10) |
| 6 | **Your turn** | Exercise IDs to do alone in a real file, **plus** a small debugging task (answer in `<details>`) and the common mistakes. | Independent practice, then debugging on purpose. | (2, 22, 23) |

A recipe page does **not** repeat the full exercise: it links to it by ID.

## 3. Exercise types

| Type | What she does | When to use it | Source |
| --- | --- | --- | --- |
| Paper trace | Predict and trace, no computer. | Before the first exercise of a new loop idea. | PRIMM (4, 17) |
| Arrange the lines (Parsons) | All lines are in the starter file, mixed up and commented out. She orders them. | The first exercise of a recipe, when a blank file is too much. | (6, 23 tip 10) |
| Write a method | Fill in one method; `./ex check` tests it. | Most exercises. | (3, 5) |
| Fix the bugs | The starter compiles but has 1–2 planted bugs. `./ex check` shows which example fails. | Right after the matching "write" exercise. Bugs must be the *common mistakes* of the recipe. | (22, 23 tips 3, 9) |
| Mastery check | A new variation, alone, another day. | End of every exercise. | (5) |

The path also follows the order of two well-known beginner courses. Conditions come before loops. Loops come in small steps: simple loops, then loops with conditions, then nested loops after one-line loops. Methods come in once the loops are solid: see the University of Helsinki *Python Programming MOOC* (24) and Microsoft Learn *Get started with C#* (25). That is why one-row drawings (L09, L10) come before 2D grids (G01).

## 4. Plain language

| Rule | Source |
| --- | --- |
| Short sentences (aim for under 20 words). One idea per sentence. | GOV.UK (7), plainlanguage.gov (8) |
| Common words. Say "box" or "variable", not "storage location". Explain every new word once, and add it to the [glossary](glossary.md). | (7, 8), COGA (9) |
| Talk to the reader: "you". Active voice: "the loop adds 1", not "1 is added". | (8) |
| Put the most important thing first: the goal, then the details. | (7) |
| Use lists and tables instead of long paragraphs. | (8), COGA (9) |
| Give concrete examples with real numbers. | COGA (9) |

## 5. Accessible pages

| Rule | Source |
| --- | --- |
| Every image has **alt text** that says what the image shows (not "image of"). SVGs in `assets/` have a `<title>`. | WCAG 1.1.1 (10), W3C images tutorial (11) |
| Every diagram is a D2 SVG in `diagrams/` whose alt text is a full text version, and the same information is also written nearby. | W3C complex images (12), GitHub Docs diagrams (13) |
| **No emoji**, anywhere: pages, headings, diagrams, code comments, `./ex` output. Use words ("Guided", "OK", "NOT YET", "done"). Colour never carries meaning alone. | WCAG 1.4.1 (10), plain language (7, 8): emoji are noise for many readers and are read aloud oddly by screen readers. |
| Link text says where it goes ("open the solution for A01"), never "here" or a bare file name. | WCAG 2.4.4 (10), GitHub Docs style (14) |
| Headings in order (`#`, then `##`, then `###`), one `#` per page. | WCAG 1.3.1, 2.4.6 (10) |
| Same navigation on every page: breadcrumb on top, Previous/Next at the bottom. | WCAG 3.2.3 (10), COGA (9) |
| Hidden content (hints) uses `<details>`, which works with the keyboard and screen readers. | COGA (9) |

## 6. Sources

1. Paas, Tuovinen, Tabbers, Van Gerven (2003). *Cognitive Load Measurement as a Means to Advance Cognitive Load Theory.* Educational Psychologist. <https://doi.org/10.1207/S15326985EP3801_8>
2. Kirschner, Sweller, Clark (2006). *Why Minimal Guidance During Instruction Does Not Work.* Educational Psychologist. <https://doi.org/10.1207/s15326985ep4102_1>
3. Renkl, Atkinson (2003). *Structuring the Transition From Example Study to Problem Solving in Cognitive Skill Acquisition.* Educational Psychologist. <https://doi.org/10.1207/S15326985EP3801_3>
4. Sentance, Waite, Kallia (2019). *Teaching computer programming with PRIMM: a sociocultural perspective.* Computer Science Education. <https://doi.org/10.1080/08993408.2019.1608781> · <https://primmportal.com/>
5. Xie, Loksa, Nelson, Davidson et al. (2019). *A theory of instruction for introductory programming skills.* Computer Science Education. <https://doi.org/10.1080/08993408.2019.1565235>
6. Parsons problems (overview and research). <https://en.wikipedia.org/wiki/Parsons_problems>
7. GOV.UK, *Writing for GOV.UK.* <https://www.gov.uk/guidance/content-design/writing-for-gov-uk>
8. plainlanguage.gov, *Federal Plain Language Guidelines.* <https://www.plainlanguage.gov/guidelines/>
9. W3C, *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA). <https://www.w3.org/TR/coga-usable/>
10. W3C, *WCAG 2.2 Quick Reference.* <https://www.w3.org/WAI/WCAG22/quickref/>
11. W3C WAI, *An alt Decision Tree.* <https://www.w3.org/WAI/tutorials/images/decision-tree/>
12. W3C WAI, *Complex Images.* <https://www.w3.org/WAI/tutorials/images/complex/>
13. GitHub Docs, *Creating diagrams for GitHub Docs.* <https://docs.github.com/en/contributing/writing-for-github-docs/creating-diagrams-for-github-docs>
14. GitHub Docs, *Style guide.* <https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide>
15. Greg Wilson (2019). *Teaching Tech Together*, chapters "A Lesson Design Process" (learner personas, learning objectives) and "Cognitive Architecture" (faded examples, Parsons problems). <https://teachtogether.tech/en/index.html#s:process>
16. Raspberry Pi Foundation, *Our computing pedagogy* (12 principles). <https://www.raspberrypi.org/teach/pedagogy>
17. Raspberry Pi Foundation, *Pedagogy Quick Read: PRIMM*. <https://static.raspberrypi.org/files/curriculum/quickreads/11-Pedagogy_Summary_PRIMM_V4_2023.pdf>
18. Raspberry Pi Foundation, *Pedagogy Quick Read: Worked examples* (at least two examples, fading, subgoal labels). <https://static.raspberrypi.org/files/curriculum/quickreads/2-Pedagogy_Summary_Worked_Examples_V6_2023.pdf>
19. Raspberry Pi Foundation, *Pedagogy Quick Read: Subgoal labels*. <https://static.raspberrypi.org/files/curriculum/quickreads/QR_31_Subgoal_Labels_29_11_2026.pdf>
20. The Carpentries, *Collaborative Lesson Development Training: Defining lesson objectives*. <https://carpentries.github.io/lesson-development-training/objectives.html>
21. The Carpentries, *Collaborative Lesson Development Training: Learner profiles*. <https://carpentries.github.io/lesson-development-training/profiles.html>
22. The Carpentries, *Collaborative Lesson Development Training: Formative assessment*. <https://carpentries.github.io/lesson-development-training/formative-assessment.html>
23. Brown, Wilson (2018). *Ten quick tips for teaching programming.* PLOS Computational Biology. <https://doi.org/10.1371/journal.pcbi.1006023>
24. University of Helsinki, *Python Programming MOOC 2024* (order of topics). <https://programming-24.mooc.fi/>
25. Microsoft Learn, *Get started with C#* learning paths (order of topics). <https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/>
26. Learning Design Alliance, *Part-task practice*. <https://wiki.learningdesignalliance.org/elements/part-task-practice/>
27. American Psychological Association, *How do students become good at a skill? Practice and the acquisition of knowledge.* <https://www.apa.org/education-career/k12/practice-acquisition>
28. Morrison, Margulieux, Decker (2020). *The Curious Case of Loops* (subgoal labelled worked examples for loops). Computer Science Education. <https://par.nsf.gov/servlets/purl/10171483>

---

[Home](../../README.md) · [AGENTS.md](../../AGENTS.md)
