# L05 · Until zero

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4a · Repeat & count | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L03](L03-count-up-and-down.md) | Custom |

## 🎯 Goal

Read whole numbers one by one. Stop when the user types 0. Print how many **non-zero** numbers were entered.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`, `-2`, `8`, `0`

```text
You entered 3 numbers.
```

**Example 2** — input: `0`

```text
You entered 0 numbers.
```

## ⚠️ Edge cases to test

- The first number is already 0.
- Negative numbers count too.

## 📏 Rules

- You do not know how many numbers will come: no `for`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

This is the [sentinel loop](../cookbook/10-sentinel-loop.md). 0 is the sentinel.

</details>

<details><summary>Hint 2</summary>

`while (true) { read; if (value == 0) break; count++; }`

</details>

<details><summary>Hint 3</summary>

Do not count the 0 itself.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Also print how many of the numbers were negative.

## 🔑 Solution

Only after a real try: [L05-until-zero](../solutions/L05-until-zero.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
