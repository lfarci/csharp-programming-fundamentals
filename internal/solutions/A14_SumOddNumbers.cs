namespace Practice
{
    // A14 · Sum the odd numbers
    // Exercise page: exercises/A14-sum-odd-numbers.md
    public static class A14_SumOddNumbers
    {
        public static int SumOfOdds(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i += 2)
            {
                sum += i;
            }
            return sum;
        }
    }
}
