namespace Practice
{
    // P04 · Has an even digit
    // Exercise page: exercises/P04-has-an-even-digit.md
    public static class P04_HasAnEvenDigit
    {
        public static bool HasEvenDigit(int n)
        {
            bool found = false;
            while (n > 0)
            {
                if (n % 10 % 2 == 0)
                {
                    found = true;
                }
                n /= 10;
            }
            return found;
        }
    }
}
