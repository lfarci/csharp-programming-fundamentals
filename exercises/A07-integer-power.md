🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A07

# A07 · Integer power

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4b · Running result | [Accumulator](../cookbook/02-accumulator.md) | [A04](A04-factorial.md) | Custom |

## 🎯 Goal

Read a base and an exponent (exponent ≥ 0). Print base^exponent using a loop.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`, `4`

```text
3^4 = 81
```

**Example 2** — input: `2`, `10`

```text
2^10 = 1024
```

**Example 3** — input: `5`, `0`

```text
5^0 = 1
```

## ⚠️ Edge cases to test

- Exponent 0 → 1.
- Base 0 → 0 (except 0^0 = 1 by our convention).

## 📏 Rules

- No `Math.Pow`. A loop with a product box.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

3^4 = 3 × 3 × 3 × 3: multiply by the **same** number, exponent times.

</details>

<details><summary>Hint 2</summary>

Difference with factorial: you multiply by `baseValue`, not by `i`.

</details>

<details><summary>Hint 3</summary>

`for (int i = 0; i < exponent; i++) result *= baseValue;`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print all powers of 2 from 2^0 to 2^N, with only one multiplication per turn.

## 🔑 Solution

Only after a real try: [open the solution for A07](../solutions/A07-integer-power.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A06 · Average until zero](A06-average-until-zero.md) · 📚 [All exercises](README.md) · Next: [A08 · Multiples of 3 or 5](A08-multiples-of-3-or-5.md) ➡️
