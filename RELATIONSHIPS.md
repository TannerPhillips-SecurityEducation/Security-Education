# Knowledge Relationships

**Governing principle:** Hierarchy for navigation, knowledge graph for relationships.

## Canonical knowledge location

- Organize specialized knowledge as **Domain → Function → Implementation**.
- Give each subject one canonical document location. A function directory is its primary navigational category.
- Keep shared foundational concepts at their canonical location in Foundations.
- Alternate views, including operating systems, cloud providers, and application types, **link to** canonical subject documents rather than maintain duplicated definitions.
- A folder's position represents navigation, **not necessarily** an ontological *is-a* relationship.

## Fundamental Concepts and Contextual Applications

In [Fundamentals](foundations/fundamentals/README.md), the **twelve areas are navigational knowledge disciplines**, while their underlying concepts and relationships supply conceptual coherence.

A foundational general concept has one canonical definition. Additional explanations in other areas or domains may describe **distinct mechanisms or implementations** rather than duplicate that definition.

For example, [Boolean logic](foundations/fundamentals/mathematics-logic/README.md) is conceptually grounded in Mathematics & Logic; its electronic realization belongs in [Digital Systems & Hardware](foundations/fundamentals/digital-systems-hardware/README.md). General state, events, and transitions are within [Models & Abstraction](foundations/fundamentals/models-abstraction/README.md); their OS-specific or distributed manifestations extend those concepts.

See the [governing Fundamentals architecture](foundations/fundamentals/ARCHITECTURE.md). Illustrative conceptual primitives are **not** a newly ratified universal primitive taxonomy.

## Fundamentals Crosswalks

The [Coverage Gap Decision Register](foundations/fundamentals/COVERAGE-GAP-DECISIONS.md) tracks seven existing-heading placements and three pending architectural scope decisions without introducing new categories or relation predicates.

The [Canonical Ownership & Relationship Register](foundations/fundamentals/CANONICAL-OWNERSHIP-REGISTER.md) gives all 109 approved subject headings a proposed general scope and an illustrative connection to another approved subject. The [Concept Overlap & Coverage Review](foundations/fundamentals/CONCEPT-OVERLAP-REVIEW.md) tracks proposed ownership boundaries and unresolved gaps. The [Canonical Concept Boundary Decisions](foundations/fundamentals/CONCEPT-BOUNDARY-DECISIONS.md) distinguishes 20 recurring overlaps, without creating a new graph schema or hiding the open temporality issue.

Both are **working architectural maps**. Their relationship labels are not an approved, machine-enforced graph vocabulary. The links lead to actual knowledge-area indexes until individual canonical articles are published.

## Explicit relationships

In content documents, record the **relationship type** and a link to the **target**. A subject may have multiple relationships and span multiple domains.

Illustrative relationship statements:

```text
Implementation -- implements --> Function
Implementation -- runs on --> Platform
Implementation -- provided by --> Provider
Concept -- depends on --> Related Concept
```

These labels are examples, **not** a formally ratified relation-type vocabulary.

## Scope of the present implementation

- Function directories and their READMEs provide navigation.
- Operating-system, provider, and application-type pages are secondary entry points.
- Markdown links can express cross-domain relationships as the knowledge develops.
- No graph database, universal metadata schema, or automated relationship index has been implemented. Those require separate architectural decisions.

[Return to Security Knowledge](README.md)
