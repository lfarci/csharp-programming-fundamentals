namespace Practice
{
    // A25 · Add the same number
    // Exercise page: exercises/A25-add-the-same-number.md
    public static class A25_AddTheSameNumber
    {
        public static int AddRepeated(int value, int times)
        {
            int total = 0;
            for (int i = 1; i <= times; i++)
            {
                total += value;
            }
            return total;
        }
    }
}
