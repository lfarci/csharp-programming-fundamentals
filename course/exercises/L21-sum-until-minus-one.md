---
prev:
  text: "L20 · Echo until zero"
  link: /exercises/L20-echo-until-zero
next:
  text: "L05 · Until zero"
  link: /exercises/L05-until-zero
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops-until-the-user-stops.md) › L21

# L21 · Sum until -1

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 2 of 8 in this group (48 of 99 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L20](L20-echo-until-zero.md), [A01](A01-sum-1-to-n.md) |

</div>

## Goal

Read points (whole numbers, 0 or more) until the user types -1. Print their sum.

## Start and check

```bash
./ex start L21     # creates practice/L21_SumUntilMinusOne.cs (never overwrites your work)
./ex check L21     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `7`, `1`, `-1`

```text
Sum: 12
```

**Example 2** — input: `10`, `0`, `5`, `-1`

```text
Sum: 15
```

**Example 3** — input: `-1`

```text
Sum: 0
```

## Edge cases to test

- The first number is already -1: the sum is 0.
- 0 is a normal value here: only -1 stops.
- -1 is not added: 4, 7, 1 give 12, not 11.

## Rules

- Sentinel loop + one box (`sum`). The sentinel is -1, not 0.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

L20 with a box: `int sum = 0;` **before** the loop.

</details>

<details><summary>Hint 2</summary>

The sentinel test is `if (value == -1) break;`. Then, after it: `sum += value;`.

</details>

<details><summary>Hint 3</summary>

Print the sum once, **after** the loop.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also print how many points were 0.

## Solution

Only after a real try: [open the solution for L21](../../internal/solutions/L21_SumUntilMinusOne.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L20 · Echo until zero](L20-echo-until-zero.md) · [Loops](../themes/loops.md) · Next: [L05 · Until zero](L05-until-zero.md)

</div>
