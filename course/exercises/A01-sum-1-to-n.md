---
prev:
  text: "A11 · Arrange: sum of squares"
  link: /exercises/A11-arrange-sum-of-squares
next:
  text: "A13 · Sum from a to b"
  link: /exercises/A13-sum-from-a-to-b
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A01

# A01 · Sum from 1 to N

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 3 of 12 in this group (16 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Counter loop](../cookbook/01-counter-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L03](L03-count-up-and-down.md) |

</div>

## Goal

Give back the sum 1 + 2 + … + n.

## Start and check

```bash
./ex start A01     # creates practice/A01_Sum1ToN.cs (never overwrites your work)
./ex check A01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumTo(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumTo(5)` | `15` |
| `SumTo(1)` | `1` |
| `SumTo(10)` | `55` |
| `SumTo(0)` | `0` |

## Edge cases to test

- N = 0 → the loop runs 0 times → sum stays 0.

## Rules

- Use a loop. No formula `n * (n + 1) / 2` (you can use it to **check** your answer).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Fill the trace table for N = 4 first: `i`, `sum before`, `sum after`.

</details>

<details><summary>Hint 2</summary>

The box `sum` is created **before** the loop and starts at 0.

</details>

<details><summary>Hint 3</summary>

Inside the loop: `sum += i;`. `return sum;` **after** the loop.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Sum from A to B (read both). Then: sum of the squares 1² + 2² + … + N².

## Solution

Only after a real try: [open the solution for A01](../../internal/solutions/A01_Sum1ToN.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A11 · Arrange: sum of squares](A11-arrange-sum-of-squares.md) · [Loops](../themes/loops.md) · Next: [A13 · Sum from a to b](A13-sum-from-a-to-b.md)

</div>
