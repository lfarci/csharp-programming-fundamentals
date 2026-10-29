---
prev:
  text: "G09 · Rows of numbers"
  link: /exercises/G09-number-rows
next:
  text: "G03 · Multiplication grid"
  link: /exercises/G03-multiplication-grid
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Draw rows and grids](../themes/loops.md#draw-rows-and-grids) › G14

# G14 · Numbers in columns

<ExerciseHeader />

<div class="gh-only">

**Loops › Draw rows and grids** · exercise 7 of 8 in this group (46 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Counter loop](../cookbook/01-counter-loop.md), [Nested grid](../cookbook/08-nested-grid.md) | [L10](L10-numbers-on-one-line.md) |

</div>

## Goal

Print 10, 20, …, n × 10 on **one** line, each number in a column 4 characters wide.

## Start and check

```bash
./ex start G14     # creates practice/G14_NumbersInColumns.cs (never overwrites your work)
./ex check G14     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void PrintInColumns(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PrintInColumns(3)` | prints:<br>`  10  20  30` |
| `PrintInColumns(1)` | prints:<br>`  10` |
| `PrintInColumns(12)` | prints:<br>`  10  20  30  40  50  60  70  80  90 100 110 120` |

## Edge cases to test

- n = 12: `100` takes 3 characters, so it gets 1 space.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`$"{x,4}"` writes x right-aligned in 4 characters: `10` becomes `  10` (2 spaces + 2 digits).

</details>

<details><summary>Hint 2</summary>

L10 with `Console.Write($"{i * 10,4}")` and no extra spaces.

</details>

<details><summary>Hint 3</summary>

One `Console.WriteLine()` after the loop.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print 1, 4, 9, …, n² in columns 5 wide.

## Solution

Only after a real try: [open the solution for G14](../../internal/solutions/G14_NumbersInColumns.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [G09 · Rows of numbers](G09-number-rows.md) · [Loops](../themes/loops.md) · Next: [G03 · Multiplication grid](G03-multiplication-grid.md)

</div>
