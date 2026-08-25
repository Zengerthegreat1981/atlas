#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""يبني داشبورد أطلس على سطح المكتب. يُشغَّل بعد كل مراجعة."""
import os, re, json, html, collections, statistics, subprocess
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR   = os.path.join(ROOT, 'content', 'ar')
REP  = os.path.join(ROOT, 'agents_specs', 'reports')
OUT  = os.path.expanduser('~/Desktop/atlas-dashboard.html')
SKIP = {'drafts', '_merged'}

STAMP = {'sch-cognitive-behavioral','sch-psychoanalysis','sch-existential-therapy',
         'sch-humanistic','sch-positive-psychology'}
FILLER = {'wrk-men-are-from-mars','wrk-12-rules-for-life','wrk-design-everyday-things',
          'wrk-power-of-habit','con-res-cogitans-res-extensa','con-set-and-setting',
          'con-voluntarism-divine-will','br-relational-cultural','br-recovered-memory-movement',
          'dbt-mao-maoism-vs-deng-ism','dbt-feminist-essentialism-vs-constructionism',
          'evt-egaz-moniz-nobel-lobotomy-1949','evt-founding-of-al-azhar-970'}
BL = ['لبنة تأسيسية','أطروحة فلسفية فارقة','تحولاً جوهرياً وتطويراً بنيوياً',
      'علامة فارقة في مجاله','رؤية نسقية تستند','منعطفاً حاسماً',
      'تفكيك المسلمات النظرية','جسراً معرفياً','لحظة تاريخية وفكرية مفصلية']

# الأساس المرجعي (2026-08-25) — الفرق عنه هو التقدم
BASE = {'files':6618,'stamped':1268,'filler':1615,'scaffold':532,'noquote':4502,
        'sources':1,'bt_name':2819,'blacklist':850,'u600':1554,'u1200':3985}
TARGET = {'stamped':0,'filler':0,'scaffold':0,'noquote':0,'sources':5000,
          'bt_name':0,'blacklist':0,'u600':300}

# خريطة المراحل: (مرحلة, تاسك, عنوان, مسار)
TASKS = {
 'spark': [('م1',1,'التراث العربي-الإسلامي'),('م1',2,'الملفات المشكوك فيها'),
   ('م1',3,'التدقيق القرائي thk-a→l'),('م1',4,'التعميق والمصادر'),
   ('م2',5,'works: المخطط الغائب'),('م2',6,'works: التعميق'),
   ('م2',7,'studies: المخطط والتكرار'),('م2',8,'instruments'),
   ('م2',9,'techniques'),('م2',10,'disorders + syndromes'),
   ('م2',11,'events'),('م2',12,'contexts/experiences/metaphors'),
   ('م3',13,'الدراسة موجودة وصاحبها غائب'),('م3',14,'دراسات وأدوات حديثة'),
   ('م3',15,'تقنيات واضطرابات غائبة'),('م3',16,'النوع الجديد drg-'),
   ('م3',17,'طبقة ما بعد 2010')],
 'minimax': [('م1',1,'التراث العربي-الإسلامي'),('م1',2,'الملفات المشكوك فيها'),
   ('م1',3,'التدقيق القرائي thk-m→z'),('م1',4,'التعميق والمصادر'),
   ('م2',5,'belongs_to الباقي'),('م2',6,'branches: إنقاذ'),
   ('م2',7,'relations: إنقاذ'),('م2',8,'schools: التوثيق'),
   ('م2',9,'concepts: إعادة الربط'),('م2',10,'concepts: كسر القالب'),
   ('م2',11,'debates + critiques'),('م2',12,'dialogues/questions/terms/axioms'),
   ('م3',13,'المدارس الغائبة'),('م3',14,'علم النفس العربي الحديث'),
   ('م3',15,'الفلاسفة الغائبون'),('م3',16,'أعمال وحوارات غائبة'),
   ('م3',17,'النوع الجديد eth-')],
}

PHASE0 = [(1,'إيقاف النماذج + لقطة'),(2,'atlas_parse.py'),(3,'atlas_health.py'),
  (4,'task.py'),(5,'الأعطال البنيوية'),(6,'حذف المطبوع والحشو'),
  (7,'حصاد السقّالات'),(8,'belongs_to الآلي'),(9,'التوحيد النصي'),
  (10,'تقليم الملفات الثلاثة'),(11,'فصل بنية المسارين'),(12,'الداشبورد')]


