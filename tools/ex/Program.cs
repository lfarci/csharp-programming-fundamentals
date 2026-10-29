// ./ex: the one command the learner uses. Plain words: every result says OK, NOT YET or DONE.
//
//   start A04   copy the starter to practice/A04_Factorial.cs (never overwrites)
//   check       build + run the tests of one exercise (tests/Practice.Tests/Exercises/A04_FactorialTests.cs)
//   run         run the exercise and type the input yourself
//   next        start the next exercise that is not done yet
//   list        all exercises, in order
//   progress    re-run the tests of every started exercise, show what is done, print the website sync code
//   done L01    mark a paper exercise as done (paper exercises have no tests)
//
// Progress is saved in practice/.done (one line per exercise: ID and date) and shown in practice/PROGRESS.md.
using System.Diagnostics;
using System.Text.Json;
using System.Text.RegularExpressions;
using System.Xml.Linq;

Console.OutputEncoding = System.Text.Encoding.UTF8;
string root = FindRoot();
var all = JsonSerializer.Deserialize<List<Ex>>(File.ReadAllText(Path.Combine(root, "tools", "exercises.json")),
    new JsonSerializerOptions { PropertyNameCaseInsensitive = true })!;
string practice = Path.Combine(root, "practice");
string currentFile = Path.Combine(practice, ".current");
string doneFile = Path.Combine(practice, ".done");
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
    "progress" => Progress(),
    "done" => MarkPaperDone(Pick(idArg, required: true)),
    _ => Help(),
};

int Help()
{
    Console.WriteLine($"""
    How to use {ex}:

      {ex} start A04    create your file for exercise A04 (practice/A04_....cs) and make it the current one
      {ex} check        test the current exercise ({ex} check A04 for another one)
      {ex} run          run the current exercise and type the input yourself
      {ex} next         start the next exercise that is not done yet
      {ex} list         show all exercises
      {ex} progress     see what is done, per roadmap step and per drill set
      {ex} done L01     mark a paper exercise as done

    The exercises: exercises/README.md
    """);
    return 0;
}

Ex? Pick(string? id, bool required = false)
{
    id ??= Current();
    if (id == null)
    {
        Console.WriteLine(required ? $"Which exercise? For example:  {ex} start A01" : $"No current exercise yet. Start one first, for example:  {ex} start A01");
        return null;
    }
    Ex? found = all.FirstOrDefault(e => e.Id == id);
    if (found == null) Console.WriteLine($"I don't know the exercise \"{id}\". See the list with:  {ex} list");
    return found;
}

string? Current() => File.Exists(currentFile) ? File.ReadAllText(currentFile).Trim() : null;
string MyFile(Ex e) => Path.Combine(practice, e.Class + ".cs");
bool Started(Ex e) => e.Kind != "paper" && File.Exists(MyFile(e));
string Rel(string path) => Path.GetRelativePath(root, path).Replace('\\', '/');
string TestFile(Ex e) => $"tests/Practice.Tests/Exercises/{e.Class}Tests.cs";

int Start(Ex? e)
{
    if (e == null) return 1;
    File.WriteAllText(currentFile, e.Id);
    if (e.Kind == "paper")
    {
        Console.WriteLine($"""
        {e.Id} · {e.Title} is a paper exercise: no code to write.
           Read it here:      exercises/{e.Name}.md
           Answer key after:  solutions/{e.Name}.md
           When it is done:   {ex} done {e.Id}
        """);
        return 0;
    }
    string mine = MyFile(e);
    if (File.Exists(mine))
    {
        Console.WriteLine($"""
        You already started {e.Id}. Your file is kept as it is: {Rel(mine)}
           (I never overwrite your work. To start again from zero, delete that file yourself first.)
           {e.Id} is now your current exercise. Check it with:  {ex} check
        """);
        return 0;
    }
    File.Copy(Path.Combine(root, "tools", "starters", e.Class + ".cs"), mine);
    string job = e.Kind == "method" ? $"fill in the method{(e.Methods.Length > 1 ? "s" : "")} {string.Join(", ", e.Methods)}" : "write your program inside Run()";
    Console.WriteLine($"""
    Started {e.Id} · {e.Title}
       Your file:     {Rel(mine)}   ({job})
       The exercise:  exercises/{e.Name}.md
       The tests:     {TestFile(e)}
       Check it:      {ex} check
       Try it:        {ex} run
    """);
    return 0;
}

