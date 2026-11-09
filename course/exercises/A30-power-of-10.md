---
prev:
  text: "A20 · Power of 2"
  link: /exercises/A20-powers-of-2
next:
  text: "A31 · Double k times"
  link: /exercises/A31-double-k-times
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Multiply](../themes/loops-multiply.md) › A30

# A30 · Power of 10

<ExerciseHeader />

<div class="gh-only">

**Loops › Multiply** · exercise 2 of 8 in this group (29 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A20](A20-powers-of-2.md) |

</div>

## Goal

Give back 10 to the power n (0 ≤ n ≤ 18), by multiplying by 10, n times.

## Start and check

```bash
./ex start A30     # creates practice/A30_PowerOf10.cs (never overwrites your work)
./ex check A30     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long PowerOf10(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PowerOf10(3)` | `1000` |
| `PowerOf10(0)` | `1` |
| `PowerOf10(1)` | `10` |
| `PowerOf10(9)` | `1000000000` |

## Edge cases to test

- n = 0: 1.

`./ex check` tests these too: `PowerOf10(12)` gives `1000000000000`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A20 with 10 instead of 2.

</details>

<details><summary>Hint 2</summary>

The product box starts at 1: `long result = 1;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back 5 to the power n.

## Solution

Only after a real try: [open the solution for A30](../../internal/solutions/A30_PowerOf10.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A20 · Power of 2](A20-powers-of-2.md) · [Loops](../themes/loops.md) · Next: [A31 · Double k times](A31-double-k-times.md)

</div>
