// R01 · Sum of an array
// Exercise: exercises/R01-sum-an-array.md
// Run: dotnet run solutions/R01-sum-an-array.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("How many numbers? ");
int count = int.Parse(Console.ReadLine()!);
int[] values = new int[count];
for (int i = 0; i < values.Length; i++)
{
    Console.Write($"Value {i}: ");
    values[i] = int.Parse(Console.ReadLine()!);
}

int sum = 0;
foreach (int value in values)
{
    sum += value;
}
Console.WriteLine($"Sum: {sum}");
