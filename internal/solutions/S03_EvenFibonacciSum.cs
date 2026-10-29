namespace Practice
{
    // S03 · Even Fibonacci sum
    // Exercise page: exercises/S03-even-fibonacci-sum.md
    public static class S03_EvenFibonacciSum
    {
        public static long EvenFibonacciSum(long limit)
        {
            long previous = 0;
            long current = 1;
            long sum = 0;
            while (previous <= limit)
            {
                if (previous % 2 == 0)
                {
                    sum += previous;
                }
                long next = previous + current;
                previous = current;
                current = next;
            }
            return sum;
        }
    }
}
