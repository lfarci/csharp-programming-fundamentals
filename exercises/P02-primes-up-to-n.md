[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › P02

# P02 · All primes up to N

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | hard | 4d · Search | [Counter loop](../cookbook/01-counter-loop.md), [Flag/search](../cookbook/05-flag-search.md), [Accumulator](../cookbook/02-accumulator.md) | [P01](P01-is-it-prime.md) | Custom |

## Goal

Read N. Print all prime numbers from 2 to N on one line, then how many there are.

## Start and check

```bash
./ex start P02     # creates practice/P02_PrimesUpToN.cs (never overwrites your work)
./ex check P02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `20`

```text
2 3 5 7 11 13 17 19
Count: 8
```

**Example 2** — input: `2`

```text
2
Count: 1
```

**Example 3** — input: `1`

```text
Count: 0
```

## Edge cases to test

- N < 2 → none.

## Rules

- Nested loops: the P01 test inside a counter loop.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Outer loop: `candidate` from 2 to N.

</details>

<details><summary>Hint 2</summary>

Inner part: copy your P01 code, with `candidate` instead of `n`.

</details>

<details><summary>Hint 3</summary>

The flag must be **reset** for every candidate (declare it inside the outer loop).

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the first N primes (not the primes up to N).

## Solution

Only after a real try: [open the solution for P02](../solutions/P02_PrimesUpToN.cs). Your solution can be different and still correct!

---

Previous: [P01 · Is it prime?](P01-is-it-prime.md) · [All exercises](README.md) · Next: [M01 · Armstrong number](M01-armstrong-number.md)
