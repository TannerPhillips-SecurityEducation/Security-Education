# Fundamentals

**Division:** [Foundations](../README.md)  
**Status:** Approved subject architecture; reference content in development

Fundamentals establishes domain-agnostic concepts, structures, principles, and mechanisms needed to understand technical systems and their behavior. It supports the seven specialized knowledge domains without making any one technology, vendor, or security practice the organizing principle.

## Governing Architecture

[**Fundamentals: Governing Knowledge Architecture**](ARCHITECTURE.md) defines the approved four requirements:

1. **Domain independence:** Explain foundational concepts without relying on a particular technical or security domain.
2. **Conceptual and mechanical depth:** Develop concepts, structures, principles, mechanisms, and relationships.
3. **Canonical knowledge ownership:** Define a general concept once, then link its contextual applications.
4. **Specialized extension:** Let the seven specialized domains build upon general fundamentals without redefining them.

The **twelve approved knowledge areas are navigation disciplines**, while their 109 subject headings form a coverage inventory. Underlying concepts and their relationships provide conceptual coherence across disciplines. Proposed universal primitives do not become additional categories without separate approval.

## Canonical Ownership & Concept Relationships

- [**Canonical Ownership & Relationship Register**](CANONICAL-OWNERSHIP-REGISTER.md): Maps all 109 approved subject headings to proposed general responsibilities and 109 cross-subject relationship references.
- [**Concept Overlap & Coverage Review**](CONCEPT-OVERLAP-REVIEW.md): Documents 20 recurrent conceptual overlaps and 10 candidate coverage questions that require review.
- [**Canonical Concept Boundary Decisions**](CONCEPT-BOUNDARY-DECISIONS.md): Provides approved conceptual boundaries and discriminating examples for all 20 overlap groups, while retaining the general-temporality coverage exception.
- [**Coverage Gap Decision Register**](COVERAGE-GAP-DECISIONS.md): Dispositions all ten coverage questions: seven assigned to existing headings for authoring and three requiring explicit scope decisions. No change to the 12/109 baseline.

**Status distinction:** The 12 areas and 109 headings are approved. The detailed ownership boundaries, relationship descriptions, and coverage-gap dispositions are **working proposals**, not automatically ratified conceptual definitions. The register links to existing area indexes until canonical articles are written and verified.

## Canonical Reference Development

**Twelve reviewed (model-assisted)** references have undergone scoped technical and editorial review in three committed audits: [Pilot (50 claim families)](PILOT-CLAIM-SOURCE-AUDIT.md), [Wave A Batch 01 (21 families)](WAVE-A-TECHNICAL-REVIEW-01.md), and [Wave A Batch 02 (27 families)](WAVE-A-TECHNICAL-REVIEW-02.md). None is represented as independently human peer-reviewed or finally accepted for publication.

| Knowledge area | Reviewed canonical references |
| --- | --- |
| Mathematics & Logic | [Numbers and Numerical Systems](mathematics-logic/numbers-and-numerical-systems.md), [Sets and Relations](mathematics-logic/sets-and-relations.md), [Boolean and Predicate Logic](mathematics-logic/boolean-and-predicate-logic.md) |
| Scientific & Analytical Reasoning | [Observation](scientific-analytical-reasoning/observation.md), [Measurement](scientific-analytical-reasoning/measurement.md), [Evidence](scientific-analytical-reasoning/evidence.md) |
| Models & Abstraction | [Entities and Attributes](models-abstraction/entities-and-attributes.md), [Relationships](models-abstraction/relationships.md), [State, Events, and Transitions](models-abstraction/state-events-and-transitions.md) |
| Information & Data | [Symbols and Encoding](information-data/symbols-and-encoding.md) |
| Digital Systems & Hardware | [Digital Logic](digital-systems-hardware/digital-logic.md) |
| Systems & Engineering | [Systems and Subsystems](systems-engineering/systems-and-subsystems.md) |

**Three new Wave A Drafts**, with substantive technical explanations and source references, have not yet received a scoped acceptance audit:

- [Algebra and Functions](mathematics-logic/algebra-and-functions.md)
- [Hypotheses and Experiments](scientific-analytical-reasoning/hypotheses-and-experiments.md)
- [Identity and Distinction](models-abstraction/identity-and-distinction.md)

The [Development & Verification Register v0.6](DEVELOPMENT-VERIFICATION-REGISTER.md) maps all 109 approved headings and distinguishes **12 Reviewed (model-assisted), 3 Draft, and 94 Inventoried without articles**. Final independent source validation and the seven Fundamentals completion gates remain outstanding.

## Review Evidence and Publication Boundaries

- [Pilot Technical Review](PILOT-TECHNICAL-REVIEW.md): first six-article correction pass.
- [Pilot Claim-to-Source Audit](PILOT-CLAIM-SOURCE-AUDIT.md): 50 material claim families.
- [Wave A Batch 01 Technical Review](WAVE-A-TECHNICAL-REVIEW-01.md): 21 material claim families.
- [Wave A Batch 02 Technical Review](WAVE-A-TECHNICAL-REVIEW-02.md): 27 material claim families.

**Reviewed** indicates a scoped, model-assisted technical/editorial audit and does **not** establish independent human expert approval or final publication status. G-01 mathematics breadth, G-04 general temporality and G-06 AI/ML remain separate architectural scope decisions.

## Development Plan of Action

The [Curriculum Development Plan of Action](CURRICULUM-DEVELOPMENT-PLAN.md) is a working production roadmap for expanding the 109 inventoried subjects into an accurate, connected technical knowledge reference. It defines authoring waves, source requirements, editorial workflow, progress tracking, cross-domain integration, and completion gates. It excludes Knowledge Checks and Practical Assessments.

## Approved Knowledge Areas

| # | Area | Subject inventory |
| --- | --- | ---: |
| 01 | [Mathematics & Logic](mathematics-logic/README.md) | 8 |
| 02 | [Scientific & Analytical Reasoning](scientific-analytical-reasoning/README.md) | 8 |
| 03 | [Models & Abstraction](models-abstraction/README.md) | 10 |
| 04 | [Physical & Electrical Principles](physical-electrical-principles/README.md) | 9 |
| 05 | [Information & Data](information-data/README.md) | 9 |
| 06 | [Digital Systems & Hardware](digital-systems-hardware/README.md) | 9 |
| 07 | [Computation & Algorithms](computation-algorithms/README.md) | 9 |
| 08 | [Software & Programming](software-programming/README.md) | 9 |
| 09 | [Operating System Principles](operating-system-principles/README.md) | 10 |
| 10 | [Communication & Distributed Systems](communication-distributed-systems/README.md) | 9 |
| 11 | [Systems & Engineering](systems-engineering/README.md) | 11 |
| 12 | [Human & Sociotechnical Systems](human-sociotechnical-systems/README.md) | 8 |
| **Total** | **12 knowledge areas** | **109 subject headings** |

Each area contains its approved subject inventory. The subject headings **do not yet represent completed explanations or verified publications**.

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

**Current milestone:** The twelve knowledge areas and 109 headings are preserved. Fifteen substantive references are now linked (12 internally Reviewed and 3 Draft). Comprehensive corpus coverage, external technical verification, and the seven completion gates remain open.

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
