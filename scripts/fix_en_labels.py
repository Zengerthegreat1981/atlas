#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_en_labels.py — remove Arabic from EN display fields (title/crumb/dates/related titles).
- title: if Arabic and `en:` is clean English -> title = en
- crumb: 'علم الاجتماع' -> 'Sociology'; Arabic crumb tail -> English title
- dates: token map (countries, qualifiers)
- related titles that are Arabic -> English title of the target node (by id)
Only those frontmatter lines change. Type/level stay (internal keys; displayed via build map)."""
import os, re, sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EN = os.path.join(ROOT, "content", "en")
AR = re.compile(r"[\u0600-\u06FF]")
TOK = [("النمسا-المجر","Austria-Hungary"),("الولايات المتحدة","USA"),("يحتاج تحقق مباشر","needs direct verification"),
 ("يحتاج تحقق","needs verification"),("تحتاج تحقق","needs verification"),("طبيب نفسي وفيلسوف","psychiatrist and philosopher"),
 ("من الثمانينيات","from the 1980s"),("من الثلاثينيات","from the 1930s"),("من الخمسينيات","from the 1950s"),
 ("كندا (أصل سويسري)","Canada (Swiss-born)"),("القرن 19","19th century"),("سويسرا","Switzerland"),("بريطانيا","Britain"),
 ("النمسا","Austria"),("فرنسا","France"),("ألمانيا","Germany"),("روسيا","Russia"),("إسبانيا","Spain"),("هولندا","Netherlands"),
 ("كندا","Canada"),("الدنمارك","Denmark"),("الصين","China"),("إسرائيل","Israel"),("ليتوانيا","Lithuania"),("أمريكا","America"),
 ("براغ","Prague"),("فيلسوفة","philosopher"),("معاصرة","contemporary"),("سارتر","Sartre"),("هايدجر","Heidegger"),
 ("كيركيغارد","Kierkegaard"),("إيطاليا","Italy"),("اليونان","Greece"),("مصر","Egypt"),("العراق","Iraq"),("الجزائر","Algeria"),
 ("المغرب","Morocco"),("لبنان","Lebanon"),("إيران","Iran"),("الهند","India"),("اليابان","Japan"),("دولي","International"),
 ("مفكر","thinker"),("أسترالي","Australian"),("بولندا","Poland"),("المجر","Hungary"),("سوريا","Syria"),("تونس","Tunisia")]
TOK.sort(key=lambda kv: -len(kv[0]))

def files():
    for root, dirs, fs in os.walk(EN):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("drafts","_merged")]
        for f in fs:
            if f.endswith(".md") and not f.startswith("._") and f.upper() != "README.MD":
                yield os.path.join(root, f)

def fm_get(fm, key):
    m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else ""

def main():
    paths = list(files()); titles = {}
    for p in paths:
        t = open(p, encoding="utf-8", newline="").read()
        m = re.match(r"^---\s*\n(.*?)\n---", t, re.S)
        if m:
            ti, en = fm_get(m.group(1), "title"), fm_get(m.group(1), "en")
            titles[os.path.splitext(os.path.basename(p))[0]] = ti if not AR.search(ti) else (en if en and not AR.search(en) else ti)
    changed = 0; left = []
    for p in paths:
        t = open(p, encoding="utf-8", newline="").read()
        m = re.match(r"^(---\s*\r?\n)(.*?)(\r?\n---)", t, re.S)
        if not m: continue
        fm = m.group(2); orig = fm
        en = fm_get(fm, "en"); ti = fm_get(fm, "title")
        if AR.search(ti) and en and not AR.search(en):
            fm = re.sub(r"^title:.*$", lambda mm: f'title: "{en}"', fm, count=1, flags=re.M); ti = en
        cr = fm_get(fm, "crumb")
        if AR.search(cr):
            new = cr.replace("علم الاجتماع", "Sociology")
            if AR.search(new) and ti and not AR.search(ti): new = "Sociology ← " + ti
            fm = re.sub(r"^crumb:.*$", lambda mm: f'crumb: "{new}"', fm, count=1, flags=re.M)
        da = fm_get(fm, "dates")
        if AR.search(da):
            new = da
            for a, b in TOK: new = new.replace(a, b)
            fm = re.sub(r"^dates:.*$", lambda mm: f'dates: "{new}"', fm, count=1, flags=re.M)
            if AR.search(new): left.append((os.path.basename(p), new))
        def rel(mm):
            line = mm.group(0)
            idm = re.search(r'id:\s*"?([^",\s]+)"?', line); tm = re.search(r'title:\s*"([^"]*)"', line)
            if idm and tm and AR.search(tm.group(1)) and titles.get(idm.group(1)) and not AR.search(titles[idm.group(1)]):
                return line.replace(tm.group(0), f'title: "{titles[idm.group(1)]}"')
            return line
        fm = re.sub(r"^\s*-\s*id:.*title:.*$", rel, fm, flags=re.M)
        if fm != orig:
            open(p, "w", encoding="utf-8", newline="").write(t[:m.start(2)] + fm + t[m.end(2):]); changed += 1
    print("changed", changed, "dates still Arabic:", left)
main()
