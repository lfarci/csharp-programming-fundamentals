// G01 · Draw a rectangle
// Exercise: exercises/G01-rectangle.md
// Run: dotnet run solutions/G01-rectangle.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= width; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}
