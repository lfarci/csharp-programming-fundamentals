namespace Practice
{
    // A30 · Power of 10
    // Exercise page: exercises/A30-power-of-10.md
    public static class A30_PowerOf10
    {
        public static long PowerOf10(int n)
        {
            long result = 1;
            for (int i = 1; i <= n; i++)
            {
                result *= 10;
            }
            return result;
        }
    }
}
