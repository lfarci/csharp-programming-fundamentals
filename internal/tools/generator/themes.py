"""Themes: the chapters of the course, in order, and their sub-groups. Single source for the roadmap, the theme
pages, the website sidebar, the course order and ./ex progress.

Placement lives HERE, not in data*.py: every exercise ID appears in exactly one group, and the order of the
groups (then of the IDs inside a group) IS the course order (theme tables, Previous/Next, ./ex next).
Inside a group: one new difficulty at a time, levels never go back (Guided, then Independent, then Challenge).
Keep titles short. No dates, no weeks: the course is self-paced. internal/tools/check-structure.py checks the rules."""
ML = "https://learn.microsoft.com/en-us/dotnet"

def g(slug, title, recipe, ids, about):
    # recipe: the cookbook recipe that is the lesson of this group ("" = none); about: one short sentence.
    return dict(slug=slug, title=title, recipe=recipe, ids=ids, about=about)

def t(slug, title, part, summary, objectives, learn, docs, ready, groups):
    return dict(slug=slug, title=title, part=part, summary=summary, objectives=objectives, learn=learn,
                docs=docs, ready=ready, groups=groups, recipes=list(dict.fromkeys(x["recipe"] for x in groups if x["recipe"])))

THEMES = [
 t("basics", "Basics", "MS Learn Part 1: Write your first code",
   "Print, read, compute with variables and decide with `if`.",
   ["write a program that prints text and reads what the user types", "predict the result of `/` and `%` on whole numbers",
    "choose between 2 or more cases with `if` / `else if` / `else`", "list the boundary values to test"],
   "`Console.WriteLine`, `Console.ReadLine`; `int`, `double`, `string`, `bool`; `/` and `%`; `if` / `else`, `&&`, `||`.",
   [("Tutorial: Hello World", f"{ML}/csharp/tour-of-csharp/tutorials/hello-world"),
    ("Selection statements", f"{ML}/csharp/language-reference/statements/selection-statements")],
   "you can say what `17 / 5` and `17 % 5` give (3 and 2), and test every branch of an `if`.",
   [g("first-programs", "First programs", "", ["B01", "B02", "B03"], "Print, read and compute."),
    g("conditions", "Conditions", "", ["C01", "C02", "C03", "C04"], "Decide with `if`, `else if` and `else`.")]),
 t("loops", "Loops", "MS Learn Parts 2 and 3: Loops and logic",
   "Repeat code with `for` and `while`: count, add up, draw, take digits apart, search.",
   ["predict and trace a loop on paper, and find an off-by-one bug", "write a sum, a count and a product with a loop",
    "draw a rectangle and a triangle with a loop inside a loop", "take the digits of a number apart with `% 10` and `/ 10`",
    "update 2 or 3 variables in the right order", "answer a yes-or-no question with a `bool` flag"],
   "`for`, `while`, `do … while`, `break`; `+=`, `*=`; nested loops; `% 10` and `/ 10`.",
   [("Iteration statements", f"{ML}/csharp/language-reference/statements/iteration-statements")],
   "you can write factorial, a triangle and the digit sum from a blank file, and say if a number is prime.",
   [g("count", "Count", "01", ["L01", "L02", "L03", "L11", "L12", "L13", "L14", "L16", "L06", "L17", "L18", "L15", "L04"],
      "One loop that prints numbers: change only the start, the test or the step."),
    g("add-up", "Add up", "02", ["L19", "A11", "A01", "A13", "A14", "A18", "A20", "A19", "A04", "A07", "A05", "A10"],
      "A box before the loop, an update inside, the result after."),
    g("keep-only-some", "Keep only some", "03", ["A02", "A15", "A16", "A21", "A22", "A12", "A03", "A17", "A23", "A24", "A08"],
      "The same box, with an `if` inside the loop."),
    g("until-the-user-stops", "Until the user stops", "10", ["L05", "A06", "A09", "L07", "L08"],
      "Read values until a stop value, or until the input is valid."),
    g("draw-rows-and-grids", "Draw rows and grids", "08", ["L09", "L10", "G07", "G08", "G01", "G09", "G14", "G03"],
      "One row, then the same row many times: a loop inside a loop."),
    g("draw-shapes", "Draw shapes", "08", ["G02", "G10", "G11", "G12", "G04", "G13", "G05", "G06"],
      "The inner loop depends on the row, or an `if` picks the character."),
    g("digits", "Digits", "06", ["D01", "D02", "D03", "D08", "D04", "D09", "D10", "D12", "D11", "D07", "D05", "D13", "D06"],
      "`% 10` gives the last digit, `/ 10` removes it."),
    g("changing-values", "Changing values", "07", ["S01", "S04", "S02", "S06", "S05", "S07", "S03"],
      "Keep the last values in variables, like Fibonacci."),
    g("search-and-combine", "Search and combine", "05", ["P03", "P04", "P07", "P05", "P06", "P01", "P02", "M01", "M02"],
      "A `bool` flag that starts false, `break` to stop early, then two recipes together.")]),
 t("arrays", "Arrays, text and lists", "MS Learn Parts 2 and 4: Work with variable data",
   "Keep many values in one variable, work on text letter by letter, save to a file, use a `List`.",
   ["create an array and read `values[i]` without going out of range", "reuse a loop recipe on an array or a string",
    "write lines to a file and read them back", "choose between an array and a `List`"],
   "arrays, index from 0, `.Length`, `for` and `foreach`; `File.ReadAllLines`; `List<T>`.",
   [("Arrays", f"{ML}/csharp/language-reference/builtin-types/arrays"), ("Collections tutorial", f"{ML}/csharp/tour-of-csharp/tutorials/list-collection")],
   "you can explain the difference between `i` (the position) and `values[i]` (the value).",
   [g("arrays", "Arrays", "11", ["R01", "R03", "R07", "R02", "R06", "R04", "R08", "R05"], "Visit every element with `values[i]`."),
    g("text", "Text", "12", ["T01", "T02", "T03"], "A string is an array of letters."),
    g("files-and-lists", "Files and lists", "11", ["F01", "K01"], "Save values in a file; use a list that grows.")]),
 t("methods", "Methods and errors", "MS Learn Parts 5 and 6: Methods and debugging",
   "Split a program into small methods, and stop bad input from crashing it.",
   ["write a method with parameters and a `return`, and call it from another method", "use `int.TryParse` or `try` / `catch`"],
   "parameters, `return`, `void`; `int.TryParse`, `try` / `catch`.",
   [("Methods", f"{ML}/csharp/methods"), ("Exceptions", f"{ML}/csharp/fundamentals/exceptions/")],
   "you can turn your Armstrong solution into 3 small methods, and typing `abc` does not crash your program.",
   [g("methods", "Methods", "", ["N02", "N01"], "Give a recipe a name."),
    g("errors", "Errors", "09", ["E02", "E01"], "Bad input must not crash the program.")]),
]
BYSLUG = {x["slug"]: x for x in THEMES}
GROUP = {}  # exercise id -> (theme, group)
for _t in THEMES:
    for _g in _t["groups"]:
        for _i in _g["ids"]:
            assert _i not in GROUP, f"{_i} is listed in two groups"
            GROUP[_i] = (_t, _g)
