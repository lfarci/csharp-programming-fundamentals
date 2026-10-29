namespace Practice
{
    // G09 · Rows of numbers
    // Exercise page: exercises/G09-number-rows.md
    public static class G09_NumberRows
    {
        public static void DrawNumberRows(int width, int height)
        {
            for (int row = 1; row <= height; row++)
            {
                for (int col = 1; col <= width; col++)
                {
                    Console.Write(col);
                }
                Console.WriteLine();
            }
        }
    }
}
