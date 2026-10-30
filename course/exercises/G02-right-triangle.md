---
prev:
  text: "G03 · Multiplication grid"
  link: /exercises/G03-multiplication-grid
next:
  text: "G10 · Triangle of row numbers"
  link: /exercises/G10-row-number-triangle
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw shapes](../themes/loops-draw-shapes.md) › G02

# G02 · Draw a right triangle

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw shapes** · exercise 1 of 8 in this group (50 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | medium | write code | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md) |

</div>

## Goal

Print a right triangle of `height` rows: row 1 has 1 star, row 2 has 2 stars, …

## Start and check

```bash
./ex start G02     # creates practice/G02_RightTriangle.cs (never overwrites your work)
./ex check G02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawTriangle(int height)`: input = height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawTriangle(4)` | prints:<br>`*`<br>`**`<br>`***`<br>`****` |
| `DrawTriangle(1)` | prints:<br>`*` |

## Edge cases to test

- Height 1.

## Rules

- Nested loops.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Make a table: row → number of stars. Row 3 has 3 stars.

</details>

<details><summary>Hint 2</summary>

Only the **test** of the inner loop changes compared to G01: `col <= row`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Draw it upside down (4 stars, then 3, 2, 1).

## Solution

Only after a real try: [open the solution for G02](../../internal/solutions/G02_RightTriangle.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G03 · Multiplication grid](G03-multiplication-grid.md) · [Loops](../themes/loops.md) · Next: [G10 · Triangle of row numbers](G10-row-number-triangle.md)

</div>
