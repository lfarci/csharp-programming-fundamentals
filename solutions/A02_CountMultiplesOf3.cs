namespace Practice
{
    // A02 · Count multiples of 3
    // Exercise page: exercises/A02-count-multiples-of-3.md
    public static class A02_CountMultiplesOf3
    {
        public static int CountMultiplesOf3(int n)
        {
            int count = 0;
            for (int i = 1; i <= n; i++)
            {
                if (i % 3 == 0)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
