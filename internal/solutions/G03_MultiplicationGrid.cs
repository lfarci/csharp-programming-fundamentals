namespace Practice
{
    // G03 · Multiplication grid
    // Exercise page: exercises/G03-multiplication-grid.md
    public static class G03_MultiplicationGrid
    {
        public static void DrawGrid(int n)
        {
            for (int row = 1; row <= n; row++)
            {
                for (int col = 1; col <= n; col++)
                {
                    Console.Write($"{row * col,4}");
                }
                Console.WriteLine();
            }
        }
    }
}
