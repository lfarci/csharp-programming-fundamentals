// D06 · Palindrome number
// Exercise: exercises/D06-palindrome-number.md
// Run: dotnet run solutions/D06-palindrome-number.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int reversed = 0;
int remaining = n;          // copy: we need n at the end
while (remaining > 0)
{
    reversed = reversed * 10 + remaining % 10;
    remaining /= 10;
}

if (reversed == n)
{
    Console.WriteLine($"{n} is a palindrome");
}
else
{
    Console.WriteLine($"{n} is not a palindrome");
}
