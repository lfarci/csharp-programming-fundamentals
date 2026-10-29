namespace Practice
{
    // L16 · Odd numbers
    // Exercise page: exercises/L16-odd-numbers.md
    public static class L16_OddNumbers
    {
        public static void PrintOdds(int n)
        {
            for (int i = 1; i <= n; i += 2)
            {
                Console.WriteLine(i);
            }
        }
    }
}
