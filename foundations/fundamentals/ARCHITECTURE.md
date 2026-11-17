# Fundamentals: Governing Knowledge Architecture

**Status:** Approved governing definition and architectural requirements  
**Scope:** Security Knowledge → Foundations → Fundamentals  
**Baseline preserved:** 12 approved knowledge areas and 109 approved subject headings  
**Implementation:** Markdown navigation and links; no additional taxonomy or graph engine authorized

## Governing Definition

> Fundamentals establishes domain-agnostic concepts, structures, principles, and mechanisms needed to understand technical systems and their behavior. It supports the seven specialized knowledge domains without making any one technology, vendor, or security practice the organizing principle.

This definition governs classification, conceptual ownership, editorial development, and future expansion within Fundamentals.

Fundamentals is **not merely introductory cybersecurity material**. It explains the common knowledge from which technical systems can be understood. Security-specific principles belong in [Security Foundations](../security-foundations/README.md); methods of security practice belong in [Operational Foundations](../operational-foundations/README.md).

## Four Governing Architectural Requirements

### 1. Domain Independence

A foundational concept must be explainable without depending on one specialized domain, technology, vendor, operating system, or security workflow.

A domain-specific example may illustrate a concept, but the example must not silently become the definition.

**Example:** The general concept of *state* is domain-agnostic. Windows process state, distributed system state, and an industrial controller's state are contextual applications and may require additional mechanisms in their specialized homes.

### 2. Conceptual and Mechanical Depth

Fundamentals must explain more than terminology. The following facets guide development; they are **not five new navigation categories**.

| Facet | Question answered |
| --- | --- |
| **Concept** | What is it, and what does the term mean? |
| **Structure** | What elements constitute or organize it? |
| **Principle** | What rules, constraints, or general relationships govern it? |
| **Mechanism** | How does it operate, produce an effect, or change? |
| **Relationship** | What does it depend upon, distinguish from, contain, or interact with? |

The [canonical subject editorial contract](README.md#canonical-subject-editorial-contract) additionally requires substantive distinctions, helpful examples, and source references. Not every facet needs an identical section format or length.

### 3. Canonical Knowledge Ownership

A foundational concept has **one canonical home** for its general definition. Contextual implementations may have distinct canonical homes for their additional mechanisms. Related sections point to those homes with explicit links rather than copy or silently redefine the foundational explanation.

A folder is a **navigation location**, not proof that a concept is ontologically subordinate to its directory label.

| Concept or mechanism | General canonical location | Contextual treatment |
| --- | --- | --- |
| **Boolean logic** | [Mathematics & Logic](mathematics-logic/README.md) | Logic gates in [Digital Systems & Hardware](digital-systems-hardware/README.md); conditions in [Software & Programming](software-programming/README.md) |
| **State, event, transition** | [Models & Abstraction](models-abstraction/README.md) | System behavior in [Systems & Engineering](systems-engineering/README.md); execution state in [Operating System Principles](operating-system-principles/README.md) |
| **Identity and distinction** | [Models & Abstraction](models-abstraction/README.md) | Authentication in [Security Foundations](../security-foundations/README.md) and specialized [Identity Knowledge](../../identity/README.md) |
| **Communication** | [Communication & Distributed Systems](communication-distributed-systems/README.md) | Concrete infrastructure, protocols, and network services in [Network Knowledge](../../network/README.md) |

**Important:** These examples identify conceptual ownership boundaries. They do not claim the complete individual articles already exist, and they do not establish a universal formal ontology.

### 4. Specialized Domains Build Upon Fundamentals

The seven specialized domains consume and extend shared foundational knowledge:

- [Network](../../network/README.md)
- [Endpoint](../../endpoint/README.md)
- [Application](../../application/README.md)
- [Cloud](../../cloud/README.md)
- [Industrial](../../industrial/README.md)
- [IoT](../../iot/README.md)
- [Identity](../../identity/README.md)

The relationship is conceptual, **not** a mandatory sequence for readers. A reader may start in any specialized domain and follow links to necessary foundational explanations.

## Separate Navigation From Conceptual Structure

**Navigation hierarchy:** The twelve approved areas organize the Fundamentals knowledge inventory. The 109 headings identify subject coverage. These labels are broad *knowledge disciplines and subjects*, not necessarily the most basic conceptual primitives.

**Conceptual knowledge graph:** Underlying concepts and their relationships may cross multiple disciplines. Each canonical entry should maintain explicit links to the relevant other concepts and specialized applications.

A subject heading does not necessarily correspond to exactly one concept or one Markdown document. Conversely, a concept appearing in many subjects does not justify duplicated canonical definitions.

Illustrative cross-cutting concepts include **entity, identity, attribute, relation, boundary, state, event, change, information, representation, function, and interaction**. This list is **illustrative, not an approved exhaustive primitive catalog**, and does not authorize new root sections.

## Placement Decision

Before adding a canonical entry, classify its scope using these checks:

1. **Generality:** Can it be defined independently of a named product, vendor, operating system, or security practice?
2. **Conceptual distinction:** Is it a new foundational concept, a context-specific realization, or merely another term for something already covered?
3. **Ownership:** Which approved area has the strongest canonical responsibility for its general definition?
4. **Extension:** Does a specialized domain need additional mechanisms, constraints, or examples beyond that definition?
5. **Relationships:** Which other canonical concepts and domains must link to it?
6. **Evidence:** What sources substantiate the definition, claims, and relevant distinctions?

**Routing rule:** General concepts belong in Fundamentals. Security-specific objectives and protections belong in Security Foundations. General methods of performing security operations belong in Operational Foundations. Specialized implementations belong in the applicable knowledge domain. If scope is ambiguous, record the issue rather than silently duplicate or create a new category.

## Publication and Architectural Controls

- Preserve the **12 approved knowledge areas and 109 original subject headings** as the current baseline.
- Maintain one canonical explanation for each fundamental concept, while recognizing genuinely different context-specific mechanisms.
- Write connected technical reference prose explaining meaning, distinctions, structures, principles, mechanisms, relationships, and examples as relevant.
- Cite authoritative technical references for verifiable claims and distinguish unresolved issues from established knowledge.
- Use the existing hierarchy and Markdown links; do not imply a formal knowledge-graph schema or graph database has been adopted.
- Introduce **no Knowledge Checks or Practical Assessments**, quizzes, or graded exercises.
- Treat proposed subject additions, relocations, formal primitives, and new graph infrastructure as separate architectural decisions.

## Readiness Criteria

A Fundamentals entry is ready for publication when its conceptual scope is clear, its canonical home has been established, its explanations are substantive, its relevant relationships are linked, and its material factual claims have been technically reviewed.

The Fundamentals body of knowledge is complete only after satisfying the [seven approved completion gates](README.md#completion-gates). The existence of headings or folders alone is not proof of completion.

## Related Documentation

- [Fundamentals index and approved areas](README.md)
- [Curriculum Development Plan of Action](CURRICULUM-DEVELOPMENT-PLAN.md)
- [Repository-wide relationship conventions](../../RELATIONSHIPS.md)
- [Foundations](../README.md)
