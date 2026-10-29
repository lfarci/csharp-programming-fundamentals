namespace Practice
{
    // L09 · Draw one row
    // Exercise page: exercises/L09-draw-a-row.md
    public static class L09_DrawARow
    {
        public static void DrawRow(int width)
        {
            for (int col = 1; col <= width; col++)
            {
                Console.Write("*");
            }
            Console.WriteLine();
        }
    }
}
