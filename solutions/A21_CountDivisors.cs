namespace Practice
{
    // A21 · Count the divisors
    // Exercise page: exercises/A21-count-divisors.md
    public static class A21_CountDivisors
    {
        public static int CountDivisors(int n)
        {
            int count = 0;
            for (int d = 1; d <= n; d++)
            {
                if (n % d == 0)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
