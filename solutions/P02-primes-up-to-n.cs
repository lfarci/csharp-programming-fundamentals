// P02 · All primes up to N
// Exercise: exercises/P02-primes-up-to-n.md
// Run: dotnet run solutions/P02-primes-up-to-n.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int count = 0;
for (int candidate = 2; candidate <= n; candidate++)
{
    bool isPrime = true;               // reset for every candidate
    for (int d = 2; d * d <= candidate; d++)
    {
        if (candidate % d == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
    {
        Console.Write(candidate + " ");
        count++;
    }
}
Console.WriteLine();
Console.WriteLine($"Count: {count}");
