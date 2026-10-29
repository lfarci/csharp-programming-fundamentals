#!/usr/bin/env bash
# Waits until the live site serves the build of a given commit (GitHub Pages and its cache can lag a few minutes).
# Usage: internal/tools/wait-for-deploy.sh <site-url> <sha> [timeout-seconds, default 300]
# Checks /version.txt and the home page's <meta name="build-sha">, with a cache-busting query.
set -uo pipefail
url=${1%/}; sha=$2; timeout=${3:-300}; start=$(date +%s)
echo "Waiting for $url to serve build $sha (timeout ${timeout}s)"
while :; do
  t=$(date +%s); bust="?t=$t$RANDOM"
  version=$(curl -fsS -H 'Cache-Control: no-cache' "$url/version.txt$bust" 2>/dev/null | tr -d '[:space:]')
  meta=$(curl -fsS -H 'Cache-Control: no-cache' "$url/$bust" 2>/dev/null | grep -o 'name="build-sha" content="[0-9a-f]*"' | grep -o '[0-9a-f]\{7,\}' | tail -1)
  elapsed=$((t - start))
  if [ "$version" = "$sha" ] && [ "$meta" = "$sha" ]; then echo "OK: live site serves $sha (after ${elapsed}s)"; exit 0; fi
  echo "  ${elapsed}s: version.txt=${version:-none} home meta=${meta:-none}"
  [ "$elapsed" -ge "$timeout" ] && { echo "FAIL: the live site still does not serve $sha after ${timeout}s"; exit 1; }
  sleep 10
done
