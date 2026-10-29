---
prev:
  text: "D08 · First digit"
  link: /exercises/D08-first-digit
next:
  text: "D09 · Count the even digits"
  link: /exercises/D09-count-even-digits
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops.md#digits) › D04

# D04 · Sum of the digits

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 5 of 12 in this group (60 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | medium | write code | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D03](D03-count-digits.md) |

</div>

## Goal

Give back the sum of the digits of n (n ≥ 0).

## Start and check

```bash
./ex start D04     # creates practice/D04_DigitSum.cs (never overwrites your work)
./ex check D04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int DigitSum(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DigitSum(352)` | `10` |
| `DigitSum(0)` | `0` |
| `DigitSum(9999)` | `36` |
| `DigitSum(7)` | `7` |

## Edge cases to test

- 0 → 0.

## Rules

- A loop with `% 10` and `/ 10`. No string.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Fill the trace table: `remaining`, `digit`, `sum`.

</details>

<details><summary>Hint 2</summary>

Three lines in the loop: take the digit, add it, remove it.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Repeat the digit sum until one digit is left (9875 → 29 → 11 → 2).

## Solution

Only after a real try: [open the solution for D04](../solutions/D04_DigitSum.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D08 · First digit](D08-first-digit.md) · [Loops](../themes/loops.md) · Next: [D09 · Count the even digits](D09-count-even-digits.md)

</div>
