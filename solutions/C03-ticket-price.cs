// C03 · Ticket price
// Exercise: exercises/C03-ticket-price.md
// Run: dotnet run solutions/C03-ticket-price.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Age: ");
int age = int.Parse(Console.ReadLine()!);

int price;
if (age < 12)
{
    price = 5;
}
else if (age >= 65)
{
    price = 7;
}
else
{
    price = 10;
}

Console.WriteLine($"Price: {price}");
