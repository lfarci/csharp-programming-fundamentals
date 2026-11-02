---
prev:
  text: "A30 · Power of 10"
  link: /exercises/A30-power-of-10
next:
  text: "A19 · Product from a to b"
  link: /exercises/A19-product-from-a-to-b
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Multiply](../themes/loops-multiply.md) › A31

# A31 · Double k times

<ExerciseHeader />

<div class="gh-only">

**Loops › Multiply** · exercise 3 of 8 in this group (30 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A20](A20-powers-of-2.md) |

</div>

## Goal

Start with `start` and double it `times` times. `DoubleTimes(5, 3)`: 5, 10, 20, 40, so 40.

## Start and check

```bash
./ex start A31     # creates practice/A31_DoubleKTimes.cs (never overwrites your work)
./ex check A31     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long DoubleTimes(int start, int times)`: input = start, an int (whole number), times, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DoubleTimes(5, 3)` | `40` |
| `DoubleTimes(7, 0)` | `7` |
| `DoubleTimes(1, 10)` | `1024` |
| `DoubleTimes(3, 1)` | `6` |

## Edge cases to test

- `times` = 0: `start` (nothing changed).

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A20, but the box starts at `start`, not at 1.

</details>

<details><summary>Hint 2</summary>

`result *= 2;` inside the loop.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Triple the value `times` times instead.

## Solution

Only after a real try: [open the solution for A31](../../internal/solutions/A31_DoubleKTimes.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A30 · Power of 10](A30-power-of-10.md) · [Loops](../themes/loops.md) · Next: [A19 · Product from a to b](A19-product-from-a-to-b.md)

</div>
