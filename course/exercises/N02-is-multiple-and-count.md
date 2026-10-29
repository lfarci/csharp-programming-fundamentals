---
prev:
  text: "Methods and errors"
  link: /themes/methods
next:
  text: "N01 · Armstrong with methods"
  link: /exercises/N01-armstrong-with-methods
---

[Home](../../README.md) › [Exercises](README.md) › [Methods and errors](../themes/methods.md) › [Methods](../themes/methods.md#methods) › N02

# N02 · A method that calls one

<ExerciseHeader />

<div class="gh-only">

**Methods and errors › Methods** · exercise 1 of 2 in this group (1 of 4 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A16](A16-count-multiples-of-5.md) |

</div>

## Goal

Write two small methods. `IsMultiple(n, k)` gives back `true` if n is divisible by k. `CountMultiples(n, k)` counts the numbers from 1 to n divisible by k, by calling `IsMultiple`.

## Start and check

```bash
./ex start N02     # creates practice/N02_IsMultipleAndCount.cs (never overwrites your work)
./ex check N02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in these methods in the file. The *parameters* are its input; what you `return` is its result.

- `bool IsMultiple(int n, int k)`: input = n, an int (whole number), k, an int (whole number); result = a bool (true or false), given back with return.
- `int CountMultiples(int n, int k)`: input = n, an int (whole number), k, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IsMultiple(12, 3)` | `true` |
| `IsMultiple(7, 2)` | `false` |
| `CountMultiples(20, 5)` | `4` |
| `CountMultiples(10, 3)` | `3` |
| `CountMultiples(4, 5)` | `0` |

## Edge cases to test

- `k` bigger than n: 0.

## Rules

- `CountMultiples` must call `IsMultiple`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`IsMultiple` is one line: `return n % k == 0;`.

</details>

<details><summary>Hint 2</summary>

`CountMultiples` is A16 with the test replaced by a call: `if (IsMultiple(i, k)) count++;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Write `IsEven(int n)` and use it in `SumOfEvens(int n)`.

## Solution

Only after a real try: [open the solution for N02](../../internal/solutions/N02_IsMultipleAndCount.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [Methods and errors](../themes/methods.md) · [Methods and errors](../themes/methods.md) · Next: [N01 · Armstrong with methods](N01-armstrong-with-methods.md)

</div>
