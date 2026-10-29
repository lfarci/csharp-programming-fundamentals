[Home](../README.md) › Practice folder

# Practice folder

**Your** code lives here: one file per exercise, created by `./ex start`.

```bash
./ex start A04     # creates practice/A04_Factorial.cs (never overwrites your file)
./ex check         # tests it with the examples of the exercise page
./ex run           # runs it; you type the values yourself
./ex progress      # how many exercises are done, and what to do next
```

On Windows, type `.\ex` instead of `./ex`. Full guide: [Getting started](../docs/getting-started.md).

## Tips

- Before typing, fill the [recipe card](../cookbook/README.md) and a trace table on paper.
- Use the debugger (VS Code: **Run › Start Debugging** on "Debug the current exercise") or a temporary `Console.WriteLine` to *watch* the variables change.
- You never need to edit `Program.cs` or `Practice.csproj`.
- `./ex check A04` and `./ex run A04` build only `Program.cs` and that exercise's file, so an unfinished file elsewhere never blocks you. (Visual Studio, Rider and Test Explorer build the whole folder, so there a broken file does block the others.)
- Your files here are ignored by Git, so `git pull` never touches them. Forked the course to your own GitHub? Save them with `git add -f practice`, `git commit`, `git push`. See [Get the files](../docs/getting-started.md#2-get-the-files-on-your-computer).
- The tests for `A04` are in `tests/Practice.Tests/Exercises/A04_FactorialTests.cs`: open them to see every input and expected result.
- `./ex check` saves the exercises you finished in `practice/.done`; `./ex progress` also writes `practice/PROGRESS.md`. Both stay on your computer.
- All OK? Compare your idea with the [solutions](../solutions/README.md).

---

[Home](../README.md) · [Getting started](../docs/getting-started.md) · [All exercises](../exercises/README.md)
