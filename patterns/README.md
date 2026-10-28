# Programming patterns: the cookbook

A **pattern** is a small reusable way of solving a common kind of problem. Learn the idea, trace the example, then practice a variation.

| Pattern | Recipe | Common use |
| --- | --- | --- |
| [Loop mechanics](loops.md) | initialize → test → do work → update | counting, stopping |
| [Counters and accumulators](accumulators.md) | start a running value → update repeatedly | totals, factorial, counting matches |
| [Digit extraction](digits.md) | remainder 10 → integer-divide by 10 | digit sum, Armstrong |
| [State updates](state-updates.md) | calculate next → shift current values | Fibonacci |
| [String traversal and building](strings.md) | visit character → decide → count or append | letters, spaces, filtered text |
| [Array traversal](arrays.md) | visit items and retain a running result | count, sum, maximum |

The recipe is a starting point, **not a formula to copy blindly**. Always ask: what changes after each iteration, and what must remain true?

## How to read a visual recipe

Start with the picture of the data and the result boxes. State what each box means. Trace a tiny example, including the first and last steps. Then read the C# translation and change one requirement.

Use tables for positions and snapshots, flowcharts for decisions and repetition, and trace tables for values over time. Choose the representation that answers your question.

For the general method of reading and decomposing an unfamiliar exercise, use [From a problem statement to an algorithm](../docs/problem-solving.md).
