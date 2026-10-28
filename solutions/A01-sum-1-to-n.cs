// A01 · Sum from 1 to N
// Exercise: exercises/A01-sum-1-to-n.md
// Run: dotnet run solutions/A01-sum-1-to-n.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += i;
}
Console.WriteLine($"Sum: {sum}");
