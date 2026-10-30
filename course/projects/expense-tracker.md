[Home](../../README.md) › [Projects](README.md) › Expense tracker

# Expense tracker

<p class="project-meta">Learn something real · Level: Medium · Effort: 3 to 5 hours</p>

**Where does your money go? Track expenses by category and see your budget melt.**

Every budget app does the same few things: record spending, group it by category, compare it with a budget and warn you. Build your own, and you will understand both lists and the 50/30/20 budgeting rule.

## A sample run

```text
=== MY BUDGET === monthly budget: 400.00
1) Add  2) List  3) Report  4) Quit
Choice: 1
What: pizza      Amount: 12.50   Category (food, fun, transport): food
Choice: 1
What: cinema     Amount: 11.00   Category: fun
Choice: 3
food       12.50  ##
fun        11.00  ##
transport   0.00
Total 23.50 of 400.00 (6%). Biggest: pizza 12.50
You can still spend 12.55 per day this month.
Choice: 4
Saved 2 expenses to expenses.txt. See you!
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- parallel lists: label, amount and category at the same position
- totals per category with a loop and an `if`
- percentages and a daily budget
- saving and loading a file

**Themes used:** [Loops](../themes/loops.md), [Arrays, text and lists](../themes/arrays.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [A09 · Min and max until zero](../exercises/A09-min-and-max-until-zero.md), [K01 · Shopping list](../exercises/K01-shopping-list.md), [F01 · Save numbers to a file](../exercises/F01-numbers-file.md), [E02 · Parse or zero](../exercises/E02-parse-or-zero.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **Menu loop.** Print the menu and read a choice until `4`.
2. **Add and list.** Keep labels in a `List<string>` and amounts in a `List<double>`; list them numbered.
3. **Total and biggest.** One loop: an accumulator and a max box.
4. **Safe amounts.** Refuse text, empty lines and negative amounts.
5. **Categories.** Add a category to each expense and print the total per category.
6. **Budget.** Ask the monthly budget once; print the percentage spent and a warning above 80 %.
7. **Save and load.** Write `pizza;12.50;food` lines to `expenses.txt` on quit, read them back at start.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Bar chart:** one `#` per 5 euros next to each category.
- **Delete:** remove an expense by its number (check that it exists).
- **Daily budget:** with [`DateTime`](https://learn.microsoft.com/en-us/dotnet/api/system.datetime), compute the days left in the month and how much you can spend per day.
- **50/30/20 rule:** classify categories as needs, wants or savings and compare with 50 %, 30 % and 20 % of the income.
- **Colours:** red when over budget ([`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor)).

## Hints (open one at a time)

<details><summary>Hint 1: One method per choice</summary>

`AddExpense(...)`, `ListExpenses(...)`, `PrintReport(...)`. The menu loop only reads the choice and calls a method.

</details>

<details><summary>Hint 2: Reading an amount</summary>

`double ReadAmount()` loops until `double.TryParse(text, out double a) && a >= 0`, like [L07](../exercises/L07-ask-until-valid.md).

</details>

<details><summary>Hint 3: Total per category</summary>

Loop over the category names; for each, an inner loop adds the amounts whose category matches. That is a [conditional accumulator](../cookbook/03-conditional-accumulator.md).

</details>

<details><summary>Hint 4: The file</summary>

`File.Exists`, `File.ReadAllLines`, then `line.Split(';')`: `[0]` label, `[1]` amount, `[2]` category.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Quiz show](text-quiz.md)
