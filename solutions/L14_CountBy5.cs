namespace Practice
{
    // L14 · Count by 5
    // Exercise page: exercises/L14-count-by-5.md
    public static class L14_CountBy5
    {
        public static void CountBy5(int n)
        {
            for (int i = 5; i <= n; i += 5)
            {
                Console.WriteLine(i);
            }
        }
    }
}
