namespace Practice
{
    // G13 · Diagonal
    // Exercise page: exercises/G13-diagonal.md
    public static class G13_Diagonal
    {
        public static void DrawDiagonal(int size)
        {
            for (int row = 1; row <= size; row++)
            {
                for (int col = 1; col <= size; col++)
                {
                    if (row == col)
                    {
                        Console.Write("*");
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
