namespace Practice
{
    // E02 · Parse or zero
    // Exercise page: exercises/E02-parse-or-zero.md
    public static class E02_ParseOrZero
    {
        public static int ParseOrZero(string text)
        {
            if (int.TryParse(text, out int number))
            {
                return number;
            }
            return 0;
        }
    }
}
