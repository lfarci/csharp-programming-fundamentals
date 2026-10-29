---
prev:
  text: "R05 · Reverse an array"
  link: /exercises/R05-reverse-an-array
next:
  text: "T02 · Remove spaces"
  link: /exercises/T02-remove-spaces
---

[Home](../../README.md) › [Exercises](README.md) › [Arrays, text and lists](../themes/arrays.md) › [Text](../themes/arrays-text.md) › T01

# T01 · Count a letter

<ExerciseHeader />

<div class="gh-only">

**Arrays, text and lists › Text** · exercise 1 of 3 in this group (7 of 11 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Build a string](../cookbook/12-string-building.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [R03](R03-count-matches.md) |

</div>

## Goal

Give back how many times `letter` appears in `text` (case-sensitive).

## Start and check

```bash
./ex start T01     # creates practice/T01_CountALetter.cs (never overwrites your work)
./ex check T01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountLetter(string text, char letter)`: input = text, a string (text), letter, a char (one character); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountLetter("banana", 'a')` | `3` |
| `CountLetter("BANANA", 'a')` | `0` |
| `CountLetter("", 'a')` | `0` |

## Edge cases to test

- Empty text.
- `'A'` is not `'a'`.

## Rules

- `foreach (char c in text)`. No LINQ.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`letter` is a `char` (single quotes: `'a'`). Compare each `c` of the text with it: `c == letter`.

</details>

<details><summary>Hint 2</summary>

`if (c == letter) count++;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count all vowels (a, e, i, o, u) in a text.

## Solution

Only after a real try: [open the solution for T01](../../internal/solutions/T01_CountALetter.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [R05 · Reverse an array](R05-reverse-an-array.md) · [Arrays, text and lists](../themes/arrays.md) · Next: [T02 · Remove spaces](T02-remove-spaces.md)

</div>
