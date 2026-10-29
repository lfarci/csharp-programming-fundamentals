---
prev:
  text: "L15 · Count by any step"
  link: /exercises/L15-count-by-step
next:
  text: "L19 · Count the turns"
  link: /exercises/L19-count-the-turns
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Count](../themes/loops.md#count) › L04

# L04 · Multiplication table

<ExerciseHeader />

<div class="gh-only">

**Loops › Count** · exercise 13 of 13 in this group (13 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | easy | write code | [Counter loop](../cookbook/01-counter-loop.md) | [L03](L03-count-up-and-down.md) |

</div>

## Goal

Read a number N and print its multiplication table from 1 to 10.

## Start and check

```bash
./ex start L04     # creates practice/L04_MultiplicationTable.cs (never overwrites your work)
./ex check L04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`

```text
3 x 1 = 3
3 x 2 = 6
3 x 10 = 30
```

**Example 2** — input: `7`

```text
7 x 7 = 49
```

## Edge cases to test

- N = 0 → all results are 0.

## Rules

- One `for` loop.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

What changes from line to line? Only the second number (1 to 10).

</details>

<details><summary>Hint 2</summary>

`Console.WriteLine($"{n} x {i} = {n * i}");`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Read a second number M and print the table up to M instead of 10.

## Solution

Only after a real try: [open the solution for L04](../solutions/L04_MultiplicationTable.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L15 · Count by any step](L15-count-by-step.md) · [Loops](../themes/loops.md) · Next: [L19 · Count the turns](L19-count-the-turns.md)

</div>
