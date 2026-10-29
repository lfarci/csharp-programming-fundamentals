---
prev:
  text: "P05 · First multiple"
  link: /exercises/P05-first-multiple
next:
  text: "P01 · Is it prime?"
  link: /exercises/P01-is-it-prime
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Search and combine](../themes/loops-search-and-combine.md) › P06

# P06 · Smallest divisor

<ExerciseHeader />

<div class="gh-only">

**Loops › Search and combine** · exercise 5 of 9 in this group (77 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Flag/search](../cookbook/05-flag-search.md) | [P05](P05-first-multiple.md), [A21](A21-count-divisors.md) |

</div>

## Goal

Give back the smallest number bigger than 1 that divides n exactly (n ≥ 2).

## Start and check

```bash
./ex start P06     # creates practice/P06_SmallestDivisor.cs (never overwrites your work)
./ex check P06     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SmallestDivisor(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SmallestDivisor(15)` | `3` |
| `SmallestDivisor(7)` | `7` |
| `SmallestDivisor(2)` | `2` |
| `SmallestDivisor(49)` | `7` |

## Edge cases to test

- n is prime: the answer is n.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

P05 with `d` from 2 and the test `n % d == 0`.

</details>

<details><summary>Hint 2</summary>

If no `d` below n works, the answer is n itself: start the box at n.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the largest divisor of n that is smaller than n.

## Solution

Only after a real try: [open the solution for P06](../../internal/solutions/P06_SmallestDivisor.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [P05 · First multiple](P05-first-multiple.md) · [Loops](../themes/loops.md) · Next: [P01 · Is it prime?](P01-is-it-prime.md)

</div>
