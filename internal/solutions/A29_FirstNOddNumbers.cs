namespace Practice
{
    // A29 · First n odd numbers
    // Exercise page: exercises/A29-first-n-odd-numbers.md
    public static class A29_FirstNOddNumbers
    {
        public static int SumFirstOdds(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += 2 * i - 1;
            }
            return sum;
        }
    }
}
