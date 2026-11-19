# Fundamentals | Administrative Editorial Pass 02: Reliance, Abstraction, and Query Execution

**Pass date:** November 19, 2026  
**Program:** [Administrative Editorial Passes](../../ADMINISTRATIVE-EDITORIAL-PASSES.md)  
**Scope:** Four previously Reviewed (model-assisted) Fundamentals articles; A0 targeted inspection, A1 clarity, A2 mechanism and assumptions, A3 independently checked worked examples, A4 supported cross-links, A5 scoped primary-source review.  
**Security Foundations:** New drafting remains paused at 39 Reviewed and 57 un-authored candidates.  
**Maturity:** Internal model-assisted administrative/technical check, not complete source verification, independent expert acceptance, or publication.

## 1. Before: bounded observed gaps

| Inspected canonical article | Observed explanatory gap | Actual change |
| --- | --- | --- |
| [Dependencies](systems-engineering/dependencies.md) | Failure propagation described correctly as conditional; no explicit derivation from reliance to Boolean failure logic or quantitative consequence of correlated dependencies | Added a success/failure transformation and a stated independent-versus-common-cause comparison |
| [Abstraction](models-abstraction/abstraction.md) | Many-to-one state map and soundness warning were present, but the required transition correspondence and counterexample mechanism remained implicit | Added distinction between state mapping and transition relation, with a cross-link to the formal worked proof |
| [Conceptual and Formal Models](models-abstraction/conceptual-and-formal-models.md) | Formal over-approximation described, but no complete small reachable-state example or proof direction | Added a four-state construction, trace table, spurious path, assumptions, and reachability safety implication |
| [Databases and Queries](information-data/databases-and-queries.md) | Logical query, schema, index and execution plan distinguished only briefly; actual mechanism of selecting access paths omitted | Added a query-to-access explanation, stable sample output, planner caveats, schema-on-read/write distinction, and safe EXPLAIN wording |

This pass **does not** assert that all Fundamentals subjects or every sentence in the four articles was audited. The historical review records remain unchanged, and article development states remain Reviewed (model-assisted).

## 2. Changes and scoped material claim checks

### Dependencies: why the topology is insufficient

A stipulated recorder needs sensor S and either storage B or C. For a single time instant: `Up = S AND (B OR C)`; therefore `Down = NOT S OR (NOT B AND NOT C)`. Under independent component down-state events of 0.02, 0.10, 0.10, the recorder down probability is `1 - 0.98(1 - 0.10×0.10) = 0.0298`. With only B: `1 - 0.98×0.90=0.118`. If B and C always fail together but their common failure is independent of S, the redundant pair's model is again `0.118`.

**Claim groups D1–D3:** (D1) dependency arrows versus operational success criteria; (D2) De Morgan's law and fault-tree event gates; (D3) independent versus common-cause probability, model population and countercase.

**Source reviewed:** [NASA *Fault Tree Handbook with Aerospace Applications*, v1.1 (August 2002), Chapter 6, printed p. 72](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf) visually inspected for inclusive OR event probability and independent versus dependent intersections. The example itself is editorial and hypothetical. No historical outage sample, reliability distribution, repair dynamics, or real system confidence interval was inferred.

### Abstract-to-concrete safety: implication direction

The added four-state transition model maps both c1 and c2 to READY. It has `c0→c1` and `c2→c3`, but the initial state c0 cannot reach c2. The conservative abstract relation admits IDLE→READY→ACTIVE as a spurious trace. The trace is an over-approximation, not a demonstrated concrete execution.

**Claim groups M1–M3:** (M1) many-to-one mapping does not define transitions; (M2) initial/step/bad-state coverage gives `α(Reach_C)⊆Reach_A`; (M3) abstract absence of reachable bad states implies concrete absence, not vice versa, and a spurious trace is a valid counterexample to reversing the implication.

**Source reviewed:** [*Handbook of Model Checking*, Chapter 30, §5.1 (2018), p. 32 of chapter](https://www.cs.cmu.edu/~aplatzer/pub/HBMC.pdf), visually inspected for abstraction mapping, step correspondence and the conservative direction of the safety lemma. The small model and its reachability calculation were independently authored and checked here. The implication does not cover physical-world fidelity or arbitrary liveness properties.

### Query requests versus storage access

The existing observation rows were reused. Filtering for `device_id='D7'` and ordering observation IDs produces O1 then O2 regardless of whether a correct engine chooses a sequential scan or valid index-based access, under the same logical data snapshot. A query plan is a cost-dependent implementation choice, not a different data model or proof of source truth.

**Claim groups Q1–Q3:** (Q1) logical query versus physical access; (Q2) index availability, read/write schema policy and overhead are distinct; (Q3) PostgreSQL EXPLAIN describes a plan while EXPLAIN ANALYZE actually executes the statement.

**Sources reviewed:** [PostgreSQL 18 *Using EXPLAIN*](https://www.postgresql.org/docs/18/using-explain.html) and [PostgreSQL 18 *Indexes*](https://www.postgresql.org/docs/18/indexes.html). The toy SQL query was **not run** against a database; no performance result or physical plan was fabricated.

**Total bounded material claim groups assessed: 9** (3 dependency, 3 model, 3 database). This is an internal editorial claim check; it does not supersede the previous technical-review audits or confer Source-Verified status.

## 3. Review, countertests, and integrity

- **Mathematics:** recompute `0.10×0.10=0.01`; `0.98×0.99=0.9702`; `1-0.9702=0.0298`; `0.98×0.90=0.882`; `1-0.882=0.118`.
- **Formal reachability:** from c0, only c0 and c1 reachable; abstract IDLE→READY→ACTIVE is admitted; concrete c3 remains unreachable. The implication is one-way only.
- **Countertests:** perfectly correlated storage invalidates independence; omitting c2→c3 from the abstraction invalidates transition coverage; the existence of an index does not force its selection; a query's correct output does not establish source-data truth.
- **Change scope:** No new subjects, relocated owners, status promotions, taxonomy ratifications, Security Foundations drafts, or publication claims.
- **Structural checks:** New relative article links were checked against fetched canonical paths. Repository GitHub Actions results should be evaluated against the commit carrying this pass, separately from the technical checks above.

## 4. Residual work and next priority

The edited articles remain only **Reviewed (model-assisted)**. Source-to-claim verification for all material passages, independent technical review, and final publication acceptance remain open. The new probabilities are stipulated, not empirical. Real index plans and timings remain environment-dependent. The example formalization proves a conditional model-level statement, not an assertion about physical equipment.

Next editorial candidates: [Verification and Validation](systems-engineering/verification-and-validation.md) as an evidence bridge, [Data Provenance and Lifecycle](information-data/data-provenance-and-lifecycle.md) as an auditability bridge, and [Search and Information Retrieval](information-data/search-and-information-retrieval.md) as an access-method bridge. Selection remains evidence-led rather than a fixed article quota.

[Fundamentals](README.md) · [Administrative Program](../../ADMINISTRATIVE-EDITORIAL-PASSES.md) · [Previous Pass](ADMINISTRATIVE-EDITORIAL-PASS-01.md)
