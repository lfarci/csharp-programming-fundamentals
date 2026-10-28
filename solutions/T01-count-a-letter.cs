// T01 · Count a letter
// Exercise: exercises/T01-count-a-letter.md
// Run: dotnet run solutions/T01-count-a-letter.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Text: ");
string text = Console.ReadLine()!;
Console.Write("Letter: ");
char letter = Console.ReadLine()![0];

int count = 0;
foreach (char c in text)
{
    if (c == letter)
    {
        count++;
    }
}
Console.WriteLine($"{letter} appears {count} times");
