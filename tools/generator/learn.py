# The theory map: which outside resource to read or watch before each theme.
# One source of truth for themes/<slug>.md ("Learn the theory" box), learn/*.md and .vitepress/course.json.
# Every name and URL below comes from the official Microsoft Learn catalog and show APIs, and returned 200.
# Rule: theory comes from Microsoft Learn only. Never reference or map the content of a copyrighted book.

TRACKER = {"title": "C# Quest Tracker", "url": "https://lfarci.github.io/csharp-quest-tracker/",
           "repo": "https://github.com/lfarci/csharp-quest-tracker"}

ML = "https://learn.microsoft.com/en-us/training/modules/"
MLP = "https://learn.microsoft.com/en-us/training/paths/"
def path_url(n): return f"{MLP}get-started-c-sharp-part-{n}/"
def module_url(slug): return f"{ML}{slug}/"

PARTS = {  # Microsoft Learn, "Get started with C#", from the official catalog (learn.microsoft.com/api/catalog)
    1: ('Write your first code using C#', [
        ('Write your first C# code', 'csharp-write-first'),
        ('Store data with variables in C#', 'csharp-literals-variables'),
        ('Perform basic operations on numbers in C#', 'csharp-basic-operations'),
        ('Add decision logic to your code in C#', 'csharp-if-elseif-else'),
    ]),
    2: ('Create and run simple C# console applications', [
        ('Install and configure Visual Studio Code', 'install-configure-visual-studio-code'),
        ('Repeat actions with loops in C#', 'csharp-repeat-actions-loops'),
        ('Organize data with arrays and lists in C#', 'csharp-arrays-lists'),
        ('Write reusable code in C#', 'csharp-reusable-code'),
        ('Read and write files in C#', 'csharp-read-write-files'),
    ]),
    3: ('Add logic to C# console applications', [
        ('Evaluate Boolean expressions to make decisions in C#', 'csharp-evaluate-boolean-expressions'),
        ('Control variable scope and logic using code blocks in C#', 'csharp-code-blocks'),
        ('Branch the flow of code using the switch-case construct in C#', 'csharp-switch-case'),
        ('Iterate through a code block using for statement in C#', 'csharp-for'),
        ('Add looping logic to your code using the do-while and while statements in C#', 'csharp-do-while'),
        ('Guided project - Develop conditional branching and looping structures in C#', 'guided-project-develop-conditional-branching-looping'),
        ('Challenge project - Develop branching and looping structures in C#', 'challenge-project-develop-branching-looping-structures-c-sharp'),
    ]),
    4: ('Work with variable data in C# console applications', [
        ('Choose the correct data type in your C# code', 'csharp-choose-data-type'),
        ('Convert data types using casting and conversion techniques in C#', 'csharp-convert-cast'),
        ('Perform operations on arrays using helper methods in C#', 'csharp-arrays-operations'),
        ('Format alphanumeric data for presentation in C#', 'csharp-format-strings'),
        ('Modify the content of strings using built-in string data type methods in C#', 'csharp-modify-content'),
        ('Guided project - Work with variable data in C#', 'guided-project-work-variable-data-c-sharp'),
        ('Challenge project - Work with variable data in C#', 'challenge-project-work-variable-data-c-sharp'),
    ]),
    5: ('Create methods in C# console applications', [
        ('Write your first C# method', 'write-first-c-sharp-method'),
        ('Create C# methods with parameters', 'create-c-sharp-methods-parameters'),
        ('Create C# methods that return values', 'create-c-sharp-methods-return-values'),
        ('Guided project - Plan a Petting Zoo Visit', 'guided-project-visit-petting-zoo'),
        ('Challenge project - Create a mini-game', 'challenge-project-create-mini-game'),
    ]),
    6: ('Debug C# console applications', [
        ('Review the principles of code debugging and exception handling', 'review-principles-code-debugging-exception-handling-c-sharp'),
        ('Implement the Visual Studio Code debugging tools for C#', 'implement-visual-studio-code-debugging-tools'),
        ('Implement exception handling in C# console applications', 'implement-exception-handling-c-sharp'),
        ('Create and throw exceptions in C# console applications', 'create-throw-exceptions-c-sharp'),
        ('Guided project - Debug and handle exceptions in a C# console application using Visual Studio Code', 'guided-project-debug-handle-exceptions-c-sharp-console-application'),
        ('Challenge project - Debug a C# console application using Visual Studio Code', 'challenge-project-debug-c-sharp-console-application'),
    ]),
}
MODULE = {slug: (n, title) for n, (_, ms) in PARTS.items() for title, slug in ms}

