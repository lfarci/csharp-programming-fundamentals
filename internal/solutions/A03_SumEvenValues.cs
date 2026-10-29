namespace Practice
{
    // A03 · Sum of the even numbers
    // Exercise page: exercises/A03-sum-even-values.md
    public static class A03_SumEvenValues
    {
        public static int SumOfEvens(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                if (i % 2 == 0)
                {
                    sum += i;
                }
            }
            return sum;
        }
    }
}
