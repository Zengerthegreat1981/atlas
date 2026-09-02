# -*- coding: utf-8 -*-
"""دمج ملفات المفكرين المكرَّرة (نفس الشخص، ملفان).

قابل للتكرار (idempotent) وقابل للعكس: الملف المكرَّر يُنقل إلى
`content/ar/_merged/thinkers/` ولا يُحذف نهائياً. كل عملية تُسجَّل في
`scripts/thinker_merges.json` حتى تُراجَع أو تُعكس.

    python3 scripts/merge_thinker_duplicates.py           # فحص
    python3 scripts/merge_thinker_duplicates.py --apply   # تنفيذ
"""
import json, os, re, sys, glob, shutil

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR     = os.path.join(ROOT, "content", "ar")
THK    = os.path.join(AR, "thinkers")
ARCH   = os.path.join(AR, "_merged", "thinkers")
LEDGER = os.path.join(ROOT, "scripts", "thinker_merges.json")
APPLY  = "--apply" in sys.argv

def read(p):  return open(p, encoding="utf-8").read()
def write(p, t):
    if APPLY: open(p, "w", encoding="utf-8").write(t)

def related_block(fm):
    m = re.search(r'^related:\n((?:\s*- id: ".*\n)*)', fm, re.M)
    return m.group(1) if m else ""

def merge_pair(keep, drop):
    """يضم مدخلات related وgaps من الملف المكرَّر إلى الباقي."""
    kp, dp = os.path.join(THK, keep + ".md"), os.path.join(THK, drop + ".md")
    kt, dt = read(kp), read(dp)
    kfm = kt.split("---", 2)[1]
    dfm = dt.split("---", 2)[1]
    have = set(re.findall(r'- id: "([^"]+)"', kfm))
    extra = [l for l in related_block(dfm).rstrip("\n").split("\n")
             if l.strip() and (m := re.match(r'\s*- id: "([^"]+)"', l))
             and m.group(1) not in have and m.group(1) not in (keep, drop)]
    if extra:
        norm = "\n".join("- " + l.strip()[2:] for l in extra)
        if re.search(r'^related:\n\s*\[\]$', kt, re.M):
            kt = re.sub(r'^related:\n\s*\[\]$', "related:\n" + norm, kt, flags=re.M, count=1)
        else:
            m = re.search(r'^related:\n((?:\s*- id: ".*\n)+)', kt, re.M)
            if m: kt = kt[:m.end(1)] + norm + "\n" + kt[m.end(1):]
            else: kt = kt.replace("\nrelated:\n", "\nrelated:\n" + norm + "\n", 1)
    # ملاحظة أثر الدمج
    tag = f'  - "دُمج معه الملف المكرَّر {drop} (نفس الشخص) — الأصل محفوظ في content/ar/_merged/."'
    if tag not in kt:
        m = re.search(r'^gaps:\n((?:  - ".*"\n)*)', kt, re.M)
        if m: kt = kt[:m.end(1)] + tag + "\n" + kt[m.end(1):]
    return kt, len(extra)

def main():
    plan = json.load(open(sys.argv[sys.argv.index("--plan")+1] if "--plan" in sys.argv
                          else os.path.join(ROOT, "scripts", "thinker_merge_plan.json"), encoding="utf-8"))
    if APPLY: os.makedirs(ARCH, exist_ok=True)
    ledger = json.load(open(LEDGER, encoding="utf-8")) if os.path.exists(LEDGER) else []
    done = {(e["keep"], d) for e in ledger for d in e["drop"]}
    remap, merged, n_rel = {}, [], 0
    for p in plan:
        keep = p["keep"]
        for drop in p["drop"]:
            if (keep, drop) in done or not os.path.exists(os.path.join(THK, drop + ".md")):
                continue
            kt, n = merge_pair(keep, drop)
            write(os.path.join(THK, keep + ".md"), kt)
            remap[drop] = keep; n_rel += n
            merged.append((keep, drop, n))
    if not remap:
        print("لا شيء للدمج — كل الأزواج منفَّذة سلفاً."); return
    # إعادة توجيه كل الروابط الواردة في كل المجلدات (بما فيها drafts)
    touched = 0
    for f in glob.glob(os.path.join(AR, "**", "*.md"), recursive=True):
        if os.sep + "_merged" + os.sep in f: continue
        t = o = read(f)
        for d, k in remap.items():
            t = re.sub(r'(- id: ")%s(")' % re.escape(d), r'\g<1>%s\g<2>' % k, t)
        # إزالة الإحالة الذاتية الناتجة عن إعادة التوجيه
        m = re.search(r'^slug: "(.*)"$', t, re.M)
        if m: t = re.sub(r'^\s*- id: "%s".*\n' % re.escape(m.group(1)), "", t, flags=re.M)
        if t != o:
            write(f, t); touched += 1
    for keep, drop, _ in merged:
        src, dst = os.path.join(THK, drop + ".md"), os.path.join(ARCH, drop + ".md")
        if APPLY: shutil.move(src, dst)
    if APPLY:
        ledger.append({"keep": k, "drop": [d for kk, d, _ in merged if kk == k]}
                      ) if False else None
        byk = {}
        for keep, drop, _ in merged: byk.setdefault(keep, []).append(drop)
        ledger.extend({"keep": k, "drop": v} for k, v in byk.items())
        json.dump(ledger, open(LEDGER, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{'APPLIED' if APPLY else 'DRY RUN'} — دُمج {len(merged)} ملفاً مكرَّراً، "
          f"نُقل {n_rel} مدخل related، وأُعيد توجيه الروابط في {touched} ملفاً.")
    for keep, drop, n in merged: print(f"   {drop:<32} → {keep}  (+{n} related)")

main()
