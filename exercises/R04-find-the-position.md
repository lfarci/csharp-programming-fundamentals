[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › R04

# R04 · Find the position

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md), [Flag/search](../cookbook/05-flag-search.md) | [R03](R03-count-matches.md) | Custom |

## Goal

Give back the **first** index where `target` is, or -1 if it is not in the array.

## Start and check

```bash
./ex start R04     # creates practice/R04_FindThePosition.cs (never overwrites your work)
./ex check R04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int IndexOf(int[] values, int target)`: input = values, an int[] (array of whole numbers), target, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IndexOf(new int[] { 7, 3, 9, 3 }, 3)` | `1` |
| `IndexOf(new int[] { 7, 3, 9, 3 }, 8)` | `-1` |
| `IndexOf(new int[] { 5 }, 5)` | `0` |
| `IndexOf(new int[0], 1)` | `-1` |

## Edge cases to test

- Target at index 0 (0 is a valid position: use -1 for "not found").
- Several matches → the first.

## Rules

- No `Array.IndexOf`. Use `break`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Box `int index = -1;` (means not found).

</details>

<details><summary>Hint 2</summary>

When found: `index = i; break;`

</details>

<details><summary>Hint 3</summary>

You can `return i;` as soon as you find it. After the loop, `return -1;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the **last** position instead (hint: loop backwards).

## Solution

Only after a real try: [open the solution for R04](../solutions/R04_FindThePosition.cs). Your solution can be different and still correct!

---

Previous: [R03 · Count matches in an array](R03-count-matches.md) · [All exercises](README.md) · Next: [R05 · Reverse an array](R05-reverse-an-array.md)
