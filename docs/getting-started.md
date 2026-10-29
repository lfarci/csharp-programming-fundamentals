[Home](../README.md) › Getting started

# Getting started

This page shows you, step by step, how to move around the course, run your code and use the exercises.

## 1. Read the course in your browser

Everything can be read on the website you are on now (github.com). No account needed.

- The page starts with a **list of folders and files**. Click a folder name (for example `exercises`) to open it. Click a file name (for example `A01-sum-1-to-n.md`) to read it.
- Below the list, GitHub shows the folder's `README.md` file: it is the welcome page of that folder.
- Every page starts with a small path like `Home › Roadmap › Exercises`. Click a word in it to go back up.
- At the bottom of each exercise there are **Previous** and **Next** links. Use them to walk through the exercises in order.
- To go back to the start at any time, click the course name at the top of the page, or the **Home** link.

## 2. Get the files on your computer

Pick **one** way. Both are fine.

| | **A. Clone** (simplest) | **B. Fork, then clone your fork** (optional) |
| --- | --- | --- |
| Good for | Practising on your own computer. | Keeping a copy of your work on **your** GitHub account (a backup). |
| How | `git clone https://github.com/lfarci/csharp-programming-fundamentals.git` | On GitHub, click **Fork** (top right). Then `git clone https://github.com/YOUR-NAME/csharp-programming-fundamentals.git` |
| Get course updates | `git pull` | On your fork's GitHub page: **Sync fork** › **Update branch**. Then `git pull`. |
| Save your work | Your files stay on your computer. | `git add -f practice` then `git commit -m "A04 done"` and `git push`. |

Then open the folder in your editor: `cd csharp-programming-fundamentals`.

### What you edit, and what you never touch

- **You only write in `practice/`**, in the files that `./ex start` creates (like `practice/A04_Factorial.cs`).
- **You never edit** `Program.cs`, `Practice.csproj`, `tests/`, `solutions/` or `tools/`. That is the course's machinery.
- Your exercise files are **ignored by Git** in the course repo (see `.gitignore`). So `git pull` never touches them, and they never clash with updates. On a fork, `git add -f practice` saves them anyway.
- Get updates before each session: `git pull` (and **Sync fork** first if you forked).

Other ways, if you prefer:

- **No Git at hand:** green **Code** button › **Download ZIP**, then extract it.
- **Nothing to install:** green **Code** button › **Codespaces** › **Create codespace on main**. A code editor with C# ready opens in your browser.

## 3. Install the tools (not needed in a codespace)

