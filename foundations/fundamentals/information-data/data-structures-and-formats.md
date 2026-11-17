# Data Structures and Formats

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Data structures and formats  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 02 audit](../WAVE-B-TECHNICAL-REVIEW-02.md); no independent human peer review

## Information organization and information encoding are different

A **data structure** organizes data elements and their relationships so that a representation can be interpreted, accessed, or manipulated. A **data format** defines conventions for representing or exchanging information, often as characters or bytes. A **serialization** maps in-memory or conceptual information into an encoded representation; **deserialization** reconstructs an interpretation from that representation.

A logical structure and its serialized form need not coincide. A collection of records may be encoded as comma-separated text, a JSON array, a structured binary representation, or another format. The choice affects supported types, ordering, explicitness, interoperability and recoverable detail, but does not independently establish factual truth.

This subject owns **general organization and representation**. [Data Types](data-types.md) owns value domains and type interpretation; [Schemas](../models-abstraction/schemas.md) owns admissibility constraints; [Computational Data Structures](../computation-algorithms/README.md) will own algorithmic operations and complexity of particular implementations.

## Logical organization: order, membership and relation

Common organizational forms include sequences, sets, mappings, tables and graphs:

| Logical organization | Essential relationship | Important qualification |
| --- | --- | --- |
| Sequence | Elements occupy ordered positions | Duplicates may be permitted |
| Set | Membership distinguishes included elements | Order and duplicates are not intrinsic to a mathematical set |
| Mapping | Keys associate with values | Key equality and duplicate handling require defined rules |
| Table | Fields/columns organize observations or tuples | Bag versus set semantics differ by system |
| Graph | Nodes and edges encode selected relations | Edge meaning depends on the model |

This is a comparison of familiar forms, not a ratified universal taxonomy or a requirement to store each in a particular way. A system may combine forms or supply different semantics under the same informal name.

[Sets and Relations](../mathematics-logic/sets-and-relations.md) owns membership and relations. [Graph Theory](../mathematics-logic/graph-theory.md) owns formal graph properties. [Datasets, Records, Fields, and Values](datasets-records-fields-and-values.md) owns dataset granularity.

## Serialization: format is not meaning

The text `[1,2,3]` can be parsed as a JSON array of three numbers under [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259). The bytes of that UTF-8 text are a serialization of the array, not the array's abstract mathematical identity. A receiver must know the relevant encoding and format rules to parse it correctly.

**JSON** defines a textual grammar for objects, arrays, strings, numbers, Booleans and null. It does not by itself define a domain-specific schema, date semantics, globally unique identifiers or arbitrary precision in every decoder.

**CSV** commonly represents records as delimited text fields. [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180) documents one interoperable convention, including quoting fields containing commas or line breaks and doubling an interior quote in quoted fields. Actual CSV dialects vary; a producer's documented dialect remains authoritative.

**CBOR**, defined by [RFC 8949](https://www.rfc-editor.org/rfc/rfc8949), is a binary serialization format for data items such as integers, text strings, byte strings, arrays and maps. It is not the only binary format and does not universally guarantee a unique encoded byte string for an abstract value without additional deterministic-encoding constraints.

A **format** defines an encoding convention; a **schema** further restricts admissible structures or values under chosen semantics. Well-formed serialization is therefore not proof of schema conformance or real-world correctness.

## Worked example: the same modeled observations in two formats

Suppose the conceptual dataset has two records:

```text
record 1: id=O1, device=D7, temperature_C=21.0
record 2: id=O2, device=D7, temperature_C=22.0
```

One possible CSV representation, under its specified column meanings, is shown below. **The displayed lines are illustrative**: RFC 4180 specifies CRLF record separators for its documented CSV convention, while other CSV dialects and transport conventions may use different separators:

```csv
id,device,temperature_C
O1,D7,21.0
O2,D7,22.0
```

One possible JSON representation is:

```json
[
  {"id":"O1","device":"D7","temperature_C":21.0},
  {"id":"O2","device":"D7","temperature_C":22.0}
]
```

These may describe the **same stipulated two observations**, but the textual representations are not structurally identical. In CSV, the value `21.0` is text whose numeric semantics follow the consumer's declared contract; in JSON it appears as a JSON number. The JSON array preserves an explicit item sequence; the CSV file's row order is present as textual order but whether it is semantically significant is a separate decision.

Neither format proves the sensor measured accurately. A schema may require a unit, version or source identifier not supplied in this simplified example.

## Structural fidelity and round trips

A **round trip** serializes and parses a value. Whether the output is equivalent to the input depends on the chosen notion of equivalence: identical bytes, equal parsed values, preserved key order, preserved numeric precision, or preserved application meaning are different requirements.

For example, `21.0` and `21` can denote the same numerical value in a mathematical model but are different text sequences. A decoder that converts both to one numeric representation may not preserve the original spelling.

Data transformations can also lose distinctions between absent and null fields, collapse duplicates, normalize text, reorder collections or replace precise values with rounded ones. Those losses need explicit documentation when meaningful to consumers.

## Operational boundaries

Data structures do not mandate a storage engine. A logical graph can be represented by adjacency lists, tables or serialized triples; these are different implementation choices. Efficient algorithms, memory management and complexity belong to [Computation & Algorithms](../computation-algorithms/README.md), not solely to the definition of a format.

[Databases and Queries](databases-and-queries.md) owns persistence and query mechanisms, while [Metadata](metadata.md) owns contextual descriptions. [Data Provenance and Lifecycle](data-provenance-and-lifecycle.md) owns representation lineage and changes.

### Sources

- [IETF RFC 8259: JSON](https://www.rfc-editor.org/rfc/rfc8259).
- [IETF RFC 4180: Common Format and MIME Type for CSV](https://www.rfc-editor.org/rfc/rfc4180).
- [IETF RFC 8949: Concise Binary Object Representation (CBOR)](https://www.rfc-editor.org/rfc/rfc8949).
- [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 02 technical audit](../WAVE-B-TECHNICAL-REVIEW-02.md). Complete source verification, independent human expert review and final publication acceptance remain separate and pending.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
