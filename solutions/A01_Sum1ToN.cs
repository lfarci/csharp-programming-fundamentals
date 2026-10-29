namespace Practice
{
    // A01 · Sum from 1 to N
    // Exercise page: exercises/A01-sum-1-to-n.md
    public static class A01_Sum1ToN
    {
        public static int SumTo(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += i;
            }
            return sum;
        }
    }
}
