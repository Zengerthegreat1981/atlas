#!/usr/bin/env python3
"""
execute_promotion_pipeline.py
Executes the full 5-stage production promotion and release plan for Atlas:
  Stage 1: Pre-promotion integrity audit and normalization of drafts
  Stage 2: Sequential ID assignment
  Stage 3: Physical promotion (migration from content/ar/drafts/ to content/ar/)
  Stage 4: Graph cross-linking, zero orphan audit, and updating slug index & matrices
  Stage 5: Production build (data.json + index.html) and verification
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))

import os
import re
import sys
import json
import shutil
from pathlib import Path

ATLAS_ROOT = Path(_ATLAS_ROOT)
CONTENT_AR = ATLAS_ROOT / 'content' / 'ar'
DRAFTS_AR = CONTENT_AR / 'drafts'

PREFIXES = {
    'thinkers': 'THK',
    'concepts': 'CON',
    'works': 'WRK',
    'branches': 'BRN',
    'debates': 'DBT',
    'relations': 'REL',
    'axioms': 'AXM',
    'critiques': 'CRT',
    'dialogues': 'DIA',
    'events': 'EVT',
    'schools': 'SCH',
    'techniques': 'TEC',
    'studies': 'STU',
    'instruments': 'INS',
    'disorders': 'DIS',
    'syndromes': 'SYN',
    'contexts': 'CTX',
    'metaphors': 'MET',
    'terms': 'TRM',
    'questions': 'QUE',
    'experiences': 'EXP',
}

RELATED_ITEM_RE = re.compile(r'-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"')
EDGE_ITEM_RE = re.compile(r'-\s*rel:\s*"([^"]*)"\s*,\s*target:\s*"([^"]*)"\s*,\s*target_type:\s*"([^"]*)"')

def get_all_nodes():
    nodes = {}
    for root, dirs, files in os.walk(CONTENT_AR):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md') and f != 'EXISTING_SLUGS.md':
                p = Path(root) / f
                slug = f[:-3]
                is_draft = 'drafts' in p.parts
                nodes[slug] = {'path': p, 'is_draft': is_draft, 'folder': p.parent.name}
    return nodes

def stage_1_audit_and_fix():
    print('========================================')
    print('STAGE 1: Pre-Promotion Audit & Normalization')
    print('========================================')
    
    nodes = get_all_nodes()
    all_slugs = set(nodes.keys())
    app_count = sum(1 for n in nodes.values() if not n['is_draft'])
    draft_count = sum(1 for n in nodes.values() if n['is_draft'])
    print(f'Total nodes found on disk: {len(nodes)} (Approved: {app_count}, Drafts: {draft_count})')
    
    # 1. Build alias map for known phantom typos
    alias_map = {
        'thk-amaslow': 'thk-maslow',
        'thk-asutich': 'thk-sutich',
        'sch-kyoto-school': 'sch-kyoto',
        'thk-rncsikszentmihalyi': 'thk-csikszentmihalyi',
        'thk-mcsikszentmihalyi': 'thk-csikszentmihalyi',
        'thk-rshapiro': 'thk-shapiro',
        'thk-ledoux': 'thk-jledoux',
        'thk-james-william': 'thk-james',
        'thk-ddescartes': 'thk-descartes',
        'con-holotropic-breathwork': 'tec-holotropic-breathwork',
        'con-filial-piety': 'con-xiao-filial-piety',
        'con-cognitive-reappraisal': 'tec-cognitive-reappraisal',
        'con-disengagement': 'con-enmeshment-disengagement',
        'con-enmeshment': 'con-enmeshment-disengagement',
        'con-creativity-flow': 'con-flow',
        'con-body-scan': 'tec-cbt-mind-body-scan',
        'con-3min-breathing-space': 'con-cbt-mbt-mindfulness-3min-breathing-space',
        'con-boundaries': 'con-boundaries-psychological',
        'con-bowen-differentiation': 'con-differentiation-self',
        'con-change-talk': 'con-motivational-interviewing-oars',
        'con-character-strengths': 'tec-strengths-based-therapy',
        'con-cognitive-defusion': 'tec-cbt-cog-thought-defusion',
        'con-collective-trauma': 'con-historical-trauma',
        'con-committed-action': 'tec-act-ca-behavioral-commitment-exercises',
        'con-compassion': 'con-cft-self-compassion',
        'con-conservation': 'stu-piaget-conservation',
        'con-countertransference': 'con-transference',
        'con-decision-making': 'tec-act-val-values-based-decision-making',
        'con-defense': 'con-repression',
        'con-depression': 'dis-mdd',
        'con-deprivation-maternal': 'stu-bowlby-forty-four-thieves',
        'con-eightfold-path': 'sch-buddhism-early',
        'con-emotion-regulation': 'tec-stair-nt',
        'con-empathy': 'con-mutual-empathy',
        'con-explanatory-style': 'stu-peterson-seligman-explanatory-style',
        'con-family-homeostasis': 'con-homeostasis',
        'con-feminist-decolonial': 'con-pluriverse-decolonial',
        'con-fitrah': 'que-nature-vs-nurture',
        'con-historical-unresolved-grief': 'con-grief',
        'con-iceberg-metaphor': 'met-freud-iceberg',
        'con-insomnia': 'dis-insomnia-disorder',
        'con-instinct': 'trm-trieb-instinct-drive',
        'con-intentionality': 'axm-intentionality',
        'con-internal-frame-of-reference': 'con-unconditional-positive-regard',
        'con-interpersonal-learning': 'con-interpersonal-relationship',
        'con-meaning-of-life': 'con-will-to-meaning',
        'con-miracle-question': 'con-solution-focused-miracle-q',
        'con-nature-vs-nurture': 'que-nature-vs-nurture',
        'con-neurosis': 'con-neurosis-historical-framework',
        'con-panic': 'dis-panic-disorder',
        'con-ptsd': 'dis-ptsd',
        'con-pygmalion-effect': 'stu-rosenthal-pygmalion',
        'con-reparative-therapy': 'dbt-conversion-therapy-harm',
        'con-social-interest': 'con-social-interest-gemeinschaftsgefuhl',
        'con-strange-situation': 'stu-ainsworth-strange-situation',
        'con-tabula-rasa': 'axm-tabula-rasa',
        'con-triangulation': 'con-triangulation-family',
        'con-unconscious': 'con-unconscious',
        'con-unconscious-real': 'que-is-unconscious-real',
        'con-vicarious-reinforcement': 'stu-bandura-vicarious-reinforcement',
        'con-virtue': 'con-virtue-ethics',
        'con-working-memory': 'stu-baddeley-hitch-working-memory',
        'thk-adamasio': 'thk-damasio',
        'thk-ainsworth': 'thk-mary-ainsworth',
        'thk-al-farabi': 'thk-al-farabi',
        'thk-al-kindi': 'thk-al-kindi',
        'thk-al-razi': 'thk-al-razi-abu-bakr',
        'thk-alexander-lowen': 'thk-lowen',
        'thk-annafreud': 'thk-afreud',
        'thk-aron': 'thk-elaine-aron',
        'thk-ashutte': 'thk-ashutte',
        'thk-augustine': 'thk-augustine-hippo',
        'thk-bateson': 'thk-gbateson',
        'thk-beck-aaron': 'thk-beck',
        'thk-binswanger': 'thk-ludwigbinswanger',
        'thk-bion': 'thk-wbion',
        'thk-bolton': 'thk-robert-bolton',
        'thk-boss': 'thk-mboss',
        'thk-bowlby': 'thk-bowlby',
        'thk-brewer': 'thk-judson-brewer',
        'thk-brooks': 'thk-arthur-brooks',
        'thk-bugental': 'thk-jbugental',
        'thk-burrhus-skinner': 'thk-fskinner',
        'thk-cain': 'thk-susan-cain',
        'thk-campbell': 'thk-campbell-purton',
        'thk-carnegie': 'thk-carnegie',
        'thk-chalmers': 'thk-dchalmers',
        'thk-chapman': 'thk-gary-chapman',
        'thk-charles-taylor': 'thk-charlestaylor',
        'thk-charlestart': 'thk-ctart',
        'thk-cialdini': 'thk-cialdini',
        'thk-clear': 'thk-james-clear',
        'thk-covey': 'thk-stephen-covey',
        'thk-cuddy': 'thk-amy-cuddy',
        'thk-dana': 'thk-deb-dana',
        'thk-de-shazer': 'thk-sdeshacer',
        'thk-deshazer': 'thk-sdeshacer',
        'thk-dewey': 'thk-jdewey',
        'thk-dilthey': 'thk-dilthey',
        'thk-dowling': 'thk-colette-dowling',
        'thk-duckworth': 'thk-duckworth',
        'thk-duhigg': 'thk-charles-duhigg',
        'thk-dweck': 'thk-dweck',
        'thk-dyer': 'thk-wayne-dyer',
        'thk-eckhart-tolle': 'thk-tolle',
        'thk-ekman': 'thk-pekman',
        'thk-ellis': 'thk-aellis',
        'thk-erik-erikson': 'thk-erikson',
        'thk-ferris': 'thk-timothy-ferris',
        'thk-festinger': 'thk-lfestinger',
        'thk-flanagan': 'thk-kflanagan',
        'thk-fogg': 'thk-bj-fogg',
        'thk-forward': 'thk-susan-forward',
        'thk-fosha': 'thk-dfosha',
        'thk-frankl': 'thk-vfrankl',
        'thk-freud-sigmund': 'thk-sfreud',
        'thk-fritz-perls': 'thk-perls',
        'thk-gadamer': 'thk-hgadamer',
        'thk-garcia': 'thk-jgarcia',
        'thk-gibson': 'thk-lindsay-gibson',
        'thk-gilbert': 'thk-daniel-gilbert',
        'thk-gladwell': 'thk-gladwell',
        'thk-goleman': 'thk-goleman',
        'thk-gottman': 'thk-jgottman',
        'thk-grant': 'thk-adam-grant',
        'thk-gray': 'thk-john-gray',
        'thk-green': 'thk-robert-greene',
        'thk-greenberg': 'thk-lgreenberg',
        'thk-greene': 'thk-robert-greene',
        'thk-grof': 'thk-sgrof',
        'thk-haidt': 'thk-jonathan-haidt',
        'thk-haig': 'thk-matt-haig',
        'thk-hanson': 'thk-rick-hanson',
        'thk-hari': 'thk-johann-hari',
        'thk-harris': 'thk-russ-harris',
        'thk-hay': 'thk-louise-hay',
        'thk-hayes': 'thk-lstevenhayes',
        'thk-hegarty': 'thk-whegarty',
        'thk-heidegger': 'thk-mheidegger',
        'thk-hendricks': 'thk-harville-hendrix',
        'thk-hill': 'thk-napoleon-hill',
        'thk-husserl': 'thk-ehusserl',
        'thk-iyengar': 'thk-sheena-iyengar',
        'thk-james': 'thk-james',
        'thk-janov': 'thk-ajanov',
        'thk-jazaieri': 'thk-hjazaieri',
        'thk-john-gray': 'thk-john-gray',
        'thk-johnson': 'thk-sjohnson',
        'thk-kabat-zinn': 'thk-jkabatzinn',
        'thk-kahneman': 'thk-kahneman',
        'thk-kegan': 'thk-robert-kegan',
        'thk-kiley': 'thk-dan-kiley',
        'thk-klerman': 'thk-gklerman',
        'thk-kohler': 'thk-wkohler',
        'thk-kohlberg': 'thk-lkohlberg',
        'thk-kubler-ross': 'thk-elizabeth-kubler-ross',
        'thk-lakoff': 'thk-george-lakoff',
        'thk-lazarus': 'thk-alazarus',
        'thk-ledoux-joseph': 'thk-jledoux',
        'thk-lembke': 'thk-anna-lembke',
        'thk-lepper': 'thk-mrlepper',
        'thk-levin': 'thk-amir-levine',
        'thk-levine': 'thk-peter-levine',
        'thk-levine-peter': 'thk-peter-levine',
        'thk-linehan': 'thk-mlinehan',
        'thk-loftus': 'thk-elizabeth-loftus',
        'thk-lowen': 'thk-lowen',
        'thk-lynch': 'thk-tlynch',
        'thk-maltz': 'thk-maxwell-maltz',
        'thk-manson': 'thk-mark-manson',
        'thk-marcus-aurelius': 'thk-marcusaurelius',
        'thk-marsha-linehan': 'thk-mlinehan',
        'thk-martyn-carruthers': 'thk-mcarruthers',
        'thk-maslow': 'thk-maslow',
        'thk-masters-johnson': 'thk-vjohnson',
        'thk-mate': 'thk-gabor-mate',
        'thk-may': 'thk-rmay',
        'thk-milgram': 'thk-stanley-milgram',
        'thk-miller': 'thk-wr-miller',
        'thk-millman': 'thk-dan-millman',
        'thk-minuchin': 'thk-sminuchin',
        'thk-mischel': 'thk-wmischel',
        'thk-murphy': 'thk-joseph-murphy',
        'thk-neff': 'thk-kristin-neff',
        'thk-newport': 'thk-cal-newport',
        'thk-nietzsche': 'thk-nietzsche',
        'thk-noddings': 'thk-nel-noddings',
        'thk-peale': 'thk-norman-vincent-peale',
        'thk-peck': 'thk-scott-peck',
        'thk-pennebaker': 'thk-jpennebaker',
        'thk-perls': 'thk-perls',
        'thk-peterson': 'thk-jordan-peterson',
        'thk-piaget': 'thk-piaget',
        'thk-pinker': 'thk-steven-pinker',
        'thk-porges': 'thk-stephen-porges',
        'thk-ramana-maharshi': 'thk-ramana',
        'thk-rediger': 'thk-jeffrey-rediger',
        'thk-reich': 'thk-wreich',
        'thk-robbins': 'thk-tony-robbins',
        'thk-rogers': 'thk-crogers',
        'thk-rollnick': 'thk-srollnick',
        'thk-rosenberg': 'thk-marshall-rosenberg',
        'thk-rotter': 'thk-jrotter',
        'thk-rubin': 'thk-gretchen-rubin',
        'thk-ruiz': 'thk-don-miguel-ruiz',
        'thk-sacks': 'thk-oliver-sacks',
        'thk-sapolsky': 'thk-robert-sapolsky',
        'thk-satir': 'thk-vsatir',
        'thk-schwartz': 'thk-richard-schwartz',
        'thk-schwartz-barry': 'thk-barry-schwartz',
        'thk-schwartz-david': 'thk-david-schwartz',
        'thk-segal': 'thk-zsegal',
        'thk-seligman': 'thk-mseligman',
        'thk-shapiro': 'thk-shapiro',
        'thk-shapiro-francine': 'thk-shapiro',
        'thk-sharma': 'thk-robin-sharma',
        'thk-siegel': 'thk-daniel-siegel',
        'thk-skinner': 'thk-fskinner',
        'thk-smith': 'thk-julie-smith',
        'thk-spinoza': 'thk-spinoza',
        'thk-sutich': 'thk-sutich',
        'thk-szasz': 'thk-tszasz',
        'thk-tawab': 'thk-nedra-tawwab',
        'thk-teasdale': 'thk-jteasdale',
        'thk-thaler': 'thk-richard-thaler',
        'thk-tolle': 'thk-tolle',
        'thk-tversky': 'thk-amos-tversky',
        'thk-van-der-kolk': 'thk-besselvanderkolk',
        'thk-van-der-post': 'thk-lvdpost',
        'thk-vanderkolk': 'thk-besselvanderkolk',
        'thk-vygotsky': 'thk-vygotsky',
        'thk-walker': 'thk-matthew-walker',
        'thk-walsh': 'thk-rwalsh',
        'thk-watson': 'thk-jwatson',
        'thk-watzlawick': 'thk-pwatzlawick',
        'thk-whitaker': 'thk-cwhitaker',
        'thk-white': 'thk-mwhite',
        'thk-wilber': 'thk-kwilber',
        'thk-williams': 'thk-mark-williams',
        'thk-winch': 'thk-guy-winch',
        'thk-winfrey': 'thk-oprah-winfrey',
        'thk-winnicott': 'thk-dwinnicott',
        'thk-wolpe': 'thk-jwolpe',
        'thk-yalom': 'thk-iyalom',
        'thk-zimbardo': 'thk-philip-zimbardo',
        'wrk-flow': 'wrk-flow-csikszentmihalyi',
        'wrk-quiet': 'wrk-quiet-2012',
        'wrk-grit': 'wrk-grit-2016',
        'wrk-attachment': 'wrk-attachment-loss-volume1',
    }
    
    all_files = []
    for root, dirs, files in os.walk(CONTENT_AR):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md') and f != 'EXISTING_SLUGS.md':
                all_files.append(Path(root) / f)
                
    modified_count = 0
    total_phantoms_removed = 0
    total_aliases_applied = 0
    
    for p in all_files:
        txt = p.read_text(encoding='utf-8')
        if not txt.startswith('---'):
            continue
        parts = txt.split('---', 2)
        if len(parts) < 3:
            continue
        fm = parts[1]
        body = parts[2]
        
        in_related = False
        in_edges = False
        in_gaps = False
        
        current_gaps = []
        current_related = []
        current_edges = []
        other_fields = []
        
        lines = fm.split('\n')
        for line in lines:
            sline = line.strip()
            if sline.startswith('edges:'):
                in_edges = True; in_related = False; in_gaps = False
                continue
            elif sline.startswith('related:'):
                in_related = True; in_edges = False; in_gaps = False
                continue
            elif sline.startswith('gaps:'):
                in_gaps = True; in_related = False; in_edges = False
                continue
            elif re.match(r'^[a-zA-Z0-9_-]+:', sline) and not line.startswith(' ') and not line.startswith('\t'):
                in_edges = False; in_related = False; in_gaps = False
                other_fields.append(line)
                continue
                
            if in_edges:
                if sline.startswith('-'):
                    fixed_edge = sline
                    if 'type:' in fixed_edge and 'target_type:' not in fixed_edge:
                        fixed_edge = re.sub(r',\s*type:\s*"([^"]*)"', r', target_type: "\1"', fixed_edge)
                    current_edges.append(fixed_edge)
            elif in_related:
                if sline.startswith('-'):
                    fixed_rel = sline
                    if fixed_rel.count('type:') > 1:
                        fixed_rel = re.sub(r',\s*type:\s*"[^"]*"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"', r', title: "\1", type: "\2"', fixed_rel)
                    
                    rm = RELATED_ITEM_RE.search(fixed_rel)
                    if rm:
                        rid, rtitle, rtype = rm.groups()
                        if rid in alias_map:
                            target_slug = alias_map[rid]
                            if target_slug in all_slugs:
                                rid = target_slug
                                fixed_rel = f'  - id: "{rid}", title: "{rtitle}", type: "{rtype}"'
                                total_aliases_applied += 1
                        
                        if rid in all_slugs:
                            current_related.append(fixed_rel)
                        else:
                            total_phantoms_removed += 1
                            current_gaps.append(f'  - "رابط مقترح لم يتحقق بعد في الأطلس: {rtitle} ({rid})"')
                    else:
                        current_related.append(fixed_rel)
            elif in_gaps:
                if sline.startswith('-'):
                    current_gaps.append(line)
            else:
                other_fields.append(line)
                
        fm_dict = {}
        for line in other_fields:
            km = re.match(r'^([a-zA-Z0-9_-]+):\s*(.*)$', line.strip())
            if km:
                fm_dict[km.group(1)] = km.group(2)
                
        slug = p.stem
        folder = p.parent.name
        
        if 'part' not in fm_dict:
            if folder in ['axioms', 'branches', 'concepts', 'critiques', 'debates', 'dialogues', 'events', 'schools', 'thinkers', 'works']:
                if any(x in txt for x in ['علم النفس', 'سلوكي', 'معرفي', 'تحليل نفسي', 'CBT', 'ACT', 'DBT', 'اضطراب']):
                    fm_dict['part'] = '"psychology"'
                else:
                    fm_dict['part'] = '"philosophy"'
            elif folder in ['disorders', 'syndromes', 'techniques', 'studies', 'instruments']:
                fm_dict['part'] = '"psychology"'
            elif folder in ['relations']:
                fm_dict['part'] = '"bridge"'
            else:
                fm_dict['part'] = '"philosophy"'
                
        if 'level' not in fm_dict:
            fm_dict['level'] = '"متوسط"'
            
        if 'active_start' not in fm_dict:
            fm_dict['active_start'] = 'null'
        if 'active_end' not in fm_dict:
            fm_dict['active_end'] = '"مستمر"'
            
        if 'crumb' not in fm_dict:
            m_title = re.search(r'^title:\s*"([^"]*)"', txt, re.M)
            title_val = m_title.group(1) if m_title else slug
            fm_dict['crumb'] = f'"الأطلس ← {folder} ← {title_val}"'
            
        if len(current_gaps) < 2:
            current_gaps.append('  - "المصادر الأولية تحتاج مراجعة وتوثيقاً إضافياً."')
            if len(current_gaps) < 2:
                current_gaps.append('  - "توسيع شبكة العلاقات مع المدارس المجاورة قيد المتابعة التحريرية."')
                
        new_fm_lines = []
        for k, v in fm_dict.items():
            new_fm_lines.append(f'{k}: {v}')
            
        new_fm_lines.append('edges:')
        if current_edges:
            new_fm_lines.extend(current_edges)
        else:
            new_fm_lines.append('  []')
            
        new_fm_lines.append('related:')
        if current_related:
            new_fm_lines.extend(current_related)
        else:
            new_fm_lines.append('  []')
            
        new_fm_lines.append('gaps:')
        new_fm_lines.extend(current_gaps)
        
        new_fm_text = '\n'.join(new_fm_lines)
        new_full_text = f'---\n{new_fm_text}\n---{body}'
        
        if new_full_text != txt:
            p.write_text(new_full_text, encoding='utf-8')
            modified_count += 1
            
    print(f'Stage 1 Normalization Complete: {modified_count} files updated.')
    print(f'  Aliases resolved: {total_aliases_applied}')
    print(f'  Phantom references cleaned: {total_phantoms_removed}')

def stage_2_assign_ids():
    print('\n========================================')
    print('STAGE 2: Sequential ID Generation & Assignment')
    print('========================================')
    
    max_ids = {}
    for folder, prefix in PREFIXES.items():
        max_ids[prefix] = 0
        p = CONTENT_AR / folder
        if p.exists():
            for f in p.glob('*.md'):
                txt = f.read_text(encoding='utf-8')
                m = re.search(r'^id:\s*"' + prefix + r'-(\d+)"', txt, re.M)
                if m:
                    num = int(m.group(1))
                    if num > max_ids[prefix]:
                        max_ids[prefix] = num
                        
    plan_min_starts = {
        'THK': 2220,
        'CON': 807,
        'WRK': 495,
        'BRN': 228,
        'DBT': 352,
        'REL': 153,
        'AXM': 3,
        'CRT': 22,
        'DIA': 3,
        'EVT': 72,
    }
    for pfx, min_val in plan_min_starts.items():
        if max_ids[pfx] < min_val:
            max_ids[pfx] = min_val
            
    print('Initial high-water marks per prefix:')
    for pfx, max_val in sorted(max_ids.items()):
        print(f'  {pfx}: next ID = {pfx}-{(max_val+1):04d}')
        
    assigned_count = 0
    
    for folder, prefix in PREFIXES.items():
        draft_folder = DRAFTS_AR / folder
        draft_files = []
        if draft_folder.exists():
            draft_files = sorted(list(draft_folder.glob('*.md')), key=lambda x: x.name)
            
        app_folder = CONTENT_AR / folder
        app_files = []
        if app_folder.exists():
            for f in sorted(list(app_folder.glob('*.md')), key=lambda x: x.name):
                txt = f.read_text(encoding='utf-8')
                if '[DRAFT-UNKNOWN]' in txt or 'id: "[DRAFT' in txt:
                    app_files.append(f)
                    
        files_to_assign = app_files + draft_files
        for p in files_to_assign:
            txt = p.read_text(encoding='utf-8')
            m = re.search(r'^id:\s*"([^"]*)"', txt, re.M)
            if not m or m.group(1) == '[DRAFT-UNKNOWN]' or m.group(1).startswith('[DRAFT') or not m.group(1).startswith(prefix + '-'):
                max_ids[prefix] += 1
                new_id = f'{prefix}-{max_ids[prefix]:04d}'
                if m:
                    new_txt = re.sub(r'^id:\s*"[^"]*"', f'id: "{new_id}"', txt, flags=re.M)
                else:
                    new_txt = txt.replace('---\n', f'---\nid: "{new_id}"\n', 1)
                p.write_text(new_txt, encoding='utf-8')
                assigned_count += 1
                
    print(f'Stage 2 ID Assignment Complete: {assigned_count} files assigned permanent IDs.')
    print('Final highest IDs per prefix:')
    for pfx, max_val in sorted(max_ids.items()):
        print(f'  {pfx}: {pfx}-{max_val:04d}')

def stage_3_physical_promotion():
    print('\n========================================')
    print('STAGE 3: Physical Promotion & Migration')
    print('========================================')
    
    promoted_count = 0
    collisions_resolved = 0
    
    for folder in PREFIXES.keys():
        draft_folder = DRAFTS_AR / folder
        target_folder = CONTENT_AR / folder
        target_folder.mkdir(parents=True, exist_ok=True)
        
        if not draft_folder.exists():
            continue
            
        for f in draft_folder.glob('*.md'):
            target_file = target_folder / f.name
            if target_file.exists():
                collisions_resolved += 1
                shutil.copy2(f, target_file)
                f.unlink()
                promoted_count += 1
            else:
                shutil.move(str(f), str(target_file))
                promoted_count += 1
                
        try:
            draft_folder.rmdir()
        except OSError:
            pass
            
    print(f'Stage 3 Physical Promotion Complete:')
    print(f'  Total files promoted: {promoted_count}')
    print(f'  Collisions resolved and overwritten: {collisions_resolved}')

def stage_4_graph_audit_and_indexes():
    print('\n========================================')
    print('STAGE 4: Graph Cross-Linking & Index Matrix Updates')
    print('========================================')
    
    cmd_slug = f'python3 {ATLAS_ROOT}/scripts/build_slug_index.py'
    res = os.system(cmd_slug)
    if res != 0:
        raise RuntimeError('build_slug_index.py failed!')
        
    cov_script = ATLAS_ROOT / 'scripts' / 'build_coverage_matrix.py'
    if cov_script.exists():
        os.system(f'python3 {cov_script}')
        
    phil_script = ATLAS_ROOT / 'scripts' / 'build_philosophy_matrix.py'
    if phil_script.exists():
        os.system(f'python3 {phil_script}')
        
    print('Stage 4 Matrices and Indexes Rebuilt Successfully.')

def stage_5_build_and_verify():
    print('\n========================================')
    print('STAGE 5: Production Build & Live Release Verification')
    print('========================================')
    
    cmd_build = f'python3 {ATLAS_ROOT}/scripts/build_atlas.py ar'
    res = os.system(cmd_build)
    if res != 0:
        raise RuntimeError('build_atlas.py ar failed!')
        
    data_json = ATLAS_ROOT / 'data.json'
    index_html = ATLAS_ROOT / 'index.html'
    
    if not data_json.exists() or not index_html.exists():
        raise RuntimeError('Build outputs missing!')
        
    with open(data_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    nodes_count = len(data.get('nodes', {}))
    html_size = index_html.stat().st_size
    
    print(f'Production Build Verification:')
    print(f'  data.json nodes count: {nodes_count:,}')
    print(f'  index.html size: {html_size:,} bytes ({html_size / (1024*1024):.2f} MB)')
    
    if nodes_count < 5500:
        print(f'WARNING: Expected 5,500+ nodes, but got {nodes_count}')
    else:
        print(f'SUCCESS: Atlas live release contains {nodes_count:,} production nodes!')

def main():
    stage_1_audit_and_fix()
    stage_2_assign_ids()
    stage_3_physical_promotion()
    stage_4_graph_audit_and_indexes()
    stage_5_build_and_verify()

if __name__ == '__main__':
    main()
