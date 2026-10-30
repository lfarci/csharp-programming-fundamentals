---
prev:
  text: "S02 · Fibonacci"
  link: /exercises/S02-fibonacci
next:
  text: "S05 · N-th Fibonacci"
  link: /exercises/S05-nth-fibonacci
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Changing values](../themes/loops-changing-values.md) › S06

# S06 · Collatz steps

<ExerciseHeader />

<div class="gh-only">

**Loops › Changing values** · exercise 4 of 7 in this group (74 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [State update](../cookbook/07-state-update.md) | [S04](S04-doubling.md), [C01](C01-even-or-odd.md) |

</div>

## Goal

Start from n (n ≥ 1). If it is even, halve it; if it is odd, change it to 3 × n + 1. Repeat until you reach 1, and give back how many steps it took. 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 is 8 steps.

## Start and check

```bash
./ex start S06     # creates practice/S06_CollatzSteps.cs (never overwrites your work)
./ex check S06     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CollatzSteps(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CollatzSteps(1)` | `0` |
| `CollatzSteps(2)` | `1` |
| `CollatzSteps(6)` | `8` |
| `CollatzSteps(7)` | `16` |
| `CollatzSteps(27)` | `111` |

## Edge cases to test

- n = 1: already 1, so 0 steps (the loop never runs).

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

You do not know how many turns: use `while (n != 1)`.

</details>

<details><summary>Hint 2</summary>

Inside: change `n` (half or 3n + 1), then `steps++`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Find the number below 100 that takes the most steps.

## Solution

Only after a real try: [open the solution for S06](../../internal/solutions/S06_CollatzSteps.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [S02 · Fibonacci](S02-fibonacci.md) · [Loops](../themes/loops.md) · Next: [S05 · N-th Fibonacci](S05-nth-fibonacci.md)

</div>
