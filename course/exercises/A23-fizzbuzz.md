---
prev:
  text: "A17 · Sum the multiples of k"
  link: /exercises/A17-sum-multiples-of-k
next:
  text: "A24 · Perfect number"
  link: /exercises/A24-perfect-number
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops-keep-only-some.md) › A23

# A23 · FizzBuzz

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 9 of 11 in this group (34 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Counter loop](../cookbook/01-counter-loop.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [L11](L11-count-from-a-to-b.md), [A02](A02-count-multiples-of-3.md) |

</div>

## Goal

Print the numbers from 1 to n, one per line. But print `Fizz` instead of a multiple of 3, `Buzz` instead of a multiple of 5, and `FizzBuzz` instead of a multiple of both.

## Start and check

```bash
./ex start A23     # creates practice/A23_Fizzbuzz.cs (never overwrites your work)
./ex check A23     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void PrintFizzBuzz(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PrintFizzBuzz(5)` | prints:<br>`1`<br>`2`<br>`Fizz`<br>`4`<br>`Buzz` |
| `PrintFizzBuzz(15)` | prints:<br>`1`<br>`2`<br>`Fizz`<br>`4`<br>`Buzz`<br>`Fizz`<br>`7`<br>`8`<br>`Fizz`<br>`Buzz`<br>`11`<br>`Fizz`<br>`13`<br>`14`<br>`FizzBuzz` |

## Edge cases to test

- n = 15: the last line is `FizzBuzz`, not `Fizz`.
- n = 0: nothing is printed.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

One counter loop from 1 to n, with an `if` / `else if` chain inside.

</details>

<details><summary>Hint 2</summary>

Test "multiple of both" (`i % 15 == 0`) **first**: if `i % 3 == 0` comes first, 15 prints `Fizz`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Add `Bazz` for multiples of 7 (and `FizzBazz`, `BuzzBazz`… for the combinations).

## Solution

Only after a real try: [open the solution for A23](../../internal/solutions/A23_Fizzbuzz.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A17 · Sum the multiples of k](A17-sum-multiples-of-k.md) · [Loops](../themes/loops.md) · Next: [A24 · Perfect number](A24-perfect-number.md)

</div>
