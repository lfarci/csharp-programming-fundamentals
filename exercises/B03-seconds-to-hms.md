# B03 · Seconds to hours, minutes, seconds

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 2 · Variables & expressions | — | [B02](B02-rectangle-calculator.md) | Custom |

## 🎯 Goal

Read a number of seconds. Print it as hours, minutes and seconds. This trains `/` and `%`, the key tools of the digit recipe later.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3725`

```text
1 h 2 min 5 s
```

**Example 2** — input: `59`

```text
0 h 0 min 59 s
```

**Example 3** — input: `7200`

```text
2 h 0 min 0 s
```

## ⚠️ Edge cases to test

- 0 seconds → `0 h 0 min 0 s`.

## 📏 Rules

- No loop, no `if`. Only `/` and `%` on `int`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

1 hour = 3600 seconds. `3725 / 3600` is 1 (integer division drops the rest).

</details>

<details><summary>Hint 2</summary>

What is left after the hours? `3725 % 3600` = 125.

</details>

<details><summary>Hint 3</summary>

Then do the same with 60 on what is left: 125 / 60 = 2 minutes, 125 % 60 = 5 seconds.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Turn a number of days into weeks and days (`17` → `2 weeks 3 days`).

## 🔑 Solution

Only after a real try: [B03-seconds-to-hms](../solutions/B03-seconds-to-hms.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
