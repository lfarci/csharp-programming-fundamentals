// D01 · Last digit
// Exercise: exercises/D01-last-digit.md
// Run: dotnet run solutions/D01-last-digit.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);
Console.WriteLine($"Last digit: {n % 10}");
