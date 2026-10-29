namespace Practice
{
    // L12 · Count down
    // Exercise page: exercises/L12-count-down.md
    public static class L12_CountDown
    {
        public static void CountDown(int n)
        {
            for (int i = n; i >= 1; i--)
            {
                Console.WriteLine(i);
            }
        }
    }
}
