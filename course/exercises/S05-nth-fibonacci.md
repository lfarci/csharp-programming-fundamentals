---
prev:
  text: "S02 · Fibonacci"
  link: /exercises/S02-fibonacci
next:
  text: "S03 · Even Fibonacci sum"
  link: /exercises/S03-even-fibonacci-sum
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Changing values](../themes/loops-changing-values.md) › S05

# S05 · N-th Fibonacci

<ExerciseHeader />

<div class="gh-only">

**Loops › Changing values** · exercise 4 of 5 in this group (71 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [State update](../cookbook/07-state-update.md) | [S02](S02-fibonacci.md) |

</div>

## Goal

Give back the Fibonacci number at position n: position 0 is 0, position 1 is 1, then 1, 2, 3, 5, 8, …

## Start and check

```bash
./ex start S05     # creates practice/S05_NthFibonacci.cs (never overwrites your work)
./ex check S05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long Fibonacci(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Fibonacci(0)` | `0` |
| `Fibonacci(1)` | `1` |
| `Fibonacci(6)` | `8` |
| `Fibonacci(10)` | `55` |

## Edge cases to test

- n = 0: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

S02 without printing: do the same 3 moves n times.

</details>

<details><summary>Hint 2</summary>

After the loop, `previous` holds the answer.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the sum of the first n Fibonacci numbers.

## Solution

Only after a real try: [open the solution for S05](../../internal/solutions/S05_NthFibonacci.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [S02 · Fibonacci](S02-fibonacci.md) · [Loops](../themes/loops.md) · Next: [S03 · Even Fibonacci sum](S03-even-fibonacci-sum.md)

</div>
