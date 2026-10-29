namespace Practice
{
    // A12 · Fix the bugs: count multiples of 7
    // Exercise page: exercises/A12-fix-count-multiples-of-7.md
    public static class A12_FixCountMultiplesOf7
    {
        public static int CountMultiplesOf7(int n)
        {
            int count = 0;
            for (int i = 1; i <= n; i++)
            {
                if (i % 7 == 0)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
