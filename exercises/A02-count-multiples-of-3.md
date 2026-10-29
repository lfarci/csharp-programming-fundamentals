---
prev:
  text: "A10 · Sum of a series"
  link: /exercises/A10-sum-of-a-series
next:
  text: "A15 · Count the even numbers"
  link: /exercises/A15-count-even-numbers
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops.md#keep-only-some) › A02

# A02 · Count multiples of 3

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 1 of 9 in this group (26 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A01](A01-sum-1-to-n.md), [C01](C01-even-or-odd.md) |

</div>

## Goal

Count how many numbers from 1 to n (included) are divisible by 3.

## Start and check

```bash
./ex start A02     # creates practice/A02_CountMultiplesOf3.cs (never overwrites your work)
./ex check A02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountMultiplesOf3(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountMultiplesOf3(10)` | `3` |
| `CountMultiplesOf3(2)` | `0` |
| `CountMultiplesOf3(9)` | `3` |
| `CountMultiplesOf3(0)` | `0` |

## Edge cases to test

- N smaller than 3 → 0.
- N itself divisible by 3 → counted.

## Rules

- Loop + `if` + counter. No division trick (`n / 3`) except to check.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Divisible by 3: `i % 3 == 0`.

</details>

<details><summary>Hint 2</summary>

Box: `count = 0`, `count++` only when the `if` is true.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count the numbers from 1 to N that are divisible by 3 **but not** by 2.

## Solution

Only after a real try: [open the solution for A02](../solutions/A02_CountMultiplesOf3.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A10 · Sum of a series](A10-sum-of-a-series.md) · [Loops](../themes/loops.md) · Next: [A15 · Count the even numbers](A15-count-even-numbers.md)

</div>
