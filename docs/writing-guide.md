🏠 [Home](../README.md) › ✍️ Writing guide (for coaches and agents)

# ✍️ Writing guide

How we write for a **struggling beginner**. Every rule below comes from a source listed at the end; numbers in brackets, like (2), point to that list. [AGENTS.md](../AGENTS.md) turns these rules into the review rubric.

## 1. Teaching rules (how people learn to program)

| Rule | Why | Source |
| --- | --- | --- |
| **One new difficulty per exercise.** Everything else in it is already known. | Working memory is small. Two new ideas at once overload it. | Cognitive load theory (1, 2) |
| **Worked example first, then fade the help.** Recipe page (full example) → 🟢 Guided (hints do most of the steps) → 🔵 Independent → 🟣 Challenge. | Beginners learn more from studied examples than from solving alone; help is removed step by step. | Worked examples, fading (3, 2) |
| **Read code before writing code.** Predict, trace, then modify, then make. Paper exercises (L01, L02, S01) come first. | Reading and tracing are separate skills that come before writing. | PRIMM (4), theory of instruction (5) |
| **Name the plan.** Recipes have a name, trigger words and a template. | Novices lack "plans"; naming them makes them reusable. | Theory of instruction (5) |
| **Arrange-the-lines tasks are welcome** for a new recipe (give the lines, mixed up). | Lower load than a blank page, same thinking. | Parsons problems (6) |
| **Hints one at a time, solutions far away.** | Minimal guidance does not work for novices, but too much help removes the thinking. | (2) |
| **Mastery = a new variation, alone, another day.** | Spaced, independent retrieval shows real learning. | (5) |

## 2. Plain language

| Rule | Source |
| --- | --- |
| Short sentences (aim for under 20 words). One idea per sentence. | GOV.UK (7), plainlanguage.gov (8) |
| Common words. Say "box" or "variable", not "storage location". Explain every new word once, and add it to the [glossary](glossary.md). | (7, 8), COGA (9) |
| Talk to the reader: "you". Active voice: "the loop adds 1", not "1 is added". | (8) |
| Put the most important thing first: the goal, then the details. | (7) |
| Use lists and tables instead of long paragraphs. | (8), COGA (9) |
| Give concrete examples with real numbers. | COGA (9) |

## 3. Accessible pages

| Rule | Source |
| --- | --- |
| Every image has **alt text** that says what the image shows (not "image of"). SVGs in `assets/` have a `<title>`. | WCAG 1.1.1 (10), W3C images tutorial (11) |
| Every Mermaid diagram has `accTitle` and `accDescr`, and the same information is also written as text nearby. | Mermaid accessibility (12), GitHub Docs diagrams (13) |
| Colour and emoji never carry meaning alone. Next to 🟢 we write "Guided". | WCAG 1.4.1 (10) |
| Link text says where it goes ("open the solution for A01"), never "here" or a bare file name. | WCAG 2.4.4 (10), GitHub Docs style (14) |
| Headings in order (`#`, then `##`, then `###`), one `#` per page. | WCAG 1.3.1, 2.4.6 (10) |
| Same navigation on every page: breadcrumb on top, Previous/Next at the bottom. | WCAG 3.2.3 (10), COGA (9) |
| Hidden content (hints) uses `<details>`, which works with the keyboard and screen readers. | COGA (9) |

## 4. Sources

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
12. Mermaid, *Accessibility options.* <https://mermaid.js.org/config/accessibility.html>
13. GitHub Docs, *Creating diagrams for GitHub Docs.* <https://docs.github.com/en/contributing/writing-for-github-docs/creating-diagrams-for-github-docs>
14. GitHub Docs, *Style guide.* <https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide>

---

⬅️ [Home](../README.md) · [AGENTS.md](../AGENTS.md)
