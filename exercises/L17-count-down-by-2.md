🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › L17

# L17 · Count down by 2

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [L12](L12-count-down.md) | Custom |

## 🎯 Goal

Print n, n−2, n−4, … while the number is at least 1, one per line.

## ▶️ Start and check

```bash
./ex start L17     # creates practice/L17_CountDownBy2.cs (never overwrites your work)
./ex check L17     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `void CountDownBy2(int n)`: input = n, an int (whole number); result = nothing is returned: the method prints with Console.Write / Console.WriteLine.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDownBy2(9)` | prints:<br>`9`<br>`7`<br>`5`<br>`3`<br>`1` |
| `CountDownBy2(6)` | prints:<br>`6`<br>`4`<br>`2` |

## ⚠️ Edge cases to test

- n = 1: one line.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

L12 with a step of `i -= 2`.

</details>

<details><summary>Hint 2</summary>

Test `i >= 1`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count down by 3 from n.

## 🔑 Solution

Only after a real try: [open the solution for L17](../solutions/L17_CountDownBy2.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L16 · Odd numbers](L16-odd-numbers.md) · 📚 [All exercises](README.md) · Next: [L18 · Square numbers](L18-squares.md) ➡️
