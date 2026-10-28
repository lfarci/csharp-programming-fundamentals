# Exercise inventory

Work in order within a stage. **Easy / Medium / Hard** reflects a true beginner's likely effort, not a formal grade. All custom prompts below are original. Use a simple C# console project of your choice; keep code solutions separate from this inventory.

## B — First programs and values

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| B01 | First change | Easy | Run a console program printing your name and a second line. Change the text; deliberately remove a semicolon, read the compiler error, and repair it. |
| B02 | Receipt | Easy | With decimal price 2.50 and integer quantity 3, print the total 7.50. Change the quantity and predict the new result first. |
| B03 | Temperature and division | Easy | Convert Celsius to Fahrenheit with fractional arithmetic: 0 → 32, 100 → 212. Separately predict and compare `5 / 2` and `5.0 / 2`. |

## C — Decisions

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| C01 | Even or odd | Easy | Classify an integer. Check 0, 7, 8, and -3. |
| C02 | Ticket price | Easy | Ages 0–11 pay 5, 12–64 pay 10, and 65+ pay 7. Reject negative ages. Test 11, 12, 64, and 65. |
| C03 | Valid score | Easy | Accept scores from 0 to 100 inclusive; reject other integers. Test -1, 0, 100, and 101. Explain the combined condition. |

## L — Loop mechanics

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| L01 | Trace a loop | Easy | Predict the output and make a trace table for `for (int i = 2; i <= 8; i += 2)` printing `i`. |
| L02 | Boundaries | Easy | Predict how many times loops with `i < 5` and `i <= 5` run, starting at 1 and increasing by 1. |
| L03 | Count up and down | Easy | Read positive N; print 1 to N, then N to 1. For N=4: 1,2,3,4 and 4,3,2,1. |
| L04 | Multiplication table | Easy | Read N; print N×1 through N×10. For N=3: 3, 6, …, 30. |
| L05 | Until zero | Medium | Repeatedly read integers; stop only when the user enters 0. Print how many **nonzero** integers were entered. |
| L06 | Ask again | Medium | Read text until `int.TryParse` succeeds and the integer is 1–10 inclusive. Test invalid text, 0, then 4. Explain when `while` or `do` / `while` is appropriate. |

## A — Counters and accumulators

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| A01 | Sum 1 to N | Easy | For N=5, output 15. Use a loop, not the arithmetic-series formula. |
| A02 | Count multiples of 3 | Easy | Count values from 1 to N inclusive divisible by 3. For N=10, output 3. |
| A03 | Sum even values | Easy | Sum even values from 1 to N inclusive. For N=6, output 12. |
| A04 | Factorial | Medium | Compute N! for 0 ≤ N ≤ 12 using a loop. For N=0, output 1; N=5, output 120. |
| A05 | Two accumulators | Medium | For 1 to N compute separately the sum of values and the sum of their squares. For N=3, outputs 6 and 14. |
| A06 | Average until zero | Medium | Read integers until 0. Exclude 0; report count, sum, and fractional average. For 2,3,0: count 2, sum 5, average 2.5. For immediate 0, report no values instead of dividing by zero. |

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
| S02 | Fibonacci | Hard | For 0 ≤ N ≤ 20, print the first N Fibonacci values, starting at 0, 1; N=0 prints none. For N=6: 0, 1, 1, 2, 3, 5. |

## R — Arrays

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| R01 | Sum an array | Easy | For `{4,9,2}`, output 15 using a loop. |
| R02 | Find largest | Easy | For `{-5,-2,-9}`, output -2; assume a nonempty array. |
| R03 | Count matches | Medium | For `{2,4,2,5,2}` and target 2, output 3. |
| R04 | First match | Medium | Find the first index of a target, or -1 when absent. For `{4,9,4}` and 4, output 0; check an empty array. |
| R05 | Modify by position | Medium | Double each value in `{2,-1,0}` using an indexed loop, producing `{4,-2,0}`. Explain why the index matters. |
| R06 | Count a character | Easy | Count lowercase `a` characters in a string with a loop. For `banana`, output 3; for an empty string, output 0. |

## G — Drawings and grids

Use positive dimensions from 1 to 10. Print directly for G01–G04; no stored grid is needed.

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| G01 | Rectangle | Easy | Print height rows of width stars. For height 2 and width 3, print 2 lines of 3 stars. Also test 1×1. |
| G02 | Triangle | Medium | Print height rows; the first has 1 star, the next 2, and so on. For height 4, the last row has 4 stars. |
| G03 | Hollow frame | Medium | Print stars only on rectangle borders and spaces inside. For 3×5, the middle row is a star, 3 spaces, a star. Test height 1 and width 1. |
| G04 | Checkerboard | Medium | Alternate `#` and `.` across rows and columns, starting with `#` at row 0, column 0. For 2×3, lines are `#.#` and `.#.`. |
| G05 | Row totals | Medium | Store `{{1,2,3},{4,5,6}}` in an `int[,]`. Traverse with nested loops and `GetLength`; print row totals 6 and 15, resetting the total once per row. |

## F — Reusable steps

| ID | Exercise | Difficulty | Goal |
| --- | --- | --- | --- |
| F01 | Sum method | Easy | Extract a function taking an `int[]` and returning its sum. Check `{4,9,2}` → 15 and empty → 0. Keep printing outside it. |
| F02 | Factorial method | Medium | Extract A04 into a function with input contract 0–12 and an integer return value. Call it for 0, 1, and 5; validate user input before calling. |
| F03 | Rectangle method | Medium | Take height and width as parameters and print G01's rectangle. Call it twice with different dimensions; keep menu input outside the method. |

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
