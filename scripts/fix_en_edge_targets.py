#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace slug-like edge targets that have no EN file with the readable English name (from the AR node's
`en`/title, else a title-cased slug). Edge targets are names by convention in this tree."""
import glob, os, re, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
en = {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT, "content", "en", "*", "*.md"))}
ar = {os.path.basename(p)[:-3]: p for p in glob.glob(os.path.join(ROOT, "content", "ar", "*", "*.md"))}
SLUG = re.compile(r"^[a-z]{2,5}-[a-z0-9-]+$")
def name(s):
    if s in ar:
        h = open(ar[s], encoding="utf-8", errors="replace").read(1500)
        m = re.search(r'^en:\s*["\']?(.*?)["\']?\s*$', h, re.M)
        if m and m.group(1) and not re.search(r"[\u0600-\u06FF]", m.group(1)): return re.sub(r"\s*\(.*?\)\s*$", "", m.group(1)).strip()
    return " ".join(w.capitalize() for w in s.split("-")[1:])
n = 0
for p in glob.glob(os.path.join(ROOT, "content", "en", "*", "*.md")):
    t = open(p, encoding="utf-8", newline="").read()
    def f(m):
        tg = m.group(2)
        return m.group(1) + (name(tg) if SLUG.match(tg) and tg not in en else tg) + m.group(3)
    t2 = re.sub(r'(target:\s*")([^"]*)(")', f, t)
    if t2 != t: open(p, "w", encoding="utf-8", newline="").write(t2); n += 1
print("files changed", n)
