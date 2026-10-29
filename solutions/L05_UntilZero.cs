namespace Practice
{
    // L05 · Until zero
    // Exercise page: exercises/L05-until-zero.md
    public static class L05_UntilZero
    {
        public static void Run()
        {
            int count = 0;
            while (true)
            {
                Console.Write("Number (0 to stop): ");
                int value = int.Parse(Console.ReadLine()!);
                if (value == 0)
                {
                    break;
                }
                count++;
            }
            Console.WriteLine($"You entered {count} numbers.");
        }
    }
}
