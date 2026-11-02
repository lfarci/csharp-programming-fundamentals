---
prev:
  text: "A29 · First n odd numbers"
  link: /exercises/A29-first-n-odd-numbers
next:
  text: "A18 · Sum of cubes"
  link: /exercises/A18-sum-of-cubes
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A27

# A27 · Sum by any step

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 10 of 14 in this group (23 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A13](A13-sum-from-a-to-b.md), [L15](L15-count-by-step.md) |

</div>

## Goal

Give back a + (a + step) + (a + 2 × step) + … while the number is at most b (step ≥ 1). `SumByStep(1, 10, 3)` is 1 + 4 + 7 + 10 = 22.

## Start and check

```bash
./ex start A27     # creates practice/A27_SumByAnyStep.cs (never overwrites your work)
./ex check A27     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumByStep(int a, int b, int step)`: input = a, an int (whole number), b, an int (whole number), step, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumByStep(1, 10, 3)` | `22` |
| `SumByStep(2, 10, 4)` | `18` |
| `SumByStep(5, 5, 2)` | `5` |
| `SumByStep(6, 5, 1)` | `0` |

## Edge cases to test

- `a` bigger than `b`: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A13 with the step of L15: `i += step`.

</details>

<details><summary>Hint 2</summary>

The test stays `i <= b`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count the numbers instead of adding them.

## Solution

Only after a real try: [open the solution for A27](../../internal/solutions/A27_SumByAnyStep.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A29 · First n odd numbers](A29-first-n-odd-numbers.md) · [Loops](../themes/loops.md) · Next: [A18 · Sum of cubes](A18-sum-of-cubes.md)

</div>
