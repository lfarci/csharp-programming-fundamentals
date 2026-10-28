// G04 · Hollow rectangle
// Exercise: exercises/G04-hollow-rectangle.md
// Run: dotnet run solutions/G04-hollow-rectangle.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= width; col++)
    {
        if (row == 1 || row == height || col == 1 || col == width)
        {
            Console.Write("*");
        }
        else
        {
            Console.Write(" ");
        }
    }
    Console.WriteLine();
}
