# L06 · Even numbers

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [L03](L03-count-up-and-down.md) | Custom |

## 🎯 Goal

Read N. Print all even numbers from 2 to N on one line.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `9`

```text
2 4 6 8
```

**Example 2** — input: `10`

```text
2 4 6 8 10
```

**Example 3** — input: `1`

```text
(nothing is printed)
```

## ⚠️ Edge cases to test

- N = 1 → nothing is printed.
- N is even → N is printed too.

## 📏 Rules

- Write it **two ways**: (1) step `i += 2`, (2) step `i++` with an `if`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Way 1: start at 2, step 2.

</details>

<details><summary>Hint 2</summary>

Way 2: test every number with `i % 2 == 0`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the multiples of 7 between 1 and N.

## 🔑 Solution

Only after a real try: [L06-even-numbers](../solutions/L06-even-numbers.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
