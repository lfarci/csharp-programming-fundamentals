#!/usr/bin/env bash
# Records the demo from a fresh clone in /tmp, then makes a small GIF for the docs.
# Needs: vhs (go install github.com/charmbracelet/vhs@latest), ttyd, ffmpeg, the .NET SDK.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
mkdir -p /tmp/demo-out
DEMO_EDIT="$here/edit.py" vhs "$here/demo.tape"
# Smaller GIF for the docs (target: under 3 MB).
ffmpeg -y -loglevel error -i /tmp/demo-out/demo.mp4 \
  -vf "fps=6,scale=900:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=32[p];[b][p]paletteuse=dither=none" \
  /tmp/demo-out/demo-small.gif
ls -la /tmp/demo-out
