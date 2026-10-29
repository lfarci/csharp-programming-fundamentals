[Home](../README.md) › [Exercises](README.md) › [Loops: draw in 2D](../themes/loops-2d.md) › G06

# G06 · Pyramid

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | hard | [Loops: draw in 2D](../themes/loops-2d.md) | [Nested grid](../cookbook/08-nested-grid.md) | [G02](G02-right-triangle.md) | Custom |

## Goal

Print a centered pyramid of `*`, `height` rows high.

## Start and check

```bash
./ex start G06     # creates practice/G06_Pyramid.cs (never overwrites your work)
./ex check G06     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawPyramid(int height)`: input = height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawPyramid(3)` | prints:<br>`  *`<br>` ***`<br>`*****` |
| `DrawPyramid(1)` | prints:<br>`*` |

## Edge cases to test

- Height 1.

## Rules

- Nested loops: **two** inner loops (spaces, then stars).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Make a table for height 3: row → spaces → stars. Row 1: 2 spaces, 1 star. Row 2: 1 space, 3 stars. Row 3: 0, 5.

</details>

<details><summary>Hint 2</summary>

Spaces = `height - row`. Stars = `2 * row - 1`.

</details>

<details><summary>Hint 3</summary>

Inside the row loop: first a loop for the spaces, then a loop for the stars, then `WriteLine()`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Draw a diamond (a pyramid, then the same pyramid upside down).

## Solution

Only after a real try: [open the solution for G06](../solutions/G06_Pyramid.cs). Your solution can be different and still correct!

---

Previous: [G05 · Checkerboard](G05-checkerboard.md) · [All exercises](README.md) · Next: [D01 · Last digit](D01-last-digit.md)
