# ATLAS DEPTH EXPANSION MASTER PLAN
**Date:** 2026-09-25  
**Status:** Phase 1 In Progress  
**Project Duration:** 4 sequential phases  
**Total Target:** 1,050-1,400 new nodes across 4 disciplines

---

## EXECUTIVE SUMMARY

This master plan coordinates systematic depth expansion of four major academic disciplines within the Atlas knowledge base:

| Discipline | Current | Target | Growth | Phase | Status |
|---|---|---|---|---|---|
| **Historiography** | 566 | 1,100 | +534 | 1 | 🔄 IN PROGRESS |
| **Linguistics** | 830 | 1,300 | +470 | 2 | 📋 QUEUED |
| **Anthropology** | 613 | 1,409 | +796 | 3 | 📋 QUEUED |
| **Sociology** | 1,266 | 1,400+ | +134-200 | 4 | 📋 QUEUED |
| **TOTALS** | **3,275** | **5,200+** | **1,050-1,400** | — | — |

---

## CONTENT STANDARDS (ALL PHASES)

### Word Depth
- Minimum: 1,200 words per node
- Target: 1,200-1,600 words
- No placeholders ("EN TRANSLATION NEEDED", "pending elaboration")

### Structure
- **7+ major sections per node:**
  1. Definition & Overview (150-200 words)
  2. Historical/Theoretical Context (200-250 words)
  3. Key Contributions & Theory (300-400 words)
  4. Theoretical Framework (200-300 words)
  5. Examples & Case Studies (150-200 words)
  6. Contemporary Relevance (100-150 words)
  7. Limitations & Gaps (100-150 words)

### Citations & Sources
- 3-5 authoritative sources per node minimum
- Mix of primary texts and secondary scholarship
- Proper citation format (Author, Year, Title, Publisher)

### Cross-Linking
- 4-6 related concepts per node
- Bidirectional relationships where applicable
- Links to schools, thinkers, works, and methodological concepts

### Bilingual Metadata
- All nodes: Arabic title + English en field
- English body text (substantive, complete)
- Proper YAML frontmatter (14 fields minimum)

---

## PHASE SPECIFICATIONS

Each phase has detailed specifications prepared:

### **PHASE 1: HISTORIOGRAPHY** (300-400 nodes)
**File:** `HISTORIOGRAPHY_PHASE1_SPEC.md`

**Batches:**
- Batch 1A: Ancient Historians (80-100 nodes) — 🔄 IN PROGRESS
- Batch 1B: Medieval & Islamic (60-80 nodes) — 📋 QUEUED
- Batch 1C: Early Modern (60-80 nodes) — 📋 QUEUED
- Batch 1D: Methods & Theory (40-60 nodes) — 📋 QUEUED

**Execution Model:** Sequential commits (40-60 nodes per commit)

---

### **PHASE 2: LINGUISTICS** (300-400 nodes)
**File:** `LINGUISTICS_PHASE2_SPEC.md`

**Batches:**
- Batch 2A: Phonology & Phonetics (80-100 nodes)
- Batch 2B: Semantics & Pragmatics (80-100 nodes)
- Batch 2C: Cognitive & Neurolinguistics (80-100 nodes)
- Batch 2D: Sociolinguistics & Language Variation (60-80 nodes)

**Key Focus:** Language as social, cognitive, and neurobiological phenomenon

---

### **PHASE 3: ANTHROPOLOGY** (300-400 nodes)
**File:** `ANTHROPOLOGY_PHASE3_SPEC.md`

**Batches:**
- Batch 3A: Economic Anthropology (80-100 nodes)
- Batch 3B: Kinship & Family (80-100 nodes)
- Batch 3C: Cultural & Symbolic Anthropology (80-100 nodes)
- Batch 3D: Methods & Epistemology (60-100 nodes)

**Key Focus:** Ethnographic diversity, decolonial perspectives, methodological reflexivity

---

### **PHASE 4: SOCIOLOGY** (150-200 nodes)
**File:** `SOCIOLOGY_PHASE4_SPEC.md`

**Batches:**
- Batch 4A: Classical & Foundational (50 nodes)
- Batch 4B: Specialized Branches & Applied (80 nodes)
- Batch 4C: Contemporary & Critical (60 nodes)
- Batch 4D: Methodological & Epistemological (40 nodes)

**Key Focus:** Contemporary sociology, critical perspectives, public sociology relevance

---

## DIRECTORY STRUCTURE

### Content Organization
```
/Users/mina/Desktop/Atlas/content/en/
├── thinkers/          # Individual scholars/historians
├── schools/           # Historiographical/linguistic/anthropological schools
├── concepts/          # Theoretical concepts, methodologies
├── works/             # Major texts & publications
├── debates/           # Historiographical/theoretical debates
├── branches/          # Sub-disciplines & specialized fields
```

### Node ID Conventions
- **Historiography:** `hst-XXXXX` (ID: HST-XXXXX)
- **Linguistics:** `ling-XXXXX` (ID: LNG-XXXXX)
- **Anthropology:** `ant-XXXXX` (ID: ANT-XXXXX)
- **Sociology:** `soc-XXXXX` (ID: SOC-XXXXX)

### File Naming
- **Thinkers:** `thk-lastname-firstname.md`
- **Concepts:** `con-concept-name.md`
- **Schools:** `sch-school-name.md`
- **Works:** `wrk-short-title.md`

---

## GIT COMMIT STRATEGY

