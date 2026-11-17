# Datasets, Records, Fields, and Values

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Datasets, records, fields, and values  
**Development status:** Draft  
**Source review:** References listed; separate scoped claim-to-source audit pending

## Information has a scope and a grain

A **dataset** is a defined collection of data treated as a unit for an intended purpose. A **record** is a distinguishable data item within a dataset, frequently representing one observation, entity, event or transaction according to a declared grain. A **field** identifies an attribute or position within a record representation. A **value** is the recorded content associated with a field in a particular record.

These are useful conceptual distinctions, not a universal requirement that all information must be rectangular tables. Graph, document, time-series and other representations can organize information differently.

The **grain** specifies what a single record represents. Without grain, counts, joins, aggregates and temporal comparisons may have ambiguous meanings. [Entities and Attributes](../models-abstraction/entities-and-attributes.md) owns general entities; [Schemas](../models-abstraction/schemas.md) owns structural constraints.

## Dataset, record, field, value: a worked decomposition

Consider a hypothetical dataset of temperature observations:

| observation_id | device_id | temperature_C |
| --- | --- | ---: |
| O1 | D7 | 21.0 |
| O2 | D7 | 22.0 |
| O3 | D8 | 19.0 |

The dataset is the complete three-record collection. Its declared grain is **one observation per record**, not one device. The field `device_id` appears in each record, while `D7` is a value appearing in two separate observations.

Three records do not imply three devices. Here there are two distinct device identifiers. The arithmetic mean of the three reported temperatures is `(21+22+19)/3≈20.67 °C`, but this is a **record-weighted mean** of observed values, not a per-device mean. Averaging one mean per device instead produces `[(21+22)/2 + 19]/2 = 20.25 °C`. These distinct results demonstrate why grain and aggregation choices must be stated.

These toy values are invented and do not claim actual sensor accuracy or calibrated measurement uncertainty.

## Identity, uniqueness, and keys

A record identifier can distinguish one record within a declared scope. A device identifier may intentionally recur across observations. An identifier is not automatically a globally unique description of an underlying physical entity, and equality of two string values does not settle identity outside a specific model.

A **key** may uniquely identify records under a defined data constraint. Composite keys combine fields. Key uniqueness, missingness, and the scope of identity must be documented before deduplication or joining. The [relational model and SQL](https://www.iso.org/standard/76584.html) are one formal approach, not a universal requirement for all datasets.

## Missingness, nulls, and absence

An absent field, an explicit null, an empty string, zero, and an unknown physical value are not automatically interchangeable. Each system may define different semantics and permitted operations.

For example, a field `temperature_C=0` is a numerical report, not a missing temperature. If a value is absent because a sensor was offline, filling the field with zero can create a spurious observation. A data-quality mechanism should identify missingness without inventing an underlying state.

[Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md) owns limits of knowledge. The planned [Data Provenance and Lifecycle](README.md) reference will treat record origin and transformations.

## Selection, grouping, and aggregation

Operations can alter scope or grain:

- **Selection** chooses records or fields under criteria.
- **Grouping** forms subsets with shared values or specified relationships.
- **Aggregation** summarizes a group into a count, statistic or other derived value.
- **Joining** relates records based on explicit keys or predicates and can multiply record counts under one-to-many or many-to-many matches.

A group summary is **not** the same object as its constituent individual records. Dropping identifiers or timestamps can make it impossible to reconstruct original data, even when a summary is arithmetically correct.

For the example, grouping by `device_id` creates D7 and D8 groups. Counting records produces 2 and 1, respectively. Counting distinct **device identifier values** produces 2 for the whole dataset. The identifier count is not independent proof that exactly two distinct physical devices existed. A clear analytical statement specifies which count is being reported.

## Record versus event versus entity

One event can generate multiple records, one record can combine several observations, and a dataset can represent entities rather than events. These correspondences are choices made by the collection and representation design. A log record should not automatically be treated as identical to the real-world event it describes.

[State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) supplies event concepts; [Observation](../scientific-analytical-reasoning/observation.md) supplies acquisition semantics. Data may include errors, duplication, omissions and corrections; record counts do not establish real-world occurrence counts without a defended mapping.

## Related representation structures

A dataset may be encoded as CSV, JSON, binary records, graph statements or another format. Those forms differ in schema capabilities, typing, ordering and preservation of identity. Record granularity does not prescribe one storage engine, query language or serialization format.

The [W3C RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/) specification defines an RDF graph as a set of triples and RDF datasets as collections of graphs. This is an example of a representation with a different natural unit than a row in a table, not proof that all datasets should be graph-shaped.

### Sources

- [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/).
- [IETF RFC 8259: JSON](https://www.rfc-editor.org/rfc/rfc8259).
- [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/).

**Editorial status:** Substantive draft. Aggregation calculations, database claims and RDF comparisons require scoped technical review. No assessment or schema adoption is introduced.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
