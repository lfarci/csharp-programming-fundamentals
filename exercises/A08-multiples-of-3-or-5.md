# A08 · Multiples of 3 or 5

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 4b · Running result | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A03](A03-sum-even-values.md) | Custom · prepares [Project Euler #1](https://projecteuler.net/problem=1) |

## 🎯 Goal

Read N. Print the sum of all numbers **below** N that are multiples of 3 or 5.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `10`

```text
Sum: 23
```

**Example 2** — input: `20`

```text
Sum: 78
```

**Example 3** — input: `1`

```text
Sum: 0
```

## ⚠️ Edge cases to test

- 15 is a multiple of 3 **and** 5: count it once.
- "below N" → N itself is not included.

## 📏 Rules

- One loop, one `if` with `||`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Below 10: 3, 5, 6, 9 → 23. Write them on paper first.

</details>

<details><summary>Hint 2</summary>

Filter: `i % 3 == 0 || i % 5 == 0`.

</details>

<details><summary>Hint 3</summary>

"below N": `i < n`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Solve [Project Euler #1](https://projecteuler.net/problem=1) (N = 1000).

## 🔑 Solution

Only after a real try: [A08-multiples-of-3-or-5](../solutions/A08-multiples-of-3-or-5.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
