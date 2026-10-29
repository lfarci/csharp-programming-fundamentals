[Home](../README.md) › [Exercises](README.md) › [Loops: draw in 2D](../themes/loops-2d.md) › G08

# G08 · Solid square

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: draw in 2D](../themes/loops-2d.md) | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md) | Custom |

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

G01 with width and height both equal to `size`.

</details>

<details><summary>Hint 2</summary>

Inner loop: one row. Outer loop: repeat the row.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print a square of `o`.

## Solution

Only after a real try: [open the solution for G08](../solutions/G08_SolidSquare.cs). Your solution can be different and still correct!

---

Previous: [G01 · Draw a rectangle](G01-rectangle.md) · [All exercises](README.md) · Next: [G09 · Rows of numbers](G09-number-rows.md)
