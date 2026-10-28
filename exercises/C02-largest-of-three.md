# C02 · Largest of three

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 3 · Conditions | [Min/max](../cookbook/04-min-max.md) | [C01](C01-even-or-odd.md) | Custom |

## 🎯 Goal

Read three whole numbers and print the largest one.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`, `9`, `5`

```text
Largest: 9
```

**Example 2** — input: `-1`, `-7`, `-3`

```text
Largest: -1
```

**Example 3** — input: `4`, `4`, `2`

```text
Largest: 4
```

## ⚠️ Edge cases to test

- Two equal values.
- All negative values.

## 📏 Rules

- No `Math.Max`. Use `if`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

You can keep a box `largest` that starts with the first number.

</details>

<details><summary>Hint 2</summary>

Compare the second number with `largest`. If bigger, replace. Same for the third.

</details>

<details><summary>Hint 3</summary>

This is the [min/max recipe](../cookbook/04-min-max.md) without a loop!

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the smallest of four numbers.

## 🔑 Solution

Only after a real try: [C02-largest-of-three](../solutions/C02-largest-of-three.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
