# Metadata

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Metadata  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 02 audit](../WAVE-B-TECHNICAL-REVIEW-02.md); no independent human peer review

## Metadata gives information a context for interpretation

**Metadata** is information describing or qualifying a resource, dataset, record, representation, process or other object for a specified purpose. It can support discovery, interpretation, use, management, provenance and accountability. Metadata is often summarized as “data about data,” but it can also describe the structure or circumstances of a physical resource, a process or a conceptual model.

Metadata is itself information and can have its own metadata. No absolute technical boundary makes a field forever “data” or “metadata” in every context: a timestamp can be a measured variable in one dataset and descriptive context in another.

[Datasets, Records, Fields, and Values](datasets-records-fields-and-values.md) owns information granularity, [Schemas](../models-abstraction/schemas.md) owns structural constraints, and [Data Provenance and Lifecycle](data-provenance-and-lifecycle.md) owns origin, derivation and change history.

## Descriptions must identify what they describe

A metadata statement needs an intended **subject**. For example, `created_at=2026-11-17` might describe the creation of a file, collection of a measurement, insertion of a database row, or modification of a derived report. These are not equivalent events.

Similarly, `unit="°C"` can describe a dataset column's measurement convention, not certify that each recorded temperature was actually measured correctly. `source="instrument-7"` is a source claim, not independent validation that the instrument was calibrated or present.

Useful metadata interpretation includes **scope, reference target, property meaning, format, value, provenance, and applicable version** when relevant. These are editorial considerations, not a mandatory repository-wide schema.

## Different purposes, overlapping mechanisms

Metadata practices often emphasize several functions:

| Illustrative function | Example question |
| --- | --- |
| Discovery | What resource is this, and how can it be found? |
| Description | What topics, variables or entities does it concern? |
| Structural interpretation | Which fields, units, encodings or relationships are used? |
| Administration | Who maintains it, and under what declared terms? |
| Provenance context | Which source or process is reported to have produced it? |
| Version context | Which specification or revision applies? |

These functions can overlap. A citation may aid discovery, attribution and provenance simultaneously. They are **not** six newly approved knowledge categories.

The [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) vocabulary defines properties such as creator, identifier, created and modified. The [W3C Data Catalog Vocabulary (DCAT) 3](https://www.w3.org/TR/vocab-dcat-3/) defines a framework for publishing interoperable dataset and data-service descriptions. Neither automatically validates truthfulness of submitted metadata.

## Metadata can be embedded, associated or external

A metadata record can be stored inside the resource, in a sidecar file, a database table, a catalog, or another referencing system. A resource may have more than one metadata description with different scope and authority. The association between metadata and the described object must remain resolvable.

A metadata reference can go stale if a source is revised, renamed, deleted or replaced. An identifier alone does not guarantee resolvability, uniqueness across all systems, immutability, or authenticity. Stable interpretation depends on explicit agreements and lifecycle controls.

## Worked example: observation context

Consider the simplified observation:

```text
value: 21.0
```

Without context, it is not known what the number represents. One possible metadata description might include:

```text
quantity_kind: temperature
unit: degree Celsius
reported_at: 2026-11-17T14:00:00Z
source_id: instrument-7
schema_version: 1.2
```

This turns an uninterpretable value into a **qualified recorded claim**, with more information for interpretation and reproducibility. It still does not demonstrate that the instrument was accurate, the reported time was correct, or the record was unmodified. The ISO 8601-style UTC timestamp here is illustrative only; what “reported_at” means is declared by the example, not inferred from its syntax.

**Schema version** declares a referenced contract if the contract is available; the mere string `1.2` does not ensure any system meets it.

## Metadata quality and semantic collisions

Metadata may be incomplete, inconsistent, overly broad, mistyped, duplicated, outdated, or wrong. Two datasets can each carry `timestamp` metadata but mean event time versus processing time. Equating the fields without confirming their semantics can invalidate comparisons.

Likewise, a field `owner` might indicate legal rights holder, organizational maintainer, or creator. A vocabulary definition and local usage rules prevent ambiguity more effectively than matching on label text.

[Ontologies and Taxonomies](../models-abstraction/ontologies-and-taxonomies.md) owns formalized conceptual relations; [Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md) owns epistemic limits. Metadata can document claims and support checks without itself becoming evidence sufficient to prove them.

## Boundaries and sources

Metadata describes and qualifies; **provenance** models history and derivation; **schema** constrains representation; **content** is the represented information under a defined interpretation. The same system may use all four, but they should not be treated as synonyms.

### Sources

- [Dublin Core Metadata Initiative: DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).
- [W3C Data Catalog Vocabulary (DCAT) Version 3](https://www.w3.org/TR/vocab-dcat-3/).
- [W3C PROV Data Model](https://www.w3.org/TR/prov-dm/).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 02 technical audit](../WAVE-B-TECHNICAL-REVIEW-02.md). Complete source verification, independent human expert review and final publication acceptance remain separate and pending.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
