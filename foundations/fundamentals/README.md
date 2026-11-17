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
- [**Canonical Concept Boundary Decisions**](CONCEPT-BOUNDARY-DECISIONS.md): Provides working ownership resolutions and discriminating examples for all 20 overlap groups, with an explicit temporality exception.

**Status distinction:** The 12 areas and 109 headings are approved. The detailed ownership boundaries, relationship descriptions, and coverage-gap dispositions are **working proposals**, not automatically ratified conceptual definitions. The register links to existing area indexes until canonical articles are written and verified.

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

**Current milestone:** The 12 knowledge areas and their 109 inventory headings have been implemented. This is **architectural scaffolding**, not confirmation that the coverage audit, canonical subject content, or technical verification gates have passed.

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
