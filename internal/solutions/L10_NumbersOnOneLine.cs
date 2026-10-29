namespace Practice
{
    // L10 · Numbers on one line
    // Exercise page: exercises/L10-numbers-on-one-line.md
    public static class L10_NumbersOnOneLine
    {
        public static void PrintNumbers(int n)
        {
            for (int i = 1; i <= n; i++)
            {
                if (i > 1)
                {
                    Console.Write(" ");
                }
                Console.Write(i);
            }
            Console.WriteLine();
        }
    }
}
