namespace Practice
{
    // A15 · Count the even numbers
    // Exercise page: exercises/A15-count-even-numbers.md
    public static class A15_CountEvenNumbers
    {
        public static int CountEvens(int n)
        {
            int count = 0;
            for (int i = 1; i <= n; i++)
            {
                if (i % 2 == 0)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
