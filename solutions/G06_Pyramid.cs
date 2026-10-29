namespace Practice
{
    // G06 · Pyramid
    // Exercise page: exercises/G06-pyramid.md
    public static class G06_Pyramid
    {
        public static void DrawPyramid(int height)
        {
            for (int row = 1; row <= height; row++)
            {
                for (int s = 1; s <= height - row; s++)
                {
                    Console.Write(" ");
                }
                for (int star = 1; star <= 2 * row - 1; star++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
            }
        }
    }
}
