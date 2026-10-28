# A03 · Sum of the even numbers

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐ | 4b · Running result | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md) | Custom |

## 🎯 Goal

Read N. Print the sum of the even numbers from 1 to N.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `6`

```text
Sum: 12
```

**Example 2** — input: `7`

```text
Sum: 12
```

**Example 3** — input: `1`

```text
Sum: 0
```

## ⚠️ Edge cases to test

- N = 1 → 0.

## 📏 Rules

- Loop + `if` + accumulator.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Same loop as A02, but the box gets `+= i` instead of `++`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the sum of the even numbers AND the sum of the odd numbers with **one** loop.

## 🔑 Solution

Only after a real try: [A03-sum-even-values](../solutions/A03-sum-even-values.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
