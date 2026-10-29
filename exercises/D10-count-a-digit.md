---
prev:
  text: "D09 · Count the even digits"
  link: /exercises/D09-count-even-digits
next:
  text: "D12 · Product of the digits"
  link: /exercises/D12-product-of-digits
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops.md#digits) › D10

# D10 · Count one digit

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 7 of 12 in this group (62 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Digit extraction](../cookbook/06-digit-extraction.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [D09](D09-count-even-digits.md) |

</div>

## Goal

Give back how many times `digit` appears in n (n > 0).

## Start and check

```bash
./ex start D10     # creates practice/D10_CountADigit.cs (never overwrites your work)
./ex check D10     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountDigit(int n, int digit)`: input = n, an int (whole number), digit, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDigit(1717, 7)` | `2` |
| `CountDigit(123, 9)` | `0` |
| `CountDigit(555, 5)` | `3` |

## Edge cases to test

- The digit is not there: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

D09 with the test `n % 10 == digit`.

</details>

<details><summary>Hint 2</summary>

Do not forget `n /= 10`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back `true` if the digit appears at least once.

## Solution

Only after a real try: [open the solution for D10](../solutions/D10_CountADigit.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D09 · Count the even digits](D09-count-even-digits.md) · [Loops](../themes/loops.md) · Next: [D12 · Product of the digits](D12-product-of-digits.md)

</div>
