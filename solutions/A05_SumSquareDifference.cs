namespace Practice
{
    // A05 · Two accumulators: sum and squares
    // Exercise page: exercises/A05-sum-square-difference.md
    public static class A05_SumSquareDifference
    {
        public static void Run()
        {
            Console.Write("N: ");
            int n = int.Parse(Console.ReadLine()!);

            long sum = 0;
            long squares = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += i;
                squares += i * i;
            }
            Console.WriteLine($"Sum: {sum}");
            Console.WriteLine($"Sum of squares: {squares}");
            Console.WriteLine($"Difference: {sum * sum - squares}");
        }
    }
}
