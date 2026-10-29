namespace Practice
{
    // L13 · Count by 3
    // Exercise page: exercises/L13-count-by-3.md
    public static class L13_CountBy3
    {
        public static void CountBy3(int n)
        {
            for (int i = 3; i <= n; i += 3)
            {
                Console.WriteLine(i);
            }
        }
    }
}
