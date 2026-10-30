namespace Practice
{
    // E01 · Safe number reader
    // Exercise page: exercises/E01-safe-number-reader.md
    public static class E01_SafeNumberReader
    {
        public static void Run()
        {
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
                catch (OverflowException)
                {
                    Console.WriteLine("That number is too big.");
                }
            }
            Console.WriteLine($"Thanks: {number}");
        }
    }
}
