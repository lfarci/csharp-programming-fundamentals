// L05 · Until zero
// Exercise: exercises/L05-until-zero.md
// Run: dotnet run solutions/L05-until-zero.cs   (.NET 10+), or paste into practice/Program.cs

int count = 0;
while (true)
{
    Console.Write("Number (0 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == 0)
    {
        break;
    }
    count++;
}
Console.WriteLine($"You entered {count} numbers.");
