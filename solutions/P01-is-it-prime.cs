// P01 · Is it prime?
// Exercise: exercises/P01-is-it-prime.md
// Run: dotnet run solutions/P01-is-it-prime.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

bool isPrime = n >= 2;
for (int d = 2; d * d <= n; d++)
{
    if (n % d == 0)
    {
        isPrime = false;
        break;
    }
}

Console.WriteLine(isPrime ? $"{n} is prime" : $"{n} is not prime");
