---
prev:
  text: "D03 · Count the digits"
  link: /exercises/D03-count-digits
next:
  text: "D04 · Sum of the digits"
  link: /exercises/D04-digit-sum
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops-digits.md) › D08

# D08 · First digit

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 4 of 13 in this group (61 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Digit extraction](../cookbook/06-digit-extraction.md) | [D03](D03-count-digits.md) |

</div>

## Goal

Give back the first (leftmost) digit of n (n ≥ 0).

## Start and check

```bash
./ex start D08     # creates practice/D08_FirstDigit.cs (never overwrites your work)
./ex check D08     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int FirstDigit(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `FirstDigit(352)` | `3` |
| `FirstDigit(7)` | `7` |
| `FirstDigit(1000)` | `1` |
| `FirstDigit(90)` | `9` |

## Edge cases to test

- One digit: n itself.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Remove the last digit (`/ 10`) again and again.

</details>

<details><summary>Hint 2</summary>

Stop when only one digit is left: `while (n >= 10)`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the second digit from the left.

## Solution

Only after a real try: [open the solution for D08](../../internal/solutions/D08_FirstDigit.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D03 · Count the digits](D03-count-digits.md) · [Loops](../themes/loops.md) · Next: [D04 · Sum of the digits](D04-digit-sum.md)

</div>
