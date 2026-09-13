#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auto_close_orphans.py — إغلاق آلي للـorphans الناتجة عن الـbackground workers.

الاستراتيجية: لكل orphan، أضف related entry في ملف من نفس النوع.
"""
import os as _os
# جذرُ المستودع يُشتقّ من موضع الملفّ نفسِه — لا مسارٌ مثبَّتٌ لجهازٍ بعينه.
_ATLAS_ROOT = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..'))
import os, re, sys, json

ROOT = _ATLAS_ROOT
AR = os.path.join(ROOT, 'content/ar')

TYPES = {
    'schools': 'مدرسة', 'concepts': 'مفهوم', 'works': 'عمل / كتاب',
    'thinkers': 'مفكر', 'debates': 'جدل', 'critiques': 'نقد خارجي موثَّق',
    'instruments': 'أداة قياس', 'studies': 'دراسة وبحث', 'techniques': 'تقنية/تدخل علاجي',
    'events': 'حدث تاريخي', 'branches': 'تيار', 'syndromes': 'متلازمة',
    'disorders': 'اضطراب/حالة إكلينيكية', 'axioms': 'مبدأ/بديهية',
    'contexts': 'سياق/تقليد', 'experiences': 'تجربة', 'metaphors': 'استعارة',
    'questions': 'سؤال', 'terms': 'مصطلح', 'dialogues': 'حوار', 'relations': 'علاقة بين مدرستين',
}

def main():
    if not os.path.exists('/tmp/minimax_orphans.json'):
        print('No orphans file found — run orphan_audit first.')
        return

    with open('/tmp/minimax_orphans.json', encoding='utf-8') as fh:
        data = json.load(fh)

    added = 0
    for typ, items in data['by_type'].items():
        folder = f'{AR}/{typ}'
        if not os.path.isdir(folder): continue
        for item in items:
            slug = item['slug']
            title = item['title']
            type_label = TYPES.get(typ, typ)
            new_entry = f'- id: "{slug}", title: "{title}", type: "{type_label}"\n'
            # Find candidate file in same folder
            for f in os.listdir(folder):
                if not f.endswith('.md') or f.startswith('_'): continue
                if f == f'{slug}.md': continue
                fp = f'{folder}/{f}'
                with open(fp, encoding='utf-8') as fh:
                    c = fh.read()
                if f'id: "{slug}"' in c: continue
                m = re.search(r'(related:\s*\n(?:\s*-\s+id:[^\n]*\n)*)', c, re.MULTILINE)
                if m:
                    block = m.group(1)
                    new_block = block + new_entry
                    new_c = c[:m.start(1)] + new_block + c[m.end(1):]
                    with open(fp, 'w', encoding='utf-8') as fh:
                        fh.write(new_c)
                    added += 1
                    break
    print(f'Added {added} incoming references')

if __name__ == '__main__':
    main()
