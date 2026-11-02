namespace Practice
{
    // A32 · Product of odd numbers
    // Exercise page: exercises/A32-product-of-odd-numbers.md
    public static class A32_ProductOfOddNumbers
    {
        public static long ProductOfOdds(int n)
        {
            long product = 1;
            for (int i = 1; i <= n; i += 2)
            {
                product *= i;
            }
            return product;
        }
    }
}
