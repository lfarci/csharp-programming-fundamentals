// Tests for D06 · Palindrome number
// Exercise page: exercises/D06-palindrome-number.md
// Your code:     practice/D06_PalindromeNumber.cs
// Run them:      ./ex check D06
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D06_PalindromeNumberTests
    {
        [Fact(DisplayName = "D06 example 1: IsPalindrome(1221) returns true")]
        public void Example1() => Expect.Returns(true, () => D06_PalindromeNumber.IsPalindrome(1221));

        [Fact(DisplayName = "D06 example 2: IsPalindrome(123) returns false")]
        public void Example2() => Expect.Returns(false, () => D06_PalindromeNumber.IsPalindrome(123));

        [Fact(DisplayName = "D06 example 3: IsPalindrome(7) returns true")]
        public void Example3() => Expect.Returns(true, () => D06_PalindromeNumber.IsPalindrome(7));

        [Fact(DisplayName = "D06 example 4: IsPalindrome(0) returns true")]
        public void Example4() => Expect.Returns(true, () => D06_PalindromeNumber.IsPalindrome(0));

        [Fact(DisplayName = "D06 example 5: IsPalindrome(10) returns false")]
        public void Example5() => Expect.Returns(false, () => D06_PalindromeNumber.IsPalindrome(10));
    }
}
