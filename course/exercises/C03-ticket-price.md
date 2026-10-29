---
prev:
  text: "C02 · Largest of three"
  link: /exercises/C02-largest-of-three
next:
  text: "C04 · Grade from a score"
  link: /exercises/C04-grade-from-a-score
---

[Home](../../README.md) › [Exercises](README.md) › [Basics](../themes/basics.md) › [Conditions](../themes/basics.md#conditions) › C03

# C03 · Ticket price

<ExerciseHeader />

<div class="gh-only">

**Basics › Conditions** · exercise 3 of 4 in this group (6 of 7 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | — | [C01](C01-even-or-odd.md) |

</div>

## Goal

A cinema ticket costs 5 for children under 12, 7 for people aged 65 or more, and 10 for everyone else. Give back the price for `age`.

## Start and check

```bash
./ex start C03     # creates practice/C03_TicketPrice.cs (never overwrites your work)
./ex check C03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int Price(int age)`: input = age, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Price(11)` | `5` |
| `Price(12)` | `10` |
| `Price(64)` | `10` |
| `Price(65)` | `7` |
| `Price(0)` | `5` |

## Edge cases to test

- The boundaries 11/12 and 64/65: test them all!

## Rules

- Use `if` / `else if` / `else`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [reading worksheet](../docs/reading-an-exercise.md#the-template): what goes in? what comes out? a tiny example by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Three categories → three branches.

</details>

<details><summary>Hint 2</summary>

"under 12" means `age < 12`. "65 or more" means `age >= 65`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Add a rule: on Wednesday (ask the day as a number 1-7) everybody pays 6.

## Solution

Only after a real try: [open the solution for C03](../../internal/solutions/C03_TicketPrice.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [C02 · Largest of three](C02-largest-of-three.md) · [Basics](../themes/basics.md) · Next: [C04 · Grade from a score](C04-grade-from-a-score.md)

</div>
