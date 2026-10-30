[Home](../../README.md) › [Projects](README.md) › What should I wear?

# What should I wear?

<p class="project-meta">Learn something real · Level: Easy · Effort: 1 to 2 hours</p>

**Convert temperatures, feel the wind chill and get outfit advice from your own program.**

Is 50 °F warm? What does 5 °C *feel* like with a strong wind? Build a little assistant that converts temperatures, computes the wind chill the way weather services do, and tells you what to wear.

## A sample run

```text
=== WHAT SHOULD I WEAR? ===
Temperature: 41
Unit (C or F): F
41 °F is 5.0 °C.
Wind speed (km/h): 30
With the wind it feels like 0.1 °C. Brrr.
Rain? (y/n) y

Your outfit:
 - winter coat and scarf
 - gloves (it feels like 0!)
 - umbrella or rain jacket
Convert another? (y/n) n
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- the Celsius and Fahrenheit scales and the formula between them
- the wind chill: why wind makes cold feel colder
- choosing among ranges with `if` / `else if`
- methods that compute a `double`

**Themes used:** [Basics](../themes/basics.md), [Loops](../themes/loops.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [B02 · Rectangle calculator](../exercises/B02-rectangle-calculator.md), [C03 · Ticket price](../exercises/C03-ticket-price.md), [C04 · Grade from a score](../exercises/C04-grade-from-a-score.md), [L07 · Ask until valid](../exercises/L07-ask-until-valid.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **C to F.** Read a temperature in °C and print it in °F: F = C × 9 / 5 + 32.
2. **Both ways.** Ask for the unit (`C` or `F`) and convert in the right direction; refuse anything else.
3. **Methods.** `double ToFahrenheit(double c)` and `double ToCelsius(double f)`. Check: 100 °C is 212 °F, -40 is the same in both.
4. **Outfit.** From the temperature in °C: below 0, 0 to 10, 10 to 18, 18 to 25, above 25. One piece of advice per range.
5. **Wind chill.** Ask the wind speed and compute the *feels like* temperature (formula in the hints). Base the outfit on it.
6. **Rain and repeat.** Add the rain question, then a loop: `Convert another?`.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Conversion table:** print -20 to 40 °C in steps of 5 next to °F, as a neat table ([number formats](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings)).
- **Kelvin:** add the scale scientists use (K = C + 273.15) and refuse temperatures below absolute zero.
- **Heat index:** for hot days, humidity makes heat feel worse. Look up the simple heat index formula and add it.
- **A week of outfits:** read 7 days and plan the week, then count how many days need an umbrella.
- **Colours:** blue advice when cold, orange when hot ([`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor)).

## Hints (open one at a time)

<details><summary>Hint 1: Decimals</summary>

Use `double` and `double.TryParse`. `9 / 5` with whole numbers is 1! Write `9.0 / 5`.

</details>

<details><summary>Hint 2: Ranges</summary>

Check from the coldest up: `if (t < 0) ... else if (t < 10) ... else if (t < 18) ...`. Each `else if` already knows the previous tests were false, like in [C04](../exercises/C04-grade-from-a-score.md).

</details>

<details><summary>Hint 3: The wind chill formula</summary>

With T in °C and V in km/h (valid when T ≤ 10 and V > 4.8): feels = 13.12 + 0.6215 × T − 11.37 × V^0.16 + 0.3965 × T × V^0.16. `Math.Pow(v, 0.16)` computes V^0.16. Otherwise, feels = T.

</details>

<details><summary>Hint 4: Rounding</summary>

Print `{feels:0.0}` for one decimal.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Expense tracker](expense-tracker.md)
