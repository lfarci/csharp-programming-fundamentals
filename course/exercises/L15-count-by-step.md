---
prev:
  text: "L18 · Square numbers"
  link: /exercises/L18-squares
next:
  text: "L04 · Multiplication table"
  link: /exercises/L04-multiplication-table
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Count](../themes/loops.md#count) › L15

# L15 · Count by any step

<ExerciseHeader />

<div class="gh-only">

**Loops › Count** · exercise 12 of 13 in this group (12 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Counter loop](../cookbook/01-counter-loop.md) | [L14](L14-count-by-5.md) |

</div>

## Goal

Print `step`, 2×`step`, 3×`step`, … up to n, one per line. (`step` is at least 1.)

## Start and check

```bash
./ex start L15     # creates practice/L15_CountByStep.cs (never overwrites your work)
./ex check L15     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void CountByStep(int step, int n)`: input = step, an int (whole number), n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountByStep(2, 7)` | prints:<br>`2`<br>`4`<br>`6` |
| `CountByStep(4, 12)` | prints:<br>`4`<br>`8`<br>`12` |
| `CountByStep(1, 3)` | prints:<br>`1`<br>`2`<br>`3` |

## Edge cases to test

- `step` bigger than n: nothing.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

L13 and L14 with the 3 or 5 replaced by `step`.

</details>

<details><summary>Hint 2</summary>

Start at `step`, step `i += step`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the multiples of `step` from n down to `step`.

## Solution

Only after a real try: [open the solution for L15](../../internal/solutions/L15_CountByStep.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L18 · Square numbers](L18-squares.md) · [Loops](../themes/loops.md) · Next: [L04 · Multiplication table](L04-multiplication-table.md)

</div>
