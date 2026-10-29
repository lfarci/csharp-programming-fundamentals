🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › N01

# N01 · Armstrong with methods

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 10 · Methods | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [M02](M02-armstrong-numbers-in-a-range.md) | Custom |

## 🎯 Goal

Rewrite M02 with three small methods: `CountDigits(int n)`, `Power(int b, int e)`, `IsArmstrong(int n)`. The main code only reads the bounds and loops.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `100`, `999`

```text
153 370 371 407
```

## ⚠️ Edge cases to test

- `CountDigits(0)` must return 1.

## 📏 Rules

- Each method does **one** recipe. No `Math.Pow`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

`static int CountDigits(int n) { ... return digits; }`

</details>

<details><summary>Hint 2</summary>

`IsArmstrong` calls the two others and returns a `bool`.

</details>

<details><summary>Hint 3</summary>

Test each method alone first: `Console.WriteLine(Power(3, 4));` → 81.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Add `IsPalindrome(int n)` and print the numbers in the range that are both (hint: 1–9).

## 🔑 Solution

Only after a real try: [open the solution for N01](../solutions/N01-armstrong-with-methods.cs). Your solution can be different and still correct!

---

⬅️ Previous: [K01 · Shopping list](K01-shopping-list.md) · 📚 [All exercises](README.md)
