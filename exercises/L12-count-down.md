🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › L12

# L12 · Count down

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [L11](L11-count-from-a-to-b.md) | Custom |

## 🎯 Goal

Print n, n−1, …, 1, one per line.

## ▶️ Start and check

```bash
./ex start L12     # creates practice/L12_CountDown.cs (never overwrites your work)
./ex check L12     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `void CountDown(int n)`: input = n, an int (whole number); result = nothing is returned: the method prints with Console.Write / Console.WriteLine.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDown(4)` | prints:<br>`4`<br>`3`<br>`2`<br>`1` |
| `CountDown(1)` | prints:<br>`1` |

## ⚠️ Edge cases to test

- `CountDown(0)` prints nothing.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Start at `n`. Step with `i--`.

</details>

<details><summary>Hint 2</summary>

Keep going while `i >= 1`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count down from n to 0 (0 included).

## 🔑 Solution

Only after a real try: [open the solution for L12](../solutions/L12_CountDown.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L11 · Count from a to b](L11-count-from-a-to-b.md) · 📚 [All exercises](README.md) · Next: [L13 · Count by 3](L13-count-by-3.md) ➡️
