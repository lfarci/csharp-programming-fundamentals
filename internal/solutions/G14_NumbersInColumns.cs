namespace Practice
{
    // G14 · Numbers in columns
    // Exercise page: exercises/G14-numbers-in-columns.md
    public static class G14_NumbersInColumns
    {
        public static void PrintInColumns(int n)
        {
            for (int i = 1; i <= n; i++)
            {
                Console.Write($"{i * 10,4}");
            }
            Console.WriteLine();
        }
    }
}
