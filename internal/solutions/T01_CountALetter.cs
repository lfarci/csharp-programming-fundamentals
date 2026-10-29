namespace Practice
{
    // T01 · Count a letter
    // Exercise page: exercises/T01-count-a-letter.md
    public static class T01_CountALetter
    {
        public static int CountLetter(string text, char letter)
        {
            int count = 0;
            foreach (char c in text)
            {
                if (c == letter)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
