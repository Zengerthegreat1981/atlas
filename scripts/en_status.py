#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
en_status.py — قياسُ حالة النسخة الإنجليزية في أمرٍ واحد.

الغرض: منع تكرار الخطأ الذي وقع في content/en/README.md (أرقامُ 2026-09-10
بقيت معروضةً بعد أن تغيّرت الحالة). شغّل هذا قبل أيّ تعديلٍ على حالة النسخة
الإنجليزية، وقارن أرقامَه بأرقام الملفّ.

    python3 scripts/en_status.py            # الطباعة فقط
    python3 scripts/en_status.py --json     # للمخرجات الآلية

القاعدة: كلُّ رقمٍ في ملفّ حالةٍ بلا تاريخ قياسٍ لا يُؤتمن.
"""
import os, re, sys, glob, json, unicodedata, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AR_RE = re.compile(r"[\u0600-\u06FF]")


def norm(s):
    return unicodedata.normalize("NFC", s)


def field(text, key):
    m = re.search(r"^" + key + r':\s*"?(.*?)"?\s*$', text, re.M)
    return (m.group(1) or "").strip().strip('"') if m else ""


def load(root):
    out = {}
    for f in glob.glob(root + "/**/*.md", recursive=True):
        b = os.path.basename(f)
        if b.startswith("._") or "/_merged/" in f or "/drafts/" in f:
            continue
        raw = os.path.splitext(b)[0]
        t = open(f, encoding="utf-8").read()
        out[norm(raw)] = {"path": f, "en_name": field(t, "en") or field(t, "title")}
    return out


def body_words(path):
    t = open(path, encoding="utf-8").read()
    body = t.split("---", 2)[-1] if t.count("---") >= 2 else t
    return len(body.split())


def main():
    en = load(os.path.join(ROOT, "content", "en"))
    ar = load(os.path.join(ROOT, "content", "ar"))

    placeholder = arabic_title = translated = 0
    for s, meta in en.items():
        if s == "README":
            continue
        t = open(meta["path"], encoding="utf-8").read()
        if "EN TRANSLATION NEEDED" in t:
            placeholder += 1
        elif AR_RE.search(field(t, "title")):
            arabic_title += 1
        else:
            translated += 1

    m_path = os.path.join(ROOT, "scripts", "en_slug_map.json")
    mapped = same = unmapped = None
    if os.path.exists(m_path):
        m = json.load(open(m_path, encoding="utf-8"))
        mapped_en = {p["en_slug"] for p in m["pairs"]} | {
            p["en_slug"] for p in m.get("duplicate_en_twins", [])
        }
        same = len((set(en) & set(ar)) - {"README"})
        unmapped = len((set(en) - set(ar) - mapped_en) - {"README"})
        mapped = len(mapped_en)

    nfd = [s for s in en if os.path.basename(en[s]["path"])[:-3] != s]

    result = {
        "en_files": len(en),
        "content_files": len(en) - 1,
        "placeholder": placeholder,
        "arabic_title": arabic_title,
        "translated": translated,
        "remaining_to_translate": placeholder + arabic_title,
        "ar_active": len(ar),
        "coverage_pct": round(100 * len(en) / len(ar), 1),
        "translation_pct": round(100 * translated / len(ar), 1),
        "slug_map": {"same": same, "mapped": mapped, "unmapped": unmapped},
        "nfd_filenames": nfd,
        "build_outputs": {
            f: (os.path.getmtime(os.path.join(ROOT, f)) if os.path.exists(os.path.join(ROOT, f)) else None)
            for f in ("data.json", "data-en.json")
        },
    }

    if "--json" in sys.argv:
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return

    print("حالة النسخة الإنجليزية — قياسٌ فعلي")
    print(f"  ملفات en: {result['en_files']} (المحتوى: {result['content_files']})")
    print(f"  نائبة: {placeholder} | عنوانها عربي: {arabic_title} | مترجمة: {translated}")
    print(f"  المتبقّي للترجمة: {result['remaining_to_translate']}")
    print(f"  مقابل {result['ar_active']} عقدة عربية — تغطية {result['coverage_pct']}% | ترجمة {result['translation_pct']}%")
    if mapped is not None:
        print(f"  slugs: متطابقة {same} | بحاجة خريطة {mapped} | بلا مقابل {unmapped}")
    if nfd:
        print(f"  ⚠️ أسماء NFD: {', '.join(nfd)}")
    for f, mt in result["build_outputs"].items():
        import datetime
        d = datetime.datetime.fromtimestamp(mt).strftime("%Y-%m-%d") if mt else "غير موجود"
        print(f"  {f}: {d}")


if __name__ == "__main__":
    main()
