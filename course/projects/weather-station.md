[Home](../../README.md) › [Projects](README.md) › Weather station

# Weather station

<p class="project-meta">Learn something real · Level: Medium · Effort: 3 to 4 hours</p>

**Turn a week of temperatures into stats, trends and an ASCII chart, like a meteorologist.**

Meteorologists do not just read a thermometer: they look for the minimum, the maximum, the average, the warmest day and the trend. Type a week of temperatures (or read them from a file) and your program writes the weather report.

## A sample run

```text
Temperature for Monday (°C): 12
Temperature for Tuesday (°C): 15
...
Temperature for Sunday (°C): 8

        WEEKLY WEATHER REPORT
Mon  12 °C | ############
Tue  15 °C | ###############
Wed  17 °C | ################# <- warmest
Thu  14 °C | ##############
Fri   9 °C | #########
Sat   7 °C | ####### <- coldest
Sun   8 °C | ########
Average 11.7 °C, range 10 degrees.
Biggest change: Thu -> Fri, 5 degrees colder.
Trend: getting colder. Take a coat this weekend!
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- min, max and average: the core of statistics
- the range and the biggest day-to-day change
- a bar chart made of characters
- what an average hides (and why weather reports give min and max too)

**Themes used:** [Loops](../themes/loops.md), [Arrays, text and lists](../themes/arrays.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [A06 · Average until zero](../exercises/A06-average-until-zero.md), [A09 · Min and max until zero](../exercises/A09-min-and-max-until-zero.md), [R01 · Sum of an array](../exercises/R01-sum-an-array.md), [R02 · Position of the largest](../exercises/R02-largest-in-an-array.md), [G09 · Rows of numbers](../exercises/G09-number-rows.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **Read the week.** 7 temperatures (whole degrees) into an `int[]`, with the day names in a `string[]`.
2. **Min, max, average.** One loop for each, or one loop for all three. Print the average with 1 decimal.
3. **Which day?** Not only the coldest temperature but the **day** it was: keep the index.
4. **The chart.** One line per day with one `#` per degree. Mark the warmest and coldest days.
5. **Change.** Find the biggest change between two days in a row and say if it got warmer or colder.
6. **Trend.** Compare the average of the first 3 days with the last 3 days: getting warmer, colder or stable. Finish with an advice line.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Negative degrees:** the chart cannot draw `-3` hashes. Shift the chart so the coldest day starts at 0, or draw `-` signs to the left of a middle line.
- **A month from a file:** read `temperatures.txt` (one number per line) with `File.ReadAllLines` and handle any number of days.
- **Celsius and Fahrenheit:** add a switch: F = C × 9 / 5 + 32. Print both in the report.
- **Heat wave alert:** 3 days or more in a row above 25 °C. Count the longest run.
- **Colours:** cold bars in blue, warm bars in red ([`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor)).

## Hints (open one at a time)

<details><summary>Hint 1: The average with decimals</summary>

Add up in an `int`, then divide as a `double`: `double average = (double)sum / days.Length;`, printed with `{average:0.0}`.

</details>

<details><summary>Hint 2: The warmest day</summary>

Keep the index, not the value: `int warmest = 0;` and in the loop `if (t[i] > t[warmest]) warmest = i;`. Same as [R02](../exercises/R02-largest-in-an-array.md).

</details>

<details><summary>Hint 3: Biggest change</summary>

Compare neighbours: loop from `i = 1` and look at `t[i] - t[i - 1]`. Keep the biggest absolute value (`Math.Abs`).

</details>

<details><summary>Hint 4: The bars</summary>

`new string('#', t[i])` makes a row of `#`, or write an inner loop like in [G09](../exercises/G09-number-rows.md).

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [What should I wear?](dress-for-the-weather.md)
