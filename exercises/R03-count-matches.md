---
prev:
  text: "R01 · Sum of an array"
  link: /exercises/R01-sum-an-array
next:
  text: "R02 · Position of the largest"
  link: /exercises/R02-largest-in-an-array
---

[Home](../README.md) › [Exercises](README.md) › [Arrays, text and lists](../themes/arrays.md) › [Arrays](../themes/arrays.md#arrays) › R03

# R03 · Count matches

<ExerciseHeader />

<div class="gh-only">

**Arrays, text and lists › Arrays** · exercise 2 of 6 in this group (2 of 11 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | easy | write code | [Array traversal](../cookbook/11-array-traversal.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [R01](R01-sum-an-array.md), [A02](A02-count-multiples-of-3.md) |

</div>

## Goal

Give back how many times `target` appears in the array.

## Start and check

```bash
./ex start R03     # creates practice/R03_CountMatches.cs (never overwrites your work)
./ex check R03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountMatches(int[] values, int target)`: input = values, an int[] (array of whole numbers), target, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountMatches(new int[] { 2, 4, 2, 5, 2 }, 2)` | `3` |
| `CountMatches(new int[] { 1, 1 }, 9)` | `0` |
| `CountMatches(new int[0], 3)` | `0` |

## Edge cases to test

- Target not present → 0.

## Rules

- No LINQ (`.Count()`).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

The array is already filled for you: it is the parameter `values`. Which recipe counts only *some* values?

</details>

<details><summary>Hint 2</summary>

Conditional accumulator: `if (value == target) count++;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count the values **greater** than the target.

## Solution

Only after a real try: [open the solution for R03](../solutions/R03_CountMatches.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [R01 · Sum of an array](R01-sum-an-array.md) · [Arrays, text and lists](../themes/arrays.md) · Next: [R02 · Position of the largest](R02-largest-in-an-array.md)

</div>
