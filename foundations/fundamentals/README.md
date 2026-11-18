# Fundamentals

**Division:** [Foundations](../README.md)  
**Status:** 12 approved knowledge areas; **116 authored subjects = 109 legacy Reviewed (model-assisted) + 7 newly Drafted (References listed)**; none Published

Fundamentals establishes domain-agnostic concepts, structures, principles, and mechanisms needed to understand technical systems and their behavior. It supports the seven specialized knowledge domains without making any one technology, vendor, or security practice the organizing principle.

## Governing Architecture

[**Fundamentals: Governing Knowledge Architecture**](ARCHITECTURE.md) defines the approved four requirements:

1. **Domain independence:** Explain foundational concepts without relying on a particular technical or security domain.
2. **Conceptual and mechanical depth:** Develop concepts, structures, principles, mechanisms, and relationships.
3. **Canonical knowledge ownership:** Define a general concept once, then link its contextual applications.
4. **Specialized extension:** Let the seven specialized domains build upon general fundamentals without redefining them.

The **twelve currently approved knowledge areas are navigation disciplines**, while the **116 currently tracked subject headings** (109 legacy Reviewed + 7 Draft) form a **versioned, revisable coverage inventory**, not a fixed quota. Underlying concepts and their relationships provide conceptual coherence across disciplines. Proposed universal primitives do not become additional categories without separate approval.

## Living Inventory Policy

