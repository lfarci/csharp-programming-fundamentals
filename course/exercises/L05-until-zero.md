---
prev:
  text: "L21 · Sum until -1"
  link: /exercises/L21-sum-until-minus-one
next:
  text: "L22 · Words until stop"
  link: /exercises/L22-words-until-stop
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops-until-the-user-stops.md) › L05

# L05 · Until zero

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 3 of 8 in this group (49 of 99 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L20](L20-echo-until-zero.md) |

</div>

## Goal

Read whole numbers one by one. Stop when the user types 0. Print how many **non-zero** numbers were entered.

## Start and check

```bash
./ex start L05     # creates practice/L05_UntilZero.cs (never overwrites your work)
./ex check L05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`, `-2`, `8`, `0`

```text
You entered 3 numbers.
```

**Example 2** — input: `0`

```text
You entered 0 numbers.
```

## Edge cases to test

- The first number is already 0.
- Negative numbers count too.

## Rules

- You do not know how many numbers will come: no `for`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

This is the [sentinel loop](../cookbook/10-sentinel-loop.md). 0 is the sentinel.

</details>

<details><summary>Hint 2</summary>

`while (true) { read; if (value == 0) break; count++; }`

</details>

<details><summary>Hint 3</summary>

Do not count the 0 itself.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also print how many of the numbers were negative.

## Solution

Only after a real try: [open the solution for L05](../../internal/solutions/L05_UntilZero.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L21 · Sum until -1](L21-sum-until-minus-one.md) · [Loops](../themes/loops.md) · Next: [L22 · Words until stop](L22-words-until-stop.md)

</div>
