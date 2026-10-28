// C02 · Largest of three
// Exercise: exercises/C02-largest-of-three.md
// Run: dotnet run solutions/C02-largest-of-three.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("First: ");
int a = int.Parse(Console.ReadLine()!);
Console.Write("Second: ");
int b = int.Parse(Console.ReadLine()!);
Console.Write("Third: ");
int c = int.Parse(Console.ReadLine()!);

int largest = a;
if (b > largest)
{
    largest = b;
}
if (c > largest)
{
    largest = c;
}

Console.WriteLine($"Largest: {largest}");
