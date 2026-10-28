// R04 · Find the position
// Exercise: exercises/R04-find-the-position.md
// Run: dotnet run solutions/R04-find-the-position.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("How many numbers? ");
int count = int.Parse(Console.ReadLine()!);
int[] values = new int[count];
for (int i = 0; i < values.Length; i++)
{
    Console.Write($"Value {i}: ");
    values[i] = int.Parse(Console.ReadLine()!);
}

Console.Write("Target: ");
int target = int.Parse(Console.ReadLine()!);

int index = -1;
for (int i = 0; i < values.Length; i++)
{
    if (values[i] == target)
    {
        index = i;
        break;
    }
}

if (index == -1)
{
    Console.WriteLine("Not found");
}
else
{
    Console.WriteLine($"First position: {index}");
}
