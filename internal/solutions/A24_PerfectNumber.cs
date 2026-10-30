namespace Practice
{
    // A24 · Perfect number
    // Exercise page: exercises/A24-perfect-number.md
    public static class A24_PerfectNumber
    {
        public static bool IsPerfect(int n)
        {
            int sum = 0;
            for (int d = 1; d < n; d++)
            {
                if (n % d == 0)
                {
                    sum += d;
                }
            }
            return sum == n;
        }
    }
}
