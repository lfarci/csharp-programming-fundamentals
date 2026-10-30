---
prev:
  text: "G07 · Arrange: a square"
  link: /exercises/G07-arrange-a-square
next:
  text: "G01 · Draw a rectangle"
  link: /exercises/G01-rectangle
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw rows and grids](../themes/loops-draw-rows-and-grids.md) › G08

# G08 · Solid square

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw rows and grids** · exercise 4 of 8 in this group (45 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Nested grid](../cookbook/08-nested-grid.md) | [G07](G07-arrange-a-square.md) |

</div>

## Goal

Print a square of `*`, `size` wide and `size` high.

## Start and check

```bash
./ex start G08     # creates practice/G08_SolidSquare.cs (never overwrites your work)
./ex check G08     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawSquare(int size)`: input = size, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawSquare(3)` | prints:<br>`***`<br>`***`<br>`***` |
| `DrawSquare(1)` | prints:<br>`*` |

## Edge cases to test

- size = 1: one star.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

G07 again, now from a blank file: the inner loop prints one row, the outer loop repeats it.

</details>

<details><summary>Hint 2</summary>

`Console.WriteLine();` after the inner loop ends the row.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print a rectangle twice as wide as it is high: `size` rows of `2 × size` stars.

## Solution

Only after a real try: [open the solution for G08](../../internal/solutions/G08_SolidSquare.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G07 · Arrange: a square](G07-arrange-a-square.md) · [Loops](../themes/loops.md) · Next: [G01 · Draw a rectangle](G01-rectangle.md)

</div>
