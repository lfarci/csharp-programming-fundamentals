// G05 · Checkerboard
// Exercise: exercises/G05-checkerboard.md
// Run: dotnet run solutions/G05-checkerboard.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Size: ");
int size = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= size; row++)
{
    for (int col = 1; col <= size; col++)
    {
        if ((row + col) % 2 == 0)
        {
            Console.Write("#");
        }
        else
        {
            Console.Write(".");
        }
    }
    Console.WriteLine();
}
