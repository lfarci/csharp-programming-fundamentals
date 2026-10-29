🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › S03

# S03 · Even Fibonacci sum

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 4d · State | [State update](../cookbook/07-state-update.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [S02](S02-fibonacci.md), [A03](A03-sum-even-values.md) | Custom · prepares [Project Euler #2](https://projecteuler.net/problem=2) |

## 🎯 Goal

Read a limit. Add up the **even** Fibonacci numbers that are **not greater** than the limit.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `10`

```text
Sum: 10
```

**Example 2** — input: `100`

```text
Sum: 44
```

**Example 3** — input: `1`

```text
Sum: 0
```

## ⚠️ Edge cases to test

- The limit itself counts if it is an even Fibonacci number (limit 8 → 2 + 8 = 10).

## 📏 Rules

- `while` loop (you do not know how many terms).
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Up to 100: 0 1 1 2 3 5 8 13 21 34 55 89 → even ones 0, 2, 8, 34 → 44.

</details>

<details><summary>Hint 2</summary>

Stop condition: `while (previous <= limit)`.

</details>

<details><summary>Hint 3</summary>

Inside: `if (previous % 2 == 0) sum += previous;` then slide like S02.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Solve [Project Euler #2](https://projecteuler.net/problem=2) (limit four million). Use `long`.

## 🔑 Solution

Only after a real try: [open the solution for S03](../solutions/S03-even-fibonacci-sum.cs). Your solution can be different and still correct!

---

⬅️ Previous: [S02 · Fibonacci](S02-fibonacci.md) · 📚 [All exercises](README.md) · Next: [P01 · Is it prime?](P01-is-it-prime.md) ➡️
