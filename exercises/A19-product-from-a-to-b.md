🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A19

# A19 · Product from a to b

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4b · Running result | [Accumulator](../cookbook/02-accumulator.md) | [A04](A04-factorial.md) | Custom |

## 🎯 Goal

Give back a × (a+1) × … × b. If `a` is bigger than `b`, give back 1.

## ▶️ Start and check

```bash
./ex start A19     # creates practice/A19_ProductFromAToB.cs (never overwrites your work)
./ex check A19     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long ProductFromTo(int a, int b)`: input = a, an int (whole number), b, an int (whole number); result = a long (big whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `ProductFromTo(2, 4)` | `24` |
| `ProductFromTo(3, 3)` | `3` |
| `ProductFromTo(1, 5)` | `120` |
| `ProductFromTo(5, 4)` | `1` |

## ⚠️ Edge cases to test

- `a` bigger than `b`: 1 (nothing was multiplied).

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Like A04: the box starts at 1.

</details>

<details><summary>Hint 2</summary>

The loop starts at `a`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Multiply only the even numbers from a to b.

## 🔑 Solution

Only after a real try: [open the solution for A19](../solutions/A19_ProductFromAToB.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A18 · Sum of cubes](A18-sum-of-cubes.md) · 📚 [All exercises](README.md) · Next: [A20 · Power of 2](A20-powers-of-2.md) ➡️
