---
prev:
  text: "G02 · Draw a right triangle"
  link: /exercises/G02-right-triangle
next:
  text: "G11 · Counting triangle"
  link: /exercises/G11-counting-triangle
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw shapes](../themes/loops-draw-shapes.md) › G10

# G10 · Triangle of row numbers

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw shapes** · exercise 2 of 8 in this group (51 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Nested grid](../cookbook/08-nested-grid.md) | [G02](G02-right-triangle.md) |

</div>

## Goal

Print a triangle where row r is the digit r, written r times: `1`, `22`, `333`.

## Start and check

```bash
./ex start G10     # creates practice/G10_RowNumberTriangle.cs (never overwrites your work)
./ex check G10     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawRowTriangle(int height)`: input = height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawRowTriangle(3)` | prints:<br>`1`<br>`22`<br>`333` |
| `DrawRowTriangle(1)` | prints:<br>`1` |

## Edge cases to test

- height = 1: `1`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

G02 (triangle): the inner loop goes up to `row`.

</details>

<details><summary>Hint 2</summary>

Print `row` instead of `*`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print `1`, `12`, `123` instead.

## Solution

Only after a real try: [open the solution for G10](../../internal/solutions/G10_RowNumberTriangle.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G02 · Draw a right triangle](G02-right-triangle.md) · [Loops](../themes/loops.md) · Next: [G11 · Counting triangle](G11-counting-triangle.md)

</div>
