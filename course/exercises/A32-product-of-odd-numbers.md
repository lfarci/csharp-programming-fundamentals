---
prev:
  text: "A19 · Product from a to b"
  link: /exercises/A19-product-from-a-to-b
next:
  text: "A33 · Product of squares"
  link: /exercises/A33-product-of-squares
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Multiply](../themes/loops-multiply.md) › A32

# A32 · Product of odd numbers

<ExerciseHeader />

<div class="gh-only">

**Loops › Multiply** · exercise 5 of 8 in this group (32 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A19](A19-product-from-a-to-b.md), [A14](A14-sum-odd-numbers.md) |

</div>

## Goal

Give back 1 × 3 × 5 × … with every odd number up to n (included). If there is none, give back 1.

## Start and check

```bash
./ex start A32     # creates practice/A32_ProductOfOddNumbers.cs (never overwrites your work)
./ex check A32     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long ProductOfOdds(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `ProductOfOdds(5)` | `15` |
| `ProductOfOdds(6)` | `15` |
| `ProductOfOdds(1)` | `1` |
| `ProductOfOdds(0)` | `1` |

## Edge cases to test

- n = 0: 1 (nothing was multiplied).

`./ex check` tests these too: `ProductOfOdds(25)` gives `7905853580625`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A14 with a product: the box starts at 1 and does `product *= i;`.

</details>

<details><summary>Hint 2</summary>

Loop over 1, 3, 5, … with `i += 2`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Multiply the even numbers 2 × 4 × … up to n.

## Solution

Only after a real try: [open the solution for A32](../../internal/solutions/A32_ProductOfOddNumbers.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A19 · Product from a to b](A19-product-from-a-to-b.md) · [Loops](../themes/loops.md) · Next: [A33 · Product of squares](A33-product-of-squares.md)

</div>
