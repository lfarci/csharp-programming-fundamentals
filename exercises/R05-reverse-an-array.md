🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › R05

# R05 · Reverse an array

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md) | [R01](R01-sum-an-array.md) | Custom |

## 🎯 Goal

Give back a **new** array with the same values in reverse order.

## ▶️ Start and check

```bash
./ex start R05     # creates practice/R05_ReverseAnArray.cs (never overwrites your work)
./ex check R05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int[] Reversed(int[] values)`: input = values, an int[] (array of whole numbers); result = an int[] (array of whole numbers), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Reversed(new int[] { 1, 2, 3, 4 })` | `new int[] { 4, 3, 2, 1 }` |
| `Reversed(new int[] { 8 })` | `new int[] { 8 }` |
| `Reversed(new int[0])` | `new int[0]` |

## ⚠️ Edge cases to test

- One element.
- Odd or even length.

## 📏 Rules

- No `Array.Reverse`. Write into the new array with an index.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

The new array has the same `Length`.

</details>

<details><summary>Hint 2</summary>

Value at index `i` goes to index `values.Length - 1 - i`. Check with a 4-box drawing.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Reverse the array **in place** (swap first and last, then second and second-to-last…).

## 🔑 Solution

Only after a real try: [open the solution for R05](../solutions/R05_ReverseAnArray.cs). Your solution can be different and still correct!

---

⬅️ Previous: [R04 · Find the position](R04-find-the-position.md) · 📚 [All exercises](README.md) · Next: [T01 · Count a letter](T01-count-a-letter.md) ➡️
