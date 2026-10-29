[Home](../README.md) › [Exercises](README.md) › [Loops: draw in 2D](../themes/loops-2d.md) › G01

# G01 · Draw a rectangle

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: draw in 2D](../themes/loops-2d.md) | [Nested grid](../cookbook/08-nested-grid.md) | [L09](L09-draw-a-row.md) | Custom |

## Goal

Print a rectangle of `*`, `width` wide and `height` high.

## Start and check

```bash
./ex start G01     # creates practice/G01_Rectangle.cs (never overwrites your work)
./ex check G01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawRectangle(int width, int height)`: input = width, an int (whole number), height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawRectangle(4, 3)` | prints:<br>`****`<br>`****`<br>`****` |
| `DrawRectangle(1, 2)` | prints:<br>`*`<br>`*` |

## Edge cases to test

- Width 1 → a vertical line.

## Rules

- Two nested `for` loops. Print one `*` at a time.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Step 1: print **one** line of `width` stars with one loop.

</details>

<details><summary>Hint 2</summary>

Step 2: repeat that line `height` times → put it in another loop.

</details>

<details><summary>Hint 3</summary>

`Console.Write("*")` in the inner loop, `Console.WriteLine()` after it.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Read the character to use too (`#`, `o`, …).

## Solution

Only after a real try: [open the solution for G01](../solutions/G01_Rectangle.cs). Your solution can be different and still correct!

---

Previous: [G07 · Arrange the lines: a square](G07-arrange-a-square.md) · [All exercises](README.md) · Next: [G08 · Solid square](G08-solid-square.md)
