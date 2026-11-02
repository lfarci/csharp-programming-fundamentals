---
prev:
  text: "A32 · Product of odd numbers"
  link: /exercises/A32-product-of-odd-numbers
next:
  text: "A04 · Factorial"
  link: /exercises/A04-factorial
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Multiply](../themes/loops-multiply.md) › A33

# A33 · Product of squares

<ExerciseHeader />

<div class="gh-only">

**Loops › Multiply** · exercise 6 of 8 in this group (33 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A19](A19-product-from-a-to-b.md) |

</div>

## Goal

Give back 1² × 2² × … × n² (0 ≤ n ≤ 10). `ProductOfSquares(3)` is 1 × 4 × 9 = 36.

## Start and check

```bash
./ex start A33     # creates practice/A33_ProductOfSquares.cs (never overwrites your work)
./ex check A33     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long ProductOfSquares(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `ProductOfSquares(3)` | `36` |
| `ProductOfSquares(1)` | `1` |
| `ProductOfSquares(0)` | `1` |
| `ProductOfSquares(4)` | `576` |

## Edge cases to test

- n = 0: 1.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A19 from 1 to n, multiplying by `i * i`.

</details>

<details><summary>Hint 2</summary>

The product box starts at 1.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back 1³ × 2³ × … × n³ (n ≤ 6).

## Solution

Only after a real try: [open the solution for A33](../../internal/solutions/A33_ProductOfSquares.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A32 · Product of odd numbers](A32-product-of-odd-numbers.md) · [Loops](../themes/loops.md) · Next: [A04 · Factorial](A04-factorial.md)

</div>