int Next()
{
    var done = LoadDone();
    int i = Math.Max(-1, all.FindIndex(e => e.Id == Current()));
    Ex? next = all.Skip(i + 1).FirstOrDefault(e => !done.ContainsKey(e.Id));
    if (next == null) { Console.WriteLine("That was the last exercise. Well done!"); return 0; }
    return Start(next);
}

int List()
{
    var done = LoadDone();
    string? cur = Current();
    Console.WriteLine("Exercises, in order.  > = current\n");
    foreach (Ex e in all)
    {
        string state = done.ContainsKey(e.Id) ? "done" : Started(e) ? "started" : e.Kind == "paper" ? "paper" : "";
        Console.WriteLine($" {(e.Id == cur ? ">" : " ")} {e.Id}  {e.Title,-42} {state}");
    }
    Console.WriteLine($"\nStart one with:  {ex} start A01     See your progress:  {ex} progress");
    return 0;
}

int Run(Ex? e)
{
    if (e == null) return 1;
    if (e.Kind == "paper") { Console.WriteLine($"{e.Id} is a paper exercise: nothing to run. Open exercises/{e.Name}.md"); return 0; }
    if (!Started(e)) { Console.WriteLine($"You have not started {e.Id} yet. Start it with:  {ex} start {e.Id}"); return 1; }
    if (!Build("practice", out string log, e.Class)) { PrintBuildErrors(log, one: true); return 1; }
    var p = Process.Start(new ProcessStartInfo("dotnet", ["run", "--project", practice, "--no-build", "--", e.Id]) { WorkingDirectory = root })!;
    p.WaitForExit();
    return p.ExitCode;
}

int Check(Ex? e)
{
    if (e == null) return 1;
    if (e.Kind == "paper")
    {
        Console.WriteLine($"{e.Id} is a paper exercise. Compare your answer with solutions/{e.Name}.md, then mark it:  {ex} done {e.Id}");
        return 0;
    }
    if (!Started(e)) { Console.WriteLine($"You have not started {e.Id} yet. Start it with:  {ex} start {e.Id}"); return 1; }
    File.WriteAllText(currentFile, e.Id);
    Console.WriteLine($"Checking {e.Id} · {e.Title}");
    Console.WriteLine($"   your code: {Rel(MyFile(e))}    the tests: {TestFile(e)}\n");

    var results = RunTests(e.Class, out string buildLog);
    if (results == null) { PrintBuildErrors(buildLog, one: true); return 1; }

    int ok = 0;
    foreach (var r in results)
    {
        string name = Regex.Replace(r.Name, @"^\w+ example (\d+): ", "");
        if (r.Pass) { ok++; Console.WriteLine($"OK       example {r.Number} of {results.Count}: {name}"); continue; }
        Console.WriteLine($"NOT YET  example {r.Number} of {results.Count}: {name}");
        foreach (string line in r.Message.Replace("\r", "").Split('\n')) Console.WriteLine("         " + line);
    }
    Console.WriteLine();
    if (results.Count > 0 && ok == results.Count)
    {
        SaveDone(e.Id, true);
        var done = LoadDone();
        Console.WriteLine($"""
        DONE: all {ok} examples are OK. {e.Id} is validated.
           Progress: {done.Count} of {all.Count} exercises done.  ({ex} progress for details)
           1. Test the edge cases from the exercise page yourself ({ex} run).
           2. Next exercise:  {ex} next
        """);
        return 0;
    }
    SaveDone(e.Id, false);
    Console.WriteLine($"{ok} of {results.Count} examples OK. Fix the first NOT YET, then run {ex} check again.");
    Console.WriteLine("Stuck? Trace the failing example on paper, then open one hint on the exercise page.");
    return 1;
}

int MarkPaperDone(Ex? e)
{
    if (e == null) return 1;
    if (e.Kind != "paper") { Console.WriteLine($"{e.Id} has tests: it is marked done when {ex} check {e.Id} says DONE."); return 1; }
    SaveDone(e.Id, true);
    Console.WriteLine($"DONE: {e.Id} · {e.Title} is marked as done. Next exercise:  {ex} next");
    return 0;
}

