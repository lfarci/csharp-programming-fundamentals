namespace Practice
{
    // D05 · Reverse a number
    // Exercise page: exercises/D05-reverse-a-number.md
    public static class D05_ReverseANumber
    {
        public static int ReverseNumber(int n)
        {
            int reversed = 0;
            int remaining = n;
            while (remaining > 0)
            {
                int digit = remaining % 10;
                reversed = reversed * 10 + digit;
                remaining /= 10;
            }
            return reversed;
        }
    }
}
