// L04 · Multiplication table
// Exercise: exercises/L04-multiplication-table.md
// Run: dotnet run solutions/L04-multiplication-table.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

for (int i = 1; i <= 10; i++)
{
    Console.WriteLine($"{n} x {i} = {n * i}");
}
