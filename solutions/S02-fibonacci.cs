// S02 · Fibonacci
// Exercise: exercises/S02-fibonacci.md
// Run: dotnet run solutions/S02-fibonacci.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

long previous = 0;
long current = 1;
for (int i = 0; i < n; i++)
{
    Console.Write(previous + " ");
    long next = previous + current;
    previous = current;
    current = next;
}
Console.WriteLine();
