namespace Practice
{
    // L21 · Sum until -1
    // Exercise page: exercises/L21-sum-until-minus-one.md
    public static class L21_SumUntilMinusOne
    {
        public static void Run()
        {
            int sum = 0;
            while (true)
            {
                Console.Write("Points (-1 to stop): ");
                int value = int.Parse(Console.ReadLine()!);
                if (value == -1)
                {
                    break;
                }
                sum += value;
            }
            Console.WriteLine($"Sum: {sum}");
        }
    }
}
