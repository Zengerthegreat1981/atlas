# -*- coding: utf-8 -*-
"""
Phase 7: Tasks 7.1 - 7.10
Complete Bridge Relations (rel-) between Philosophy and Psychology.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os

BASE_DIR = _ATLAS_ROOT

def write_draft(subfolder, slug, frontmatter_dict, body_text):
    out_dir = os.path.join(BASE_DIR, "content", "ar", "drafts", subfolder)
    os.makedirs(out_dir, exist_ok=True)
    lines = ["---"]
    lines.append(f'slug: "{slug}"')
    lines.append('id: "[DRAFT-UNKNOWN]"')
    for k, v in frontmatter_dict.items():
        if k in ["slug", "id"]:
            continue
        if isinstance(v, list):
            if k == "edges":
                lines.append("edges:")
                for edge in v:
                    lines.append(f'  - rel: "{edge.get("rel","belongs_to")}", target: "{edge.get("target","")}", target_type: "{edge.get("target_type","مدرسة")}"')
            elif k == "related":
                lines.append("related:")
                for rel in v:
                    lines.append(f'  - id: "{rel.get("id","")}", title: "{rel.get("title","")}", type: "{rel.get("type","")}"')
            elif k == "gaps":
                lines.append("gaps:")
                for g in v:
                    lines.append(f'  - "{g}"')
            else:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f'  - "{item}"')
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f'{k}: "{v}"')
    lines.append("---")
    lines.append("")
    lines.append(body_text.strip())
    lines.append("")
    
    filepath = os.path.join(out_dir, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(chr(10).join(lines))
    print(f"✅ Generated: {subfolder}/{slug}.md")

# Bridge Relations
write_draft("relations", "rel-kierkegaardianism-nietzscheanism-existential-therapy", {
    "type": "علاقة بين مدرستين",
    "part": "bridge",
    "level": "متقدم",
    "title": "العلاقة بين الكيركغاردية والنيتشوية والعلاج النفسي الوجودي",
    "en": "Relationship between Kierkegaardianism/Nietzscheanism and Existential Psychotherapy",
    "crumb": "الجسر المعرفي ← الفلسفة وعلم النفس ← الكيركغاردية والنيتشوية والعلاج الوجودي",
    "active_start": 1946,
    "active_end": "مستمر",
    "edges": [
        {"rel": "relates_to", "target": "الكيركغاردية (الوجودية المبكرة الدينية)", "target_type": "مدرسة"},
        {"rel": "relates_to", "target": "النيتشوية", "target_type": "مدرسة"},
        {"rel": "relates_to", "target": "sch-existential-therapy", "target_type": "مدرسة"}
    ],
    "related": [
        {"id": "thk-kierkegaard", "title": "سورين كيركغارد", "type": "مفكر"},
        {"id": "thk-nietzsche", "title": "فريدريش نيتشه", "type": "مفكر"},
        {"id": "thk-vfrankl", "title": "فيكتور فرانكل", "type": "مفكر"},
        {"id": "thk-yalom", "title": "إيرفين يالوم", "type": "مفكر"}
    ],
    "gaps": ["صياغة فرانكل لمفهوم 'إرادة المعنى' بديلاً عن 'إرادة القوة' النيتشوية، وتحليل رولو ماي للقلق الكيركغاردي.", "لا يوجد اقتباس مباشر موثوق متاح."]
}, """# العلاقة بين الكيركغاردية والنيتشوية والعلاج النفسي الوجودي

جسر معرفي وسريري استثنائي يربط بين فلسفتي كيركغارد ونيتشه في القرن التاسع عشر ونشأة العلاج النفسي الوجودي واللوغوثيرابيا في القرن العشرين؛ حيث استلهم فيكتور فرانكل ورولو ماي وإيرفين يالوم مفاهيم القلق الوجودي، والشجاعة في مواجهة العدم، ومسؤولية خلق المعنى الفردي.""")

write_draft("relations", "rel-british-empiricism-behaviorism", {
    "type": "علاقة بين مدرستين",
    "part": "bridge",
    "level": "متوسط",
    "title": "العلاقة بين التجريبية البريطانية واللوح الفارغ والمدرسة السلوكية",
    "en": "Relationship between British Empiricism and Behaviorism",
    "crumb": "الجسر المعرفي ← الفلسفة وعلم النفس ← التجريبية والسلوكية",
    "active_start": 1913,
    "active_end": "مستمر",
    "edges": [
        {"rel": "relates_to", "target": "التجريبية البريطانية (كمظلة)", "target_type": "مدرسة"},
        {"rel": "relates_to", "target": "sch-behaviorism", "target_type": "مدرسة"}
    ],
    "related": [
        {"id": "thk-locke", "title": "جون لوك", "type": "مفكر"},
        {"id": "thk-jwatson", "title": "جون ب. واطسون", "type": "مفكر"},
        {"id": "thk-fskinner", "title": "ب. ف. سكينر", "type": "مفكر"}
    ],
    "gaps": ["تأثير مبدأ الترابطية (Associationism) لهيوم ولوك في صياغة الإشراط الكلاسيكي والإجرائي.", "لا يوجد اقتباس مباشر موثوق متاح."]
}, """# العلاقة بين التجريبية البريطانية واللوح الفارغ والمدرسة السلوكية

