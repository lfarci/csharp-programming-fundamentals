---
prev:
  text: "P07 · All digits odd"
  link: /exercises/P07-all-digits-odd
next:
  text: "P06 · Smallest divisor"
  link: /exercises/P06-smallest-divisor
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Search and combine](../themes/loops.md#search-and-combine) › P05

# P05 · First multiple

<ExerciseHeader />

<div class="gh-only">

**Loops › Search and combine** · exercise 4 of 9 in this group (76 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Flag/search](../cookbook/05-flag-search.md) | [P03](P03-has-a-multiple-of-7.md) |

</div>

## Goal

Give back the first number from `a` to `b` that is divisible by `k` (k ≥ 1), or -1 if there is none.

## Start and check

```bash
./ex start P05     # creates practice/P05_FirstMultiple.cs (never overwrites your work)
./ex check P05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int FirstMultiple(int a, int b, int k)`: input = a, an int (whole number), b, an int (whole number), k, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `FirstMultiple(10, 20, 7)` | `14` |
| `FirstMultiple(1, 5, 6)` | `-1` |
| `FirstMultiple(6, 9, 3)` | `6` |
| `FirstMultiple(1, 30, 10)` | `10` |

## Edge cases to test

- None found: -1.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

The box starts at -1: it means not found.

</details>

<details><summary>Hint 2</summary>

When you find one, keep it and stop the loop with `break;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the **last** number from `a` to `b` divisible by `k` (loop backwards).

## Solution

Only after a real try: [open the solution for P05](../solutions/P05_FirstMultiple.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [P07 · All digits odd](P07-all-digits-odd.md) · [Loops](../themes/loops.md) · Next: [P06 · Smallest divisor](P06-smallest-divisor.md)

</div>
