# C# Programming Fundamentals

[![Checks](https://github.com/lfarci/csharp-programming-fundamentals/actions/workflows/checks.yml/badge.svg)](https://github.com/lfarci/csharp-programming-fundamentals/actions/workflows/checks.yml)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/lfarci/csharp-programming-fundamentals?quickstart=1)

A self-paced companion for a first C# course: small exercises on loops and the basics, reusable loop recipes, and a checker (`./ex`) that tests your code.

**Read it on the website: <https://lfarci.github.io/csharp-programming-fundamentals/>** (search, progress ticks, the demo video).

![VS Code demo: ./ex start L11 creates the file in practice/, ./ex check says NOT YET with what was expected and what the code printed, a first loop misses the last number, the fix makes ./ex check say DONE, then ./ex progress and ./ex next.](docs/assets/demo.gif)

## Quick start

```bash
git clone https://github.com/lfarci/csharp-programming-fundamentals.git
cd csharp-programming-fundamentals
./ex start L03     # creates your file practice/L03_CountUpAndDown.cs
./ex check         # tests it: every example says OK or NOT YET
```

On Windows, type `.\ex` instead of `./ex`. Full setup: [Getting started](docs/getting-started.md).

## What is inside

| Folder or page | What it holds |
| --- | --- |
| [Roadmap](ROADMAP.md) | The 15 themes, in order. |
| [`exercises/`](exercises/README.md) | Every exercise page, grouped by theme. |
| [`cookbook/`](cookbook/README.md) | The 12 loop recipes and [which loop to use](cookbook/which-loop.md). |
| [`learn/`](learn/README.md) | The theory, from Microsoft Learn (the 6 parts of *Get started with C#*), and extra exercises in the [C# Quest Tracker](https://lfarci.github.io/csharp-quest-tracker/). |
| [`docs/`](docs/getting-started.md) | Getting started, how to read an exercise, problem solving, glossary. |
| `practice/` | Your own code (created by `./ex start`, ignored by Git). |
| `solutions/` | Reference solutions. Look only after a real try. |
| `tests/`, `tools/` | The tests behind `./ex check`, the generator, the website. |

## Sources

- [Microsoft Learn: C# docs](https://learn.microsoft.com/en-us/dotnet/csharp/), linked from each theme.
- [Project Euler](https://projecteuler.net/archives): a few optional extra challenges.

All exercises are original. Working on this repo (coach or AI agent)? Read [AGENTS.md](AGENTS.md).
