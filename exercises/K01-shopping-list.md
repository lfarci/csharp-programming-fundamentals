# K01 · Shopping list

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 9 · Collections | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Array traversal](../cookbook/11-array-traversal.md) | [R01](R01-sum-an-array.md), [L05](L05-until-zero.md) | Custom |

## 🎯 Goal

Read items until the user types `done`. Store them in a `List<string>`. Print them numbered, then the total.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `milk`, `eggs`, `bread`, `done`

```text
1. milk
2. eggs
3. bread
Total: 3 items
```

**Example 2** — input: `done`

```text
Total: 0 items
```

## ⚠️ Edge cases to test

- `done` right away.

## 📏 Rules

- `List<string>`, `Add`, `Count`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

`List<string> items = new List<string>();`

</details>

<details><summary>Hint 2</summary>

Sentinel loop with `"done"`.

</details>

<details><summary>Hint 3</summary>

Numbering: a `for` loop with `i + 1`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Do not add an item that is already in the list (`items.Contains(item)`).

## 🔑 Solution

Only after a real try: [K01-shopping-list](../solutions/K01-shopping-list.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
