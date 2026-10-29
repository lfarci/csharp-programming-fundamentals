namespace Practice
{
    // D06 · Palindrome number
    // Exercise page: exercises/D06-palindrome-number.md
    public static class D06_PalindromeNumber
    {
        public static bool IsPalindrome(int n)
        {
            int reversed = 0;
            int remaining = n;          // copy: we need n at the end
            while (remaining > 0)
            {
                reversed = reversed * 10 + remaining % 10;
                remaining /= 10;
            }
            return reversed == n;
        }
    }
}
