---
layout: home
title: Home
hero:
  name: C# Fundamentals
  text: Solve problems with loops, one small step at a time.
  image:
    src: /vscode-done.jpg
    alt: VS Code with an exercise file open and ./ex check in the terminal, showing DONE.
  tagline: A free, self-paced companion for a first C# course. Short exercises, reusable recipes, and a tool that checks your code for you.
  actions:
    - theme: brand
      text: Get started
      link: /docs/getting-started
    - theme: alt
      text: See the roadmap
      link: /ROADMAP
    - theme: alt
      text: Browse the exercises
      link: /exercises/
features:
  - title: Learn the theory
    details: "The theory comes from Microsoft Learn, free: the 6 parts of Get started with C# and the Absolute Beginners videos. Each theme says which module to do first."
    link: /learn/
    linkText: Learn
  - title: A cookbook of loop recipes
    details: 12 patterns you can recognise and reuse, such as counting, adding up, finding the biggest, and taking digits apart.
    link: /cookbook/
    linkText: Open the cookbook
  - title: Exercises by theme
    details: 96 small exercises in 15 themes, from Hello World to methods. Each one adds a single new difficulty.
    link: /exercises/
    linkText: All exercises
  - title: A checker in your terminal
    details: "./ex start opens your file, ./ex check runs the tests and tells you, in plain words, what is still wrong."
    link: /docs/getting-started#check-your-work
    linkText: How it works
  - title: Your progress
    details: Tick exercises as you finish them, see each theme fill up, and copy your results from the terminal.
    link: /progress
    linkText: My progress
  - title: Extra exercises
    details: "Want more? Do extra challenges and track them, with XP, in the C# Quest Tracker."
    link: /learn/quest-tracker
    linkText: Extra exercises
---

<!-- Website home page. The GitHub front page is README.md: keep the two separate. -->

## How it works

![How one exercise goes: read the exercise and trace an example on paper, start it with ./ex start, write the code in VS Code, run ./ex check. All OK means DONE, then ./ex next. NOT YET means read the message, open one hint, and fix the code.](diagrams/how-it-works.svg)

## What is in the course

| Part | What it is for |
| --- | --- |
| [Roadmap](ROADMAP.md) | The themes in order. Start at the top, go at your own pace. |
| [Learn](learn/README.md) | The theory on Microsoft Learn: modules and videos. |
| [Cookbook](cookbook/README.md) | The loop recipes, and which loop to use. |
| [Exercises](exercises/README.md) | Every exercise, grouped by theme, with your progress. |
| [How to read an exercise](docs/reading-an-exercise.md) | A template to organise your ideas before coding. |
| [Solving a problem](docs/problem-solving.md) | What an algorithm is, and how to find one. |
| [Glossary](docs/glossary.md) | The words of programming, in plain language. |

The website does not run C#. Your code runs on your own computer, in your copy of the course. [Getting started](docs/getting-started.md) shows how to set it up in about 15 minutes.
