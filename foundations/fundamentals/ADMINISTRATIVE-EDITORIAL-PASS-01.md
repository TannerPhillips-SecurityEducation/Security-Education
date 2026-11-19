# Fundamentals | Administrative Editorial Pass 01: Readability and Derivation Depth

**Pass date:** November 19, 2026  
**Program:** [Administrative Editorial Passes](../../ADMINISTRATIVE-EDITORIAL-PASSES.md), applying **A0 baseline sample**, **A1 conceptual clarity**, **A2 in-depth mechanical explanation** and **A3 worked reasoning**.  
**Scope:** A bounded cross-area sample of **10 existing Fundamentals articles**; two substantive improvements committed under the existing Systems & Engineering area. **No Security Foundations new articles or taxonomy changes**.  
**Publication status:** This is a model-assisted administrative and scoped technical pass, **not** a complete corpus review, independent expert review, full source verification, new taxonomy approval or Published status.

## 1. Baseline: what was inspected

The following ten article files were retrieved from the repository at the start of this pass. Their content structure, existing example/derivation patterns, source/evidence notes and immediate cross-article relationships were inspected at varying depth; the two indicated targets received direct full-text inspection, substantive editing and separate verification.

| Existing article | Observed content | Administrative disposition |
| --- | --- | --- |
| [Graph Theory](mathematics-logic/graph-theory.md) | Four-vertex example, handshake sum, paths, trees and DAG distinctions; previous scoped correction of a false “complete graph” claim remains documented | **No edit** in this pass; preserve the established audit and formulas |
| [Probability and Statistics](mathematics-logic/probability-and-statistics.md) | Conditional probability, independence and Bayesian example with declared prior and rates | **No edit**; future depth candidate for explicit base-rate and decision-threshold interpretation |
| [Causality and Correlation](scientific-analytical-reasoning/causality-and-correlation.md) | Numeric common-cause counterexample plus conditional versus interventional interpretation | **No edit**; future optional depth in collider conditioning and evidence limitations |
| [Abstraction](models-abstraction/abstraction.md) | Many-to-one state mapping and explicit caution that mapping alone does not establish sound transition abstraction | **No edit**; preserve this non-equivalence; a future example may formalize simulation preservation |
| [Conceptual and Formal Models](models-abstraction/conceptual-and-formal-models.md) | Syntax/semantics distinction, transition-system illustration and model-to-world proof obligations | **No edit**; suitable for later relationship pass with abstraction and validation |
| [Information Theory](information-data/information-theory.md) | Self-information, entropy, mutual information, DMC capacity and a perfect-versus-independent observation example | **No edit**; mathematical scope and semantic-value distinction remain important |
| [Databases and Queries](information-data/databases-and-queries.md) | SQL grouping, record-versus-entity grain, NULL, three-valued logic and a basic integrity/transaction distinction | **No edit**; future candidate for deeper schema/index/storage/search explanation |
| [Dependencies](systems-engineering/dependencies.md) | Directed reliance, AND/OR alternatives, cycles and an 11-unit critical-path worked example | **No edit**; important prerequisite for both revised articles |
| [Reliability and Failure](systems-engineering/reliability-and-failure.md) | Correct but compressed reliability/availability/maintainability definitions and two separate basic numerical examples | **Improved.** Added one common stochastic scenario showing why failure-free interval reliability and long-run availability differ |
| [Queueing and Service-System Models](systems-engineering/queueing-and-service-system-models.md) | Little's law, M/M/1 total time and occupancy, and prose warning against conflating waiting time with full-system time | **Improved.** Derived queue-only waiting/occupancy, added a two-load comparison and checks for scope and units |

This is **a ten-file sample**, not a statistically representative sample of the approximately 120 currently inventoried canonical Fundamentals subjects. The table records observed editorial opportunities, **not** fabricated article scores or a claim that every technical assertion across all ten was source-verified.

## 2. Revision A | Reliability versus availability

