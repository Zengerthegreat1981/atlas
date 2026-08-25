import os, glob, re
from collections import defaultdict

base = "/Users/minamoheb/Desktop/Atlas/content/ar"
slug_set = set()
slug_to_file = {}
slug_to_meta = {}

RELATED_ITEM_RE = re.compile(r"-\s*id:\s*"([^"]*)"\s*,\s*title:\s*"([^"]*)"\s*,\s*type:\s*"([^"]*)"")

for root, dirs, files in os.walk(base):
    if "drafts" in root or "_merged" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            slug = f[:-3]
            slug_set.add(slug)
            fpath = os.path.join(root, f)
            slug_to_file[slug] = fpath
            with open(fpath, "r", encoding="utf-8") as fp:
                txt = fp.read()
            m_title = re.search(r"^title:\s*"([^"]*)"", txt, re.M)
            m_type = re.search(r"^type:\s*"([^"]*)"", txt, re.M)
            slug_to_meta[slug] = {
                "title": m_title.group(1).strip() if m_title else slug,
                "type": m_type.group(1).strip() if m_type else "مفكر"
            }

in_links = defaultdict(list)
existing_related = defaultdict(list)

for slug, fpath in slug_to_file.items():
    with open(fpath, "r", encoding="utf-8") as fp:
        txt = fp.read()
    if not txt.startswith("---"):
        continue
    raw_yaml = txt.split("---", 2)[1]
    rel_items = RELATED_ITEM_RE.findall(raw_yaml)
    existing_related[slug] = rel_items
    for rid, rtitle, rtype in rel_items:
        if rid in slug_set and rid != slug:
            in_links[rid].append((slug, slug_to_meta[slug]["title"], slug_to_meta[slug]["type"]))

files_updated = 0
links_added = 0
NL = chr(10)

for slug, fpath in slug_to_file.items():
    cur_rels = existing_related[slug]
    cur_rel_ids = set(r[0] for r in cur_rels)
    
    if len(cur_rels) < 3 and slug in in_links:
        candidates = in_links[slug]
        to_add = []
        for src_id, src_title, src_type in candidates:
            if src_id not in cur_rel_ids and src_id != slug:
                to_add.append((src_id, src_title, src_type))
                cur_rel_ids.add(src_id)
                if len(cur_rels) + len(to_add) >= 5:
                    break
        
        if to_add:
            with open(fpath, "r", encoding="utf-8") as fp:
                txt = fp.read()
            parts = txt.split("---", 2)
            if len(parts) < 3:
                continue
            raw_yaml = parts[1]
            body = parts[2]
            
            lines_list = [f"- id: \"{aid}\", title: \"{atitle}\", type: \"{atype}\"" for aid, atitle, atype in to_add]
            formatted_add = NL.join(lines_list)
            
            if "related:" + NL + "  []" in raw_yaml:
                new_yaml = raw_yaml.replace("related:" + NL + "  []", "related:" + NL + formatted_add)
            elif "related: []" in raw_yaml:
                new_yaml = raw_yaml.replace("related: []", "related:" + NL + formatted_add)
            elif "related:" in raw_yaml:
                new_yaml = re.sub(r"(related:\s*
)", r"" + formatted_add + NL, raw_yaml, count=1)
            else:
                if "gaps:" in raw_yaml:
                    new_yaml = raw_yaml.replace("gaps:", "related:" + NL + formatted_add + NL + "gaps:")
                else:
                    new_yaml = raw_yaml + NL + "related:" + NL + formatted_add + NL
                    
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(f"---{new_yaml}---{body}")
            files_updated += 1
            links_added += len(to_add)

print(f"Reciprocal Link Densification Complete: {links_added} links added across {files_updated} files.")
