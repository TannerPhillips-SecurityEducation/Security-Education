# Data Types

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Data types  
**Development status:** Draft  
**Source review:** References listed; separate scoped claim-to-source audit pending

## Type constrains possible values and their interpretation

A **data type** is a defined category of values, often with associated operations, representations or validity rules in a specified computational or information model. Type semantics depend on the system or language. A data type should not be confused with the identity of an entity, the measurement kind of a physical quantity, a machine-learning classification, or an empirical claim about a recorded value.

An integer, string, Boolean and timestamp may each be treated as a data type, but their formal value domains vary by implementation. A programming language may have a fixed-width integer; a mathematical integer domain is unbounded. The distinction affects overflow and interoperability.

[Classification](../models-abstraction/classification.md) owns generic category membership, while [Schemas](../models-abstraction/schemas.md) owns rules for which fields and values are admissible in a structured representation.

## Values, representations, and operations

Three distinct layers are frequently conflated:

- **Abstract value:** the item being represented, such as integer forty-five.
- **Representation:** a bit sequence, text token or structured encoding used to communicate it.
- **Type semantics:** the permitted values and operations a system assigns to the representation.

The text string `"45"` and number `45` can look similar but do not have identical operations. String concatenation of `"4"` and `"5"` produces `"45"`; numeric addition yields `4+5=9`.

The same byte pattern may represent an unsigned integer, signed integer, character code, bit field or floating-point fragment. Correct interpretation depends on the declared type and encoding, not merely its visual appearance.

## Common type families without a universal taxonomy

Some systems distinguish Boolean, numeric, textual, enumerated, sequence, collection, record, variant and reference types. These examples describe **different system-dependent possibilities**, not an approved universal type hierarchy.

A **Boolean** commonly has true and false values. An **enumeration** permits one of a declared set of alternatives. A **record type** associates named fields with specified types. A **nullable or optional representation** adds rules for missingness or distinguished null values; it must not automatically be interpreted as epistemic ignorance.

The same type name can differ in representation across systems. For instance, a type labeled `number` in [JSON](https://www.rfc-editor.org/rfc/rfc8259) has a portable textual grammar, but consuming implementations can differ in numerical range and precision. JSON has no intrinsic date or arbitrary-precision integer type distinguished by the base syntax.

## Nominal, ordinal, interval, and ratio scales are measurement properties

Measurement scales distinguish what comparisons and transformations are meaningful for recorded quantities. Nominal identifiers support sameness/difference; ordinal values support ordering; interval scales support meaningful differences; ratio scales add a meaningful zero for ratios in the intended quantity kind.

These are **levels of measurement**, not automatically software storage types. Coding categorical labels as integers does not make the category quantitative. A device identifier `00123` may be a string that preserves leading zeros; converting it to integer `123` can erase meaningful representation details.

[Measurement](../scientific-analytical-reasoning/measurement.md) and [Units and Quantities](../mathematics-logic/units-and-quantities.md) govern the underlying measurement and dimensional concepts.

## Type checking, coercion, and validation

**Type checking** asks whether an expression or value is admissible under a type system. **Coercion** converts or interprets values according to specified rules. **Schema validation** checks a structured instance against additional representation constraints. A system that accepts a parsed value does not prove that it is semantically correct or faithfully measured.

For example, the string `"20"` might be converted to the number `20` by an application. Conversion can be appropriate if explicitly authorized, but it should not be silently assumed. Likewise, a numeric temperature without an associated unit may pass a number type check while remaining physically ambiguous.

## Worked example: nominal identifiers versus quantities

Suppose records contain `id="0007"`, `temperature_C=21.5`, and `state="ON"`. The id is best treated as a nominal identifier whose leading zeros may matter; `temperature_C` is a numeric reported value with a conventional unit in its field name; `state` is a categorical value.

Computing a numerical mean of the identifiers has no established interpretation. Computing a mean of valid, comparable temperature measurements may be meaningful under appropriate sampling assumptions. Type correctness is necessary for some operations but not sufficient for a defensible analysis.

## Boundaries and references

Data type is not synonymous with schema, ontology, format, or physical quantity. [Datasets, Records, Fields, and Values](datasets-records-fields-and-values.md) owns information granularity. [Data Structures and Formats](README.md) remains a future canonical subject for organization and exchange. [Numbers and Numerical Systems](../mathematics-logic/numbers-and-numerical-systems.md) owns arithmetic.

### Sources

- [RFC 8259: The JSON Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259).
- [W3C XML Schema Definition Language 1.1: Datatypes](https://www.w3.org/TR/xmlschema11-2/).
- [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/).

**Editorial status:** Substantive draft. Its generalizations across type systems and numeric representation must be tested in a dedicated source audit. No implementation-specific type system is mandated.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
