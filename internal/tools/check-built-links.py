#!/usr/bin/env python3
"""Checks every link between pages of the BUILT website (internal/site/.vitepress/dist).

VitePress's dead-link check resolves a link from the source file, so a link to a page moved by a
`rewrites` entry (answer-keys/X.md is served at /solutions/X) passes the build but 404s on the site.
This check reads the final HTML: every same-site href must point to a file that exists in dist/."""
import html, os, re, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST = os.path.join(ROOT, "internal/site/.vitepress/dist")
BASE = "/csharp-programming-fundamentals/"
if not os.path.isdir(DIST): sys.exit("FAIL: build the site first (npm --prefix internal run docs:build)")

def exists(path):  # path: inside dist, no leading slash; cleanUrls: x -> x.html, folder -> folder/index.html
    p = os.path.join(DIST, path)
    return any(os.path.isfile(c) for c in (p, p + ".html", os.path.join(p, "index.html")))

bad = []
for d, _, files in os.walk(DIST):
    for f in files:
        if not f.endswith(".html"): continue
        page = os.path.join(d, f); rel = "/" + os.path.relpath(page, DIST).replace(os.sep, "/")
        for href in re.findall(r'<a [^>]*?href="([^"]*)"', open(page, encoding="utf-8").read()):
            href = html.unescape(href).split("#")[0].split("?")[0]
            if not href or re.match(r"^[a-z]+:|^//", href, re.I): continue
            target = urllib.parse.urljoin(BASE + rel.lstrip("/"), href)
            if not target.startswith(BASE): bad.append(f"{rel}: {href} leaves the site base"); continue
            if not exists(urllib.parse.unquote(target[len(BASE):]).strip("/")): bad.append(f"{rel}: {href} (404)")
for b in sorted(set(bad)): print("FAIL:", b)
if bad: sys.exit(1)
print("OK: every link between site pages lands on a built page")
