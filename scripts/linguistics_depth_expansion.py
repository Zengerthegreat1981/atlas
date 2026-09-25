#!/usr/bin/env python3
"""
Linguistics Depth Expansion - Phase 2 (Batch Processing)
Expands linguistics nodes from ~242 words average to 1,200-1,600 words per node
"""

import json
import os
import sys
from pathlib import Path
import re
from typing import Dict, List, Tuple

# Batch content templates with real linguistic content
BATCH_EXPANSIONS = {
    'Batch 1: Phonology & Phonetics': {
        'phoneme': """## التعريف والخلفية التاريخية

الفونيم هو أصغر وحدة صوتية في اللغة تغيّر المعنى عند تبديلها. طوّره نيكولاي تروبتسكوي ورومان ياكوبسون في حلقة براغ اللسانية (1926+)، محدّثين قطيعة بين الفونيتيكا (الصوتيات الفيزيائية) والفونولوجيا (دراسة الوظائف الصوتية).

### التطور التاريخي

في البدايات، كان المصطلح مستخدماً بشكل غير منتظم في الدراسات اللسانية المبكرة. لكن تروبتسكوي أضفى عليه صرامة منهجية عبر كتابه الأساسي "Principles of Phonology" (1939). رأى تروبتسكوي أن الأصوات ليست مجرد حقائق فيزيائية، بل وحدات وظيفية داخل نسق لغوي معين. ياكوبسون طوّر هذا الفكر لاحقاً بإدخال السمات التمييزية (Distinctive Features)، مما جعل الفونيم قابلاً للتحليل إلى مكونات أصغر.

## الأسس النظرية

يستند مفهوم الفونيم على افتراضات عديدة:

### 1. الدالة التواصلية
كل لغة لديها مجموعة محدودة من الأصوات المميزة وظيفياً. هذه الأصوات ليست عشوائية بل منتقاة من الإمكانيات الفسيولوجية البشرية الشاملة.

### 2. التمييز الثنائي
يتم التعرّف على الفونيمات عبر أزواج التقابل الأدنى (Minimal Pairs). مثال عربي: "باب" و"تاب" يختلفان فقط في الصوت الأول (/ب/ مقابل /ت/)، مما يثبت أنهما فونيمان متمايزان.

### 3. الألوفونات
التنويعات النطقية لفونيم واحد التي لا تغيّر المعنى تُسمّى ألوفونات. مثلاً، القاف القاهرية قد تُنطق مختلفة عن القاف الخليجية، لكن كلاهما يمثل الفونيم /ق/ في العربية.

## الآليات والعمليات الأساسية

### تحديد الفونيمات المنهجي

تُتبع خطوات منهجية:
1. **جمع الكلمات المتناقضة**: البحث عن كلمات تختلف في صوت واحد فقط
2. **تحليل النطق**: تسجيل وتحليل الفروق الفيزيائية
3. **اختبار الوظيفة**: التحقق من أن الاختلاف يؤثر على المعنى
4. **التصنيف**: تجميع الأصوات في فونيمات حسب الوظيفة

### التوزيع المتكامل (Complementary Distribution)

عندما يظهر صوتان دائماً في سياقات مختلفة ولا يغيّران المعنى، يعتبران ألوفونات لفونيم واحد. مثلاً، /p/ في الإنجليزية له نطقان: مرقق (aspirated) وغير مرقق، حسب موضعه في الكلمة (pit vs. spit).

## الأدلة التجريبية

### دراسات الإدراك السمعي

أظهرت دراسات Lisker & Abramson (1964) أن المستمعين يدركون الفروقات الصوتية بطريقة قاطعة (categorical perception)، وليس بشكل متدرج. هذا يدعم فكرة الفونيم كوحدة منفصلة عن التنويعات المستمرة.

### دراسات العصبية المتعلقة

استخدمت fMRI و EEG لإظهار أن الدماغ يعالج الفونيمات المختلفة بنشاطات عصبية متمايزة، حتى عندما تكون الاختلافات الفيزيائية دقيقة جداً.

## التفاصيل الصوتية والنطقية

### الصفات الفسيولوجية

يُصنّف الفونيم حسب خصائصه:
- **نقطة النطق** (Articulation Point): الشفاه، الأسنان، اللثة، الحنك، إلخ
- **طريقة النطق** (Manner): انفجاري، احتكاكي، أنفي، إلخ
- **الأصوات المجهورة/المهموسة** (Voicing): اهتزاز الأحبال الصوتية أم لا
- **الأنفية** (Nasality): مرور الهواء من الأنف أم لا

### خصائص صوتية متقدمة

في العربية، المجموعة الفونيمية تشمل:
- الأصوات الانفجارية: /ب، ت، ج، د، ك، ق/
- الاحتكاكية: /ف، ث، ح، خ، س، ش، ص، ض، ز، ظ، غ/
- الأنفية: /م، ن/
- الجانبية: /ل/
- الرنينية: /ر، ي (كنصف متحرك)، و (كنصف متحرك)/

## التطبيقات المعاصرة

### في تعليم اللغات الأجنبية

فهم الفونيمات يساعد المتعلمين على النطق الصحيح. عندما يتعلم العربي الإنجليزية، يجب أن يدرك أن /p/ و/b/ فونيمان منفصلان (pit vs. bit)، بينما قد لا يميز بسهولة بين /ɪ/ و/i:/ (bit vs. beat).

### في معالجة الكلام الآلية

تُعتمد الفونيمات كوحدات أساسية في تحويل النص إلى كلام (TTS) والتعرّف على الكلام (ASR). نماذج الكلام الحديثة تستخدم تمثيلات فونيمية كمرحلة وسيطة.

### في الترميز والضغط الرقمي

صيغ الضغط الصوتي مثل MP3 تُستفيد من فهم الفونيمات لحذف المعلومات غير الضرورية بدون تأثير على المعنى.

## القيود والاتجاهات البحثية المستقبلية

### النقاد والقيود

1. **التعريف الدائري**: بعض الانتقادات ترى أن تعريف الفونيم قد يكون دائرياً (الفونيم هو ما يميّز المعنى، والمعنى يُحدّد الفونيم).

2. **اللغات المعقدة**: في بعض اللغات مثل الماندرين، يصعب فصل الفونيمات عن التنويعات النبرية، مما يثير أسئلة حول عالمية المفهوم.

3. **اللهجات والمتغيرات**: الفونيمات قد تختلف بين اللهجات، مما يجعل وضع نموذج موحد صعباً.

### الاتجاهات المستقبلية

- **البحث العصبي المتطور**: استخدام fMRI و fNIRS عالية الدقة لفهم كيف يشفّر الدماغ الفونيمات
- **الدراسات متعددة اللغات**: فهم كيف تختلف الأنظمة الفونيمية عبر اللغات
- **النماذج الحاسوبية**: تطوير نماذج عصبية قادرة على تعلم الفونيمات من البيانات الخام

## المصادر الموثوقة

- Trubetzkoy, N. S. (1939/1969). *Principles of Phonology*. University of California Press.
- Jakobson, R., Fant, G., & Halle, M. (1951). *Preliminaries to Speech Analysis*. MIT Press.
- Anderson, S. R. (1985). *Phonology in the Twentieth Century*. University of Chicago Press.
- Ladefoged, P., & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Lisker, L., & Abramson, A. S. (1964). "A cross-language study of voicing in initial stops." *Journal of the Acoustical Society of America*, 20(3), 459-474.""",
    },
    'Batch 2: Semantics & Pragmatics': {
        'implicature': """## التعريف والمفاهيم الأساسية

الاستلزام (Implicature) هو معنى ضمني يُستنتج من الجملة لكن لا يكون جزءاً من المعنى الحرفي الصريح. طوّره بول جرايس (Paul Grice) في نظريته عن المعاني غير الصريحة، مميزاً بينها وبين الاستدلالات المنطقية والافتراضات المسبقة (Presuppositions).

### الخلفية التاريخية

في الستينيات والسبعينيات، كان فهم المعنى في علم اللغة مركزاً على الدلالة الحرفية والافتراضات المنطقية. لكن جرايس لاحظ أن هناك فجوة كبيرة بين ما تقوله الجملة حرفياً وما يقصده المتحدث بالفعل. مثلاً، عندما تقول لشخص "أنت لطيف" في سياق سلبي، قد تعني الضد تماماً. جرايس وضع إطار نظري يشرح هذه الظاهرة.

## الأسس النظرية الجريسية

### مبادئ التعاون (Cooperative Principle)

افترض جرايس أن المحادثة تخضع لمبدأ تعاوني أساسي: كل طرف يتوقع من الآخر أن يساهم بمعلومات صادقة ومفيدة. هذا المبدأ ينقسم إلى أربع قوانين:

#### 1. قانون الكمية (Quantity)
- اجعل مساهمتك بقدر المعلومات المطلوبة
- لا تعطِ معلومات أكثر من اللازم
- لا تعطِ معلومات أقل من اللازم

#### 2. قانون الكيفية (Quality)
- لا تقل ما تعتقد أنه غير صحيح
- لا تقل شيئاً تفتقر إلى أدلة عليه

#### 3. قانون العلاقة (Relevance)
- كن ذا صلة بموضوع الحوار

#### 4. قانون الطريقة (Manner)
- تجنب الغموض
- تجنب اللبس
- كن موجزاً
- كن منظماً

### أنواع الاستلزامات

#### الاستلزام الحرفي (Conventional Implicature)
مرتبط بالكلمات نفسها، بغض النظر عن السياق. مثلاً، "إنه غني، لكنه متواضع" الكلمة "لكن" تستلزم مقابلة أو تعارضاً.

#### الاستلزام المحادثي (Conversational Implicature)
يعتمد على السياق والافتراضات المشتركة بين المتحدثين.

## الآليات والعمليات

### الاستلزام السلمي (Scalar Implicature)

عندما يقول "بعض الطلاب نجحوا"، يستلزم أن ليس كل الطلاب نجحوا. لأن "كل" يكون أقوى من "بعض" على سلم الكمية. إذا كان الكل صحيحاً، كان يجب على المتحدث أن يقوله.

الأمثلة:
- "أكلت بعض الفطائر" ← لم آكل كلها
- "يمكنك استخدام القلم أو القلم الرصاص" ← لا يمكنك استخدام كليهما

### الانحراف عن مبادئ التعاون

عندما يتعارض الكلام مع المبادئ، ينشأ استلزام. مثلاً:
- **انحراف الكمية**: "س: هل أحببت الحفلة؟ ج: كانت الموسيقى جميلة" → (استلزام: الحفلة لم تكن رائعة)
- **انحراف العلاقة**: تعليق بدون صلة يستلزم محاولة الإجابة على ما لم يُسأل

## الأدلة التجريبية والنفسية

### دراسات المعالجة

أظهرت دراسات Noveck & Posada (2003) أن معالجة الاستلزامات السلمية تأخذ وقتاً أطول من معالجة المعاني الحرفية. هذا يشير إلى أن استنتاج الاستلزامات عملية معرفية تتطلب موارد إضافية.

### دراسات فحص العين

استخدم الباحثون eye-tracking لإظهار أن المستمعين ينظرون إلى الكائنات ذات الصلة بالاستلزام بعد قليل من سماع الكلام، قبل أن يكملوا الجملة.

### فحوصات التصوير الدماغي

أظهرت fMRI أن معالجة الاستلزامات تنشط مناطق مختلفة عن معالجة المعنى الحرفي، خاصة المناطق المسؤولة عن نمذجة العقل (Theory of Mind).

## التطبيقات المعاصرة

### معالجة اللغة الطبيعية (NLP)

فهم الاستلزامات ضروري لأنظمة الفهم الآلي. نماذج الذكاء الاصطناعي الحديثة تحاول تعلم هذه المعاني الضمنية من البيانات الضخمة.

### في التعليم والترجمة

معلمو اللغات الأجنبية يجب أن يعلموا الطلاب الاستلزامات الثقافية. الترجمة الآلية تفشل بشكل متكرر في نقل الاستلزامات بدقة.

### في الإعلام والتسويق

الرسائل الإعلانية تستخدم الاستلزامات لإيصال معانٍ بدون قولها صراحة. مثلاً، "تقريباً الجميع يستخدمون منتجنا" تستلزم أنك يجب أن تستخدمه أيضاً.

## القيود والتطورات الحديثة

### النقاد والحدود

1. **الحدود الضبابية**: ليس من الواضح دائماً أين ينتهي الاستلزام ويبدأ الاستنتاج
2. **التباين الثقافي**: الاستلزامات تختلف بشدة بين الثقافات واللغات
3. **العام والخاص**: يصعب فصل الاستلزامات العام (كل لغة) عن الخاصة (لغة واحدة)

### الاتجاهات البحثية

- **دراسات مقارنة بين اللغات**: فهم كيف تختلف الاستلزامات
- **البحث العصبي**: تطبيق تقنيات تصوير دماغي متقدمة
- **النماذج الحاسوبية**: تطوير نماذج شبكات عصبية تتعلم الاستلزامات

## المصادر الموثوقة

- Grice, P. (1975). "Logic and conversation." In *Syntax and Semantics 3*, 41-58. Academic Press.
- Levinson, S. C. (1983). *Pragmatics*. Cambridge University Press.
- Noveck, I. A., & Posada, A. (2003). "Characterizing the time course of an implicature." *Brain and Language*, 85(2), 203-210.
- Huang, Y. (2007). *Pragmatics*. Oxford University Press.
- Sperber, D., & Wilson, D. (1986/1995). *Relevance: Communication and Cognition*. Blackwell.""",
    },
}

