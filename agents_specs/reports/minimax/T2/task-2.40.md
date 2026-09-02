# Task 2.40
الحالة: مكتمل
العملية: تحقّق وجود (Task 2) على 10 ملفات مشكوك فيها بين thk-m وthk-z | الملفات: 10

## الأرقام
موثّق (أُعيد كتابته/صُحّح): 9 → حُجر: 1

## أمر التحقق
`python3 scripts/preflight_check.py --report agents_specs/reports/minimax/T2/task-2.40.md`
→ أول تشغيل: مخالفتان (gaps تؤكد حقيقة في thk-prasastapada؛ edges.belongs_to بtarget نص حر لا slug في thk-mark-wolynn) — صُححتا. ثاني تشغيل: `✅ 10 ملف — صفر مخالفات آلية`

## قرارات اتخذتها
- thk-rschafer: موثّق. روي شيفر (Roy Schafer، 1922–2018) محلل نفسي أمريكي حقيقي موثق (Sigourney Award، Contemporary Psychoanalysis). صُحح active_end من 2014 (خطأ) إلى 2018 (تاريخ وفاته الفعلي 5 أغسطس 2018)، وحُذفت جملة القائمة السوداء من gaps.
- thk-vatsyayana: موثّق. فاتسيايانا شارح Nyāya-bhāṣya، شخصية كلاسيكية موثقة في تاريخ الفلسفة الهندية. حُذف قسم "اقتباسات مختارة" (كان يحوي جملة القائمة السوداء) وأُعيدت صياغة gaps.
- thk-prasastapada: موثّق. معلّق فايشيشيكا حقيقي (Padārthadharmasaṃgraha). صُححت 4 عناوين related متضاربة مع عناوين الملفات المستهدفة الفعلية (thk-kanada، thk-gotama-kanad، thk-shankara، con-jawhar-fard-atomic-monad).
- thk-maburaiya: موثّق بعد تصحيح هوية جوهري. الشخص الحقيقي هو **هشام أبو ريا** (Hisham Abu-Raiya، أستاذ في جامعة تل أبيب، دكتوراه Bowling Green State 2008)، وليس "محمد محمود أبو ريا" كما كتب الملف الأصلي. أعيد كتابة الملف بالكامل: الاسم، الجامعة، أداة القياس الصحيحة (PMIR لا "IRMA")، وحُذفت ادّعاءات موسوعتين محررتين غير موثقتين.
- thk-mark-wolynn: موثّق. مؤلف "It Didn't Start with You" (2016)، شخصية شعبية معاصرة موثقة بكتابها الأكثر مبيعاً. حُذفت جملة القائمة السوداء وصُححت 3 عناوين related.
- thk-sojourner-truth: موثّق. شخصية تاريخية مركزية موثقة. صُححت 3 أخطاء وقائعية: (1) خلط مؤتمر سينيكا فولز (نيويورك 1848) بمؤتمر أوهايو في أكرون (حيث أُلقي خطاب "ألستُ امرأة؟" فعلياً، مايو 1851)، (2) لقاء مختلق مع "الرئيس جون تايلر 1844" استُبدل باللقاء الموثّق مع أبراهام لينكولن (29 أكتوبر 1864)، (3) جملة غامضة عن "مؤتمر نسوي ماكليسفيل" غير قابلة للتحقق استُبدلت بانضمامها الموثق لجماعة نورثهامبتون 1843. حُذف edge بrel="developed" وtarget نص حر غير slug، وصُحح عنوان related متضارب (thk-crenshaw).
- thk-vachaspati-misra: موثّق. منظّم أدفايتا فيدانتا الكلاسيكي، شخصية موثقة أكاديمياً. لا تعديلات مطلوبة (عناوين related كلها مطابقة، لا جملة قائمة سوداء حرفية).
- thk-sdesha: **حُجر**. المتن يصف Kamlesh D. Patel ("داجي" Daaji، الرئيس الرابع لبعثة شري رام تشاندرا ومرشد حركة Heartfulness) — شخص حقيقي موثّق (ويكيبيديا، heartfulness.org) — لكن الـslug "sdesha" لا يطابق اسمه بأي صورة (علامة تحذير القاعدة 6). حُوّل الملف الحي لقالب حجر موحّد، سُجّل في quarantine-minimax.md، وطُلب slug جديد (thk-kamlesh-patel أو thk-daaji) كـR-003 في requests-minimax.md. النسخة الأصلية محفوظة في quarantine-minimax-archive/thk-sdesha.md.archived.2026-08-27.
- thk-mandana-misra: موثّق. جسر ميمامسا-أدفايتا، شخصية كلاسيكية موثقة أكاديمياً. لا تعديلات مطلوبة (لا جملة قائمة سوداء حرفية، عناوين related مطابقة).
- thk-mstein: موثّق. موراي شتاين، محلل يونغي بارز وصاحب "Jung's Map of the Soul" (1998)، موثق أكاديمياً. حُذفت جملة القائمة السوداء من gaps وحُذف قسم "اقتباسات مختارة".

## متوقف عنده (لرئيس التحرير)
- thk-sdesha: يحتاج قرار slug جديد نهائي (thk-kamlesh-patel أو thk-daaji) — مسجّل R-003.

## الملفات
content/ar/thinkers/thk-rschafer.md
content/ar/thinkers/thk-vatsyayana.md
content/ar/thinkers/thk-prasastapada.md
content/ar/thinkers/thk-maburaiya.md
content/ar/thinkers/thk-mark-wolynn.md
content/ar/thinkers/thk-sojourner-truth.md
content/ar/thinkers/thk-vachaspati-misra.md
content/ar/thinkers/thk-sdesha.md
content/ar/thinkers/thk-mandana-misra.md
content/ar/thinkers/thk-mstein.md
