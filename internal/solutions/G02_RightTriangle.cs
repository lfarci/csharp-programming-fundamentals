namespace Practice
{
    // G02 · Draw a right triangle
    // Exercise page: exercises/G02-right-triangle.md
    public static class G02_RightTriangle
    {
        public static void DrawTriangle(int height)
        {
            for (int row = 1; row <= height; row++)
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
