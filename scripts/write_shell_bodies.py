# -*- coding: utf-8 -*-
"""يستبدل جسم ملف مفكر بمحتوى مكتوب، مع إبقاء الـfrontmatter والعنوان والسطر التعريفي كما هي.

يُستدعى ببيانات من ملف JSON: {slug: "نص الأقسام بعد السطر التعريفي"}.
لا يلمس أي ملف جسمه مكتوب فعلاً (يرفض إن لم يجد نص القالب).
"""
import json, os, re, sys
THK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "content", "ar", "thinkers")
TEMPLATE = re.compile(
    r'^## (?:ما أعطاه|ما أعطته|الإسهام الفكري[^\n]*|الأثر الفلسفي[^\n]*'
    r'|الإسهامات والتحولات الفكرية)\n[\s\S]*$', re.M)
data = json.load(open(sys.argv[1], encoding="utf-8"))
apply = "--apply" in sys.argv
ok = bad = 0
for slug, body in data.items():
    p = os.path.join(THK, slug + ".md")
    if not os.path.exists(p): print("MISSING", slug); bad += 1; continue
    t = open(p, encoding="utf-8").read()
    m = re.search(r'^# .*\n\n.*\n', t, re.M)
    tail = t[m.end():]
    # لا يكفي وجود العنوان: لازم الجسم يكون فعلاً نصّاً قالبياً فارغاً،
    # وإلا فالكتابة فوقه تمحو محتوى حقيقياً (حصل فعلاً مع thk-suarez).
    BOILER = ("قدم هذا المفكر مساهمات تأسيسية عميقة", "قدم هذا المفكر إسهامات جوهرية",
              "قدم هذا المفكر إسهامات تأسيسية صاغت معالم المدرسة",
              "تعد أفكاره ومؤلفاته مرجعاً رئيسياً", "إسهامات تأسيسية خالدة في تاريخ الفلسفة",
              "إسهامات نوعية ومؤثرة في مجال", "تعد أعماله مرجعاً رئيسياً لفهم الأسئلة الكبرى",
              "إسهامات رئيسية في مجال", "وصياغة وتعميم مفاهيم إنسانية وعلاجية وتطبيقية")
    if not m or not TEMPLATE.search(tail) or not any(b in tail for b in BOILER):
        print("NOT A BOILERPLATE SHELL (skipped)", slug); bad += 1; continue
    new = t[:m.end()] + "\n" + body.strip() + "\n"
    if apply: open(p, "w", encoding="utf-8").write(new)
    ok += 1
print(f"{'APPLIED' if apply else 'DRY RUN'} — {ok} written, {bad} skipped")
