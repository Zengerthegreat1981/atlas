"""
المرحلة 4 — الإحالاتُ والوصولُ بالتنقّل.

أربعةُ أعمال:

**(1) `redirect_to` لكلِّ إحالة.** كان 38 ملفَّ إحالةٍ بلا حقلٍ يُقرأ آلياً،
فهدفُها مذكورٌ في العنوان أو المتن فقط — أي أنّ أيَّ سكربتٍ أو فحصٍ لا يعرف
إلى أين تُحيل. والتمييزُ المهمُّ هنا بين **الإحالة** (دُمجت، ولها هدف)
و**الحجر** (لم تُوثَّق، ولا هدفَ لها): فالمحجورُ لا يُعطى `redirect_to` لأنّ
لا شيءَ يُحال إليه — ويُوسَم بـ`status: quarantined` ليُقرأ آلياً كذلك.

**(2) وسمُ العنوان.** عشرةُ ملفاتٍ كانت إحالاتٍ مُصرِّحةً في متنها وبعضُها
يحمل `redirect_to` فعلاً، لكنّ **عنوانَها لا يُبيّن ذلك** — فتظهر في الفهارس
والبحث مدخلاً كاملاً يزاحم الملفَّ القانونيّ. وهذا بعينه العيبُ الذي وُصف في
`sch-cbt` قبلاً: «عنوانه كان مطابقاً لعنوان الملف القانوني فيظهر للمستخدم
مدرستان لا يفرّق بينهما شيء».

**(3) روابطُ ماركداون إلى ملفات `.md`.** عشرون عقدةً فيها 26 رابطاً بصيغة
`[نص](slug.md)` — والأطلسُ **لا يفسّر روابطَ الملفات**، فتُطبع حرفيّاً أو
تُكسَر (وهو ما نصَّ عليه تعليلُ إصلاح `sch-cbt`). فحُوِّلت إلى صيغة الأطلس:
الـslug بين علامتَي اقتباسٍ مائلة.

**(4) الوصولُ بالتنقّل.** أمران: إعادةُ توجيهِ كلِّ إشارةٍ حيّةٍ تنتهي إلى
إحالة (63 رابطاً و3 أضلاع) إلى الهدف النهائيّ — بتتبُّعِ سلسلةِ الإحالات حتى
ملفٍّ قائم؛ وإصلاحُ `scripts/template/data_extras.json` الذي يشير إلى
`thk-buber` ولا ملفَّ له (والموجودُ `thk-mbuber`) وإلى إحالتين.
"""
import os, sys, json, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_edit as E

# إحالاتٌ لها هدفٌ مؤكَّد (رُوجعت واحدةً واحدة)
REDIRECT_TO = {
    "axm-existence-precedes-essence": "axi-existence-precedes-essence-axiom",
    "axm-tabula-rasa": "axi-tabula-rasa-rule",
    "br-irfan-shuhudi-sirhindi": "sch-wahdat-alshuhud",
    "br-logical-positivism-vienna-circle": "sch-vienna-circle",
    "br-transpersonal-psychology": "sch-transpersonal",
    "con-archetypes": "con-archetype",
    "con-coloniality-of-power-quijano": "con-coloniality-of-power-concept",
    "con-cosmopolitanism-world-citizen": "con-cosmopolitanism",
    "con-epoché-phenomenological-reduction": "con-epoche-phenomenological-reduction",
    "con-sense-and-reference-frege": "con-sense-vs-reference",
    "dis-borderline-personality": "dis-bpd",
    "dis-major-depressive": "dis-mdd",
    "rel-cbt-mindfulness": "rel-mbct-cbt",
    "rel-cbt-psychodynamic": "rel-psychoanalysis-cbt",
    "rel-cognitive-revolution": "rel-behaviorism-cognitive",
    "rel-emdr-trauma": "rel-trauma-ptsd-therapy",
    "rel-existential-phenomenology": "rel-phenomenology-existential-therapy",
    "rel-gestalt-existential": "rel-humanistic-existential-gestalt",
    "rel-positive-humanistic": "rel-humanistic-positive",
    "rel-poststructuralism-antipsychiatry": "rel-post-structuralism-antipsychiatry",
    "rel-somatic-trauma": "rel-trauma-somatic",
    "rel-spinozism-affective-neuroscience": "rel-spinoza-affect-neurobiology",
    "sch-cbt": "sch-cognitive-behavioral",
    "syn-hwa-byung": "dis-hwabyung",
    "syn-impostor": "syn-impostor-syndrome",
    "syn-taijin-kyofusho": "dis-taijin-kyofusho",
    "thk-edward-de-bono": "thk-de-bono",
    "thk-jkabat": "thk-jkabat-zinn",
    "thk-jonathanbaylin": "thk-jbaylin",
    "thk-kmithoefer": "thk-amithoefer",
    "thk-meillassoux": "thk-quentin-meillassoux",
    "thk-mwhitehouse": "thk-mary-whitehouse",
    "thk-pdeegan": "thk-patdeegan",
    "thk-pkuhn": "thk-thomas-kuhn",
    "thk-richard-thaler": "thk-rkthaler",
    "thk-rick-doblin": "thk-rmdoblin",
    "thk-rwilliams": "thk-rames",
    "trm-wille-zur-macht-nietzsche": "con-will-to-power",
}

