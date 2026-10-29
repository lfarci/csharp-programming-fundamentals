namespace Practice
{
    // B02 · Rectangle calculator
    // Exercise page: exercises/B02-rectangle-calculator.md
    public static class B02_RectangleCalculator
    {
        public static int Area(int width, int height)
        {
            return width * height;
        }

        public static int Perimeter(int width, int height)
        {
            return 2 * (width + height);
        }
    }
}
