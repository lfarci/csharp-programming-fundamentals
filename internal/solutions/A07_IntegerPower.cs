namespace Practice
{
    // A07 · Integer power
    // Exercise page: exercises/A07-integer-power.md
    public static class A07_IntegerPower
    {
        public static long Power(int baseValue, int exponent)
        {
            long result = 1;
            for (int i = 0; i < exponent; i++)
            {
                result *= baseValue;
            }
            return result;
        }
    }
}
