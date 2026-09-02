# Task 2.6
الحالة: مكتمل
العملية: الملفات المشكوك في وجود أصحابها: توثيق أو حجْر أو gaps دقيقة | الملفات: 6

## الأرقام
جمل القائمة السوداء: قبل 6 → بعد 0
فيها ## المصادر: قبل 0/6 → بعد 6/6
preflight_check مخالفات: قبل غير مشغّل → بعد 0 (بعد تصحيح إشارة "بعد وفاته" لسنة 1985 في thk-sferenczi)

## أمر التحقق
`python3 scripts/task.py verify minimax 2.6` → جمل القائمة السوداء: 0، سقّالة ظاهرة: 0، فيها ## المصادر: 6/6
`python3 scripts/preflight_check.py <6 ملفات>` → ✅ صفر مخالفات آلية

## قرارات اتخذتها
- thk-peter-clough: **موثّق** — Peter Clough، أستاذ علم النفس بجامعة مانشستر متروبوليتان، مطوّر أداة MTQ48 ونموذج 4Cs للصلابة الذهنية (مع Keith Earle وDoug Strycharczyk). أعيدت كتابته بمصادر حقيقية (Huddersfield News، PubMed 2021، AQR International). حُذفت الادعاءات غير القابلة للتحقق (كتاب Developing and Enhancing Teamwork في 2016، مقالات Personality and Individual Differences) لعدم توثيقها.
- thk-sferenczi: **موثّق** — Sándor Ferenczi، محلل نفسي مجري حقيقي جداً الشهرة. صُححت أخطاء واقعية: رئاسة IPA كانت 1918–1919 (لا 1920)، تأسيس الجمعية المجرية 1913 (لا 1908)، وأُضيف السياق الصحيح لتعيينه أستاذاً 1919. أُضيف `## المصادر` (Freud Museum London، PEP-Web، الشبكة الدولية لفيرينتسي).
- thk-mbillig: **موثّق** — Michael Billig، أستاذ العلوم الاجتماعية بجامعة لوفبرا، مؤسس مشارك لعلم النفس الخطابي مع بوتر وإدواردز. أعيدت كتابته بمصادر حقيقية (Wikipedia، Internet Archive، صفحته الشخصية)، مع تصحيح/إضافة أعمال حقيقية (Arguing and Thinking 1987، Banal Nationalism 1995) وحذف ادعاءات مفهومية غير موثقة (الشعبوية اليومية، الذاكرة المنسية).
- thk-pakman: **موثّق** — Marcelo Pakman، طبيب ومعالج نفسي أرجنتيني، شخصية قيادية في العلاج الأسري النسقي (AFTA، ASC). أعيدت كتابته بمصادر حقيقية (EFTA، ASC 2011، Springer)، وصُححت active_start/active_end (كانت 2011–2011 بشكل غير منطقي، أصبحت 1989–مستمر).
- thk-mathew: **غير موجود** — بحث ويب مباشر بالاسم الإنجليزي + IAAP/Journal of Analytical Psychology/Jung and Nazism لم يُظهر أي أثر مستقل لشخص بهذا الدور (مؤرخ يونغي أرشيفي لـIAAP). الملف نفسه كان يحمل تناقضاً بين سيرة واثقة الشكل واعتراف "سيرة محدودة — مذكور في أرشيف IAAP وSAP فقط" في الـgaps (نمط القاعدة 11). طُبّق الحجر: النسخة الأصلية أُرشفت في `agents_specs/quarantine-minimax-archive/thk-mathew.md.archived.2026-08-27`، استُبدل المتن بقالب حجر موحّد، وسُجّل في `agents_specs/quarantine-minimax.md` (القسم 2).
- thk-tbickmore: **موثّق** — Timothy Bickmore، أستاذ علوم حاسوب بجامعة نورث إيسترن، مدير مجموعة Relational Agents، مصطلح "الوكيل العلائقي" مؤكد بمصدره. أعيدت كتابته بمصادر حقيقية (صفحته على Khoury College، Healthcare IT News، relationalagents.com)، وحُذفت الأعمال والمفاهيم غير القابلة للتحقق (Modern ELIZA، Positive Dialogue Therapy، The Relagent Framework 2018).

## متوقف عنده (لرئيس التحرير)
- لا يوجد. الدفعة اكتملت بالكامل بالقرارات الثلاثة المطلوبة (5 توثيق + 1 حجر).

## الملفات
- content/ar/thinkers/thk-peter-clough.md
- content/ar/thinkers/thk-sferenczi.md
- content/ar/thinkers/thk-mbillig.md
- content/ar/thinkers/thk-pakman.md
- content/ar/thinkers/thk-mathew.md
- content/ar/thinkers/thk-tbickmore.md
