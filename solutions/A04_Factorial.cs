namespace Practice
{
    // A04 · Factorial
    // Exercise page: exercises/A04-factorial.md
    public static class A04_Factorial
    {
        public static long Factorial(int n)
        {
            long product = 1;
            for (int i = 1; i <= n; i++)
            {
                product *= i;
            }
            return product;
        }
    }
}
