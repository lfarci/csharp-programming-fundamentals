---
prev:
  text: "A25 · Add the same number"
  link: /exercises/A25-add-the-same-number
next:
  text: "A34 · Sum of a times table"
  link: /exercises/A34-sum-of-a-times-table
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A26

# A26 · Sum of tens

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 5 of 14 in this group (18 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A25](A25-add-the-same-number.md) |

</div>

## Goal

Give back 10 + 20 + … + n × 10. `SumOfTens(3)` is 10 + 20 + 30 = 60.

## Start and check

```bash
./ex start A26     # creates practice/A26_SumOfTens.cs (never overwrites your work)
./ex check A26     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfTens(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfTens(3)` | `60` |
| `SumOfTens(1)` | `10` |
| `SumOfTens(0)` | `0` |
| `SumOfTens(5)` | `150` |

## Edge cases to test

- n = 0: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A01, but each turn adds `i * 10`.

</details>

<details><summary>Hint 2</summary>

Box before, add inside, return after.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back 5 + 10 + … + n × 5.

## Solution

Only after a real try: [open the solution for A26](../../internal/solutions/A26_SumOfTens.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A25 · Add the same number](A25-add-the-same-number.md) · [Loops](../themes/loops.md) · Next: [A34 · Sum of a times table](A34-sum-of-a-times-table.md)

</div>
