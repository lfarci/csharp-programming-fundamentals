// B03 · Seconds to hours, minutes, seconds
// Exercise: exercises/B03-seconds-to-hms.md
// Run: dotnet run solutions/B03-seconds-to-hms.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("Seconds: ");
int total = int.Parse(Console.ReadLine()!);

int hours = total / 3600;
int rest = total % 3600;
int minutes = rest / 60;
int seconds = rest % 60;

Console.WriteLine($"{hours} h {minutes} min {seconds} s");
