# Knowledge Relationships

**Approved rule:** Use a hierarchy to navigate knowledge and a knowledge graph to represent relationships.

## Minimal convention

- Give a concept a canonical document location in the navigation hierarchy.
- Link to that document from other relevant sections rather than duplicating canonical definitions.
- When a relationship matters, state its **type** and its **target** explicitly.
- A document's directory is its navigation location, **not** necessarily its conceptual parent.
- A subject may relate to multiple domains.

Example (illustrative only):

```text
Concept A -- depends on --> Concept B
Concept A -- used by --> Concept C
```

No fixed relationship-type vocabulary, metadata schema, or graph engine has been approved yet. Those remain future architectural decisions.
