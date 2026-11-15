# Atlas Translation Rule

**Current decision (2026-11-15): English first. Arabic translation starts only after the
English edition is closed (see `ASTRA_FULL_AUDIT_EN_2026-11-15.md`, Phase 6 → Phase 7).**

- `content/en/` is the source of truth for the English release. Counts are measured by
  `python scripts/check_en_release.py` (writes `reports/en-release-check.json` and
  `reports/en-scope-registry.csv`), never taken from older closeout notes.
- The earlier claim of 65,529 published English term files is **not verified** in this tree
  (`content/en/terms/` holds a single file). Treat the claim as unreconciled until it is matched
  against a manifest or archive (audit P0-01 / P0.2). It is not counted as published content.
- Status vocabulary: `placeholder` / `draft-pending` / `draft-short` / `review-candidate` /
  `reviewed` / `published`. "Not a placeholder" does not mean reviewed.
- Arabic work resumes at Phase 7 from the frozen English edition, preserving ids, slugs and links.

*Supersedes the 2026-09-25 version, which deferred translation and cited the unverified 65,529 figure.*
