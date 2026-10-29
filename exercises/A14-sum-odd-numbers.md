[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › A14

# A14 · Sum the odd numbers

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | 4b · Running result | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md), [L16](L16-odd-numbers.md) | Custom |

## Goal

Give back 1 + 3 + 5 + … (the odd numbers up to n).

## Start and check

```bash
./ex start A14     # creates practice/A14_SumOddNumbers.cs (never overwrites your work)
./ex check A14     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfOdds(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfOdds(5)` | `9` |
| `SumOfOdds(6)` | `9` |
| `SumOfOdds(1)` | `1` |
| `SumOfOdds(0)` | `0` |

## Edge cases to test

- n = 0: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Loop over 1, 3, 5, … with `i += 2` (like L16).

</details>

<details><summary>Hint 2</summary>

Add each one to `sum`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Do it again with `i++` and an `if (i % 2 != 0)`.

## Solution

Only after a real try: [open the solution for A14](../solutions/A14_SumOddNumbers.cs). Your solution can be different and still correct!

---

Previous: [A13 · Sum from a to b](A13-sum-from-a-to-b.md) · [All exercises](README.md) · Next: [A15 · Count the even numbers](A15-count-even-numbers.md)