CERT = ("Foundational C# with Microsoft", "https://www.freecodecamp.org/learn/foundational-c-sharp-with-microsoft/")

# Main video series: C# Fundamentals for Absolute Beginners (Bob Tabor, 25 episodes), from the show's episode API.
SERIES = ("C# Fundamentals for Absolute Beginners", "https://learn.microsoft.com/en-us/shows/csharp-fundamentals-for-absolute-beginners/")
def episode_url(slug): return f"{SERIES[1]}{slug}/"
EPISODES = {  # slug: (title, minutes)
    'creating-and-adding-references-to-assemblies': ('Creating and Adding References to Assemblies', 20),
    'understanding-data-types-and-variables': ('Understanding Data Types and Variables', 28),
    'where-to-go-from-here': ('Where to Go from Here', 32),
    'working-with-code-files-projects-and-solutions': ('Working with Code Files, Projects, and Solutions', 11),
    'understanding-arrays': ('Understanding Arrays', 17),
    'more-about-classes-and-methods': ('More About Classes and Methods', 34),
    'working-with-strings': ('Working with Strings', 23),
    'enumerations-and-the-switch-decision-statement': ('Enumerations and the Switch Decision Statement', 13),
    'understanding-scope-and-accessibility-modifiers': ('Understanding Scope and Accessibility Modifiers', 16),
    'understanding-your-first-c-program': ('Understanding Your First C# Program', 17),
    'installing-visual-studio': ('Installing Visual Studio', 5),
    'understanding-events-and-event-driven-programming': ('Understanding Events and Event-Driven Programming', 21),
    'while-iteration-statement': ('While Iteration Statement', 18),
    'gracefully-handling-exceptions': ('Gracefully Handling Exceptions', 21),
    'working-with-collections': ('Working with Collections', 23),
    'understanding-classes': ('Understanding Classes', 24),
    'operators-expressions-and-statements': ('Operators, Expressions, and Statements', 15),
    'working-with-linq': ('Working with LINQ', 24),
    'course-introduction': ('Course Introduction', 8),
    'working-with-dates-and-times': ('Working with Dates and Times', 10),
    'creating-your-first-c-program': ('Creating Your First C# Program', 16),
    'understanding-namespaces-and-working-with-the-dotnet-class-library': ('Understanding Namespaces and Working with the .NET Class Library', 17),
    'for-iteration-statement': ('for Iteration Statement', 18),
    'defining-and-calling-methods': ('Defining and Calling Methods', 31),
    'the-if-decision-statement': ('The if Decision Statement', 23),
}

# In the order Bob Tabor teaches them. Selection rule (see AGENTS.md): keep an episode only if it teaches a
# fundamentals idea that one of our themes practises (it is listed in THEORY below). Everything else is dropped:
DROPPED = {  # slug: why it is not on the Videos page
    "course-introduction": "series overview, no idea to practise",
    "installing-visual-studio": "installs Visual Studio; this course uses VS Code (see Getting started)",
    "working-with-code-files-projects-and-solutions": "project tooling, not a fundamentals idea",
    "working-with-dates-and-times": "no theme uses dates",
    "understanding-classes": "classes and objects come after this course",
    "more-about-classes-and-methods": "classes and objects come after this course",
    "understanding-namespaces-and-working-with-the-dotnet-class-library": "too advanced for the fundamentals",
    "creating-and-adding-references-to-assemblies": "too advanced for the fundamentals",
    "understanding-scope-and-accessibility-modifiers": "accessibility modifiers belong with classes",
    "working-with-linq": "LINQ is not used: you write the loops yourself",
    "understanding-events-and-event-driven-programming": "too advanced for the fundamentals",
    "where-to-go-from-here": "next steps after the series, no idea to practise",
}
EPISODE_ORDER = ["creating-your-first-c-program", "understanding-your-first-c-program", "understanding-data-types-and-variables",
    "the-if-decision-statement", "operators-expressions-and-statements", "for-iteration-statement", "understanding-arrays",
    "defining-and-calling-methods", "while-iteration-statement", "working-with-strings",
    "enumerations-and-the-switch-decision-statement", "gracefully-handling-exceptions", "working-with-collections"]
assert sorted(EPISODE_ORDER + list(DROPPED)) == sorted(EPISODES), "every episode is either kept (EPISODE_ORDER) or DROPPED, once"

# Extra videos (optional): the newer C# for Beginners series.
VIDEOS = ("C# for Beginners (Scott Hanselman and David Fowler)", "https://learn.microsoft.com/en-us/shows/csharp-for-beginners/")
TOUR = ("A tour of the C# language", "https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/")

