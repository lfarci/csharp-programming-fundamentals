namespace Practice
{
    // T03 · Count and keep the digits
    // Exercise page: exercises/T03-count-and-keep-digits.md
    public static class T03_CountAndKeepDigits
    {
        public static string KeepDigits(string text)
        {
            string kept = "";
            foreach (char c in text)
            {
                if (c >= '0' && c <= '9')
                {
                    kept += c;
                }
            }
            return kept;
        }
    }
}
