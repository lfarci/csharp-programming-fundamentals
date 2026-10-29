namespace Practice
{
    // G01 · Draw a rectangle
    // Exercise page: exercises/G01-rectangle.md
    public static class G01_Rectangle
    {
        public static void DrawRectangle(int width, int height)
        {
            for (int row = 1; row <= height; row++)
            {
                for (int col = 1; col <= width; col++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
            }
        }
    }
}
