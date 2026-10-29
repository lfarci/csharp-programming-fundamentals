# Contributing

Thanks for helping! This course is written for one struggling beginner, so every change follows [AGENTS.md](../AGENTS.md) (audience, pedagogy rubric, formats) and [docs/writing-guide.md](../course/docs/writing-guide.md) (plain language and accessibility).

The repo has three folders: `practice/` (the learner's code), `course/` (every page she reads, and the website's source) and `internal/` (tests, solutions, generator, `./ex`, scripts, website config). Learner pages go in `course/`, everything else in `internal/`; the root stays as it is (`internal/tools/check-root.py`). VS Code opens `course/` and `internal/` read-only for the learner: run **File: Toggle Active Editor Read-only in Session**, or set `files.readonlyExclude` in your user settings, to edit them.

1. Exercises are generated: edit `internal/tools/generator/data*.py`, then run `python3 internal/tools/generator/gen.py`. See [.agents/skills/add-exercise](../.agents/skills/add-exercise/SKILL.md).
2. Run `internal/tools/verify.sh` (needs a .NET 8+ SDK, Python 3 and Node.js). CI runs the same checks on every pull request.
3. Open a pull request. It is merged when all checks are green.
