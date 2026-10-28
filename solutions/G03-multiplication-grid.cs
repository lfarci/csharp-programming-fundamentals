// G03 · Multiplication grid
// Exercise: exercises/G03-multiplication-grid.md
// Run: dotnet run solutions/G03-multiplication-grid.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= n; row++)
{
    for (int col = 1; col <= n; col++)
    {
        Console.Write($"{row * col,4}");
    }
    Console.WriteLine();
}
