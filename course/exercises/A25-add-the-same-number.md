---
prev:
  text: "A01 · Sum from 1 to N"
  link: /exercises/A01-sum-1-to-n
next:
  text: "A26 · Sum of tens"
  link: /exercises/A26-sum-of-tens
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A25

# A25 · Add the same number

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 4 of 14 in this group (17 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) |

</div>

## Goal

Give back `value` + `value` + … (`times` times), with a loop. `AddRepeated(4, 3)` is 4 + 4 + 4 = 12.

## Start and check

```bash
./ex start A25     # creates practice/A25_AddTheSameNumber.cs (never overwrites your work)
./ex check A25     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int AddRepeated(int value, int times)`: input = value, an int (whole number), times, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `AddRepeated(4, 3)` | `12` |
| `AddRepeated(7, 1)` | `7` |
| `AddRepeated(5, 0)` | `0` |
| `AddRepeated(2, 10)` | `20` |

## Edge cases to test

- `times` = 0: 0 (nothing was added).

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A01, but each turn adds `value`, not `i`.

</details>

<details><summary>Hint 2</summary>

The loop only counts the turns: `for (int i = 1; i <= times; i++)`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Start the total at `start` instead of 0, then add `value`, `times` times.

## Solution

Only after a real try: [open the solution for A25](../../internal/solutions/A25_AddTheSameNumber.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A01 · Sum from 1 to N](A01-sum-1-to-n.md) · [Loops](../themes/loops.md) · Next: [A26 · Sum of tens](A26-sum-of-tens.md)

</div>
