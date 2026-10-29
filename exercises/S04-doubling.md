🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › S04

# S04 · Doubling

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4d · State | [State update](../cookbook/07-state-update.md) | [L11](L11-count-from-a-to-b.md) | Custom |

## 🎯 Goal

Print `count` values: `start`, then each value doubled (`3, 6, 12`).

## ▶️ Start and check

```bash
./ex start S04     # creates practice/S04_Doubling.cs (never overwrites your work)
./ex check S04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `void PrintDoubling(int start, int count)`: input = start, an int (whole number), count, an int (whole number); result = nothing is returned: the method prints with Console.Write / Console.WriteLine.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PrintDoubling(1, 5)` | prints:<br>`1`<br>`2`<br>`4`<br>`8`<br>`16` |
| `PrintDoubling(3, 3)` | prints:<br>`3`<br>`6`<br>`12` |

## ⚠️ Edge cases to test

- count = 0: nothing.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

One box `value`, starting at `start`.

</details>

<details><summary>Hint 2</summary>

Each turn: print it, then `value = value * 2;`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Each value is the previous one plus 3.

## 🔑 Solution

Only after a real try: [open the solution for S04](../solutions/S04_Doubling.cs). Your solution can be different and still correct!

---

⬅️ Previous: [S01 · Trace two changing variables (paper)](S01-trace-updates.md) · 📚 [All exercises](README.md) · Next: [S02 · Fibonacci](S02-fibonacci.md) ➡️
