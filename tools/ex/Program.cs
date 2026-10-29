// ./ex — the one command the learner uses. Plain words, and every result says OK or NOT YET in letters
// (so nothing depends on colour or emoji).
using System.Diagnostics;
using System.Text.Json;
using System.Xml.Linq;

Console.OutputEncoding = System.Text.Encoding.UTF8;
string root = FindRoot();
var all = JsonSerializer.Deserialize<List<Ex>>(File.ReadAllText(Path.Combine(root, "tools", "exercises.json")),
    new JsonSerializerOptions { PropertyNameCaseInsensitive = true })!;
string currentFile = Path.Combine(root, "practice", ".current");
string ex = OperatingSystem.IsWindows() ? @".\ex" : "./ex";

string command = args.Length > 0 ? args[0].ToLowerInvariant() : "help";
string? idArg = args.Length > 1 ? args[1].ToUpperInvariant() : null;

// "./ex A04" is short for "./ex check A04".
if (all.Any(e => e.Id == command.ToUpperInvariant())) { idArg = command.ToUpperInvariant(); command = "check"; }

return command switch
{
    "start" => Start(Pick(idArg, required: true)),
    "check" => Check(Pick(idArg)),
    "run" => Run(Pick(idArg)),
    "next" => Next(),
    "list" => List(),
    _ => Help(),
};

int Help()
{
    Console.WriteLine($"""
    How to use {ex}:

      {ex} start A04    create your file for exercise A04 (practice/A04_….cs) and make it the current one
      {ex} check        test the current exercise with its examples   ({ex} check A04 for another one)
      {ex} run          run the current exercise and type the input yourself
      {ex} next         start the next exercise in the list
      {ex} list         show all exercises and which ones you started

    The exercises: exercises/README.md
    """);
    return 0;
}

Ex? Pick(string? id, bool required = false)
{
    id ??= File.Exists(currentFile) ? File.ReadAllText(currentFile).Trim() : null;
    if (id == null)
    {
        Console.WriteLine(required ? $"Which exercise? For example:  {ex} start A01" : $"No current exercise yet. Start one first, for example:  {ex} start A01");
        return null;
    }
    Ex? found = all.FirstOrDefault(e => e.Id == id);
    if (found == null) Console.WriteLine($"I don't know the exercise \"{id}\". See the list with:  {ex} list");
    return found;
}

string MyFile(Ex e) => Path.Combine(root, "practice", e.Class + ".cs");
string Rel(string path) => Path.GetRelativePath(root, path).Replace('\\', '/');

int Start(Ex? e)
{
    if (e == null) return 1;
    File.WriteAllText(currentFile, e.Id);
    if (e.Kind == "paper")
    {
        Console.WriteLine($"""
        📝 {e.Id} · {e.Title} is a paper exercise: no code to write.
           Read it here:      exercises/{e.Name}.md
           Answer key after:  solutions/{e.Name}.md
           Then:              {ex} next
        """);
        return 0;
    }
    string mine = MyFile(e);
    if (File.Exists(mine))
    {
        Console.WriteLine($"""
        📂 You already started {e.Id}. Your file is kept as it is: {Rel(mine)}
           (I never overwrite your work. To start again from zero, delete that file yourself first.)
           {e.Id} is now your current exercise. Check it with:  {ex} check
        """);
        return 0;
    }
    File.Copy(Path.Combine(root, "tools", "starters", e.Class + ".cs"), mine);
    string job = e.Kind == "method" ? $"fill in the method{(e.Methods.Length > 1 ? "s" : "")} {string.Join(", ", e.Methods)}" : "write your program inside Run()";
    Console.WriteLine($"""
    ✨ Started {e.Id} · {e.Title}
       Your file:     {Rel(mine)}   ({job})
       The exercise:  exercises/{e.Name}.md
       Check it:      {ex} check
       Try it:        {ex} run
    """);
    return 0;
}

int Next()
{
    string? cur = File.Exists(currentFile) ? File.ReadAllText(currentFile).Trim() : null;
    int i = cur == null ? -1 : all.FindIndex(e => e.Id == cur);
    if (i + 1 >= all.Count) { Console.WriteLine("🏁 That was the last exercise. Well done!"); return 0; }
    return Start(all[i + 1]);
}

