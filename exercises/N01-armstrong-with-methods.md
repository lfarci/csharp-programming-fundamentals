[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › N01

# N01 · Armstrong with methods

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | hard | 10 · Methods | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [M02](M02-armstrong-numbers-in-a-range.md) | Custom |

## Goal

Split the Armstrong check into three small methods: `CountDigits`, `Power` and `IsArmstrong` (which uses the other two).

## Start and check

```bash
./ex start N01     # creates practice/N01_ArmstrongWithMethods.cs (never overwrites your work)
./ex check N01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in these methods in the file. The *parameters* are its input; what you `return` is its result.

- `int CountDigits(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.
- `int Power(int baseValue, int exponent)`: input = baseValue, an int (whole number), exponent, an int (whole number); result = an int (whole number), given back with return.
- `bool IsArmstrong(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDigits(352)` | `3` |
| `CountDigits(0)` | `1` |
| `Power(3, 4)` | `81` |
| `Power(5, 0)` | `1` |
| `IsArmstrong(153)` | `true` |
| `IsArmstrong(154)` | `false` |
| `IsArmstrong(9474)` | `true` |

## Edge cases to test

- `CountDigits(0)` must return 1.

## Rules

- Each method does **one** recipe. No `Math.Pow`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`static int CountDigits(int n) { ... return digits; }`

</details>

<details><summary>Hint 2</summary>

`IsArmstrong` calls the two others and returns a `bool`.

</details>

<details><summary>Hint 3</summary>

Test each method alone first: `./ex check` shows which one is wrong, and `./ex run` lets you try your own values.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Add `IsPalindrome(int n)` and print the numbers in the range that are both (hint: 1–9).

## Solution

Only after a real try: [open the solution for N01](../solutions/N01_ArmstrongWithMethods.cs). Your solution can be different and still correct!

---

Previous: [K01 · Shopping list](K01-shopping-list.md) · [All exercises](README.md)
