namespace Practice
{
    // A22 · Sum of the divisors
    // Exercise page: exercises/A22-sum-of-divisors.md
    public static class A22_SumOfDivisors
    {
        public static int SumOfDivisors(int n)
        {
            int sum = 0;
            for (int d = 1; d <= n; d++)
            {
                if (n % d == 0)
                {
                    sum += d;
                }
            }
            return sum;
        }
    }
}
