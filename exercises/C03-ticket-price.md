# C03 · Ticket price

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 3 · Conditions | — | [C01](C01-even-or-odd.md) | Custom |

## 🎯 Goal

A cinema ticket costs 5 for children under 12, 7 for people aged 65 or more, and 10 for everyone else. Read an age and print the price.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `11`

```text
Price: 5
```

**Example 2** — input: `12`

```text
Price: 10
```

**Example 3** — input: `64`

```text
Price: 10
```

**Example 4** — input: `65`

```text
Price: 7
```

## ⚠️ Edge cases to test

- The boundaries 11/12 and 64/65: test them all!

## 📏 Rules

- Use `if` / `else if` / `else`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Three categories → three branches.

</details>

<details><summary>Hint 2</summary>

"under 12" means `age < 12`. "65 or more" means `age >= 65`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Add a rule: on Wednesday (ask the day as a number 1-7) everybody pays 6.

## 🔑 Solution

Only after a real try: [C03-ticket-price](../solutions/C03-ticket-price.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
