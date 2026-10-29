---
prev:
  text: "P03 · Has a multiple of 7"
  link: /exercises/P03-has-a-multiple-of-7
next:
  text: "P07 · All digits odd"
  link: /exercises/P07-all-digits-odd
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Search and combine](../themes/loops.md#search-and-combine) › P04

# P04 · Has an even digit

<ExerciseHeader />

<div class="gh-only">

**Loops › Search and combine** · exercise 2 of 9 in this group (74 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Flag/search](../cookbook/05-flag-search.md), [Digit extraction](../cookbook/06-digit-extraction.md) | [P03](P03-has-a-multiple-of-7.md), [D09](D09-count-even-digits.md) |

</div>

## Goal

Give back `true` if at least one digit of n is even (n > 0).

## Start and check

```bash
./ex start P04     # creates practice/P04_HasAnEvenDigit.cs (never overwrites your work)
./ex check P04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool HasEvenDigit(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `HasEvenDigit(135)` | `false` |
| `HasEvenDigit(1352)` | `true` |
| `HasEvenDigit(8)` | `true` |
| `HasEvenDigit(7)` | `false` |

## Edge cases to test

- One digit: look at that digit only.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

P03 with the digit loop of D09: `while (n > 0)`, the digit is `n % 10`, then `n /= 10;`.

</details>

<details><summary>Hint 2</summary>

`found = true;` when the digit is even.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back `true` if n has the digit 7.

## Solution

Only after a real try: [open the solution for P04](../solutions/P04_HasAnEvenDigit.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [P03 · Has a multiple of 7](P03-has-a-multiple-of-7.md) · [Loops](../themes/loops.md) · Next: [P07 · All digits odd](P07-all-digits-odd.md)

</div>
