// D02 · Remove the last digit
// Exercise: exercises/D02-remove-last-digit.md
// Run: dotnet run solutions/D02-remove-last-digit.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);
Console.WriteLine($"Without last digit: {n / 10}");
