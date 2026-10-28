// A10 · Sum of a series
// Exercise: exercises/A10-sum-of-a-series.md
// Run: dotnet run solutions/A10-sum-of-a-series.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

double sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += 1.0 / i;   // 1.0 makes it a double division
}
Console.WriteLine($"Sum: {sum:F4}");
