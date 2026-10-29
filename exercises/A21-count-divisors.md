[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › A21

# A21 · Count the divisors

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | 4b · Running result | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A16](A16-count-multiples-of-5.md) | Custom |

## Goal

Give back how many numbers from 1 to n divide n exactly (n ≥ 1).

## Start and check

```bash
./ex start A21     # creates practice/A21_CountDivisors.cs (never overwrites your work)
./ex check A21     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountDivisors(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDivisors(6)` | `4` |
| `CountDivisors(7)` | `2` |
| `CountDivisors(1)` | `1` |
| `CountDivisors(12)` | `6` |

## Edge cases to test

- n = 1: 1 divisor.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Loop d from 1 to n.

</details>

<details><summary>Hint 2</summary>

`n % d == 0` means d divides n. Count it.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back how many divisors are even.

## Solution

Only after a real try: [open the solution for A21](../solutions/A21_CountDivisors.cs). Your solution can be different and still correct!

---

Previous: [A20 · Power of 2](A20-powers-of-2.md) · [All exercises](README.md) · Next: [A22 · Sum of the divisors](A22-sum-of-divisors.md)
