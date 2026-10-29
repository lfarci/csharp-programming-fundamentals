[Home](../README.md) › [Exercises](README.md) › [Loops: remember changing values](../themes/loops-state.md) › S02

# S02 · Fibonacci

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | hard | [Loops: remember changing values](../themes/loops-state.md) | [State update](../cookbook/07-state-update.md) | [S01](S01-trace-updates.md), [A01](A01-sum-1-to-n.md) | Custom · teacher topic: Fibonacci |

## Goal

Read N. Print the first N Fibonacci numbers on one line, starting with 0 and 1. Each number is the sum of the two before it.

## Start and check

```bash
./ex start S02     # creates practice/S02_Fibonacci.cs (never overwrites your work)
./ex check S02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `6`

```text
0 1 1 2 3 5
```

**Example 2** — input: `1`

```text
0
```

**Example 3** — input: `10`

```text
0 1 1 2 3 5 8 13 21 34
```

## Edge cases to test

- N = 0 → nothing.
- N = 1 → only 0.
- N = 2 → 0 1.

## Rules

- No array, no recursion. Variables `previous`, `current`, `next`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Write the first 8 numbers on paper. Which two numbers do you need to make the next one?

</details>

<details><summary>Hint 2</summary>

Print `previous` at the start of each turn, then compute `next`, then slide.

</details>

<details><summary>Hint 3</summary>

Order: `next = previous + current; previous = current; current = next;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the N-th Fibonacci number only (position 0 is 0, position 1 is 1, position 10 is 55).

## Solution

Only after a real try: [open the solution for S02](../solutions/S02_Fibonacci.cs). Your solution can be different and still correct!

---

Previous: [S04 · Doubling](S04-doubling.md) · [All exercises](README.md) · Next: [S05 · The n-th Fibonacci number](S05-nth-fibonacci.md)
