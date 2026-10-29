namespace Practice
{
    // D12 · Product of the digits
    // Exercise page: exercises/D12-product-of-digits.md
    public static class D12_ProductOfDigits
    {
        public static int ProductOfDigits(int n)
        {
            int product = 1;
            while (n > 0)
            {
                product *= n % 10;
                n /= 10;
            }
            return product;
        }
    }
}
