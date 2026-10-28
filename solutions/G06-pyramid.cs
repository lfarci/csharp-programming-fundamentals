// G06 · Pyramid
// Exercise: exercises/G06-pyramid.md
// Run: dotnet run solutions/G06-pyramid.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int s = 1; s <= height - row; s++)
    {
        Console.Write(" ");
    }
    for (int star = 1; star <= 2 * row - 1; star++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}
