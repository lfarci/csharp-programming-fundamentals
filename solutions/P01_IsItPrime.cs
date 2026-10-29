namespace Practice
{
    // P01 · Is it prime?
    // Exercise page: exercises/P01-is-it-prime.md
    public static class P01_IsItPrime
    {
        public static bool IsPrime(int n)
        {
            bool isPrime = n >= 2;
            for (int d = 2; d * d <= n; d++)
            {
                if (n % d == 0)
                {
                    isPrime = false;
                    break;
                }
            }
            return isPrime;
        }
    }
}
