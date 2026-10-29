[Home](../README.md) › [Exercises](README.md) › [Loops: repeat and count](../themes/loops-repeat.md) › L13

# L13 · Count by 3

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: repeat and count](../themes/loops-repeat.md) | [Counter loop](../cookbook/01-counter-loop.md) | [L11](L11-count-from-a-to-b.md) | Custom |

## Goal

Print 3, 6, 9, … up to n (included when it is a multiple of 3), one per line.

## Start and check

```bash
./ex start L13     # creates practice/L13_CountBy3.cs (never overwrites your work)
./ex check L13     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void CountBy3(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountBy3(10)` | prints:<br>`3`<br>`6`<br>`9` |
| `CountBy3(3)` | prints:<br>`3` |
| `CountBy3(12)` | prints:<br>`3`<br>`6`<br>`9`<br>`12` |

## Edge cases to test

- n smaller than 3: nothing is printed.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Start at 3. The step is `i += 3`.

</details>

<details><summary>Hint 2</summary>

The test is `i <= n`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count by 4 up to n.

## Solution

Only after a real try: [open the solution for L13](../solutions/L13_CountBy3.cs). Your solution can be different and still correct!

---

Previous: [L12 · Count down](L12-count-down.md) · [All exercises](README.md) · Next: [L14 · Count by 5](L14-count-by-5.md)
