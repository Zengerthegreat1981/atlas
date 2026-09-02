# Task 9.11
الحالة: مكتمل
المسار: spark | العملية: techniques: ربط بالمدرسة/المبتكر/الاضطراب/الدراسة + evidence_level | الملفات: 30

## الأرقام
جمل القائمة السوداء: 0 → 0
سقّالة ظاهرة: 0 → 0
evidence_level موجود: 0/30 → 30/30
## المصادر موجود: تقريباً 0/30 → 3/30
مخالفات ظهرت وأُصلحت: 4 (2 title mismatch، 1 YAML مكسور، 1 سنة بعد active_end)

## أمر التحقق
python3 scripts/task.py verify spark 9.11
→
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 3 / 30
فيها الحقل evidence_level: 30 / 30

## قرارات اتخذتها
- tec-penile-vibration-stimulator.md: صُححت title لـ tec-sex-therapy-overview.
- tec-process-experiential-tasks.md: **إصلاح جوهري** — thk-greenberg-lisa كان title خاطئاً "ليزا فيرلي غرينبرغ"، صُحح إلى "ليزلي س. غرينبرغ". اكتُشف خطأ هوية ثانٍ: thk-rice كان يشير خطأً لشخص مختلف تماماً (روبرت رايس، فيلسوف أمريكي) بدل المؤسِّسة الحقيقية لورا نورين رايس (thk-lrice) — صُحح.
- tec-psychodrama.md: أُصلح edges بـtarget="ياكوب مورينو" نص حر → thk-jmoreno، مع تصحيح الاسم لـ"جاكوب مورينو" ليطابق الملف الحقيقي.
- tec-primal-therapy-technique.md: evidence_level = discredited بوضوح — رُفضت من الجمعيات المهنية الكبرى، غياب تكرار تجريبي مستقل.
- tec-recovered-memory-technique.md: evidence_level = discredited (مذكورة صراحة في SPARK.md) — تجارب لوفتس على الذاكرة الزائفة، إقرار APA 1995-1996. عُدِّل active_end من 1995 إلى 1996 ليطابق تاريخ إقرار APA المذكور بالمتن.
- tec-pbsp.md: صُححت title لـ thk-dboyden.
- tec-progressive-counting.md: صُححت title لـ thk-greenwald؛ استُرجع رابطان (thk-greenwald وthk-foa) كانا اعتُبرا خطأً "غير متحقَّق منهما" رغم كونهما معتمدين فعلياً.
- tec-relapse-prevention.md: صُححت title لـ tec-mbrp؛ حُذف رابط dis-schizoaffective غير المبرر نصياً.
- tec-phenomenological-exploration.md: **إصلاح YAML** — نقص سطر `---` إغلاق قبل المتن.
- tec-positive-psychotherapy-peseschkian.md مقابل tec-positive-psychotherapy.md: تحقق كامل — **ملفان مختلفان فعلياً** (نسخة بيسشكيان الألمانية 1977 مقابل نسخة راشد-سليغمان الأمريكية 2006)، لا تكرار. أُضيف قسم يشرح الفرق في كل ملف.
- tec-rebt.md: **إصلاح هوية** — "ألفريد إليس" صُحح إلى "ألبرت إليس" (Albert Ellis) ليطابق thk-ellis.
- كل الروابط تحققت من EXISTING_SLUGS.md أو بقراءة الملف المرتبط فعلياً؛ لا slug مخترع.

## متوقف عنده (لرئيس التحرير)
- تكرار slug مؤكد: thk-greenberg-lisa وthk-lgreenberg لنفس الشخص (ليزلي س. غرينبرغ) — يحتاج قرار دمج بشري.
- ملف br-psychodrama.md (خارج نطاق Task 9) فيه نفس خلل edges بنص حر لمورينو — يُنصح بمعالجته في تاسك branches/ لاحق.
- عدة مؤسسين حقيقيين بلا ملف thk- (أنطون بويسن لـPastoral Counseling، جورج براون لمفهوم Expressed Emotion، روبرت ووبولدينغ لـReality Therapy، مارفن غولدفريد، ستيفان هوفمان): مسجَّلون في requests-spark.md أو gaps.
- ملاحظة: أحد الوكلاء أنشأ تقرير وسطر INDEX إضافي بترقيم غير رسمي ("9.pastoral-pbsp-pcit") لملفات pastoral-counseling/pbsp/pcit — هذا خارج آلية task.py الرسمية لكنه لا يتعارض مع هذا التقرير الرسمي 9.11 (نفس الملفات مُدرجة هنا بالكامل أيضاً).

## الملفات
content/ar/techniques/tec-pastoral-counseling.md
content/ar/techniques/tec-pbsp.md
content/ar/techniques/tec-pcit.md
content/ar/techniques/tec-penile-vibration-stimulator.md
content/ar/techniques/tec-person-centered-core-conditions.md
content/ar/techniques/tec-phenomenological-exploration.md
content/ar/techniques/tec-phototherapy.md
content/ar/techniques/tec-play-therapy-branches.md
content/ar/techniques/tec-poetry-therapy.md
content/ar/techniques/tec-polyvagal-ladder-mapping.md
content/ar/techniques/tec-positive-psychotherapy-peseschkian.md
content/ar/techniques/tec-positive-psychotherapy.md
content/ar/techniques/tec-prep-program.md
content/ar/techniques/tec-prescription-task.md
content/ar/techniques/tec-primal-therapy-technique.md
content/ar/techniques/tec-problem-solving-therapy.md
content/ar/techniques/tec-process-based-cbt.md
content/ar/techniques/tec-process-experiential-tasks.md
content/ar/techniques/tec-process-experiential.md
content/ar/techniques/tec-progressive-counting.md
content/ar/techniques/tec-prolonged-exposure.md
content/ar/techniques/tec-provocative-therapy.md
content/ar/techniques/tec-psychedelic-assisted-therapy.md
content/ar/techniques/tec-psychodrama.md
content/ar/techniques/tec-psychoeducational-family.md
content/ar/techniques/tec-reality-choice-therapy.md
content/ar/techniques/tec-rebt.md
content/ar/techniques/tec-recovered-memory-technique.md
content/ar/techniques/tec-reflecting-teams.md
content/ar/techniques/tec-relapse-prevention.md
