// B01 · Hello you
// Exercise: exercises/B01-hello-you.md
// Run: dotnet run solutions/B01-hello-you.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("What is your name? ");
string name = Console.ReadLine()!;
Console.WriteLine($"Hello, {name}!");
