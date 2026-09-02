# Task 10.4
الحالة: مكتمل
المسار: spark | العملية: disorders+syndromes: السقف الإكلينيكي + العلاقة بالمفهوم الفلسفي المقابل + dsm5tr_code/icd11_code (لـdis- فقط) | الملفات: 30 (23 dis- + 7 syn-)

## الأرقام
"## السقف الإكلينيكي" موجود: 0/30 → 30/30
"## العلاقة بالمفهوم الفلسفي المقابل" موجود: 0/30 → 30/30
ملفات syn-: تُركت بلا dsm5tr_code/icd11_code عمداً (الحقول خاصة بـdis- فقط حسب نص المهمة).

## أمر التحقق
python3 scripts/task.py verify spark 10.4
→
=== تحقق Task 10.4 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **الفصل بين dis- وsyn-**: أول دفعة تخلط النوعين معاً. طُبِّق القسمان (السقف الإكلينيكي + العلاقة الفلسفية) على كليهما، لكن حقلي dsm5tr_code/icd11_code اقتصرا على dis- فقط، تماشياً مع نص Task 10 الحرفي ("وضيف dsm_code وicd_code لكل dis-").
- **متلازمات ثقافية (culture-bound)**: dis-taijin-kyofusho.md، syn-ahfa-arabian.md — وُثِّق طابعها الثقافي المحدد صراحة، وdsm5tr_code/icd11_code تُركا null بسبب موثق في dis-taijin-kyofusho.md (لا كود مستقل رسمي).
- **dis-retts-disorder-historical.md**: متلازمة ريت — أُلغيت كفئة نفسية مستقلة في DSM-5 وICD-11 يصنّفها ضمن الفصل العصبي لا النفسي؛ dsm5tr_code/icd11_code = null مع سبب موثق.
- **syn-akathisia.md**: بالتمييز المتعمد المطلوب — هذه متلازمة عصبية-طبية معروفة رسمياً (آلية دوبامينية موثقة)، لا متلازمة ثقافية مثل syn-ahab-syndrome.md أو syn-ahfa-arabian.md المجاورتين لها في الدفعة؛ التمييز وُضِّح صراحة في السقف الإكلينيكي.
- **dis-unspecified-mental.md**: فئة مظلة عامة (unspecified) لا اضطراب فردي محدد — طُبِّق ما يُعقل دون افتعال كود دقيق واحد لا ينطبق.
- روابط "## العلاقة بالمفهوم الفلسفي المقابل" استخدمت مفاهيم حقيقية موجودة فعلاً (أمثلة: con-mind-body, con-cognitive-decentering, con-schizophrenia, con-loneliness-solitude, con-schizoanalysis-desiring-machines, con-addiction, con-parrhesia-fearless-speech, con-attachment-styles, con-status-anxiety-concept, con-lived-body, con-tabula-rasa, con-fear, con-anxiety-existential, con-sadness, con-taijin-kyofusho-concept, con-will-to-power, con-anatta-non-self-concept, con-body-schema, con-freedom, con-shame-guilt, con-panopticon-surveillance, con-blind-will-to-life) — لا اختراع مفاهيم.
- تصحيحات preflight موجودة سلفاً عبر الدفعة (غير ناتجة عن إضافاتنا لكن أُصلحت لتحقيق صفر مخالفات): عشرات عناوين related غير مطابقة، حذف كتل edges تشير لـ"classification-dsm-5-tr"/"classification-icd-11" (شكل slug غير مقبول)، وحذف/استبدال جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" في عدة ملفات (بينها dis-voyeuristic.md وsyn-acute-anxiety.md اللذان احتاجا تصحيحاً يدوياً أخيراً بعد فحص الدفعة كاملة: عنوان related غير مطابق + جملة قائمة سوداء متبقية في كل منهما).

## متوقف عنده (لرئيس التحرير)
- لا شيء عاجل جديد في هذه الدفعة (لا تكرارات ملفات جديدة اكتُشفت). الفجوات المتبقية (أكواد null بسبب موثق للمتلازمات الثقافية والتشخيصات الملغاة) مسجّلة داخل gaps كل ملف.

## الملفات
content/ar/disorders/dis-retts-disorder-historical.md
content/ar/disorders/dis-rumination.md
content/ar/disorders/dis-schizoaffective.md
content/ar/disorders/dis-schizoid-personality.md
content/ar/disorders/dis-schizophrenia.md
content/ar/disorders/dis-schizophreniform.md
content/ar/disorders/dis-schizotypal-personality.md
content/ar/disorders/dis-sedative-use.md
content/ar/disorders/dis-selective-mutism.md
content/ar/disorders/dis-separation-anxiety.md
content/ar/disorders/dis-social-anxiety-disorder.md
content/ar/disorders/dis-somatic-symptom-disorder.md
content/ar/disorders/dis-specific-learning-disorder.md
content/ar/disorders/dis-specific-phobia.md
content/ar/disorders/dis-stimulant-use.md
content/ar/disorders/dis-substance-induced-anxiety.md
content/ar/disorders/dis-substance-induced-mood.md
content/ar/disorders/dis-taijin-kyofusho.md
content/ar/disorders/dis-tic-disorders.md
content/ar/disorders/dis-tobacco-use.md
content/ar/disorders/dis-trichotillomania.md
content/ar/disorders/dis-unspecified-mental.md
content/ar/disorders/dis-voyeuristic.md
content/ar/syndromes/syn-acute-anxiety.md
content/ar/syndromes/syn-ahab-syndrome.md
content/ar/syndromes/syn-ahfa-arabian.md
content/ar/syndromes/syn-akathisia.md
content/ar/syndromes/syn-alice-in-wonderland.md
content/ar/syndromes/syn-alien-hand.md
content/ar/syndromes/syn-amok.md