# محجورةٌ بلا هدف: لا `redirect_to` — بل وسمُ حالة
QUARANTINE = ["thk-kathylaurenceau", "thk-lbarrett", "thk-mwagreich", "thk-ptedeschi",
              "thk-rcabrera", "thk-sdesha", "thk-twsalisbury", "met-frankl-statue-in-stone",
              "que-mind-body-interaction", "thk-mgrof"]

# عناوينُ إحالاتٍ غيرِ موسومة
MARK_TITLE = ["thk-mwhitehouse", "thk-pdeegan", "trm-archetype", "trm-tabula-rasa-locke",
              "trm-ubertragung-transference", "trm-verdrangung-repression",
              "wrk-being-and-nothingness-sartre", "wrk-being-nothingness",
              "wrk-merleau-ponty-phenomenology-perception",
              "wrk-the-structure-of-scientific-revolutions-kuhn"]

EXTRAS = os.path.join(E.ROOT, "scripts", "template", "data_extras.json")
EXTRAS_FIX = {"thk-buber": "thk-mbuber", "thk-rick-doblin": "thk-rmdoblin",
              "thk-rcabrera": None}  # None = يُترك ويُبلَّغ


def main():
    d = json.load(open(os.path.join(E.ROOT, "data.json"), encoding="utf-8"))["nodes"]
    c = collections.Counter()

    # (1) redirect_to
    for s, tgt in REDIRECT_TO.items():
        if tgt not in d:
            print("  ⚠️  هدفٌ غيرُ موجود:", s, "→", tgt); continue
        if d[s].get("redirect_to") == tgt:
            continue
        p, t = E.load(s)
        t2 = E.set_field(t, "redirect_to", tgt)
        if t2 is None:
            continue
        t2 = E.add_gap(t2, f"**أُضيف `redirect_to` 2026-09-10:** كان هدفُ هذه الإحالة مذكوراً في "
                           f"العنوان أو المتن فقط، فلا يقرأه أيُّ سكربتٍ أو فحص. وأُثبت الحقلُ "
                           f"صراحةً نحو `{tgt}`.") or t2
        E.save(p, t2); c["redirect_to"] += 1

    # وسمُ الحجر
    for s in QUARANTINE:
        if s not in d or d[s].get("status") == "quarantined":
            continue
        p, t = E.load(s)
        t2 = E.set_field(t, "status", "quarantined")
        if t2 is None:
            continue
        t2 = E.add_gap(t2, "**وُسم بالحجر 2026-09-10:** هذا الملفُّ **محجورٌ لا مُحال**: لم يُوثَّق "
                           "مضمونُه ولا يوجد ملفٌّ يُحال إليه، فلا يصحُّ إعطاؤه `redirect_to`. "
                           "وأُضيف `status: quarantined` ليُقرأ الفرقُ آلياً بين الإحالة والحجر.") or t2
        E.save(p, t2); c["quarantine"] += 1

    # (2) وسمُ العنوان
    for s in MARK_TITLE:
        tgt = REDIRECT_TO.get(s) or d[s].get("redirect_to")
        t0 = d[s].get("title") or ""
        if "إحالة" in t0 or "حجر" in t0:
            continue
        p, t = E.load(s)
        t2 = E.set_field(t, "title", f"{t0} — إحالة، انظر {tgt}")
        if t2 is None:
            continue
        t2 = E.add_gap(t2, f"**وُسم العنوان 2026-09-10:** كان هذا الملفُّ إحالةً مُصرِّحةً في متنه إلى "
                           f"`{tgt}`، لكنّ عنوانَه لا يُبيّن ذلك — فيظهر في الفهارس والبحث مدخلاً "
                           f"كاملاً يزاحم الملفَّ القانونيَّ بعنوانٍ يكاد يطابقه. وهو العيبُ نفسُه "
                           f"الذي أُصلح في `sch-cbt` قبلاً.") or t2
        E.save(p, t2); c["title"] += 1

    # (3) روابطُ ماركداون إلى ملفات .md
    for path in E.all_files():
        t0 = open(path, encoding="utf-8").read()
        t = re.sub(r'\[([^\]]*)\]\(([a-zA-Z0-9\-_éÉ]+)\.md\)', lambda m: f'`{m.group(2)}`', t0)
        if t != t0:
            open(path, "w", encoding="utf-8").write(t); c["mdlink"] += 1

    # (4) إعادةُ التوجيه إلى الهدف النهائيّ (بتتبُّع السلسلة)
    def final(s, seen=None):
        seen = seen or set()
        while True:
            tgt = REDIRECT_TO.get(s) or d.get(s, {}).get("redirect_to")
            if not tgt or tgt not in d or tgt in seen:
                return s
            seen.add(s); s = tgt

    red = {s for s in d if (d[s].get("redirect_to") or s in REDIRECT_TO
                            or "إحالة" in (d[s].get("title") or "") or "حجر" in (d[s].get("title") or ""))}
    for path in E.all_files():
        me = os.path.basename(path)[:-3]
        if me in red:
            continue
        t0 = open(path, encoding="utf-8").read()
        t = t0
        for r in sorted(red):
            if r not in t:
                continue
            f = final(r)
            if f == r or f not in d:
                continue
            ft = (d[f].get("title") or "").replace('"', "'")
            t = re.sub(r'-\s*id:\s*"' + re.escape(r) + r'"\s*,\s*title:\s*"[^"]*"\s*,\s*type:\s*"[^"]*"',
                       f'- id: "{f}", title: "{ft}", type: "{d[f]["type"]}"', t)
            t = re.sub(r'(rel:\s*"[^"]*"\s*,\s*)target:\s*"' + re.escape(r) + r'"(\s*,\s*)target_type:\s*"[^"]*"',
                       lambda m: f'{m.group(1)}target: "{f}"{m.group(2)}target_type: "{d[f]["type"]}"', t)
        if t != t0:
            # إزالةُ التكرار والإشارةِ الذاتية الناتجَين
            m = re.search(r'^related:\n((?:- .*\n)*)', t, re.M)
            if m:
                seen, out = set(), []
                for ln in m.group(1).rstrip("\n").split("\n"):
                    i = re.search(r'id:\s*"([^"]*)"', ln)
                    if not i or i.group(1) == me or i.group(1) in seen:
                        continue
                    seen.add(i.group(1)); out.append(ln)
                t = t[:m.start()] + ("related:\n" + "\n".join(out) + "\n" if out else "related: []\n") + t[m.end():]
            open(path, "w", encoding="utf-8").write(t); c["repoint"] += 1

    # data_extras.json
    ex0 = open(EXTRAS, encoding="utf-8").read()
    ex = ex0
    for old, new in EXTRAS_FIX.items():
        if new and f'"{old}"' in ex:
            ex = ex.replace(f'"{old}"', f'"{new}"'); c["extras"] += 1
    if ex != ex0:
        open(EXTRAS, "w", encoding="utf-8").write(ex)
    left = [s for s in EXTRAS_FIX if EXTRAS_FIX[s] is None and f'"{s}"' in ex]
    if left:
        print("  ℹ️  باقٍ في data_extras.json بلا هدفٍ بديل (محجور):", left)

    print("النتيجة:", dict(c))


if __name__ == "__main__":
    main()
