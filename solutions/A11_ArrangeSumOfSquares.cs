namespace Practice
{
    // A11 · Arrange: sum of squares
    // Exercise page: exercises/A11-arrange-sum-of-squares.md
    public static class A11_ArrangeSumOfSquares
    {
        public static int SumOfSquares(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += i * i;
            }
            return sum;
        }
    }
}
