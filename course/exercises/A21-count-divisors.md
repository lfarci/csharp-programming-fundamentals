---
prev:
  text: "A16 · Count multiples of 5"
  link: /exercises/A16-count-multiples-of-5
next:
  text: "A22 · Sum of the divisors"
  link: /exercises/A22-sum-of-divisors
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops-keep-only-some.md) › A21

# A21 · Count the divisors

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 4 of 11 in this group (29 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A16](A16-count-multiples-of-5.md) |

</div>

## Goal

Give back how many numbers from 1 to n divide n exactly (n ≥ 1).

## Start and check

```bash
./ex start A21     # creates practice/A21_CountDivisors.cs (never overwrites your work)
./ex check A21     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountDivisors(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDivisors(6)` | `4` |
| `CountDivisors(7)` | `2` |
| `CountDivisors(1)` | `1` |
| `CountDivisors(12)` | `6` |

## Edge cases to test

- n = 1: 1 divisor.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Loop d from 1 to n.

</details>

<details><summary>Hint 2</summary>

`n % d == 0` means d divides n. Count it.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back how many divisors are even.

## Solution

Only after a real try: [open the solution for A21](../../internal/solutions/A21_CountDivisors.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A16 · Count multiples of 5](A16-count-multiples-of-5.md) · [Loops](../themes/loops.md) · Next: [A22 · Sum of the divisors](A22-sum-of-divisors.md)

</div>
