// L08 · Guess the number
// Exercise: exercises/L08-guess-the-number.md
// Run: dotnet run solutions/L08-guess-the-number.cs   (.NET 10+), or paste into practice/Program.cs

int secret = 42;     // later: Random.Shared.Next(1, 101)
int tries = 0;
int guess;
do
{
    Console.Write("Your guess: ");
    guess = int.Parse(Console.ReadLine()!);
    tries++;
    if (guess < secret)
    {
        Console.WriteLine("Higher!");
    }
    else if (guess > secret)
    {
        Console.WriteLine("Lower!");
    }
}
while (guess != secret);

Console.WriteLine($"Correct! You needed {tries} tries.");
