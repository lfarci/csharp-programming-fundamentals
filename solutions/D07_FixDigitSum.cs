namespace Practice
{
    // D07 · Fix: digit sum
    // Exercise page: exercises/D07-fix-digit-sum.md
    public static class D07_FixDigitSum
    {
        public static int DigitSum(int n)
        {
            int sum = 0;
            while (n > 0)
            {
                sum += n % 10;
                n = n / 10;
            }
            return sum;
        }
    }
}