int Progress()
{
    // The tests decide: re-run them for every started exercise, then show the saved state.
    if (all.Any(Started))
    {
        Console.WriteLine("Re-running the tests of your started exercises...\n");
        var results = RunTests(null, out _);
        if (results == null)
            Console.WriteLine($"(One of your files does not compile, so I show the results saved by {ex} check.)\n");
        else
            foreach (var g in results.GroupBy(r => r.Class))
            {
                Ex? e = all.FirstOrDefault(x => x.Class + "Tests" == g.Key);
                if (e != null) SaveDone(e.Id, g.All(r => r.Pass));
            }
    }
    var done = LoadDone();
    var lines = new List<string>();
    int started = all.Count(e => Started(e) && !done.ContainsKey(e.Id));
    lines.Add($"Progress: {done.Count} of {all.Count} exercises done, {started} started (not done yet).");
    lines.Add("");
    lines.Add("By roadmap step:");
    foreach (var g in all.GroupBy(e => e.Step))
    {
        int d = g.Count(e => done.ContainsKey(e.Id)), s = g.Count(e => Started(e) && !done.ContainsKey(e.Id));
        lines.Add($"  {g.Key,-28} {d,3} of {g.Count(),-3} done{(s > 0 ? $", {s} started" : "")}");
    }
    lines.Add("");
    lines.Add("Drill sets (x = done, o = started, . = not started):");
    foreach (string set in all.SelectMany(e => e.Drills).Distinct())
    {
        var ids = all.Where(e => e.Drills.Contains(set)).ToList();
        lines.Add($"  {set} ({ids.Count(e => done.ContainsKey(e.Id))} of {ids.Count})");
        lines.Add("    " + string.Join("  ", ids.Select(e => (done.ContainsKey(e.Id) ? "x " : Started(e) ? "o " : ". ") + e.Id)));
    }
    Ex? next = all.Skip(Math.Max(0, all.FindIndex(e => e.Id == Current()))).FirstOrDefault(e => !done.ContainsKey(e.Id));
    lines.Add("");
    if (next != null) lines.Add($"Next suggestion: {next.Id} · {next.Title}   ({ex} next)");
    foreach (string l in lines) Console.WriteLine(l);

    var md = new List<string> { "# My progress", "", $"Written by `{ex} progress` on {DateTime.Now:yyyy-MM-dd}.", "", "| Exercise | Title | State | Date |", "| --- | --- | --- | --- |" };
    foreach (Ex e in all.Where(e => done.ContainsKey(e.Id) || Started(e)))
        md.Add($"| {e.Id} | {e.Title} | {(done.ContainsKey(e.Id) ? "done" : "started")} | {(done.TryGetValue(e.Id, out string? date) ? date : "")} |");
    md.Add("");
    md.Add(lines[0]);
    File.WriteAllText(Path.Combine(practice, "PROGRESS.md"), string.Join("\n", md) + "\n");
    Console.WriteLine("\nSaved in practice/PROGRESS.md.");
    Console.WriteLine("\nSync code for the website (My progress > Sync with the terminal):");
    Console.WriteLine("  " + SyncCode(done.Keys));
    return 0;
}

// "CPF1:A1-4,7;B1-3" = A01..A04, A07, B01..B03. The website (.vitepress/theme/progress.ts) reads the same format.
static string SyncCode(IEnumerable<string> ids)
{
    var parts = ids.Where(id => id.Length == 3).OrderBy(id => id, StringComparer.Ordinal).GroupBy(id => id[0]).Select(g =>
    {
        var ns = g.Select(id => int.Parse(id[1..])).ToList();
        var runs = new List<string>();
        for (int i = 0; i < ns.Count; i++)
        {
            int j = i;
            while (j + 1 < ns.Count && ns[j + 1] == ns[j] + 1) j++;
            runs.Add(j > i ? $"{ns[i]}-{ns[j]}" : $"{ns[i]}");
            i = j;
        }
        return g.Key + string.Join(",", runs);
    });
    return "CPF1:" + string.Join(";", parts);
}

Dictionary<string, string> LoadDone() =>
    File.Exists(doneFile)
        ? File.ReadAllLines(doneFile).Select(l => l.Split(' ', 2)).Where(p => p[0].Length > 0)
              .GroupBy(p => p[0]).ToDictionary(g => g.Key, g => g.Last().Length > 1 ? g.Last()[1] : "")
        : new();

void SaveDone(string id, bool isDone)
{
    var done = LoadDone();
    if (isDone) { if (!done.ContainsKey(id)) done[id] = DateTime.Now.ToString("yyyy-MM-dd"); }
    else done.Remove(id);
    File.WriteAllLines(doneFile, all.Where(e => done.ContainsKey(e.Id)).Select(e => $"{e.Id} {done[e.Id]}"));
}

