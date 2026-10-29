namespace Practice
{
    // G11 · Counting triangle
    // Exercise page: exercises/G11-counting-triangle.md
    public static class G11_CountingTriangle
    {
        public static void DrawCountingTriangle(int height)
        {
            for (int row = 1; row <= height; row++)
            {
                for (int col = 1; col <= row; col++)
                {
                    Console.Write(col);
                }
                Console.WriteLine();
            }
        }
    }
}
