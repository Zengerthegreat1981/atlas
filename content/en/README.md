# `content/en/` — English edition (in progress, English-first)

**Status (2026-11-15):** English is the active product; Arabic translation is deferred until the
English edition is closed (audit phases 0–6, then 7). Older "frozen / 130 / 424 placeholders"
statements are historical. Measure, don't quote:

```bash
python scripts/check_en_release.py            # report + reports/en-scope-registry.csv
python scripts/check_en_release.py --strict   # exit 1 while release blockers remain
python scripts/build_atlas.py en --strict     # build; fail on any unreadable frontmatter line
```

## Frontmatter formats read (`scripts/atlas_frontmatter.py`)
1. Compact quoted items: `- id: "x", title: "y", type: "z"`
2. Multi-line YAML items (bare or quoted)
3. Short items without title: `- id: "x", type: "z"` (title resolved from the target node)

Scalars may be quoted, single-quoted or bare; `sources:` / `gaps:` are lists. Unreadable lines are
reported, never silently dropped.

## Status vocabulary
`placeholder` · `draft-pending` · `draft-short` · `review-candidate` · `reviewed` · `published`.
`review-candidate` = no automatic flag only; sources/claims still need human review.

See `reports/EN_STATUS.md` for what this pass did and what remains.
