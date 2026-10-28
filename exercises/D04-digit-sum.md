# D04 · Sum of the digits

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D03](D03-count-digits.md) | Custom |

## 🎯 Goal

Read N ≥ 0. Print the sum of its digits.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `352`

```text
Digit sum: 10
```

**Example 2** — input: `0`

```text
Digit sum: 0
```

**Example 3** — input: `9999`

```text
Digit sum: 36
```

## ⚠️ Edge cases to test

- 0 → 0.

## 📏 Rules

- A loop with `% 10` and `/ 10`. No string.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Fill the trace table: `remaining`, `digit`, `sum`.

</details>

<details><summary>Hint 2</summary>

Three lines in the loop: take the digit, add it, remove it.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Repeat the digit sum until one digit is left (9875 → 29 → 11 → 2).

## 🔑 Solution

Only after a real try: [D04-digit-sum](../solutions/D04-digit-sum.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
