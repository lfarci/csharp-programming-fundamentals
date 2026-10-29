---
prev:
  text: "D04 · Sum of the digits"
  link: /exercises/D04-digit-sum
next:
  text: "D10 · Count one digit"
  link: /exercises/D10-count-a-digit
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops.md#digits) › D09

# D09 · Count the even digits

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 6 of 12 in this group (61 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Digit extraction](../cookbook/06-digit-extraction.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [D04](D04-digit-sum.md) |

</div>

## Goal

Give back how many digits of n are even (n > 0).

## Start and check

```bash
./ex start D09     # creates practice/D09_CountEvenDigits.cs (never overwrites your work)
./ex check D09     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountEvenDigits(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountEvenDigits(2468)` | `4` |
| `CountEvenDigits(135)` | `0` |
| `CountEvenDigits(1234)` | `2` |

## Edge cases to test

- No even digit: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

The D04 loop: take the last digit with `int digit = n % 10;`, then remove it with `n /= 10;`.

</details>

<details><summary>Hint 2</summary>

Between the two, count it only if `digit % 2 == 0`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count the odd digits.

## Solution

Only after a real try: [open the solution for D09](../../internal/solutions/D09_CountEvenDigits.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D04 · Sum of the digits](D04-digit-sum.md) · [Loops](../themes/loops.md) · Next: [D10 · Count one digit](D10-count-a-digit.md)

</div>
