[Home](../README.md) › Getting started

# Getting started

This page sets up the course on your computer, then walks you through your first exercise. It takes about 15 minutes.

## Install the tools

You need two things:

- **The .NET SDK**, version 8 or newer: [download it here](https://dotnet.microsoft.com/download). It lets your computer run C#.
- **VS Code** with the **C# Dev Kit** extension: [download VS Code](https://code.visualstudio.com/). Visual Studio or Rider also work.

Check that .NET works. Open a terminal and type:

```bash
dotnet --version
```

You should see a number like `10.0.100`.

> A **terminal** is a window where you type commands. In VS Code: menu **Terminal › New Terminal**.

## Get the course

Copy the course to your computer with Git:

```bash
git clone https://github.com/lfarci/csharp-programming-fundamentals.git
```

No Git? On the GitHub page, click the green **Code** button, then **Download ZIP**, and unzip it.

## Open it in VS Code

1. In VS Code, choose **File › Open Folder…** and pick the `csharp-programming-fundamentals` folder.
2. Open the terminal (**Terminal › New Terminal**). It already points to the course folder.

The folders you will use:

| Folder | What is in it | Do you edit it? |
| --- | --- | --- |
| `practice/` | **Your** code, one file per exercise | Yes, only here |
| `exercises/` | The exercise pages | No, read them |
| `tests/` | The tests that check your code | No, read them if you like |
| `solutions/` | One solution per exercise | No, only look after a real try |

## Start your first exercise

Pick an exercise, for example [A04 · Factorial](../exercises/A04-factorial.md), and type:

```bash
./ex start A04
```

On Windows, type `.\ex` instead of `./ex`.

This creates **your file** `practice/A04_Factorial.cs` and opens the exercise. The comment at the top of the file says what to do. Most exercises ask you to fill in **one method**:

```csharp
public static long Factorial(int n)
{
    // TODO: write your code here.
    return 0;
}
```

- The **input** is the parameter (`n`). It is given to you.
- The **result** is what you `return`.

The checker calls your method with the examples of the page. You do not read the keyboard or print anything.

## Check your work

```bash
./ex check
```

Each example of the page says **OK** or **NOT YET**. A NOT YET shows what was expected and what your code gave:

```text
NOT YET  example 1 of 5: Factorial(5) returns 120
         Factorial(5) should return 120, but your method returned 0.
         Hint: 0 is the start value. Does your loop run at all?
```

Fix your code and check again. When every example is OK, you see **DONE** and the exercise is saved as done. Then go on:

```bash
./ex next
```

The first check takes a little longer, because it builds everything.

### All the commands

| Command | What it does |
| --- | --- |
| `./ex start A04` | Creates your file for A04. It never overwrites your work. |
| `./ex check` | Tests your code with every example. |
| `./ex run` | Runs your code; you type the values yourself. |
| `./ex next` | Starts the next exercise. |
| `./ex list` | Lists the exercises: done, started, not started. |
| `./ex progress` | Shows what is done in each theme, and a sync code for the website. |
| `./ex done L01` | Marks a paper exercise as done (paper exercises have no tests). |

### Where the tests are

Each exercise has one test file, for example `tests/Practice.Tests/Exercises/A04_FactorialTests.cs`. Each test is one example:

```csharp
[Fact(DisplayName = "A04 example 1: Factorial(5) returns 120")]
public void Example1() => Expect.Returns(120L, () => A04_Factorial.Factorial(5));
```

Read it as: "`Factorial(5)` must return `120`". You can read the tests, but do not change them. The **Test Explorer** of VS Code runs the same tests.

## Track your progress

- In the terminal, `./ex progress` shows what is done.
- On the website, tick **Mark as done** on an exercise page, or open [My progress](../progress.md).
- To copy your terminal results to the website, paste the **sync code** from the last line of `./ex progress` (it looks like `CPF1:A1-4;L3-11`) into **My progress**.

The website only remembers ticks in your browser. The real check is always `./ex check`.

## Get updates

New exercises come from time to time. Before a session, type:

```bash
git pull
```

Your files in `practice/` are never touched: Git ignores them.

## Save your work (optional)

Want a backup of your code on GitHub? Make your own copy (a **fork**):

1. On the course's GitHub page, click **Fork**.
2. Clone **your** fork instead: `git clone https://github.com/YOUR-NAME/csharp-programming-fundamentals.git`.
3. Save your code: `git add -f practice`, then `git commit -m "A04 done"`, then `git push`.
4. To get updates: on your fork's page, click **Sync fork**, then `git pull`.

## Learn the theory

This course is for practice. The theory comes from **Microsoft Learn**, free: the 6 parts of *Get started with C#* and the video series *C# Fundamentals for Absolute Beginners*. Each theme page says which module and video to use. See [Learn](../learn/README.md).

## Hints and solutions

- Each exercise has **hints**. Open **one**, then try again for 10 minutes before the next.
- The **solution** link is at the bottom of each exercise. Open it only after a real try. Your code can be different and still be correct.

New word? Look it up in the [glossary](glossary.md).

---

[Home](../README.md) · Next: [How to read an exercise](reading-an-exercise.md)
