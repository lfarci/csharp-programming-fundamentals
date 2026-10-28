// S03 · Even Fibonacci sum
// Exercise: exercises/S03-even-fibonacci-sum.md
// Run: dotnet run solutions/S03-even-fibonacci-sum.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Limit: ");
long limit = long.Parse(Console.ReadLine()!);

long previous = 0;
long current = 1;
long sum = 0;
while (previous <= limit)
{
    if (previous % 2 == 0)
    {
        sum += previous;
    }
    long next = previous + current;
    previous = current;
    current = next;
}
Console.WriteLine($"Sum: {sum}");
