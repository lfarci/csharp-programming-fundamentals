🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 🍳 [Cookbook](README.md) › Recipe 8 · Nested loops

# Recipe 8 · Nested loops — draw 2D grids 🎨

> One loop for the **rows**, one loop inside it for the **columns**. Like writing a page: line after line, letter after letter.

## 🔎 Recognize it

Trigger words: **"draw"**, **"rectangle"**, **"triangle"**, **"pyramid"**, **"grid"**, **"board"**, **"table of tables"**, **"every pair"**, **"rows and columns"**.

## 🧠 The idea

- The **outer** loop picks a row: `row`.
- The **inner** loop walks along that row: `col`, printing **without** a newline (`Console.Write`).
- **After** the inner loop: one `Console.WriteLine()` to go to the next line.

```mermaid
flowchart TD
    accTitle: Nested grid
    accDescr: Outer loop on row from 1 to height. For each row, inner loop on col from 1 to width prints one character. After the inner loop, go to a new line and add 1 to row.
    A["row = 1"] --> B{"row #lt;= height ?"}
    B -- yes --> C["col = 1"]
    C --> D{"col #lt;= width ?"}
    D -- yes --> E["Console.Write('*')"]
    E --> F["col++"]
    F --> D
    D -- no --> G["Console.WriteLine()<br/>new line"]
    G --> H["row++"]
    H --> B
    B -- no --> I(["picture done"])
```

**The secret:** the shape is decided by **what the inner loop does in row `row`**. Write a small table "row → what is printed" before coding:

| Shape | Row `row` contains… | Inner test / char rule |
| --- | --- | --- |
| Rectangle `w × h` | `w` stars | `col <= width` |
| Right triangle | `row` stars | `col <= row` |
| Hollow rectangle | star on the border, space inside | `row == 1 \|\| row == h \|\| col == 1 \|\| col == w` |
| Checkerboard | alternate `#` and `.` | `(row + col) % 2 == 0` |
| Pyramid (height h) | `h - row` spaces, then `2*row - 1` stars | two inner loops |
| Multiplication grid | the numbers `row * col` | print `row * col` |

```text
Rectangle 4x3   Triangle 4   Hollow 5x4   Checkerboard 4   Pyramid 3
****            *            *****        #.#.               *
****            **           *   *        .#.#              ***
****            ***          *   *        #.#.             *****
                ****         *****        .#.#
```

## 📝 Template

```csharp
for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= width; col++)   // <- change THIS test or the char
    {
        Console.Write("*");
    }
    Console.WriteLine();                      // end of the row
}
```

## 🔬 Trace table: triangle of height 3

| `row` | inner loop runs for `col` = | printed line |
| ---: | --- | --- |
| 1 | 1 | `*` |
| 2 | 1, 2 | `**` |
| 3 | 1, 2, 3 | `***` |

Total `Console.Write` calls: 1 + 2 + 3 = 6. The inner loop **starts again from 1** on every row.

## ⚠️ Common mistakes

- `Console.WriteLine("*")` inside the inner loop → one star per line.
- `Console.WriteLine()` **inside** the inner loop instead of after it.
- Using the same variable name `i` for both loops.
- Declaring `col` before the outer loop → it does not restart at 1.
- Start small: first print **one row** of 4 stars. Then repeat that row 3 times. Then change the rule.

## 🏋️ Mini exercises

1. [**G01**](../exercises/G01-rectangle.md) Rectangle `width × height`.
2. [**G02**](../exercises/G02-right-triangle.md) Right triangle, then [**G06**](../exercises/G06-pyramid.md) pyramid.
3. [**G05**](../exercises/G05-checkerboard.md) Checkerboard, and [**G03**](../exercises/G03-multiplication-grid.md) multiplication grid (the same idea with numbers).

➡️ Next: [Recipe 9 · Input validation loop](09-input-validation.md)
