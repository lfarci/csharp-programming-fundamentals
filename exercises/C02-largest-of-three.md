🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › C02

# C02 · Largest of three

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 3 · Conditions | [Min/max](../cookbook/04-min-max.md) | [C01](C01-even-or-odd.md) | Custom |

## 🎯 Goal

Give back the largest of the three numbers.

## ▶️ Start and check

```bash
./ex start C02     # creates practice/C02_LargestOfThree.cs (never overwrites your work)
./ex check C02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int Largest(int a, int b, int c)`: input = a, an int (whole number), b, an int (whole number), c, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Largest(3, 9, 5)` | `9` |
| `Largest(-1, -7, -3)` | `-1` |
| `Largest(4, 4, 2)` | `4` |
| `Largest(1, 2, 8)` | `8` |

## ⚠️ Edge cases to test

- Two equal values.
- All negative values.

## 📏 Rules

- No `Math.Max`. Use `if`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

You can keep a box `largest` that starts with the first number.

</details>

<details><summary>Hint 2</summary>

Compare the second number with `largest`. If bigger, replace. Same for the third.

</details>

<details><summary>Hint 3</summary>

This is the [min/max recipe](../cookbook/04-min-max.md) without a loop!

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the smallest of four numbers.

## 🔑 Solution

Only after a real try: [open the solution for C02](../solutions/C02_LargestOfThree.cs). Your solution can be different and still correct!

---

⬅️ Previous: [C01 · Even or odd](C01-even-or-odd.md) · 📚 [All exercises](README.md) · Next: [C03 · Ticket price](C03-ticket-price.md) ➡️
