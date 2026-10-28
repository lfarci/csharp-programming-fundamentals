// C01 · Even or odd
// Exercise: exercises/C01-even-or-odd.md
// Run: dotnet run solutions/C01-even-or-odd.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Number: ");
int n = int.Parse(Console.ReadLine()!);

if (n % 2 == 0)
{
    Console.WriteLine($"{n} is even");
}
else
{
    Console.WriteLine($"{n} is odd");
}
