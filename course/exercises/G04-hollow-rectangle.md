---
prev:
  text: "G12 · Upside-down triangle"
  link: /exercises/G12-upside-down-triangle
next:
  text: "G13 · Diagonal"
  link: /exercises/G13-diagonal
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw shapes](../themes/loops-draw-shapes.md) › G04

# G04 · Hollow rectangle

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw shapes** · exercise 5 of 8 in this group (54 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md) |

</div>

## Goal

Print only the border of a `width` × `height` rectangle with `*`; the inside is spaces.

## Start and check

```bash
./ex start G04     # creates practice/G04_HollowRectangle.cs (never overwrites your work)
./ex check G04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawHollowRectangle(int width, int height)`: input = width, an int (whole number), height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawHollowRectangle(5, 4)` | prints:<br>`*****`<br>`*   *`<br>`*   *`<br>`*****` |
| `DrawHollowRectangle(3, 3)` | prints:<br>`***`<br>`* *`<br>`***` |

## Edge cases to test

- Height 1 or 2 → no inside.

`./ex check` tests these too: `DrawHollowRectangle(4, 2)` prints `****` `****`.

## Rules

- Nested loops + one `if` inside.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A cell is on the border if it is in the first row, the last row, the first column or the last column.

</details>

<details><summary>Hint 2</summary>

`if (row == 1 || row == height || col == 1 || col == width)`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Draw an X inside a square (cells where `row == col` or `row + col == size + 1`).

## Solution

Only after a real try: [open the solution for G04](../../internal/solutions/G04_HollowRectangle.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G12 · Upside-down triangle](G12-upside-down-triangle.md) · [Loops](../themes/loops.md) · Next: [G13 · Diagonal](G13-diagonal.md)

</div>
