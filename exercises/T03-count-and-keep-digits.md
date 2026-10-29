[Home](../README.md) › [Exercises](README.md) › [Arrays and text](../themes/arrays.md) › T03

# T03 · Count and keep the digits

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | medium | [Arrays and text](../themes/arrays.md) | [Build a string](../cookbook/12-string-building.md), [Accumulator](../cookbook/02-accumulator.md) | [T02](T02-remove-spaces.md) | Custom |

## Goal

Give back a new text with only the digit characters of `text`, in order.

## Start and check

```bash
./ex start T03     # creates practice/T03_CountAndKeepDigits.cs (never overwrites your work)
./ex check T03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `string KeepDigits(string text)`: input = text, a string (text); result = a string (text), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `KeepDigits("a1 b2!")` | `"12"` |
| `KeepDigits("abc")` | `""` |
| `KeepDigits("2026")` | `"2026"` |

## Edge cases to test

- No digit → 0 and empty text.

## Rules

- One loop, two boxes. `char.IsDigit(c)` or `c >= '0' && c <= '9'`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Two boxes: `count = 0` and `kept = ""`.

</details>

<details><summary>Hint 2</summary>

Update **both** inside the same `if`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also compute the **sum** of those digits (`c - '0'` turns `'7'` into 7).

## Solution

Only after a real try: [open the solution for T03](../solutions/T03_CountAndKeepDigits.cs). Your solution can be different and still correct!

---

Previous: [T02 · Remove spaces](T02-remove-spaces.md) · [All exercises](README.md) · Next: [F01 · Save numbers to a file](F01-numbers-file.md)
