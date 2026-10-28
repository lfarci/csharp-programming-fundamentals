# C# fundamentals roadmap

Follow this order. Move on when you can write the program from scratch and explain how it works.

| Step | Learn | Put it into practice |
| --- | --- | --- |
| 1. Run a program | Console projects, statements, execution order, compiler errors, `Console.WriteLine` | Create a program, change its output, and fix a syntax error. |
| 2. Work with values | Variables, assignment, `int`, `double`, `decimal`, `bool`, `string`, arithmetic, integer division | Calculate a receipt total and convert temperatures. Trace values after reassignment. |
| 3. Make decisions | Comparisons, Boolean operators, `if` / `else`, scope | Calculate a ticket price from age. Test every boundary. |
| 4. Read input | `Console.ReadLine`, `int.TryParse`, valid ranges | Read a number and either use it or explain why it is invalid. |
| 5. Repeat work | `for`, `while`, `do` / `while`, bounds, termination | Print a times table, retry invalid input, and stop on a sentinel. Trace each iteration. |
| 6. Track results | Counters, sums, products, conditional accumulation | Count entries, calculate an average, and compute factorial. Handle no entries and 0!. |
| 7. Write methods | Parameters, return values, `void`, local scope | Extract calculations into methods. Keep input and output separate from returned results. |
| 8. Process collections | Arrays, indices, `Length`, `for`, `foreach`, string traversal | Find a maximum, count matches, search for a value, and modify array elements. Handle empty inputs. |
| 9. Nest loops | Rows and columns, inner-loop reset, 2D arrays | Draw a rectangle and hollow frame; then calculate row totals in a stored grid. |
| 10. Combine the basics | Decomposition, choosing state and loops, debugging | Build a console score manager: enter scores, list them, and report count, average, and maximum. Use methods and validate input. |

At every step: predict a small example, run it, test boundaries, and use breakpoints or a variable trace to investigate mistakes.

Use *The C# Player's Guide* for explanations and the [exercise inventory](exercises/README.md) for practice: L01–L05 for loops, A01–A05 for accumulators, R01–R03 for arrays, then M01 for a mixed problem.

After the core path, use D01–D04, S01–S02, and M02–M03 for extra algorithm practice with digits, Fibonacci, and Armstrong numbers. Then continue with classes and objects, lists and dictionaries, exceptions, file I/O, and automated tests.
