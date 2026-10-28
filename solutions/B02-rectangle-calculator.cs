// B02 · Rectangle calculator
// Exercise: exercises/B02-rectangle-calculator.md
// Run: dotnet run solutions/B02-rectangle-calculator.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

int area = width * height;
int perimeter = 2 * (width + height);

Console.WriteLine($"Area: {area}");
Console.WriteLine($"Perimeter: {perimeter}");
