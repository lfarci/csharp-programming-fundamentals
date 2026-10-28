// K01 · Shopping list
// Exercise: exercises/K01-shopping-list.md
// Run: dotnet run solutions/K01-shopping-list.cs   (.NET 10+), or paste into practice/Program.cs

List<string> items = new List<string>();
while (true)
{
    Console.Write("Item (done to stop): ");
    string item = Console.ReadLine()!;
    if (item == "done")
    {
        break;
    }
    items.Add(item);
}

for (int i = 0; i < items.Count; i++)
{
    Console.WriteLine($"{i + 1}. {items[i]}");
}
Console.WriteLine($"Total: {items.Count} items");
