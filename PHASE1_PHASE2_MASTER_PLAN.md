# Atlas Phase 1 + Phase 2 Expansion: Master Plan (~1000 nodes)

**Date Created:** 2026-09-24
**Total Target Nodes:** 1003 nodes across 4 sections
**Execution Model:** Direct agent work (Haiku speed) + batch execution

---

## 📊 Overall Summary

### Current State
| Section | Current | Target | Gap |
|---------|---------|--------|-----|
| Anthropology | 357 | 600 | +243 |
| Historiography | 194 | 400 | +206 |
| Legal-Theory | 139 | 400 | +261 |
| Ethics | 12 | 300 | +288 |
| **TOTAL** | **702** | **1700** | **+998** |

### Phase Structure

**Phase 1 (Initiated):** 454 nodes total
- Anthropology: 357→600 (+243)
- Historiography: 194→400 (+206)

**Phase 2 (Planned):** 549 nodes total
- Legal-Theory: 139→400 (+261)
- Ethics: 12→300 (+288)

**GRAND TOTAL:** 1003 new nodes

---

## ✅ Phase 1: Execution Status

### Anthropology (357→600, +243)

**Batch 1 ✅ COMPLETED**
- Commit: 563d17b7
- 11 schools created (SCH-12377 to SCH-12387)
- 1 concept created (CON-12602)
- **Progress:** 12/243 (5%)

**Remaining:** Batches 2-6 (~231 nodes)
- Batch 2: Fieldwork methods (40 nodes)
- Batch 3: Material culture (45 nodes)
- Batch 4: Kinship systems (50 nodes)
- Batch 5-6: Economics, medicine, urban, applied, linguistic, postcolonial expansion (100 nodes)

**Detailed Backlog:** `agents_specs/phase1-anthropology-backlog.md`

### Historiography (194→400, +206)

**Status:** 0 batches (not yet started)
- 0/206 nodes created
- **Progress:** 0% (waiting for Batch 1)

**Plan:** 11 schools + 195 supporting nodes
- Schools to create: SCH-12388 to SCH-12398
- Batches: 4 batches of 45-50 nodes each

**Detailed Backlog:** `agents_specs/phase1-historiography-backlog.md`

---

## 📋 Phase 2: Detailed Plan

### Legal-Theory (139→400, +261)

**11 New Schools:**
1. SCH-12399: Constitutional Law Theory
2. SCH-12400: Jurisprudence Foundations
3. SCH-12401: Rights Theory
4. SCH-12402: Comparative Legal Systems
5. SCH-12403: International Law
6. SCH-12404: Criminal Law & Punishment
7. SCH-12405: Philosophy of Law
8. SCH-12406: Applied Ethics in Law
9. SCH-12407: Law and Society
10. SCH-12408: Legal History
11. SCH-12409: Feminist Jurisprudence

**Supporting Nodes:** 250 nodes (thinkers, concepts, works, etc.)

**Batches:** 5 batches of 52 nodes each

### Ethics (12→300, +288)

**12 New Schools:**
1. SCH-12410: Virtue Ethics
2. SCH-12411: Consequentialism/Utilitarianism
3. SCH-12412: Deontology (Kantian)
4. SCH-12413: Care Ethics
5. SCH-12414: Comparative Ethics (Eastern/African/Indigenous)
6. SCH-12415: Bioethics & Medical
7. SCH-12416: Environmental Ethics
8. SCH-12417: Business Ethics
9. SCH-12418: Professional Ethics
10. SCH-12419: Metaethics & Moral Realism
11. SCH-12420: Moral Psychology & Development
12. SCH-12421: Ethics, Society & Justice

**Supporting Nodes:** 276 nodes (thinkers, concepts, works, etc.)

**Batches:** 6 batches (60, 50, 50, 45, 45, 38 nodes each)

**Detailed Backlog:** `agents_specs/phase2-legal-ethics-backlog.md`

---

## 🔄 Execution Sequence

### Phase 1 (In Progress)

**✅ Week 1 - Anthropology Batch 1**
- Commit: 563d17b7
- 11 schools + 1 concept
- Status: DONE

**⏳ Week 2-3 - Anthropology Batches 2-6**
- Target: 232 nodes
- Estimated: 1-2 sessions (Haiku speed)

**⏳ Week 4 - Historiography Batches 1-4**
- Target: 206 nodes
- Estimated: 1-2 sessions
- 11 schools + 195 supporting nodes

### Phase 2 (Follows Phase 1)

**⏳ Week 5-6 - Legal-Theory Batches 1-5**
- Target: 261 nodes
- Estimated: 2 sessions
- 11 schools + 250 supporting nodes

**⏳ Week 7-8 - Ethics Batches 1-6**
- Target: 288 nodes
- Estimated: 2 sessions
- 12 schools + 276 supporting nodes

---

## 🛠️ Technical Execution Rules

### Node Creation Standards

**Mandatory Metadata (14 fields):**
1. slug: unique identifier
2. id: prefixed (THK-*, CON-*, WRK-*, SCH-*)
3. type: المنوع
4. part: section name
5. level: متوسط/متقدم/أساسي
6. title: Arabic title
7. en: English title
8. crumb: breadcrumb hierarchy
9. dates/active_start/active_end: temporal
10. country/origin: geographic
11. edges: internal relationships
12. related: external references
13. gaps: documentation notes

