---
prev:
  text: "R04 · Find the position"
  link: /exercises/R04-find-the-position
next:
  text: "R05 · Reverse an array"
  link: /exercises/R05-reverse-an-array
---

[Home](../../README.md) › [Exercises](README.md) › [Arrays, text and lists](../themes/arrays.md) › [Arrays](../themes/arrays-arrays.md) › R08

# R08 · Is it sorted?

<ExerciseHeader />

<div class="gh-only">

**Arrays, text and lists › Arrays** · exercise 7 of 8 in this group (7 of 13 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Array traversal](../cookbook/11-array-traversal.md), [Flag/search](../cookbook/05-flag-search.md) | [R02](R02-largest-in-an-array.md), [P03](P03-has-a-multiple-of-7.md) |

</div>

## Goal

Give back `true` if every value is bigger than or equal to the one before it (smallest to largest).

## Start and check

```bash
./ex start R08     # creates practice/R08_IsItSorted.cs (never overwrites your work)
./ex check R08     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool IsSorted(int[] values)`: input = values, an int[] (array of whole numbers); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IsSorted(new int[] { 1, 2, 2, 5 })` | `true` |
| `IsSorted(new int[] { 3, 1, 2 })` | `false` |
| `IsSorted(new int[] { 1, 2, 4, 3 })` | `false` |
| `IsSorted(new int[] { 7 })` | `true` |
| `IsSorted(new int[0])` | `true` |

## Edge cases to test

- 0 or 1 value: nothing to compare, so `true`.
- Starting at `i = 0` reads `values[-1]` and crashes.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Compare each value with the one before: start at `i = 1` and look at `values[i - 1]`.

</details>

<details><summary>Hint 2</summary>

One pair in the wrong order is enough: `return false;` right away. After the loop: `return true;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also accept arrays sorted from largest to smallest.

## Solution

Only after a real try: [open the solution for R08](../../internal/solutions/R08_IsItSorted.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [R04 · Find the position](R04-find-the-position.md) · [Arrays, text and lists](../themes/arrays.md) · Next: [R05 · Reverse an array](R05-reverse-an-array.md)

</div>
