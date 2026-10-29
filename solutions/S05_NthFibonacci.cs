namespace Practice
{
    // S05 · The n-th Fibonacci number
    // Exercise page: exercises/S05-nth-fibonacci.md
    public static class S05_NthFibonacci
    {
        public static long Fibonacci(int n)
        {
            long previous = 0;
            long current = 1;
            for (int i = 0; i < n; i++)
            {
                long next = previous + current;
                previous = current;
                current = next;
            }
            return previous;
        }
    }
}
