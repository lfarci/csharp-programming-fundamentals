namespace Practice
{
    // G04 · Hollow rectangle
    // Exercise page: exercises/G04-hollow-rectangle.md
    public static class G04_HollowRectangle
    {
        public static void DrawHollowRectangle(int width, int height)
        {
            for (int row = 1; row <= height; row++)
            {
                for (int col = 1; col <= width; col++)
                {
                    if (row == 1 || row == height || col == 1 || col == width)
                    {
                        Console.Write("*");
                    }
                    else
                    {
                        Console.Write(" ");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
