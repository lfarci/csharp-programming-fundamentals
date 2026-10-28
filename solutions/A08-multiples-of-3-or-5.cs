// A08 · Multiples of 3 or 5
// Exercise: exercises/A08-multiples-of-3-or-5.md
// Run: dotnet run solutions/A08-multiples-of-3-or-5.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
for (int i = 1; i < n; i++)
{
    if (i % 3 == 0 || i % 5 == 0)
    {
        sum += i;
    }
}
Console.WriteLine($"Sum: {sum}");
