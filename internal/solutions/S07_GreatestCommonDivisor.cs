namespace Practice
{
    // S07 · Greatest common divisor
    // Exercise page: exercises/S07-greatest-common-divisor.md
    public static class S07_GreatestCommonDivisor
    {
        public static int Gcd(int a, int b)
        {
            while (b != 0)
            {
                int rest = a % b;
                a = b;
                b = rest;
            }
            return a;
        }
    }
}