# theme slug -> Microsoft Learn part (the main one), modules (any part), episodes.
THEORY = {
    "hello-world": dict(part=1, modules=["csharp-write-first", "install-configure-visual-studio-code"],
                        episodes=["creating-your-first-c-program", "understanding-your-first-c-program"]),
    "variables": dict(part=1, modules=["csharp-literals-variables", "csharp-basic-operations", "csharp-choose-data-type", "csharp-convert-cast"],
                      episodes=["understanding-data-types-and-variables", "operators-expressions-and-statements"]),
    "conditions": dict(part=1, modules=["csharp-if-elseif-else", "csharp-evaluate-boolean-expressions", "csharp-switch-case"],
                       episodes=["the-if-decision-statement", "enumerations-and-the-switch-decision-statement"]),
    "loops-repeat": dict(part=3, modules=["csharp-for", "csharp-do-while", "csharp-repeat-actions-loops"],
                         episodes=["for-iteration-statement", "while-iteration-statement"]),
    "loops-running-result": dict(part=3, modules=["csharp-for"], episodes=["for-iteration-statement"]),
    "loops-2d": dict(part=3, modules=["csharp-for", "csharp-code-blocks"], episodes=["for-iteration-statement"]),
    "loops-digits": dict(part=3, modules=["csharp-do-while", "csharp-basic-operations"], episodes=["while-iteration-statement", "operators-expressions-and-statements"]),
    "loops-state": dict(part=3, modules=["csharp-code-blocks", "csharp-do-while"], episodes=["while-iteration-statement"]),
    "loops-search": dict(part=3, modules=["csharp-do-while", "csharp-evaluate-boolean-expressions"], episodes=["while-iteration-statement"]),
    "combine": dict(part=3, modules=["guided-project-develop-conditional-branching-looping", "challenge-project-develop-branching-looping-structures-c-sharp",
                                     "implement-visual-studio-code-debugging-tools"], episodes=["for-iteration-statement", "the-if-decision-statement"]),
    "arrays": dict(part=4, modules=["csharp-arrays-lists", "csharp-arrays-operations", "csharp-modify-content", "csharp-format-strings"],
                   episodes=["understanding-arrays", "working-with-strings"]),
    "files": dict(part=2, modules=["csharp-read-write-files"], episodes=["working-with-strings"]),
    "exceptions": dict(part=6, modules=["review-principles-code-debugging-exception-handling-c-sharp", "implement-exception-handling-c-sharp", "create-throw-exceptions-c-sharp"],
                       episodes=["gracefully-handling-exceptions"]),
    "collections": dict(part=2, modules=["csharp-arrays-lists"], episodes=["working-with-collections"]),
    "methods": dict(part=5, modules=["write-first-c-sharp-method", "create-c-sharp-methods-parameters", "create-c-sharp-methods-return-values", "csharp-reusable-code"],
                    episodes=["defining-and-calling-methods"]),
}
for _s, _t in THEORY.items():
    assert _t["part"] in PARTS, f"{_s}: unknown Microsoft Learn part"
    assert _t["modules"] and _t["episodes"], f"{_s}: every theme needs at least one module and one episode"
    for _m in _t["modules"]: assert _m in MODULE, f"{_s}: module {_m} is not in PARTS"
    for _e in _t["episodes"]: assert _e in EPISODE_ORDER, f"{_s}: episode {_e} is not a kept episode (EPISODE_ORDER)"
_used_eps = {e for t in THEORY.values() for e in t["episodes"]}
assert _used_eps == set(EPISODE_ORDER), f"kept episodes no theme uses: {set(EPISODE_ORDER) - _used_eps}"

def modules_md(slugs): return " · ".join(f"[{MODULE[m][1]}]({module_url(m)}) (Part {MODULE[m][0]})" for m in slugs)
def episodes_md(slugs): return " · ".join(f"[{EPISODES[e][0]}]({episode_url(e)})" for e in slugs)

