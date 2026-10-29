[Home](../README.md) › [Exercises](README.md) › [Loops: draw in 2D](../themes/loops-2d.md) › G09

# G09 · Rows of numbers

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: draw in 2D](../themes/loops-2d.md) | [Nested grid](../cookbook/08-nested-grid.md) | [G08](G08-solid-square.md) | Custom |

## Goal

Print `height` rows; each row is `1234…` up to `width`.

## Start and check

```bash
./ex start G09     # creates practice/G09_NumberRows.cs (never overwrites your work)
./ex check G09     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawNumberRows(int width, int height)`: input = width, an int (whole number), height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawNumberRows(4, 2)` | prints:<br>`1234`<br>`1234` |
| `DrawNumberRows(3, 3)` | prints:<br>`123`<br>`123`<br>`123` |

## Edge cases to test

- width = 1: every row is `1`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

G01, but print `col` instead of `*`.

</details>

<details><summary>Hint 2</summary>

`Console.Write(col);`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the row number instead: `111`, `222`, `333`.

## Solution

Only after a real try: [open the solution for G09](../solutions/G09_NumberRows.cs). Your solution can be different and still correct!

---

Previous: [G08 · Solid square](G08-solid-square.md) · [All exercises](README.md) · Next: [G02 · Draw a right triangle](G02-right-triangle.md)
