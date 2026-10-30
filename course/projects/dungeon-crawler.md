[Home](../../README.md) › [Projects](README.md) › Tiny dungeon

# Tiny dungeon

<p class="project-meta">Just for fun · Level: Hard · Effort: 5 to 8 hours</p>

**Explore rooms, fight slimes, find the treasure: a text adventure on a map.**

You wake up in a damp cellar with a torch and 10 hit points. Somewhere there is a treasure, and somewhere there are slimes. A text adventure is a game loop, a map in an array and a lot of `if`: and you decide how funny the descriptions are.

## A sample run

```text
You are in the CELLAR. It smells like old cheese.
Exits: north, east.   HP 10   Gold 0
> north
You are in the HALL. A slime blocks the way! (HP 4)
> attack
You hit the slime for 3. The slime hits you for 1.
> attack
You hit the slime for 2. The slime melts into a puddle.
> look
Map:  [ ][T][ ]
      [ ][@][ ]
      [ ][ ][ ]
> north
*** You found the TREASURE! 37 gold. You win in 6 moves. ***
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- a game loop that reads commands
- a map in an array and a position that moves
- random fights with hit points
- split a bigger program into methods

**Themes used:** [Loops](../themes/loops.md), [Arrays, text and lists](../themes/arrays.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [L05 · Until zero](../exercises/L05-until-zero.md), [G13 · Diagonal](../exercises/G13-diagonal.md), [R04 · Find the position](../exercises/R04-find-the-position.md), [N01 · Armstrong with methods](../exercises/N01-armstrong-with-methods.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **Two rooms.** Room names and descriptions in arrays. `north` and `south` move between them; `quit` ends.
2. **A map.** 9 rooms in a 3x3 grid: room number = row × 3 + column. Refuse walking through a wall.
3. **Look.** `look` prints the map with `@` where you are.
4. **Treasure.** Hide it in a random room; finding it wins the game.
5. **Monsters.** Some rooms have a slime with hit points. `attack` deals 1 to 4 damage, the slime hits back.
6. **Health and game over.** At 0 HP the game ends. Show HP and gold after each command.
7. **Polish.** `help`, a move counter, and a funny line for unknown commands.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Items:** a potion (+5 HP) and a sword (+2 damage) lying in rooms, and an `inventory` command.
- **Fog of war:** the map only shows rooms you have visited (a `bool[]`).
- **Bigger dungeon from a file:** read the map from a text file where each character is a room or a wall.
- **Save the game:** write the position, HP, gold and visited rooms to a file and load them back.
- **Colours and pauses:** red for damage, yellow for gold ([`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor)), a short pause in fights ([`Thread.Sleep`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.sleep)).

## Hints (open one at a time)

<details><summary>Hint 1: The game loop</summary>

`while (playing) { Console.Write("> "); string command = Console.ReadLine()!.Trim().ToLower(); ... }`. Each command is an `if` (or a [`switch`](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/selection-statements#the-switch-statement)).

</details>

<details><summary>Hint 2: Moving on a 3x3 map</summary>

Keep `row` and `col`. `north` is `row - 1`, but only if `row > 0`. The room number is `row * 3 + col`, the index into your arrays.

</details>

<details><summary>Hint 3: Drawing the map</summary>

Two nested loops over rows and columns, like [G13](../exercises/G13-diagonal.md): print `[@]` at your position, `[ ]` elsewhere.

</details>

<details><summary>Hint 4: Monsters</summary>

`int[] slimeHp` with one cell per room, 0 when there is none. A fight is a small loop that runs while both have HP.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Study skills](../docs/README.md)