1. Install the **.NET SDK** (version 8 or newer) from [dotnet.microsoft.com/download](https://dotnet.microsoft.com/download).
2. Install **one** editor: [Visual Studio](https://visualstudio.microsoft.com/) (Windows), [VS Code](https://code.visualstudio.com/) with the **C# Dev Kit** extension, or [Rider](https://www.jetbrains.com/rider/).
3. Check it works: open a terminal and type `dotnet --version`. You should see a number like `10.0.100`.

> A **terminal** is a window where you type commands. In VS Code: menu **Terminal › New Terminal**. On Windows you can also open **PowerShell**.

## 4. Your first check (2 minutes)

Open a terminal **in the course folder** and type:

```bash
./ex start A01
./ex check
```

On **Windows**, type `.\ex` instead of `./ex` (for example `.\ex start A01`).

The first time takes a little longer (it builds everything). You should see 4 lines starting with `NOT YET` or `OK`. That is normal: you have not written any code yet. Your setup works.

In **VS Code** or a **codespace** you can also click: menu **Terminal › Run Task…** › **Exercise: start** / **Exercise: check**. **Visual Studio** and **Rider**: open `CSharpFundamentals.sln`. Your exercises are in the **Practice** project, and the **Test Explorer** shows a test for every example.

## 5. Do one exercise

What one exercise looks like, from start to DONE:

![Terminal demo, about 70 seconds: clone the course, ./ex start L11, ./ex check says NOT YET with what was expected and what the code printed, a first for loop misses the last number, the fix i <= b makes ./ex check say DONE, then ./ex progress and ./ex next.](assets/demo.gif)


| Command | What it does |
| --- | --- |
| `./ex start A04` | Creates **your file** `practice/A04_Factorial.cs` from a starter. It never overwrites a file you already have. A04 becomes your *current* exercise. |
| `./ex check` | Tests the current exercise with every example of its page. Each example says **OK** or **NOT YET**, and why. |
| `./ex run` | Runs the current exercise. You type the values yourself, like a normal program. |
| `./ex next` | Starts the next exercise in the list. |
| `./ex list` | Shows all exercises: done, started, or not started yet. |
| `./ex progress` | Shows how far you are: how many exercises are done, per roadmap step and per drill set. It also writes `practice/PROGRESS.md`. |
| `./ex done L01` | Marks a paper exercise as done (paper exercises have no tests). |

The steps, every time:

1. Open the exercise page, for example [A04 · Factorial](../exercises/A04-factorial.md). Read it with [How to read an exercise](reading-an-exercise.md) and fill a trace table on paper.
2. `./ex start A04`, then open `practice/A04_Factorial.cs`. The comment at the top says what to do.
3. Most exercises ask you to fill in **one method**, for example `Factorial(int n)`:
   - its **input** is the parameter `n`, already filled in for you;
   - its **result** is what you `return`.
   You do not read the keyboard or print anything: the tests call your method with the examples. Write your code where it says `TODO`.
   A few exercises (input loops, menus) are a whole program instead: then you write everything inside `Run()`.
4. `./ex check`. Read the first **NOT YET**: it shows what was expected and what your code gave. Fix, check again.
5. All **OK**? `./ex check` says **DONE** and saves the exercise as done. Test the edge cases of the page with `./ex run`, then type `./ex next`.

Your work stays in `practice/`. The [solutions](../solutions/README.md) are in another folder, so you never mix them up.

### Why not one big `Main` where you comment lines in and out?

In a project like the Player's Guide challenges, you switch exercises by putting `//` in front of lines in `Program.cs`, then you check the output with your eyes. Here:

- **Nothing to edit to switch:** `./ex start` and `./ex check A04` pick the exercise for you.
- **No copy-paste plumbing:** no `Run(args)` wrapper, no reading input just to test an idea. You write the part that matters: the method.
- **A real check:** the computer compares your result with every example, so you know for sure, and it tells you what is different.

These checks are real **unit tests** (xUnit), the tool professional developers use. You do not have to learn them now: `./ex check` runs them for you.

### Where the tests are

Each exercise has **one test file**: `tests/Practice.Tests/Exercises/<your file name>Tests.cs`. `./ex start` and `./ex check` print its path. Open it to see the exact inputs and results the computer checks. For example `A04_FactorialTests.cs`:

```csharp
[Fact(DisplayName = "A04 example 1: Factorial(5) returns 120")]
public void Example1() => Expect.Returns(120L, () => A04_Factorial.Factorial(5));

[Fact(DisplayName = "A04 example 2: Factorial(0) returns 1")]
public void Example2() => Expect.Returns(1L, () => A04_Factorial.Factorial(0));
```

Read a line as: "calling `Factorial(5)` must return `120`". (The `L` after `120` only means "a `long` number".) Read the tests, but do not change them.

Three ways to run them, all the same tests:

- `./ex check A04` (the easiest, with plain-language messages);
- `dotnet test tests/Practice.Tests --filter-class "*A04*"`;
- the **Test Explorer** of Visual Studio, Rider or VS Code.

Only the exercises you started are tested, so the exercises you have not started never get in your way.

### Your progress

`./ex check` remembers each exercise that passes (in `practice/.done`, on your computer only). `./ex progress` shows the count, for example:

```text
Progress: 12 of 96 exercises done, 2 started (not done yet).
```

then a line per roadmap step and a line per drill set, where `x` means done, `o` started and `.` not started. It ends with the exercise to do next.

## 6. Hints and solutions

- A **hint** is hidden under a line like **Hint 1**. Click it to open it. Open **one** hint, close the page, and try again for 10 minutes before opening the next one.
- The **solution** link is at the bottom of each exercise. Open it only after a real try, or after all the hints. Your code can be different from it and still be correct.
- Days later, do the **Mastery check** of the exercise alone. That is how you know you really learned it.

## 7. Words you do not know?

Look them up in the [glossary](glossary.md).

---

[Home](../README.md) · Next: [How to read an exercise](reading-an-exercise.md)
