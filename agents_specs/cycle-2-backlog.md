# Cycle 2 Backlog — 2026-08-24 onwards

> المهام المتراكمة بعد Cycle 5 (2026-08-24). استخدم هذا الـbacklog في الـplanning للدورة القادمة.

## Status
- **Current cycle**: 5 (2026-08-24) — mostly complete
- **Next cycle**: 6 — to start
- **Backlog owner**: Atlas root session

## High-priority (next cycle)

### H1. Complete thinker audit (L1.1 carry-over)
- **Goal**: read the 1,166 remaining thinkers in `scripts/audit_unread_thinkers.txt`
- **Method**: 28-file batches, add fixes to `scripts/thinkers_audit_fixes.json`, then `reapply`
- **Expected**: 4-6 fixes per file, ~5,000-7,000 total fixes
- **Effort**: 6-8 hours with 4 background workers
- **Deliverable**: empty `audit_unread_thinkers.txt`

### H2. Bridge section expansion (L3.4)
- **Goal**: reclassify 12 candidates from `agents_specs/bridge-candidates-2026-08-24.json` to `part: bridge`
- **Candidates include**: William James, Antonio Damasio, Pierre Bourdieu, Eric Kandel, etc.
- **Method**: For each, update `part:` field and add `bridge` to the `edges` if not present
- **Effort**: 1 hour + 30 min human review

### H3. Slug/identity conflict review (L1.3)
- **Goal**: review the 30 documented conflicts and decide per case
- **File**: `agents_specs/slug-identity-conflicts-2026-08-24.md`
- **Decisions needed**: keep slug as-is, rename slug, or rename en
- **Effort**: 1 hour with human

## Medium-priority

### M1. Re-run density boost on the new content from background workers
- **When**: After H1 (audit) and the workers complete
- **Goal**: bring density of any newly-added weak files up to ≥4 related
- **Method**: re-run `scripts/atlas_density_boost.py --apply`
- **Effort**: 30 minutes

### M2. Implement bidirectional links for asymmetric pairs
- **Current state**: 8,181 asymmetric pairs (mostly thinker→concept which is one-way by design)
- **Goal**: review and either accept asymmetry (mark as expected) or add reverse links
- **File**: `agents_specs/bidirectional-audit-2026-08-24.md`
- **Effort**: 2-3 hours

### M3. Continue school expansion
- **Current state**: 319 schools with ≤2 thinkers
- **Goal**: add 3-5 thinkers to each "high-priority" weak school
- **Method**: per-school lists compiled from `agents_specs/school-gap-analysis-2026-08-24.md`
- **Effort**: 10-15 hours with 4-6 background workers

### M4. Expand to new types
- **Currently missing or thin**: rituals, archetypes (some schools), case studies
- **Goal**: 50+ new files across underrepresented types
- **Method**: background workers
- **Effort**: 4-6 hours

## Low-priority (deferred)

### L1. English translation
- Status: deferred per PROJECT_PLAN §5.6
- Method: re-evaluate when content stabilizes

### L2. Schema migration
- The YAML flow-style syntax is fragile; consider moving to a DB
- Defer until content reaches 10,000+ items

## Quick wins (≤30 min)

- [ ] Re-run `python3 scripts/build_atlas.py ar` to confirm no build errors
- [ ] Update EXISTING_SLUGS.md after the workers complete
- [ ] Verify the new cross-school relations have proper incoming references
- [ ] Add a `README.md` for the scripts/ folder documenting the pipeline
- [ ] Set up a cron self-reminder to check on background workers every 30 min

## Definition of Done for Cycle 6

1. All 1,166 unread thinkers processed (H1).
2. Bridge section has 5+ thinkers (H2).
3. All 30 slug conflicts resolved (H3).
4. New content from background workers integrated (M1, M3, M4).
5. 0 phantoms, 0 orphans, 0 duplicates maintained.
6. AUDIT_HANDOFF.md updated with Cycle 6 results.
7. Network centrality report shows top-3 hubs still healthy (>1000 degree each).

## Risks

- Background workers may produce inconsistent content — needs human sampling.
- New content may break the orphan=0 invariant — need to re-audit.
- Bridge reclassification may surface more `part: philosophy` ↔ `bridge` confusion.

