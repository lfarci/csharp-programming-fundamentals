"""Demo helper: puts CODE in place of the body of the method in FILE (what Sam types in her editor)."""
import re, sys
path, code = sys.argv[1], sys.argv[2].replace("\\n", "\n")
src = open(path).read()
body = "\n".join("            " + l for l in code.split("\n"))
src = re.sub(r"(public static void PrintFromTo\(int a, int b\)\n        \{\n)(.*?)(\n        \})", lambda m: m.group(1) + body + m.group(3), src, flags=re.S)
open(path, "w").write(src)
