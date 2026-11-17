# Data Provenance and Lifecycle

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Data provenance and lifecycle  
**Development status:** Draft  
**Source review:** References listed; scoped claim-to-source audit pending

## Data history matters to meaning and trust

**Data provenance** describes information about the origin, sources, activities, transformations and responsible agents associated with a data resource or statement. **Data lifecycle** describes phases and transitions in a resource's existence and management, including creation or acquisition, processing, use, retention, revision, archiving and removal as applicable.

Provenance concerns a resource's **reported history and derivation**; lifecycle concerns **management over time**. They intersect but are not interchangeable. Neither guarantees that a recorded measurement was correct, that a source was honest, or that every historical step has been captured.

[Metadata](metadata.md) supplies descriptive context; [Datasets, Records, Fields, and Values](datasets-records-fields-and-values.md) owns the granularity of what is recorded; [Evidence](../scientific-analytical-reasoning/evidence.md) owns claim-relative evidentiary support.

## Origins, derivations, agents and activities

The [W3C PROV Data Model](https://www.w3.org/TR/prov-dm/) uses concepts such as:

- **Entity:** a modeled resource or thing whose state or identity matters to the provenance description.
- **Activity:** an action or process associated with how entities are used, generated or changed.
- **Agent:** an entity to which some responsibility for an activity or resource may be attributed.
- **Derivation:** an assertion that one entity was derived from another, under stated modeling semantics.
- **Generation and usage:** relations linking activities with generated or used entities.

These are established standard examples, **not** newly ratified primitive types for this repository. PROV relations express modeled claims. A declared `wasDerivedFrom` edge is not independent evidence that the asserted transformation actually occurred.

## Lineage and provenance are related but distinct

**Lineage** often emphasizes how output data depends on earlier inputs through processing steps. **Provenance** can include lineage plus origin, attribution and broader process context. The precise breadth of either term varies by system, so a practical specification should define which relations and metadata are captured.

A lineage graph can show input `A` processed into output `B`. It may still omit operator identity, model version, timing, source acquisition conditions, discarded records or external dependencies. The absence of a recorded lineage link is not proof that no transformation occurred.

The provenance graph is a representation of historical claims, not the historical events themselves. [Graph Theory](../mathematics-logic/graph-theory.md) owns graph structure, and [Causality and Correlation](../scientific-analytical-reasoning/causality-and-correlation.md) owns causal inference; provenance relations should not silently be treated as a complete causal model.

## A lifecycle is a model, not a universal seven-stage law

Data may be generated, observed, acquired, ingested, validated, transformed, stored, queried, published, revised, retained, archived or deleted. These activities may be repeated, reordered, omitted or performed in parallel. A backup, derivative or legal record may have a different lifecycle from the source.

A useful lifecycle description specifies:

- Which **resource or version** is under management.
- Which **activities or state transitions** are represented.
- Which identifiers and times belong to each assertion.
- Which **retention, access, correction or deletion policies** apply in the particular environment.
- Which observations support the assertion that each transition occurred.

This is an editorial checklist, not a newly approved lifecycle taxonomy or mandatory record schema. [State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) owns general event/state semantics; **G-04** general temporality remains an unresolved architectural scope decision.

## Worked example: a traceable unit conversion

Suppose an instrument supplies a recorded temperature `68 °F` in a source record `R1`. A derived record `R2` stores the computed equivalent `20 °C`, using the declared mapping:

```text
R1: reported_temperature_F = 68
    |
    | activity A1: C = (F - 32) × 5/9
    v
R2: calculated_temperature_C = 20
```

The calculation is `(68−32)×5/9 = 20`. Under the stated equation, the derived value is arithmetically correct.

A provenance description might state that activity A1 **used** R1, **generated** R2, and that R2 **was derived from** R1. To support reproduction it might also record the transformation rule, source identifier, software or method version, units, rounding policy and relevant timestamps.

This traceability makes the calculation inspectable but does not prove the original instrument reported the true physical temperature. A perfectly recorded conversion can faithfully reproduce a bad source value.

## Revision, retention and deletion

Data change can mean correcting an error, appending observations, changing schema, regenerating an analysis, or replacing a resource. These are different operations with different interpretive consequences.

A **version** refers to a distinguished revision under a given identity and versioning policy. A matching content hash is evidence that encoded bytes may be identical, **not a mathematical guarantee of byte equality**, because hash collisions are possible. The strength of this evidence depends on the algorithm, threat model, and manner of comparison. Even identical bytes need not have identical meaning under different interpretation contexts. Different hashes may arise from representation changes without a change in intended meaning. A hash alone does not establish authorship or source authenticity.

Deleting a primary record does not automatically erase backups, replicas, derived tables, caches or records held by other systems. Claims about complete deletion require a stated scope, process and verification evidence. Conversely, retaining every copy indefinitely is not automatically justified; data governance, privacy obligations and risk vary by context.

The exact meaning of collection time, event time, processing time and revision time must be explicitly distinguished. This article does not resolve general temporality G-04 by editorial fiat.

## Quality and accountability limits

Provenance supports traceability and auditability only to the extent its records are complete, attributable and trustworthy. Missing activities, unverifiable source assertions, incompatible versions and ambiguous time fields can weaken downstream conclusions.

The [W3C Data Catalog Vocabulary 3](https://www.w3.org/TR/vocab-dcat-3/) provides interoperable dataset catalog descriptions, including versioning-oriented capabilities; it is not a replacement for the more detailed PROV model.

## Canonical boundaries and sources

Data provenance and lifecycle are domain-independent mechanisms. This article establishes no universal retention duration, approval workflow, compliance regime, security monitoring method, or mandatory knowledge-graph predicates.

### Sources

- [W3C PROV Data Model](https://www.w3.org/TR/prov-dm/).
- [W3C PROV Ontology](https://www.w3.org/TR/prov-o/).
- [W3C Data Catalog Vocabulary (DCAT) Version 3](https://www.w3.org/TR/vocab-dcat-3/).

**Editorial status:** Substantive draft; provenance and lifecycle claims and numeric examples require a dedicated technical audit. G-04 remains open; no new curriculum headings or assessments introduced.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
