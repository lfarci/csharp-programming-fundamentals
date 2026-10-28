# P01 · Is it prime?

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4d · Search | [Flag/search](../cookbook/05-flag-search.md) | [A02](A02-count-multiples-of-3.md) | Custom |

## 🎯 Goal

Read N. Say if it is a prime number (≥ 2 and only divisible by 1 and itself).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `7`

```text
7 is prime
```

**Example 2** — input: `9`

```text
9 is not prime
```

**Example 3** — input: `1`

```text
1 is not prime
```

**Example 4** — input: `2`

```text
2 is prime
```

**Example 5** — input: `97`

```text
97 is prime
```

## ⚠️ Edge cases to test

- 0 and 1 are not prime.
- 2 is the only even prime.

## 📏 Rules

- A loop with a `bool` flag. No library.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Try every divisor `d` from 2 to N − 1. One divisor is enough to say "not prime".

</details>

<details><summary>Hint 2</summary>

Flag: `bool isPrime = n >= 2;` and set it to `false` when `n % d == 0`.

</details>

<details><summary>Hint 3</summary>

Do not print inside the loop. Decide **after** the loop.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Make it faster: stop at `d * d <= n`. Why does that work?

## 🔑 Solution

Only after a real try: [P01-is-it-prime](../solutions/P01-is-it-prime.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