/// <summary>Builds the tests (only for <paramref name="only"/> if given) and runs them. Null when the build fails.</summary>
List<Result>? RunTests(string? only, out string buildLog)
{
    if (!Build(Path.Combine("tests", "Practice.Tests"), out buildLog, only)) return null;
    string xml = Path.Combine(Path.GetTempPath(), $"ex-{Environment.ProcessId}.xml");
    string dll = Path.Combine(root, "tests", "Practice.Tests", "bin", "Debug", "net8.0", "Practice.Tests.dll");
    List<string> a = [dll, "-xml", xml, "-noLogo", "-noColor"];
    if (only != null) a.AddRange(["-class", $"Practice.Tests.{only}Tests"]);
    var psi = new ProcessStartInfo("dotnet", a) { WorkingDirectory = Path.GetTempPath(), RedirectStandardOutput = true, RedirectStandardError = true };
    var p = Process.Start(psi)!;
    p.StandardOutput.ReadToEnd(); p.StandardError.ReadToEnd();
    if (!p.WaitForExit(120_000)) { p.Kill(true); Console.WriteLine("NOT YET: the tests took more than 2 minutes. Is there a loop that never stops?"); return []; }
    if (!File.Exists(xml)) return [];
    var results = XDocument.Load(xml).Descendants("test").Select(t =>
    {
        string name = Unescape((string)t.Attribute("name")!);
        var m = Regex.Match(name, @" example (\d+):");
        string type = ((string)t.Attribute("type")!).Replace("Practice.Tests.", "");
        return new Result(type, name, m.Success ? int.Parse(m.Groups[1].Value) : 0, (string)t.Attribute("result")! == "Pass",
            Unescape(t.Descendants("message").FirstOrDefault()?.Value ?? ""));
    }).OrderBy(r => r.Class).ThenBy(r => r.Number).ToList();
    File.Delete(xml);
    return results;
}

bool Build(string project, out string log, string? only = null)
{
    if (!Directory.Exists(Path.Combine(root, project, "obj")))
        Console.WriteLine("Building (the first time takes up to a minute)...\n");
    List<string> a = ["build", Path.Combine(root, project), "-nologo", "-v", "q", "-clp:NoSummary"];
    // Build only this exercise's file (and its tests): other unfinished files cannot block it.
    if (only != null) a.Add("-p:OnlyExercise=" + only);
    var psi = new ProcessStartInfo("dotnet", a) { WorkingDirectory = root, RedirectStandardOutput = true, RedirectStandardError = true };
    var p = Process.Start(psi)!;
    log = p.StandardOutput.ReadToEnd() + p.StandardError.ReadToEnd();
    p.WaitForExit();
    return p.ExitCode == 0;
}

void PrintBuildErrors(string log, bool one)
{
    var errors = log.Split('\n').Where(l => l.Contains(": error ")).Select(l => l.Trim()).Distinct().ToList();
    Console.WriteLine("NOT YET: your code does not compile, so it cannot be tested.");
    if (one) Console.WriteLine("   Only this exercise's file is built, so the error is in this file.\n");
    foreach (string line in errors.Take(10))
    {
        // "/path/practice/A04_Factorial.cs(12,5): error CS1002: ; expected [project]"
        var m = Regex.Match(line, @"^(.*?)\((\d+),(\d+)\): error (\w+): (.*?)( \[.*\])?$");
        Console.WriteLine(m.Success ? $"   {Rel(m.Groups[1].Value)}, line {m.Groups[2].Value}: {m.Groups[5].Value}  ({m.Groups[4].Value})" : "   " + line);
    }
    if (errors.Count == 0) Console.WriteLine(log);
    if (errors.Any(l => l.Contains("Exercises" + Path.DirectorySeparatorChar) || l.Contains("Exercises/")))
        Console.WriteLine("\nThe error is in a test file: did you rename the method or change its first line? Keep it as it was in the starter.");
    Console.WriteLine("\nTip: fix the first error first; often the others disappear with it. A missing ; or } is the most common one.");
}

static string Unescape(string s) => s.Replace("\\\"", "\"");

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

record Result(string Class, string Name, int Number, bool Pass, string Message);
record Ex(string Id, string Name, string Class, string Title, string Kind, string Step, string[] Methods, string[] Drills);
