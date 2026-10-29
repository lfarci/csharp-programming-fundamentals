[Home](../README.md) › [Exercises](README.md) › [Arrays and text](../themes/arrays.md) › T02

# T02 · Remove spaces

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | easy | [Arrays and text](../themes/arrays.md) | [Build a string](../cookbook/12-string-building.md) | [T01](T01-count-a-letter.md) | Custom |

## Goal

Give back `text` without its spaces.

## Start and check

```bash
./ex start T02     # creates practice/T02_RemoveSpaces.cs (never overwrites your work)
./ex check T02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `string RemoveSpaces(string text)`: input = text, a string (text); result = a string (text), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `RemoveSpaces("a b c")` | `"abc"` |
| `RemoveSpaces("   ")` | `""` |
| `RemoveSpaces("no-space")` | `"no-space"` |

## Edge cases to test

- Only spaces → empty result.

## Rules

- Build a new string with `+=`. No `Replace`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Box `result = ""`.

</details>

<details><summary>Hint 2</summary>

Keep the character when `c != ' '`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Reverse the text (`abc` → `cba`).

## Solution

Only after a real try: [open the solution for T02](../solutions/T02_RemoveSpaces.cs). Your solution can be different and still correct!

---

Previous: [T01 · Count a letter](T01-count-a-letter.md) · [All exercises](README.md) · Next: [T03 · Count and keep the digits](T03-count-and-keep-digits.md)
