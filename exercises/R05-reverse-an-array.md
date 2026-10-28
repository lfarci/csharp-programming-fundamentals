# R05 · Reverse an array

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md) | [R01](R01-sum-an-array.md) | Custom |

## 🎯 Goal

Read numbers into an array. Build a **new** array with the values in reverse order, then print it on one line. Input format: first how many numbers, then one number per line. Fill the array with a loop (see [array traversal](../cookbook/11-array-traversal.md)).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `1`, `2`, `3`, `4`

```text
4 3 2 1
```

**Example 2** — input: `1`, `8`

```text
8
```

## ⚠️ Edge cases to test

- One element.
- Odd or even length.

## 📏 Rules

- No `Array.Reverse`. Write into the new array with an index.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

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

Only after a real try: [R05-reverse-an-array](../solutions/R05-reverse-an-array.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
