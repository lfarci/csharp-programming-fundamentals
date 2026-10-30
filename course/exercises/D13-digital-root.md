---
prev:
  text: "D05 · Reverse a number"
  link: /exercises/D05-reverse-a-number
next:
  text: "D06 · Palindrome number"
  link: /exercises/D06-palindrome-number
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops-digits.md) › D13

# D13 · Digital root

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 12 of 13 in this group (69 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Digit extraction](../cookbook/06-digit-extraction.md) | [D04](D04-digit-sum.md) |

</div>

## Goal

Add the digits of n (n ≥ 0), then add the digits of the result, and so on, until one digit remains. Give it back. 9875 → 29 → 11 → 2.

## Start and check

```bash
./ex start D13     # creates practice/D13_DigitalRoot.cs (never overwrites your work)
./ex check D13     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int DigitalRoot(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DigitalRoot(7)` | `7` |
| `DigitalRoot(38)` | `2` |
| `DigitalRoot(9875)` | `2` |
| `DigitalRoot(10)` | `1` |
| `DigitalRoot(999)` | `9` |

## Edge cases to test

- n already has one digit: give it back as it is.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

The inner loop is D04 (sum of the digits).

</details>

<details><summary>Hint 2</summary>

The outer loop repeats while the number still has 2 digits or more: `while (n >= 10)`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count how many rounds it takes (the additive persistence: 9875 takes 3).

## Solution

Only after a real try: [open the solution for D13](../../internal/solutions/D13_DigitalRoot.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D05 · Reverse a number](D05-reverse-a-number.md) · [Loops](../themes/loops.md) · Next: [D06 · Palindrome number](D06-palindrome-number.md)

</div>
