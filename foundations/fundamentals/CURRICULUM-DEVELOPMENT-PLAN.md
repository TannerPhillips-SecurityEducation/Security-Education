# Curriculum Development Plan of Action

**Program:** Security Knowledge → Foundations → Fundamentals  
**Document status:** Working plan v0.1, proposed for review  
**Baseline:** 12 approved knowledge areas; 109 inventoried subject headings  
**Source of authority:** [Fundamentals index](README.md) and the [repository's publication scope](../../README.md)

## 1. Mission

Develop Fundamentals into a technically accurate, navigable, source-grounded **reference curriculum** that supplies the common concepts required by Network, Endpoint, Application, Cloud, Industrial, IoT, and Identity Knowledge.

Here, *curriculum* means an organized body of reference knowledge with deliberate coverage and conceptual dependencies. It does **not** mean a classroom course or an assessment program.

**Out of scope:** Knowledge Checks, Practical Assessments, quizzes, graded exercises, learner scoring, course schedules, and training certifications. Worked examples are permitted when they clarify concepts. Factual validation and editorial review remain required.

## 2. Starting Position

- **Approved structure:** 12 knowledge areas containing 109 subject headings.
- **Implemented today:** 12 area READMEs and a Fundamentals index listing their inventories.
- **Not yet demonstrated:** 109 fully developed canonical references, a verified dependency/relationship map, complete seven-domain coverage, or satisfaction of all seven completion gates.
- **Unit of work:** A canonical *concept or tightly coherent subject*, not necessarily one file for each inventory heading. Some headings may need several canonical entries; others may be adequately covered together. Changes to scope and the canonical map should be recorded before drafting to avoid duplication.

The 109 headings are the **initial coverage baseline**, not proof that no additional foundational concepts will be needed.

## 3. Governing Rules

1. **Hierarchy for navigation; knowledge graph for relationships.** Every canonical subject has a discoverable home, with explicit cross-references to relevant concepts and domain applications.
2. **Domain neutrality.** Define general concepts independently of particular products, vendors, operating systems, or security practices. Domain-specific implementation belongs in its specialized domain.
3. **One canonical definition.** Related pages link to the authoritative explanation instead of silently redefining it.
4. **Evidence over assertion.** Prefer primary specifications, foundational texts, and authoritative technical documentation; cite sources near substantive technical claims. Separate sourced facts from editorial interpretation and illustrative models.
5. **Connected technical prose.** Explain concepts progressively through meaning, distinctions, mechanisms, relationships, and worked examples, rather than filling a glossary with isolated definitions.
6. **No assessments.** No Knowledge Checks or Practical Assessments appear anywhere in this development plan or in the resulting knowledge reference.
7. **Versioned evolution.** Preserve approved category identities while documenting proposed additions, merges, relocations, and corrections before changing canonical structure.

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

1. **Locate:** Decide its canonical home and identify which inventory headings it satisfies.
2. **Bound:** Record its scope, adjacent concepts, exclusions, and dependency assumptions.
3. **Research:** Gather authoritative references and compare relevant definitions; note material uncertainty or disagreement.
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

Maintain a lightweight **coverage register** (future deliverable; not yet created) with, at minimum:

| Field | Purpose |
| --- | --- |
| Approved area and inventory heading | Preserves traceability to the 109-heading baseline |
| Canonical document link | Identifies where the subject is authoritatively explained |
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
| Expanding scope without closure | Maintain the 109-heading baseline and record additions in a separate proposed-gap list |
| Duplicate or conflicting definitions | One canonical home, explicit cross-links, and consistency review |
| Superficial completion | Apply the six-part editorial contract and seven completion gates |
| Vendor-specific drift | Preserve domain-neutral explanations; move implementation detail to specialized domains |
| Unsourced claims | Keep source notes and block publication of unresolved material technical assertions |
| Rigid study sequence | Production waves guide authors; navigation remains non-linear |
| Unbounded planning | Pilot a small cross-area sample, calibrate review criteria, then scale wave by wave |

## 12. Initial Action Order

1. **Ratify the plan's process** as a working method without altering the already-approved 12-area taxonomy.
2. **Build the 109-heading coverage register** from the existing area READMEs, preserving their wording and links.
3. **Perform a duplication-and-dependency pass** across the register, identifying canonical concept candidates and unresolved overlaps.
4. **Pilot six representative references**: *Sets and relations*, *Observation*, *Entities and attributes*, *Symbols and encoding*, *Systems and subsystems*, and *Digital logic*. Use this pilot to calibrate narrative depth, source rigor, and cross-links.
5. **Review the pilot**, resolve editorial and architectural problems, and then develop Wave A through Wave E.
6. **Audit each wave** for source accuracy, concept relationships, navigation, and relevance to all seven domains.
7. **Run the final seven-gate review** before identifying Fundamentals as complete.

The six pilot topics are **proposed production choices**, not new categories or changes to the approved inventory.

## 13. Reference and Governance Links

- [Fundamentals approved index](README.md)
- [Foundations divisions](../README.md)
- [Knowledge relationship conventions](../../RELATIONSHIPS.md)
- [Security Knowledge publication scope](../../README.md)
- [ACM/IEEE-CS/AAAI CS2023 knowledge areas](https://csed.acm.org/knowledge-areas/)
- [Computing Curricula recommendations](https://www.acm.org/education/curricula-recommendations)
- [Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page)

**Current document state:** This is an actionable, committed *working plan*, not a declaration that the proposed process, pilot sequence, or all reference content is already ratified or completed.
