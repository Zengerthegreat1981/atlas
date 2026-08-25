# -*- coding: utf-8 -*-
"""يضيف أقسام المحتوى لملفات ليس في جسمها أي عنوان فرعي (`## `).

يختلف عن `write_shell_bodies.py`: هناك يُستبدل نصّ قالبي، وهنا **يُضاف** محتوى
إلى ملف ليس فيه إلا السطر التعريفي. يرفض السكريبت أي ملف يحتوي جسمه على `## `
أصلاً، حتى لا يُمحى محتوى قائم.
"""
import json, os, re, sys
THK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "content", "ar", "thinkers")
data = json.load(open(sys.argv[1], encoding="utf-8"))
apply = "--apply" in sys.argv
ok = bad = 0
for slug, body in data.items():
    p = os.path.join(THK, slug + ".md")
    if not os.path.exists(p): print("MISSING", slug); bad += 1; continue
    t = open(p, encoding="utf-8").read()
    pre, fm, b = t.split("---", 2)
    if "## " in b:
        print("HAS SECTIONS ALREADY (skipped)", slug); bad += 1; continue
    m = re.search(r'^# .*\n\n.*\n', b, re.M)
    if not m: print("NO LEDE (skipped)", slug); bad += 1; continue
    new = pre + "---" + fm + "---" + b[:m.end()] + "\n" + body.strip() + "\n"
    if apply: open(p, "w", encoding="utf-8").write(new)
    ok += 1
print(f"{'APPLIED' if apply else 'DRY RUN'} — {ok} written, {bad} skipped")
