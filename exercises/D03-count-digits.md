# D03 · Count the digits

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D02](D02-remove-last-digit.md), [L05](L05-until-zero.md) | Custom |

## 🎯 Goal

Read N ≥ 0. Print how many digits it has.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `352`

```text
Digits: 3
```

**Example 2** — input: `0`

```text
Digits: 1
```

**Example 3** — input: `1000`

```text
Digits: 4
```

## ⚠️ Edge cases to test

- **0 has 1 digit** (a plain `while (n > 0)` loop says 0).

## 📏 Rules

- A loop. No `ToString().Length`, no `Math.Log10`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

How many times can you remove the last digit before the number becomes 0?

</details>

<details><summary>Hint 2</summary>

Trace 352 → 35 → 3 → 0: three removals.

</details>

<details><summary>Hint 3</summary>

For 0: a `do … while` runs at least once, so it counts 1.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count how many digits of N are even.

## 🔑 Solution

Only after a real try: [D03-count-digits](../solutions/D03-count-digits.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
