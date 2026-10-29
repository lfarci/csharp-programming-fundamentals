namespace Practice
{
    // A20 · Power of 2
    // Exercise page: exercises/A20-powers-of-2.md
    public static class A20_PowersOf2
    {
        public static long PowerOf2(int n)
        {
            long result = 1;
            for (int i = 1; i <= n; i++)
            {
                result *= 2;
            }
            return result;
        }
    }
}
