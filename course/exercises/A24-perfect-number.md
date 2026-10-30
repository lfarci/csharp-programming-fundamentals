---
prev:
  text: "A23 · FizzBuzz"
  link: /exercises/A23-fizzbuzz
next:
  text: "A08 · Multiples of 3 or 5"
  link: /exercises/A08-multiples-of-3-or-5
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops-keep-only-some.md) › A24

# A24 · Perfect number

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 10 of 11 in this group (35 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A22](A22-sum-of-divisors.md) |

</div>

## Goal

A number is **perfect** when it equals the sum of its divisors smaller than itself: 6 = 1 + 2 + 3. Give back `true` if n is perfect (n ≥ 1).

## Start and check

```bash
./ex start A24     # creates practice/A24_PerfectNumber.cs (never overwrites your work)
./ex check A24     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool IsPerfect(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IsPerfect(6)` | `true` |
| `IsPerfect(28)` | `true` |
| `IsPerfect(12)` | `false` |
| `IsPerfect(1)` | `false` |
| `IsPerfect(496)` | `true` |

## Edge cases to test

- n = 1: there is no divisor smaller than 1, the sum is 0, so `false`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

This is A22 (sum of the divisors) with one change: stop **before** n (`d < n`).

</details>

<details><summary>Hint 2</summary>

After the loop, compare: `return sum == n;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print every perfect number up to 10 000 (there are 4).

## Solution

Only after a real try: [open the solution for A24](../../internal/solutions/A24_PerfectNumber.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A23 · FizzBuzz](A23-fizzbuzz.md) · [Loops](../themes/loops.md) · Next: [A08 · Multiples of 3 or 5](A08-multiples-of-3-or-5.md)

</div>
