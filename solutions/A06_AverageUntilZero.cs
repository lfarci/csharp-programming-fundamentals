namespace Practice
{
    // A06 · Average until zero
    // Exercise page: exercises/A06-average-until-zero.md
    public static class A06_AverageUntilZero
    {
        public static void Run()
        {
            int sum = 0;
            int count = 0;
            while (true)
            {
                Console.Write("Number (0 to stop): ");
                int value = int.Parse(Console.ReadLine()!);
                if (value == 0)
                {
                    break;
                }
                sum += value;
                count++;
            }

            if (count == 0)
            {
                Console.WriteLine("No numbers.");
            }
            else
            {
                double average = (double)sum / count;
                Console.WriteLine($"Average: {average}");
            }
        }
    }
}