def scan():
    m = collections.Counter(); lens = collections.defaultdict(list)
    if not os.path.isdir(AR): return m, lens
    for d in sorted(os.listdir(AR)):
        p = os.path.join(AR, d)
        if not os.path.isdir(p) or d in SKIP: continue
        for f in sorted(os.listdir(p)):
            if not f.endswith('.md'): continue
            try: t = open(os.path.join(p, f), encoding='utf-8', errors='replace').read()
            except OSError: continue
            m['files'] += 1
            parts = t.split('---', 2)
            body = (parts[2] if len(parts) > 2 else t).strip()
            lens[d].append(len(body))
            if len(body) < 600: m['u600'] += 1
            if len(body) < 1200: m['u1200'] += 1
            rel = re.findall(r'- id: "([^"]+)"', t)
            if len(rel) >= 2 and len(set(rel[:3]) & STAMP) >= 2: m['stamped'] += 1
            if set(rel) & FILLER: m['filler'] += 1
            if any(k in t for k in ('أفكار روابط لم تُتحقق','ملاحظة معمارية','مراجعة وكيل')):
                m['scaffold'] += 1
            if 'لا يوجد اقتباس مباشر موثوق' in t: m['noquote'] += 1
            if '## المصادر' in t: m['sources'] += 1
            if any(b in t for b in BL): m['blacklist'] += 1
            for mm in re.finditer(r'rel: "belongs_to", target: "([^"]+)"', t):
                if not re.match(r'^[a-z]+-', mm.group(1)): m['bt_name'] += 1
    return m, lens


def read_index(track):
    """يقرأ INDEX.md ويرجّع {task_no: {'done':n,'last':str,'partial':n}}"""
    path = os.path.join(REP, track, 'INDEX.md')
    out = collections.defaultdict(lambda: {'done':0,'partial':0,'stopped':0,'last':'','files':0})
    rows = []
    if not os.path.isfile(path): return out, rows
    for line in open(path, encoding='utf-8', errors='replace'):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 4 or not re.match(r'^\d+\.\d+$', c[0]): continue
        major = c[0].split('.')[0]
        st = c[1]
        e = out[major]
        if '✅' in st or 'مكتمل' == st: e['done'] += 1
        elif '⚠' in st or 'جزئي' in st: e['partial'] += 1
        else: e['stopped'] += 1
        e['last'] = c[2] if len(c) > 2 else ''
        n = re.search(r'(\d+)', c[4]) if len(c) > 4 else None
        if n: e['files'] += int(n.group(1))
        rows.append({'id':c[0],'st':st,'date':c[2] if len(c)>2 else '',
                     'what':c[3] if len(c)>3 else '','n':c[4] if len(c)>4 else ''})
    return out, rows[-12:]


def git_info():
    try:
        log = subprocess.run(['git','log','-1','--format=%h|%ci|%s'], cwd=ROOT,
                             capture_output=True, text=True, timeout=10).stdout.strip()
        dirty = subprocess.run(['git','status','--porcelain'], cwd=ROOT,
                               capture_output=True, text=True, timeout=30).stdout
        h, d, s = (log.split('|', 2) + ['', '', ''])[:3]
        return h, d[:16], s[:70], len([x for x in dirty.splitlines() if x.strip()])
    except Exception:
        return '—', '—', '—', 0


def bar(cur, base, target, invert=True):
    """نسبة الإنجاز 0-100"""
    if invert:
        if base == target: return 100
        return max(0, min(100, round(100 * (base - cur) / (base - target))))
    if target == base: return 100
    return max(0, min(100, round(100 * (cur - base) / (target - base))))


