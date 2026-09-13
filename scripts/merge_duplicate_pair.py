# -*- coding: utf-8 -*-
"""يدمج عقدتين تصفان الشيءَ نفسَه تحت بادئتين مختلفتين.

    python3 scripts/merge_duplicate_pair.py <القانوني> <المُحال> <ملفُّ المتن المدموج>

ما يفعله:
  1. يحفظ نسخةَ المُحال كما هي في `content/ar/_merged/` (لا يضيع شيء).
  2. يكتب المتنَ المدموج في الملفّ القانوني، ويوحِّد ترويستَه:
     `related` و`edges` اتحادٌ بلا تكرار، و`gaps` اتحادٌ، والهويةُ تبقى للقانوني.
  3. يحوّل المُحال إلى إحالةٍ صريحة: `redirect_to` وعنوانٌ يقول ذلك ومتنٌ يشير.
  4. يعيد توجيه كلِّ إشارةٍ واردةٍ في الأطلس من المُحال إلى القانوني.
المعرِّفات (`id`) لا تُمسّ أبداً — كلاهما يحتفظ بمعرِّفه.
"""
import os, re, sys, glob, json, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AR = os.path.join(ROOT, "content", "ar")
MERGED = os.path.join(AR, "_merged")
TODAY = "2026-09-13"

