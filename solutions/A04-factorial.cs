// A04 · Factorial
// Exercise: exercises/A04-factorial.md
// Run: dotnet run solutions/A04-factorial.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

long product = 1;
for (int i = 1; i <= n; i++)
{
    product *= i;
}
Console.WriteLine($"{n}! = {product}");
