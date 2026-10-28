# How to practice

For each new pattern:

1. **Predict:** Look at a tiny example and state what it prints without running it.
2. **Trace:** Make a table showing the loop variable and other variables *before and after* each iteration.
3. **Implement:** Write an easy exercise from scratch.
4. **Adapt:** Change a requirement, such as counting even values instead of all values.
5. **Recognize:** Try an unlabeled mixed challenge and decide which patterns apply.

Use [From a problem statement to an algorithm](problem-solving.md) for a worked example, diagram conventions and a reusable paper worksheet.

## Before coding

Write down:

- **Input:** What information do I start with?
- **Output:** What exactly must I produce?
- **Example:** Can I solve a tiny case by hand?
- **State:** What values must I remember?
- **Repetition:** What action repeats, and when does it stop?
- **Check:** What result should I expect for a small example or an edge case?

## Asking for help

Ask for **one hint** at a time. The helper should ask questions, offer a smaller example, or suggest a trace table before showing code. Do not replace the learner's solution with a more advanced version.

A practical 35-minute session: 5 minutes recall, 10 minutes paper tracing, 15 minutes independent coding, 5 minutes explaining the solution.

## Progress rule

A pattern is *ready* when the learner can solve two variations without step-by-step prompts, including one attempted on a different day. If not, repeat with easier inputs or one smaller building block. Keep progress in the existing book tracker for book challenges; this repository does not duplicate that tracker.

## Constraints for the first stages

Use simple top-level console code with variables, conditionals and loops. No LINQ, recursion, clever formulas, array helpers, or complicated abstractions to bypass the intended exercise. Where input is requested, a fixed test value is fine while learning the algorithm.

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