REL_RE = re.compile(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"')
EDG_RE = re.compile(r'-\s*rel:\s*"([^"]*)"\s*,\s*target:\s*"([^"]*)"\s*,\s*target_type:\s*"([^"]*)"')


def paths():
    return {os.path.basename(f)[:-3]: f
            for f in glob.glob(os.path.join(AR, "*", "*.md"))
            if "/_merged/" not in f and "/drafts/" not in f}


def split(p):
    s = open(p, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", s, re.S)
    if not m:
        raise SystemExit(f"ترويسةٌ غيرُ صالحة: {p}")
    return m.group(1), m.group(2)


def field(fm, key):
    m = re.search(rf'^{key}:\s*"(.*?)"\s*$', fm, re.M)
    return m.group(1) if m else None


def block(fm, key):
    """أسطرُ كتلةٍ (related/edges/gaps) كما هي."""
    out, on = [], False
    for ln in fm.split("\n"):
        if re.match(rf"^{key}:\s*$", ln):
            on = True; continue
        if re.match(rf"^{key}:\s*\[\]\s*$", ln):
            return []
        if on:
            if ln.startswith("  ") or ln.startswith("- ") or ln.strip() in ("[]",):
                if ln.strip() not in ("[]",): out.append(ln)
                continue
            on = False
    return out


def strip_blocks(fm):
    """الترويسةُ بلا كتل related/edges/gaps."""
    out, skip = [], False
    for ln in fm.split("\n"):
        if re.match(r"^(related|edges|gaps):", ln):
            skip = True; continue
        if skip:
            if ln.startswith("  ") or ln.startswith("- ") or not ln.strip():
                continue
            skip = False
        out.append(ln)
    return [l for l in out if l.strip()]


def main():
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    canon, dup, bodyfile = sys.argv[1], sys.argv[2], sys.argv[3]
    P = paths()
    for s in (canon, dup):
        if s not in P: raise SystemExit(f"لا ملفَّ لـ{s}")
    cfm, cbody = split(P[canon])
    dfm, dbody = split(P[dup])
    ctitle = field(cfm, "title")

    # 1) أرشفةُ المُحال كما هو
    os.makedirs(MERGED, exist_ok=True)
    open(os.path.join(MERGED, dup + ".md"), "w", encoding="utf-8").write(
        "---\n" + dfm + "\n---\n" + dbody.rstrip("\n") +
        f"\n\n# ⚠️ دُمج هذا الملفُّ في `{canon}` بتاريخ {TODAY}. "
        f"هذه نسختُه كما كانت قبل الدمج، محفوظةً للسجلّ.\n")

    # 2) اتحادُ الكتل
    seen, rel = set(), []
    for ln in block(cfm, "related") + block(dfm, "related"):
        m = REL_RE.search(ln)
        if not m: continue
        if m.group(1) in (canon, dup) or m.group(1) in seen: continue
        seen.add(m.group(1)); rel.append(ln.rstrip())
    seene, edg = set(), []
    for ln in block(cfm, "edges") + block(dfm, "edges"):
        m = EDG_RE.search(ln)
        if not m: continue
        k = (m.group(1), m.group(2))
        if m.group(2) in (canon, dup) or k in seene: continue
        seene.add(k); edg.append(ln.rstrip())
    gseen, gaps = set(), []
    for ln in block(cfm, "gaps") + block(dfm, "gaps"):
        t = ln.strip()
        if not t.startswith("- ") or t in gseen: continue
        gseen.add(t); gaps.append("  " + t)
    gaps.append(f'  - "**دُمج {dup} في هذا الملفّ {TODAY}:** كان العنصران يصفان '
                f'الشيءَ نفسَه تحت بادئتين مختلفتين، فنُقل ما انفرد به {dup} إلى هنا '
                f'وصار إحالةً. نسختُه قبل الدمج في `content/ar/_merged/{dup}.md`."')

    head = strip_blocks(cfm)
    nfm = "\n".join(head)
    nfm += "\nedges:\n" + ("\n".join(edg) if edg else "  []")
    nfm += "\nrelated:\n" + ("\n".join(rel) if rel else "  []")
    nfm += "\ngaps:\n" + "\n".join(gaps)
    newbody = open(bodyfile, encoding="utf-8").read().strip("\n")
    open(P[canon], "w", encoding="utf-8").write("---\n" + nfm + "\n---\n\n" + newbody + "\n")

    # 3) المُحال يصير إحالة
    dhead = [l for l in strip_blocks(dfm)
             if not re.match(r"^(title|en|crumb|redirect_to|status):", l)]
    dtitle = field(dfm, "title") or dup
    dcrumb = field(dfm, "crumb") or ""
    parts = [x.strip() for x in dcrumb.split("←")]
    if parts: parts[-1] = "[إحالة]"
    den = field(dfm, "en") or ""
    dfm2 = "\n".join(dhead)
    dfm2 += f'\ntitle: "{dtitle} — إحالة، انظر {canon}"'
    if den: dfm2 += f'\nen: "{den} — merged, see {canon}"'
    dfm2 += f'\ncrumb: "{" ← ".join(parts)}"'
    dfm2 += f'\nredirect_to: "{canon}"'
    dfm2 += "\nedges:\n  []"
    dfm2 += f'\nrelated:\n- id: "{canon}", title: "{ctitle}", type: "{field(cfm,"type")}"'
    dfm2 += ("\ngaps:\n"
             f'  - "**دُمج في {canon} بتاريخ {TODAY}.** كان هذا الملفُّ والملفُّ القانونيُّ '
             f'يصفان الشيءَ نفسَه تحت بادئتين مختلفتين، فوُحِّدا. نُقل ما انفرد به هذا الملفُّ '
             f'إلى القانوني، وحُفظت نسختُه قبل الدمج في `content/ar/_merged/{dup}.md`."')
    rbody = (f"# {dtitle} — إحالة\n\n"
             f"**دُمج هذا المدخلُ في `{canon}`.** المتنُ الكاملُ والمصادرُ والروابطُ هناك:\n"
             f"[{ctitle}]({canon}).\n\n"
             f"يبقى هذا الملفُّ إحالةً دائمةً كي لا تنكسر الروابطُ القديمةُ إليه.\n")
    open(P[dup], "w", encoding="utf-8").write("---\n" + dfm2 + "\n---\n\n" + rbody)

    # 4) إعادةُ توجيه الإشارات الواردة
    ctype = field(cfm, "type")
    touched = 0
    for f in P.values():
        if os.path.basename(f)[:-3] in (canon, dup): continue
        s = open(f, encoding="utf-8").read(); o = s
        s = re.sub(r'(-\s*id:\s*")' + re.escape(dup) + r'("\s*,\s*title:\s*")[^"]*("\s*,\s*type:\s*")[^"]*(")',
                   lambda m: m.group(1) + canon + m.group(2) + ctitle + m.group(3) + ctype + m.group(4), s)
        s = re.sub(r'(-\s*rel:\s*"[^"]*"\s*,\s*target:\s*")' + re.escape(dup) + r'("\s*,\s*target_type:\s*")[^"]*(")',
                   lambda m: m.group(1) + canon + m.group(2) + ctype + m.group(3), s)
        s = re.sub(r'\]\(' + re.escape(dup) + r'\)', f']({canon})', s)
        if s != o:
            # لا تُكرَّر إشارةٌ صار هدفُها واحداً
            fm2, body2 = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", s, re.S).groups()
            out, seen2 = [], set()
            for ln in fm2.split("\n"):
                m = REL_RE.search(ln)
                if m and ln.strip().startswith("- id:"):
                    if m.group(1) in seen2: continue
                    seen2.add(m.group(1))
                out.append(ln)
            s = "---\n" + "\n".join(out) + "\n---\n" + body2
            open(f, "w", encoding="utf-8").write(s); touched += 1

    print(f"✔ {dup} → {canon}   (أُعيد توجيهُ {touched} ملفاً)")


if __name__ == "__main__":
    main()
