namespace Practice
{
    // A10 · Sum of a series
    // Exercise page: exercises/A10-sum-of-a-series.md
    public static class A10_SumOfASeries
    {
        public static double SeriesSum(int n)
        {
            double sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += 1.0 / i;   // 1.0 makes it a double division
            }
            return sum;
        }
    }
}
