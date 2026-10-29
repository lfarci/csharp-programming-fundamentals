namespace Practice
{
    // L08 · Guess the number
    // Exercise page: exercises/L08-guess-the-number.md
    public static class L08_GuessTheNumber
    {
        public static void Run()
        {
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
        }
    }
}
