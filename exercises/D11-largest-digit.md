[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › D11

# D11 · Largest digit

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md), [Min/max](../cookbook/04-min-max.md) | [D04](D04-digit-sum.md), [C02](C02-largest-of-three.md) | Custom |

## Goal

Give back the largest digit of n (n > 0).

## Start and check

```bash
./ex start D11     # creates practice/D11_LargestDigit.cs (never overwrites your work)
./ex check D11     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int LargestDigit(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `LargestDigit(3829)` | `9` |
| `LargestDigit(111)` | `1` |
| `LargestDigit(5)` | `5` |
| `LargestDigit(2061)` | `6` |

## Edge cases to test

- One digit: itself.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

The D04 loop, with a max box instead of a sum.

</details>

<details><summary>Hint 2</summary>

A digit is never below 0, so `max = 0` is a safe start.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the smallest digit.

## Solution

Only after a real try: [open the solution for D11](../solutions/D11_LargestDigit.cs). Your solution can be different and still correct!

---

Previous: [D10 · Count one digit](D10-count-a-digit.md) · [All exercises](README.md) · Next: [D12 · Product of the digits](D12-product-of-digits.md)
