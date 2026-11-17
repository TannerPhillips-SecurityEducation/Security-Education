# Wave B Technical Review: Batch 02

**Review date:** November 17, 2026  
**Scope:** Data Structures and Formats; Metadata; Databases and Queries; Data Provenance and Lifecycle.  
**Method:** Reopened four GitHub drafts; tested their principal CSV/JSON, SQL and temperature-conversion examples; inspected the cited IETF, W3C, DCMI, ISO catalog and PostgreSQL documentation for the corresponding claim families; and reopened all distinct relative Markdown file destinations referenced in the drafts.  
**Disposition:** **24 material claim families reviewed; four references pass scoped model-assisted technical review** after the documented corrections. This is not exhaustive claim-by-claim verification, independent expert peer review or final publication acceptance.

## Claim-to-source ledger

### Data Structures and Formats

[Reviewed article](information-data/data-structures-and-formats.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| SF-01 | Data structures, formats and serialization express distinct organization and encoding concerns | [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) and [RFC 8949](https://www.rfc-editor.org/rfc/rfc8949); conceptual distinction retained, not a new classification schema |
| SF-02 | Sequence, set, map, table and graph differ in their core organization | [RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/) and [JSON](https://www.rfc-editor.org/rfc/rfc8259); informal comparison not a universal type hierarchy |
| SF-03 | JSON supports textual arrays, objects and numbers without application-specific units | RFC 8259; the illustrative JSON array parses successfully and produces two records |
| SF-04 | CSV fields are strings under the illustrated reading contract, and delimiters/quotes require dialect rules | [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180); illustrative CSV parses as two rows, numeric-looking fields initially read as text; **corrected** displayed-line-break versus CRLF normative convention |
| SF-05 | CBOR does not force uniquely determined bytes absent deterministic encoding requirements | [RFC 8949 §4.2](https://www.rfc-editor.org/rfc/rfc8949#section-4.2); deterministic profile requirements are distinct from generic well-formedness |
| SF-06 | Reversible parsing, byte identity and semantic equivalence differ | RFC 8259; `21.0` and `21` may have equal interpreted numerical values but different spellings; no false claim of universal lossless round-trip |

### Metadata

[Reviewed article](information-data/metadata.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| MD-01 | Metadata describes/qualifies a chosen subject and may be context-relative | [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/); metadata-as-content boundaries are interpretive, not immutable |
| MD-02 | Created, reported and modified timestamps are distinct assertions | DCMI `created`/`modified` properties and article's stipulated example; syntax alone does not establish event provenance |
| MD-03 | Discovery, description, administration, provenance and version context can overlap | [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/); categories are illustrative purposes, not additional approved knowledge areas |
| MD-04 | Metadata may be embedded or externally associated with a resource | DCMI/DCAT; references require an explicit identity relationship, and metadata assertions can become stale |
| MD-05 | Contextual metadata improves interpretation without proving instrument accuracy | Hypothetical 21.0 °C record; semantics, timing, origin and calibration remain separate evidentiary obligations |
| MD-06 | Metadata is not synonymous with schema, ontology or full provenance history | [PROV-DM](https://www.w3.org/TR/prov-dm/) and DCAT 3; canonical ownership boundaries retained |

### Databases and Queries

[Reviewed article](information-data/databases-and-queries.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| DQ-01 | Logical database, DBMS, data model and query result differ | [ISO/IEC 9075-1:2023 catalog](https://www.iso.org/standard/76583.html) and [PostgreSQL query overview](https://www.postgresql.org/docs/current/queries.html); distinct concepts, not a mandated engine |
| DQ-02 | Relational operations include filtering, projection, joins and aggregation | [PostgreSQL table expressions](https://www.postgresql.org/docs/current/queries-table-expressions.html); treatment does not equate SQL bag results with mathematical sets |
| DQ-03 | Worked grouped SQL query returns counts and means by identifier | Executed using SQLite: D7 -> count 2, mean 21.5; D8 -> count 1, mean 19.0; consistent with [PostgreSQL aggregate documentation](https://www.postgresql.org/docs/current/functions-aggregate.html) |
| DQ-04 | COUNT(DISTINCT device_id) counts unique non-null identifier values | Executed under stipulated rows: 2; not a count independently verifying physical devices |
| DQ-05 | SQL null comparisons, aggregate behavior and unordered result rows require explicit semantics | Tested SQLite `NULL=NULL` (unknown), `NULL IS NULL` (true); `COUNT(*)` versus `COUNT(column)` differentiated; [PostgreSQL null functions](https://www.postgresql.org/docs/current/functions-comparison.html) |
| DQ-06 | ACID guarantees depend on system and isolation level; SPARQL has four query forms | [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) and [SPARQL 1.1](https://www.w3.org/TR/sparql11-query/); no false implication of universal serializability |

### Data Provenance and Lifecycle

[Reviewed article](information-data/data-provenance-and-lifecycle.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| PL-01 | Provenance and data lifecycle describe overlapping but distinct concerns | [W3C PROV-DM](https://www.w3.org/TR/prov-dm/); history claims distinct from management over time |
| PL-02 | PROV entities, activities, agents, usage, generation and derivation have defined meanings | PROV-DM §2 and §5; article presents standard examples, not repository-invented ontology predicates |
| PL-03 | A provenance graph records assertions, not automatic confirmation of causal truth | PROV-DM; derivation assertions and source authenticity require separate evidence |
| PL-04 | Data lifecycle stages can iterate, branch or differ by resource type | Explicit editorial modeling principle; does not impose a universal seven-stage policy |
| PL-05 | Worked Fahrenheit–Celsius transformation and R1/A1/R2 lineage | Independently computed `(68-32)×5/9=20`; PROV usage/generation/derivation relation examples have appropriately conditional interpretation |
| PL-06 | Hash equality, version identity, retention, deletion and replicas require scope | **Corrected** overly compressed hash explanation: equal hashes are evidence, not absolute proof of identical bytes due to possible collisions. Deletion scope and provenance reliability remain conditional |

## Corrections made before acceptance

1. **Data Structures and Formats:** Clarified that the displayed CSV rows are illustrative and RFC 4180's documented record separator is CRLF. Other CSV dialects can differ; the example does not claim universal CSV semantics.
2. **Data Provenance and Lifecycle:** Distinguished matching content hashes from a proof of byte identity; collision assumptions, encoded representation and authorship verification remain independent.
3. **No additional corrections:** The other two articles' scoped conceptual claims and calculations passed as written.

## Executed examples and link checks

- A Python standard-library CSV reader parsed the two illustrated CSV rows with temperature strings; a JSON parser read the corresponding numeric fields as numbers.
- A SQLite in-memory test, using the article's three-row dataset and its literal SQL queries, returned D7=(2,21.5), D8=(1,19.0), and two distinct non-null device identifiers. `NULL = NULL` evaluated to unknown and `NULL IS NULL` to true in that engine.
- The Fahrenheit–Celsius example returned exactly 20 °C for the stipulated 68 °F input.
- **45 relative Markdown link occurrences** in the four articles resolved to **19 distinct file destinations**. All 19 destinations were fetched from the repository through GitHub; **19/19 resolved**. Anchor fragments, external URLs and repository-wide links were not exhaustively checked.
- SQL execution was tested in SQLite, **not** against every conformant SQL implementation or the paid full text of ISO/IEC 9075. The normative and implementation sources were compared at the claim-family level.

## Architecture and acceptance disposition

- **Data Structures and Formats** owns representation and serialization; **Metadata** owns contextual description; **Databases and Queries** owns query and persistence mechanisms; **Data Provenance and Lifecycle** owns origin/derivation and data management over time.
- The related approved areas retain ownership of schemas, measurement, graph theory, evidence, uncertainty and state/events/transitions.
- All four articles are **Reviewed (model-assisted)** with **Core claims checked**, not **Verified** or **Published**. Independent human peer review and final publication acceptance remain pending.
- Information & Data has **9/9 authored and internally Reviewed** references. Total: **37 Reviewed**, **0 Draft**, **72 Inventoried without article** across the unchanged **109 approved subject headings**.
- G-01 mathematical breadth, G-04 general temporality and G-06 AI/ML remain open scope decisions. No Knowledge Checks, Practical Assessments, new subject headings or repository-wide schema mandates were introduced.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
