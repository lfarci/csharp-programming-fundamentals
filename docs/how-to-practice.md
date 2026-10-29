🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › How to practice

# How to practice

For each new recipe, go through these 5 stages, in order:

1. **Predict:** look at a tiny piece of code. Say what it prints **before** you run it.
2. **Trace:** fill a table with the value of each variable, turn after turn.
3. **Write:** solve an easy exercise from a blank file.
4. **Change:** change one rule (for example, count only the even values).
5. **Recognize:** take a mixed exercise and find which recipes it needs.

This is close to the PRIMM method used in schools: *Predict, Run, Investigate, Modify, Make*.

Want the deeper "why"? Read [From a problem statement to an algorithm](problem-solving.md).

## Before coding

Write down:

- **Input:** what do I start with?
- **Output:** what exactly must I show?
- **Example:** can I solve a tiny case by hand?
- **Boxes:** which values must I remember?
- **Repeat:** what repeats, and when does it stop?
- **Check:** what result do I expect for a small example and for an edge case?

## A session

About 40 minutes: **5 min** recall what you did last time · **10 min** trace on paper · **20 min** code alone · **5 min** explain your code out loud.

## Asking for help

Ask for **one hint** at a time. A good helper asks you questions, gives you a smaller example, or fills a trace table with you. A good helper does **not** write the code for you.

## Drill sets

A pattern sticks when you use it **many times in a row**, with quick feedback. That is what drill sets are for.

- Pick **one** drill set in the [exercise inventory](../exercises/README.md#-drill-sets-same-pattern-many-times) (for example the counter-loop drill).
- Do 3 to 5 of its exercises in one short session, in order. Run `./ex check` after each one.
- Each drill changes only a small detail (count by 3, then by 5). Say the recipe's subgoals out loud each time.
- Next session, start with the last one you did, then continue. Mix in an older drill set now and then.
- When the set feels boring, you are ready: do the mastery check of the last exercise.

## When is a recipe "ready"?

When you solve **two** variations without help, and one of them on **another day**. Not yet? Repeat with smaller inputs, or go back one exercise. Tick it in your [progress checklist](progress-checklist.md).

## Rules for the first weeks

Write simple code: variables, `if` and loops. No LINQ, no recursion, no clever formulas, no ready-made array helpers. The goal is to write the loop yourself.

## For the coach: 5 questions when she is stuck

Ask, don't tell:

1. What must the program **produce**? Show me on a tiny example.
2. Which **recipe** does this look like? (Use the [decision diagram](../cookbook/README.md).)
3. What must you **remember** between two turns of the loop? What does it start at?
4. When should the loop **stop**?
5. What **changes** on each turn? Let's fill the trace table together for 2 turns.

A good exercise for the coach: give working code and ask her to **predict** its output before running it. It separates "reading loops" from "inventing an algorithm".

## Loop mastery checklist

- [ ] Trace a `for` loop on paper and predict its output (L01, L02)
- [ ] Write a loop from a blank file (L03, L04)
- [ ] Use an accumulator for a sum and a product (A01, A04)
- [ ] Combine an `if` with a loop (A02, A03, A08)
- [ ] Draw a shape with nested loops (G02, G05)
- [ ] Extract digits with `% 10` and `/ 10` (D03, D04)
- [ ] Explain and write Fibonacci alone (S01, S02)
- [ ] Solve a new mixed problem without step-by-step help (M01, P02, D06)

---

⬅️ [Home](../README.md) · [Progress checklist](progress-checklist.md) ➡️
