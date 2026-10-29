[Home](../README.md) › Cookbook

# The loop cookbook

A **recipe** is a small piece of code you can recognize and reuse. Almost every beginner exercise is **one recipe**, or **two or three recipes glued together**.

Learn them like cooking: first follow the recipe exactly, then change one ingredient, then invent your own dish.

## The 12 recipes

<CardList list="recipes" />

### Trigger words at a glance

| # | Recipe | Trigger words: you read… | Box(es) to keep | Loop |
| ---: | --- | --- | --- | --- |
| 1 | [Counter loop](01-counter-loop.md) | "from 1 to N", "N times", "count down" | `i` | `for` |
| 2 | [Accumulator](02-accumulator.md) | "sum", "total", "how many", "product", "factorial", "power" | `sum = 0` / `count = 0` / `product = 1` | `for` |
| 3 | [Conditional accumulator](03-conditional-accumulator.md) | "sum of the **even**…", "count the… **that**…", "multiples of" | box + `if` filter | `for` |
| 4 | [Min / max tracker](04-min-max.md) | "largest", "smallest", "best", "highest" | `max = first value` | `for` / `foreach` |
| 5 | [Flag / search](05-flag-search.md) | "is there", "contains", "is it prime", "find the position" | `found = false` / `index = -1` | `for` + `break` |
| 6 | [Digit extraction](06-digit-extraction.md) | "digits", "reverse the number", "palindrome", "Armstrong" | `remaining`, `digit` | `while (remaining > 0)` |
| 7 | [State update](07-state-update.md) | "each term is the sum of the previous two", "Fibonacci", "sequence" | `previous`, `current`, `next` | `for` / `while` |
| 8 | [Nested loops / 2D grid](08-nested-grid.md) | "draw", "rectangle", "triangle", "grid", "board", "every pair" | `row`, `col` | `for` in `for` |
| 9 | [Input validation](09-input-validation.md) | "between 1 and 10", "ask again", "must be valid" | `valid` | `do … while` |
| 10 | [Sentinel loop](10-sentinel-loop.md) | "until the user enters 0", "-1 to stop" | boxes of other recipes | `while (true)` + `break` |
| 11 | [Array traversal](11-array-traversal.md) | "array", "each element", "lines of a file" | `i`, `values[i]` | `for` / `foreach` |
| 12 | [Build a string](12-string-building.md) | "each letter", "remove", "reverse the word", "join" | `result = ""` | `foreach` |

## How to pick a recipe

Ask the questions from top to bottom. The first **yes** gives your recipe.

![How to pick a recipe, as questions from top to bottom. A picture of rows and columns: 8, nested loops. Read input until it is OK: 9, input validation. Values come until a stop value: 10, sentinel loop plus a recipe below. Work on the digits of a number: 6, digit extraction plus a recipe below. Next value depends on the last ones: 7, state update. A list of values to print: 1, counter loop. One total, count or product: 2, accumulator, or 3 if only some values. The biggest or the smallest: 4, min and max. Yes or no, or a position: 5, flag and search. A new text: 12, build a string.](../diagrams/cookbook-index.svg)

Values stored in an **array**, a **list** or a **file**? Use [11 · Array traversal](11-array-traversal.md) to visit them, and the recipe from the diagram for the work.

## Theory pages

- [Which loop should I use?](which-loop.md): `for`, `while`, `do … while` or `foreach`.
- [Combining recipes](combining-recipes.md): two or three recipes in one exercise.
- [The maths behind the exercises](the-maths.md): sum, factorial, power, prime… with tiny examples.

## Recipe card (the same 5 questions every time)

Before writing code, fill this card on paper:

| Question | Example: factorial of 5 |
| --- | --- |
| 1. What is the **result**? | one number: 1 × 2 × 3 × 4 × 5 |
| 2. Which **recipe(s)**? | counter loop + product accumulator |
| 3. Which **boxes**, and their **start** value? | `product = 1` |
| 4. What **repeats**, and what **stops** it? | multiply by `i`, for `i` from 1 to 5 |
| 5. **Tiny example** traced by hand? | 1 → 1 → 2 → 6 → 24 → 120 |

Then translate the card into C#. If you can't fill line 5, you are not ready to code yet — and that's fine.

## How every recipe page is built

Every recipe is one short lesson, always in the same 6 steps. Do them in order, with a pen:

1. **Goal** — what you will be able to do, in one sentence.
2. **Predict** — read a small working program and write down what it prints. Then check.
3. **Trace it** — follow the same program turn by turn in a table.
4. **The pattern** — the steps with names (*subgoals*), the trigger words, a diagram and the template.
5. **Complete it** — fill the blanks or put mixed-up lines in order. Then check.
6. **Your turn** — exercises to do alone, a small bug to find, and the common mistakes.

Some exercises are special: **arrange the lines** (all the code is given, mixed up) and **fix the bugs** (the code is given, with mistakes). Both are checked by `./ex check` like the others.

New to algorithms? Start with [Solving a problem](../docs/problem-solving.md).
