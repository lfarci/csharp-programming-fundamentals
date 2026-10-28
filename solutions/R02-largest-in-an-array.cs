// R02 · Largest value in an array
// Exercise: exercises/R02-largest-in-an-array.md
// Run: dotnet run solutions/R02-largest-in-an-array.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("How many numbers? ");
int count = int.Parse(Console.ReadLine()!);
int[] values = new int[count];
for (int i = 0; i < values.Length; i++)
{
    Console.Write($"Value {i}: ");
    values[i] = int.Parse(Console.ReadLine()!);
}

int max = values[0];
int maxIndex = 0;
for (int i = 1; i < values.Length; i++)
{
    if (values[i] > max)
    {
        max = values[i];
        maxIndex = i;
    }
}
Console.WriteLine($"Largest: {max} at index {maxIndex}");
