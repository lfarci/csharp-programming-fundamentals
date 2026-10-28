# P02 · All primes up to N

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 4d · Search | [Counter loop](../cookbook/01-counter-loop.md), [Flag/search](../cookbook/05-flag-search.md), [Accumulator](../cookbook/02-accumulator.md) | [P01](P01-is-it-prime.md) | Custom |

## 🎯 Goal

Read N. Print all prime numbers from 2 to N on one line, then how many there are.

## 🧪 Examples

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

## ⚠️ Edge cases to test

- N < 2 → none.

## 📏 Rules

- Nested loops: the P01 test inside a counter loop.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Outer loop: `candidate` from 2 to N.

</details>

<details><summary>Hint 2</summary>

Inner part: copy your P01 code, with `candidate` instead of `n`.

</details>

<details><summary>Hint 3</summary>

The flag must be **reset** for every candidate (declare it inside the outer loop).

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the first N primes (not the primes up to N).

## 🔑 Solution

Only after a real try: [P02-primes-up-to-n](../solutions/P02-primes-up-to-n.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
