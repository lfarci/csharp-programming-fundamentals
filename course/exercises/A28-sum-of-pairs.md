---
prev:
  text: "A18 · Sum of cubes"
  link: /exercises/A18-sum-of-cubes
next:
  text: "A05 · Sum and sum of squares"
  link: /exercises/A05-sum-square-difference
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A28

# A28 · Sum of i × (i + 1)

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 12 of 14 in this group (25 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A18](A18-sum-of-cubes.md) |

</div>

## Goal

Give back 1 × 2 + 2 × 3 + … + n × (n + 1). `SumOfPairs(3)` is 2 + 6 + 12 = 20.

## Start and check

```bash
./ex start A28     # creates practice/A28_SumOfPairs.cs (never overwrites your work)
./ex check A28     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfPairs(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfPairs(3)` | `20` |
| `SumOfPairs(1)` | `2` |
| `SumOfPairs(0)` | `0` |
| `SumOfPairs(4)` | `40` |

## Edge cases to test

- n = 0: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A18 with `i * (i + 1)` instead of `i * i * i`.

</details>

<details><summary>Hint 2</summary>

Keep the brackets: `i * i + 1` is not the same.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back 1 × 3 + 2 × 4 + … + n × (n + 2).

## Solution

Only after a real try: [open the solution for A28](../../internal/solutions/A28_SumOfPairs.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A18 · Sum of cubes](A18-sum-of-cubes.md) · [Loops](../themes/loops.md) · Next: [A05 · Sum and sum of squares](A05-sum-square-difference.md)

</div>
