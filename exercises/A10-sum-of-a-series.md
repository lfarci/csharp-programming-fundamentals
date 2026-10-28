# A10 · Sum of a series

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 4b · Running result | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) | Custom |

## 🎯 Goal

Read N. Print the sum 1 + 1/2 + 1/3 + … + 1/N with 4 decimals.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `1`

```text
Sum: 1.0000
```

**Example 2** — input: `2`

```text
Sum: 1.5000
```

**Example 3** — input: `4`

```text
Sum: 2.0833
```

> ℹ️ On a French/Dutch computer the output is `2,0833`. That is fine.

## ⚠️ Edge cases to test

- `1 / 2` with two `int`s is **0**! Use `1.0 / i`.

## 📏 Rules

- A loop with a `double` box.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

The box is a `double` that starts at 0.

</details>

<details><summary>Hint 2</summary>

Each turn adds `1.0 / i`.

</details>

<details><summary>Hint 3</summary>

Print with 4 decimals: `{sum:F4}`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Compute 1 − 1/2 + 1/3 − 1/4 + … (the sign changes every turn). Hint: a `sign` box that flips with `sign = -sign`.

## 🔑 Solution

Only after a real try: [A10-sum-of-a-series](../solutions/A10-sum-of-a-series.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
