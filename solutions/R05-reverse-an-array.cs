// R05 · Reverse an array
// Exercise: exercises/R05-reverse-an-array.md
// Run: dotnet run solutions/R05-reverse-an-array.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("How many numbers? ");
int count = int.Parse(Console.ReadLine()!);
int[] values = new int[count];
for (int i = 0; i < values.Length; i++)
{
    Console.Write($"Value {i}: ");
    values[i] = int.Parse(Console.ReadLine()!);
}

int[] reversed = new int[values.Length];
for (int i = 0; i < values.Length; i++)
{
    reversed[values.Length - 1 - i] = values[i];
}

foreach (int value in reversed)
{
    Console.Write(value + " ");
}
Console.WriteLine();
