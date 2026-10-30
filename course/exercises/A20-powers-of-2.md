---
prev:
  text: "A18 · Sum of cubes"
  link: /exercises/A18-sum-of-cubes
next:
  text: "A19 · Product from a to b"
  link: /exercises/A19-product-from-a-to-b
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A20

# A20 · Power of 2

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 7 of 12 in this group (20 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) |

</div>

## Goal

Give back 2 to the power n (n ≥ 0), by multiplying by 2, n times.

## Start and check

```bash
./ex start A20     # creates practice/A20_PowersOf2.cs (never overwrites your work)
./ex check A20     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long PowerOf2(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PowerOf2(3)` | `8` |
| `PowerOf2(0)` | `1` |
| `PowerOf2(10)` | `1024` |

## Edge cases to test

- n = 0: 1.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A product box starts at 1, not 0 (0 times anything is 0): `long result = 1;`.

</details>

<details><summary>Hint 2</summary>

The loop runs n times; each turn: `result *= 2`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back 3 to the power n.

## Solution

Only after a real try: [open the solution for A20](../../internal/solutions/A20_PowersOf2.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A18 · Sum of cubes](A18-sum-of-cubes.md) · [Loops](../themes/loops.md) · Next: [A19 · Product from a to b](A19-product-from-a-to-b.md)

</div>
