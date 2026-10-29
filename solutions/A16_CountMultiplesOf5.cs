namespace Practice
{
    // A16 · Count multiples of 5
    // Exercise page: exercises/A16-count-multiples-of-5.md
    public static class A16_CountMultiplesOf5
    {
        public static int CountMultiplesOf5(int n)
        {
            int count = 0;
            for (int i = 1; i <= n; i++)
            {
                if (i % 5 == 0)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
