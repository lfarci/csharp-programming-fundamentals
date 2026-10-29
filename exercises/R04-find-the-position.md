🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › R04

# R04 · Find the position

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md), [Flag/search](../cookbook/05-flag-search.md) | [R03](R03-count-matches.md) | Custom |

## 🎯 Goal

Read numbers into an array, then a target. Print the **first** index where the target is, or `Not found`. Input format: first how many numbers, then one number per line. Fill the array with a loop (see [array traversal](../cookbook/11-array-traversal.md)).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `7`, `3`, `9`, `3`, `3`

```text
First position: 1
```

**Example 2** — input: `4`, `7`, `3`, `9`, `3`, `8`

```text
Not found
```

## ⚠️ Edge cases to test

- Target at index 0 (0 is a valid position: use -1 for "not found").
- Several matches → the first.

## 📏 Rules

- No `Array.IndexOf`. Use `break`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Box `int index = -1;` (means not found).

</details>

<details><summary>Hint 2</summary>

When found: `index = i; break;`

</details>

<details><summary>Hint 3</summary>

Decide what to print **after** the loop.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the **last** position instead (hint: loop backwards).

## 🔑 Solution

Only after a real try: [open the solution for R04](../solutions/R04-find-the-position.cs). Your solution can be different and still correct!

---

⬅️ Previous: [R03 · Count matches in an array](R03-count-matches.md) · 📚 [All exercises](README.md) · Next: [R05 · Reverse an array](R05-reverse-an-array.md) ➡️
