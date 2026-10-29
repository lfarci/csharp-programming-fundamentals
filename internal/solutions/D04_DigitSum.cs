namespace Practice
{
    // D04 · Sum of the digits
    // Exercise page: exercises/D04-digit-sum.md
    public static class D04_DigitSum
    {
        public static int DigitSum(int n)
        {
            int sum = 0;
            int remaining = n;
            while (remaining > 0)
            {
                int digit = remaining % 10;
                sum += digit;
                remaining /= 10;
            }
            return sum;
        }
    }
}