def main():
    m, lens = scan()
    gh, gd, gs, dirty = git_info()
    med = {d: int(statistics.median(v)) for d, v in lens.items() if v}

    metrics = [
        ('الروابط المطبوعة آلياً','stamped',True),
        ('روابط الحشو','filler',True),
        ('أقسام السقّالة الظاهرة','scaffold',True),
        ('«لا يوجد اقتباس موثوق»','noquote',True),
        ('الجمل القالبية','blacklist',True),
        ('belongs_to نصي غير محلول','bt_name',True),
        ('ملفات متنها أقل من 600 حرف','u600',True),
        ('ملفات فيها قسم المصادر','sources',False),
    ]
    rows = []
    for label, key, inv in metrics:
        cur = m.get(key, 0); b = BASE[key]; t = TARGET[key]
        rows.append({'label':label,'cur':cur,'base':b,'target':t,
                     'pct':bar(cur,b,t,inv),'delta':(b-cur) if inv else (cur-b)})

    tracks = {}
    for tr in ('spark','minimax'):
        idx, recent = read_index(tr)
        ts = []
        for phase, no, title in TASKS[tr]:
            e = idx.get(str(no), {'done':0,'partial':0,'stopped':0,'last':'','files':0})
            state = 'done' if e['done'] and not e['partial'] and not e['stopped'] else \
                    ('active' if (e['done'] or e['partial'] or e['stopped']) else 'todo')
            ts.append({'phase':phase,'no':no,'title':title,'state':state,
                       'sub':e['done'],'partial':e['partial'],'stopped':e['stopped'],
                       'files':e['files'],'last':e['last']})
        tracks[tr] = {'tasks':ts,'recent':recent,
                      'done':sum(1 for x in ts if x['state']=='done'),
                      'total':len(ts),
                      'subs':sum(x['sub'] for x in ts),
                      'files':sum(x['files'] for x in ts)}

    p0done = os.path.isfile(os.path.join(ROOT,'scripts','task.py'))
    data = {'gen':datetime.now().strftime('%Y-%m-%d %H:%M'),
            'files':m.get('files',0),'base_files':BASE['files'],
            'git':{'h':gh,'d':gd,'s':gs,'dirty':dirty},
            'metrics':rows,'tracks':tracks,'median':med,
            'phase0':[{'no':n,'t':t} for n,t in PHASE0],'p0':p0done}

    open(OUT,'w',encoding='utf-8').write(TPL.replace('__DATA__', json.dumps(data, ensure_ascii=False)))
    print(f"✅ {OUT}")
    print(f"   ملفات: {m.get('files',0)} | Spark: {tracks['spark']['subs']} sub-task | MiniMax: {tracks['minimax']['subs']} sub-task")


