# Databases and Queries

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Databases and queries  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 02 audit](../WAVE-B-TECHNICAL-REVIEW-02.md); no independent human peer review

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

## Relational and entity–relationship models describe different things

The **relational model** represents relations as sets of tuples under a mathematical schema and interprets operations such as selection, projection, joins and constraints. A database SQL table may permit duplicate rows and null values under specific SQL semantics, so it is not automatically identical to a mathematical set of complete tuples. Physical indexes, storage layouts and query execution plans implement the chosen logical behavior but are not part of the pure relational model.

An **entity–relationship (ER) model** is a conceptual design technique representing entity types, relationships, attributes and constraints. It helps describe the intended data domain before deciding how the entities and relationships become relational tables, graph structures or another implementation. An ER diagram is therefore **not** equivalent to a normalized SQL schema, much less to a particular physical storage engine.

Consider Customers(customer_id, name) and Orders(order_id, customer_id, total). Each order may be associated with one customer through a reference to customer_id; a customer may have several orders. A conceptual one-to-many association can be implemented by a foreign key, but only if its integrity and optionality constraints have actually been declared and enforced.

**Worked interpretation:** If customer C1 has three order rows and C2 has one, an inner join grouped by customers produces **four order-associated joined rows**. Counting joined rows is not the same as counting distinct customers (**two**). An inner join also omits customers without matching orders. Queries need explicit grain, key, missingness and aggregation choices.

The relational model and ER modeling do not determine whether the data are historically accurate. [Data Provenance and Lifecycle](data-provenance-and-lifecycle.md) owns records of data origin and transformation; [Schemas](../models-abstraction/schemas.md) owns general field and validation contracts.

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

## From the logical query to physical access

A query declares **what result is requested**, while an execution plan selects **how an implementation will obtain that result**. In a relational DBMS, a useful analytical separation is:

| Concern | Question it answers | Example |
| --- | --- | --- |
| Data and schema | Which records, types, constraints and meanings exist? | `observations(device_id, temperature_c)` |
| Logical query | Which qualifying records and result operations are requested? | `WHERE device_id = 'D7'` |
| Physical organization and access | How are rows/columns/pages arranged and which access paths exist? | Heap/table data, B-tree index, sequential scan |
| Execution plan | Which operations and access paths are chosen for this request? | Sequential scan with filter, or index scan plus row fetch |
| Result and provenance | Which values are returned, based on which data and observation history? | Two stored observations for identifier D7 |

This is a **separation of responsibilities**, not an assertion that every DBMS implements the same pipeline. Parsing and binding a query, rewriting/optimizing logical operations, selecting physical operators, reading data, and applying final result semantics can be organized differently across systems.

Using the earlier three-row `observations` example:

```sql
SELECT observation_id
FROM observations
WHERE device_id = 'D7'
ORDER BY observation_id;
```

The stipulated result is `O1` followed by `O2`. A table scan can inspect each stored row and apply the predicate. If a suitable index on `device_id` exists, an engine **may** use it to identify candidate locations, then fetch qualifying rows and satisfy the requested ordering. The mere presence of an index does **not** require the optimizer to use it; small tables or nonselective predicates can favor a scan. Any correct plan under the same data visibility and query semantics must return the same qualifying logical result. Inappropriate index behavior, inconsistent snapshots, or engine defects are outside that correctness premise.

An **index** is an auxiliary access structure, not a schema, a source-of-truth guarantee, or a synonym for the query itself. It can reduce search work for selected predicates, but it consumes storage and imposes maintenance costs on changes. An unindexed or 'indexless' access path may still support queries by scanning or other engine-specific structures. Whether a column is validated at ingestion (**schema on write**) or interpreted when read (**schema on read**) is another axis of design: it changes when interpretation and conformance checks occur, not the definition of indexing. Neither policy ensures the original recorded measurement is true.

For PostgreSQL 18, the primary documentation explicitly distinguishes sequential, index, and bitmap scans and describes cost-based plan selection in [Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html); [Indexes](https://www.postgresql.org/docs/18/indexes.html) documents performance gains and maintenance overhead. `EXPLAIN` without `ANALYZE` reports a proposed plan rather than measured execution. **`EXPLAIN ANALYZE` actually executes the statement**, which matters especially for write statements with side effects. This article does not claim the toy query was executed against PostgreSQL or that any specific plan or timing was observed.

For deeper conceptual boundaries, see [Schemas](../models-abstraction/schemas.md), [Search and Information Retrieval](search-and-information-retrieval.md), [Data Provenance and Lifecycle](data-provenance-and-lifecycle.md), and [Data Structures and Formats](data-structures-and-formats.md).

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

- [ISO/IEC 9075-2:2023 SQL/Foundation (standard scope)](https://www.iso.org/standard/76584.html).
- [PostgreSQL documentation: Table Expressions and Joins](https://www.postgresql.org/docs/current/queries-table-expressions.html).


- [ISO/IEC 9075-1:2023, Database Languages SQL: Framework](https://www.iso.org/standard/76583.html).
- [ISO/IEC 9075-2:2023, SQL/Foundation](https://www.iso.org/standard/76584.html).
- [PostgreSQL documentation: Queries](https://www.postgresql.org/docs/current/queries.html), as an illustrative SQL implementation.
- [W3C SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 02 technical audit](../WAVE-B-TECHNICAL-REVIEW-02.md). Complete source verification, independent human expert review and final publication acceptance remain separate and pending.

**Additional technical review (November 18, 2026):** The established-framework/model additions above were checked under the [Wave G 39-family scoped model-assisted review](../WAVE-G-TECHNICAL-REVIEW-01.md) (three material claim groups for this article). The earlier audit record remains historical. This does not establish complete source-level verification, independent expert review, or final publication acceptance.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
