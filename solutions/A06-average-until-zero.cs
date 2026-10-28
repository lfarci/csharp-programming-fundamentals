// A06 · Average until zero
// Exercise: exercises/A06-average-until-zero.md
// Run: dotnet run solutions/A06-average-until-zero.cs   (.NET 10+), or paste into practice/Program.cs

int sum = 0;
int count = 0;
while (true)
{
    Console.Write("Number (0 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == 0)
    {
        break;
    }
    sum += value;
    count++;
}

if (count == 0)
{
    Console.WriteLine("No numbers.");
}
else
{
    double average = (double)sum / count;
    Console.WriteLine($"Average: {average}");
}
