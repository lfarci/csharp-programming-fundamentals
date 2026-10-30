---
prev:
  text: "G13 · Diagonal"
  link: /exercises/G13-diagonal
next:
  text: "G06 · Pyramid"
  link: /exercises/G06-pyramid
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw shapes](../themes/loops-draw-shapes.md) › G05

# G05 · Checkerboard

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw shapes** · exercise 7 of 8 in this group (54 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Challenge | medium | write code | [Nested grid](../cookbook/08-nested-grid.md) | [G04](G04-hollow-rectangle.md), [C01](C01-even-or-odd.md) |

</div>

## Goal

Print a size×size checkerboard with `#` and `.`, starting with `#` in the top-left corner.

## Start and check

```bash
./ex start G05     # creates practice/G05_Checkerboard.cs (never overwrites your work)
./ex check G05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawCheckerboard(int size)`: input = size, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawCheckerboard(4)` | prints:<br>`#.#.`<br>`.#.#`<br>`#.#.`<br>`.#.#` |
| `DrawCheckerboard(1)` | prints:<br>`#` |

## Edge cases to test

- Odd size.

`./ex check` tests these too: `DrawCheckerboard(3)` prints `#.#` `.#.` `#.#`.

## Rules

- Nested loops. No `string` tricks.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Look at `row + col` for every `#` cell. What do they have in common?

</details>

<details><summary>Hint 2</summary>

Even sum → `#`, odd sum → `.` (with rows and columns starting at 1).

</details>

## Mastery check

Solve this variation **alone**, on another day:

Make each square 2×2 characters big.

## Solution

Only after a real try: [open the solution for G05](../../internal/solutions/G05_Checkerboard.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G13 · Diagonal](G13-diagonal.md) · [Loops](../themes/loops.md) · Next: [G06 · Pyramid](G06-pyramid.md)

</div>
