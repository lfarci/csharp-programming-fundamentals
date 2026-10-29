[Home](../README.md) › [Roadmap](../ROADMAP.md) › From a problem statement to an algorithm

# From a problem statement to an algorithm

An algorithm is a precise sequence of steps. You can design and test it on paper before choosing a programming language.

> Short on time? The practical, step-by-step version (trigger words → recipes, worksheet, unstuck techniques, worked Armstrong example) is [How to read an exercise](reading-an-exercise.md). This page explains the *why* in more depth.

## 1. Read to find what goes in and what comes out

Read once for the story. Then read again for the rules. Underline the **input**. Circle the **result** you must give. List the small words that change everything: “each”, “only”, “until”, “inclusive”, “at least”.

Careful: the word “each” does not always mean a loop.

Example: **Given a list of prices, report how many prices are above 10 and their total.**

| Question | Answer |
| --- | --- |
| What do I receive? | A list of prices |
| What must I produce? | Two numbers: how many prices are above 10, and their total |
| Which prices qualify? | Strictly greater than 10; 10 does not qualify |
| What is unclear? | Euros or cents? Can a price be negative? Ask if the exercise does not say. |
| What if none qualify? | Count 0, total 0 |

Say the task in your own words. Is the answer a **count** (how many) or a **total** (added up)? Is it printed once at the end, or on every turn?

## 2. Solve a tiny example by hand

Use prices 8, 12, 10, 15. Keep 12 and 15. That is **2** prices, and their total is **27**. Write this answer down before any code.

Ask: “What did I do, and what did I need to remember?” Here: look at a price, compare it with 10, keep a count and a total. The same algorithm should work for other lists.

## 3. Cut the problem into small jobs

| Small job | Rule | What to remember |
| --- | --- | --- |
| Decide whether to include a price | price > 10 | Current price |
| Count included prices | Add 1 for each match | count, initially 0 |
| Add included prices | Add the price for each match | total, initially 0 |
| Know when finished | No unvisited prices remain | Position in the list |

These are thinking steps. Each job does **not** need its own loop: count and total can share one loop. Start with fixed values in the code. Add reading from the keyboard once the idea works.

## 4. Draw the choices and the repeats

Shapes: rounded box = start or end. Rectangle = an action. Diamond = a yes/no question. Slanted box = input or output. Write “yes” and “no” on the two arrows of each question. Every repeat must go back to a question, and something must move toward the end.

```mermaid
flowchart TD
    accTitle: Count and total of prices above 10
    accDescr: Start, receive the prices, set count and total to 0. For each unvisited price: if it is above 10, add 1 to count and add the price to total. When no price is left, report count and total, then end.
    S([Start]) --> I[/Receive prices/]
    I --> A["count = 0; total = 0"]
    A --> B{"Any unvisited price?"}
    B -- Yes --> C["Take the next price"]
    C --> D{"price > 10?"}
    D -- Yes --> E["Increase count and add price to total"]
    D -- No --> B
    E --> B
    B -- No --> O[/Report count and total/]
    O --> Z([End])
```

The diagram shows the idea, not C# code. A simple calculation only needs actions. A choice needs a question. A repeat needs an arrow going back. Not every exercise needs a loop.

## 5. Write the steps in plain words

```text
count ← 0
total ← 0
for each price:
    if price > 10:
        count ← count + 1
        total ← total + price
report count and total
```

Here ← means “put a new value in the box”. Explain every step out loud, also what happens when the answer to the `if` is no.

## 6. Trace the steps like a computer

Follow the steps exactly as written. Do not fix them in your head because you know the answer.

| Step | Current price | price > 10? | count before → after | total before → after |
| --- | ---: | --- | --- | --- |
| Start | — | — | — → 0 | — → 0 |
| 1 | 8 | No | 0 → 0 | 0 → 0 |
| 2 | 12 | Yes | 0 → 1 | 0 → 12 |
| 3 | 10 | No | 1 → 1 | 12 → 12 |
| 4 | 15 | Yes | 1 → 2 | 12 → 27 |
| Finish | No items left | — | 2 → 2 | 27 → 27 |

**A sentence that stays true:** after each step, count and total are about the prices above 10 **seen so far**. If you can say such a sentence, you understand your loop.

In any trace, write every value that can change, the answer to each question, and what is printed. Write the start values, and the last test that stops the loop. Confused by the order of updates? Use one row per line of code.

## 7. Check boundaries, then write the C# code

| Input | Expected count | Expected total | What it checks |
| --- | ---: | ---: | --- |
| Empty list | 0 | 0 | The loop runs 0 times |
| 8, 10 | 0 | 0 | No match; 10 is not “above 10” |
| 12 | 1 | 12 | One match |
| 12, 15 | 2 | 27 | All match |

Only now write C#. Trace your code on the same input and compare with your paper. If they differ, find the **first** step where they differ.

## A reusable worksheet

Copy these prompts onto paper for any exercise. A fill-in markdown version is in [How to read an exercise § 4](reading-an-exercise.md#4-the-worksheet-copy-it).

1. In my own words, the task is…
2. What goes in, what comes out, the rules, what is unclear…
3. A tiny example and its expected answer…
4. The small jobs…
5. What I must remember, and its start value…
6. Steps or a diagram, with the questions and when it stops…
7. A trace, from the start values to the last test…
8. Boundary examples…
9. The C# code, then a check against my paper answer…

## Practice without syntax

- Explain how to choose the larger of two numbers, including equal numbers. Draw the choice and trace both branches.
- For a rectangle's width and height, describe how to calculate perimeter and area. Explain why no repetition is needed.
- Use the worked price example, then change “above 10” to “at least 10”. Predict which trace row changes before recalculating.
- Design a way to count spaces in a short text using the [string model](../cookbook/12-string-building.md). Write the trace before code.

## For the coach

See [the 5 questions when she is stuck](how-to-practice.md#for-the-coach-5-questions-when-she-is-stuck).

---

[How to read an exercise](reading-an-exercise.md) · [How to practice](how-to-practice.md)
