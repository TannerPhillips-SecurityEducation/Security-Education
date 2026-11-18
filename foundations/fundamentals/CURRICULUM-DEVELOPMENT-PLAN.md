# Curriculum Development Plan of Action

**Program:** Security Knowledge → Foundations → Fundamentals  
**Document status:** Working plan v1.24; **120/120 substantive articles internally Reviewed (model-assisted)** across Waves A–H, including Wave G depth reviews; none fully source-level Verified or independently Published; none source-level Verified or Published; independent human acceptance pending
**Current inventory:** 12 knowledge areas, **120 authored and Reviewed (model-assisted) subjects** (116 earlier + four Wave H). Historical 109- and 116-heading snapshots remain traceable; count may expand or contract.  
**Source of authority:** [Fundamentals governing architecture](ARCHITECTURE.md), [Fundamentals index](README.md), and the [repository's publication scope](../../README.md)

## Governing Definition and Classification

> Fundamentals establishes domain-agnostic concepts, structures, principles, and mechanisms needed to understand technical systems and their behavior. It supports the seven specialized knowledge domains without making any one technology, vendor, or security practice the organizing principle.

Follow the [approved Fundamentals governing architecture](ARCHITECTURE.md) throughout the program:

- **Domain independence:** Begin with general concepts, not vendor or implementation descriptions.
- **Conceptual and mechanical depth:** Explain concepts, structures, principles, mechanisms, and relationships rather than assembling only definitions.
- **Canonical ownership:** A concept has one general canonical home; specialized areas link to it and develop distinct contextual mechanisms.
- **Specialized extension:** Domain applications build on Fundamentals, without turning Fundamentals into a technology-specific taxonomy.

The **12 approved knowledge areas are navigational disciplines**, and **116 headings form the current, revisable coverage inventory**, not 116 presumed one-to-one concepts or a fixed quota. The knowledge graph captures conceptual relationships across disciplinary boundaries. Illustrative primitives are not a separately approved taxonomy.

## 1. Mission

Develop Fundamentals into a technically accurate, navigable, source-grounded **reference curriculum** that supplies the common concepts required by Network, Endpoint, Application, Cloud, Industrial, IoT, and Identity Knowledge.

Here, *curriculum* means an organized body of reference knowledge with deliberate coverage and conceptual dependencies. It does **not** mean a classroom course or an assessment program.

**Out of scope:** Knowledge Checks, Practical Assessments, quizzes, graded exercises, learner scoring, course schedules, and training certifications. Worked examples are permitted when they clarify concepts. Factual validation and editorial review remain required.

## 2. Starting Position

- **Current working snapshot:** 12 knowledge areas and **120 Reviewed (model-assisted) subjects**, including four added and reviewed under Wave H. The heading count may expand or contract through documented coverage/ownership review.
- **Implemented today:** 12 area READMEs and a Fundamentals index listing their inventories.
- **Implemented for architectural review:** [Canonical Ownership & Relationship Register](CANONICAL-OWNERSHIP-REGISTER.md) maps all **116 currently tracked headings** to conceptual scopes and illustrative links; [Concept Overlap & Coverage Review](CONCEPT-OVERLAP-REVIEW.md) catalogs 20 overlap groups and 10 candidate gaps.
- **Not yet demonstrated:** fully developed canonical references, verified concept-level dependency relationships, complete seven-domain coverage, or satisfaction of all seven completion gates.
- **Unit of work:** A canonical *concept or tightly coherent subject*, not necessarily one file for each inventory heading. Identify the general definition's owner before adding implementations. Some headings may need several canonical entries; others may be adequately covered together. Changes to scope and the canonical map should be recorded before drafting to avoid duplication.

The original 109 headings are a **historical baseline**; the seven additional subjects are documented in [Adjudication 01](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md), yielding 116 tracked subjects. The original count is **not** a maximum, minimum, or final quota. Model- and framework-grounded review may justify added, split, consolidated, or retired subjects.

## Boundary and Gap-Resolution Milestones

The [Coverage Gap Decision Register](COVERAGE-GAP-DECISIONS.md) gives all ten candidate gaps working dispositions: seven assigned to existing approved headings **pending actual authoring**, with three architectural scope decisions unresolved. This is not a claim of complete coverage. The 20 ownership boundaries are approved as conceptual placement guidance, while specific technical claims remain subject to source verification.



The [Canonical Concept Boundary Decisions](CONCEPT-BOUNDARY-DECISIONS.md) record working distinctions for all 20 overlapping concept groups. **This does not close the 10 candidate coverage gaps**, and the general notion of temporality is explicitly open. Use these boundaries during concept authoring while treating the detailed ownership statements as revisable until validated.

## 3. Governing Rules

1. **Hierarchy for navigation; knowledge graph for relationships.** Every canonical subject has a discoverable home, with explicit cross-references to relevant concepts and domain applications.
2. **Domain neutrality.** Define general concepts independently of particular products, vendors, operating systems, or security practices. Domain-specific implementation belongs in its specialized domain.
3. **One canonical definition.** Related pages link to the authoritative explanation instead of silently redefining it.
4. **Evidence over assertion.** Prefer primary specifications, foundational texts, and authoritative technical documentation; cite sources near substantive technical claims. Separate sourced facts from editorial interpretation and illustrative models.
5. **Connected technical prose.** Explain concepts progressively through meaning, distinctions, mechanisms, relationships, and worked examples, rather than filling a glossary with isolated definitions.
6. **No assessments.** No Knowledge Checks or Practical Assessments appear anywhere in this development plan or in the resulting knowledge reference.
7. **Versioned evolution.** Preserve historical identifiers and the presently approved category identities while documenting subject additions, splits, merges, renames, retirements, relocations and corrections. **The subject count is not fixed.**

## Living subject inventory rule

**Clarification, November 18, 2026:** The **initial 109-subject inventory** was always revisable in either direction and has now expanded to **116** through adjudication. New foundational frameworks, models, or architectures may expose missing concepts that warrant extra headings; overlapping or mis-scoped subjects may warrant merges or retirement. Neither growth nor contraction is an achievement by itself. Use [architecture-level versioned change control](ARCHITECTURE.md#living-subject-inventory-and-versioned-change-control), log the rationale, and reconcile the denominators, paths, status evidence and ownership links after an accepted change.

Historical 109/109 Reviewed (model-assisted) refers only to the audited snapshot. Never equate it to automatic review of additions or merged replacements.

## Execution Status: 120/120 authored and internally Reviewed; publication gates open

- **Wave A:** 26/26 subject articles authored and Reviewed (model-assisted).
- **Wave B:** 28/28 subject articles authored and Reviewed (model-assisted).
- **Wave C:** 18/18 subject articles authored and Reviewed (model-assisted).
- **Wave D:** 18/18 subject articles authored and Reviewed (model-assisted), including the [54-family Software & Programming audit](WAVE-D-TECHNICAL-REVIEW-03-04.md).
- **Wave E Operating System Principles:** All ten articles passed the [60-family Wave E OS technical audit](WAVE-E-TECHNICAL-REVIEW-01.md). Corrections addressed MIT OS documentation links and strengthened copy-on-write source grounding; model calculations, canonical boundaries and 35 distinct internal file destinations were checked.
- **Wave E Communication & Distributed Systems:** All nine articles passed the [54-family Wave E Communication technical audit](WAVE-E-TECHNICAL-REVIEW-02.md). Corrections strengthened TCP byte-stream, reserved address/name, linearizability and asynchronous-consensus sources and limits. The mathematical examples and 28 distinct internal file destinations were checked.
- **Wave F authored and internally reviewed:** [Adjudication 01](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md) added seven subjects in four existing areas; all seven now have substantive articles and passed the [42-family Wave F audit](WAVE-F-TECHNICAL-REVIEW-01.md). Source state is Core claims checked, not complete Verified or final Published.
- **Wave G established-model depth pass:** [Wave G 39-family audit](WAVE-G-TECHNICAL-REVIEW-01.md) strengthened 13 existing canonical articles with primary model/standard grounding and explicit limitations. The 116-subject inventory and bounded Review states are unchanged.
- **Wave H source-grounded gap closure:** Four genuinely distinct canonical subjects have been authored and passed the [24-family scoped technical audit](WAVE-H-TECHNICAL-REVIEW-01.md). [Coverage Triage 02](COVERAGE-AND-SOURCE-TRIAGE-02.md) documents boundaries, remaining sources/depth questions and incremental cross-domain link policy.
- **Current portfolio reconciliation:** **120 headings/120 canonical articles internally Reviewed (model-assisted), 0 Draft, 0 Inventoried without article, 0 Published**. The [Development & Verification Register v1.23](DEVELOPMENT-VERIFICATION-REGISTER.md) records separate legacy Wave A–E and Wave F evidence. Core claims checked is not exhaustive source Verified.
- **Preliminary publication-readiness check completed:** [Publication Readiness Audit 01](PUBLICATION-READINESS-AUDIT-01.md) checked the pre-report snapshot of **152 Fundamentals Markdown files**, **2,681 inline relative Markdown-link occurrences**, all twelve area indexes, **109 canonical paths**, and **55 fragment-link occurrences** resolving to 32 distinct heading targets. No missing internal file destinations or heading targets were found within the stated parser and snapshot scope.
- **Publication remains pending:** Execute the seven [Fundamentals completion gates](README.md#completion-gates), especially complete claim-to-source traceability, editorial/technical depth and relationship consistency, external URL/fragment checks, seven-domain coverage and independent qualified human expert peer review.
- **Architecture scope and scoped authoring/review completed:** G-01 mathematical breadth, G-04 general temporality and G-06 AI/ML now have canonical owners and internally Reviewed articles. **Complete source-passage verification and final publication acceptance remain open**. No Knowledge Checks, Practical Assessments, quizzes or mandated vendors were added.

**Next execution:** Move from scoped article-level review to corpus-wide publication-readiness work: stronger source-passage traceability across all 116 articles, external-reference freshness and anchors, model/architecture relationship consistency, seven-domain coverage, editorial depth and qualified independent expert review.

## Architecture Adjudication and New-Subject Execution

The [2026-11-18 model-architecture adjudication](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md) resolved fourteen FMA cases into seven additional subjects and nine deeper-treatment decisions, with no removals and the twelve-area navigation intact. All seven subjects have since been authored and passed the [Wave F 42-family scoped technical audit](WAVE-F-TECHNICAL-REVIEW-01.md). **The 109/109 audited Wave A–E results remain historical**, while Wave F separately substantiates the seven additions. Comprehensive source verification and final publication acceptance remain pending.


**Subsequent deepening:** The [Wave G 39-family technical review](WAVE-G-TECHNICAL-REVIEW-01.md) covers 13 pre-existing subjects associated with the nine deeper-treatment decisions, including modeling notations, architecture, lifecycle standards, transport layering, distributed consistency, measurement uncertainty, provenance, human factors and control. It does not equate a standards citation with full conformance or advance any article to Published.

## 4. Work Packages and Stage Gates

| Stage | Work package | Required deliverable | Exit criterion |
| --- | --- | --- | --- |
| P0 | Baseline and scope | Confirmed inventory and domain boundaries | All 12 areas and 109 original headings traceable |
| P1 | Coverage architecture | Canonical-subject register, scope notes, and provisional dependencies | Each heading maps to at least one intended canonical explanation; gaps and overlaps flagged |
| P2 | Source acquisition | Reference list and source notes for each subject | Credible sources identified for claims requiring external verification |
| P3 | Canonical authoring | Coherent technical reference content | Definition, distinctions, mechanisms, relationships, examples, and references present as applicable |
| P4 | Concept integration | Cross-links and revised neighboring pages | Definitions and relationships agree; no unintended duplicates or orphaned references |
| P5 | Technical and editorial review | Review findings and resolved corrections | Material factual claims checked, prose clear, boundaries respected |
| P6 | Publication and navigation | Merged canonical pages and linked indexes | Navigation resolves and published pages meet quality criteria |
| P7 | Final coverage audit and maintenance | Seven-domain coverage review, gap register, and update policy | All seven approved completion gates satisfied or explicit exceptions remain open |

These stages can overlap for different subjects. P7 cannot be declared complete while required gaps, unresolved factual disputes, or broken navigation remain.

## 5. Production Waves

The following waves organize **authoring dependencies**, not a mandatory order in which readers must study the repository.

| Wave | Knowledge areas | Inventory headings | Purpose |
| --- | --- | ---: | --- |
| A: Conceptual primitives | Mathematics & Logic (8); Scientific & Analytical Reasoning (8); Models & Abstraction (10) | **26** | Establish distinction, representation, inference, evidence, and formal relationships |
| B: Information and systems | Information & Data (9); Systems & Engineering (11); Human & Sociotechnical Systems (8) | **28** | Connect models to information, composed systems, and the humans operating them |
| C: Physical foundations | Physical & Electrical Principles (9); Digital Systems & Hardware (9) | **18** | Explain physical signals, digital representation, computing hardware, and device interaction |
| D: Executable systems | Computation & Algorithms (9); Software & Programming (9) | **18** | Establish algorithms, program behavior, software structure, and runtime mechanisms |
| E: Managed and distributed execution | Operating System Principles (10); Communication & Distributed Systems (9) | **19** | Extend computing into resource-managed execution and communicating systems |
| **Total** | **12 areas** | **109** | **All initial subject headings accounted for** |

**Cross-wave rule:** If a later concept is required to explain an earlier one, provide a concise scoped introduction and a forward link, rather than duplicating or prematurely completing the later article. Authoring sequence may be revised in light of discovered dependencies.

## 6. Repeatable Canonical-Subject Workflow

Use the same process for each canonical subject:

1. **Locate:** Decide its canonical home, distinguish general concepts from domain-specific realizations, and identify which inventory headings it satisfies.
2. **Bound:** Record its scope, adjacent concepts, exclusions, and dependency assumptions.
3. **Research:** Gather authoritative references and compare relevant definitions; note material uncertainty, scope differences, and disagreement.
4. **Draft:** Write connected technical prose that satisfies the six-part editorial contract.
5. **Relate:** Add explicit, human-readable links to foundational and specialized knowledge without inventing a mandatory graph schema.
6. **Inspect:** Review conceptual accuracy, internal consistency, technical terminology, examples, clarity, and citations.
7. **Publish:** Merge the page, update indexes, verify relative links, and mark its review state.
8. **Maintain:** Record corrections and review when specifications, technologies, or knowledge relationships change.

A heading is **not complete** merely because it has a directory, README, placeholder, or list entry.

### Six-part editorial contract

Each canonical reference includes, as applicable:

- **Definition and scope:** What the concept is and its limits.
- **Distinctions:** How it differs from nearby or commonly conflated concepts.
- **Mechanisms:** How it behaves, operates, or is derived.
- **Relationships:** Dependencies and associations, with links to canonical locations.
- **Examples:** Concrete illustrations that illuminate the mechanism without becoming an assessment.
- **References:** Credible sources supporting relevant factual claims.

The format can vary with the subject. Mathematical, physical, computational, and sociotechnical concepts do not all require identical section lengths or examples.

## 7. Review and Acceptance Criteria

Use the approved **seven completion gates**:

| Gate | Evidence required |
| --- | --- |
| Architecture | Every knowledge area has a defined scope and approved inventory |
| Coverage | All essential shared concepts needed by the seven domains have canonical homes |
| Consistency | No unresolved contradictory or unnecessary duplicate canonical definitions |
| Relationships | Relevant dependencies, prerequisites, and cross-domain references are linked |
| Explanations | Required concepts have substantive definitions, distinctions, mechanisms, and examples |
| Verification | Material technical claims are reviewed against credible references |
| Navigation | Every canonical subject can be discovered without a fixed reading sequence; links resolve |

**Review outcomes:** Ready to publish; revise; blocked by missing sources; or requires an architectural decision. These are workflow states, not an approved ontology for security knowledge.

Do not claim *Fundamentals complete* based on a percentage of inventory headings alone. The seven gates and the cross-domain gap review determine completion.

## 8. Coverage and Progress Tracking

The [Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) is implemented and distinct from the [ownership register](CANONICAL-OWNERSHIP-REGISTER.md). Keep the live progress register updated for every authored article, source review, unresolved relationship, and pending scope decision. Its required fields are:

| Field | Purpose |
| --- | --- |
| Approved area and inventory heading | Preserves traceability to the 109-heading baseline |
| Canonical document link | Identifies where its general concept is authoritatively explained and distinguishes contextual implementations |
| Scope / dependencies | Makes boundaries and prerequisite concepts explicit |
| Development state | Inventoried → Scoped → Researched → Drafted → Reviewed → Published |
| Source verification | Records whether substantive technical claims have been checked |
| Cross-domain relevance | Notes which of the seven knowledge domains depend on the subject |
| Outstanding work | Captures factual disputes, gaps, corrections, and unresolved relationships |

Measure and report **heading coverage**, **canonical entries published**, **verified entries**, **unresolved gaps**, and **broken/orphaned links** separately. Do not treat an index heading as a published reference or equate a published page with a verified page.

## 9. Cross-Domain Integration Audit

After each wave, compare its concepts against existing or planned content in all seven specialized domains:

- **Network:** communication, models, addressing, measurements, systems.
- **Endpoint:** hardware, execution, memory, operating systems.
- **Application:** algorithms, software, information, interfaces.
- **Cloud:** distributed systems, resources, software, systems engineering.
- **Industrial:** physical principles, instrumentation, control, reliability.
- **IoT:** sensing, embedded computation, device communication.
- **Identity:** formal logic, identity and distinction, information, systems, human context.

Identify missing shared concepts, duplicated definitions, misleading parent-child assumptions, and implementation-specific material incorrectly placed in Fundamentals. Record proposed taxonomy changes for review rather than silently expanding the approved structure.

## 10. Publication Workflow

- **Working branch or pull request:** Develop individual subject or bounded subject group changes independently where practical.
- **Review:** Check conceptual scope, technical claims, citations, internal consistency, and link resolution before merge.
- **Canonical index update:** Link accepted content from its knowledge-area README and, where useful, from related domains.
- **Release notes:** Summarize significant new coverage, changed definitions, corrections, and known gaps.
- **Maintenance triggers:** New authoritative specifications, corrected technical claims, newly approved domains or functions, substantial technology shifts, or identified broken references.

No graph database or universal front-matter schema is required at this stage. Preserve the existing Markdown-based relationship conventions until a separate schema is approved.

## 11. Risks and Controls

| Risk | Control |
| --- | --- |
| Unbounded scope changes | Maintain a versioned historical 109-heading baseline; assess additions, consolidation and retirements against model-grounded coverage and canonical ownership before adoption |
| Duplicate or conflicting definitions | One canonical home, explicit cross-links, and consistency review |
| Superficial completion | Apply the six-part editorial contract and seven completion gates |
| Vendor-specific drift | Preserve domain-neutral explanations; move implementation detail to specialized domains |
| Unsourced claims | Keep source notes and block publication of unresolved material technical assertions |
| Rigid study sequence | Production waves guide authors; navigation remains non-linear |
| Unbounded planning | Pilot a small cross-area sample, calibrate review criteria, then scale wave by wave |

## 12. Execution History and Next Actions

1. **Completed:** Approved Fundamentals definition and preserved 12 knowledge areas and 109 subject headings.
2. **Completed:** Canonical ownership map, twenty conceptual boundaries, and ten coverage-gap dispositions with three open scope decisions.
3. **Completed:** Six pilot references and 50-family internal source audit.
4. **Completed:** Wave A Batch 01–06 source reviews (21, 27, 24, 24, 24 and 24 claim families).
5. **Completed:** Three Wave A Batch 06 references passed scoped model-assisted review; [24-family audit](WAVE-A-TECHNICAL-REVIEW-06.md).
6. **Completed authoring:** Five Wave A Batch 07 drafts cover Units and Quantities; Validation and Falsification; Ontologies and Taxonomies; Schemas; Conceptual and Formal Models. **Review gate completed:** [Batch 07 technical audit](WAVE-A-TECHNICAL-REVIEW-07.md); **source state:** Core claims checked. Independent human acceptance and corpus-wide publication gates remain open.
7. **Completed:** Wave B Information & Data, nine references, internally Reviewed after [Batches 01](WAVE-B-TECHNICAL-REVIEW-01.md) and [02](WAVE-B-TECHNICAL-REVIEW-02.md).
8. **Completed:** Wave B Batch 03 [24-family audit](WAVE-B-TECHNICAL-REVIEW-03.md) and Batch 04 [36-family audit](WAVE-B-TECHNICAL-REVIEW-04.md); Systems & Engineering is 11/11 internally Reviewed.
9. **Completed:** Eight Human & Sociotechnical Systems articles passed the [Wave B Batch 05 48-family audit](WAVE-B-TECHNICAL-REVIEW-05.md), completing Wave B internal review (28/28).
10. **Completed:** Four Wave C Batch 01 references passed the [24-family scoped technical audit](WAVE-C-TECHNICAL-REVIEW-01.md).
11. **Completed:** Four Wave C Batch 02 articles passed the [24-family technical audit](WAVE-C-TECHNICAL-REVIEW-02.md), with an exact aliasing-example correction.
12. **Completed:** Wave C Batch 03's nine articles passed the [54-family technical audit](WAVE-C-TECHNICAL-REVIEW-03.md). Wave C is 18/18 internally Reviewed.
13. **Completed:** The four Wave D Batch 01 references passed the [24-family scoped review](WAVE-D-TECHNICAL-REVIEW-01.md).
14. **Completed:** Five Wave D Batch 02 articles passed the [30-family scoped technical review](WAVE-D-TECHNICAL-REVIEW-02.md); Computation & Algorithms is 9/9 internally Reviewed.
15. **Completed:** Nine Software & Programming articles passed the [54-family Wave D Software Batches 03–04 technical audit](WAVE-D-TECHNICAL-REVIEW-03-04.md); Wave D is 18/18 internally Reviewed.
16. **Completed:** Wave E's ten Operating System Principles articles passed the [60-family scoped technical audit](WAVE-E-TECHNICAL-REVIEW-01.md).
17. **Completed:** Wave E's nine Communication & Distributed Systems articles passed the [54-family scoped technical audit](WAVE-E-TECHNICAL-REVIEW-02.md). All **109/109 Fundamentals headings** are authored and internally Reviewed (model-assisted).
18. **Completed preliminary navigation verification:** [Publication Readiness Audit 01](PUBLICATION-READINESS-AUDIT-01.md) recorded 152 files, 2,681 relative-link occurrences, zero missing file targets, and 32 valid distinct fragment targets.
19. **Completed scoped Wave F review:** Seven model-grounded additional subjects were authored and passed the [Wave F Technical Review 01](WAVE-F-TECHNICAL-REVIEW-01.md) (42 material claim groups). The **116-heading inventory** remains not publication-complete until the Fundamentals gates, full source evidence and independent acceptance are satisfied.

Production waves guide authors, **not reader prerequisites**. Knowledge Checks and Practical Assessments remain excluded.

## 13. Reference and Governance Links

- [Fundamentals governing architecture](ARCHITECTURE.md)
- [Canonical Ownership & Relationship Register](CANONICAL-OWNERSHIP-REGISTER.md)
- [Concept Overlap & Coverage Review](CONCEPT-OVERLAP-REVIEW.md)
- [Canonical Concept Boundary Decisions](CONCEPT-BOUNDARY-DECISIONS.md)
- [Coverage Gap Decision Register](COVERAGE-GAP-DECISIONS.md)
- [Development & Verification Register (116 tracked headings)](DEVELOPMENT-VERIFICATION-REGISTER.md)
- [Six-Pilot Technical and Editorial Review](PILOT-TECHNICAL-REVIEW.md)
- [Pilot Claim-to-Source Audit (50 claim families)](PILOT-CLAIM-SOURCE-AUDIT.md)
- [Wave A Batch 01 Claim-to-Source Review (21 families)](WAVE-A-TECHNICAL-REVIEW-01.md)
- [Wave A Batch 02 Claim-to-Source Review (27 families)](WAVE-A-TECHNICAL-REVIEW-02.md)
- [Wave A Batch 03 Claim-to-Source Review (24 families)](WAVE-A-TECHNICAL-REVIEW-03.md)
- [Wave A Batch 04 Claim-to-Source Review (24 families)](WAVE-A-TECHNICAL-REVIEW-04.md)
- [Wave A Batch 05 Claim-to-Source Review (24 families)](WAVE-A-TECHNICAL-REVIEW-05.md)
- [Wave A Batch 06 Claim-to-Source Review (24 families)](WAVE-A-TECHNICAL-REVIEW-06.md)
- [Wave A Batch 07 Claim-to-Source Review (30 families)](WAVE-A-TECHNICAL-REVIEW-07.md)
- [Wave B Batch 01 Claim-to-Source Review (24 families)](WAVE-B-TECHNICAL-REVIEW-01.md)
- [Wave B Batch 02 Claim-to-Source Review (24 families)](WAVE-B-TECHNICAL-REVIEW-02.md)
- [Wave B Batch 03 Claim-to-Source Review (24 families)](WAVE-B-TECHNICAL-REVIEW-03.md)
- [Wave B Batch 04 Claim-to-Source Review (36 families)](WAVE-B-TECHNICAL-REVIEW-04.md)
- [Wave B Batch 05 Claim-to-Source Review (48 families)](WAVE-B-TECHNICAL-REVIEW-05.md)
- [Wave C Batch 01 Claim-to-Source Review (24 families)](WAVE-C-TECHNICAL-REVIEW-01.md)
- [Wave C Batch 02 Claim-to-Source Review (24 families)](WAVE-C-TECHNICAL-REVIEW-02.md)
- [Wave C Batch 03 Claim-to-Source Review (54 families)](WAVE-C-TECHNICAL-REVIEW-03.md)
- [Wave D Batch 01 Claim-to-Source Review (24 families)](WAVE-D-TECHNICAL-REVIEW-01.md)
- [Wave D Batch 02 Claim-to-Source Review (30 families)](WAVE-D-TECHNICAL-REVIEW-02.md)
- [Wave D Software Batches 03–04 Claim-to-Source Review (54 families)](WAVE-D-TECHNICAL-REVIEW-03-04.md)
- [Wave E Authoring Verification (19 draft references)](WAVE-E-AUTHORING-VERIFICATION.md)
- [Wave E Operating System Principles Technical Review (60 claim families)](WAVE-E-TECHNICAL-REVIEW-01.md)
- [Wave E Communication & Distributed Systems Technical Review (54 claim families)](WAVE-E-TECHNICAL-REVIEW-02.md)
- [Wave F Model & Architecture References Technical Review (42 claim families)](WAVE-F-TECHNICAL-REVIEW-01.md)
- [Wave G Established Models & Frameworks Depth Review (39 claim families)](WAVE-G-TECHNICAL-REVIEW-01.md)
- [Wave H Four Source-Grounded Gap References (24 claim families)](WAVE-H-TECHNICAL-REVIEW-01.md)
- [Publication Readiness Audit 01: Corpus Inventory and Internal Navigation](PUBLICATION-READINESS-AUDIT-01.md)
- [Fundamentals approved index](README.md)
- [Foundations divisions](../README.md)
- [Knowledge relationship conventions](../../RELATIONSHIPS.md)
- [Security Knowledge publication scope](../../README.md)
- [ACM/IEEE-CS/AAAI CS2023 knowledge areas](https://csed.acm.org/knowledge-areas/)
- [Computing Curricula recommendations](https://www.acm.org/education/curricula-recommendations)
- [Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)

**Current document state:** This is an actionable, committed *working plan*, not a declaration that the proposed process, pilot sequence, or all reference content is already ratified or completed.
