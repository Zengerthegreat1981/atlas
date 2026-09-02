# Task 5.12
الحالة: مكتمل | العملية: belongs_to — تحويل الأسماء العربية الحرة لـ slugs + بنك المدارس الغائبة (schools/) | الملفات: 40

## الأرقام
مخالفات preflight: 19 → 0
belongs_to/evolved_from/founded_by نصية حرة عولجت: ~20
  - تحويل فعلي لـslug موجود: 5 — sch-dbt (evolved_from→con-biosocial-dbt، founded_by→thk-mlinehan)، sch-eft-couples (evolved_from→br-attachment-theory، founded_by→thk-greenberg-lisa)، sch-feminism-black (evolved_from→sch-postcolonial-philosophy)
  - حُذف الرابط دائري/self-reference: sch-existentialism (belongs_to لنفسها)، sch-critical-realism (سطرين split_into داخليين وهميين)، sch-donghak (فئة عامة دائرية)
  - تسجيل مدارس/مظلات حقيقية بلا ملف: **13 سطراً جديداً** في missing-schools.md (تفاصيل تحت) — أكبر دفعة اكتشاف مظلات حتى الآن
تصحيحات هوية خطيرة (أخطر من عناوين متضاربة عادية):
  - **sch-critical-realism.md:** id `thk-rogers` كان مربوطاً بعنوان "أرثر ك. روجرز" (Arthur Kenyon Rogers، فيلسوف واقعية نقدية 1920) لكن الملف الفعلي وراء الـid هو **كارل روجرز** (Carl Rogers، عالم نفس إنساني) — خلط هوية كامل. حُذف الرابط الخاطئ وسُجّل في gaps بدل الحذف الصامت.
  - **sch-emdr.md:** رابط `thk-francesharville` ("فرانسيس شارفيل") تبيّن أنه نسخة مكررة مغلوطة الاسم لنفس thk-francine-shapiro (فرانسين شابيرو) — حُذف الرابط المكرر.
تصحيحات عناوين related متضاربة: ~15 حالة
إصلاح تاريخ بعد active_end: sch-existentialism-atheist.md (وفاة سيمون دي بوفوار 1986 بعد active_end=1980)

## أمر التحقق
`python3 scripts/task.py verify minimax 5.12` → قائمة سوداء متبقية: **0** · سقّالة ظاهرة: 0 · `## المصادر`: 0/40
`python3 scripts/build_slug_index.py` → 6869 عنصر، 398 تعارض pre-existing (لم ألمسها)

## قرارات اتخذتها
- **sch-critical-realism.md:** خلط هوية thk-rogers (أرثر ك. روجرز الفيلسوف ≠ كارل روجرز المعالج الإنساني المرتبط فعلياً بالـid). حذفت الرابط الخاطئ، وثّقت الاكتشاف في gaps بدل الحذف الصامت — قد يحتاج مراجعة لباقي استخدامات thk-rogers في الأطلس.
- **sch-emdr.md:** thk-francesharville مكرر خاطئ الاسم لـthk-francine-shapiro (نفس الشخص بعنوانين مختلفين) — حُذف الرابط المكرر، أبقيت thk-francine-shapiro الصحيح.
- **13 سطراً جديداً في missing-schools.md** — أبرزها: تقاليد الحكمة القديمة (مصر/الرافدين/العبرية، 3 أعضاء)، الفلسفة السياسية المعاصرة (مظلة، 2 عضو)، الفلسفة الهلنستية (2 عضو)، تقاليد سقراطية-متفرعة (كلبية+قورينائية)، الداووية (فلسفية+دينية)، تقاليد ما قبل سقراط، فلسفات السكان الأصليين لأستراليا/أوقيانوسيا (مستقلة عن أمريكا الشمالية)، الموجة الثالثة من CBT، علم النفس الفيزيولوجي (فونت)، البنائية المعرفية (بياجيه).
- sch-eft.md وsch-eft-couples.md: راجعتهما فعلياً رغم إشارة MINIMAX.md لتطابق حرفي محتمل — **غير متطابقين حرفياً**، محتوى مختلف فعلياً (فردي مقابل زوجي)؛ لم أدمج (قرار Task 8).

## متوقف عنده (لرئيس التحرير)
- **thk-rogers في sch-critical-realism.md:** خلط هوية (أرثر ك. روجرز ↔ كارل روجرز) — يستحق فحص هل نفس الـid مستخدم غلط في ملفات تانية بالأطلس.
- **thk-francesharville:** رابط مكرر خاطئ لنفس thk-francine-shapiro — يستحق فحص باقي الأطلس لوجود استخدامات مماثلة.
- 13 مظلة/مدرسة جديدة في missing-schools.md تنتظر Task 13.
- 398 تعارض slug قديمة، لم تُلمس.

## الملفات
content/ar/schools/sch-cosmopolitanism.md
content/ar/schools/sch-critical-realism.md
content/ar/schools/sch-cynicism.md
content/ar/schools/sch-cyrenaic.md
content/ar/schools/sch-daoism-philosophical.md
content/ar/schools/sch-daoism-religious.md
content/ar/schools/sch-dbt.md
content/ar/schools/sch-decolonial-latin.md
content/ar/schools/sch-decolonial-philosophy.md
content/ar/schools/sch-deconstruction.md
content/ar/schools/sch-deep-ecology.md
content/ar/schools/sch-deism.md
content/ar/schools/sch-deliberative-democracy.md
content/ar/schools/sch-dependency-theory.md
content/ar/schools/sch-developmental.md
content/ar/schools/sch-dogon.md
content/ar/schools/sch-donghak.md
content/ar/schools/sch-dreamtime.md
content/ar/schools/sch-dvaita-vedanta.md
content/ar/schools/sch-eclecticism.md
content/ar/schools/sch-ecofeminism.md
content/ar/schools/sch-eft-couples.md
content/ar/schools/sch-eft.md
content/ar/schools/sch-egyptian-maat.md
content/ar/schools/sch-eleatic.md
content/ar/schools/sch-emdr.md
content/ar/schools/sch-engaged-buddhism.md
content/ar/schools/sch-enlightenment.md
content/ar/schools/sch-environmental-ethics.md
content/ar/schools/sch-epicureanism.md
content/ar/schools/sch-ethiopian-hataata.md
content/ar/schools/sch-ethnophilosophy.md
content/ar/schools/sch-existential-therapy.md
content/ar/schools/sch-existentialism-atheist.md
content/ar/schools/sch-existentialism-religious.md
content/ar/schools/sch-existentialism.md
content/ar/schools/sch-experimental-philosophy.md
content/ar/schools/sch-faxiang.md
content/ar/schools/sch-feminism-black.md
content/ar/schools/sch-feminism-existential.md
