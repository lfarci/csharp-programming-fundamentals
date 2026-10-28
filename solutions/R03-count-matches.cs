// R03 · Count matches in an array
// Exercise: exercises/R03-count-matches.md
// Run: dotnet run solutions/R03-count-matches.cs   (.NET 10+), or paste into practice/Program.cs

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

int matches = 0;
foreach (int value in values)
{
    if (value == target)
    {
        matches++;
    }
}
Console.WriteLine($"{target} appears {matches} times");
