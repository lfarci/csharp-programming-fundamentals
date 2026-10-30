---
prev:
  text: "D10 · Count one digit"
  link: /exercises/D10-count-a-digit
next:
  text: "D11 · Largest digit"
  link: /exercises/D11-largest-digit
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops-digits.md) › D12

# D12 · Product of the digits

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 8 of 13 in this group (65 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D04](D04-digit-sum.md) |

</div>

## Goal

Give back the product of the digits of n (n > 0): 234 → 2 × 3 × 4 = 24.

## Start and check

```bash
./ex start D12     # creates practice/D12_ProductOfDigits.cs (never overwrites your work)
./ex check D12     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int ProductOfDigits(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `ProductOfDigits(234)` | `24` |
| `ProductOfDigits(5)` | `5` |
| `ProductOfDigits(105)` | `0` |
| `ProductOfDigits(1111)` | `1` |

## Edge cases to test

- A 0 digit makes the product 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

D04 with a product box: start at 1.

</details>

<details><summary>Hint 2</summary>

`product *= n % 10;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the sum of the digits squared.

## Solution

Only after a real try: [open the solution for D12](../../internal/solutions/D12_ProductOfDigits.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D10 · Count one digit](D10-count-a-digit.md) · [Loops](../themes/loops.md) · Next: [D11 · Largest digit](D11-largest-digit.md)

</div>
