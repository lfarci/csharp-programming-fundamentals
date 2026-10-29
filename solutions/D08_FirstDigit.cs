namespace Practice
{
    // D08 · First digit
    // Exercise page: exercises/D08-first-digit.md
    public static class D08_FirstDigit
    {
        public static int FirstDigit(int n)
        {
            while (n >= 10)
            {
                n /= 10;
            }
            return n;
        }
    }
}
