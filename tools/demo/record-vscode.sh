#!/usr/bin/env bash
# Records the VS Code demo: fresh clone in /tmp, VS Code on a virtual display driven by xdotool,
# screen captured with ffmpeg. Every command shown really runs.
# Needs: code (VS Code), Xvfb, xdotool, ffmpeg, git, the .NET SDK (~/.dotnet or on PATH).
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)/vscode
out=${OUT:-/tmp/demo-out}; W=1600; H=900; export DISPLAY=:77
repo=/tmp/csharp-programming-fundamentals; prof=/tmp/demo-vscode
mkdir -p "$out"; rm -rf "$repo" "$prof"; mkdir -p "$prof/User"
cp "$here/settings.json" "$here/keybindings.json" "$prof/User/"
git clone -q "${REPO_URL:-https://github.com/lfarci/csharp-programming-fundamentals.git}" "$repo"
cat > /tmp/demo-rc <<'RC'
export PS1='\[\e[1;32m\]$ \[\e[0m\]' PATH=$HOME/.dotnet:$PATH DOTNET_NOLOGO=1 DOTNET_CLI_TELEMETRY_OPTOUT=1
PROMPT_COMMAND='date +%s%N > /tmp/demo-prompt'
code() { command code --user-data-dir /tmp/demo-vscode --extensions-dir /tmp/demo-vscode/ext -r "$@"; }
RC
ff=; Xvfb $DISPLAY -screen 0 ${W}x${H}x24 -nolisten tcp >/dev/null 2>&1 & xvfb=$!
trap 'kill $ff $xvfb 2>/dev/null; pkill -f "user-data-dir $prof" || true' EXIT
sleep 1
code --no-sandbox --disable-gpu --disable-workspace-trust --skip-release-notes --skip-welcome \
  --user-data-dir "$prof" --extensions-dir "$prof/ext" --new-window "$repo" >/dev/null 2>&1 &
for _ in $(seq 60); do win=$(xdotool search --onlyvisible --name "Visual Studio Code" 2>/dev/null | head -1) && [ -n "$win" ] && break; sleep 1; done
xdotool windowmove "$win" 0 0 windowsize "$win" $W $H windowfocus "$win"; sleep 6
k() { xdotool key --clearmodifiers "$@"; sleep 0.4; }
t() { xdotool type --delay "${D:-45}" -- "$1"; }
wait_prompt() { local before=$(cat /tmp/demo-prompt 2>/dev/null); for _ in $(seq 240); do sleep 0.5; [ "$(cat /tmp/demo-prompt 2>/dev/null)" != "$before" ] && return; done; }
run() { t "$1"; sleep 0.3; : > /tmp/demo-prompt.tmp; local before=$(cat /tmp/demo-prompt 2>/dev/null); k Return; for _ in $(seq 240); do sleep 0.5; [ "$(cat /tmp/demo-prompt 2>/dev/null)" != "$before" ] && break; done; sleep "${2:-2}"; }
ffmpeg -y -loglevel error -f x11grab -framerate 25 -video_size ${W}x${H} -i $DISPLAY \
  -c:v libx264 -preset veryfast -crf 23 -pix_fmt yuv420p "$out/raw.mp4" & ff=$!
xdotool mousemove $W $H; sleep 2
k ctrl+grave; sleep 3                          # open the integrated terminal
run "# Step 1: the course is cloned and open in VS Code" 1
run "# Step 2: start an exercise, it creates your file in practice/" 0.5
run "./ex start L11" 3
k ctrl+alt+m; run "# Step 3: check it before writing anything: NOT YET, and why" 0.5
run "./ex check" 5
k ctrl+alt+m; run clear 0.5
run "# The tests are plain C#: one file per exercise" 0.3
run "code tests/Practice.Tests/Exercises/L11_CountFromAToBTests.cs" 5
k ctrl+alt+t; run "# Now write the method in your file" 0.3
run "code practice/L11_CountFromAToB.cs" 2
k ctrl+g; t "19"; k Return; sleep 1
k Home; k shift+End; sleep 0.8
t "for (int i = a; i < b; i++)"; k Return
t "            {"; k Return
t "                Console.WriteLine(i);"; k Return
t "            }"; sleep 1; k ctrl+s; sleep 1.5
k ctrl+alt+t; run "# Step 4: a first try with a for loop. Check again" 0.5
k ctrl+alt+m; run "./ex check" 6
run "# The last number is missing: i < b stops one too early" 1.5
k ctrl+alt+m; k ctrl+alt+e; sleep 0.5
k ctrl+f; t "i < b"; sleep 0.8; k Escape; sleep 0.5
t "i <= b"; sleep 1; k ctrl+s; sleep 1.5
k ctrl+alt+t; run clear 0.3
run "# Step 5: the fix is i <= b. Check again" 0.5
k ctrl+alt+m; run "./ex check" 5
run clear 0.3
run "# Step 6: done. See how far you are, then go on" 0.5
run "./ex progress | head -14" 4
run "./ex next" 5
kill -INT $ff; wait $ff || true
"$here/../make-gif.sh" "$out/raw.mp4" "$out"