int List()
{
    string? cur = File.Exists(currentFile) ? File.ReadAllText(currentFile).Trim() : null;
    Console.WriteLine("Exercises (in order). ● = started, ▶ = current, 📝 = paper\n");
    foreach (Ex e in all)
    {
        string mark = e.Id == cur ? "▶" : (e.Kind != "paper" && File.Exists(MyFile(e))) ? "●" : " ";
        string started = e.Kind == "paper" ? "📝 paper" : File.Exists(MyFile(e)) ? "started" : "";
        Console.WriteLine($" {mark} {e.Id}  {e.Title,-42} {started}");
    }
    Console.WriteLine($"\nStart one with:  {ex} start A01");
    return 0;
}

int Run(Ex? e)
{
    if (e == null) return 1;
    if (e.Kind == "paper") { Console.WriteLine($"📝 {e.Id} is a paper exercise: nothing to run. Open exercises/{e.Name}.md"); return 0; }
    if (!File.Exists(MyFile(e))) { Console.WriteLine($"You have not started {e.Id} yet. Start it with:  {ex} start {e.Id}"); return 1; }
    if (!Build("practice", out _)) return 1;
    var p = Process.Start(new ProcessStartInfo("dotnet", ["run", "--project", Path.Combine(root, "practice"), "--no-build", "--", e.Id]) { WorkingDirectory = root })!;
    p.WaitForExit();
    return p.ExitCode;
}

int Check(Ex? e)
{
    if (e == null) return 1;
    if (e.Kind == "paper")
    {
        Console.WriteLine($"📝 {e.Id} is a paper exercise. Compare your answer with: solutions/{e.Name}.md");
        return 0;
    }
    if (!File.Exists(MyFile(e))) { Console.WriteLine($"You have not started {e.Id} yet. Start it with:  {ex} start {e.Id}"); return 1; }
    File.WriteAllText(currentFile, e.Id);
    Console.WriteLine($"🔎 Checking {e.Id} · {e.Title}   ({Rel(MyFile(e))})\n");

    if (!Build(Path.Combine("tests", "Practice.Tests"), out string buildLog))
    {
        PrintBuildErrors(buildLog);
        return 1;
    }
    string xml = Path.Combine(Path.GetTempPath(), $"ex-{Environment.ProcessId}.xml");
    string dll = Path.Combine(root, "tests", "Practice.Tests", "bin", "Debug", "net8.0", "Practice.Tests.dll");
    var psi = new ProcessStartInfo("dotnet", [dll, "-class", "Practice.Tests." + e.Class, "-xml", xml, "-noLogo", "-noColor"])
    { WorkingDirectory = Path.GetTempPath(), RedirectStandardOutput = true, RedirectStandardError = true };
    psi.Environment.Remove("EXERCISE_ASSEMBLY");
    var p = Process.Start(psi)!;
    p.StandardOutput.ReadToEnd(); p.StandardError.ReadToEnd();
    if (!p.WaitForExit(60_000)) { p.Kill(true); Console.WriteLine("❌ NOT YET: the tests took more than 60 seconds. Is there a loop that never stops?"); return 1; }

    var results = XDocument.Load(xml).Descendants("test")
        .Select(t => (Name: (string)t.Attribute("name")!, Result: (string)t.Attribute("result")!, Message: t.Descendants("message").FirstOrDefault()?.Value ?? ""))
        .OrderBy(t => t.Name.Contains(".Method(") ? 0 : 1).ThenBy(t => Number(t.Name)).ToList();
    File.Delete(xml);

    int ok = 0, n = 0;
    foreach (var r in results)
    {
        n++;
        int k = Number(r.Name);
        bool pass = r.Result == "Pass";
        string what = r.Name.Contains(".Method(") ? Describe(e.Cases[k - 1], pass) : $"input {Inputs(e.Examples[k - 1].Input)}";
        if (r.Result == "Pass")
        {
            ok++;
            Console.WriteLine($"✅ OK       example {n} of {results.Count}: {what}");
        }
        else
        {
            Console.WriteLine($"❌ NOT YET  example {n} of {results.Count}: {what}");
            foreach (string line in r.Message.Replace("\r", "").Replace("\\\"", "\"").Split('\n')) Console.WriteLine("           " + line);
        }
    }
    Console.WriteLine();
    if (n > 0 && ok == n)
    {
        Console.WriteLine($"""
        🎉 All {n} examples are OK. Well done!
           1. Test the edge cases from the exercise page yourself ({ex} run).
           2. Tick {e.Id} in docs/progress-checklist.md.
           3. Next exercise:  {ex} next
        """);
        return 0;
    }
    Console.WriteLine($"{ok} of {n} examples OK. Fix the first ❌ NOT YET, then run {ex} check again.");
    Console.WriteLine("Stuck? Trace the failing example on paper, then open one hint on the exercise page.");
    return 1;
}

