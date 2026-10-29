namespace Practice
{
    // R04 · Find the position
    // Exercise page: exercises/R04-find-the-position.md
    public static class R04_FindThePosition
    {
        public static int IndexOf(int[] values, int target)
        {
            for (int i = 0; i < values.Length; i++)
            {
                if (values[i] == target)
                {
                    return i;
                }
            }
            return -1;
        }
    }
}
