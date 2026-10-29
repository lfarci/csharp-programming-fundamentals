#!/usr/bin/env python3
"""Check Markdown links: relative files + #anchors always; http(s) with --external."""
import os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")
external = "--external" in sys.argv

def md_files():
    out = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True).stdout
    return [os.path.join(ROOT, p) for p in out.split()]

def slug(h):
    h = re.sub(r"[`*_]", "", h.strip().lower())
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")

def anchors(path):
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    seen, res = {}, set()
    for h in re.findall(r"^#{1,6} (.+)$", text, flags=re.M):
        s = slug(h); n = seen.get(s, 0); seen[s] = n + 1
        res.add(s if n == 0 else f"{s}-{n}")
    return res

bad, urls = [], set()
for f in md_files():
    text = re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S)
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://")):
            urls.add(target); continue
        if target.startswith("mailto:"):
            continue
        path, _, anchor = target.partition("#")
        dest = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        rel = os.path.relpath(f, ROOT)
        if not os.path.exists(dest):
            bad.append(f"{rel}: missing file {target}")
        elif anchor and dest.endswith(".md") and anchor not in anchors(dest):
            bad.append(f"{rel}: missing anchor {target}")

if external:
    for u in sorted(urls):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 link-check"})
            code = urllib.request.urlopen(req, timeout=20).status
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:
            code = str(e)
        if code == 404 or not isinstance(code, int):
            bad.append(f"external {u}: {code}")

for b in bad: print("❌", b)
print(f"{'✅' if not bad else '❌'} links checked ({len(urls)} external {'checked' if external else 'skipped'}), {len(bad)} problem(s)")
sys.exit(1 if bad else 0)
