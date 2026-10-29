namespace Practice
{
    // L19 · Count the turns
    // Exercise page: exercises/L19-count-the-turns.md
    public static class L19_CountTheTurns
    {
        public static int CountTurns(int a, int b)
        {
            int turns = 0;
            for (int i = a; i <= b; i++)
            {
                turns++;
            }
            return turns;
        }
    }
}
