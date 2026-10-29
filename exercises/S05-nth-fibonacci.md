🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › S05

# S05 · The n-th Fibonacci number

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4d · State | [State update](../cookbook/07-state-update.md) | [S02](S02-fibonacci.md) | Custom |

## 🎯 Goal

Give back the Fibonacci number at position n: position 0 is 0, position 1 is 1, then 1, 2, 3, 5, 8, …

## ▶️ Start and check

```bash
./ex start S05     # creates practice/S05_NthFibonacci.cs (never overwrites your work)
./ex check S05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long Fibonacci(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Fibonacci(0)` | `0` |
| `Fibonacci(1)` | `1` |
| `Fibonacci(6)` | `8` |
| `Fibonacci(10)` | `55` |

## ⚠️ Edge cases to test

- n = 0: 0.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

S02 without printing: do the same 3 moves n times.

</details>

<details><summary>Hint 2</summary>

After the loop, `previous` holds the answer.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Give back the sum of the first n Fibonacci numbers.

## 🔑 Solution

Only after a real try: [open the solution for S05](../solutions/S05_NthFibonacci.cs). Your solution can be different and still correct!

---

⬅️ Previous: [S02 · Fibonacci](S02-fibonacci.md) · 📚 [All exercises](README.md) · Next: [S03 · Even Fibonacci sum](S03-even-fibonacci-sum.md) ➡️
