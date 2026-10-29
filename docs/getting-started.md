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

## 4. Open the practice project and run it

All your code goes in **one file**: `practice/Program.cs`.

- **Visual Studio:** **File › Open › Project/Solution**, choose `practice/Practice.csproj`. Press the green ▶️ button.
- **VS Code or Codespaces:** **File › Open Folder**, choose the course folder. Open `practice/Program.cs`. In the terminal, type `dotnet run --project practice` and press Enter.
- **Rider:** **Open**, choose `practice/Practice.csproj`. Press the green ▶️ button.

You should see `Hello! Replace me with your exercise.` 🎉 Your setup works.

## 5. Do one exercise

1. Open an exercise page, for example [L03 · Count up and down](../exercises/L03-count-up-and-down.md).
2. Read it with [How to read an exercise](reading-an-exercise.md). Fill a trace table on paper.
3. Delete the code in `practice/Program.cs` and write your own.
4. Run it. Type the **input** from an example (for example `5`, then Enter).
5. Compare what your program prints with the **Examples** box of the exercise. The question text (like `N: `) can be different. The **results** must be the same.
6. Try the **Edge cases** listed on the page too.
7. Proud of it? Save a copy as `practice/done/L03.cs.txt` (the `.txt` ending keeps it from running) and commit it.
8. Tick it in your [progress checklist](progress-checklist.md).

## 6. Hints and solutions

- A **hint** is hidden under a line like ▶ **Hint 1**. Click it to open it. Open **one** hint, close the page, and try again for 10 minutes before opening the next one.
- The **solution** link is at the bottom of each exercise. Open it only after a real try, or after all the hints. Your code can be different from it and still be correct.
- Days later, do the **Mastery check** of the exercise alone. That is how you know you really learned it.

## 7. Words you do not know?

Look them up in the [glossary](glossary.md).

---

⬅️ [Home](../README.md) · Next: [How to read an exercise](reading-an-exercise.md) ➡️
