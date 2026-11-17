# Knowledge Relationships

**Governing principle:** Hierarchy for navigation, knowledge graph for relationships.

## Canonical knowledge location

- Organize specialized knowledge as **Domain → Function → Implementation**.
- Give each subject one canonical document location. A function directory is its primary navigational category.
- Keep shared foundational concepts at their canonical location in Foundations.
- Alternate views, including operating systems, cloud providers, and application types, **link to** canonical subject documents rather than maintain duplicated definitions.
- A folder's position represents navigation, **not necessarily** an ontological *is-a* relationship.

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