TPL = r'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>أطلس — لوحة المتابعة</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#f6f7f9;--card:#fff;--ink:#15181d;--dim:#697082;--line:#e3e6ec;
--ok:#1f9d5b;--warn:#d98317;--todo:#b4bac6;--accent:#3f6fd8;--accent2:#c0447a;--bar:#eceff4}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#101318;--card:#171b22;--ink:#eef1f6;
--dim:#98a0b0;--line:#262c37;--bar:#232833;--todo:#4a515f}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Cairo,system-ui,sans-serif;padding:22px 16px 60px}
.wrap{max-width:1120px;margin:0 auto}
h1{font-size:26px;font-weight:800;margin:0 0 2px}
.sub{color:var(--dim);font-size:13px;margin-bottom:20px}
.grid{display:grid;gap:14px}
.g4{grid-template-columns:repeat(4,1fr)}.g2{grid-template-columns:1fr 1fr}
@media(max-width:820px){.g4{grid-template-columns:1fr 1fr}.g2{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px}
.kpi .n{font-size:32px;font-weight:800;line-height:1.1}
.kpi .l{color:var(--dim);font-size:12px;margin-top:4px}
h2{font-size:15px;font-weight:700;margin:26px 0 12px;color:var(--dim)}
.m{display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid var(--line)}
.m:last-child{border:0}
.m .lab{flex:1;font-size:13.5px}
.m .num{font-variant-numeric:tabular-nums;font-size:13px;color:var(--dim);white-space:nowrap}
.m .num b{color:var(--ink);font-size:15px}
.track{width:120px;height:7px;background:var(--bar);border-radius:6px;overflow:hidden;flex:none}
.track i{display:block;height:100%;border-radius:6px;background:var(--ok)}
.chip{font-size:11px;padding:2px 8px;border-radius:20px;background:var(--bar);color:var(--dim)}
.th{display:flex;align-items:center;gap:9px;margin-bottom:12px}
.dot{width:11px;height:11px;border-radius:50%}
.t{display:flex;align-items:center;gap:10px;padding:7px 0;font-size:13px;border-bottom:1px solid var(--line)}
.t:last-child{border:0}
.t .ph{font-size:10.5px;color:var(--dim);width:22px;flex:none}
.t .st{width:9px;height:9px;border-radius:50%;flex:none;background:var(--todo)}
.t.done .st{background:var(--ok)}.t.active .st{background:var(--warn)}
.t .ti{flex:1}.t.done .ti{color:var(--dim)}
.t .n{font-size:11px;color:var(--dim);font-variant-numeric:tabular-nums}
.p0{display:flex;flex-wrap:wrap;gap:7px}
.p0 span{font-size:11.5px;padding:4px 10px;border-radius:8px;background:var(--bar);color:var(--dim)}
.p0 span.on{background:var(--ok);color:#fff}
.rec{font-size:12px;color:var(--dim);padding:5px 0;border-bottom:1px solid var(--line)}
.rec:last-child{border:0}
.foot{margin-top:28px;color:var(--dim);font-size:11.5px;text-align:center;line-height:1.9}
code{background:var(--bar);padding:2px 7px;border-radius:5px;font-size:11px;font-family:ui-monospace,monospace;direction:ltr;display:inline-block}
</style></head><body><div class="wrap">
<h1>أطلس النفس البشرية</h1>
<div class="sub" id="sub"></div>
<div class="grid g4" id="kpis"></div>
<h2>المرحلة 0 — البنية التحتية والتنظيف الميكانيكي</h2>
<div class="card"><div class="p0" id="p0"></div></div>
<h2>المؤشرات — كل واحد مقاوم للحشو</h2>
<div class="card" id="metrics"></div>
<h2>المساران</h2>
<div class="grid g2" id="tracks"></div>
<div class="foot" id="foot"></div>
</div>
<script>
const D = __DATA__;
const el = (h)=>{const d=document.createElement('div');d.innerHTML=h;return d.firstElementChild};

document.getElementById('sub').textContent =
  `آخر تحديث ${D.gen} · لقطة ${D.git.h} (${D.git.d})` + (D.git.dirty? ` · ${D.git.dirty} تغيير غير محفوظ` : ' · المستودع محفوظ');

const sp=D.tracks.spark, mm=D.tracks.minimax;
const kp=[
 [D.files.toLocaleString('en'),'ملف في الأطلس'],
 [(sp.subs+mm.subs).toLocaleString('en'),'sub-task مكتملة'],
 [`${sp.done+mm.done} / ${sp.total+mm.total}`,'تاسك مكتمل'],
 [(sp.files+mm.files).toLocaleString('en'),'ملف اتعالج'],
];
const K=document.getElementById('kpis');
kp.forEach(([n,l])=>K.appendChild(el(`<div class="card kpi"><div class="n">${n}</div><div class="l">${l}</div></div>`)));

const P=document.getElementById('p0');
D.phase0.forEach(t=>P.appendChild(el(`<span class="${D.p0&&t.no<=4?'on':''}">${t.no}. ${t.t}</span>`)));

const M=document.getElementById('metrics');
D.metrics.forEach(m=>{
  const d = m.delta>0? `<span class="chip">−${m.delta.toLocaleString('en')}</span>` :
            (m.delta<0? `<span class="chip">+${(-m.delta).toLocaleString('en')}</span>` : '');
  M.appendChild(el(`<div class="m"><span class="lab">${m.label}</span>${d}
    <span class="num"><b>${m.cur.toLocaleString('en')}</b> / ${m.target.toLocaleString('en')}</span>
    <span class="track"><i style="width:${m.pct}%"></i></span>
    <span class="num" style="width:34px;text-align:left">${m.pct}%</span></div>`));
});

const T=document.getElementById('tracks');
[['spark','Spark','الإكلينيكي والتجريبي','#3f6fd8'],
 ['minimax','MiniMax','البنيوي والفلسفي','#c0447a']].forEach(([k,name,desc,c])=>{
  const t=D.tracks[k];
  let h=`<div class="card"><div class="th"><span class="dot" style="background:${c}"></span>
    <b style="font-size:15px">${name}</b><span class="chip">${desc}</span>
    <span style="margin-inline-start:auto" class="chip">${t.subs} sub-task</span></div>`;
  t.tasks.forEach(x=>{
    const n = x.sub? `${x.sub} دفعة${x.partial?' ⚠':''}` : '';
    h+=`<div class="t ${x.state}"><span class="ph">${x.phase}</span><span class="st"></span>
        <span class="ti">${x.no}. ${x.title}</span><span class="n">${n}</span></div>`;
  });
  if(t.recent.length){
    h+=`<div style="margin-top:14px;padding-top:12px;border-top:1px solid var(--line)">
        <div style="font-size:11px;color:var(--dim);margin-bottom:6px">آخر ما تم</div>`;
    t.recent.slice().reverse().forEach(r=>{
      h+=`<div class="rec">${r.st} <b style="color:var(--ink)">${r.id}</b> — ${r.what} <span style="opacity:.7">${r.n}</span></div>`;
    });
    h+='</div>';
  }
  T.appendChild(el(h+'</div>'));
});

document.getElementById('foot').innerHTML =
 `للتحديث: دوس دبل-كليك على <code>atlas-refresh.command</code> على سطح المكتب<br>
  أو <code>python3 scripts/atlas_dashboard.py</code> من مجلد Atlas`;
</script></body></html>'''

if __name__ == '__main__':
    main()
