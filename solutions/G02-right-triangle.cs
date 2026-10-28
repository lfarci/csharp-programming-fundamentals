// G02 · Draw a right triangle
// Exercise: exercises/G02-right-triangle.md
// Run: dotnet run solutions/G02-right-triangle.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= row; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}
