---
prev:
  text: "G04 · Hollow rectangle"
  link: /exercises/G04-hollow-rectangle
next:
  text: "G05 · Checkerboard"
  link: /exercises/G05-checkerboard
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw shapes](../themes/loops-draw-shapes.md) › G13

# G13 · Diagonal

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw shapes** · exercise 6 of 8 in this group (55 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Nested grid](../cookbook/08-nested-grid.md) | [G08](G08-solid-square.md), [G04](G04-hollow-rectangle.md) |

</div>

## Goal

Print a `size` × `size` square of `.` with `*` on the diagonal (where row equals column).

## Start and check

```bash
./ex start G13     # creates practice/G13_Diagonal.cs (never overwrites your work)
./ex check G13     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawDiagonal(int size)`: input = size, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawDiagonal(3)` | prints:<br>`*..`<br>`.*.`<br>`..*` |
| `DrawDiagonal(1)` | prints:<br>`*` |

## Edge cases to test

- size = 1: `*`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

G08 square, with an `if` inside the inner loop.

</details>

<details><summary>Hint 2</summary>

`if (row == col)` print `*`, else `.`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Put the `*` on the other diagonal (`row + col == size + 1`).

## Solution

Only after a real try: [open the solution for G13](../../internal/solutions/G13_Diagonal.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G04 · Hollow rectangle](G04-hollow-rectangle.md) · [Loops](../themes/loops.md) · Next: [G05 · Checkerboard](G05-checkerboard.md)

</div>
