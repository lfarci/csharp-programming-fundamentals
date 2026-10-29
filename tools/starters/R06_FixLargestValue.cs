namespace Practice
{
    // R06 · Fix the bugs: largest value
    // Exercise page: exercises/R06-fix-largest-value.md
    //
    // Goal: Largest(values) should give back the largest value of the array (at least 1 value).
    // The code is written, but it has 2 bugs. Fix them.
    //
    // YOUR JOB: the method below compiles, but it has bugs.
    // Run the check, read what fails, trace it on paper, then fix it.
    //
    // Check your code:  ./ex check R06     (Windows: .\ex check R06)
    // Try it yourself:  ./ex run R06
    public static class R06_FixLargestValue
    {
        public static int Largest(int[] values)
        {
            // This code has 2 bugs. Find them and fix them.
            int max = 0;
            for (int i = 0; i <= values.Length; i++)
            {
                if (values[i] > max)
                {
                    max = values[i];
                }
            }
            return max;
        }
    }
}
