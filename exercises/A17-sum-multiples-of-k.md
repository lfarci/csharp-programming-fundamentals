[Home](../README.md) › [Exercises](README.md) › [Loops: keep a running result](../themes/loops-running-result.md) › A17

# A17 · Sum the multiples of k

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | [Loops: keep a running result](../themes/loops-running-result.md) | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A03](A03-sum-even-values.md), [A16](A16-count-multiples-of-5.md) | Custom |

## Goal

Give back the sum of the numbers from 1 to n that are divisible by k (k ≥ 1).

## Start and check

```bash
./ex start A17     # creates practice/A17_SumMultiplesOfK.cs (never overwrites your work)
./ex check A17     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumMultiplesOf(int k, int n)`: input = k, an int (whole number), n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumMultiplesOf(3, 10)` | `18` |
| `SumMultiplesOf(5, 20)` | `50` |
| `SumMultiplesOf(4, 3)` | `0` |

## Edge cases to test

- k bigger than n: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Like A03, with `k` instead of 2.

</details>

<details><summary>Hint 2</summary>

`if (i % k == 0) sum += i;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count them instead of adding them.

## Solution

Only after a real try: [open the solution for A17](../solutions/A17_SumMultiplesOfK.cs). Your solution can be different and still correct!

---

Previous: [A16 · Count multiples of 5](A16-count-multiples-of-5.md) · [All exercises](README.md) · Next: [A18 · Sum of cubes](A18-sum-of-cubes.md)
