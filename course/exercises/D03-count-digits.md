---
prev:
  text: "D02 · Remove the last digit"
  link: /exercises/D02-remove-last-digit
next:
  text: "D08 · First digit"
  link: /exercises/D08-first-digit
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops-digits.md) › D03

# D03 · Count the digits

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 3 of 13 in this group (60 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | medium | write code | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D02](D02-remove-last-digit.md), [L05](L05-until-zero.md) |

</div>

## Goal

Give back how many digits n has (n ≥ 0). 0 has 1 digit.

## Start and check

```bash
./ex start D03     # creates practice/D03_CountDigits.cs (never overwrites your work)
./ex check D03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountDigits(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDigits(352)` | `3` |
| `CountDigits(0)` | `1` |
| `CountDigits(1000)` | `4` |
| `CountDigits(7)` | `1` |

## Edge cases to test

- **0 has 1 digit** (a plain `while (n > 0)` loop says 0).

## Rules

- A loop. No `ToString().Length`, no `Math.Log10`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

How many times can you remove the last digit before the number becomes 0?

</details>

<details><summary>Hint 2</summary>

Trace 352 → 35 → 3 → 0: three removals.

</details>

<details><summary>Hint 3</summary>

For 0: a `do … while` runs at least once, so it counts 1.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count how many digits of N are even.

## Solution

Only after a real try: [open the solution for D03](../../internal/solutions/D03_CountDigits.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D02 · Remove the last digit](D02-remove-last-digit.md) · [Loops](../themes/loops.md) · Next: [D08 · First digit](D08-first-digit.md)

</div>
