namespace Practice
{
    // A26 · Sum of tens
    // Exercise page: exercises/A26-sum-of-tens.md
    public static class A26_SumOfTens
    {
        public static int SumOfTens(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += i * 10;
            }
            return sum;
        }
    }
}
