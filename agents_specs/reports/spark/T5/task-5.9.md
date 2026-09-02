# Task 5.9
الحالة: مكتمل
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 40/40
preflight_check: 40/40 → صفر مخالفات (بعد تصحيح 15 رابط edges بنص حر/معطوب، 8 تعارضات title/id، 8 مشاكل سنة/active_end)

## أمر التحقق
python3 scripts/task.py verify spark 5.9 → author 40/40

## قرارات اتخذتها
- 40/40 ملف أُضيف له author؛ author_slug فقط للموثقين فعلياً.
- wrk-insight-lieberman.md: ماثيو ليبرمان مؤلف الكتاب مختلف عن thk-lieberman (أليسيا ليبرمان) — لم يُستخدم الـslug الموجود لتفادي إعادة تدويره، وسُجّل طلب slug صحيح.
- wrk-kashf-al-murad-hilli.md: العلامة الحلي بلا slug — سُجّل في requests-spark.md.
- wrk-kephalaia.md: publication_year: null (نص جماعي مجهول تاريخ التدوين) — صححت صياغة gaps لأنها كانت تكرر حقيقة/تفصيل مؤكد بدل تسمية فجوة (شرط القبول 5).
- wrk-liber-de-causis-pseudo.md: مؤلف مجهول منسوب خطأً لأرسطو — بلا author_slug عمداً.
- wrk-interpersonal-world-infant.md: صحّح authored_by إلى thk-daniel-stern (المفكر الذي استُحدث slug له حديثاً في هذه الدفعة، وحلّ تعارض هويته مع thk-dstern/دونل سترن).
- بعد preflight: حذفت 10 روابط belongs_to بنص حر، صححت 5 روابط authored_by/written_by لـslugs حقيقية، صححت 8 تعارضات title/id، ووسّعت active_end في 8 ملفات.

## متوقف عنده (لرئيس التحرير)
- طلبات slugs جديدة في requests-spark.md: Matthew D. Lieberman، العلامة الحلي.
- wrk-kuzari.md وwrk-kuzari-judah-halevi.md يبدوان ملفين مكررين لنفس الكتاب — يحتاجان دمج، خارج نطاق هذا التاسك.

## الملفات
40 ملفاً في content/ar/works/ (wrk-inquiry-into-good → wrk-liquid-love، ترتيب أبجدي)
