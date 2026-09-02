# Task 17.1 — النوع الجديد `eth-` (وثائق أخلاقية/قانونية معيارية)
الحالة: مكتمل | الملفات: 10

## العملية
هذا نوع محتوى جديد كلياً في الأطلس. ابتُكرت بنية frontmatter متسقة قياساً على `schools/`
(slug/id بادئة ETH-/type: "وثيقة معيارية" أو "مبدأ معياري" أو "سابقة قانونية"/part: "ethics"/
level/title/en/crumb/dates/country/language/register/related/gaps) بمتن من 5 أقسام ثابتة:
السياق والنشأة، البنود/المضمون الأساسي، الأثر على الممارسة الإكلينيكية والبحثية، النقد والقيود، المصادر.

## الملفات (10 من 15-20 المطلوبة في Task 17)
- eth-nuremberg-code — مدونة نورمبرغ (1947)
- eth-helsinki-declaration — إعلان هلسنكي (1964)
- eth-belmont-report — تقرير بلمونت (1979)
- eth-apa-ethics-code — مدونة أخلاقيات APA
- eth-italian-law-180 — القانون الإيطالي 180 / قانون باساليا (1978)
- eth-crpd-2006 — اتفاقية حقوق ذوي الإعاقة (2006)
- eth-informed-consent — الموافقة المستنيرة (مبدأ متطور، لا وثيقة واحدة)
- eth-involuntary-commitment — الإيداع القسري (مبدأ معياري)
- eth-tarasoff-duty-warn — واجب التحذير / قضية تاراسوف (سابقة قانونية)
- eth-confidentiality-limits — حدود السرية العلاجية

## الأرقام
preflight_check.py على العشرة معاً: صفر مخالفات (بعد إعادة ترقيم يدوية — كل الوكلاء العشرة اختاروا
ETH-0001/0002 بشكل مستقل بما أن هذا أول استخدام للنمط في الأطلس؛ أُعيد الترقيم لـETH-0001–0010 فريدة).

## قرارات اتخذتها
- لم تُربط الملفات ببعضها البعض بروابط `eth-` متبادلة أثناء الكتابة المتوازية (كل وكيل لم ير نواتج الآخرين
  وقت كتابته) — سُجّلت الفجوات في `gaps` بدل اختراع روابط. **يحتاج مرور تدقيق لاحق يربط الشبكة بين
  العشرة الآن بعد أن أصبحوا جميعاً موجودين** (مثلاً: eth-helsinki-declaration ← evolved_from ← eth-nuremberg-code،
  eth-tarasoff-duty-warn ← eth-confidentiality-limits، eth-crpd-2006 ← eth-involuntary-commitment).
- eth-italian-law-180 مُيِّز صراحة عن `evt-basaglia-law-italy-1978` الموجود مسبقاً (ذلك يوثق الحدث التاريخي، هذا يوثق مضمون الوثيقة القانونية).

## متوقف عنده (لرئيس التحرير)
- **الشبكة الداخلية بين ملفات eth- العشرة تحتاج مرور ربط لاحق** (راجع أعلاه).
- Task 17 يطلب 15-20 مدخلاً؛ تبقّى: قوانين الصحة النفسية (عام)، حدود إضافية غير مغطاة.
- طلبات `evt-` لـSpark (توسكيغي، ويلوبروك، أكتسيون T4، بينيل، مطرقة الساحرات، بيان واطسون، مقياس بينيه-سيمون، تأسيس شبكة سماع الأصوات، لجنة لانسيت 2018) سُجّلت في `agents_specs/requests-minimax.md`.

## الملفات
content/ar/drafts/minimax/eth/{eth-nuremberg-code,eth-helsinki-declaration,eth-belmont-report,eth-apa-ethics-code,eth-italian-law-180,eth-crpd-2006,eth-informed-consent,eth-involuntary-commitment,eth-tarasoff-duty-warn,eth-confidentiality-limits}.md