**Article:** [Reliability and Failure](systems-engineering/reliability-and-failure.md)  
**Observed depth gap:** The original article defined \(R(t)=P(T>t)\) for nonrepairable service and separately gave \(A=U/(U+D)\) with 90 units up/10 units down. It explicitly warned that availability was **not** failure-free survival, but it did not work through both quantities for **one consistent stipulated process**.

**Change made:** Added a section **Why reliability and availability can have very different percentages**, using one hypothetical repairable service with exponentially distributed up periods (mean 90 hours), restoration periods with mean 10 hours, stationary renewal-cycle assumptions and a declared no-hidden-degraded-state condition.

For an exponential time to failure with constant hazard \(\lambda=1/90\) per hour:

\[
R(90)=e^{-(1/90)90}=e^{-1}=0.3678794412.
\]

Long-run availability of the same up/down renewal model:

\[
A=\frac{90}{90+10}=0.90.
\]

Therefore the same toy service may be operational **90% of the long-run time** while the probability of remaining **continuously failure-free for the next 90 hours** is only about **36.8%**. The difference is a consequence of the **event being counted and its time boundary**, not a conflict between definitions.

**Source check:** [NIST Engineering Statistics Handbook, Exponential Reliability](https://www.itl.nist.gov/div898/handbook/apr/section1/apr161.htm) explicitly derives \(R(t)=e^{-\lambda t}\) and mean time to failure \(1/\lambda\) for a constant-hazard exponential life model. [SEBoK System Reliability, Availability and Maintainability](https://sebokwiki.org/wiki/System_Reliability%2C_Availability%2C_and_Maintainability) explicitly distinguishes survival, restoration, time-up/down distributions and availability categories.

**Countertests:** If uptime were deterministic at 90 hours (not exponential), the same mean would **not** give the same \(R(90)\). If repair were impossible, the long-run renewal availability expression would not describe a repeating up/down process. If the system is responsive but untrusted, an availability observation alone does not validate security.

**Administrative result:** The article now contains a direct conceptual bridge between the two original measures, complete units, source-linked equations and an explicit counterexample to inferring failure-free survival from an availability percentage. Prior Wave B review remains historical; this new example received its own **scoped model/source check**, not independent human acceptance.

## 3. Revision B | Why queue waiting grows near capacity

**Article:** [Queueing and Service-System Models](systems-engineering/queueing-and-service-system-models.md)  
**Observed depth gap:** The article distinguished **time in system** versus **time waiting**, and supplied \(W=1/(\mu-\lambda)\), but its worked M/M/1 case stopped at total time \(W\) and total occupancy \(L\). The reader had to infer how to obtain the missing queue-only quantities and why utilization approaching capacity disproportionately increases waiting.

**Change made:** Added a derivation from mean system time to mean queue waiting:

\[
W=W_q+\frac1\mu,\qquad
W_q=\frac1{\mu-\lambda}-\frac1\mu=\frac{\lambda}{\mu(\mu-\lambda)}.
\]

By Little's law applied **separately** to whole-system and waiting-queue boundaries:

\[
L=\lambda W,\qquad L_q=\lambda W_q,
\qquad L-L_q=\rho=\lambda/\mu.
\]

The difference \(L-L_q\) is **mean in-service occupancy**, not necessarily one even for a one-server model, because that server can be idle.

For \(\mu=6\) requests per second, compare two explicitly hypothetical, stable M/M/1 FCFS arrival rates:

| Quantity | \(\lambda=3\)/s | \(\lambda=5\)/s |
| --- | ---: | ---: |
| Utilization | 0.5000 | 0.8333 |
| Mean system time \(W\) | 0.3333 s | 1.0000 s |
| Mean waiting \(W_q\) | 0.1667 s | 0.8333 s |
| Whole-system mean occupancy \(L\) | 1.0000 | 5.0000 |
| Queue-only mean occupancy \(L_q\) | 0.5000 | 4.1667 |
| Mean in service \(L-L_q\) | 0.5000 | 0.8333 |

**Independent arithmetic:** At \(\lambda=5\), \(L=5(1)=5\), \(L_q=5(5/6)=25/6\), so mean in service is \(5-25/6=5/6=\rho\). At \(\lambda=3\), \(L=3(1/3)=1\) and \(L_q=3(1/6)=1/2\). All are derived from the same stated M/M/1 assumptions.

**Source check:** [MIT OpenCourseWare 2.854/2.853, M/M/1 Queue (2016)](https://www.ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/927056a1af54772a587fd84ad4951e71_MIT2_854F16_Mm1Queue.pdf), **PDF pages 0–1 (printed pp. 1–2)**, were visually inspected. They distinguish full-system and queue-only measures and derive \(W_q\), \(L_q\) and utilization contributions.

**Countertests:** If the queue has finite capacity, drops arrivals or admits them selectively, the offered rate and effective throughput differ. If service-time variability or arrival processes violate M/M/1, the *particular* waiting formula need not hold. Under suitable stable averaging, Little's law remains a more general flow relation. Thus the example must not be generalized to every real workload.

**Administrative result:** Added an inspectable chain from \(W\) to \(W_q\), \(L\) to \(L_q\), and utilization to mean occupancy, with a complete numerical comparison that makes the hidden inference understandable. Existing Wave H technical review remains valid historical evidence for earlier content; the **added** equations and cases received these new scoped checks.

## 4. Editorial and review-state safeguards

- Both target articles retain their existing **Reviewed (model-assisted)** development state. Their original Wave B/Wave H audits were **not** modified or retroactively expanded to claim they checked new content.
- The two additions are substantive explanatory depth, so **this pass separately recomputes the new mathematics and ties the central claims to primary sources**. This is bounded model-assisted validation, not a full source-to-passage audit or independent expert acceptance.
- The ten inspected files retain their established canonical owners. No new subject identifiers, reorganized folders, duplicate articles, quizzes or classroom assessments were created.
- All numeric values are **hypothetical**, with units and stochastic assumptions declared. No system reliability or queueing data were measured.
- No Security Foundations article was newly authored or substantively edited in this pass. Its user-directed drafting pause remains active after [Technical Review 11](../security-foundations/PILOT-TECHNICAL-REVIEW-11.md).

## 5. Remaining administrative opportunities

**Priority 1:** Continue deep-understanding passes across neighboring **Systems & Engineering** concepts, especially explaining where [Dependencies](systems-engineering/dependencies.md) transitions from graph structure to causal/failure assumptions, and where [Verification and Validation](systems-engineering/verification-and-validation.md) becomes evidence for actual required behavior. These are **candidate tasks**, not new approved subjects.

**Priority 2:** Inspect the **Models & Abstraction** pair [Abstraction](models-abstraction/abstraction.md) and [Conceptual and Formal Models](models-abstraction/conceptual-and-formal-models.md) for a carefully bounded example of property preservation across model-to-system abstraction, checking the direction of the implication.

**Priority 3:** Expand **Information & Data** understanding only where content needs a stronger mechanism-level bridge, for instance how query filtering, grouping, schema enforcement, physical index access and source provenance differ. Preserve [Databases and Queries](information-data/databases-and-queries.md) as the general owner and link specialized search/storage material without duplicating it.

Next batches should remain **variable in size and depth**. Apply A1 when the problem is editorial clarity, A2/A3 with fresh scoped source/model checks when explanation is materially expanded, and A4/A5 as the evidence demands. The aim is detailed comprehension rather than uniformly longer articles.

**Pass outcome:** **A0 sampled 10**, **A2/A3 materially improved 2**, **new mathematical checks recorded for both**, **all prior review/publication gates preserved**. Link and GitHub integrity validation are required for the commit carrying these changes.

[Fundamentals](README.md) · [Systems & Engineering](systems-engineering/README.md) · [Administrative Program](../../ADMINISTRATIVE-EDITORIAL-PASSES.md)
