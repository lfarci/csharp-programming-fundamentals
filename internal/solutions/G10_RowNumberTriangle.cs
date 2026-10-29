namespace Practice
{
    // G10 · Triangle of row numbers
    // Exercise page: exercises/G10-row-number-triangle.md
    public static class G10_RowNumberTriangle
    {
        public static void DrawRowTriangle(int height)
        {
            for (int row = 1; row <= height; row++)
            {
                for (int col = 1; col <= row; col++)
                {
                    Console.Write(row);
                }
                Console.WriteLine();
            }
        }
    }
}
