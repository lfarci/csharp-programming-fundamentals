// T03 · Count and keep the digits
// Exercise: exercises/T03-count-and-keep-digits.md
// Run: dotnet run solutions/T03-count-and-keep-digits.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Text: ");
string text = Console.ReadLine()!;

int count = 0;
string kept = "";
foreach (char c in text)
{
    if (c >= '0' && c <= '9')
    {
        count++;
        kept += c;
    }
}
Console.WriteLine($"Digits: {count}");
Console.WriteLine($"Kept: {kept}");