bool Build(string project, out string log)
{
    if (!Directory.Exists(Path.Combine(root, project, "obj")))
        Console.WriteLine("⏳ Building (the first time takes up to a minute)…\n");
    var psi = new ProcessStartInfo("dotnet", ["build", Path.Combine(root, project), "-nologo", "-v", "q", "-clp:NoSummary"])
    { WorkingDirectory = root, RedirectStandardOutput = true, RedirectStandardError = true };
    var p = Process.Start(psi)!;
    log = p.StandardOutput.ReadToEnd() + p.StandardError.ReadToEnd();
    p.WaitForExit();
    if (p.ExitCode != 0 && project == "practice") PrintBuildErrors(log);
    return p.ExitCode == 0;
}

void PrintBuildErrors(string log)
{
    var errors = log.Split('\n').Where(l => l.Contains(": error ")).Select(l => l.Trim()).Distinct().ToList();
    Console.WriteLine("❌ NOT YET: your code does not compile, so it cannot be tested.");
    Console.WriteLine("   All your exercise files are built together, so an error in any of them stops the check.\n");
    foreach (string line in errors.Take(10))
    {
        // "/path/practice/A04_Factorial.cs(12,5): error CS1002: ; expected [project]"
        var m = System.Text.RegularExpressions.Regex.Match(line, @"^(.*?)\((\d+),(\d+)\): error (\w+): (.*?)( \[.*\])?$");
        if (m.Success)
            Console.WriteLine($"   {Rel(m.Groups[1].Value)}, line {m.Groups[2].Value}: {m.Groups[5].Value}  ({m.Groups[4].Value})");
        else
            Console.WriteLine("   " + line);
    }
    if (errors.Count == 0) Console.WriteLine(log);
    Console.WriteLine("\nTip: fix the first error first; often the others disappear with it. A missing ; or } is the most common one.");
}

static int Number(string testName)
{
    var m = System.Text.RegularExpressions.Regex.Match(testName, @"test: (\d+)\)");
    return m.Success ? int.Parse(m.Groups[1].Value) : 0;
}

static string Inputs(string[] input) => input.Length == 0 ? "(none)" : string.Join(", ", input.Select(i => i == "" ? "(empty line)" : i));

static string Describe(Case c, bool withResult)
{
    string args = string.Join(", ", c.Args.Select(Show));
    if (!withResult) return $"{c.Method}({args})";
    return c.Expected.ValueKind == JsonValueKind.String && c.Expected.GetString()!.Contains('\n')
        ? $"{c.Method}({args}) draws the picture"
        : $"{c.Method}({args}) → {Show(c.Expected)}";
}

static string Show(JsonElement v) => v.ValueKind switch
{
    JsonValueKind.String => v.GetString()!.Length == 1 ? $"'{v.GetString()}'" : $"\"{v.GetString()}\"",
    JsonValueKind.Array => "{ " + string.Join(", ", v.EnumerateArray().Select(x => x.ToString())) + " }",
    JsonValueKind.True => "true",
    JsonValueKind.False => "false",
    _ => v.ToString(),
};

static string FindRoot()
{
    DirectoryInfo? dir = null;
    foreach (string start in new[] { Directory.GetCurrentDirectory(), AppContext.BaseDirectory })
    {
        dir = new DirectoryInfo(start);
        while (dir != null && !File.Exists(Path.Combine(dir.FullName, "tools", "exercises.json"))) dir = dir.Parent;
        if (dir != null) break;
    }
    if (dir == null) { Console.WriteLine("Run ./ex from inside the course folder."); Environment.Exit(1); }
    return dir!.FullName;
}

record Case(string Method, JsonElement[] Args, JsonElement Expected);
record Example(string[] Input, string[] Expected);
record Ex(string Id, string Name, string Class, string Title, string Kind, string[] Methods, Case[] Cases, Example[] Examples);
