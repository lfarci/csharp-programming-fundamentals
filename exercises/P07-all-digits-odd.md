---
prev:
  text: "P04 · Has an even digit"
  link: /exercises/P04-has-an-even-digit
next:
  text: "P05 · First multiple"
  link: /exercises/P05-first-multiple
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Search and combine](../themes/loops.md#search-and-combine) › P07

# P07 · All digits odd

<ExerciseHeader />

<div class="gh-only">

**Loops › Search and combine** · exercise 3 of 9 in this group (75 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Flag/search](../cookbook/05-flag-search.md), [Digit extraction](../cookbook/06-digit-extraction.md) | [P04](P04-has-an-even-digit.md) |

</div>

## Goal

Give back `true` if every digit of n is odd (n > 0).

## Start and check

```bash
./ex start P07     # creates practice/P07_AllDigitsOdd.cs (never overwrites your work)
./ex check P07     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool AllDigitsOdd(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `AllDigitsOdd(1357)` | `true` |
| `AllDigitsOdd(1352)` | `false` |
| `AllDigitsOdd(7)` | `true` |
| `AllDigitsOdd(20)` | `false` |

## Edge cases to test

- One even digit anywhere: `false`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

The other way round: start with `bool allOdd = true;` (no even digit seen yet).

</details>

<details><summary>Hint 2</summary>

One even digit is enough to make it `false`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back `true` if every digit of n is smaller than 5.

## Solution

Only after a real try: [open the solution for P07](../solutions/P07_AllDigitsOdd.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [P04 · Has an even digit](P04-has-an-even-digit.md) · [Loops](../themes/loops.md) · Next: [P05 · First multiple](P05-first-multiple.md)

</div>
