namespace Practice
{
    // A34 · Sum of a times table
    // Exercise page: exercises/A34-sum-of-a-times-table.md
    public static class A34_SumOfATimesTable
    {
        public static int SumOfTable(int k, int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += k * i;
            }
            return sum;
        }
    }
}