### Per-Batch Commits
**Format:**
```
Phase X Batch Y: [Description]

- X thinker nodes ([names])
- Y concept nodes
- Z methodology/works
- Complete bilingual metadata (Arabic + English)
- 3-5 authoritative sources per node
- 4-6 cross-references per node
- Word depth: 1,200-1,600 per node

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### Commit Frequency
- 40-60 nodes per commit
- Sequential: no parallel batches within a phase
- Phase completion → next phase begins

---

## VALIDATION CHECKLIST

Before each commit, verify:

- [ ] All nodes have unique ID within phase range
- [ ] All nodes have complete YAML frontmatter (14 fields)
- [ ] Word count: 1,200-1,600 per node
- [ ] 7+ major sections per node (Definition, Context, Contributions, Theory, Examples, Relevance, Limitations)
- [ ] 3-5 sources with proper citations
- [ ] 4-6 related concepts linked per node
- [ ] No placeholder text ("EN TRANSLATION NEEDED", "pending elaboration", etc.)
- [ ] Gap documentation explicit and specific
- [ ] Bilingual metadata (Arabic title + English en field)
- [ ] Proper slug convention and ID sequencing
- [ ] YAML syntax valid (parseable)
- [ ] Content is substantive and discipline-specific
- [ ] Cross-links are semantically justified
- [ ] Examples are concrete and informative

---

## QUALITY METRICS

### Target Outcomes
- **Total New Nodes:** 1,050-1,400
- **Total Content Generated:** ~1.5-2.2 million words
- **Unique ID Range:** 4,000+ IDs assigned
- **Cross-Reference Network:** 4,200-8,400 internal links created
- **Source Citations:** 3,150-7,000 authoritative references

### Quality Benchmarks
- **Avg Word Count:** 1,300-1,450 per node
- **Avg Sources:** 3.5-4 per node
- **Avg Cross-Links:** 4.5-5 per node
- **Zero Placeholder Entries:** 100%
- **Bilingual Completeness:** 100%
- **YAML Validity:** 100%

---

## EXECUTION TIMELINE

### Current Status (2026-09-25)
- ✅ Master plan created
- ✅ All phase specifications prepared
- 🔄 Phase 1 Batch 1 generation in progress (Ancient Historiography)

### Expected Timeline
- **Phase 1:** 7-10 days (4 batches, sequential)
- **Phase 2:** 7-10 days (4 batches, sequential)
- **Phase 3:** 10-14 days (4 batches, sequential)
- **Phase 4:** 5-7 days (4 batches, sequential)
- **TOTAL:** 29-41 days estimated

### Flexibility
- Batch size can be adjusted (40-60 range) based on execution speed
- Phase transitions can be accelerated if previous phase completes early
- Quality gates all phases; no compromise on standards

---

## INTEGRATION NOTES

### Cross-Section Linking
- **Historiography ↔ Anthropology:** Ethnographic history, historical anthropology
- **Historiography ↔ Sociology:** Social history, historical sociology
- **Linguistics ↔ Anthropology:** Language and culture, ethnolinguistics
- **Linguistics ↔ Sociology:** Sociolinguistics, language and inequality
- **Anthropology ↔ Sociology:** Comparative social analysis
- **All Sections ↔ Philosophy:** Epistemological foundations, methodology
- **All Sections ↔ Psychology:** Human cognition, behavior, development

### Concurrent Work
- **Note:** Other sessions may be working on AR (Arabic) content
- Git coordination required to avoid conflicts
- Phase execution is sequential within this project
- Other concurrent work on psychology/psychiatry/arab-thought unaffected

---

## SUCCESS CRITERIA

### Phase Completion
✅ All nodes created (target count)
✅ All YAML valid and properly formatted
✅ All word depths meet minimum (1,200 words)
✅ All sections included (7+ per node)
✅ All sources cited (3-5 per node)
✅ All cross-links functional (4-6 per node)
✅ Zero placeholder text remaining
✅ Git commits clean with proper attribution
✅ No duplicate IDs or naming conflicts

### Project Completion
✅ All 4 phases complete
✅ 1,050-1,400 new nodes created
✅ ~1.5-2.2 million words of substantive content
✅ Disciplines depth-expanded: historiography, linguistics, anthropology, sociology
✅ Integration with existing sections (philosophy, psychology, etc.) established
✅ Cross-disciplinary linking network functional
✅ Master consolidation report generated

---

## NOTES FOR EXECUTION

1. **Autonomous Execution:** This project is authorized for autonomous execution with full coordination authority
2. **Quality > Speed:** Maintain content standards even if timeline extends
3. **Documentation:** All gaps explicitly documented in nodes; future work clearly identified
4. **Bilingual:** All nodes must be bilingual-ready (Arabic metadata + English body)
5. **Git Hygiene:** Clean commits, proper attribution, sequential execution
6. **Concurrent Work:** Coordinate with other sessions to avoid conflicts

---

## MASTER PLAN CONTACTS & COORDINATION

**Current Executor:** Claude Haiku 4.5  
**Execution Model:** Multi-agent coordination  
**Authorization Level:** Full autonomy across all phases  
**Status Reporting:** Consolidation reports per phase

---

**Master Plan Status:** ACTIVE  
**Next Action:** Monitor Phase 1 Batch 1 completion, then initiate Phase 1 Batch 2

---

*Master Plan created 2026-09-25*  
*Updated as phases complete*
