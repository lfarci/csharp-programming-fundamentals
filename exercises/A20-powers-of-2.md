[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › A20

# A20 · Power of 2

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | 4b · Running result | [Accumulator](../cookbook/02-accumulator.md) | [A04](A04-factorial.md) | Custom |

## Goal

Give back 2 to the power n (n ≥ 0), by multiplying by 2, n times.

## Start and check

```bash
./ex start A20     # creates practice/A20_PowersOf2.cs (never overwrites your work)
./ex check A20     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long PowerOf2(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PowerOf2(3)` | `8` |
| `PowerOf2(0)` | `1` |
| `PowerOf2(10)` | `1024` |

## Edge cases to test

- n = 0: 1.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Product box `result = 1`.

</details>

<details><summary>Hint 2</summary>

The loop runs n times; each turn: `result *= 2`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back 3 to the power n.

## Solution

Only after a real try: [open the solution for A20](../solutions/A20_PowersOf2.cs). Your solution can be different and still correct!

---

Previous: [A19 · Product from a to b](A19-product-from-a-to-b.md) · [All exercises](README.md) · Next: [A21 · Count the divisors](A21-count-divisors.md)
