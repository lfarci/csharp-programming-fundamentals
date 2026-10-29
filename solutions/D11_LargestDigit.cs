namespace Practice
{
    // D11 · Largest digit
    // Exercise page: exercises/D11-largest-digit.md
    public static class D11_LargestDigit
    {
        public static int LargestDigit(int n)
        {
            int max = 0;
            while (n > 0)
            {
                if (n % 10 > max)
                {
                    max = n % 10;
                }
                n /= 10;
            }
            return max;
        }
    }
}
