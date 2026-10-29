#!/usr/bin/env bash
# Render every ```mermaid block in every tracked .md file. Fails on the first syntax error.
set -euo pipefail
cd "$(dirname "$0")/.."
out=$(mktemp -d)
cfg="$out/puppeteer.json"; echo '{"args":["--no-sandbox"]}' > "$cfg"
n=0; fail=0
for f in $(git ls-files '*.md'); do
  grep -q '^```mermaid' "$f" || continue
  n=$((n+1))
  if ! npx -y -p "${MERMAID_CLI:-@mermaid-js/mermaid-cli@12.0.0}" mmdc -q -p "$cfg" -i "$f" -o "$out/$(echo "$f" | tr / _)" >"$out/log" 2>&1; then
    echo "❌ $f"; cat "$out/log"; fail=1
  fi
done
[ $fail = 0 ] && echo "✅ mermaid: $n files rendered" || { echo "❌ mermaid errors"; exit 1; }
