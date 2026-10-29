namespace Practice
{
    // G07 · Arrange: a square
    // Exercise page: exercises/G07-arrange-a-square.md
    public static class G07_ArrangeASquare
    {
        public static void DrawSquare(int size)
        {
            for (int row = 1; row <= size; row++)
            {
                for (int col = 1; col <= size; col++)
                {
                    Console.Write("#");
                }
                Console.WriteLine();
            }
        }
    }
}
