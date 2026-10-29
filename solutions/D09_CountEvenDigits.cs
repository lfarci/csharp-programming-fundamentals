namespace Practice
{
    // D09 · Count the even digits
    // Exercise page: exercises/D09-count-even-digits.md
    public static class D09_CountEvenDigits
    {
        public static int CountEvenDigits(int n)
        {
            int count = 0;
            while (n > 0)
            {
                if (n % 10 % 2 == 0)
                {
                    count++;
                }
                n /= 10;
            }
            return count;
        }
    }
}
