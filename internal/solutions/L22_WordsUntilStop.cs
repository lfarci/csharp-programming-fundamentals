namespace Practice
{
    // L22 · Words until stop
    // Exercise page: exercises/L22-words-until-stop.md
    public static class L22_WordsUntilStop
    {
        public static void Run()
        {
            int count = 0;
            while (true)
            {
                Console.Write("Word (stop to end): ");
                string word = Console.ReadLine()!;
                if (word == "stop")
                {
                    break;
                }
                count++;
            }
            Console.WriteLine($"You typed {count} words.");
        }
    }
}
