#!/usr/bin/env bash
# Runs the same checks as .github/workflows/checks.yml.
# Usage: tools/verify.sh [--external]   (--external also checks web links, with lychee if installed)
set -uo pipefail
cd "$(dirname "$0")/.."
status=0
step() { echo; echo "== $1"; shift; "$@" || status=1; }

regen() {
  # Run the generator on a copy, then compare with the working tree.
  local tmp; tmp=$(mktemp -d)
  cp -r tools exercises solutions docs tests themes learn diagrams ROADMAP.md .vitepress "$tmp"/
  python3 "$tmp/tools/generator/gen.py" >/dev/null || return 1
  local bad=0
  for p in exercises solutions themes learn ROADMAP.md diagrams/roadmap.d2 docs/progress-checklist.md tools/starters tools/exercises.json tests/Practice.Tests/Exercises .vitepress/course.json; do
    diff -r -x bin -x obj "$tmp/$p" "$p" >/dev/null || { echo "FAIL: $p differs from generator output"; bad=1; }
  done
  [ $bad = 0 ] && echo "OK: generator output identical to the files" ||
    { echo "   Edit tools/generator/data*.py, run python3 tools/generator/gen.py, commit both."; return 1; }
}

step "Generator in sync" regen
step "Exercises: solutions pass, starters compile, ./ex works" tools/check-exercises.sh
step "No emoji" python3 tools/check-no-emoji.py
step "Links (internal)" python3 tools/check-links.py
lychee_check() {
  if command -v lychee >/dev/null; then lychee --config lychee.toml --root-dir "$PWD" --no-progress './**/*.md'
  else python3 tools/check-links.py --external; fi
}
if [ "${1:-}" = "--external" ]; then step "Links (external)" lychee_check; fi
step "Diagrams (D2 sources match the SVGs)" tools/diagrams.sh --check
site() { [ -d node_modules ] || npm ci --silent; node tools/check-site-sync.ts && npm run --silent docs:build >/dev/null && echo "OK: website builds"; }
step "Website (VitePress build, no dead links)" site
site_test() { [ -d ~/.cache/ms-playwright ] || npx playwright install chromium >/dev/null; npx playwright test --reporter=line; }
step "Website: progress ticks work in a real browser" site_test
step "Markdown lint" npx -y markdownlint-cli2@0.24.0
step "Spelling" npx -y cspell@10.4.0 --no-progress "**/*.md"
echo; [ $status = 0 ] && echo "OK: ALL CHECKS PASSED" || echo "FAIL: SOME CHECKS FAILED"
exit $status
