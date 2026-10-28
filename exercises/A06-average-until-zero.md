# A06 · Average until zero

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4b · Running result | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L05](L05-until-zero.md), [A01](A01-sum-1-to-n.md) | Custom |

## 🎯 Goal

Read whole numbers until 0. Print their average. If no number was entered, print `No numbers.`

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `7`, `1`, `0`

```text
Average: 4
```

**Example 2** — input: `1`, `2`, `0`

```text
Average: 1.5
```

**Example 3** — input: `0`

```text
No numbers.
```

> ℹ️ On a computer set to French/Dutch, `1.5` may print as `1,5`. Both are correct.

## ⚠️ Edge cases to test

- First value 0 → never divide by 0!
- The average can have decimals.

## 📏 Rules

- Sentinel loop + two boxes (`sum`, `count`).
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Average = sum / count, so you need **both** boxes.

</details>

<details><summary>Hint 2</summary>

`(double)sum / count` keeps the decimals. `sum / count` with two `int`s does not.

</details>

<details><summary>Hint 3</summary>

Check `count == 0` **after** the loop.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Also print how many numbers were above the average. (Why is that hard without an array? → step 6!)

## 🔑 Solution

Only after a real try: [A06-average-until-zero](../solutions/A06-average-until-zero.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
