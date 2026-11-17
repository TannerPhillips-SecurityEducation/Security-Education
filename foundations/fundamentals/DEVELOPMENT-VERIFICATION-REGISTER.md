# Fundamentals: Development and Verification Register

**Working edition:** v0.3  
**Scope:** 12 approved knowledge areas and exactly 109 approved subject headings, transcribed from the [area inventories](README.md).  
**Purpose:** Track authoring, source validation, relationships, canonical article paths, and outstanding architecture decisions without overstating completion.

## Interpretation and status

- **Inventoried:** Approved heading exists in its area index, but no canonical subject article is yet claimed.
- **Pilot queued:** One of the six approved first authoring targets; a queued article is **not** published or technically validated.
- **Draft:** Substantive article has been committed and can be reviewed; not necessarily source-verified or accepted.
- **Reviewed:** Technical and editorial review passed, with evidence documented.
- **Published:** Canonical reference accepted under the [seven completion gates](README.md#completion-gates), including link and source checks. A commit alone does **not** constitute this status.

**Source review** is tracked separately from development state: **Not reviewed**, **References listed**, **Core claims checked**, or **Verified**. *References listed* indicates linked sources. *Core claims checked* means a documented second-pass source review and example checks occurred, but does not establish complete claim-to-source verification or independent human acceptance. *Verified* requires evidence of a complete scoped technical acceptance review. **Relationship state:** The separate [109-heading canonical ownership register](CANONICAL-OWNERSHIP-REGISTER.md) proposes one conceptual link per heading; those link descriptions are not a fully verified graph.

**IDs are administrative tracking identifiers only**, not a ratified formal ontology, graph predicate set, or new knowledge-category taxonomy. No Knowledge Checks, Practical Assessments, or quizzes will appear in this repository.

## Portfolio-wide progress

| Measure | Initial baseline |
| --- | ---: |
| Approved knowledge areas | 12 |
| Approved subject headings | 109 |
| Initial authoring pilot targets | 6 |
| Initially completed canonical articles | 0 |
| Initially source-verified canonical articles | 0 |
| Architectural gap decisions still requiring explicit scope approval | 3 (G-01, G-04, G-06) |
| Concept overlap boundaries | 20 approved at architectural level; article-level verification remains |

> The table above is the baseline **at initial register creation**. Current item states are below and must be updated as authoring proceeds.

## Current progress after six pilot drafts

| State | Subject headings | Evidence |
| --- | ---: | --- |
| Draft articles committed | **6** | Linked from their area indexes and this register |
| Inventoried headings without canonical articles | **103** | Retained in approved subject inventories |
| Core-claim source-checks documented for pilot articles | **6** | [Pilot Technical Review](PILOT-TECHNICAL-REVIEW.md); final full claim-to-source validation pending |
| Fully verified or independently accepted pilot articles | **0** | Final technical/editorial acceptance not yet claimed |
| Accepted as final published reference | **0** | Publication gate still pending |

**Interpretation:** The six pilots are real GitHub files containing substantive prose and examples; they are not merely queued. Their existence advances the authoring stage, but does not demonstrate comprehensive source verification or closure of the seven Fundamentals completion gates.

## Pilot review record

The six substantive draft articles received a second-pass [technical and editorial review](PILOT-TECHNICAL-REVIEW.md). The review confirmed core mathematical examples, Unicode encoding/normalization cases, circuit truth tables, and technical scope distinctions, and corrected misleading statements and stale citations. All six remain **Draft**. A documented human acceptance and complete final source-to-claim review have **not** been recorded, so none is marked **Verified** or **Published**.

## Detailed coverage by approved knowledge area

### 01. Mathematics & Logic (Wave A; 8 headings)

**Area index:** [Mathematics & Logic](mathematics-logic/README.md). **Coverage questions:** [G-01](COVERAGE-GAP-DECISIONS.md#g-01-linear-algebra-geometry-topology), [G-02](COVERAGE-GAP-DECISIONS.md#g-02-numerical-methods-and-optimization), [G-03](COVERAGE-GAP-DECISIONS.md#g-03-formal-methods-and-model-checking). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-01-01 | Numbers and numerical systems | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-01-02 | Sets and relations | [Draft article](mathematics-logic/sets-and-relations.md) | Draft | Core claims checked | [Pilot technical review](PILOT-TECHNICAL-REVIEW.md); final acceptance pending |
| F-01-03 | Boolean and predicate logic | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-01-04 | Algebra and functions | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-01-05 | Discrete mathematics | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-01-06 | Graph theory | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-01-07 | Probability and statistics | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-01-08 | Units and quantities | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 02. Scientific & Analytical Reasoning (Wave A; 8 headings)

**Area index:** [Scientific & Analytical Reasoning](scientific-analytical-reasoning/README.md). **Coverage questions:** [G-02](COVERAGE-GAP-DECISIONS.md#g-02-numerical-methods-and-optimization), [G-07](COVERAGE-GAP-DECISIONS.md#g-07-data-quality-and-semantics), [G-09](COVERAGE-GAP-DECISIONS.md#g-09-scientific-and-engineering-validation). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-02-01 | Observation | [Draft article](scientific-analytical-reasoning/observation.md) | Draft | Core claims checked | [Pilot technical review](PILOT-TECHNICAL-REVIEW.md); final acceptance pending |
| F-02-02 | Measurement | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-02-03 | Evidence | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-02-04 | Hypotheses and experiments | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-02-05 | Deduction, induction, and abduction | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-02-06 | Causality and correlation | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-02-07 | Uncertainty and confidence | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-02-08 | Validation and falsification | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 03. Models & Abstraction (Wave A; 10 headings)

**Area index:** [Models & Abstraction](models-abstraction/README.md). **Coverage questions:** [G-03](COVERAGE-GAP-DECISIONS.md#g-03-formal-methods-and-model-checking), [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-03-01 | Entities and attributes | [Draft article](models-abstraction/entities-and-attributes.md) | Draft | Core claims checked | [Pilot technical review](PILOT-TECHNICAL-REVIEW.md); final acceptance pending |
| F-03-02 | Identity and distinction | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-03 | Relationships | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-04 | Boundaries | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-05 | Abstraction | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-06 | Classification | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-07 | Ontologies and taxonomies | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-08 | Schemas | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-09 | State, events, and transitions | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-03-10 | Conceptual and formal models | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 04. Physical & Electrical Principles (Wave C; 9 headings)

**Area index:** [Physical & Electrical Principles](physical-electrical-principles/README.md). **Coverage questions:** [G-05](COVERAGE-GAP-DECISIONS.md#g-05-signal-processing). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-04-01 | Matter and energy | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-02 | Electricity | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-03 | Electrical circuits | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-04 | Electronics | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-05 | Analog and digital signals | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-06 | Waves and frequency | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-07 | Sensors and actuators | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-08 | Signal conversion | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-04-09 | Physical control mechanisms | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 05. Information & Data (Wave B; 9 headings)

**Area index:** [Information & Data](information-data/README.md). **Coverage questions:** [G-07](COVERAGE-GAP-DECISIONS.md#g-07-data-quality-and-semantics), [G-10](COVERAGE-GAP-DECISIONS.md#g-10-lifecycle-evolution-and-versioning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-05-01 | Symbols and encoding | [Draft article](information-data/symbols-and-encoding.md) | Draft | Core claims checked | [Pilot technical review](PILOT-TECHNICAL-REVIEW.md); final acceptance pending |
| F-05-02 | Bits and bytes | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-05-03 | Information theory | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-05-04 | Data types | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-05-05 | Datasets, records, fields, and values | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-05-06 | Data structures and formats | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-05-07 | Metadata | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-05-08 | Databases and queries | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-05-09 | Data provenance and lifecycle | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 06. Digital Systems & Hardware (Wave C; 9 headings)

**Area index:** [Digital Systems & Hardware](digital-systems-hardware/README.md). **Coverage questions:** [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-06-01 | Digital logic | [Draft article](digital-systems-hardware/digital-logic.md) | Draft | Core claims checked | [Pilot technical review](PILOT-TECHNICAL-REVIEW.md); final acceptance pending |
| F-06-02 | Computing components | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-06-03 | Processors and instruction sets | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-06-04 | Memory and storage | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-06-05 | Buses and interfaces | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-06-06 | Input/output | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-06-07 | Timing and clocks | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-06-08 | Firmware | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-06-09 | Hardware abstraction | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 07. Computation & Algorithms (Wave D; 9 headings)

**Area index:** [Computation & Algorithms](computation-algorithms/README.md). **Coverage questions:** [G-02](COVERAGE-GAP-DECISIONS.md#g-02-numerical-methods-and-optimization), [G-06](COVERAGE-GAP-DECISIONS.md#g-06-artificial-intelligence-and-machine-learning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-07-01 | Computability | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-02 | Algorithms | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-03 | Algorithm design | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-04 | Complexity | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-05 | Computational data structures | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-06 | Iteration and recursion | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-07 | Concurrency and parallelism | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-08 | Synchronization | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-07-09 | Computational efficiency | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 08. Software & Programming (Wave D; 9 headings)

**Area index:** [Software & Programming](software-programming/README.md). **Coverage questions:** [G-03](COVERAGE-GAP-DECISIONS.md#g-03-formal-methods-and-model-checking), [G-09](COVERAGE-GAP-DECISIONS.md#g-09-scientific-and-engineering-validation), [G-10](COVERAGE-GAP-DECISIONS.md#g-10-lifecycle-evolution-and-versioning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-08-01 | Programming languages | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-02 | Syntax and semantics | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-03 | Programming paradigms | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-04 | Compilation and interpretation | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-05 | Runtime environments | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-06 | Modules and dependencies | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-07 | Software interfaces | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-08 | Error handling | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-08-09 | Testing and software lifecycle | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 09. Operating System Principles (Wave E; 10 headings)

**Area index:** [Operating System Principles](operating-system-principles/README.md). **Coverage questions:** [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-09-01 | Kernels | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-02 | System calls | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-03 | Processes and threads | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-04 | Scheduling | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-05 | Memory management | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-06 | Filesystems | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-07 | Drivers and devices | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-08 | Execution contexts | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-09 | System initialization | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-09-10 | Resource management | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 10. Communication & Distributed Systems (Wave E; 9 headings)

**Area index:** [Communication & Distributed Systems](communication-distributed-systems/README.md). **Coverage questions:** [G-04](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks), [G-08](COVERAGE-GAP-DECISIONS.md#g-08-distributed-consistency-and-partial-failure). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-10-01 | Communication models | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-02 | Transmission and signaling | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-03 | Communication channels | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-04 | Protocols and layering | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-05 | Addressing and naming | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-06 | Latency and throughput | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-07 | Reliability and ordering | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-08 | Distributed state | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-10-09 | Synchronization and coordination | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 11. Systems & Engineering (Wave B; 11 headings)

**Area index:** [Systems & Engineering](systems-engineering/README.md). **Coverage questions:** [G-08](COVERAGE-GAP-DECISIONS.md#g-08-distributed-consistency-and-partial-failure), [G-09](COVERAGE-GAP-DECISIONS.md#g-09-scientific-and-engineering-validation), [G-10](COVERAGE-GAP-DECISIONS.md#g-10-lifecycle-evolution-and-versioning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-11-01 | Systems and subsystems | [Draft article](systems-engineering/systems-and-subsystems.md) | Draft | Core claims checked | [Pilot technical review](PILOT-TECHNICAL-REVIEW.md); final acceptance pending |
| F-11-02 | Components and interfaces | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-03 | Architecture and composition | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-04 | Dependencies | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-05 | State and behavior | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-06 | Feedback and control | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-07 | Emergence and complexity | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-08 | Reliability and failure | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-09 | Requirements | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-10 | Verification and validation | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-11-11 | System lifecycle | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

### 12. Human & Sociotechnical Systems (Wave B; 8 headings)

**Area index:** [Human & Sociotechnical Systems](human-sociotechnical-systems/README.md). **Coverage questions:** [G-06](COVERAGE-GAP-DECISIONS.md#g-06-artificial-intelligence-and-machine-learning). These indicate *areas to check*, not a conclusion that every subject is deficient.

| Tracker ID | Exact approved subject | Canonical article | Development | Source review | Relationships / blockers |
| --- | --- | --- | --- | --- | --- |
| F-12-01 | Human cognition and perception | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-12-02 | Decision-making | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-12-03 | Human-computer interaction | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-12-04 | Usability and accessibility | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-12-05 | Human error | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-12-06 | Collaboration and communication | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-12-07 | Organizational structures | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |
| F-12-08 | Ethics and professional responsibilities | Not authored | Inventoried | Not reviewed | Proposed ownership crosswalk; pending article links |

## Required update procedure

1. Preserve exact subject wording and **tracker ID** when updating states. Do not delete approved inventory headings because multiple topics eventually share a canonical article.
2. Once an actual article exists, replace *Not authored / Queued* with a **relative Markdown link to the real file**, and mark the development state **Draft**.
3. Link sources near relevant claims, record what has been independently checked, and only then promote **Source review** to **Verified**.
4. Replace broad, area-level conceptual references with precise canonical article links when those destinations exist.
5. Keep the three pending architectural decisions [G-01 mathematical breadth](COVERAGE-GAP-DECISIONS.md#g-01-linear-algebra-geometry-topology), [G-04 general temporality](COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks), and [G-06 AI/ML](COVERAGE-GAP-DECISIONS.md#g-06-artificial-intelligence-and-machine-learning) visible until explicitly resolved.
6. Make a separate technical/editorial pass after pilot drafting before declaring an article **Reviewed** or **Published**.

## Approved exclusions

This is a **technical knowledge reference**, not an evaluation course: no Knowledge Checks, Practical Assessments, quizzes, test questions, grades, or learner scoring. Worked explanatory examples and verification of factual correctness are encouraged.

[Fundamentals](README.md) · [Curriculum Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md) · [Governing Architecture](ARCHITECTURE.md)
