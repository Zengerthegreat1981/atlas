#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
atlas_frontmatter.py — tolerant, loss-reporting frontmatter reader used by build_atlas.py
and the integrity checks (Audit P0-02).

Supported (all three styles found in content/):
  1. Legacy compact, quoted:      - id: "x", title: "y", type: "z"
  2. Multi-line YAML-ish items:   - id: x
                                    title: y
                                    type: z
  3. Short items without title:   - id: "x", type: "z"        (title resolved later)
Scalar fields may be double-quoted, single-quoted ('' escapes) or bare; integers are
returned as int. Block lists (gaps, sources, any other `key:` followed by `- item`) are
returned as list[str]. `[]` is an empty list.

Nothing is dropped silently: every line that cannot be understood is appended to
`warnings` as (line_no, text), so builders/checkers can fail on it.
"""
import re

LIST_KEYS_STRUCTURED = {"related": ("id", "title", "type"), "edges": ("rel", "target", "target_type")}
_KV_QUOTED = re.compile(r'''([A-Za-z_][\w-]*)\s*:\s*("(?:[^"\\]|\\.)*"|'(?:[^']|'')*')''')
_TOP_KEY = re.compile(r'^([A-Za-z_][\w-]*)\s*:\s*(.*)$')
_ITEM = re.compile(r'^\s*-\s*(.*)$')
_KV_LINE = re.compile(r'^\s*([A-Za-z_][\w-]*)\s*:\s*(.*)$')
_INT = re.compile(r'^-?\d+$')


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1].replace('\\"', '"').replace('\\\\', '\\')
    if len(v) >= 2 and v[0] == "'" and v[-1] == "'":
        return v[1:-1].replace("''", "'")
    return v


def scalar(v):
    raw = v.strip()
    s = unquote(raw)
    if raw == s and _INT.match(s):  # only bare integers become ints
        return int(s)
    return s


def _parse_item_pairs(chunks):
    """chunks: list of text pieces (first item line minus '- ', then continuation lines)."""
    pairs = {}
    bad = []
    for ch in chunks:
        ch = ch.strip()
        if not ch:
            continue
        found = list(_KV_QUOTED.finditer(ch))
        # compact quoted style (possibly several pairs on one line)
        if found and re.sub(r'[\s,]', '', _KV_QUOTED.sub('', ch)) == '':
            for m in found:
                pairs[m.group(1)] = unquote(m.group(2))
            continue
        m = _KV_LINE.match(ch)
        if m:
            pairs[m.group(1)] = unquote(m.group(2))
            continue
        bad.append(ch)
    return pairs, bad


def parse_frontmatter(raw, path=""):
    """Returns (node: dict, warnings: list[(lineno, text)])."""
    node, warnings = {}, []
    lines = raw.split("\n")
    i, n = 0, len(lines)
    last_struct = None  # last related/edges key seen; stray col-0 items after `related: []` attach to it
    stray = {}
    while i < n:
        line = lines[i].rstrip("\r")
        if not line.strip():
            i += 1
            continue
        m = _TOP_KEY.match(line) if not line[0].isspace() else None
        if not m:
            if _ITEM.match(line) and last_struct:
                stray.setdefault(last_struct, []).append([_ITEM.match(line).group(1)])
                # absorb indented continuation lines too
                i += 1
                while i < n and lines[i][:1].isspace() and lines[i].strip() and not _ITEM.match(lines[i]):
                    stray[last_struct][-1].append(lines[i])
                    i += 1
                continue
            warnings.append((i + 1, line))
            i += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        i += 1
        if key in LIST_KEYS_STRUCTURED:
            last_struct = key
        else:
            last_struct = None
        if rest in ("null", "~") and key not in LIST_KEYS_STRUCTURED:
            continue  # bare null == absent
        if rest not in ("",):
            if rest == "[]":
                node[key] = []
            elif key in LIST_KEYS_STRUCTURED:
                warnings.append((i, f"{key}: inline value not supported: {rest[:40]}"))
                node[key] = []
            else:
                node[key] = scalar(rest)
            continue
        # block: gather following list/indented lines
        items = []  # each item = list of chunks
        while i < n:
            l2 = lines[i].rstrip("\r")
            if not l2.strip():
                i += 1
                continue
            im = _ITEM.match(l2)
            if im and (l2[0].isspace() or l2.startswith("-")) :
                items.append([im.group(1)])
                i += 1
            elif l2[0].isspace() and items:
                items[-1].append(l2)  # continuation of a multi-line item
                i += 1
            elif l2.strip() == "[]":
                i += 1
            else:
                break
        if key in LIST_KEYS_STRUCTURED:
            fields = LIST_KEYS_STRUCTURED[key]
            out = []
            for it in items:
                pairs, bad = _parse_item_pairs(it)
                for b in bad:
                    warnings.append((i, f"{key}: unreadable item part: {b[:60]}"))
                key0 = fields[0]
                if key0 not in pairs or not pairs[key0]:
                    warnings.append((i, f"{key}: item without {key0}: {it[0][:60]}"))
                    continue
                row = [pairs.get(f, "") for f in fields]
                out.append(row)
            node[key] = out
        else:
            vals = []
            for it in items:
                txt = it[0] if len(it) == 1 else " ".join(c.strip() for c in it)
                vals.append(unquote(txt))
            node[key] = vals
    for key, its in stray.items():
        fields = LIST_KEYS_STRUCTURED[key]
        for it in its:
            pairs, bad = _parse_item_pairs(it)
            if pairs.get(fields[0]):
                node.setdefault(key, []).append([pairs.get(f, "") for f in fields])
            else:
                warnings.append((0, f"{key}: stray item unreadable: {it[0][:60]}"))
    for k in ("related", "edges", "gaps"):
        node.setdefault(k, [])
    return node, warnings
