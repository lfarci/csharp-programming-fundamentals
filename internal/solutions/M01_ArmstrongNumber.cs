namespace Practice
{
    // M01 · Armstrong number
    // Exercise page: exercises/M01-armstrong-number.md
    public static class M01_ArmstrongNumber
    {
        public static bool IsArmstrong(int n)
        {
            // 1. count the digits
            int digits = 0;
            int remaining = n;
            do
            {
                digits++;
                remaining /= 10;
            }
            while (remaining > 0);

            // 2-4. add digit^digits for every digit
            int sum = 0;
            remaining = n;
            while (remaining > 0)
            {
                int digit = remaining % 10;
                int power = 1;
                for (int i = 0; i < digits; i++)
                {
                    power *= digit;
                }
                sum += power;
                remaining /= 10;
            }

            // 5. compare
            return sum == n;
        }
    }
}