# Official thumbnails from the show's episode API (image_url), hotlinked. None = the API image returns 404: no picture.
THUMBS = {
 "creating-your-first-c-program": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-08bc33cd-9b30-4544-9491-bd6d7d769c43/creating-your-first-c-program_960.jpg",
 "understanding-your-first-c-program": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-6321880c-40b1-4d77-8cc6-e43c32c67a06/understanding-your-first-c-program_960.jpg",
 "understanding-data-types-and-variables": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-53ebc4e6-52f1-4de8-9c72-6b6dea73eb7b/understanding-data-types-and-variables_960.jpg",
 "the-if-decision-statement": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-6d088f29-9a6a-4daf-9955-dc6326cd0738/the-if-decision-statement_960.jpg",
 "operators-expressions-and-statements": None,
 "for-iteration-statement": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-d44cd0b2-b866-4b0e-ad02-ee1a7f31157c/for-iteration-statement_960.jpg",
 "understanding-arrays": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-5e3151e9-bb9b-4068-a337-600c4bdd8cb1/understanding-arrays_960.jpg",
 "defining-and-calling-methods": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-c407acc8-05ef-4f09-a1ee-82482fa4d0d1/defining-and-calling-methods_960.jpg",
 "while-iteration-statement": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-4f54adb3-0479-4327-9e48-4ac4c5caf34d/while-iteration-statement_960.jpg",
 "working-with-strings": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-02de69b5-c775-4830-934b-46344ac60ec3/working-with-strings_960.jpg",
 "enumerations-and-the-switch-decision-statement": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-2662ad9f-3f72-49ad-84a9-7737766cf987/enumerations-and-the-switch-decision-statement_960.jpg",
 "gracefully-handling-exceptions": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-b2a0103b-1484-415e-81a6-61a2b54a60b1/gracefully-handling-exceptions_960.jpg",
 "working-with-collections": "https://videoencodingpublic-hgeaeyeba8gycee3.b01.azurefd.net/public-652b0c55-41da-43c3-b9fe-b987ed2a2885/working-with-collections_960.jpg"
}
assert set(THUMBS) == set(EPISODE_ORDER), "every kept episode needs a THUMBS entry (None if there is no official image)"

# Our own short notes for each kept episode: what to watch for, and key words (glossary entries). Never copy the video.
NOTES = {
    "creating-your-first-c-program": (["Where the program starts running.", "How text is printed with `Console.WriteLine`.", "The video uses Visual Studio; in this course you use VS Code and `./ex`, the idea is the same."], ["Method", "Statement"]),
    "understanding-your-first-c-program": (["Each part of the first program, line by line.", "Why every statement ends with `;`.", "What the curly braces `{ }` group together."], ["Statement", "Method"]),
    "understanding-data-types-and-variables": (["A variable is a named box with a type.", "The difference between `int`, `double`, `string` and `bool`.", "Turning text the user typed into a number."], ["Variable", "Type"]),
    "the-if-decision-statement": (["How an `if` tests a Boolean expression.", "When the `else` part runs.", "Comparing with `==`, `<`, `>=`."], ["Boolean expression", "Selection statement"]),
    "operators-expressions-and-statements": (["The arithmetic operators, including `%` (remainder).", "Integer division: `7 / 2` is `3`.", "Short forms like `+=` and `++`."], ["Modulo (`%`)", "Expression"]),
    "enumerations-and-the-switch-decision-statement": (["How `switch` picks one case among many.", "Skip the enumeration part for now: no exercise needs it."], ["Selection statement"]),
    "for-iteration-statement": (["The three parts of a `for`: start, test, step.", "How many times the loop runs, and the value of `i` in each turn.", "Pause the video and trace the loop on paper."], ["Iteration statement", "Iteration", "Trace table"]),
    "while-iteration-statement": (["A `while` loop repeats while its test is true.", "When to use `while` instead of `for`: you do not know the number of turns.", "How to make sure the loop stops."], ["Iteration statement", "Sentinel"]),
    "understanding-arrays": (["Indexes start at 0.", "The last index is `Length - 1`.", "Visiting every element with a loop."], ["Array", "Index"]),
    "working-with-strings": (["A string is text, and you can read it letter by letter.", "Building a new string from pieces.", "Common string helpers; in the exercises, write the loop yourself."], ["String"]),
    "gracefully-handling-exceptions": (["What happens when a program crashes.", "How `try` and `catch` stop the crash.", "Why checking input with `int.TryParse` is often simpler."], ["Exception"]),
    "working-with-collections": (["A `List` can grow, an array cannot.", "Adding items and looping over them with `foreach`.", "Skip anything about LINQ: you do the loops yourself here."], ["List", "foreach"]),
    "defining-and-calling-methods": (["A method has a name, parameters (input) and a return value (result).", "Calling the same method with different values.", "Most exercises here are one method to fill in."], ["Method", "Parameter", "Return value"]),
}
assert set(NOTES) == set(EPISODE_ORDER), "every kept episode needs NOTES"
CERT_SOURCES = [("freeCodeCamp: Earn a Free C# Certification from Microsoft and freeCodeCamp", "https://www.freecodecamp.org/news/free-microsoft-c-sharp-certification/"),
                ("Microsoft .NET Blog: Announcing the New Foundational C# Certification with freeCodeCamp", "https://devblogs.microsoft.com/dotnet/announcing-foundational-csharp-certification/")]
