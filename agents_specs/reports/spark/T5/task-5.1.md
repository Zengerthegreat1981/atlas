# Task 5.1
الحالة: مكتمل جزئياً
العملية: works: إضافة author / author_slug / publication_year / original_language | الملفات: 40

## الأرقام
author موجود: قبل 0 → بعد 37/40 (39 لهم مؤلف؛ الفرق راجع لعدّاد grep)
جمل القائمة السوداء: 33 متبقية (خارج نطاق التاسك — تنظيف المتن مهمة Task 3/4)
سقّالة ظاهرة: 0

## أمر التحقق
python3 scripts/task.py verify spark 5.1 → author 37/40، مصادر 0/40 (متوقع، خارج نطاق هذا التاسك)

## قرارات اتخذتها
- wrk-acts-of-meaning.md: تعارض هوية مؤلف حقيقي (العنوان الإنجليزي يطابق كتاب Jerome Bruner 1990، لكن الملف ينسبه لدانيال ستيرن 1995) — لم أكتب author حتى يُحسم، وثّقته في gaps وrequests-spark.md.
- wrk-al-ifsah-fi-al-imama-mufid.md / wrk-al-irshad-juwayni.md / wrk-al-milal-wa-al-nihal-shahrastani.md / wrk-al-tamhid-baqillani.md / wrk-al-shafi-fi-al-imama-murtada.md: مؤلفون تراثيون موثقون لكن بلا ملف مفكر في الأطلس — أضفت author بدون author_slug، وسجّلتهم في requests-spark.md (لا اختراع slug).
- wrk-affect-regulation-mentalization.md: عمل بأربعة مؤلفين، الحقل يدعم واحداً فقط — استخدمت المؤلف الأول (thk-fonagy) وأضفت edges لـ thk-mtarget، وسجّلت Gergely وJurist (بلا slug) في requests-spark.md.
- صحّحت بعد preflight: روابط belongs_to بنص حر بدل slug حقيقي (6 ملفات) — حذفتها بدل اختراع slug مدرسة غير موجود. صحّحت 3 تعارضات title/id في related (روبن شارما، ياكوب بانكسيب، ألاسدير ماكنتاير، الغزالي).

## متوقف عنده (لرئيس التحرير)
- wrk-acts-of-meaning.md: يحتاج قرار تحريري — هل الكتاب الموصوف هو Bruner (1990) أم Stern (1995)؟ المتن الحالي يخلط بينهما.
- طلبات slugs جديدة مسجّلة في requests-spark.md: thk-al-mufid، thk-al-juwayni، thk-shahrastani، thk-sharif-al-murtada، thk-baqillani، thk-gergely، thk-jurist.

## الملفات
40 ملفاً في content/ar/works/ (wrk-12-rules-for-life → wrk-al-tamhid-baqillani، ترتيب أبجدي)
