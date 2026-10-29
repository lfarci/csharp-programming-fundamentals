namespace Practice
{
    // M02 · Armstrong in a range
    // Exercise page: exercises/M02-armstrong-numbers-in-a-range.md
    public static class M02_ArmstrongNumbersInARange
    {
        public static void Run()
        {
            Console.Write("From: ");
            int lower = int.Parse(Console.ReadLine()!);
            Console.Write("To: ");
            int upper = int.Parse(Console.ReadLine()!);

            for (int candidate = lower; candidate <= upper; candidate++)
            {
                int digits = 0;
                int remaining = candidate;
                do
                {
                    digits++;
                    remaining /= 10;
                }
                while (remaining > 0);

                int sum = 0;
                remaining = candidate;
                while (remaining > 0)
                {
                    int digit = remaining % 10;
                    int power = 1;
                    for (int i = 0; i < digits; i++)
                    {
                        power *= digit;
                    }
                    sum += power;
                    remaining /= 10;
                }

                if (sum == candidate)
                {
                    Console.Write(candidate + " ");
                }
            }
            Console.WriteLine();
        }
    }
}
