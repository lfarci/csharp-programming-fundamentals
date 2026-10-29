---
prev:
  text: "L08 · Guess the number"
  link: /exercises/L08-guess-the-number
next:
  text: "L10 · Numbers on one line"
  link: /exercises/L10-numbers-on-one-line
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw rows and grids](../themes/loops.md#draw-rows-and-grids) › L09

# L09 · Draw one row

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw rows and grids** · exercise 1 of 8 in this group (40 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Counter loop](../cookbook/01-counter-loop.md), [Nested grid](../cookbook/08-nested-grid.md) | [L03](L03-count-up-and-down.md) |

</div>

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

<div class="gh-only">

Previous: [L08 · Guess the number](L08-guess-the-number.md) · [Loops](../themes/loops.md) · Next: [L10 · Numbers on one line](L10-numbers-on-one-line.md)

</div>
