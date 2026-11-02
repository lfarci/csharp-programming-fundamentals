---
prev:
  text: "A14 · Sum the odd numbers"
  link: /exercises/A14-sum-odd-numbers
next:
  text: "A27 · Sum by any step"
  link: /exercises/A27-sum-by-any-step
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A29

# A29 · First n odd numbers

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 9 of 14 in this group (22 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A14](A14-sum-odd-numbers.md) |

</div>

## Goal

Give back the sum of the **first n** odd numbers: 1 + 3 + 5 + … (n numbers). `SumFirstOdds(3)` is 1 + 3 + 5 = 9.

## Start and check

```bash
./ex start A29     # creates practice/A29_FirstNOddNumbers.cs (never overwrites your work)
./ex check A29     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumFirstOdds(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumFirstOdds(3)` | `9` |
| `SumFirstOdds(1)` | `1` |
| `SumFirstOdds(0)` | `0` |
| `SumFirstOdds(5)` | `25` |

## Edge cases to test

- n = 0: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Not like A14: here n is **how many** numbers, so the loop runs n times.

</details>

<details><summary>Hint 2</summary>

Turn i adds the i-th odd number: `2 * i - 1` (1, 3, 5, …).

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the sum of the first n even numbers: 2 + 4 + 6 + …

## Solution

Only after a real try: [open the solution for A29](../../internal/solutions/A29_FirstNOddNumbers.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A14 · Sum the odd numbers](A14-sum-odd-numbers.md) · [Loops](../themes/loops.md) · Next: [A27 · Sum by any step](A27-sum-by-any-step.md)

</div>
