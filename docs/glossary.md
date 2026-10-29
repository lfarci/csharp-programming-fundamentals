🏠 [Home](../README.md) › 📖 Glossary

# 📖 Glossary

Short meanings of the words used in this course, in alphabetical order. A word in *italics* has its own entry.

| Word | Meaning | Example |
| --- | --- | --- |
| **Accumulator** | A *variable* that collects a result while the *loop* runs: a sum, a count, a product. See [recipe 2](../cookbook/02-accumulator.md). | `sum += i;` |
| **Algorithm** | The list of steps that solves a problem, written in plain words before the code. | "Add each number to the total." |
| **Array** | A row of boxes with a fixed size. Each box has a position (an *index*) starting at 0. | `int[] values = { 4, 9, 2 };` |
| **Boundary** | The first or last value a *loop* or `if` must handle, where mistakes happen most. | Is 10 included in "1 to 10"? |
| **Box** | Our friendly word for a *variable*: a named place that holds one value. | `int count = 0;` |
| **Bug** | A mistake in the code. The program runs, but does the wrong thing, or crashes. | |
| **`char`** | One single character, written with single quotes. | `'a'` |
| **Condition** | A question with a yes/no (`true`/`false`) answer, used by `if` and loops. | `n > 0` |
| **Counter** | A *variable* that goes up (or down) by 1 on each turn. | `i++` |
| **Edge case** | An unusual input that must still work: 0, 1, a negative number, empty text. | N = 0 |
| **Exception** | An error that stops the program (a crash), unless you catch it with `try`/`catch`. | typing `abc` for `int.Parse` |
| **Flag** | A `bool` *variable* that remembers "did it happen yet?". See [recipe 5](../cookbook/05-flag-search.md). | `bool found = false;` |
| **Index** | The position of an item in an *array* or string. The first index is 0. | `values[0]` |
| **Infinite loop** | A *loop* that never stops, because its *condition* never becomes false. | forgetting `i++` |
| **Input** | What the program reads (from the keyboard or a file). | `Console.ReadLine()` |
| **Integer division** | `/` between two `int` values: the part after the decimal point is thrown away. | `17 / 5` is `3` |
| **Iteration** | One turn of a *loop*. A loop from 1 to 5 does 5 iterations. | |
| **LINQ** | A C# toolbox that does loops for you (`.Sum()`, `.Max()`…). Not used here: you learn to write the loop yourself. | |
| **Loop** | Code that repeats: `for`, `while`, `do … while`, `foreach`. | `for (int i = 1; i <= n; i++)` |
| **Mastery check** | A new variation of an exercise you solve alone, on another day, to prove you learned it. | |
| **Method** | A named piece of code you can call again and again. It gets its **input** through *parameters* and gives back its **result** with `return`. Most exercises ask you to fill in one. | `static int SumTo(int n) { … return sum; }` |
| **Parameter** | An input of a *method*, written between the brackets. The caller gives its value. | `n` in `SumTo(int n)` |
| **Return** | Gives the result of a *method* back to the code that called it, and ends the method. | `return sum;` |
| **Unit test** | Code that calls your *method* with an example and checks the result. `./ex check` runs them for you. | `SumTo(5)` must give `15` |
| **Modulo (`%`)** | The remainder of a division. | `17 % 5` is `2`, `352 % 10` is `2` |
| **Nested loop** | A *loop* inside another loop. See [recipe 8](../cookbook/08-nested-grid.md). | rows and columns |
| **Output** | What the program shows (prints). | `Console.WriteLine("Hi")` |
| **Recipe** | A small code pattern that solves a common kind of problem. See the [cookbook](../cookbook/README.md). | counter loop, accumulator |
| **Repository (repo)** | The online folder that holds this whole course on GitHub. | this website |
| **Sentinel** | A special value that means "stop", like 0. See [recipe 10](../cookbook/10-sentinel-loop.md). | "enter 0 to stop" |
| **Solution** | One possible correct code for an exercise. Yours can be different and still be right. | |
| **String** | Text, written with double quotes. | `"Hello"` |
| **Terminal** | A window where you type commands like `dotnet run`. | |
| **Trace table** | A table on paper with one row per *iteration*, showing each *variable*'s value. | |
| **Variable** | A named place in memory that holds one value. Also called a *box* here. | `int age = 20;` |

---

⬅️ [Home](../README.md) · [Getting started](getting-started.md)
