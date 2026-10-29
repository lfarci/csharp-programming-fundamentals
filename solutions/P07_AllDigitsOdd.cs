namespace Practice
{
    // P07 · All digits odd
    // Exercise page: exercises/P07-all-digits-odd.md
    public static class P07_AllDigitsOdd
    {
        public static bool AllDigitsOdd(int n)
        {
            bool allOdd = true;
            while (n > 0)
            {
                if (n % 10 % 2 == 0)
                {
                    allOdd = false;
                }
                n /= 10;
            }
            return allOdd;
        }
    }
}
