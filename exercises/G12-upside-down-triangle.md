[Home](../README.md) › [Exercises](README.md) › [Loops: draw in 2D](../themes/loops-2d.md) › G12

# G12 · Upside-down triangle

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: draw in 2D](../themes/loops-2d.md) | [Nested grid](../cookbook/08-nested-grid.md) | [G02](G02-right-triangle.md), [L12](L12-count-down.md) | Custom |

## Goal

Print a triangle whose first row has `height` stars, then one less on each row.

## Start and check

```bash
./ex start G12     # creates practice/G12_UpsideDownTriangle.cs (never overwrites your work)
./ex check G12     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawUpsideDown(int height)`: input = height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawUpsideDown(3)` | prints:<br>`***`<br>`**`<br>`*` |
| `DrawUpsideDown(1)` | prints:<br>`*` |

## Edge cases to test

- height = 1: one star.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Make the outer loop count down: `row = height; row >= 1; row--`.

</details>

<details><summary>Hint 2</summary>

The inner loop stays `col <= row`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the counting triangle (G11) upside down.

## Solution

Only after a real try: [open the solution for G12](../solutions/G12_UpsideDownTriangle.cs). Your solution can be different and still correct!

---

Previous: [G11 · Counting triangle](G11-counting-triangle.md) · [All exercises](README.md) · Next: [G14 · Numbers in columns](G14-numbers-in-columns.md)
