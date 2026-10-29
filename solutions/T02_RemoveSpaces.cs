namespace Practice
{
    // T02 · Remove spaces
    // Exercise page: exercises/T02-remove-spaces.md
    public static class T02_RemoveSpaces
    {
        public static string RemoveSpaces(string text)
        {
            string result = "";
            foreach (char c in text)
            {
                if (c != ' ')
                {
                    result += c;
                }
            }
            return result;
        }
    }
}
