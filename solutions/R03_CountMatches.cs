namespace Practice
{
    // R03 · Count matches in an array
    // Exercise page: exercises/R03-count-matches.md
    public static class R03_CountMatches
    {
        public static int CountMatches(int[] values, int target)
        {
            int matches = 0;
            foreach (int value in values)
            {
                if (value == target)
                {
                    matches++;
                }
            }
            return matches;
        }
    }
}
