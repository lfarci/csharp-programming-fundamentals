---
prev:
  text: "A15 · Count the even numbers"
  link: /exercises/A15-count-even-numbers
next:
  text: "A21 · Count the divisors"
  link: /exercises/A21-count-divisors
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops.md#keep-only-some) › A16

# A16 · Count multiples of 5

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 3 of 9 in this group (28 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A15](A15-count-even-numbers.md) |

</div>

## Goal

Give back how many numbers from 1 to n are divisible by 5.

## Start and check

```bash
./ex start A16     # creates practice/A16_CountMultiplesOf5.cs (never overwrites your work)
./ex check A16     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountMultiplesOf5(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountMultiplesOf5(20)` | `4` |
| `CountMultiplesOf5(4)` | `0` |
| `CountMultiplesOf5(26)` | `5` |

## Edge cases to test

- n below 5: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A02 with 5 instead of 3.

</details>

<details><summary>Hint 2</summary>

`i % 5 == 0` means: divisible by 5.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count the multiples of 7 from 1 to n.

## Solution

Only after a real try: [open the solution for A16](../../internal/solutions/A16_CountMultiplesOf5.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A15 · Count the even numbers](A15-count-even-numbers.md) · [Loops](../themes/loops.md) · Next: [A21 · Count the divisors](A21-count-divisors.md)

</div>
