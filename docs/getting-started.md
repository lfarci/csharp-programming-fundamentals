🏠 [Home](../README.md) › 🚀 Getting started

# 🚀 Getting started

This page shows you, step by step, how to move around the course, run your code and use the exercises.

## 1. Read the course in your browser

Everything can be read on the website you are on now (github.com). No account needed.

- The page starts with a **list of folders and files**. Click a folder name (for example `exercises`) to open it. Click a file name (for example `A01-sum-1-to-n.md`) to read it.
- Below the list, GitHub shows the folder's `README.md` file: it is the welcome page of that folder.
- Every page starts with a small path like `🏠 Home › 🗺️ Roadmap › 📚 Exercises`. Click a word in it to go back up.
- At the bottom of each exercise there are **Previous** and **Next** links. Use them to walk through the exercises in order.
- To go back to the start at any time, click the course name at the top of the page, or the **🏠 Home** link.

## 2. Get the files on your computer

```bash
git clone https://github.com/lfarci/csharp-programming-fundamentals.git
```

Run `git pull` before each session to get the newest exercises.

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

The first time takes a little longer (it builds everything). You should see 4 lines starting with `❌ NOT YET` or `✅ OK`. That is normal: you have not written any code yet. 🎉 Your setup works.

In **VS Code** or a **codespace** you can also click: menu **Terminal › Run Task…** › **Exercise: start** / **Exercise: check**. **Visual Studio** and **Rider**: open `CSharpFundamentals.sln`. Your exercises are in the **Practice** project, and the **Test Explorer** shows a test for every example.

## 5. Do one exercise

| Command | What it does |
| --- | --- |
| `./ex start A04` | Creates **your file** `practice/A04_Factorial.cs` from a starter. It never overwrites a file you already have. A04 becomes your *current* exercise. |
| `./ex check` | Tests the current exercise with every example of its page. Each example says **OK** or **NOT YET**, and why. |
| `./ex run` | Runs the current exercise. You type the values yourself, like a normal program. |
| `./ex next` | Starts the next exercise in the list. |
| `./ex list` | Shows all exercises, and which ones you started. |

The steps, every time:

1. Open the exercise page, for example [A04 · Factorial](../exercises/A04-factorial.md). Read it with [How to read an exercise](reading-an-exercise.md) and fill a trace table on paper.
2. `./ex start A04`, then open `practice/A04_Factorial.cs`. The comment at the top says what to do.
3. Most exercises ask you to fill in **one method**, for example `Factorial(int n)`:
   - its **input** is the parameter `n`, already filled in for you;
   - its **result** is what you `return`.
   You do not read the keyboard or print anything: the tests call your method with the examples. Write your code where it says `TODO`.
   A few exercises (input loops, menus) are a whole program instead: then you write everything inside `Run()`.
4. `./ex check`. Read the first **NOT YET**: it shows what was expected and what your code gave. Fix, check again.
5. All **OK**? Test the edge cases of the page with `./ex run`, then commit your file and tick the exercise in your [progress checklist](progress-checklist.md).

Your work stays in `practice/`. The [solutions](../solutions/README.md) are in another folder, so you never mix them up.

### Why not one big `Main` where you comment lines in and out?

In a project like the Player's Guide challenges, you switch exercises by putting `//` in front of lines in `Program.cs`, then you check the output with your eyes. Here:

- **Nothing to edit to switch:** `./ex start` and `./ex check A04` pick the exercise for you.
- **No copy-paste plumbing:** no `Run(args)` wrapper, no reading input just to test an idea. You write the part that matters: the method.
- **A real check:** the computer compares your result with every example, so you know for sure, and it tells you what is different.

These checks are real **unit tests** (xUnit), the tool professional developers use. You do not have to learn them now: `./ex check` runs them for you.

## 6. Hints and solutions

- A **hint** is hidden under a line like ▶ **Hint 1**. Click it to open it. Open **one** hint, close the page, and try again for 10 minutes before opening the next one.
- The **solution** link is at the bottom of each exercise. Open it only after a real try, or after all the hints. Your code can be different from it and still be correct.
- Days later, do the **Mastery check** of the exercise alone. That is how you know you really learned it.

## 7. Words you do not know?

Look them up in the [glossary](glossary.md).

---

⬅️ [Home](../README.md) · Next: [How to read an exercise](reading-an-exercise.md) ➡️
