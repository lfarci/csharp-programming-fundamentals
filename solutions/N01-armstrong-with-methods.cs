// N01 · Armstrong with methods
// Exercise: exercises/N01-armstrong-with-methods.md
// Run: dotnet run solutions/N01-armstrong-with-methods.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("From: ");
int lower = int.Parse(Console.ReadLine()!);
Console.Write("To: ");
int upper = int.Parse(Console.ReadLine()!);

for (int candidate = lower; candidate <= upper; candidate++)
{
    if (IsArmstrong(candidate))
    {
        Console.Write(candidate + " ");
    }
}
Console.WriteLine();

static int CountDigits(int n)
{
    int digits = 0;
    do
    {
        digits++;
        n /= 10;
    }
    while (n > 0);
    return digits;
}

static int Power(int baseValue, int exponent)
{
    int result = 1;
    for (int i = 0; i < exponent; i++)
    {
        result *= baseValue;
    }
    return result;
}

static bool IsArmstrong(int n)
{
    int digits = CountDigits(n);
    int sum = 0;
    int remaining = n;
    while (remaining > 0)
    {
        sum += Power(remaining % 10, digits);
        remaining /= 10;
    }
    return sum == n;
}
