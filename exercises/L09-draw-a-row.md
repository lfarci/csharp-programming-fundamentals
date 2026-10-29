[Home](../README.md) › [Exercises](README.md) › [Loops: draw in 2D](../themes/loops-2d.md) › L09

# L09 · Draw one row

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: draw in 2D](../themes/loops-2d.md) | [Counter loop](../cookbook/01-counter-loop.md), [Nested grid](../cookbook/08-nested-grid.md) | [L03](L03-count-up-and-down.md) | Custom |

## Goal

Print `width` stars **on one line**, then end the line. `DrawRow(5)` prints `*****`. This is the inside of every 2D drawing.

## Start and check

```bash
./ex start L09     # creates practice/L09_DrawARow.cs (never overwrites your work)
./ex check L09     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawRow(int width)`: input = width, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawRow(5)` | prints:<br>`*****` |
| `DrawRow(1)` | prints:<br>`*` |
| `DrawRow(0)` | prints:<br>`` |

## Edge cases to test

- `DrawRow(0)` prints only the line break.

## Rules

- Use `Console.Write` inside the loop and **one** `Console.WriteLine()` after it.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`Console.Write("*")` prints a star and stays on the same line. `Console.WriteLine()` ends the line.

</details>

<details><summary>Hint 2</summary>

The loop runs `width` times. Where does the line break go: inside or after the loop?

</details>

## Mastery check

Solve this variation **alone**, on another day:

Write `DrawDashes(int width)` that prints `-*-*-` style rows: a dash at odd positions, a star at even ones.

## Solution

Only after a real try: [open the solution for L09](../solutions/L09_DrawARow.cs). Your solution can be different and still correct!

---

Previous: [A22 · Sum of the divisors](A22-sum-of-divisors.md) · [All exercises](README.md) · Next: [L10 · Numbers on one line](L10-numbers-on-one-line.md)
