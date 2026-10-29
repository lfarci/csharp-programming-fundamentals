---
prev:
  text: "G14 · Numbers in columns"
  link: /exercises/G14-numbers-in-columns
next:
  text: "G02 · Draw a right triangle"
  link: /exercises/G02-right-triangle
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw rows and grids](../themes/loops.md#draw-rows-and-grids) › G03

# G03 · Multiplication grid

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw rows and grids** · exercise 8 of 8 in this group (47 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md), [L04](L04-multiplication-table.md), [G14](G14-numbers-in-columns.md) |

</div>

## Goal

Print an n×n grid where the cell at row `r` and column `c` contains `r × c`. Each number takes 4 characters (right-aligned).

## Start and check

```bash
./ex start G03     # creates practice/G03_MultiplicationGrid.cs (never overwrites your work)
./ex check G03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawGrid(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawGrid(4)` | prints:<br>`   1   2   3   4`<br>`   2   4   6   8`<br>`   3   6   9  12`<br>`   4   8  12  16` |
| `DrawGrid(1)` | prints:<br>`   1` |

## Edge cases to test

- N = 1 → one cell.

## Rules

- Nested loops.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Same skeleton as G01, but print a number instead of a star.

</details>

<details><summary>Hint 2</summary>

Right-align on 4 characters, like in [G14](G14-numbers-in-columns.md): `Console.Write($"{row * col,4}");`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Only print the cells where `c <= r` (a triangle of numbers).

## Solution

Only after a real try: [open the solution for G03](../../internal/solutions/G03_MultiplicationGrid.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G14 · Numbers in columns](G14-numbers-in-columns.md) · [Loops](../themes/loops.md) · Next: [G02 · Draw a right triangle](G02-right-triangle.md)

</div>
