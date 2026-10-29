[Home](../README.md) › [Exercises](README.md) › [Loops: take digits apart](../themes/loops-digits.md) › D12

# D12 · Product of the digits

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: take digits apart](../themes/loops-digits.md) | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D04](D04-digit-sum.md) | Custom |

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

Only after a real try: [open the solution for D12](../solutions/D12_ProductOfDigits.cs). Your solution can be different and still correct!

---

Previous: [D11 · Largest digit](D11-largest-digit.md) · [All exercises](README.md) · Next: [D07 · Fix the bugs: digit sum](D07-fix-digit-sum.md)