def load_nodes_by_batch():
    """Load and categorize linguistics nodes by batch."""
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    nodes = data['nodes']

    batch_keywords = {
        'Batch 1: Phonology & Phonetics': [
            'phonology', 'phonetic', 'autosegmental', 'feature', 'optimality', 'tone',
            'stress', 'intonation', 'prosody', 'articulatory', 'acoustic', 'minimalist',
            'generative phonology', 'laboratory phonology', 'distinctive feature', 'natural class',
            'aspiration', 'palatalization', 'suprasegmental', 'SPE', 'Goldsmith', 'Kager',
            'Johnson', 'Ladefoged', 'phonetic feature', 'segmental process'
        ],
        'Batch 2: Semantics & Pragmatics': [
            'semantic', 'pragmatic', 'formal semantic', 'cognitive semantic', 'truth condition',
            'reference', 'sense', 'implicature', 'presupposition', 'speech act', 'politeness',
            'context', 'metaphor', 'metonymy', 'semantic change', 'Montague', 'Grice',
            'entailment', 'scalar implicature', 'denotation', 'face work', 'turn-taking',
            'repair', 'Frege', 'Russell', 'Carnap', 'Levinson', 'Searle', 'Brown', 'Lakoff',
            'Johnson', 'discourse'
        ],
        'Batch 3: Cognitive & Neurolinguistics': [
            'cognitive', 'neurolinguistic', 'neural', 'garden-path', 'processing', 'bilingual',
            'fMRI', 'EEG', 'MEG', 'TMS', 'PET', 'eye-tracking', 'event-related', 'prediction',
            'semantic integration', 'syntactic parsing', 'working memory', 'neural plasticity',
            'language development', 'aphasia', 'N400', 'P600', 'Broca', 'Wernicke',
            'Friederici', 'Kutas', 'Kuperberg', 'psycholinguistic', 'computational'
        ],
        'Batch 4: Sociolinguistics & Language Variation': [
            'sociolinguistic', 'language variation', 'dialect', 'social stratification',
            'gender', 'class', 'endangered', 'language death', 'revitalization',
            'code-switching', 'diaspora', 'identity', 'multilingual', 'creole', 'pidgin',
            'Labov', 'Eckert', 'Trudgill', 'Fishman', 'Weinreich', 'Myers-Scotton',
            'variationist', 'ethnography', 'prestige', 'stigma', 'accommodation',
            'language shift', 'language maintenance'
        ]
    }

    batches = {}
    for batch, keywords in batch_keywords.items():
        batches[batch] = []
        for sid, node in nodes.items():
            if node.get('part') == 'linguistics' and not (node.get('status') == 'quarantined' or node.get('redirect_to')):
                title = node.get('title', '').lower()
                en_text = node.get('en', '').lower()
                full_text = f"{title} {en_text}".lower()

                if any(kw.lower() in full_text for kw in keywords):
                    batches[batch].append(sid)
                    break

    return batches

def get_file_path(node_id, node):
    """Determine file path for a node."""
    node_type = node.get('type', 'مفهوم').lower()

    # Map Arabic type to English directory
    type_map = {
        'مفهوم': 'concepts',
        'مدرسة': 'schools',
        'مفكر': 'thinkers',
        'عمل': 'works',
        'دراسة': 'studies',
        'عملية': 'processes',
        'تقنية': 'techniques',
    }

    subdir = type_map.get(node_type, 'concepts')
    filename = f"{node_id.lower()}.md"
    return f"content/ar/{subdir}/{filename}"

if __name__ == "__main__":
    batches = load_nodes_by_batch()
    for batch, nodes in batches.items():
        print(f"{batch}: {len(nodes)} nodes")
