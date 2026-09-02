# Task 5.3
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 6 روابط belongs_to بنص حر، 4 تعارضات title/id، سنة/active_end في 7 ملفات)

## أمر التحقق
python3 scripts/task.py verify spark 5.3 → author 40/40، مصادر 0/40 (خارج نطاق هذا التاسك)

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للمؤلفين الموثقين فعلياً في EXISTING_SLUGS.md/thinkers (تحقق فردي قبل كل كتابة).
- wrk-atlas-of-ai-crawford.md: كيت كراوفورد غير موجودة في الأطلس — سُجّلت في requests-spark.md بلا اختراع slug.
- wrk-bhagavad-gita.md: المؤلف التقليدي "فياسا" غير موجود (thk-vyasatirtha شخص مختلف) — سُجّل طلب slug منفصل.
- بعد preflight: حذفت 6 روابط edges/belongs_to بنص حر عوض اختراع slug مدرسة، صححت 4 تعارضات title↔id في related (بولبي، هايدجر، إريك بيرن، خصومة قراءته)، ووسّعت active_end في 7 ملفات ليطابق سنوات مذكورة فعلاً في المتن (بيانات موجودة أصلاً، مجرد نطاق تاريخي ضيق).
- صححت publication_year لـ wrk-artofwar.md من نص حر إلى -500 (رقم صحيح، القيمة النصية كانت تكسر النمط المطلوب).
- حذفت سطرين gaps كاذبين يزعمان غياب ملف مفكر لواطسون وسابولسكي رغم وجودهما فعلياً (thk-jwatson، thk-robert-sapolsky) — يخالف شرط القبول 5.

## متوقف عنده (لرئيس التحرير)
- طلبات slugs جديدة في requests-spark.md: thk-kate-crawford، thk-vyasa.
- wrk-anti-oedipus-deleuze-guattari.md وwrk-a-thousand-plateaus: نمط author_slug_2 لمؤلفين مشتركين غير موحّد في المخطط الأصلي — استُخدم بشكل استرشادي.

## الملفات
40 ملفاً في content/ar/works/ (wrk-anarchy-state-and-utopia-nozick → wrk-bhagavad-gita، ترتيب أبجدي)
