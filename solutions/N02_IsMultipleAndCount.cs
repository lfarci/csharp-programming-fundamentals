namespace Practice
{
    // N02 · A method that calls one
    // Exercise page: exercises/N02-is-multiple-and-count.md
    public static class N02_IsMultipleAndCount
    {
        public static bool IsMultiple(int n, int k)
        {
            return n % k == 0;
        }

        public static int CountMultiples(int n, int k)
        {
            int count = 0;
            for (int i = 1; i <= n; i++)
            {
                if (IsMultiple(i, k))
                {
                    count++;
                }
            }
            return count;
        }
    }
}
