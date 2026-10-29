# Terminal demo of the course: start an exercise, see it fail, write it, see it pass.
# Record:  tools/demo/record.sh   (needs vhs, ttyd, ffmpeg)
Output "/tmp/demo-out/demo.mp4"
Output "/tmp/demo-out/demo.gif"
Require git
Require dotnet
Set Shell bash
Set FontSize 16
Set Width 1200
Set Height 960
Set Padding 20
Set TypingSpeed 35ms
Set Theme "Builtin Light"
Set WaitPattern /\$$/

Hide
Type "export PS1='$ ' PATH=$HOME/.dotnet:$PATH && cd /tmp && rm -rf csharp-programming-fundamentals && clear" Enter
Show

Type "# 1. Get the course (once)" Enter
Type "git clone -q https://github.com/lfarci/csharp-programming-fundamentals.git && cd csharp-programming-fundamentals" Enter
Wait
Sleep 1s

Type "# 2. Start an exercise: it creates your file in practice/" Enter
Type "./ex start L11" Enter
Wait
Sleep 3s
Hide
Type "clear" Enter
Show

Type "# 3. Check it before writing anything: NOT YET, and why" Enter
Type "./ex check" Enter
Wait@90s
Sleep 4s
Hide
Type "clear" Enter
Show

Type "# The tests are plain: one file per exercise" Enter
Type "sed -n 11,18p tests/Practice.Tests/Exercises/L11_CountFromAToBTests.cs" Enter
Wait
Sleep 4s
Hide
Type "clear" Enter
Show

Hide
Type `python3 "$DEMO_EDIT" practice/L11_CountFromAToB.cs 'for (int i = a; i < b; i++)\n{\n    Console.WriteLine(i);\n}' && clear` Enter
Show
Type "# 4. Sam writes a first try in her editor (a for loop)" Enter
Type "sed -n 17,23p practice/L11_CountFromAToB.cs" Enter
Wait
Sleep 2s
Type "./ex check" Enter
Wait@60s
Sleep 5s
Hide
Type "clear" Enter
Show

Hide
Type "sed -i 's/i < b/i <= b/' practice/L11_CountFromAToB.cs && clear" Enter
Show
Type "# The last number is missing: i < b stops one too early. She fixes it: i <= b" Enter
Type "sed -n 17,23p practice/L11_CountFromAToB.cs" Enter
Wait
Sleep 2s
Type "./ex check" Enter
Wait@60s
Sleep 4s
Hide
Type "clear" Enter
Show

Type "# 5. Done. See how far you are" Enter
Type "./ex progress | head -12" Enter
Wait@120s
Sleep 4s
Type "# 6. And go on with the next exercise" Enter
Type "./ex next" Enter
Wait@60s
Sleep 4s
