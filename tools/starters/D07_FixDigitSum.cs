namespace Practice
{
    // D07 · Fix: digit sum
    // Exercise page: exercises/D07-fix-digit-sum.md
    //
    // Goal: DigitSum(n) should give back the sum of the digits of n (n ≥ 0). The code is
    // written, but it has 2 bugs. Fix them.
    //
    // YOUR JOB: the method below compiles, but it has bugs.
    // Run the check, read what fails, trace it on paper, then fix it.
    //
    // Check your code:  ./ex check D07     (Windows: .\ex check D07)
    // Try it yourself:  ./ex run D07
    public static class D07_FixDigitSum
    {
        public static int DigitSum(int n)
        {
            // This code has 2 bugs. Find them and fix them.
            int sum = 0;
            while (n > 10)
            {
                sum += n / 10;
                n = n % 10;
            }
            return sum;
        }
    }
}
