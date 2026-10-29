namespace Practice
{
    // C04 · Grade from a score
    // Exercise page: exercises/C04-grade-from-a-score.md
    public static class C04_GradeFromAScore
    {
        public static string Grade(int score)
        {
            if (score >= 90)
            {
                return "A";
            }
            else if (score >= 80)
            {
                return "B";
            }
            else if (score >= 70)
            {
                return "C";
            }
            else if (score >= 50)
            {
                return "D";
            }
            else
            {
                return "F";
            }
        }
    }
}
