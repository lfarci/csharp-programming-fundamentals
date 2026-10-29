// Small helpers used by every test file in Exercises/.
// They run your code with a time limit, capture what it prints,
// and explain a failure in plain words. The checks themselves
// (which input, which expected result) are in Exercises/<exercise>Tests.cs.
using System.Runtime.CompilerServices;

namespace Practice.Tests
{
    public static class Expect
    {
        static readonly TimeSpan TimeLimit = TimeSpan.FromSeconds(5);

        /// <summary>Your method must return <paramref name="expected"/>.</summary>
        public static void Returns<T>(T expected, Func<T> call, string? hint = null,
            [CallerArgumentExpression(nameof(call))] string code = "")
        {
            T got = default!;
            Capture("", () => got = call());
            if (Same(expected, got)) return;
            string msg = $"{Call(code)} should return {Show(expected)}, but your method returned {Show(got)}.";
            Fail(msg, hint ?? ReturnHint(expected, got));
        }

        /// <summary>Your method must print exactly <paramref name="expected"/> (spaces at the end of a line do not count).</summary>
        public static void Prints(string expected, Action call, string? hint = null,
            [CallerArgumentExpression(nameof(call))] string code = "")
        {
            string printed = Capture("", call);
            string[] want = Lines(expected), got = Lines(printed);
            for (int i = 0; i < Math.Max(want.Length, got.Length); i++)
            {
                string w = i < want.Length ? want[i] : "(no line)";
                string g = i < got.Length ? got[i] : "(no line)";
                if (w.TrimEnd() == g.TrimEnd()) continue;
                string msg = $"{Call(code)} should print:\n{Box(expected)}\nYour method printed:\n{Box(printed)}\n" +
                             $"The first difference is on line {i + 1}: expected \"{w}\", got \"{g}\".";
                string auto = printed.Trim().Length == 0 && expected.Trim().Length > 0 ? "nothing was printed yet. Use Console.Write for one piece and Console.WriteLine() to end a line."
                    : got.Length == 1 && want.Length > 1 ? "everything is on one line. Use Console.WriteLine() at the end of each line."
                    : w.Trim() == g.Trim() ? "only the spaces at the start of the line are different."
                    : "trace the first row (or the first line) on paper.";
                Fail(msg, hint ?? auto);
            }
        }

        /// <summary>A whole program (Run): typed <paramref name="input"/> must make it print each of <paramref name="lines"/>, in this order.
        /// Your questions ("N: ") can be anything: a line only has to END with the expected text.</summary>
        public static void Output(string[] input, string[] lines, Action run, string? hint = null)
        {
            string printed = Capture(string.Join("\n", input) + "\n", run);
            string[] got = Lines(printed);
            int at = 0;
            foreach (string want in lines)
            {
                int found = Array.FindIndex(got, at, l => l.TrimEnd().EndsWith(want.TrimEnd(), StringComparison.Ordinal));
                if (found >= 0) { at = found + 1; continue; }
                string typed = input.Length == 0 ? "(no input)" : string.Join(", ", input.Select(i => i == "" ? "(empty line)" : i));
                string msg = $"With the input {typed}, I expected a line ending with:\n    {want}\nYour program printed:\n{Box(printed)}";
                string auto = got.Any(l => l.Contains(want.Trim())) ? "the text is there, but more text follows it on the same line. Use Console.WriteLine to end the line."
                    : got.Any(l => l.Contains(want.Trim(), StringComparison.OrdinalIgnoreCase)) ? "only upper/lower case letters are different."
                    : "run it yourself with ./ex run and type the same input.";
                Fail(msg, hint ?? auto);
            }
        }

        // ---------- the rest is plumbing ----------

        static string ReturnHint(object? want, object? got) => (want, got) switch
        {
            (int or long, int or long) when Convert.ToInt64(got) == 0 => "0 is the start value. Does your loop run at all? Is the result updated inside the loop?",
            (int or long, int or long) => "trace this call on paper, one row per turn of the loop. Check the first and the last turn (< or <=? start at 0 or 1?).",
            (string w, string g) when w.Trim() == g.Trim() => "only spaces at the start or end are different.",
            (string w, string g) when string.Equals(w, g, StringComparison.OrdinalIgnoreCase) => "only upper/lower case letters are different.",
            (bool, _) => "test this value by hand. Which branch of your if does it take?",
            _ => "trace this call on paper with a trace table.",
        };

        static void Fail(string message, string hint) => Assert.Fail(message + "\nHint: " + hint);

        /// <summary>Runs your code with fake keyboard input and a time limit, and returns what it printed.</summary>
        static string Capture(string input, Action action)
        {
            TextReader oldIn = Console.In;
            TextWriter oldOut = Console.Out;
            var output = new StringWriter();
            Console.SetIn(new StringReader(input));
            Console.SetOut(output);
            try
            {
                Task task = Task.Run(action);
                if (!task.Wait(TimeLimit))
                    Assert.Fail($"Your code was still running after {TimeLimit.TotalSeconds} seconds. Is there a loop that never stops? Check that its condition becomes false.");
            }
            catch (AggregateException ae) when (ae.InnerException is not null and not Xunit.Sdk.IAssertionException)
            {
                string what = ae.InnerException switch
                {
                    ArgumentNullException => "your program tried to read more input than the example gives (Console.ReadLine() returned null). Does it stop at the right moment?",
                    IndexOutOfRangeException => "an index went outside the array or the text (IndexOutOfRangeException). Check the loop condition: < Length, not <= Length.",
                    DivideByZeroException => "a division by zero.",
                    FormatException => "int.Parse got something that is not a number (FormatException).",
                    var other => $"{other.GetType().Name}: {other.Message}",
                };
                Assert.Fail($"Your code crashed: {what}\nWhat it printed before the crash:\n{Box(output.ToString())}");
            }
            finally
            {
                Console.SetIn(oldIn);
                Console.SetOut(oldOut);
            }
            return output.ToString();
        }

        static bool Same(object? a, object? b) => (a, b) switch
        {
            (double x, double y) => Math.Abs(x - y) < 1e-4,
            (int[] x, int[] y) => x.SequenceEqual(y),
            _ => Equals(a, b),
        };

        /// <summary>"() => A01_Sum1ToN.SumTo(5)" becomes "SumTo(5)".</summary>
        static string Call(string code)
        {
            string c = code.Trim();
            if (c.StartsWith("() =>")) c = c[5..].Trim();
            int dot = c.IndexOf('.');
            return dot > 0 && c[..dot].Contains('_') ? c[(dot + 1)..] : c;
        }

        static string Show(object? v) => v switch
        {
            null => "null",
            string s => "\"" + s + "\"",
            char ch => "'" + ch + "'",
            bool b => b ? "true" : "false",
            double d => d.ToString("0.####", System.Globalization.CultureInfo.InvariantCulture),
            int[] a => "[" + string.Join(", ", a) + "]",
            _ => Convert.ToString(v, System.Globalization.CultureInfo.InvariantCulture) ?? "",
        };

        static string[] Lines(string text) => text.Replace("\r", "").TrimEnd('\n').Split('\n');

        static string Box(string text)
        {
            string t = text.Replace("\r", "").TrimEnd('\n');
            return t.Length == 0 ? "    (nothing)" : string.Join("\n", t.Split('\n').Select(l => "    | " + l));
        }
    }
}
