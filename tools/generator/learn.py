# The theory map: which outside resource to read or watch before each theme.
# One source of truth for themes/<slug>.md ("Learn the theory" box), learn/*.md and .vitepress/course.json.
# Every name and URL below was checked on the official site (book TOC: the free sample PDF on csharpplayersguide.com;
# Microsoft Learn: the learn.microsoft.com catalog). Do not add a resource you have not opened.

BOOK = {
    "title": "The C# Player's Guide",
    "author": "RB Whitaker",
    "edition": "5th edition",
    "url": "https://csharpplayersguide.com/",
    "sample": "https://csharpplayersguide.com/TheCSharpPlayersGuide-5thEdition-Sample.pdf",
}
# Level names, from the table of contents of the 5th edition (only the levels we point to).
LEVELS = {3: "Hello World: Your First Program", 4: "Comments", 5: "Variables", 6: "The C# Type System", 7: "Math",
          8: "Console 2.0", 9: "Decision Making", 10: "Switches", 11: "Looping", 12: "Arrays", 13: "Methods",
          32: "Some Useful Types", 35: "Error Handling and Exceptions", 39: "Files"}

TRACKER = {"title": "C# Quest Tracker", "url": "https://lfarci.github.io/csharp-quest-tracker/",
           "repo": "https://github.com/lfarci/csharp-quest-tracker"}

ML = "https://learn.microsoft.com/en-us/training/modules/"
MLP = "https://learn.microsoft.com/en-us/training/paths/"
VID = "https://learn.microsoft.com/en-us/shows/csharp-for-beginners/"
PATHS = [  # Microsoft Learn, "Get started with C#" (the six paths of the Foundational C# certification)
    ("Write your first code using C#", MLP + "get-started-c-sharp-part-1/"),
    ("Create and run simple C# console applications", MLP + "get-started-c-sharp-part-2/"),
    ("Add logic to C# console applications", MLP + "get-started-c-sharp-part-3/"),
    ("Work with variable data in C# console applications", MLP + "get-started-c-sharp-part-4/"),
    ("Create methods in C# console applications", MLP + "get-started-c-sharp-part-5/"),
    ("Debug C# console applications", MLP + "get-started-c-sharp-part-6/"),
]
CERT = ("Foundational C# with Microsoft (free certification, with freeCodeCamp)", "https://www.freecodecamp.org/learn/foundational-c-sharp-with-microsoft/")
VIDEOS = ("C# for Beginners (19 videos, Scott Hanselman and David Fowler)", VID)
TOUR = ("A tour of the C# language", "https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/")

def m(title, slug): return (title, ML + slug + "/")
def v(title, slug): return (title, VID + slug + "/")

# theme slug -> book levels, Microsoft Learn modules, C# for Beginners videos
THEORY = {
    "hello-world": dict(levels=[3, 4], modules=[m("Write your first C# code", "csharp-write-first")],
                        videos=[v("Hello World!", "hello-world-csharp-for-beginners"), v("Hello World, Introducing Strings!", "hello-world-introducing-strings-csharp-for-beginners")]),
    "variables": dict(levels=[5, 6, 7, 8], modules=[m("Store data with variables in C#", "csharp-literals-variables"), m("Perform basic operations on numbers in C#", "csharp-basic-operations"),
                                                    m("Convert data types using casting and conversion techniques in C#", "csharp-convert-cast")],
                      videos=[v("Numbers, Integers, and Math", "numbers-integers-and-math-csharp-for-beginners"), v("Numbers, Precision, Casting, Doubles, and More", "numbers-precision-casting-doubles-and-more-csharp-for-beginners")]),
    "conditions": dict(levels=[9, 10], modules=[m("Add decision logic to your code in C#", "csharp-if-elseif-else"), m("Evaluate Boolean expressions to make decisions in C#", "csharp-evaluate-boolean-expressions"),
                                                m("Branch the flow of code using the switch-case construct in C#", "csharp-switch-case")],
                       videos=[v("Branching, Ifs, and Conditional Logic", "branching-ifs-and-conditional-logic-csharp-for-beginners")]),
    "loops-repeat": dict(levels=[11], modules=[m("Iterate through a code block using for statement in C#", "csharp-for"), m("Add looping logic to your code using the do-while and while statements in C#", "csharp-do-while")],
                         videos=[v("Branching and While Loops", "branching-and-while-loops-csharp-for-beginners"), v("For Loops", "for-loops-csharp-for-beginners")]),
    "loops-running-result": dict(levels=[11], modules=[m("Repeat actions with loops in C#", "csharp-repeat-actions-loops")], videos=[v("For Loops", "for-loops-csharp-for-beginners")]),
    "loops-2d": dict(levels=[11], modules=[m("Iterate through a code block using for statement in C#", "csharp-for")], videos=[]),
    "loops-digits": dict(levels=[7, 11], modules=[m("Perform basic operations on numbers in C#", "csharp-basic-operations")], videos=[]),
    "loops-state": dict(levels=[11], modules=[m("Control variable scope and logic using code blocks in C#", "csharp-code-blocks")], videos=[]),
    "loops-search": dict(levels=[11], modules=[m("Add looping logic to your code using the do-while and while statements in C#", "csharp-do-while")], videos=[]),
    "combine": dict(levels=[11], modules=[m("Guided project - Develop conditional branching and looping structures in C#", "guided-project-develop-conditional-branching-looping")], videos=[]),
    "arrays": dict(levels=[12], modules=[m("Organize data with arrays and lists in C#", "csharp-arrays-lists"), m("Perform operations on arrays using helper methods in C#", "csharp-arrays-operations"),
                                         m("Modify the content of strings using built-in string data type methods in C#", "csharp-modify-content")],
                   videos=[v("Arrays, Lists, Indexing, and Foreach", "arrays-lists-indexing-and-foreach-csharp-for-beginners"), v("The Basics of Strings!", "the-basics-of-strings-csharp-for-beginners")]),
    "files": dict(levels=[39], modules=[m("Read and write files in C#", "csharp-read-write-files")], videos=[]),
    "exceptions": dict(levels=[35], modules=[m("Implement exception handling in C# console applications", "implement-exception-handling-c-sharp")], videos=[]),
    "collections": dict(levels=[32], modules=[m("Organize data with arrays and lists in C#", "csharp-arrays-lists")], videos=[v("Arrays, Lists, Indexing, and Foreach", "arrays-lists-indexing-and-foreach-csharp-for-beginners")]),
    "methods": dict(levels=[13], modules=[m("Write your first C# method", "write-first-c-sharp-method"), m("Create C# methods with parameters", "create-c-sharp-methods-parameters"),
                                          m("Create C# methods that return values", "create-c-sharp-methods-return-values")], videos=[]),
}

def level_text(levels):
    return ", ".join(f"Level {n}: {LEVELS[n]}" for n in levels)
