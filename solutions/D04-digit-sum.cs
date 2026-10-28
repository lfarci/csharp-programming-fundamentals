// D04 · Sum of the digits
// Exercise: exercises/D04-digit-sum.md
// Run: dotnet run solutions/D04-digit-sum.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
int remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    sum += digit;
    remaining /= 10;
}
Console.WriteLine($"Digit sum: {sum}");
