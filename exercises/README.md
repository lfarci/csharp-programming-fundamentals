# Exercise inventory

Work in order within a stage. **Easy / Medium / Hard** reflects a true beginner's likely effort, not a formal grade. All custom prompts below are original. Use a simple C# console project of your choice; keep code solutions separate from this inventory.

## L — Loop mechanics

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| L01 | Trace a loop | Easy | Predict the output and make a trace table for `for (int i = 2; i <= 8; i += 2)` printing `i`. |
| L02 | Boundaries | Easy | Predict how many times loops with `i < 5` and `i <= 5` run, starting at 1 and increasing by 1. |
| L03 | Count up and down | Easy | Read positive N; print 1 to N, then N to 1. For N=4: 1,2,3,4 and 4,3,2,1. |
| L04 | Multiplication table | Easy | Read N; print N×1 through N×10. For N=3: 3, 6, …, 30. |
| L05 | Until zero | Medium | Repeatedly read integers; stop only when the user enters 0. Print how many **nonzero** integers were entered. |

## A — Counters and accumulators

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| A01 | Sum 1 to N | Easy | For N=5, output 15. Use a loop, not the arithmetic-series formula. |
| A02 | Count multiples of 3 | Easy | Count values from 1 to N inclusive divisible by 3. For N=10, output 3. |
| A03 | Sum even values | Easy | Sum even values from 1 to N inclusive. For N=6, output 12. |
| A04 | Factorial | Medium | Compute N! for 0 ≤ N ≤ 12 using a loop. For N=0, output 1; N=5, output 120. |
| A05 | Two accumulators | Medium | For 1 to N compute separately the sum of values and the sum of their squares. For N=3, outputs 6 and 14. |

## D — Digit manipulation

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| D01 | Last digit | Easy | Given nonnegative N, print `N % 10`. For 352, output 2. |
| D02 | Remove last digit | Easy | Given nonnegative N, print the result of integer division by 10. For 352, output 35. |
| D03 | Count digits | Medium | Count decimal digits of nonnegative N using division. For 0, output 1; for 352, output 3. |
| D04 | Digit sum | Medium | Add the decimal digits of nonnegative N. For 352, output 10; for 0, output 0. |

## S — Variable state

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| S01 | Trace updates | Medium | Starting with `a=1`, `b=2`, repeat three times: `next=a+b; a=b; b=next;`. Record all values after each iteration. |
| S02 | Fibonacci | Hard | Print the first N Fibonacci values, starting at 0, 1. For N=6: 0, 1, 1, 2, 3, 5. |

## R — Arrays

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| R01 | Sum an array | Easy | For `{4,9,2}`, output 15 using a loop. |
| R02 | Find largest | Easy | For `{-5,-2,-9}`, output -2; assume a nonempty array. |
| R03 | Count matches | Medium | For `{2,4,2,5,2}` and target 2, output 3. |

## M — Mixed assessments (do not reveal patterns ahead of time)

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| M01 | Multiples challenge | Medium | For integers below N, calculate the sum of values divisible by 3 or 5, counting each number only once. Try N=10 before [Project Euler #1](https://projecteuler.net/problem=1). |
| M02 | Number palindrome | Hard | Determine if a nonnegative integer reads the same forwards and backwards, without converting to text. For 1221: true; for 123: false. |
| M03 | Armstrong number | Hard | For a nonnegative integer, check whether it equals the sum of its digits each raised to the total digit count. For 153: true; for 154: false. First implement an integer-power loop; handle 0 explicitly. |

## External milestones

- *The C# Player's Guide*, 5th ed., Level 11: **The Prototype** (p. 88), **The Magic Cannon** (p. 89).
- Level 12: **The Replicator of D’To** (p. 94), **The Laws of Freach** (p. 95).
- [Project Euler #1](https://projecteuler.net/problem=1) after A03/M01; [#6](https://projecteuler.net/problem=6) after A05; [#2](https://projecteuler.net/problem=2) after S02.
- Teacher exercises: factorial, Fibonacci, Armstrong; compare exact requirements with the course sheets before marking them equivalent.

## When stuck

See [How to practice](../docs/how-to-practice.md) and the [pattern cookbook](../patterns/README.md). Work a smaller example on paper, trace variables, then request a hint. Do not start with an answer key.