### ID Assignment

**Current Allocations:**
- THK: Next available = 12661 (last allocated: 12660)
- CON: Next available = 12734 (last allocated: 12733)
- WRK: Next available = 12491 (last allocated: 12490)
- SCH: Next available = 12399 (after Phase 1 = 12388+)

### Source Verification
- All thinkers/works verified via OpenLibrary or CrossRef
- No fabrication — evidence-based entries only
- Publication dates and titles cross-checked

### Batch Commits
- Format: `جديد القسم: العنوان العربي - Number of nodes`
- Include attribution line: `Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>`
- Explicit paths only — no `-A` flag
- Verify: `git show --stat` confirms files

### Quality Assurance

**After Each Batch:**
1. Run: `python3 scripts/check_content_integrity.py`
2. Run: `python3 scripts/audit_atlas.py`
3. Check for:
   - No duplicate IDs
   - No broken links (all `related` exist)
   - No orphaned nodes
   - All mandatory fields populated
   - Proper encoding (UTF-8 for Arabic)

### Linking Strategy

**Internal (within section):**
- Each school → 3-5 related schools
- Each thinker → 2-4 schools + concepts
- Each concept → parent school + 2-3 related

**Cross-section (between Phase 1 sections):**
- Historiography → Anthropology (where applicable)
- Social anthropology ↔ Historiography concepts
- Method-shared nodes link bidirectionally

**Phase 2 Cross-section:**
- Legal-Theory ↔ Philosophy section (foundations)
- Ethics ↔ Philosophy (Kant, Aristotle, Mill)
- Applied Ethics ↔ Medicine/Psychology sections

---

## 📁 Reference Documents

### Backlogs Created
1. `agents_specs/phase1-anthropology-backlog.md` — 232 remaining nodes, 6 batches
2. `agents_specs/phase1-historiography-backlog.md` — 206 nodes, 4 batches
3. `agents_specs/phase2-legal-ethics-backlog.md` — 549 nodes, 11 batches total

### Scripts Available
- `scripts/phase1_batch_generator.py` — Template generator
- `scripts/phase1_batch_writer.py` — Batch writer utility
- `scripts/check_content_integrity.py` — Validation
- `scripts/audit_atlas.py` — Final audit

---

## ✨ Success Metrics

### Phase 1 Success
- [ ] Anthropology: 600 nodes (357 + 243)
- [ ] Historiography: 400 nodes (194 + 206)
- [ ] All integrity checks pass
- [ ] No broken links
- [ ] All schools + supporting nodes created

### Phase 2 Success
- [ ] Legal-Theory: 400 nodes (139 + 261)
- [ ] Ethics: 300 nodes (12 + 288)
- [ ] All 23 new schools created
- [ ] All cross-section bridges established
- [ ] Final audit: ~1000 nodes added total

### Combined Success Criteria
- **Total Nodes Added:** 1003 (454 Phase 1 + 549 Phase 2)
- **All Sections:** Pass integrity + audit checks
- **Cross-linking:** All bridges established
- **Final State:** 4 sections mature and interconnected

---

## 🎯 Current Session Summary

**Work Completed:**
✅ Anthropology Batch 1 (12 nodes, 5% of Phase 1)
✅ Comprehensive backlogs created (3 documents)
✅ Master plan established

**Next Actions (for future sessions):**
1. Continue Anthropology Batches 2-6 (232 nodes)
2. Execute Historiography Batches 1-4 (206 nodes)
3. Phase 2: Legal-Theory + Ethics (549 nodes)
4. Final verification and cross-linking

**Estimated Timeline to Completion:**
- Phase 1: 2-3 weeks (1-2 sessions remaining)
- Phase 2: 2-3 weeks (2-3 sessions)
- **Total:** 4-6 weeks to 1000 nodes

---

## 📞 Session Handoff Notes

**For Next Session:**
- Start with Phase 1 Anthropology Batch 2
- Use `agents_specs/phase1-anthropology-backlog.md` as reference
- Follow ID allocations established (THK-12589+, CON-12603+, etc.)
- Check concurrent session status before committing
- Use backlog documents as node specifications

**Git State:**
- Last commit: 563d17b7 (Anthropology Batch 1)
- Current branch: main
- No uncommitted Anthropology/Historiography work
- Other sessions may have pending changes (check status)

**Quality Gate:**
All new nodes must pass:
1. `check_content_integrity.py` (no duplicate IDs, all fields present)
2. `audit_atlas.py` (no broken links, proper structure)
3. Manual review (Arabic/English accuracy, conceptual accuracy)

---

## 🔗 Related Documents

- [Atlas Master Plan](./ATLAS_MASTER_PLAN.md) — Overall project scope
- [Anthropology Schools Backlog](./agents_specs/anthropology-schools-backlog.md) — Original schools (completed)
- [Phase 1 Anthropology Details](./agents_specs/phase1-anthropology-backlog.md) — Detailed specs
- [Phase 1 Historiography Details](./agents_specs/phase1-historiography-backlog.md) — Detailed specs
- [Phase 2 Legal-Ethics Details](./agents_specs/phase2-legal-ethics-backlog.md) — Detailed specs
