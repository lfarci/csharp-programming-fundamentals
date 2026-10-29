namespace Practice
{
    // L17 · Count down by 2
    // Exercise page: exercises/L17-count-down-by-2.md
    public static class L17_CountDownBy2
    {
        public static void CountDownBy2(int n)
        {
            for (int i = n; i >= 1; i -= 2)
            {
                Console.WriteLine(i);
            }
        }
    }
}
