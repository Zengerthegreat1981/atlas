"""
يرفع وسمَ 77 دراسةً من العامّ «علم النفس» إلى مجالها الدقيق.

هذه الدراساتُ صُحِّح مسارُها في `fix_wrong_existential_crumbs.py` (كانت موسومةً
«المدرسة الوجودية» خطأً)، وأُعطيت وقتَها وسماً **عامّاً صادقاً** لأنّ تصنيفاً
آلياً بالكلمات الدالّة كان قد أخطأ — أسند «التيسير الاجتماعي» لتريبليت إلى علم
النفس العصبي، و«النمذجة الاجتماعية» إلى علم النفس النمائي — فأُسقِط التصنيفُ
الآليُّ وقتَها بقاعدة «أعمُّ وصادقٌ خيرٌ من أخصَّ وخاطئ».

وهذه الخريطةُ **يدويةٌ لا آلية**: الدراساتُ السبعُ والسبعون كلُّها من متن علم
النفس المعروف (بافلوف، ميلغرام، بياجيه، هارلو، لوفتوس، سبيري وغازانيغا…)،
وتصنيفُ كلٍّ منها إلى حقلها لا يحتاج استنباطاً.

    python3 scripts/refine_generic_study_crumbs.py            # فحص
    python3 scripts/refine_generic_study_crumbs.py --apply
"""
import json, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GENERIC = "علم النفس"

D = {
 "علم النفس الاجتماعي": [
   "stu-asch-conformity","stu-berenda-children-conformity","stu-costanzo-shaw-conformity-age",
   "stu-darley-latane-bystander","stu-good-samaritan-darley-batson","stu-latane-darley-smoke",
   "stu-festinger-cognitive-dissonance","stu-hofling-hospital","stu-milgram-obedience",
   "stu-jones-harris-castro","stu-ross-fundamental-attribution-error","stu-ringelmann-social-loafing",
   "stu-robbers-cave","stu-stanford-prison","stu-tajfel-minimal-group","stu-triplett-social-facilitation",
   "stu-lord-ross-polarization","stu-clark-doll-test","stu-farina-mental-illness-stigma",
   "stu-link-modified-labeling-theory","stu-rosenthal-pygmalion","stu-hawthorne-effect",
   "stu-coleman-adolescent-society"],
 "علم نفس الدافعية": [
   "stu-deci-intrinsic-motivation","stu-lepper-overjustification","stu-dweck-growth-mindset-praise"],
 "علم نفس التعلّم والسلوك": [
   "stu-pavlov-classical-conditioning","stu-skinner-operant-conditioning","stu-thorndike-puzzle-box",
   "stu-bandura-bobo-doll","stu-bandura-vicarious-reinforcement","stu-walters-social-modeling-inhibition",
   "stu-hirotto-seligman-human-helplessness","stu-dweck-learned-helplessness-children"],
 "علم النفس المعرفي والإدراكي": [
   "stu-bartlett-war-of-ghosts","stu-craik-lockhart-levels-processing","stu-ebbinghaus-forgetting-curve",
   "stu-miller-magical-number-seven","stu-peterson-peterson-short-term-memory","stu-sperling-iconic-memory",
   "stu-roediger-mcdermott-drm","stu-loftus-misinformation-effect","stu-loftus-lost-in-mall",
   "stu-loftus-palmer-car-crash","stu-hyman-false-childhood-memories","stu-scoville-milner-patient-hm"],
 "علم النفس العصبي والفيزيولوجي": [
   "stu-broca-tan-localization","stu-hubel-wiesel-visual-cortex","stu-sperry-gazzaniga-split-brain",
   "stu-libet-voluntary-action-readiness","stu-rosenzweig-enriched-environment",
   "stu-bexton-heron-sensory-deprivation","stu-lilly-sensory-deprivation-tank"],
 "علم النفس النمائي": [
   "stu-piaget-conservation","stu-piaget-object-permanence-a-not-b","stu-piaget-three-mountains",
   "stu-wimmer-perner-false-belief","stu-meltzoff-moore-neonatal-imitation",
   "stu-curtiss-genie-isolation-case","stu-bucharest-early-intervention-project",
   "stu-dunedin-longitudinal-study","stu-harvard-adult-development"],
 "نظرية التعلق": [
   "stu-bowlby-forty-four-thieves","stu-harlow-rhesus-monkeys","stu-klaus-kennell-maternal-bonding"],
 "الإيثولوجيا (علم السلوك الحيواني)": ["stu-lorenz-imprinting"],
 "علم نفس الانفعال": ["stu-ekman-original-facial","stu-himba-facial"],
 "علم النفس الفارقي والوراثة السلوكية": [
   "stu-minnesota-twins-reared-apart","stu-terman-gifted-longitudinal"],
 "علم النفس الإيجابي": [
   "stu-peterson-seligman-explanatory-style","stu-werner-kauai-resilience"],
 "الطب النفسي والتشخيص": ["stu-rosenhan-on-being-sane","stu-temerlin-diagnostic-bias-suggestion"],
 "مناهج البحث الظاهراتي": ["stu-descriptive-phenomenological-method-giorgi"],
 "العلاج النفسي الوجودي": ["stu-breitbart-mcp-rct"],
 "علم نفس الصدمة والتعافي": ["stu-meaning-making-model-park"],
}

def find_file(slug):
    base = os.path.join(ROOT, "content", "ar")
    for sub in os.listdir(base):
        p = os.path.join(base, sub, slug + ".md")
        if os.path.exists(p): return p

def main():
    apply = "--apply" in sys.argv
    with open(os.path.join(ROOT, "data.json"), encoding="utf-8") as f:
        d = json.load(f)["nodes"]
    target = {s for s, n in d.items()
              if s.startswith("stu-") and (n.get("crumb") or "").startswith(GENERIC + " ←")}
    flat = {s: lab for lab, xs in D.items() for s in xs}
    dup = [s for s in flat if s not in d]
    if dup: print("!! slugs not in atlas:", dup)
    missing = sorted(target - set(flat))
    extra = sorted(set(flat) - target)
    print(f"دراساتٌ بوسمٍ عامّ: {len(target)}   في الخريطة: {len(flat)}")
    if missing: print(f"لم تُصنَّف بعد ({len(missing)}): {missing}")
    if extra: print(f"في الخريطة ولا تحمل الوسمَ العامّ ({len(extra)}): {extra}")
    n_ok = 0
    for s in sorted(target & set(flat)):
        parts = [p.strip() for p in (d[s].get("crumb") or "").split("←")]
        parts[0] = flat[s]
        newcrumb = " ← ".join(parts)
        n_ok += 1
        print(f"{'APPLY' if apply else 'DRY'}  {s:46} -> {flat[s]}")
        if not apply: continue
        p = find_file(s)
        if not p: continue
        t = open(p, encoding="utf-8").read()
        t = re.sub(r'^crumb: ".*"$', 'crumb: "' + newcrumb + '"', t, count=1, flags=re.M)
        note = ('  - "**دُقِّق مسار التنقّل 2026-09-08:** كان الوسمُ الأول «علم النفس» عامّاً '
                '(وُضع عند تصحيح وسمِ «المدرسة الوجودية» الخاطئ)، ورُفع إلى «' + flat[s] + '» '
                'بخريطةٍ يدوية."')
        t = re.sub(r'^gaps:$', 'gaps:\n' + note, t, count=1, flags=re.M)
        open(p, "w", encoding="utf-8").write(t)
    print(f"\nدُقِّق: {n_ok}")

if __name__ == "__main__":
    main()
