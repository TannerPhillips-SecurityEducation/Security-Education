# Schemas

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Schemas  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## A schema states expectations for a representation

A **schema** is an explicit description of the structure, admissible values, relationships, and constraints of information or model elements for a specified purpose. Schemas can be informal, graphical, logical, or machine-interpretable. Different schema languages expose different constraint capabilities and validation semantics.

A schema does not automatically establish that records are truthful, that sensors are correct, or that a description matches real-world behavior. **Conformance to a schema is conformance to specified representation rules**, under a particular implementation and validation process.

[Conceptual and Formal Models](conceptual-and-formal-models.md) addresses broader modeling and semantics; [Ontologies and Taxonomies](ontologies-and-taxonomies.md) addresses kinds and conceptual relations. [Information & Data](../information-data/README.md) owns actual data encoding, records and formats.

## Structural, value, and relational constraints

A schema may specify:

- **Fields and structure:** allowed properties, nesting, records and references.
- **Types and domains:** text, integer, number, boolean or more specialized categories.
- **Presence and multiplicity:** required, optional, nullable, single or repeated values.
- **Ranges and patterns:** bounds on numbers, lengths, enumerations and text patterns.
- **Relationship constraints:** uniqueness, keys, foreign keys, referential integrity or allowed combinations.
- **Versioning rules:** which representation contract a record claims to satisfy.

These are mechanisms used in some schema languages, not features that every schema system universally supports. Constraints must be read under the precise standard and version being used.

## Worked example: record structure versus truth

A hypothetical schema expects:

```text
DeviceRecord:
  id: nonempty string
  temperature_C: number
  state: one of {ON, OFF, UNKNOWN}
```

A record `{id:"device-17",temperature_C:20.5,state:"ON"}` conforms to those *stated* conditions. A record with `temperature_C:"warm"` does not satisfy the numeric-type requirement, absent additional coercion rules.

Yet a conforming record can still misreport the physical temperature. A correct schema checks the representation; it does not independently validate the observation, calibration or causality. The string `UNKNOWN` is a declared **field value** in this toy schema, and should not be confused with the broader epistemic distinction between whether a claim is known and its underlying truth value.

To avoid ambiguity, a production contract would also define measurement unit, timestamp semantics, provenance, null handling, permitted additional fields and version identity as needed. **Those extra requirements are not presumed universal.**

## JSON Schema: constraints within a particular vocabulary

[JSON Schema](https://json-schema.org/specification) is one machine-readable approach for describing and validating JSON instances. A simplified illustrative example:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["id", "temperature_C", "state"],
  "properties": {
    "id": {"type": "string", "minLength": 1},
    "temperature_C": {"type": "number"},
    "state": {"enum": ["ON", "OFF", "UNKNOWN"]}
  },
  "additionalProperties": false
}
```

The example disallows unspecified top-level properties, requires the three named properties, and constrains their values according to the stated dialect. It does **not** mandate that all schemas use JSON, require keys, or close the world to unspecified fields. JSON Schema itself supports additional dialect and keyword semantics.

## Relational and graph-related constraints

In the relational model, a database schema may describe relation headings, attribute domains, keys and integrity constraints. A **primary key** identifies rows according to the database's constraints; a **foreign key** links allowed references between relations. SQL implementations impose additional details concerning nulls, defaults, type conversion and enforcement.

Graph representations may also be constrained. RDF data can be validated with [SHACL](https://www.w3.org/TR/shacl/), which describes shapes and constraints over RDF graphs. SHACL validation is not equivalent to OWL logical entailment, although the two may be used together. A particular RDF graph's conformance to a SHACL shape does not establish that its asserted statements are real-world facts.

## Schemas, data types, and formats

These must not be conflated:

| Concept | Main question |
| --- | --- |
| Data type | What operations or values characterize an item? |
| Schema | Which structures and constraints count as conformant? |
| Data format | How is the content encoded and exchanged? |
| Ontology | What kinds and relationships are modeled, and with which semantics? |
| Validation | Does a candidate satisfy stated criteria under a chosen procedure? |

For example, JSON is a format, while JSON Schema is a vocabulary for specifying constraints on JSON instances. The fact that a file parses as JSON does not imply that it satisfies an application schema.

## Evolution and compatibility

Schema evolution can introduce, remove, rename or reinterpret fields and constraints. The operational effects depend on reader/writer behavior, deployment sequence and chosen compatibility rules. An optional field in a permissive reader may preserve some old data, but it does not prove full semantic or behavioral compatibility.

**Syntactic compatibility** concerns successful parsing or conformance. **Semantic compatibility** concerns whether consumers interpret the same data consistently. **Behavioral compatibility** concerns whether systems still meet intended expectations. These are overlapping but non-equivalent claims.

A version string without migration policy, tests or stated consumer expectations does not ensure safe evolution. [Data Provenance and Lifecycle](../information-data/README.md) and [System Lifecycle](../systems-engineering/README.md) cover neighboring ownership.

## Scope and editorial boundary

This article introduces no universal schema for the repository, no required record IDs or ontology predicates, and no new validation engine. The example schemas are pedagogical, not normative specifications for specialized domains.

### Sources

- [JSON Schema Specification](https://json-schema.org/specification).
- [IETF JSON Data Interchange Format (RFC 8259)](https://www.rfc-editor.org/rfc/rfc8259).
- [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/).
- [W3C OWL 2 Overview](https://www.w3.org/TR/owl2-overview/).

**Editorial status:** Substantive draft; tool/dialect claims and worked examples require scoped second-pass source verification. No publication acceptance implied.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
