// A05 · Two accumulators: sum and squares
// Exercise: exercises/A05-sum-square-difference.md
// Run: dotnet run solutions/A05-sum-square-difference.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

long sum = 0;
long squares = 0;
for (int i = 1; i <= n; i++)
{
    sum += i;
    squares += i * i;
}
Console.WriteLine($"Sum: {sum}");
Console.WriteLine($"Sum of squares: {squares}");
Console.WriteLine($"Difference: {sum * sum - squares}");
