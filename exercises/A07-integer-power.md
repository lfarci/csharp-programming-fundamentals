[Home](../README.md) › [Exercises](README.md) › [Loops: keep a running result](../themes/loops-running-result.md) › A07

# A07 · Integer power

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | [Loops: keep a running result](../themes/loops-running-result.md) | [Accumulator](../cookbook/02-accumulator.md) | [A04](A04-factorial.md) | Custom |

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

Only after a real try: [open the solution for A07](../solutions/A07_IntegerPower.cs). Your solution can be different and still correct!

---

Previous: [A06 · Average until zero](A06-average-until-zero.md) · [All exercises](README.md) · Next: [A08 · Multiples of 3 or 5](A08-multiples-of-3-or-5.md)
