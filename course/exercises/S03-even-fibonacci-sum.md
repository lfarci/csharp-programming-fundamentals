---
prev:
  text: "S05 · N-th Fibonacci"
  link: /exercises/S05-nth-fibonacci
next:
  text: "P03 · Has a multiple of 7"
  link: /exercises/P03-has-a-multiple-of-7
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Changing values](../themes/loops.md#changing-values) › S03

# S03 · Even Fibonacci sum

<ExerciseHeader />

<div class="gh-only">

**Loops › Changing values** · exercise 5 of 5 in this group (72 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Challenge | hard | write code | [State update](../cookbook/07-state-update.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [S02](S02-fibonacci.md), [A03](A03-sum-even-values.md) |

</div>

Source: prepares [Project Euler #2](https://projecteuler.net/problem=2).

## Goal

Add up the **even** Fibonacci numbers that are **not greater** than `limit`, and give back the sum.

## Start and check

```bash
./ex start S03     # creates practice/S03_EvenFibonacciSum.cs (never overwrites your work)
./ex check S03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long EvenFibonacciSum(long limit)`: input = limit, a long (big whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `EvenFibonacciSum(10)` | `10` |
| `EvenFibonacciSum(100)` | `44` |
| `EvenFibonacciSum(1)` | `0` |
| `EvenFibonacciSum(34)` | `44` |

## Edge cases to test

- The limit itself counts if it is an even Fibonacci number (limit 8 → 2 + 8 = 10).

## Rules

- `while` loop (you do not know how many terms).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Up to 100: 0 1 1 2 3 5 8 13 21 34 55 89 → even ones 0, 2, 8, 34 → 44.

</details>

<details><summary>Hint 2</summary>

Stop condition: `while (previous <= limit)`.

</details>

<details><summary>Hint 3</summary>

Inside: `if (previous % 2 == 0) sum += previous;` then slide like S02.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Solve [Project Euler #2](https://projecteuler.net/problem=2) (limit four million). Use `long`.

## Solution

Only after a real try: [open the solution for S03](../../internal/solutions/S03_EvenFibonacciSum.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [S05 · N-th Fibonacci](S05-nth-fibonacci.md) · [Loops](../themes/loops.md) · Next: [P03 · Has a multiple of 7](P03-has-a-multiple-of-7.md)

</div>
