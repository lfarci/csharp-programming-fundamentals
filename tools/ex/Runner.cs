// Plumbing shared by practice/Program.cs: runs one exercise by hand.
// Method exercises: asks a value for each parameter, calls the method, prints the result.
// Program exercises: calls Run().
using System.Reflection;

namespace Practice
{
    internal static class Runner
    {
        public static void Main(Assembly assembly, string[] args)
        {
            string? id = args.Length > 0 ? args[0] : CurrentExercise();
            if (id == null)
            {
                Console.WriteLine("No exercise selected yet. Start one with:  ./ex start A01");
                return;
            }
            Type? type = FindExercise(assembly, id);
            if (type == null)
            {
                Console.WriteLine($"Exercise {id.ToUpperInvariant()} is not started yet. Start it with:  ./ex start {id.ToUpperInvariant()}");
                return;
            }
            Console.WriteLine($"▶ Running {type.Name}  (type the input, press Enter after each value)");
            Console.WriteLine();
            MethodInfo? run = type.GetMethod("Run", BindingFlags.Public | BindingFlags.Static, Type.EmptyTypes);
            if (run != null)
            {
                run.Invoke(null, null);
                return;
            }
            foreach (MethodInfo method in type.GetMethods(BindingFlags.Public | BindingFlags.Static | BindingFlags.DeclaredOnly))
            {
                var values = new List<object?>();
                foreach (ParameterInfo p in method.GetParameters())
                {
                    values.Add(Ask(p));
                }
                string call = $"{method.Name}({string.Join(", ", values.Select(Show))})";
                object? result = method.Invoke(null, values.ToArray());
                if (method.ReturnType == typeof(void))
                {
                    Console.WriteLine($"(that was printed by {call})");
                }
                else
                {
                    Console.WriteLine($"{call} returned {Show(result)}");
                }
                Console.WriteLine();
            }
        }

        public static Type? FindExercise(Assembly assembly, string id)
        {
            string prefix = id.ToUpperInvariant() + "_";
            return assembly.GetTypes().FirstOrDefault(t => t.IsClass && t.Namespace == "Practice" && t.Name.StartsWith(prefix, StringComparison.Ordinal));
        }

        public static string? CurrentExercise()
        {
            string? root = RepoRoot();
            string file = root == null ? "" : Path.Combine(root, "practice", ".current");
            return File.Exists(file) ? File.ReadAllText(file).Trim() : null;
        }

        public static string? RepoRoot()
        {
            foreach (string start in new[] { Directory.GetCurrentDirectory(), AppContext.BaseDirectory })
            {
                var dir = new DirectoryInfo(start);
                while (dir != null)
                {
                    if (File.Exists(Path.Combine(dir.FullName, "practice", "Practice.csproj"))) return dir.FullName;
                    dir = dir.Parent;
                }
            }
            return null;
        }

        static object? Ask(ParameterInfo p)
        {
            while (true)
            {
                string kind = p.ParameterType == typeof(int[]) ? "numbers separated by spaces" : FriendlyType(p.ParameterType);
                Console.Write($"{p.Name} ({kind}): ");
                string text = Console.ReadLine() ?? "";
                try
                {
                    return Parse(text, p.ParameterType);
                }
                catch (FormatException)
                {
                    Console.WriteLine($"  That is not {FriendlyType(p.ParameterType)}. Try again.");
                }
            }
        }

        static object Parse(string text, Type type)
        {
            if (type == typeof(string)) return text;
            if (type == typeof(char)) return text.Length > 0 ? text[0] : throw new FormatException();
            if (type == typeof(int)) return int.Parse(text);
            if (type == typeof(long)) return long.Parse(text);
            if (type == typeof(double)) return double.Parse(text.Replace(',', '.'), System.Globalization.CultureInfo.InvariantCulture);
            if (type == typeof(bool)) return bool.Parse(text);
            if (type == typeof(int[])) return text.Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToArray();
            throw new FormatException();
        }

        static string FriendlyType(Type t) =>
            t == typeof(int) ? "a whole number" : t == typeof(long) ? "a whole number" : t == typeof(double) ? "a decimal number" :
            t == typeof(string) ? "a text" : t == typeof(char) ? "one character" : t == typeof(bool) ? "true or false" : t.Name;

        public static string Show(object? v) => v switch
        {
            null => "null",
            string s => $"\"{s}\"",
            char c => $"'{c}'",
            bool b => b ? "true" : "false",
            double d => d.ToString("0.####", System.Globalization.CultureInfo.InvariantCulture),
            int[] a => "{ " + string.Join(", ", a) + " }",
            _ => Convert.ToString(v, System.Globalization.CultureInfo.InvariantCulture) ?? "",
        };
    }
}
