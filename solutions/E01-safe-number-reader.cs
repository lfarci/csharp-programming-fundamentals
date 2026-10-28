// E01 · Safe number reader
// Exercise: exercises/E01-safe-number-reader.md
// Run: dotnet run solutions/E01-safe-number-reader.cs   (.NET 10+), or paste into practice/Program.cs

int number;
while (true)
{
    Console.Write("Whole number: ");
    try
    {
        number = int.Parse(Console.ReadLine()!);
        break;
    }
    catch (FormatException)
    {
        Console.WriteLine("That is not a number.");
    }
}
Console.WriteLine($"Thanks: {number}");
