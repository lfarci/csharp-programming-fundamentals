// L03 · Count up and down
// Exercise: exercises/L03-count-up-and-down.md
// Run: dotnet run solutions/L03-count-up-and-down.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

for (int i = 1; i <= n; i++)
{
    Console.Write(i + " ");
}
Console.WriteLine();

for (int i = n; i >= 1; i--)
{
    Console.Write(i + " ");
}
Console.WriteLine();
