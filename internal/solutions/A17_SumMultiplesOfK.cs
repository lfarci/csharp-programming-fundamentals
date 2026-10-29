namespace Practice
{
    // A17 · Sum the multiples of k
    // Exercise page: exercises/A17-sum-multiples-of-k.md
    public static class A17_SumMultiplesOfK
    {
        public static int SumMultiplesOf(int k, int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                if (i % k == 0)
                {
                    sum += i;
                }
            }
            return sum;
        }
    }
}
