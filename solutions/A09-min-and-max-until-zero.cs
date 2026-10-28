// A09 · Smallest and largest until zero
// Exercise: exercises/A09-min-and-max-until-zero.md
// Run: dotnet run solutions/A09-min-and-max-until-zero.cs   (.NET 10+), or paste into practice/Program.cs

int count = 0;
int min = 0;
int max = 0;
while (true)
{
    Console.Write("Number (0 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == 0)
    {
        break;
    }
    count++;
    if (count == 1)
    {
        min = value;   // the first value is both the smallest and the largest so far
        max = value;
    }
    else
    {
        if (value < min) min = value;
        if (value > max) max = value;
    }
}

if (count == 0)
{
    Console.WriteLine("No numbers.");
}
else
{
    Console.WriteLine($"Min: {min}");
    Console.WriteLine($"Max: {max}");
}
