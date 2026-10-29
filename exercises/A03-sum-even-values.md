🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A03

# A03 · Sum of the even numbers

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐ | 4b · Running result | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md) | Custom |

## 🎯 Goal

Give back the sum of the even numbers from 1 to n.

## ▶️ Start and check

```bash
./ex start A03     # creates practice/A03_SumEvenValues.cs (never overwrites your work)
./ex check A03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfEvens(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfEvens(6)` | `12` |
| `SumOfEvens(7)` | `12` |
| `SumOfEvens(1)` | `0` |
| `SumOfEvens(10)` | `30` |

## ⚠️ Edge cases to test

- N = 1 → 0.

## 📏 Rules

- Loop + `if` + accumulator.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Same loop as A02 (loop + `if (i % 2 == 0)`).

</details>

<details><summary>Hint 2</summary>

The box is `sum`, not `count`: inside the `if`, write `sum += i;` instead of `count++;`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the sum of the even numbers AND the sum of the odd numbers with **one** loop.

## 🔑 Solution

Only after a real try: [open the solution for A03](../solutions/A03_SumEvenValues.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A12 · Fix the bugs: count multiples of 7](A12-fix-count-multiples-of-7.md) · 📚 [All exercises](README.md) · Next: [A04 · Factorial](A04-factorial.md) ➡️
