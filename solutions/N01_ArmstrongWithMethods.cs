namespace Practice
{
    // N01 · Armstrong with methods
    // Exercise page: exercises/N01-armstrong-with-methods.md
    public static class N01_ArmstrongWithMethods
    {
        public static int CountDigits(int n)
        {
            int digits = 0;
            do
            {
                digits++;
                n /= 10;
            }
            while (n > 0);
            return digits;
        }

        public static int Power(int baseValue, int exponent)
        {
            int result = 1;
            for (int i = 0; i < exponent; i++)
            {
                result *= baseValue;
            }
            return result;
        }

        public static bool IsArmstrong(int n)
        {
            int digits = CountDigits(n);
            int sum = 0;
            int remaining = n;
            while (remaining > 0)
            {
                sum += Power(remaining % 10, digits);
                remaining /= 10;
            }
            return sum == n;
        }
    }
}
