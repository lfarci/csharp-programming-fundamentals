namespace Practice
{
    // D03 · Count the digits
    // Exercise page: exercises/D03-count-digits.md
    public static class D03_CountDigits
    {
        public static int CountDigits(int n)
        {
            int digits = 0;
            int remaining = n;
            do
            {
                digits++;
                remaining /= 10;
            }
            while (remaining > 0);
            return digits;
        }
    }
}