**The historical count of 109 was not an architectural limit.** The current working inventory is **116 subjects**, with the seven additions documented in [Architecture Adjudication 01](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md). Subjects may be **added, split, merged, renamed or retired** when model-grounded coverage and canonical-ownership analysis justify the change. The twelve existing knowledge areas remain the separate approved navigation baseline. The [governing architecture](ARCHITECTURE.md#living-subject-inventory-and-versioned-change-control) defines the change-control and historical-traceability rules.

A newly added or materially revised article must be reviewed on its own merits; a past 109/109 model-assisted status must not be projected onto future inventory versions. Historical reports retain their original denominator.

## Established Frameworks, Models & Architectures Audit

The [Foundational Models, Frameworks & Architectures Review 01](FOUNDATIONAL-MODELS-FRAMEWORKS-ARCHITECTURES-AUDIT-01.md) compares existing explanations and canonical boundaries against established technical knowledge structures. Its reproducible [77-name lexical ledger](NAMED-MODEL-LEXICAL-LEDGER-01.md) scanned the **109 historical subject articles** before the new seven headings were inventoried; a separate sampled content review examines why literal model names are **not** reliable measures of conceptual coverage.

[Architecture Adjudication 01](FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md) resolved fourteen audit cases into **seven newly Inventoried subjects** and deeper-treatment recommendations for existing articles. The earlier audit itself changed no subjects; the subsequent adjudication did. The [living-inventory rule](ARCHITECTURE.md#living-subject-inventory-and-versioned-change-control) permits growth and contraction with recorded conceptual justification.

## Canonical Ownership & Concept Relationships

- [**Canonical Ownership & Relationship Register**](CANONICAL-OWNERSHIP-REGISTER.md): Maps the current **116 subjects** (109 legacy reviewed + seven inventoried) to intended conceptual responsibilities and illustrative relationships.
- [**Concept Overlap & Coverage Review**](CONCEPT-OVERLAP-REVIEW.md): Documents 20 recurrent conceptual overlaps and 10 candidate coverage questions that require review.
- [**Canonical Concept Boundary Decisions**](CONCEPT-BOUNDARY-DECISIONS.md): Provides approved conceptual boundaries and discriminating examples for all 20 overlap groups, while documenting the former general-temporality ownership exception, now structurally placed under F-03-11; content verification remains open.
- [**Coverage Gap Decision Register**](COVERAGE-GAP-DECISIONS.md): Preserves ten original gap cases; G-01, G-04 and G-06 now have explicit new-subject placement, while source-verified article content remains pending.

**Status distinction:** The existing 12 areas and 109 legacy headings retain their approved historical status. Seven additional subjects are now authored as Drafts following documented architectural adjudication; **116 is not fixed**. The detailed ownership boundaries, relationship descriptions, and coverage-gap dispositions are **working proposals**, not automatically ratified conceptual definitions. The register links to existing area indexes until canonical articles are written and verified.

## Canonical Reference Development

**All 109 historical Fundamentals articles** passed scoped model-assisted technical reviews. **Seven additional inventoried subjects have no article and are Not reviewed.** This includes the final [Wave E Operating System Principles review](WAVE-E-TECHNICAL-REVIEW-01.md) (60 material claim groups) and [Wave E Communication & Distributed Systems review](WAVE-E-TECHNICAL-REVIEW-02.md) (54 claim groups).

| Approved knowledge area | Reviewed canonical reference articles |
| --- | --- |
| Mathematics & Logic | [Numbers and numerical systems](mathematics-logic/numbers-and-numerical-systems.md); [Sets and relations](mathematics-logic/sets-and-relations.md); [Boolean and predicate logic](mathematics-logic/boolean-and-predicate-logic.md); [Algebra and functions](mathematics-logic/algebra-and-functions.md); [Discrete mathematics](mathematics-logic/discrete-mathematics.md); [Graph theory](mathematics-logic/graph-theory.md); [Probability and statistics](mathematics-logic/probability-and-statistics.md); [Units and quantities](mathematics-logic/units-and-quantities.md); **New Draft articles:** [Linear algebra and vector spaces](mathematics-logic/linear-algebra-and-vector-spaces.md); [Geometry and spatial reasoning](mathematics-logic/geometry-and-spatial-reasoning.md); [Topology and continuity](mathematics-logic/topology-and-continuity.md) |
| Scientific & Analytical Reasoning | [Observation](scientific-analytical-reasoning/observation.md); [Measurement](scientific-analytical-reasoning/measurement.md); [Evidence](scientific-analytical-reasoning/evidence.md); [Hypotheses and experiments](scientific-analytical-reasoning/hypotheses-and-experiments.md); [Deduction, induction, and abduction](scientific-analytical-reasoning/deduction-induction-abduction.md); [Causality and correlation](scientific-analytical-reasoning/causality-and-correlation.md); [Uncertainty and confidence](scientific-analytical-reasoning/uncertainty-and-confidence.md); [Validation and falsification](scientific-analytical-reasoning/validation-and-falsification.md) |
| Models & Abstraction | [Entities and attributes](models-abstraction/entities-and-attributes.md); [Identity and distinction](models-abstraction/identity-and-distinction.md); [Relationships](models-abstraction/relationships.md); [Boundaries](models-abstraction/boundaries.md); [Abstraction](models-abstraction/abstraction.md); [Classification](models-abstraction/classification.md); [Ontologies and taxonomies](models-abstraction/ontologies-and-taxonomies.md); [Schemas](models-abstraction/schemas.md); [State, events, and transitions](models-abstraction/state-events-and-transitions.md); [Conceptual and formal models](models-abstraction/conceptual-and-formal-models.md); **New Draft articles:** [Temporal concepts and models](models-abstraction/temporal-concepts-and-models.md) |
| Physical & Electrical Principles | [Matter and energy](physical-electrical-principles/matter-and-energy.md); [Electricity](physical-electrical-principles/electricity.md); [Electrical circuits](physical-electrical-principles/electrical-circuits.md); [Electronics](physical-electrical-principles/electronics.md); [Analog and digital signals](physical-electrical-principles/analog-and-digital-signals.md); [Waves and frequency](physical-electrical-principles/waves-and-frequency.md); [Sensors and actuators](physical-electrical-principles/sensors-and-actuators.md); [Signal conversion](physical-electrical-principles/signal-conversion.md); [Physical control mechanisms](physical-electrical-principles/physical-control-mechanisms.md) |
| Information & Data | [Symbols and encoding](information-data/symbols-and-encoding.md); [Bits and bytes](information-data/bits-and-bytes.md); [Information theory](information-data/information-theory.md); [Data types](information-data/data-types.md); [Datasets, records, fields, and values](information-data/datasets-records-fields-and-values.md); [Data structures and formats](information-data/data-structures-and-formats.md); [Metadata](information-data/metadata.md); [Databases and queries](information-data/databases-and-queries.md); [Data provenance and lifecycle](information-data/data-provenance-and-lifecycle.md) |
| Digital Systems & Hardware | [Digital logic](digital-systems-hardware/digital-logic.md); [Computing components](digital-systems-hardware/computing-components.md); [Processors and instruction sets](digital-systems-hardware/processors-and-instruction-sets.md); [Memory and storage](digital-systems-hardware/memory-and-storage.md); [Buses and interfaces](digital-systems-hardware/buses-and-interfaces.md); [Input/output](digital-systems-hardware/input-output.md); [Timing and clocks](digital-systems-hardware/timing-and-clocks.md); [Firmware](digital-systems-hardware/firmware.md); [Hardware abstraction](digital-systems-hardware/hardware-abstraction.md); **New Draft articles:** [Computer architecture models](digital-systems-hardware/computer-architecture-models.md) |
| Computation & Algorithms | [Computability](computation-algorithms/computability.md); [Algorithms](computation-algorithms/algorithms.md); [Algorithm design](computation-algorithms/algorithm-design.md); [Complexity](computation-algorithms/complexity.md); [Computational data structures](computation-algorithms/computational-data-structures.md); [Iteration and recursion](computation-algorithms/iteration-and-recursion.md); [Concurrency and parallelism](computation-algorithms/concurrency-and-parallelism.md); [Synchronization](computation-algorithms/synchronization.md); [Computational efficiency](computation-algorithms/computational-efficiency.md); **New Draft articles:** [Artificial intelligence foundations](computation-algorithms/artificial-intelligence-foundations.md); [Machine learning foundations](computation-algorithms/machine-learning-foundations.md) |
| Software & Programming | [Programming languages](software-programming/programming-languages.md); [Syntax and semantics](software-programming/syntax-and-semantics.md); [Programming paradigms](software-programming/programming-paradigms.md); [Compilation and interpretation](software-programming/compilation-and-interpretation.md); [Runtime environments](software-programming/runtime-environments.md); [Modules and dependencies](software-programming/modules-and-dependencies.md); [Software interfaces](software-programming/software-interfaces.md); [Error handling](software-programming/error-handling.md); [Testing and software lifecycle](software-programming/testing-and-software-lifecycle.md) |
| Operating System Principles | [Kernels](operating-system-principles/kernels.md); [System calls](operating-system-principles/system-calls.md); [Processes and threads](operating-system-principles/processes-and-threads.md); [Scheduling](operating-system-principles/scheduling.md); [Memory management](operating-system-principles/memory-management.md); [Filesystems](operating-system-principles/filesystems.md); [Drivers and devices](operating-system-principles/drivers-and-devices.md); [Execution contexts](operating-system-principles/execution-contexts.md); [System initialization](operating-system-principles/system-initialization.md); [Resource management](operating-system-principles/resource-management.md) |
| Communication & Distributed Systems | [Communication models](communication-distributed-systems/communication-models.md); [Transmission and signaling](communication-distributed-systems/transmission-and-signaling.md); [Communication channels](communication-distributed-systems/communication-channels.md); [Protocols and layering](communication-distributed-systems/protocols-and-layering.md); [Addressing and naming](communication-distributed-systems/addressing-and-naming.md); [Latency and throughput](communication-distributed-systems/latency-and-throughput.md); [Reliability and ordering](communication-distributed-systems/reliability-and-ordering.md); [Distributed state](communication-distributed-systems/distributed-state.md); [Synchronization and coordination](communication-distributed-systems/synchronization-and-coordination.md) |
| Systems & Engineering | [Systems and subsystems](systems-engineering/systems-and-subsystems.md); [Components and interfaces](systems-engineering/components-and-interfaces.md); [Architecture and composition](systems-engineering/architecture-and-composition.md); [Dependencies](systems-engineering/dependencies.md); [State and behavior](systems-engineering/state-and-behavior.md); [Feedback and control](systems-engineering/feedback-and-control.md); [Emergence and complexity](systems-engineering/emergence-and-complexity.md); [Reliability and failure](systems-engineering/reliability-and-failure.md); [Requirements](systems-engineering/requirements.md); [Verification and validation](systems-engineering/verification-and-validation.md); [System lifecycle](systems-engineering/system-lifecycle.md) |
| Human & Sociotechnical Systems | [Human cognition and perception](human-sociotechnical-systems/human-cognition-and-perception.md); [Decision-making](human-sociotechnical-systems/decision-making.md); [Human-computer interaction](human-sociotechnical-systems/human-computer-interaction.md); [Usability and accessibility](human-sociotechnical-systems/usability-and-accessibility.md); [Human error](human-sociotechnical-systems/human-error.md); [Collaboration and communication](human-sociotechnical-systems/collaboration-and-communication.md); [Organizational structures](human-sociotechnical-systems/organizational-structures.md); [Ethics and professional responsibilities](human-sociotechnical-systems/ethics-and-professional-responsibilities.md) |

The [Development & Verification Register v1.18](DEVELOPMENT-VERIFICATION-REGISTER.md) reconciles **116 authored headings: 109 historically Reviewed (model-assisted), seven Draft with References listed, zero Inventoried without articles**. The [Canonical Ownership Register v1.15](CANONICAL-OWNERSHIP-REGISTER.md) links all 116 actual article files while keeping technical-review status distinct.

## Publication Readiness

**Complete authoring and internal model-assisted technical review are not the same as publication acceptance.** A scoped technical review establishes that selected material claim groups and examples were checked, not that every sentence has complete source support or that qualified independent experts have reviewed the corpus.

The [Curriculum Development Plan v1.21](CURRICULUM-DEVELOPMENT-PLAN.md) now directs work toward complete source-level verification, external link integrity, semantic relationship and subject-depth consistency, seven-domain coverage, and independent human expert peer review.

The [Publication Readiness Audit 01](PUBLICATION-READINESS-AUDIT-01.md) checked the **pre-report snapshot of 152 Fundamentals Markdown files**: **2,681 inline relative Markdown-link occurrences**, **zero missing internal file destinations**, and **55 fragment-link occurrences** resolving to **32 distinct existing heading anchors**. All twelve subject-area indexes and 109 canonical article links aligned with the register. This **preliminary internal navigation check** does not constitute acceptance under every publication gate.

[Wave E Authoring Verification](WAVE-E-AUTHORING-VERIFICATION.md) is a **historical pre-audit authoring snapshot**; the two Wave E technical audits above supersede its pending-review states.

**G-01, G-04 and G-06 now have both canonical subject placement and substantive Draft articles**. Their scoped technical review, stronger source validation, and publication acceptance remain separate gates. Twelve area categories are unchanged. No Knowledge Checks, Practical Assessments, or mandatory vendor technologies were introduced.

## Technical Audit Evidence

- [Pilot Technical Review](PILOT-TECHNICAL-REVIEW.md): initial correction pass.
- [Six-Pilot Claim-to-Source Audit](PILOT-CLAIM-SOURCE-AUDIT.md): 50 claim families.
- [Wave A Batch 01 Review](WAVE-A-TECHNICAL-REVIEW-01.md): 21 claim families.
- [Wave A Batch 02 Review](WAVE-A-TECHNICAL-REVIEW-02.md): 27 claim families.
- [Wave A Batch 03 Review](WAVE-A-TECHNICAL-REVIEW-03.md): 24 claim families.
- [Wave A Batch 04 Review](WAVE-A-TECHNICAL-REVIEW-04.md): 24 claim families.
- [Wave A Batch 05 Review](WAVE-A-TECHNICAL-REVIEW-05.md): 24 claim families.
- [Wave A Batch 06 Review](WAVE-A-TECHNICAL-REVIEW-06.md): 24 claim families.
- [Wave A Batch 07 Review](WAVE-A-TECHNICAL-REVIEW-07.md): 30 claim families.
- [Wave B Batch 01 Review](WAVE-B-TECHNICAL-REVIEW-01.md): 24 claim families.
- [Wave B Batch 02 Review](WAVE-B-TECHNICAL-REVIEW-02.md): 24 claim families.
- [Wave B Batch 03 Review](WAVE-B-TECHNICAL-REVIEW-03.md): 24 claim families.
- [Wave B Batch 04 Review](WAVE-B-TECHNICAL-REVIEW-04.md): 36 claim families.
- [Wave B Batch 05 Review](WAVE-B-TECHNICAL-REVIEW-05.md): 48 claim families.
- [Wave C Batch 01 Review](WAVE-C-TECHNICAL-REVIEW-01.md): 24 claim families.
- [Wave C Batch 02 Review](WAVE-C-TECHNICAL-REVIEW-02.md): 24 claim families.
- [Wave C Batch 03 Review](WAVE-C-TECHNICAL-REVIEW-03.md): 54 claim families.
- [Wave D Batch 01 Review](WAVE-D-TECHNICAL-REVIEW-01.md): 24 claim families.
- [Wave D Batch 02 Review](WAVE-D-TECHNICAL-REVIEW-02.md): 30 claim families.
- [Wave D Software Batches 03–04 Review](WAVE-D-TECHNICAL-REVIEW-03-04.md): 54 claim families.
- [Wave E Operating System Principles Review](WAVE-E-TECHNICAL-REVIEW-01.md): 60 claim families.
- [Wave E Communication & Distributed Systems Review](WAVE-E-TECHNICAL-REVIEW-02.md): 54 claim families.

**Reviewed** denotes documented internal model-assisted review, not independent human approval or publication. G-01 mathematical breadth, G-04 general temporality and G-06 AI/ML have new canonical inventory owners, but new content and verification remain outstanding.

## Development Plan of Action

The [Curriculum Development Plan of Action](CURRICULUM-DEVELOPMENT-PLAN.md) is a working production roadmap for developing and, when justified, **revising** the current 116-subject inventory into an accurate, connected technical knowledge reference. It defines authoring waves, source requirements, editorial workflow, progress tracking, cross-domain integration, and completion gates. It excludes Knowledge Checks and Practical Assessments.

## Approved Knowledge Areas

| # | Area | Subject inventory |
| --- | --- | ---: |
| 01 | [Mathematics & Logic](mathematics-logic/README.md) | 11 (8 Reviewed + 3 Draft) |
| 02 | [Scientific & Analytical Reasoning](scientific-analytical-reasoning/README.md) | 8 |
| 03 | [Models & Abstraction](models-abstraction/README.md) | 11 (10 Reviewed + 1 Draft) |
| 04 | [Physical & Electrical Principles](physical-electrical-principles/README.md) | 9 |
| 05 | [Information & Data](information-data/README.md) | 9 |
| 06 | [Digital Systems & Hardware](digital-systems-hardware/README.md) | 10 (9 Reviewed + 1 Draft) |
| 07 | [Computation & Algorithms](computation-algorithms/README.md) | 11 (9 Reviewed + 2 Draft) |
| 08 | [Software & Programming](software-programming/README.md) | 9 |
| 09 | [Operating System Principles](operating-system-principles/README.md) | 10 |
| 10 | [Communication & Distributed Systems](communication-distributed-systems/README.md) | 9 |
| 11 | [Systems & Engineering](systems-engineering/README.md) | 11 |
| 12 | [Human & Sociotechnical Systems](human-sociotechnical-systems/README.md) | 8 |
| **Total** | **12 knowledge areas** | **116 subject headings (109 Reviewed + 7 Draft)** |

The historical 109 subjects have Reviewed articles, while seven new subjects now have Draft articles awaiting technical review. No subject has achieved independent human publication acceptance.

## Scope Boundaries

| Division | Primary purpose |
| --- | --- |
| **Fundamentals** | Explain general technical concepts and how systems, information, computation, and reasoning work |
| [**Security Foundations**](../security-foundations/README.md) | Explain security objectives, threats, vulnerabilities, protections, and security principles |
| [**Operational Foundations**](../operational-foundations/README.md) | Explain methods and practices for observing, evaluating, securing, and responding within operational environments |

Examples: The general concept of *identity* is foundational; identity verification and security protections are security subjects; monitoring identity events is an operational subject. Domain-specific implementations belong in their respective specialized knowledge domains.

## Canonical Subject Editorial Contract

Develop each canonical subject as connected technical reference prose. Each completed entry should cover:

1. **Concept and definition:** What the subject means and its scope.
2. **Distinctions:** What it is not, and how it differs from adjacent concepts.
3. **Mechanisms:** How it works or behaves.
4. **Relationships:** Dependencies and relevant connections to canonical concepts, with explicit links.
5. **Application:** Worked examples and domain-specific illustrations where helpful.
6. **References:** Cite credible original or authoritative documentation for verifiable technical claims.

This is a knowledge reference, not an assessment platform. Do **not** add Knowledge Checks, Practical Assessments, quizzes, or graded exercises. Technical explanations may include illustrative or worked examples. Do not present unverified claims as facts or duplicate canonical definitions.

## Completion Gates

A claim of *complete Fundamentals* requires evidence for all seven gates:

| Gate | Acceptance criterion |
| --- | --- |
| Architecture | Each knowledge area has an approved scope and subject inventory |
| Coverage | All essential concepts needed by the seven domains have a canonical home |
| Consistency | Definitions do not contradict or unnecessarily duplicate each other |
| Relationships | Dependencies, prerequisites, and cross-domain references are represented |
| Explanations | Each required concept has developed definitions, distinctions, mechanisms, and examples |
| Verification | Technical claims have been reviewed against credible references |
| Navigation | Every canonical subject can be discovered without requiring fixed reading order |

**Current milestone:** **116 authored subjects: 109 historical articles internally Reviewed (model-assisted), seven new Drafts awaiting technical review**. The preliminary link integrity audit passed within its scope; complete source validation, independent qualified human review and all seven publication gates remain open; none is finally Published.

## Coverage Across Specialized Domains

These relationships indicate especially relevant foundations, not exclusive ownership:

| Specialized domain | Especially relevant fundamentals |
| --- | --- |
| [Network](../../network/README.md) | Mathematics, Communication, Systems |
| [Endpoint](../../endpoint/README.md) | Hardware, Computation, Operating Systems |
| [Application](../../application/README.md) | Software, Algorithms, Information & Data |
| [Cloud](../../cloud/README.md) | Distributed Systems, Software, Systems Engineering |
| [Industrial](../../industrial/README.md) | Physical Principles, Control, Systems Engineering |
| [IoT](../../iot/README.md) | Electronics, Hardware, Communication, Software |
| [Identity](../../identity/README.md) | Logic, Information, Models, Human Systems |

## Reference Frameworks for Future Coverage Review

- [ACM/IEEE-CS/AAAI CS2023](https://csed.acm.org/knowledge-areas/)
- [Computing Curricula 2020](https://www.acm.org/education/curricula-recommendations)
- [Systems Engineering Body of Knowledge (SEBoK)](https://sebokwiki.org/wiki/Main_Page)

These are external coverage references, not the authority defining this repository's taxonomy.

[Foundations](../README.md) · [Knowledge relationship conventions](../../RELATIONSHIPS.md) · [Security Knowledge](../../README.md)
