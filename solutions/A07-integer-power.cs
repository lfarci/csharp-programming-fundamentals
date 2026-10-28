// A07 · Integer power
// Exercise: exercises/A07-integer-power.md
// Run: dotnet run solutions/A07-integer-power.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Base: ");
int baseValue = int.Parse(Console.ReadLine()!);
Console.Write("Exponent: ");
int exponent = int.Parse(Console.ReadLine()!);

long result = 1;
for (int i = 0; i < exponent; i++)
{
    result *= baseValue;
}
Console.WriteLine($"{baseValue}^{exponent} = {result}");
