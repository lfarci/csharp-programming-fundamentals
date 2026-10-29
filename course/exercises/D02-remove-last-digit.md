---
prev:
  text: "D01 · Last digit"
  link: /exercises/D01-last-digit
next:
  text: "D03 · Count the digits"
  link: /exercises/D03-count-digits
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops-digits.md) › D02

# D02 · Remove the last digit

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 2 of 12 in this group (57 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Digit extraction](../cookbook/06-digit-extraction.md) | [D01](D01-last-digit.md) |

</div>

## Goal

Give back n without its last digit (n ≥ 0).

## Start and check

```bash
./ex start D02     # creates practice/D02_RemoveLastDigit.cs (never overwrites your work)
./ex check D02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int RemoveLastDigit(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `RemoveLastDigit(352)` | `35` |
| `RemoveLastDigit(7)` | `0` |
| `RemoveLastDigit(0)` | `0` |
| `RemoveLastDigit(1000)` | `100` |

## Edge cases to test

- One digit → 0.

## Rules

- No string. Use integer `/`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

What is 352 divided by 10, if you throw away everything after the decimal point?

</details>

<details><summary>Hint 2</summary>

With two `int`s, `/` drops the rest: `352 / 10` gives `35`, not `35.2`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the first digit of a 3-digit number using only `/`.

## Solution

Only after a real try: [open the solution for D02](../../internal/solutions/D02_RemoveLastDigit.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D01 · Last digit](D01-last-digit.md) · [Loops](../themes/loops.md) · Next: [D03 · Count the digits](D03-count-digits.md)

</div>
