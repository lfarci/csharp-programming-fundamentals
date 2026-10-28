// A02 · Count multiples of 3
// Exercise: exercises/A02-count-multiples-of-3.md
// Run: dotnet run solutions/A02-count-multiples-of-3.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int count = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 3 == 0)
    {
        count++;
    }
}
Console.WriteLine($"Count: {count}");
