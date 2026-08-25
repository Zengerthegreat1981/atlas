#!/usr/bin/env python3
"""
create_missing_nodes_batch.py
Creates canonical nodes for Nel Noddings, Vladimir Jankelevitch, and The Open Society by Karl Popper.
"""

from pathlib import Path
from atlas_content_generator import write_node

# Thinkers
thinkers = [
    ("thk-nel-noddings", "نيل نودينغز", "Nel Noddings",
     "الأخلاق النسوية وفلسفة التربية ← رواد ← نيل نودينغز",
     "الفيلسوفة والتربوية الأمريكية ورائدة «أخلاق الرعاية» (Ethics of Care) ومؤلفة كتاب «Caring: A Relational Approach to Ethics and Moral Education» (1984).",
     [("أخلاق الرعاية العلائقية", "تأسيس الأخلاق على الاستجابة الوجدانية والالتزام بالرعاية المباشرة للآخرين بدلاً من المبادئ والقوانين الكونية المجردة."),
      ("العلاقة بين الراعي والمرعي (One-Caring & Cared-For)", "تحليل ديناميكية اللقاء الأخلاقي بوصفه مسؤولية متبادلة تغذي كرامة الطرفين."),
      ("الأثر في فلسفة التربية والتعليم", "الدعوة لإعادة هيكلة المدارس لتكون مجتمعات دافئة لتعليم الرعاية والتعاطف.")],
     [("belongs_to", "sch-care-ethics", "مدرسة")], [("que-care-ethics-vs-justice-ethics", "أخلاق الرعاية وأخلاق العدالة", "سؤال توليدي")]),

    ("thk-vladimir-jankelevitch", "فلاديمير جانكليفيتش", "Vladimir Jankélévitch",
     "الفلسفة الأخلاقية والموسيقية الفرنسية ← رواد ← فلاديمير جانكليفيتش",
     "الفيلسوف وعالم الموسيقى الفرنسي، تلميذ برغسون ومؤلف «Le Pardon» (1967) و«La Mort» (1966)، رائد التأمل الأخلاقي الصارم في حدود الغفران والموت والفضيلة.",
     [("فلسفة ما لا يغتفر (L'Imprescriptible)", "الأطروحة الصارمة بأن الجرائم ضد الإنسانية لا تسقط بالتقادم ولا تغتفر في غياب الندم الحقيقي من الجلاد."),
      ("الغموض الأخلاقي واللحظة الآنية", "تحليل الفضائل كحالات باطنية عابرة ودقيقة ترفض الاختزال في المنطق النفعي."),
      ("الأثر في فلسفة الأخلاق المعاصرة", "أثارت أطروحاته سجالاً عميقاً مع جاك دريدا وبول ريكور حول طبيعة المصالحة والذاكرة التاريخية.")],
     [("belongs_to", "sch-phenomenology", "مدرسة")], [("que-can-we-forgive-the-unforgivable", "الغفران المستحيل", "سؤال توليدي")])
]

# Works
works = [
    ("wrk-popper-open-society", "المجتمع المفتوح وأعداؤه", "The Open Society and Its Enemies by Karl Popper",
     "فلسفة السياسة ونظرية المجتمع المفتوح ← أمهات الكتب ← المجتمع المفتوح وأعداؤه",
     "العمل السياسي الكلاسيكي لكارل بوبر في مجلدين (1945)، الذي قدم فيه دفاعاً مستميتاً عن الديمقراطية الليبرالية والمجتمع المفتوح ضد النزعات الشمولية والهندسة الاجتماعية اليوتوبية.",
     [("نقد أفلاطون وهيغل وماركس", "تفكيك الجذور الفلسفية للشمولية عبر نقد النزعة التاريخانية (Historicism) التي تدعي معرفة مسار التاريخ الحتمي."),
      ("الهندسة الاجتماعية الجزئية (Piecemeal Social Engineering)", "الدعوة للإصلاح التدريجي القائم على التجربة والخطأ والتصويب النقدي المستمر لحل مشكلات محددة دون تدمير المجتمع."),
      ("مفارقة التسامح والدفاع عن الحرية", "صياغة المبدأ الشهير بوجوب عدم التسامح مع اللامتسامحين الذين يستخدمون العنف لإلغاء الديمقراطية.")],
     [("belongs_to", "sch-phil-science", "مدرسة")], [("thk-karl-popper", "كارل بوبر", "مفكر"), ("que-tolerance-of-intolerant-popper", "مفارقة التسامح لبوبر", "سؤال توليدي")])
]

for slug, title, en, crumb, lede, sections, edges, related in thinkers:
    write_node("thinkers", slug, {"type": "مفكر", "part": "philosophy", "level": "متقدم", "title": title, "en": en, "crumb": crumb}, lede, sections, edges, related)

for slug, title, en, crumb, lede, sections, edges, related in works:
    write_node("works", slug, {"type": "عمل / كتاب", "part": "philosophy", "level": "متقدم", "title": title, "en": en, "crumb": crumb}, lede, sections, edges, related)

print("Created canonical thinkers and works.")
