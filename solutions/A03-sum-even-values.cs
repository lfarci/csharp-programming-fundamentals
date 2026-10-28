// A03 · Sum of the even numbers
// Exercise: exercises/A03-sum-even-values.md
// Run: dotnet run solutions/A03-sum-even-values.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 2 == 0)
    {
        sum += i;
    }
}
Console.WriteLine($"Sum: {sum}");
