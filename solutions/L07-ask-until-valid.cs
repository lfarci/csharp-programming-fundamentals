// L07 · Ask until valid
// Exercise: exercises/L07-ask-until-valid.md
// Run: dotnet run solutions/L07-ask-until-valid.cs   (.NET 10+), or paste into practice/Program.cs

int number;
bool valid;
do
{
    Console.Write("Number between 1 and 10: ");
    string? text = Console.ReadLine();
    valid = int.TryParse(text, out number) && number >= 1 && number <= 10;
    if (!valid)
    {
        Console.WriteLine("Invalid, try again.");
    }
}
while (!valid);

Console.WriteLine($"You chose {number}");
