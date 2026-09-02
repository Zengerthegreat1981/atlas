# Task 10.7
الحالة: مكتمل
المسار: spark | العملية: syndromes: السقف الإكلينيكي + العلاقة بالمفهوم الفلسفي المقابل (بلا dsm/icd code — كل الملفات syn-) | الملفات: 30

## الأرقام
"## السقف الإكلينيكي" موجود: 0/30 → 30/30
"## العلاقة بالمفهوم الفلسفي المقابل" موجود: 0/30 → 30/30

## أمر التحقق
python3 scripts/task.py verify spark 10.7
→
=== تحقق Task 10.7 (30 ملفاً) ===
جمل القائمة السوداء متبقية: 0 (المستهدف 0)
سقّالة ظاهرة متبقية: 0 (المستهدف 0)
فيها ## المصادر: 0 / 30

python3 scripts/preflight_check.py <30 ملفاً معاً>
→ ✅ 30 ملف — صفر مخالفات آلية.

## قرارات اتخذتها
- **تكرار جديد ثالث مكتشف: syn-hwa-byung.md ↔ dis-hwabyung.md**: نفس الموضوع (متلازمة الغضب المكبوت الكورية Hwa-byung) موزَّع على نوعين مختلفين (dis- من Task 10.4، وsyn- في هذه الدفعة). لم يُحذف أو يُدمج أي ملف؛ اكتمل كل ملف بنفس المعيار، ووُثِّق في gaps كل ملف ملاحظة صريحة تسمّي الملف الآخر بدقة — يحتاج قرار محرر بشري (خاصة قرار توحيد النوع dis- أم syn-).
- **رابع تكرار مكتشف: syn-impostor-syndrome.md ↔ syn-impostor.md**: كلاهما "متلازمة/ظاهرة المحتال" بحقول ومحتوى مختلفين جزئياً (SYN-0195 وSYN-0091). اكتمل كل ملف بمفهوم فلسفي مختلف (con-authenticity وcon-jonah-complex على التوالي) لتفادي تضارب related، ووُثِّق التكرار صراحة في gaps كل ملف.
- مصطلحات شعبية غير رسمية وُضِّحت صراحة: syn-hamlet-syndrome.md (مسرحية شكسبير)، syn-fomo.md (ظاهرة اجتماعية معاصرة لا فئة DSM/ICD).
- متلازمات ثقافية متعددة في هذه الدفعة وُضِّح طابعها المحدد: syn-frigophobia.md (صينية)، syn-ghost-sickness.md (قبائل أمريكية أصلية)، syn-grisi-siknis.md (ميسكيتو، نيكاراغوا/هندوراس)، syn-gururumba.md (بابوا غينيا الجديدة)، syn-havana.md (سياق دبلوماسي كوبي منذ 2016)، syn-hikikomori.md (يابانية)، syn-india-delhi.md.
- syn-holiday-heart.md: حالة قلبية طبية حقيقية موثقة (لا مجازية).
- syn-historical-neurasthenia.md: تصنيف طبي منقرض تفكك في DSM-III — وُضِّح تاريخياً.
- روابط "## العلاقة بالمفهوم الفلسفي المقابل" استخدمت مفاهيم حقيقية موجودة فعلاً (أمثلة: con-the-look-of-the-other-sartre, con-scarcity-mindset, con-narrative-identity, con-social-model-disability, con-identity-of-indiscernibles, con-mind-body, con-bad-faith-mauvaise-foi, con-body-schema, con-will-to-meaning, con-grief, con-language-games-late-wittgenstein, con-hypnotic-trance, con-trauma, con-cultural-unconscious, con-isolation, con-anxiety, con-lived-body, con-repression, con-memory, con-jonah-complex, con-authenticity, con-pleasure, con-ipseity) — لا اختراع مفاهيم.
- تصحيحات preflight موجودة سلفاً عبر الدفعة (غير ناتجة عن إضافاتنا لكن أُصلحت لتحقيق صفر مخالفات): عشرات عناوين related غير مطابقة، حذف/استبدال جملة القائمة السوداء "لا يوجد اقتباس مباشر موثوق متاح" في عدة ملفات.

## متوقف عنده (لرئيس التحرير)
- **syn-hwa-byung.md ↔ dis-hwabyung.md**: تكرار عبر النوعين dis-/syn- لنفس المتلازمة الثقافية — يحتاج قرار محرر بشري.
- **syn-impostor-syndrome.md ↔ syn-impostor.md**: تكرار كامل لنفس الموضوع — يحتاج قرار محرر بشري (دمج أم تمييز نطاق).

## الملفات
content/ar/syndromes/syn-folie-a-deux.md
content/ar/syndromes/syn-fomo.md
content/ar/syndromes/syn-foreign-accent.md
content/ar/syndromes/syn-fragile-x-behavioral.md
content/ar/syndromes/syn-fregoli.md
content/ar/syndromes/syn-frigophobia.md
content/ar/syndromes/syn-ganser.md
content/ar/syndromes/syn-gerstmann.md
content/ar/syndromes/syn-geschwind.md
content/ar/syndromes/syn-ghost-sickness.md
content/ar/syndromes/syn-global-aphasia.md
content/ar/syndromes/syn-grisi-siknis.md
content/ar/syndromes/syn-gulf-war.md
content/ar/syndromes/syn-gururumba.md
content/ar/syndromes/syn-hamlet-syndrome.md
content/ar/syndromes/syn-havana.md
content/ar/syndromes/syn-hikikomori.md
content/ar/syndromes/syn-historical-neurasthenia.md
content/ar/syndromes/syn-holiday-heart.md
content/ar/syndromes/syn-horner.md
content/ar/syndromes/syn-hwa-byung.md
content/ar/syndromes/syn-hyperthymesia.md
content/ar/syndromes/syn-hyperventilation.md
content/ar/syndromes/syn-hypervigilance.md
content/ar/syndromes/syn-hypoactive-sexual-desire.md
content/ar/syndromes/syn-impostor-syndrome.md
content/ar/syndromes/syn-impostor.md
content/ar/syndromes/syn-india-delhi.md
content/ar/syndromes/syn-insomnia.md
content/ar/syndromes/syn-intermetamorphosis.md
