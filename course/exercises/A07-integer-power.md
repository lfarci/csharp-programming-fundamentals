---
prev:
  text: "A04 · Factorial"
  link: /exercises/A04-factorial
next:
  text: "A05 · Sum and sum of squares"
  link: /exercises/A05-sum-square-difference
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A07

# A07 · Integer power

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 10 of 12 in this group (23 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Accumulator](../cookbook/02-accumulator.md) | [A04](A04-factorial.md) |

</div>

## Goal

Give back `baseValue` to the power `exponent` (exponent ≥ 0), using a loop.

## Start and check

```bash
./ex start A07     # creates practice/A07_IntegerPower.cs (never overwrites your work)
./ex check A07     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long Power(int baseValue, int exponent)`: input = baseValue, an int (whole number), exponent, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Power(3, 4)` | `81` |
| `Power(2, 10)` | `1024` |
| `Power(5, 0)` | `1` |
| `Power(-2, 3)` | `-8` |

## Edge cases to test

- Exponent 0 → 1.
- Base 0 → 0 (except 0^0 = 1 by our convention).

`./ex check` tests these too: `Power(0, 3)` gives `0`; `Power(0, 0)` gives `1`.

## Rules

- No `Math.Pow`. A loop with a product box.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

3^4 = 3 × 3 × 3 × 3: multiply by the **same** number, exponent times.

</details>

<details><summary>Hint 2</summary>

Difference with factorial: you multiply by `baseValue`, not by `i`.

</details>

<details><summary>Hint 3</summary>

`for (int i = 0; i < exponent; i++) result *= baseValue;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print all powers of 2 from 2^0 to 2^N, with only one multiplication per turn.

## Solution

Only after a real try: [open the solution for A07](../../internal/solutions/A07_IntegerPower.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A04 · Factorial](A04-factorial.md) · [Loops](../themes/loops.md) · Next: [A05 · Sum and sum of squares](A05-sum-square-difference.md)

</div>
