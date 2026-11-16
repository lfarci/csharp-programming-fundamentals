"""Sentinel-loop drills added on 2026-11-16 (original text and code, written for this course).
The group "Until the user stops" opened with an Independent exercise (L05) and recipe 10 had only 3 exercises
and no drill set. These Guided and Independent drills keep the same loop (read, test the stop value, use it)
and change one thing each:
- L20 Echo until zero: the bare pattern, print each value back.
- L21 Sum until -1: the same loop, with a sum box (recipe 2); the stop value is -1, so adding it by mistake shows in the result.
- L22 Words until stop: the stop value is a word, compared with `==`.
"""
from data4 import ex

ex(id="L20", slug="echo-until-zero", title="Echo until zero", level="Guided", stars=1, recipes=["10"], pre=["L03"],
   goal="Read whole numbers one by one. For each one, print `You typed X`. Stop when the user types 0, then print `Bye.`",
   examples=[(["5", "8", "0"], ["You typed 5", "You typed 8", "Bye."]), (["-3", "0"], ["You typed -3", "Bye."]), (["0"], ["Bye."])],
   edge=["The first number is already 0: only `Bye.` is printed.", "The 0 itself is not echoed: try it with `./ex run L20`."],
   constraints=["You do not know how many numbers will come: use `while (true)` and `break`."],
   hints=["This is the [sentinel loop](../cookbook/10-sentinel-loop.md). 0 is the sentinel.",
          "In the loop, in this order: read, `if (value == 0) break;`, then print.",
          "`Bye.` comes after the loop, so it is printed once."],
   mastery="For each number, print `You typed X (even)` or `You typed X (odd)`.",
   code=r'''while (true)
{
    Console.Write("Number (0 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == 0)
    {
        break;
    }
    Console.WriteLine($"You typed {value}");
}
Console.WriteLine("Bye.");
''')

ex(id="L21", slug="sum-until-minus-one", title="Sum until -1", level="Guided", stars=1, recipes=["10", "02"], pre=["L20", "A01"],
   goal="Read points (whole numbers, 0 or more) until the user types -1. Print their sum.",
   examples=[(["4", "7", "1", "-1"], ["Sum: 12"]), (["10", "0", "5", "-1"], ["Sum: 15"]), (["-1"], ["Sum: 0"])],
   edge=["The first number is already -1: the sum is 0.", "0 is a normal value here: only -1 stops.", "-1 is not added: 4, 7, 1 give 12, not 11."],
   constraints=["Sentinel loop + one box (`sum`). The sentinel is -1, not 0."],
   hints=["L20 with a box: `int sum = 0;` **before** the loop.",
          "The sentinel test is `if (value == -1) break;`. Then, after it: `sum += value;`.",
          "Print the sum once, **after** the loop."],
   mastery="Also print how many points were 0.",
   code=r'''int sum = 0;
while (true)
{
    Console.Write("Points (-1 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == -1)
    {
        break;
    }
    sum += value;
}
Console.WriteLine($"Sum: {sum}");
''')

ex(id="L22", slug="words-until-stop", title="Words until stop", level="Independent", stars=2, recipes=["10"], pre=["L05"],
   goal="Read words one by one. Stop when the user types `stop`. Print how many words came before it.",
   examples=[(["cat", "dog", "stop"], ["You typed 2 words."]), (["red", "green", "blue", "stop"], ["You typed 3 words."]), (["stop"], ["You typed 0 words."])],
   edge=["The first word is already `stop`: 0 words.", "`stop` itself is not counted."],
   constraints=["Same loop as L05; only the stop test changes."],
   hints=["Read the text as it is: `string word = Console.ReadLine()!;` (no `int.Parse`).",
          "The sentinel test compares text: `if (word == \"stop\") break;`."],
   mastery="Also print the longest word (`word.Length`).",
   code=r'''int count = 0;
while (true)
{
    Console.Write("Word (stop to end): ");
    string word = Console.ReadLine()!;
    if (word == "stop")
    {
        break;
    }
    count++;
}
Console.WriteLine($"You typed {count} words.");
''')
