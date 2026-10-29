namespace Practice
{
    // G05 · Checkerboard
    // Exercise page: exercises/G05-checkerboard.md
    public static class G05_Checkerboard
    {
        public static void DrawCheckerboard(int size)
        {
            for (int row = 1; row <= size; row++)
            {
                for (int col = 1; col <= size; col++)
                {
                    if ((row + col) % 2 == 0)
                    {
                        Console.Write("#");
                    }
                    else
                    {
                        Console.Write(".");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
