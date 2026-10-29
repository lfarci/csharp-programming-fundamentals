---
prev:
  text: "C03 · Ticket price"
  link: /exercises/C03-ticket-price
next:
  text: "Next theme: Loops"
  link: /themes/loops
---

[Home](../README.md) › [Exercises](README.md) › [Basics](../themes/basics.md) › [Conditions](../themes/basics.md#conditions) › C04

# C04 · Grade from a score

<ExerciseHeader />

<div class="gh-only">

**Basics › Conditions** · exercise 4 of 4 in this group (7 of 7 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | — | [C03](C03-ticket-price.md) |

</div>

## Goal

Give back the grade for a score from 0 to 100: 90 or more → `"A"`, 80–89 → `"B"`, 70–79 → `"C"`, 50–69 → `"D"`, below 50 → `"F"`.

## Start and check

```bash
./ex start C04     # creates practice/C04_GradeFromAScore.cs (never overwrites your work)
./ex check C04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `string Grade(int score)`: input = score, an int (whole number); result = a string (text), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Grade(95)` | `"A"` |
| `Grade(90)` | `"A"` |
| `Grade(89)` | `"B"` |
| `Grade(80)` | `"B"` |
| `Grade(75)` | `"C"` |
| `Grade(50)` | `"D"` |
| `Grade(49)` | `"F"` |
| `Grade(0)` | `"F"` |

## Edge cases to test

- Exactly 90, 80, 70 and 50: which grade? Test the borders.
- 0 and 100.

## Rules

- Use one `if` / `else if` / `else` chain. Test the biggest border first.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [reading worksheet](../docs/reading-an-exercise.md#the-template): what goes in? what comes out? a tiny example by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Write the borders on a number line first: 0 … 50 … 70 … 80 … 90 … 100.

</details>

<details><summary>Hint 2</summary>

Start with `if (score >= 90) return "A";`. The next test only runs when the first one was false, so `else if (score >= 80)` already means 80 to 89.

</details>

<details><summary>Hint 3</summary>

The last case (below 50) needs no test: a plain `else` or a final `return "F";`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Write `Season(int month)`: 12, 1, 2 → `"winter"`, 3–5 → `"spring"`, 6–8 → `"summer"`, 9–11 → `"autumn"`.

## Solution

Only after a real try: [open the solution for C04](../solutions/C04_GradeFromAScore.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [C03 · Ticket price](C03-ticket-price.md) · [Basics](../themes/basics.md) · Next: [Next theme: Loops](../themes/loops.md)

</div>
