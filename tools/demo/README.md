# Demo recording

The GIF in the README and in `docs/getting-started.md` (`docs/assets/demo.gif`) shows a learner in
VS Code: `./ex start L11`, `./ex check` says NOT YET, a first loop misses the last number, the fix
`i <= b` makes it DONE, then `./ex progress` and `./ex next`. Every command in it really runs.

## Regenerate (VS Code, the default)

Needs Linux with VS Code (`code`), Xvfb, xdotool, ffmpeg, git and the .NET SDK.

```bash
tools/demo/record-vscode.sh            # writes /tmp/demo-out/demo.mp4 and demo.gif
cp /tmp/demo-out/demo.gif docs/assets/demo.gif
```

How it works:

- It clones the course into `/tmp`, starts VS Code on a virtual display (1600x900) with a clean
  profile from `vscode/settings.json` and `vscode/keybindings.json` (no welcome page, no workspace
  trust, no telemetry, no minimap, larger fonts, no auto-closing brackets so typing looks natural).
- xdotool types the commands in the integrated terminal and the loop in the editor.
- ffmpeg records the screen; `make-gif.sh` turns the recording into an MP4 (H.264) and a small GIF.
- Set `REPO_URL` to record from another clone, `OUT` to change the output folder.

## Alternative: terminal only (vhs)

`record.sh` with `demo.tape` and `edit.py` records the same story in a plain terminal with
[vhs](https://github.com/charmbracelet/vhs).
