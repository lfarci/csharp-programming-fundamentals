#!/usr/bin/env bash
# Usage: make-gif.sh RAW.mp4 OUTDIR -> OUTDIR/demo.mp4 (H.264, yuv420p) and OUTDIR/demo.gif (small, for the docs).
set -euo pipefail
raw=$1; out=$2
ffmpeg -y -loglevel error -i "$raw" -c:v libx264 -crf 24 -pix_fmt yuv420p -movflags +faststart "$out/demo.mp4"
ffmpeg -y -loglevel error -i "$raw" \
  -vf "fps=5,scale=960:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=48:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle" \
  "$out/demo.gif"
ls -la "$out"
