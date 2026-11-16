namespace Practice
{
    // L20 · Echo until zero
    // Exercise page: exercises/L20-echo-until-zero.md
    public static class L20_EchoUntilZero
    {
        public static void Run()
        {
            while (true)
            {
                Console.Write("Number (0 to stop): ");
                int value = int.Parse(Console.ReadLine()!);
                if (value == 0)
                {
                    break;
                }
                Console.WriteLine($"You typed {value}");
            }
            Console.WriteLine("Bye.");
        }
    }
}