الجذر الفلسفي الأبوي للمدرسة السلوكية؛ حيث حوّل جون واطسون وب. ف. سكينر مبدأ جون لوك الإبستمولوجي حول «اللوح الفارغ» (Tabula Rasa) ونظرية الترابط الحسي لهيوم إلى برنامج تجريبي فيزيائي صارم يفسر السلوك البشري عبر الإشراط البيئي المكتسب دون افتراضات عقلية فطرية مسبقة.""")

write_draft("relations", "rel-hegelianism-psychoanalysis", {
    "type": "علاقة بين مدرستين",
    "part": "bridge",
    "level": "متقدم",
    "title": "العلاقة بين الديالكتيك الهيغلي والتحليل النفسي",
    "en": "Relationship between Hegelian Dialectics and Psychoanalysis",
    "crumb": "الجسر المعرفي ← الفلسفة وعلم النفس ← الهيغلية والتحليل النفسي",
    "active_start": 1930,
    "active_end": "مستمر",
    "edges": [
        {"rel": "relates_to", "target": "الهيغلية", "target_type": "مدرسة"},
        {"rel": "relates_to", "target": "sch-psychoanalysis", "target_type": "مدرسة"}
    ],
    "related": [
        {"id": "thk-hegel", "title": "هيغل", "type": "مفكر"},
        {"id": "thk-freud", "title": "سيغموند فرويد", "type": "مفكر"},
        {"id": "thk-lacan", "title": "جاك لاكان", "type": "مفكر"}
    ],
    "gaps": ["حلقات ألكسندر كوجيف حول فينومينولوجيا الروح في باريس الثلاثينيات وأثرها على مرحلة المرآة اللاكانية.", "لا يوجد اقتباس مباشر موثوق متاح."]
}, """# العلاقة بين الديالكتيك الهيغلي والتحليل النفسي

العلاقة الفلسفية المعمقة التي أعادت هيكلة التحليل النفسي اللاكاني والفرويدي النقدي؛ حيث وظف جاك لاكان وإريك فروم ومدرسة فرانكفورت جدلية السيد والعبد وصراع الاعتراف الهيغلي لتفسير الرغبة الإنسانية كـ «رغبة في رغبة الآخر»، وتفكيك نشأة الأنا عبر الصدام الجدلي مع الواقع واللغة.""")

write_draft("relations", "rel-poststructuralism-antipsychiatry", {
    "type": "علاقة بين مدرستين",
    "part": "bridge",
    "level": "متقدم",
    "title": "العلاقة بين ما بعد البنيوية وحركة مناهضة الطب النفسي",
    "en": "Relationship between Post-Structuralism and Anti-Psychiatry",
    "crumb": "الجسر المعرفي ← الفلسفة وعلم النفس ← ما بعد البنيوية ومناهضة الطب النفسي",
    "active_start": 1961,
    "active_end": "مستمر",
    "edges": [
        {"rel": "relates_to", "target": "ما بعد البنيوية", "target_type": "مدرسة"},
        {"rel": "relates_to", "target": "sch-antipsychiatry", "target_type": "مدرسة"}
    ],
    "related": [
        {"id": "thk-michel-foucault", "title": "ميشيل فوكو", "type": "مفكر"},
        {"id": "thk-szasz", "title": "توماس ساس", "type": "مفكر"},
        {"id": "thk-rlaing", "title": "ر. د. لينغ", "type": "مفكر"}
    ],
    "gaps": ["صدور كتاب 'تاريخ الجنون' لفوكو و'أسطورة المرض النفسي' لساس في نفس العام (1961).", "لا يوجد اقتباس مباشر موثوق متاح."]
}, """# العلاقة بين ما بعد البنيوية وحركة مناهضة الطب النفسي

التقاطع الفلسفي والإكلينيكي النقدي الذي فكك المؤسسة السيكياترية التقليدية؛ حيث وفرت تحليلات ميشيل فوكو وجيل دولوز حول السلطة والانضباط الأرضية المعرفية لرواد مناهضة الطب النفسي (توماس ساس ورونالد لينغ وديفيد كوبر) لإثبات أن تصنيفات الجنون والشذوذ أدوات سلطوية لضبط الاختلاف وليست مجرد حقائق بيولوجية محايدة.""")

write_draft("relations", "rel-spinozism-affective-neuroscience", {
    "type": "علاقة بين مدرستين",
    "part": "bridge",
    "level": "متقدم",
    "title": "العلاقة بين السبينوزية والعلوم العصبية الوجدانية (داماسيو)",
    "en": "Relationship between Spinozism and Affective Neuroscience (Damasio)",
    "crumb": "الجسر المعرفي ← الفلسفة وعلم النفس ← سبينوزا والعلوم العصبية",
    "active_start": 1994,
    "active_end": "مستمر",
    "edges": [
        {"rel": "relates_to", "target": "السبينوزية", "target_type": "مدرسة"},
        {"rel": "relates_to", "target": "sch-biological-neuro", "target_type": "مدرسة"}
    ],
    "related": [
        {"id": "thk-spinoza", "title": "سبينوزا", "type": "مفكر"},
        {"id": "thk-descartes", "title": "ديكارت", "type": "مفكر"}
    ],
    "gaps": ["كتاب أنطونيو داماسيو 'خطأ ديكارت' (1994) و'البحث عن سبينوزا: الفرح والحزن والدماغ الشاعر' (2003).", "لا يوجد اقتباس مباشر موثوق متاح."]
}, """# العلاقة بين السبينوزية والعلوم العصبية الوجدانية (داماسيو)

الجسر العلمي والفلسفي المعاصر الذي شيده عالم الأعصاب الشهير أنطونيو داماسيو؛ أثبتت فيه العلوم العصبية الحديثة صحة رؤية سبينوزا الأحادية للجسد والعقل ونظريته في «الكوناتوس»؛ مفندة ثنائية ديكارت، ومؤكدة أن العواطف والمشاعر الجسدية هي البوصلة الأساسية لعمليات التفكير العقلاني واتخاذ القرار الإنساني.""")

print("Phase 7 Bridge Relations Completed Successfully!")
