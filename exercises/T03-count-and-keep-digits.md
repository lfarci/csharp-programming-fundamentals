# T03 · Count and keep the digits

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 6 · Arrays | [Build a string](../cookbook/12-string-building.md), [Accumulator](../cookbook/02-accumulator.md) | [T02](T02-remove-spaces.md) | Custom |

## 🎯 Goal

Read a text. Count its digit characters and build a string with only those digits, in order.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `a1 b2!`

```text
Digits: 2
Kept: 12
```

**Example 2** — input: `abc`

```text
Digits: 0
Kept: 
```

## ⚠️ Edge cases to test

- No digit → 0 and empty text.

## 📏 Rules

- One loop, two boxes. `char.IsDigit(c)` or `c >= '0' && c <= '9'`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Two boxes: `count = 0` and `kept = ""`.

</details>

<details><summary>Hint 2</summary>

Update **both** inside the same `if`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Also compute the **sum** of those digits (`c - '0'` turns `'7'` into 7).

## 🔑 Solution

Only after a real try: [T03-count-and-keep-digits](../solutions/T03-count-and-keep-digits.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
