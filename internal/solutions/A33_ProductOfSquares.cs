namespace Practice
{
    // A33 · Product of squares
    // Exercise page: exercises/A33-product-of-squares.md
    public static class A33_ProductOfSquares
    {
        public static long ProductOfSquares(int n)
        {
            long product = 1;
            for (int i = 1; i <= n; i++)
            {
                product *= i * i;
            }
            return product;
        }
    }
}
