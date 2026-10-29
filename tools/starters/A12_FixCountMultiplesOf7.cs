namespace Practice
{
    // A12 · Fix: multiples of 7
    // Exercise page: exercises/A12-fix-count-multiples-of-7.md
    //
    // Goal: CountMultiplesOf7(n) should count the numbers from 1 to n (included) divisible by 7.
    // The code is written, but it has 2 bugs. Fix them.
    //
    // YOUR JOB: the method below compiles, but it has bugs.
    // Run the check, read what fails, trace it on paper, then fix it.
    //
    // Check your code:  ./ex check A12     (Windows: .\ex check A12)
    // Try it yourself:  ./ex run A12
    public static class A12_FixCountMultiplesOf7
    {
        public static int CountMultiplesOf7(int n)
        {
            // This code has 2 bugs. Find them and fix them.
            int count = 1;
            for (int i = 1; i < n; i++)
            {
                if (i % 7 == 0)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
