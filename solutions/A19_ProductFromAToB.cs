namespace Practice
{
    // A19 · Product from a to b
    // Exercise page: exercises/A19-product-from-a-to-b.md
    public static class A19_ProductFromAToB
    {
        public static long ProductFromTo(int a, int b)
        {
            long product = 1;
            for (int i = a; i <= b; i++)
            {
                product *= i;
            }
            return product;
        }
    }
}
