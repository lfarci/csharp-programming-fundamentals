[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › P01

# P01 · Is it prime?

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | 4d · Search | [Flag/search](../cookbook/05-flag-search.md) | [A02](A02-count-multiples-of-3.md) | Custom |

## Goal

Give back `true` if n is a prime number (≥ 2 and only divisible by 1 and itself).

## Start and check

```bash
./ex start P01     # creates practice/P01_IsItPrime.cs (never overwrites your work)
./ex check P01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool IsPrime(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IsPrime(7)` | `true` |
| `IsPrime(9)` | `false` |
| `IsPrime(1)` | `false` |
| `IsPrime(2)` | `true` |
| `IsPrime(97)` | `true` |
| `IsPrime(0)` | `false` |

## Edge cases to test

- 0 and 1 are not prime.
- 2 is the only even prime.

## Rules

- A loop with a `bool` flag. No library.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Try every divisor `d` from 2 to N − 1. One divisor is enough to say "not prime".

</details>

<details><summary>Hint 2</summary>

Flag: `bool isPrime = n >= 2;` and set it to `false` when `n % d == 0`.

</details>

<details><summary>Hint 3</summary>

Do not `return true` inside the loop: you only know it is prime **after** checking every divisor.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Make it faster: stop at `d * d <= n`. Why does that work?

## Solution

Only after a real try: [open the solution for P01](../solutions/P01_IsItPrime.cs). Your solution can be different and still correct!

---

Previous: [S03 · Even Fibonacci sum](S03-even-fibonacci-sum.md) · [All exercises](README.md) · Next: [P02 · All primes up to N](P02-primes-up-to-n.md)
