namespace Practice
{
    // S02 · Fibonacci
    // Exercise page: exercises/S02-fibonacci.md
    public static class S02_Fibonacci
    {
        public static void Run()
        {
            Console.Write("N: ");
            int n = int.Parse(Console.ReadLine()!);

            long previous = 0;
            long current = 1;
            for (int i = 0; i < n; i++)
            {
                Console.Write(previous + " ");
                long next = previous + current;
                previous = current;
                current = next;
            }
            Console.WriteLine();
        }
    }
}
