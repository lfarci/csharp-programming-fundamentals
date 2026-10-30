#!/usr/bin/env bash
# Runs the same checks as .github/workflows/checks.yml.
# Usage: internal/tools/verify.sh [--external]   (--external also checks web links, with lychee if installed)
set -uo pipefail
cd "$(dirname "$0")/../.."  # the repo root
status=0
step() { echo; echo "== $1"; shift; "$@" || status=1; }

regen() {
  # Run the generator on a copy, then compare with the working tree.
  local tmp; tmp=$(mktemp -d)
  cp -r course "$tmp"/ && mkdir -p "$tmp/internal/site" &&
    cp -r internal/tools internal/tests internal/solutions "$tmp/internal"/ && cp -r internal/site/.vitepress "$tmp/internal/site"/
  python3 "$tmp/internal/tools/generator/gen.py" >/dev/null || return 1
  local bad=0
  for p in course/exercises course/answer-keys internal/solutions course/themes course/learn course/ROADMAP.md course/diagrams/roadmap.d2 course/docs/progress-checklist.md course/docs/README.md internal/tools/starters internal/tools/exercises.json internal/tests/Practice.Tests/Exercises internal/site/.vitepress/course.json; do
    diff -r -x bin -x obj -x cache -x dist "$tmp/$p" "$p" >/dev/null || { echo "FAIL: $p differs from generator output"; bad=1; }
  done
  [ $bad = 0 ] && echo "OK: generator output identical to the files" ||
    { echo "   Edit internal/tools/generator/data*.py, run python3 internal/tools/generator/gen.py, commit both."; return 1; }
}

step "Generator in sync" regen
step "Course structure (titles, groups, levels, balance, sidebar)" python3 internal/tools/check-structure.py
step "Exercises: solutions pass, starters compile, ./ex works" internal/tools/check-exercises.sh
step "No emoji" python3 internal/tools/check-no-emoji.py
step "Links (internal)" python3 internal/tools/check-links.py
lychee_check() {
  if command -v lychee >/dev/null; then lychee --config internal/lychee.toml --root-dir "$PWD" --no-progress './**/*.md'
  else python3 internal/tools/check-links.py --external; fi
}
if [ "${1:-}" = "--external" ]; then step "Links (external)" lychee_check; fi
step "Diagrams (D2 sources match the SVGs)" internal/tools/diagrams.sh --check
npmi() { npm --prefix internal "$@"; }   # the website tools live in internal/ (package.json)
site() { [ -d internal/node_modules ] || npmi ci --silent; node internal/tools/check-site-sync.ts && npmi run --silent docs:build >/dev/null && echo "OK: website builds"; }
step "Website (VitePress build, no dead links)" site
site_test() { [ -d ~/.cache/ms-playwright ] || npmi exec playwright install chromium >/dev/null; npmi run --silent test:site -- --reporter=line; }
step "Website: progress ticks work in a real browser" site_test
step "Root folder (only the allowed entries)" python3 internal/tools/check-root.py
step "Prose (doubled words, stray spaces, code spans)" python3 internal/tools/check-prose.py
step "Markdown lint" npx -y markdownlint-cli2@0.24.0 --config internal/.markdownlint-cli2.jsonc
step "Spelling" npx -y cspell@10.4.0 -c internal/cspell.json --no-progress "**/*.md"
echo; [ $status = 0 ] && echo "OK: ALL CHECKS PASSED" || echo "FAIL: SOME CHECKS FAILED"
exit $status
