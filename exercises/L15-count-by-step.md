🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › L15

# L15 · Count by any step

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [L14](L14-count-by-5.md) | Custom |

## 🎯 Goal

Print `step`, 2×`step`, 3×`step`, … up to n, one per line. (`step` is at least 1.)

## ▶️ Start and check

```bash
./ex start L15     # creates practice/L15_CountByStep.cs (never overwrites your work)
./ex check L15     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void CountByStep(int step, int n)`: input = step, an int (whole number), n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountByStep(2, 7)` | prints:<br>`2`<br>`4`<br>`6` |
| `CountByStep(4, 12)` | prints:<br>`4`<br>`8`<br>`12` |
| `CountByStep(1, 3)` | prints:<br>`1`<br>`2`<br>`3` |

## ⚠️ Edge cases to test

- `step` bigger than n: nothing.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

L13 and L14 with the 3 or 5 replaced by `step`.

</details>

<details><summary>Hint 2</summary>

Start at `step`, step `i += step`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the multiples of `step` from n down to `step`.

## 🔑 Solution

Only after a real try: [open the solution for L15](../solutions/L15_CountByStep.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L14 · Count by 5](L14-count-by-5.md) · 📚 [All exercises](README.md) · Next: [L16 · Odd numbers](L16-odd-numbers.md) ➡️
