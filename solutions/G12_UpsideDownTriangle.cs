namespace Practice
{
    // G12 · Upside-down triangle
    // Exercise page: exercises/G12-upside-down-triangle.md
    public static class G12_UpsideDownTriangle
    {
        public static void DrawUpsideDown(int height)
        {
            for (int row = height; row >= 1; row--)
            {
                for (int col = 1; col <= row; col++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
            }
        }
    }
}
