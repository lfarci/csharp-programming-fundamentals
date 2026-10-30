[Home](../../README.md) › [Projects](README.md) › Expense tracker

# Expense tracker

**Goal:** a small menu program to note what you spend. Add an expense (a label and an amount), list them, see the total and the biggest one, and keep them in a file so they are still there next time.

**Themes used:** [Loops](../themes/loops.md) (sentinel loop, min/max), [Arrays, text and lists](../themes/arrays.md) (lists, files), [Methods and errors](../themes/methods.md).
**Exercises that prepare it:** [A09 Min and max until zero](../exercises/A09-min-and-max-until-zero.md), [K01 Shopping list](../exercises/K01-shopping-list.md), [F01 Save numbers to a file](../exercises/F01-numbers-file.md), [E02 Parse or zero](../exercises/E02-parse-or-zero.md).

```text
1) Add  2) List  3) Total  4) Quit
Choice: 1
Label: lunch
Amount: 12.50
Choice: 1
Label: bus
Amount: 2.10
Choice: 2
1. lunch  12.50
2. bus     2.10
Choice: 3
Total: 14.60 (2 expenses, biggest: lunch 12.50)
Choice: 4
Saved 2 expenses.
```

## Milestones

- [ ] **1. Menu loop.** Print the menu and read a choice until the user types `4`. For now each choice just prints its name.
- [ ] **2. Add and list.** Keep the labels in a `List<string>` and the amounts in a `List<double>` (same position = same expense). List them numbered.
- [ ] **3. Total and biggest.** One loop over the amounts: an accumulator for the total and a min/max box for the biggest one.
- [ ] **4. Safe amounts.** `abc`, an empty line or a negative amount is refused with a message, and the program asks again.
- [ ] **5. Save and load.** On quit, write one line per expense, like `lunch;12.50`, to `expenses.txt`. At start, read the file back if it exists.

## Stretch goals

- Add a category to each expense (`food`, `transport`…) and print the total per category.
- Delete an expense by its number (check that the number exists).
- Print a tiny bar chart: one `#` per euro, next to each expense.

## Hints (open one at a time)

<details><summary>Hint 1: one method per menu choice</summary>

`AddExpense(labels, amounts)`, `ListExpenses(labels, amounts)`, `PrintTotal(amounts)`. The menu loop in `Main` only reads the choice and calls the right method.

</details>

<details><summary>Hint 2: reading an amount</summary>

Write `double ReadAmount()` with a loop: `double.TryParse(text, out double amount) && amount >= 0`. Same idea as [L07](../exercises/L07-ask-until-valid.md).

</details>

<details><summary>Hint 3: the file</summary>

`File.Exists("expenses.txt")`, then `File.ReadAllLines`. Split each line with `line.Split(';')`: part `[0]` is the label, part `[1]` the amount. To save, build a `List<string>` of lines and call `File.WriteAllLines`.

</details>

<details><summary>Hint 4: decimals</summary>

Print amounts with 2 decimals: `amount.ToString("0.00")`, or `{amount,6:0.00}` inside `$"..."` to align them in a column.

</details>

There is no full solution: if your program does what the example shows, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Text quiz](text-quiz.md)
