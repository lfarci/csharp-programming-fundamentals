// D03 · Count the digits
// Exercise: exercises/D03-count-digits.md
// Run: dotnet run solutions/D03-count-digits.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int digits = 0;
int remaining = n;
do
{
    digits++;
    remaining /= 10;
}
while (remaining > 0);

Console.WriteLine($"Digits: {digits}");
