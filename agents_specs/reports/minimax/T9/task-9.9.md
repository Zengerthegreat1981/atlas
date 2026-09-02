# Task 9.9
الحالة: مكتمل
المسار: minimax | العملية: concepts: إعادة بناء related من الصفر مع تبرير كل رابط | الملفات: 30

## الأرقام
edges.belongs_to بنص حر بدل slug: 3 (con-ego-depletion، con-emotional-blackmail، con-emotional-immaturity-parents) → أُصلحت (اثنتان كانتا موثقتين بـgaps بالفعل لكن الرابط نفسه لم يُحذف فعلياً — صُحح)
سنة بعد active_end بلا تفسير: 1 (con-drive-reduction: 1997 بعد active_end=1980) → أُضيفت جملة توضيحية في gaps
سقّالة "## ملاحظة معمارية" متبقية من عمل سابق: 3 ملفات (con-eft-couples-bond-cycle، con-emic-etic، con-empty-chair) → حُذفت (معلومات مكررة عن edges/related موجودة أصلاً)

## أمر التحقق
python3 scripts/task.py verify minimax 9.9
→ جمل القائمة السوداء متبقية: 0 (المستهدف 0) | سقّالة ظاهرة متبقية: 0 (المستهدف 0) | فيها ## المصادر: 0 / 30

## قرارات اتخذتها
- con-drive-reduction.md: صُححت أسماء (كلارك هال)، أُضيف con-habit-strength وthk-nealmiller وthk-jdollard وthk-freud وthk-fskinner. سنة 1997 اللاحقة لـactive_end=1980 وُضح سببها بـgaps (بحث لاحق للنظرية لا جزء منها).
- con-dukkha-suffering.md: متن قالبي بالكامل — رابط واحد فقط (sch-buddhism-early).
- con-dunbars-number.md: edges.belongs_to نص حر — استُبدل بـsch-social-psychology.
- con-dunning-kruger-effect.md: حُذفت 4 روابط غير مبررة، edges.belongs_to نص حر — حُذف، أُبقي sch-social-psychology فقط.
- con-dynamic-couple-family.md: أُعيد بناء related بعشرة روابط (فرويد، لاكان، كلاين، مينوخين، بوين، سلفيني-بالاتزولي، كيرنبرغ...).
- con-dzogchen-great-perfection.md: متن قالبي بالكامل — رابطان فقط (sch-nyingma، br-tibetan-nyingma-dzogchen).
- con-ecology-of-freedom.md: أُضيف con-deep-ecology-naess وthk-arne-naess وthk-engels وsch-ecofeminism.
- con-ecopsychoanalysis.md: edges.belongs_to كان حلقة ذاتية — صُحح لـsch-psychoanalysis.
- con-ecstatic-moment.md: أُضيف br-archetypal.
- con-eft-couples-bond-cycle.md، con-eft-couples-emotion-focused.md، con-eft-couples-stuck-points.md: صُححت عناوين، حُذفت روابط غير مبررة نصياً، حُذف قسم "## ملاحظة معمارية" الزائد من الأول.
- con-ego-depletion.md: صُحح عنوان wrk-willpower-baumeister، edges.belongs_to نص حر — حُذف.
- con-ego-self.md: صُححت عناوين thk-edinger وthk-jung.
- con-eje-transversal.md: صُححت عناوين متعددة.
- con-electra-complex.md: edges.belongs_to نص حر — صُحح لـsch-psychoanalysis.
- con-elimination-of-metaphysics.md: بُني related من الصفر (كارناب، sch-vienna-circle).
- con-emanation-islamic.md: أُضيف sch-ashariyya وابن عربي ومحمد عبده.
- con-emanative-scheme-avicenna.md: متن قالبي — أُعيد كتابته (ابن سينا، sch-islamic-peripatetic).
- con-embodied-cognition.md: صُحح عنوان (لاكوف)، حُذف ميرلو-بونتي (غير مذكور)، أُضيف كلارك وتشالمرز.
- con-embodied-perception-merleau-ponty.md: تقليص related لما يدعمه المتن فعلاً.
- con-emerald-tablet.md: أُضيف ابن سينا وفيتشينو ونيوتن (مذكورون بسنوات).
- con-emergence.md: أُضيف thk-varela، استُبعد thk-thompson (شخص مختلف).
- con-emic-etic.md: أُضيف sch-positive-psychology، حُذف "## ملاحظة معمارية" الزائدة.
- con-emotional-blackmail.md: edges.belongs_to نص حر — حُذف فعلياً (كان موثقاً بـgaps لكن الرابط باقٍ).
- con-emotional-cutoff.md: أُضيف con-multigenerational-transmission (بدل تخمين خاطئ للـslug).
- con-emotional-immaturity-parents.md: edges.belongs_to نص حر — حُذف فعلياً.
- con-emotional-intelligence.md: لا تعديل جوهري.
- con-empty-chair.md: صُححت عناوين، حُذفت "## ملاحظة معمارية" الزائدة.
- con-emunah.md: حُذف con-autonomy-homonomy، أُضيف سعديا جاؤون وموسى بن ميمون وكيركغارد وتيليش.

## متوقف عنده (لرئيس التحرير)
- con-drive-reduction.md: التوضيح المضاف لسنة 1997 يعتمد على تفسير أن active_end يمثل أفول النظرية لا نهاية البحث حولها — قاعدة عامة يُنصح بتوضيحها في المعيار لملفات concepts (مقابل thinkers حيث active_end = وفاة).
- con-eft-couples-bond-cycle.md، con-emic-etic.md، con-empty-chair.md: كانت فيها أقسام "## ملاحظة معمارية" من عمل تحريري سابق غير موثق في أي تقرير — رُصدت فقط بالتحقق الآلي، يُنصح بفحص باقي concepts/ لنفس النمط.

## الملفات
content/ar/concepts/con-drive-reduction.md
content/ar/concepts/con-dukkha-suffering.md
content/ar/concepts/con-dunbars-number.md
content/ar/concepts/con-dunning-kruger-effect.md
content/ar/concepts/con-dynamic-couple-family.md
content/ar/concepts/con-dzogchen-great-perfection.md
content/ar/concepts/con-ecology-of-freedom.md
content/ar/concepts/con-ecopsychoanalysis.md
content/ar/concepts/con-ecstatic-moment.md
content/ar/concepts/con-eft-couples-bond-cycle.md
content/ar/concepts/con-eft-couples-emotion-focused.md
content/ar/concepts/con-eft-couples-stuck-points.md
content/ar/concepts/con-ego-depletion.md
content/ar/concepts/con-ego-self.md
content/ar/concepts/con-eje-transversal.md
content/ar/concepts/con-electra-complex.md
content/ar/concepts/con-elimination-of-metaphysics.md
content/ar/concepts/con-emanation-islamic.md
content/ar/concepts/con-emanative-scheme-avicenna.md
content/ar/concepts/con-embodied-cognition.md
content/ar/concepts/con-embodied-perception-merleau-ponty.md
content/ar/concepts/con-emerald-tablet.md
content/ar/concepts/con-emergence.md
content/ar/concepts/con-emic-etic.md
content/ar/concepts/con-emotional-blackmail.md
content/ar/concepts/con-emotional-cutoff.md
content/ar/concepts/con-emotional-immaturity-parents.md
content/ar/concepts/con-emotional-intelligence.md
content/ar/concepts/con-empty-chair.md
content/ar/concepts/con-emunah.md
