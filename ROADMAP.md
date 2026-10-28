# Learning path

This is a **sequence of skills, not a calendar**. University assignments come first when due. Spend 20–40 minutes per session; repeat a stage until new variations can be solved independently.

| Stage | Patterns | Practice | Ready to move on when... |
| --- | --- | --- | --- |
| 0. Diagnose | loop trace, variables | L01–L02 | Can predict variable values on each iteration |
| 1. Loop mechanics | `for`, `while`, bounds | L03–L05 | Can write a terminating loop without copying |
| 2. Count & accumulate | counter, sum, running product, conditional accumulation | A01–A05 | Can explain why a total starts at 0 and a product at 1 |
| 3. Work with digits | remainder, integer division, repeated extraction | D01–D04 | Can process each digit of a positive integer |
| 4. Change state | previous/current/next | S01–S02 | Can trace Fibonacci without confusing updates |
| 5. Combine patterns | mixed problems | M01–M03 | Can plan an algorithm and choose patterns independently |
| 6. Arrays | traversal, counter, running maximum | R01–R03 | Can process an array with a loop |

**Current priority:** stages 0–2, then the digit and state patterns required by factorial, Fibonacci and Armstrong. Array practice can run alongside those once the first loop skills are stable.

## Connections to existing materials

- *The C# Player's Guide*, 5th edition, Level 11: **The Prototype** (p. 88) and **The Magic Cannon** (p. 89).
- Level 12: **The Replicator of D’To** (p. 94) and **The Laws of Freach** (p. 95).
- Project Euler [#1](https://projecteuler.net/problem=1): after conditional accumulation.
- Project Euler [#6](https://projecteuler.net/problem=6): after two accumulators.
- Project Euler [#2](https://projecteuler.net/problem=2): after Fibonacci state updates.
- Teacher factorial/Fibonacci/Armstrong problems: revisit as mixed assessments once their prerequisites are mastered.

Use [the exercise inventory](exercises/README.md) to pick the next problem. Do not treat the sequence as a race.

## A parallel strand: learning to think through a problem

At every stage, practice the [problem-solving method](docs/problem-solving.md): restate the contract, solve a small example, split responsibilities, draw decisions, trace, check boundaries, then translate to C#. Include straight calculations and simple choices as well as loops.

Alongside array traversal, use [strings](patterns/strings.md) and T01–T03 to transfer the same ideas to characters. Readiness means explaining why a recipe fits and adapting its state/update rule, as well as reproducing its syntax.
