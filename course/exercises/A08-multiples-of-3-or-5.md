---
prev:
  text: "A17 · Sum the multiples of k"
  link: /exercises/A17-sum-multiples-of-k
next:
  text: "L05 · Until zero"
  link: /exercises/L05-until-zero
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops-keep-only-some.md) › A08

# A08 · Multiples of 3 or 5

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 9 of 9 in this group (34 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Challenge | medium | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A03](A03-sum-even-values.md) |

</div>

Source: prepares [Project Euler #1](https://projecteuler.net/problem=1).

## Goal

Give back the sum of all numbers **below** n that are multiples of 3 or 5.

## Start and check

```bash
./ex start A08     # creates practice/A08_MultiplesOf3Or5.cs (never overwrites your work)
./ex check A08     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfMultiples(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfMultiples(10)` | `23` |
| `SumOfMultiples(20)` | `78` |
| `SumOfMultiples(1)` | `0` |
| `SumOfMultiples(16)` | `60` |

## Edge cases to test

- 15 is a multiple of 3 **and** 5: count it once.
- "below N" → N itself is not included.

## Rules

- One loop, one `if` with `||`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Below 10: 3, 5, 6, 9 → 23. Write them on paper first.

</details>

<details><summary>Hint 2</summary>

Filter: `i % 3 == 0 || i % 5 == 0`.

</details>

<details><summary>Hint 3</summary>

"below N": `i < n`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Solve [Project Euler #1](https://projecteuler.net/problem=1) (N = 1000).

## Solution

Only after a real try: [open the solution for A08](../../internal/solutions/A08_MultiplesOf3Or5.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A17 · Sum the multiples of k](A17-sum-multiples-of-k.md) · [Loops](../themes/loops.md) · Next: [L05 · Until zero](L05-until-zero.md)

</div>
