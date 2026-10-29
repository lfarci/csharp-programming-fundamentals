[Home](../README.md) › [Exercises](README.md) › [Loops: take digits apart](../themes/loops-digits.md) › D09

# D09 · Count the even digits

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: take digits apart](../themes/loops-digits.md) | [Digit extraction](../cookbook/06-digit-extraction.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [D04](D04-digit-sum.md) | Custom |

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

Only after a real try: [open the solution for D09](../solutions/D09_CountEvenDigits.cs). Your solution can be different and still correct!

---

Previous: [D04 · Sum of the digits](D04-digit-sum.md) · [All exercises](README.md) · Next: [D10 · Count one digit](D10-count-a-digit.md)
