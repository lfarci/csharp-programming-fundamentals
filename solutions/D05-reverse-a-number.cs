// D05 · Reverse a number
// Exercise: exercises/D05-reverse-a-number.md
// Run: dotnet run solutions/D05-reverse-a-number.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int reversed = 0;
int remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    reversed = reversed * 10 + digit;
    remaining /= 10;
}
Console.WriteLine($"Reversed: {reversed}");
