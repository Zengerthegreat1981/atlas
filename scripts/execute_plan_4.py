#!/usr/bin/env python3
"""
execute_plan_4.py
Executes Plan 4: Specialized Psychology Packages (DSM Evolution & Psychometrics)
  - Phase 1: Clinical Integration of DSM Evolution
  - Phase 2: Psychometrics & Instruments (ins-) Cross-linking and Deepening
  - Phase 3: Classical Psychological Studies (stu-) Cross-linking and Deepening
  - Phase 4: Rebuild indexes, matrices, and live Atlas build
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import re
import sys
import json
from pathlib import Path

ATLAS_ROOT = Path(_ATLAS_ROOT)
CONTENT_AR = ATLAS_ROOT / 'content' / 'ar'

RELATED_ITEM_RE = re.compile(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"')

def get_all_slugs():
    slugs = {}
    for root, dirs, files in os.walk(CONTENT_AR):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md') and f != 'EXISTING_SLUGS.md':
                p = Path(root) / f
                txt = p.read_text(encoding='utf-8')
                m = re.search(r'^title:\s*"([^"]*)"', txt, re.M)
                title = m.group(1) if m else f[:-3]
                m_type = re.search(r'^type:\s*"([^"]*)"', txt, re.M)
                ntype = m_type.group(1) if m_type else ''
                slugs[f[:-3]] = {'path': p, 'title': title, 'type': ntype}
    return slugs

def phase_1_dsm_evolution(slug_map):
    print('========================================')
    print('PHASE 1: Clinical Integration of DSM Evolution')
    print('========================================')
    
    notes_map = {
        'dis-depersonalization-derealization': ('التطور التاريخي في DSM', 'كانت هذه الفئة تُسمّى في DSM-IV «اضطراب تبدد الشخصية» (Depersonalization Disorder)؛ وأُعيدت تسميتها في DSM-5 إلى «اضطراب تبدد الشخصية / تبدد الواقع» لإبراز أعراض تبدد الواقع (Derealization) كمعيار تشخيصي صريح متكافئ.'),
        'dis-dissociative-identity': ('التطور التاريخي في DSM', 'اقتُرحت فئة «اضطراب الغيبة الانشقاقية» سابقاً في ملحق أبحاث DSM-IV كتشخيص مستقل، ثم دُمجت مظاهر الغيبة والانخطاف غير الإرادي ضمن طيف الاضطرابات الانشقاقية في DSM-5، بينما خصص لها ICD-11 فئة «اضطراب الغيبة التملكية» (6B63).'),
        'dis-mdd': ('التطور التاريخي في DSM', 'كان DSM-IV يستثني نوبات الاكتئاب التي تعقب وفاة شخص عزيز (استثناء الفجيعة) لمدة شهرين؛ وقد أُلغي هذا الاستثناء في DSM-5 ليتاح تشخيص نوبة الاكتئاب الجسيم بعد الفقد مباشرة إذا استوفت المعايير السريرية الكاملة، مع تمييزها عن اضطراب الفجيعة المطولة.'),
        'dis-gad': ('التطور التاريخي في DSM', 'اقتُرح تشخيص «اضطراب القلق والاكتئاب المختلط» في ملحق أبحاث DSM-IV للحالات التي تجمع أعراض القلق والاكتئاب دون استيفاء عتبة أي منهما كاملاً؛ ورغم عدم اعتماده كاضطراب مستقل في DSM-5، فقد اعتمده ICD-11 رسمياً كفئة تشخيصية مستقلة برمز (6A73).'),
        'dis-arfid': ('التطور التاريخي في DSM', 'كان هذا الاضطراب في DSM-IV مقصوراً على الرضع والأطفال الصغار تحت مسمى اضطراب التغذية؛ وقد استُبدل ووُسِّع نطاقه في DSM-5 ليصبح «اضطراب تجنب/تقييد تناول الطعام» (ARFID) شاملاً كافة المراحل العمرية دون حصر النمط في الطفولة المبكرة.'),
        'dis-adjustment-disorders': ('التطور التاريخي في DSM', 'كانت محددات اضطراب التكيف في DSM-IV تفصل بين التكيف مع قلق، واكتئاب، ومزيج منهما؛ وتم الحفاظ على هذه المحددات في DSM-5 مع تبسيط المعايير السريرية للتمييز عن الاضطرابات المزاجية الصريحة.'),
        'dis-factitious': ('التطور التاريخي في DSM', 'كان يُصنف في ملحق أبحاث DSM-IV باسم «الاضطراب المفتعل بالوكالة»؛ وأُعيدت تسميته وهيكلته في DSM-5 تحت مسمى رسمي هو «الاضطراب المفتعل المفروض على شخص آخر» (Factitious Disorder Imposed on Another) لتمييزه عن إساءة معاملة الأطفال الجنائية.'),
        'dis-fetishistic': ('التطور التاريخي في DSM', 'أُعيدت تسمية «الفيتيشية» (Fetishism) في DSM-5 إلى «اضطراب الفيتيشية» (Fetishistic Disorder)، مع التأكيد الصارم على أن الانجذاب للأشياء غير الحية لا يعد اضطراباً إلا إذا اقترن بضيق نفسي ملحوظ أو ضرر وظيفي واجتماعي.'),
        'dis-voyeuristic': ('التطور التاريخي في DSM', 'أُعيدت تسمية التلصص في DSM-5 إلى «اضطراب التلصصية» (Voyeuristic Disorder) للتفريق بين الاهتمام التلصصي النظري والاضطراب الإكلينيكي المقترن بسلوك فعلي مع أشخاص غير مدركين أو مسبب لضائقة سريرية.'),
        'dis-exhibitionistic': ('التطور التاريخي في DSM', 'أُعيدت تسمية الاستعراضية في DSM-5 إلى «اضطراب الاستعراضية» (Exhibitionistic Disorder)، مع اشتراط كشف العورات لشخص غير راغب أو وجود ضائقة شديدة لمنح التشخيص السريري.'),
        'dis-autism-spectrum': ('التطور التاريخي في DSM', 'كان «الاضطراب النمائي الشامل غير المحدد» (PDD-NOS) ومتلازمة هيلر فئتين شائعتين في DSM-IV للحالات غير النمطية؛ وقد أُلغي استقلالهما في DSM-5 ودُمجا كلياً ضمن «اضطراب طيف التوحد» (ASD) مع تحديد شدة الدعم المطلوبة.'),
        'dis-insomnia-disorder': ('التطور التاريخي في DSM', 'ألغى DSM-5 التقسيم الثنائي القديم لاضطرابات النوم (الأولية مقابل الثانوية الناتجة عن اضطراب نفسي آخر)، واعتمد نموذج المراضة المشتركة (Comorbid Sleep-Wake Disorders) الذي يعالج الأرق كاضطراب سريري مستقل يتطلب تدخلاً نوعياً بذاته.'),
        'dis-nightmare-disorder': ('التطور التاريخي في DSM', 'أُلغيت فئة «الخطل النومي غير المحدد» في DSM-5 لصالح تفصيل نوعي صارم: خطل نوم حركة العين غير السريعة (NREM) مقابل اضطراب سلوك نوم حركة العين السريعة واضطراب الكوابيس.'),
        'dis-alcohol-use-disorder': ('التطور التاريخي في DSM', 'ألغى DSM-5 الفصل الثنائي القديم بين إساءة استخدام الكحول والاعتماد الكحولي، ودُمجت المعايير في متصل تشخيصي موحد هو «اضطراب تعاطي الكحول» (Alcohol Use Disorder - AUD) مع إدراج معيار «التوق الشديد / اللهفة» (Craving).'),
        'dis-cannabis-use': ('التطور التاريخي في DSM', 'كان DSM-IV يفصل بين «إساءة استخدام الحشيش» و«الاعتماد على الحشيش»؛ وقد دمجهما DSM-5 في تشخيص متصل واحد هو «اضطراب تعاطي القنب» (Cannabis Use Disorder - CUD) محدد بدرجات شدة.'),
        'dis-somatic-symptom-disorder': ('التطور التاريخي في DSM', 'دُمجت فئات اضطراب الجسدنة والألم النفسي والجسدنة غير المتمايزة في DSM-5 ضمن تشخيص موحد هو «اضطراب العَرَض الجسدي» (Somatic Symptom Disorder)، مع تحويل التركيز التشخيصي من «غياب التفسير الطبي للعرض» إلى «وجود أفكار ومشاعر وسلوكيات غير متناسبة ومفرطة تجاه العرض».'),
    }
    
    updated_dsm = 0
    for slug, (sec_title, note_text) in notes_map.items():
        if slug in slug_map:
            p = slug_map[slug]['path']
            txt = p.read_text(encoding='utf-8')
            if 'التطور التاريخي في DSM' not in txt and 'DSM-IV' not in txt:
                new_txt = txt.rstrip() + f'\n\n## {sec_title}\n\n{note_text}\n'
                p.write_text(new_txt, encoding='utf-8')
                updated_dsm += 1
                
    # Historical disorder cross-links
    hist_pairs = [
        ('dis-aspergers-disorder-historical', 'dis-autism-spectrum'),
        ('dis-gender-identity-disorder-historical', 'dis-gender-dysphoria'),
        ('dis-retts-disorder-historical', 'dis-autism-spectrum'),
        ('dis-depressive-personality-historical', 'dis-persistent-depressive-disorder'),
        ('dis-passive-aggressive-personality-historical', 'dis-borderline-personality'),
    ]
    for h_slug, mod_slug in hist_pairs:
        if h_slug in slug_map and mod_slug in slug_map:
            for s1, s2 in [(h_slug, mod_slug), (mod_slug, h_slug)]:
                p = slug_map[s1]['path']
                txt = p.read_text(encoding='utf-8')
                target_info = slug_map[s2]
                rel_line = f'  - id: "{s2}", title: "{target_info["title"]}", type: "{target_info["type"]}"'
                if s2 not in txt:
                    if 'related:\n' in txt:
                        new_txt = txt.replace('related:\n', f'related:\n{rel_line}\n', 1)
                    elif 'related:  []' in txt:
                        new_txt = txt.replace('related:  []', f'related:\n{rel_line}', 1)
                    else:
                        new_txt = txt
                    p.write_text(new_txt, encoding='utf-8')
                    
    print(f'Phase 1 Complete: {updated_dsm} disorders enriched with historical DSM notes & bidirectional cross-links verified.')

def phase_2_psychometrics_enrichment(slug_map):
    print('========================================')
    print('PHASE 2: Psychometrics & Instruments (ins-) Deepening')
    print('========================================')
    
    ins_links = {
        'ins-bdi-ii': [('dis-mdd', 'اضطراب الاكتئاب الجسيم', 'اضطراب/حالة إكلينيكية'), ('thk-beck', 'آرون تيموثي بيك', 'مفكر')],
        'ins-phq-9': [('dis-mdd', 'اضطراب الاكتئاب الجسيم', 'اضطراب/حالة إكلينيكية'), ('thk-rspitzer', 'روبرت سبيتزر', 'مفكر')],
        'ins-gad7': [('dis-gad', 'اضطراب القلق العام', 'اضطراب/حالة إكلينيكية'), ('thk-rspitzer', 'روبرت سبيتزر', 'مفكر')],
        'ins-bai': [('dis-panic-disorder', 'اضطراب الهلع', 'اضطراب/حالة إكلينيكية'), ('thk-beck', 'آرون تيموثي بيك', 'مفكر')],
        'ins-y-bocs': [('dis-ocd', 'اضطراب الوسواس القهري', 'اضطراب/حالة إكلينيكية')],
        'ins-oci-r': [('dis-ocd', 'اضطراب الوسواس القهري', 'اضطراب/حالة إكلينيكية'), ('thk-foa', 'إدنا ب. فوا', 'مفكر')],
        'ins-pcl-5': [('dis-ptsd', 'اضطراب ما بعد الصدمة', 'اضطراب/حالة إكلينيكية')],
        'ins-caps-5': [('dis-ptsd', 'اضطراب ما بعد الصدمة', 'اضطراب/حالة إكلينيكية')],
        'ins-ados-2': [('dis-autism-spectrum', 'اضطراب طيف التوحد', 'اضطراب/حالة إكلينيكية')],
        'ins-m-chat-r-autism': [('dis-autism-spectrum', 'اضطراب طيف التوحد', 'اضطراب/حالة إكلينيكية')],
        'ins-aq-autism-spectrum': [('dis-autism-spectrum', 'اضطراب طيف التوحد', 'اضطراب/حالة إكلينيكية')],
        'ins-conners-rating-scales': [('dis-adhd', 'اضطراب فرط الحركة وتشتت الانتباه', 'اضطراب/حالة إكلينيكية')],
        'ins-audit': [('dis-alcohol-use-disorder', 'اضطراب تعاطي الكحول', 'اضطراب/حالة إكلينيكية')],
        'ins-dast': [('dis-cannabis-use', 'اضطراب تعاطي القنب', 'اضطراب/حالة إكلينيكية')],
        'ins-lsas': [('dis-social-anxiety-disorder', 'اضطراب القلق الاجتماعي', 'اضطراب/حالة إكلينيكية')],
        'ins-spin': [('dis-social-anxiety-disorder', 'اضطراب القلق الاجتماعي', 'اضطراب/حالة إكلينيكية')],
        'ins-mmpi': [('sch-cognitive-behavioral', 'العلاج المعرفي السلوكي (CBT)', 'مدرسة')],
        'ins-wais': [('sch-developmental', 'علم النفس التطوري', 'مدرسة')],
        'ins-wisc': [('dis-intellectual-disability', 'الإعاقة الفكرية', 'اضطراب/حالة إكلينيكية')],
        'ins-mbti': [('thk-jung', 'كارل غوستاف يونغ', 'مفكر')],
        'ins-rorschach': [('sch-psychoanalysis', 'التحليل النفسي (Psychoanalysis)', 'مدرسة')],
        'ins-swls': [('thk-ed-diener', 'إد دينر', 'مفكر'), ('sch-positive-psychology', 'علم النفس الإيجابي', 'مدرسة')],
    }
    
    updated_ins = 0
    for ins_slug, targets in ins_links.items():
        if ins_slug in slug_map:
            p = slug_map[ins_slug]['path']
            txt = p.read_text(encoding='utf-8')
            new_lines = []
            for tid, ttitle, ttype in targets:
                if tid in slug_map and tid not in txt:
                    new_lines.append(f'  - id: "{tid}", title: "{ttitle}", type: "{ttype}"')
            if new_lines:
                ins_block = '\n'.join(new_lines)
                if 'related:\n' in txt:
                    new_txt = txt.replace('related:\n', f'related:\n{ins_block}\n', 1)
                elif 'related:  []' in txt:
                    new_txt = txt.replace('related:  []', f'related:\n{ins_block}', 1)
                else:
                    new_txt = txt
                p.write_text(new_txt, encoding='utf-8')
                updated_ins += 1
                
    print(f'Phase 2 Complete: {updated_ins} psychometric instruments enhanced with verified clinical and theoretical links.')

def phase_3_studies_enrichment(slug_map):
    print('========================================')
    print('PHASE 3: Classical Psychological Studies (stu-) Deepening')
    print('========================================')
    
    stu_links = {
        'stu-milgram-obedience': [('thk-stanley-milgram', 'ستانلي ميلغرام', 'مفكر'), ('con-agentic-state-milgram', 'الحالة الوكالية والانصياع للسلطة', 'مفهوم')],
        'stu-asch-conformity': [('thk-sasch', 'سولومون آش', 'مفكر')],
        'stu-stanford-prison': [('thk-philip-zimbardo', 'فيليب زيمباردو', 'مفكر'), ('con-lucifer-effect', 'تأثير لوسيفر والشر المؤسسي', 'مفهوم')],
        'stu-festinger-cognitive-dissonance': [('thk-lfestinger', 'ليون فستنغر', 'مفكر'), ('con-cognitive-dissonance', 'التنافر المعرفي', 'مفهوم')],
        'stu-loftus-palmer-car-crash': [('thk-elizabeth-loftus', 'إليزابيث لوفتوس', 'مفكر'), ('con-misinformation-effect-loftus', 'تأثير التضليل وقابلية الذاكرة للتعديل', 'مفهوم')],
        'stu-loftus-lost-in-mall': [('thk-elizabeth-loftus', 'إليزابيث لوفتوس', 'مفكر')],
        'stu-seligman-maier-learned-helplessness': [('thk-mseligman', 'مارتن سليغمان', 'مفكر'), ('con-learned-helplessness', 'العجز المتعلم', 'مفهوم')],
        'stu-bandura-bobo-doll': [('thk-abandura', 'ألبرت باندورا', 'مفكر'), ('con-modeling', 'النمذجة والتعلم بالملاحظة', 'مفهوم')],
        'stu-pavlov-classical-conditioning': [('thk-ipavlov', 'إيفان بافلوف', 'مفكر'), ('axm-classical-conditioning', 'بديهية الإشراط الكلاسيكي', 'بديهية/مبدأ تأسيسي')],
        'stu-skinner-operant-conditioning': [('thk-fskinner', 'بوريس فريدريك سكينر', 'مفكر'), ('axm-operant-conditioning', 'بديهية الإشراط الإجرائي', 'بديهية/مبدأ تأسيسي')],
        'stu-watson-little-albert': [('thk-jwatson', 'جون ب. واتسون', 'مفكر')],
        'stu-harlow-rhesus-monkeys': [('thk-hharlow', 'هاري هارلو', 'مفكر'), ('sch-developmental', 'علم النفس التطوري', 'مدرسة')],
        'stu-ainsworth-strange-situation': [('thk-mary-ainsworth', 'ماري أينسورث', 'مفكر'), ('sch-developmental', 'علم النفس التطوري', 'مدرسة')],
        'stu-bowlby-forty-four-thieves': [('thk-bowlby', 'جون بولبي', 'مفكر')],
        'stu-mischel-marshmallow-test': [('thk-wmischel', 'والتر ميشيل', 'مفكر'), ('axm-delayed-gratification', 'بديهية تأجيل الإشباع', 'بديهية/مبدأ تأسيسي')],
        'stu-kahneman-tversky-prospect-theory': [('thk-kahneman', 'دانيال كانيمان', 'مفكر'), ('thk-amos-tversky', 'عاموس تفيرسكي', 'مفكر'), ('con-loss-aversion', 'كراهية الخسارة', 'مفهوم')],
        'stu-kahneman-tversky-heuristics-biases': [('thk-kahneman', 'دانيال كانيمان', 'مفكر'), ('con-confirmation-bias', 'انحياز التأكيد', 'مفهوم')],
        'stu-strack-facial-feedback-pen': [('crt-replication-crisis', 'نقد أزمة التكرار في علم النفس', 'نقد خارجي موثَّق'), ('dbt-psychology-replication-crisis', 'أزمة تكرار النتائج في علم النفس التجريبي', 'جدل')],
        'stu-bargh-automaticity-elderly-priming': [('crt-replication-crisis', 'نقد أزمة التكرار في علم النفس', 'نقد خارجي موثَّق'), ('dbt-psychology-replication-crisis', 'أزمة تكرار النتائج في علم النفس التجريبي', 'جدل')],
    }
    
    updated_stu = 0
    for stu_slug, targets in stu_links.items():
        if stu_slug in slug_map:
            p = slug_map[stu_slug]['path']
            txt = p.read_text(encoding='utf-8')
            new_lines = []
            for tid, ttitle, ttype in targets:
                if tid in slug_map and tid not in txt:
                    new_lines.append(f'  - id: "{tid}", title: "{ttitle}", type: "{ttype}"')
            if new_lines:
                stu_block = '\n'.join(new_lines)
                if 'related:\n' in txt:
                    new_txt = txt.replace('related:\n', f'related:\n{stu_block}\n', 1)
                elif 'related:  []' in txt:
                    new_txt = txt.replace('related:  []', f'related:\n{stu_block}', 1)
                else:
                    new_txt = txt
                p.write_text(new_txt, encoding='utf-8')
                updated_stu += 1
                
    print(f'Phase 3 Complete: {updated_stu} classical studies enriched with direct links to thinkers, concepts, and replication debates.')

def phase_4_rebuild_and_verify():
    print('========================================')
    print('PHASE 4: Rebuilding Indexes, Matrices & Production Build')
    print('========================================')
    
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_slug_index.py')
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_coverage_matrix.py')
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_philosophy_matrix.py')
    os.system(f'python3 {ATLAS_ROOT}/scripts/build_atlas.py ar')
    
    data_json = ATLAS_ROOT / 'data.json'
    index_html = ATLAS_ROOT / 'index.html'
    
    with open(data_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    nodes_count = len(data.get('nodes', {}))
    html_size = index_html.stat().st_size
    
    print(f'Live Atlas Status:')
    print(f'  Nodes: {nodes_count:,}')
    print(f'  HTML size: {html_size:,} bytes ({html_size / (1024*1024):.2f} MB)')

def main():
    slug_map = get_all_slugs()
    print(f'Loaded {len(slug_map)} slugs across Atlas.')
    phase_1_dsm_evolution(slug_map)
    phase_2_psychometrics_enrichment(slug_map)
    phase_3_studies_enrichment(slug_map)
    phase_4_rebuild_and_verify()

if __name__ == '__main__':
    main()
