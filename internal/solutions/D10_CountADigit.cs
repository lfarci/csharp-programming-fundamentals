namespace Practice
{
    // D10 · Count one digit
    // Exercise page: exercises/D10-count-a-digit.md
    public static class D10_CountADigit
    {
        public static int CountDigit(int n, int digit)
        {
            int count = 0;
            while (n > 0)
            {
                if (n % 10 == digit)
                {
                    count++;
                }
                n /= 10;
            }
            return count;
        }
    }
}
