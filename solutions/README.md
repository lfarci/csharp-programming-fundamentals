🏠 [Home](../README.md) › 🔑 Solutions

# 🔑 Solutions

**Stop!** Did you really try? Did you open the hints? Did you fill a trace table?
A solution read too early teaches less than an exercise solved with 3 hints. 🙂

- One file per exercise: `<ID>-<name>.cs` (C# code) or `.md` (answer key for paper exercises).
- Your solution can be different and still be correct. Compare the **idea** (which recipe? which boxes?), not the exact words.
- The code only uses what the matching roadmap step teaches (no LINQ, no tricks).

## How to run a solution

- **.NET 10 or newer:** `dotnet run solutions/A04-factorial.cs`
- **Any .NET:** paste the code into [`practice/Program.cs`](../practice/Program.cs) and run `dotnet run --project practice`.

## For the coach: check all solutions

Every solution is run with the examples from its exercise (`tests.json`) and the expected lines must appear in the output:

```bash
python3 tools/check-solutions.py          # all
python3 tools/check-solutions.py A0 M01   # only some
```

Requires the .NET 10 SDK. Exercise files, the inventory and this folder are generated from one data source ([`tools/generator/`](../tools/generator/), run `python3 tools/generator/gen.py`), so the examples in `exercises/` and `tests.json` always match.
