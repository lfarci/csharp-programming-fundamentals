namespace Practice
{
    // A28 · Sum of i × (i + 1)
    // Exercise page: exercises/A28-sum-of-pairs.md
    public static class A28_SumOfPairs
    {
        public static int SumOfPairs(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += i * (i + 1);
            }
            return sum;
        }
    }
}
