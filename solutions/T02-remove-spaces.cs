// T02 · Remove spaces
// Exercise: exercises/T02-remove-spaces.md
// Run: dotnet run solutions/T02-remove-spaces.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Text: ");
string text = Console.ReadLine()!;

string result = "";
foreach (char c in text)
{
    if (c != ' ')
    {
        result += c;
    }
}
Console.WriteLine($"[{result}]");
