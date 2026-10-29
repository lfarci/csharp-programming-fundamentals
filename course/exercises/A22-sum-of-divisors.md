---
prev:
  text: "A21 · Count the divisors"
  link: /exercises/A21-count-divisors
next:
  text: "A12 · Fix: multiples of 7"
  link: /exercises/A12-fix-count-multiples-of-7
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops-keep-only-some.md) › A22

# A22 · Sum of the divisors

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 5 of 9 in this group (30 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A21](A21-count-divisors.md) |

</div>

## Goal

Give back the sum of all numbers from 1 to n that divide n exactly (n ≥ 1).

## Start and check

```bash
./ex start A22     # creates practice/A22_SumOfDivisors.cs (never overwrites your work)
./ex check A22     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfDivisors(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfDivisors(6)` | `12` |
| `SumOfDivisors(7)` | `8` |
| `SumOfDivisors(1)` | `1` |

## Edge cases to test

- n = 1: 1.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A21 with `sum += d` instead of `count++`.

</details>

<details><summary>Hint 2</summary>

`sum = 0` before the loop.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Sum the divisors below n only (6 → 1 + 2 + 3 = 6).

## Solution

Only after a real try: [open the solution for A22](../../internal/solutions/A22_SumOfDivisors.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A21 · Count the divisors](A21-count-divisors.md) · [Loops](../themes/loops.md) · Next: [A12 · Fix: multiples of 7](A12-fix-count-multiples-of-7.md)

</div>
