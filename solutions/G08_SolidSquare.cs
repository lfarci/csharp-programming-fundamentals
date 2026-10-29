namespace Practice
{
    // G08 · Solid square
    // Exercise page: exercises/G08-solid-square.md
    public static class G08_SolidSquare
    {
        public static void DrawSquare(int size)
        {
            for (int row = 1; row <= size; row++)
            {
                for (int col = 1; col <= size; col++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
            }
        }
    }
}
