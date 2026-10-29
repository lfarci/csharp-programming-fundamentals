# Contributing

Thanks for helping! This course is written for one struggling beginner, so every change follows [AGENTS.md](AGENTS.md) (audience, pedagogy rubric, formats) and [docs/writing-guide.md](docs/writing-guide.md) (plain language and accessibility).

1. Exercises are generated: edit `tools/generator/data*.py`, then run `python3 tools/generator/gen.py`. See [.agents/skills/add-exercise](.agents/skills/add-exercise/SKILL.md).
2. Run `tools/verify.sh` (needs the .NET 10 SDK, Python 3 and Node.js). CI runs the same checks on every pull request.
3. Open a pull request. It is merged when all checks are green.
