# Task 17.2 — مرور ربط شبكة eth- الداخلية
الحالة: مكتمل | لا ملفات جديدة — إصلاح روابط بين الملفات العشرة الموجودة من Task 17.1

## السبب
تقرير 17.1 وثّق صراحة أن الملفات العشرة كُتبت بالتوازي بدون رؤية بعضها البعض، فسجَّلت روابطها المتبادلة كفجوات (gaps) بدل إنشائها. بعد أن أصبحت العشرة جميعاً موجودة، طُبِّقت الروابط المقترحة يدوياً.

## الروابط المضافة (نفَّذت شخصياً، بدون subagents)
- eth-nuremberg-code ↔ eth-helsinki-declaration (`evolved_from`) + ↔ eth-belmont-report
- eth-belmont-report ↔ eth-nuremberg-code + eth-helsinki-declaration
- eth-informed-consent ↔ eth-helsinki-declaration + eth-belmont-report
- eth-tarasoff-duty-warn ↔ eth-confidentiality-limits
- eth-apa-ethics-code (كان `related: []` فارغاً بالكامل) ← رُبط بـeth-tarasoff-duty-warn، eth-confidentiality-limits، eth-nuremberg-code، eth-helsinki-declaration
- eth-crpd-2006 ↔ eth-involuntary-commitment
- eth-involuntary-commitment ↔ eth-crpd-2006 + eth-italian-law-180

كل رابط جديد تحقَّق `type:` فيه من الملف الهدف الفعلي قبل الكتابة (وليس تخميناً) — مثال: صُحِّح نوع eth-italian-law-180 من "سابقة قانونية" (تخمين أولي) إلى "وثيقة معيارية" (النوع الفعلي في frontmatter الملف).

## التحقق
- `preflight_check.py` على العشرة معاً: 19 "مخالفة" — تحقَّقت يدوياً بـ`test -f` أن كل ملف مُستهدَف موجود فعلاً؛ كلها من نمط sibling-draft المعروف (مجلد eth/ بالكامل جديد، لم يُرقَّ أي ملف منه بعد لـcontent/ar).
- grep قائمة سوداء مباشر على الملفات العشرة: صفر تطابق.

## متوقف عنده
- Task 17 لا يزال يحتاج 5-10 ملفات إضافية (من 15-20 المطلوبة) — مرشحون معروفون: قوانين صحة نفسية عامة إضافية، وربما ميثاق مدونة أخلاقيات أخرى (BACP، BPS).
