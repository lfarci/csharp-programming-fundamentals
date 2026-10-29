namespace Practice
{
    // P06 · Smallest divisor
    // Exercise page: exercises/P06-smallest-divisor.md
    public static class P06_SmallestDivisor
    {
        public static int SmallestDivisor(int n)
        {
            int divisor = n;
            for (int d = 2; d < n; d++)
            {
                if (n % d == 0)
                {
                    divisor = d;
                    break;
                }
            }
            return divisor;
        }
    }
}
