---
prev:
  text: "A02 · Count multiples of 3"
  link: /exercises/A02-count-multiples-of-3
next:
  text: "A16 · Count multiples of 5"
  link: /exercises/A16-count-multiples-of-5
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops.md#keep-only-some) › A15

# A15 · Count the even numbers

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 2 of 9 in this group (27 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md) |

</div>

## Goal

Give back how many numbers from 1 to n are even.

## Start and check

```bash
./ex start A15     # creates practice/A15_CountEvenNumbers.cs (never overwrites your work)
./ex check A15     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountEvens(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountEvens(10)` | `5` |
| `CountEvens(7)` | `3` |
| `CountEvens(1)` | `0` |

## Edge cases to test

- n = 1: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Like A02: only the test changes.

</details>

<details><summary>Hint 2</summary>

`if (i % 2 == 0) count++;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count the odd numbers from 1 to n.

## Solution

Only after a real try: [open the solution for A15](../../internal/solutions/A15_CountEvenNumbers.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A02 · Count multiples of 3](A02-count-multiples-of-3.md) · [Loops](../themes/loops.md) · Next: [A16 · Count multiples of 5](A16-count-multiples-of-5.md)

</div>
