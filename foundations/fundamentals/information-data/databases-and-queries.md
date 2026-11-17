# Databases and Queries

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Databases and queries  
**Development status:** Draft  
**Source review:** References listed; scoped claim-to-source audit pending

## Databases manage information; queries ask defined questions

A **database** is an organized collection of information managed under specified structures, integrity rules and operational mechanisms. A **database management system** (DBMS) provides means to define, store, retrieve or modify data, often also providing concurrency, recovery and access management. A **query** is a request to retrieve, test, transform or summarize information under a defined data model and language.

The conceptual database, logical schema, physical storage and query result are distinct. A logical relation need not be stored physically as a literal two-dimensional table. A document database, graph database and relational database may represent similar facts under different models and query mechanisms.

[Data Structures and Formats](data-structures-and-formats.md) covers representation and serialization. [Schemas](../models-abstraction/schemas.md) covers conformance constraints. [Datasets, Records, Fields, and Values](datasets-records-fields-and-values.md) covers grain.

## Models and operations

A relational model organizes information into relations of tuples with typed attributes under a specified schema. SQL implements a widely used family of languages for interacting with relational systems, while introducing practical behavior such as duplicate-preserving query results and null markers that differs from pure mathematical set semantics.

Other systems may use document-oriented retrieval, graph-pattern matching, key-value lookup or other operations. The choice of query language is not a universal definition of a database.

Query operations commonly include:

- **Filtering/selection:** restrict which records satisfy a predicate.
- **Projection:** choose which attributes appear in a result.
- **Joining:** relate information across sources under declared matching conditions.
- **Grouping:** form subsets of records for comparison or aggregation.
- **Aggregation:** calculate group-level statistics, counts or other summaries.
- **Ordering:** impose a defined presentation order, when supported.

These words describe general operations; exact SQL syntax, null handling, and duplicate semantics are language-specific. [Sets and Relations](../mathematics-logic/sets-and-relations.md) owns formal mathematical relations, and [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns inferential statistics.

## Worked example: query changes what is counted

Suppose a table `observations` contains these stipulated rows:

| observation_id | device_id | temperature_c |
| --- | --- | ---: |
| O1 | D7 | 21.0 |
| O2 | D7 | 22.0 |
| O3 | D8 | 19.0 |

In SQL, a grouped summary might be expressed as:

```sql
SELECT device_id,
       COUNT(*) AS observation_count,
       AVG(temperature_c) AS mean_temperature_c
FROM observations
GROUP BY device_id;
```

Under this example's no-null numeric values, the result contains D7 with 2 observations and mean `21.5`, and D8 with 1 observation and mean `19.0`. The query counts **records** grouped by an identifier, not verified real-world devices.

A separate SQL query:

```sql
SELECT COUNT(DISTINCT device_id) AS distinct_ids
FROM observations;
```

returns `2` under the example's values. This is a count of distinct **non-null identifier values** under the database's equality rules. It does not prove the number of physical devices.

## Missingness and result semantics

SQL null is a marker with special semantics. A predicate such as `temperature_c = NULL` does **not** correctly test whether a value is null in standard SQL; `IS NULL` is the appropriate predicate. With standard SQL's three-valued truth semantics, comparisons involving null generally evaluate to unknown rather than true or false.

`COUNT(*)` counts result rows; `COUNT(temperature_c)` counts rows where that expression is non-null under standard SQL semantics. If some temperature fields are null, those counts may differ.

A result table is not guaranteed to appear in a particular row order without an ordering clause such as `ORDER BY`, unless some other specified contract provides ordering. Record count, duplicate handling and aggregation therefore require explicit query semantics.

[Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md) owns epistemic unknowns, which should not be equated with every implementation's null marker.

## Integrity, transactions and operational behavior

A schema can state keys, reference constraints, allowed values and other integrity conditions. A DBMS may provide transactions to coordinate logical operations, with properties commonly summarized as **atomicity, consistency, isolation and durability (ACID)**. The scope and guarantees of these terms depend on the implementation and transaction configuration.

**Atomicity** concerns all-or-nothing effects under the transaction contract. **Isolation** concerns permitted interactions between concurrent operations, not proof that all applications observe one globally serialized history. **Durability** concerns persistence guarantees after acknowledged commits within documented failure assumptions. A database constraint can prevent some inconsistent representations, but it does not prove that the stored data matches external reality.

Indexes and execution plans can improve performance but must preserve the defined semantics of a correct query. Performance characteristics, transaction anomalies and distributed behavior require additional system assumptions and are developed in specialized domains.

## Queries across graph representations

The W3C [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) expresses graph-pattern queries over RDF datasets, with `SELECT`, `ASK`, `CONSTRUCT` and `DESCRIBE` forms. A graph pattern is not the same as a SQL table row, although mappings and integrations can exist.

Queries can retrieve a logically correct result from incomplete, biased or incorrect source data. **Query correctness is not evidence correctness.** Provenance, observation quality, scope and assumptions determine how findings should be interpreted.

## Canonical boundaries and sources

This article does not choose a database engine, SQL dialect, indexing method, schema or graph platform for the Security Education repository. [Metadata](metadata.md) describes dataset context, and [Data Provenance and Lifecycle](data-provenance-and-lifecycle.md) describes the origin and transformations of underlying records.

### Sources

- [ISO/IEC 9075-1:2023, Database Languages SQL: Framework](https://www.iso.org/standard/76583.html).
- [ISO/IEC 9075-2:2023, SQL/Foundation](https://www.iso.org/standard/76584.html).
- [PostgreSQL documentation: Queries](https://www.postgresql.org/docs/current/queries.html), as an illustrative SQL implementation.
- [W3C SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/).

**Editorial status:** Substantive draft. SQL result calculations and language semantics are examples requiring a scoped technical audit; no particular vendor product is adopted as canonical.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
