#!/usr/bin/env bash
# Renders every diagrams/*.d2 to diagrams/*.svg with D2 (https://d2lang.com), one shared style (diagrams/_style.d2).
# Usage: tools/diagrams.sh           render all
#        tools/diagrams.sh --check   fail if a committed SVG is missing or differs from its .d2 source
set -euo pipefail
cd "$(dirname "$0")/.."
command -v d2 >/dev/null || { echo "FAIL: d2 is not installed. See https://d2lang.com/tour/install (version in .github/workflows/checks.yml)"; exit 1; }
check=0; [ "${1:-}" = "--check" ] && check=1
tmp=$(mktemp -d); bad=0; n=0
for src in diagrams/*.d2; do
  case "$(basename "$src")" in _*) continue;; esac
  name=$(basename "$src" .d2); n=$((n+1))
  if ! d2 --omit-version "$src" "$tmp/$name.svg" >"$tmp/$name.log" 2>&1; then
    echo "FAIL: $src does not render:"; cat "$tmp/$name.log"; bad=1; continue
  fi
  if [ $check = 1 ]; then
    cmp -s "$tmp/$name.svg" "diagrams/$name.svg" || { echo "FAIL: diagrams/$name.svg is out of date. Run tools/diagrams.sh and commit."; bad=1; }
  else cp "$tmp/$name.svg" "diagrams/$name.svg"; fi
done
[ $bad = 0 ] && echo "OK: $n diagrams $( [ $check = 1 ] && echo 'up to date' || echo 'rendered')"
exit $bad
