# Wave A Technical Review: Batch 04

**Date:** November 17, 2026  
**Status:** Scoping and claim-to-source review, model-assisted, v0.1  
**Articles reviewed:** Discrete Mathematics; Deduction, Induction, and Abduction; Boundaries  
**Material claim groups checked:** 24  
**Acceptance:** **Reviewed (model-assisted)** for the three articles, not independent human peer-review or final publication acceptance

## Method and limits

The exact three GitHub drafts were reopened. Their material claims were compared with the public [MIT Mathematics for Computer Science course](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/), [SEP Abduction](https://plato.stanford.edu/entries/abduction/), [SEP Induction](https://plato.stanford.edu/entries/induction-problem/) and [SEBoK boundary/context references](https://sebokwiki.org/wiki/Engineered_System_Context). Concrete mathematical examples were recalculated, and conceptual labels were checked against governing Fundamentals scope.

The 24 rows group *material claims*, not every sentence; a **reviewed** claim family may contain author-created examples, which are marked editorial rather than misattributed to formal standards. Independently certified accuracy, human editorial approval and final publication have **not** occurred.

## Source and claim review register

### Discrete Mathematics

[Reviewed article](mathematics-logic/discrete-mathematics.md)

| ID | Material claim family | Relevant authority | Outcome and limits |
| --- | --- | --- | --- |
| DM-01 | Discrete mathematical structures are not synonymous with finite or binary sets | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) | Verified broad subject scope; the infinite integers furnish a counterexample |
| DM-02 | Set, sequence, and function differ in uniqueness/order/mapping semantics | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | Logical distinction and example checked |
| DM-03 | Counting product rule and inclusion–exclusion under stated assumptions | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | Four-position labels give 10^4=10,000; inclusion–exclusion correct |
| DM-04 | Permutations and combinations distinguish ordered from unordered selection | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/) | P(5,3)=60 and C(5,3)=10 recomputed |
| DM-05 | Generalized pigeonhole does not require every bin to be occupied | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) | Corrected premise; k positive bins with exactly one assignment per object, ceil(13/12)=2 |
| DM-06 | Mathematical induction is deductive proof with base and inductive step | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/) | Sum 1..n formula checked for examples and algebraically |
| DM-07 | Recurrence relation needs sufficient initial conditions; Fibonacci example | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | First ten terms independently computed |
| DM-08 | State invariants require preservation across all permitted transitions | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/) | Even-counter example consistent; unmodeled update exception explicit |

### Deduction, Induction, and Abduction

[Reviewed article](scientific-analytical-reasoning/deduction-induction-abduction.md)

| ID | Material claim family | Relevant authority | Outcome and limits |
| --- | --- | --- | --- |
| DI-01 | Deduction preserves truth conditional upon valid premises | [Source](https://plato.stanford.edu/entries/logical-consequence/) | No countermodel for all S-members P and a∈S entails P(a) |
| DI-02 | Validity of inference differs from factual truth of premises | [Source](https://plato.stanford.edu/entries/logic-classical/) | Conditional validity explicitly distinguished from sound argument |
| DI-03 | Empirical induction extrapolates from observed to unobserved and is not deductive | [Source](https://plato.stanford.edu/entries/induction-problem/) | Sampling and stability assumptions qualified |
| DI-04 | Abduction encompasses hypothesis generation and explanatory evaluation in differing uses | [Source](https://plato.stanford.edu/entries/abduction/) | Corrected to preserve historical and modern senses |
| DI-05 | Inference to best explanation is contested rather than a guaranteed truth method | [Source](https://plato.stanford.edu/entries/abduction/) | Defeasible explanatory preference qualified |
| DI-06 | Sensor reading may be compatible with multiple explanations | [Source](https://plato.stanford.edu/entries/abduction/) | Example editorial: correct inference limit, alternatives not treated as observed |
| DI-07 | Mathematical induction is a deductive proof principle, distinct from empirical induction | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/) | Proof structure and induction terminology distinguished |
| DI-08 | Affirming consequent is an invalid deduction even when abduction considers its hypothesis | [Source](https://plato.stanford.edu/entries/logical-consequence/) | Countermodel H=false,R=true satisfies conditional and R but not H |

### Boundaries

[Reviewed article](models-abstraction/boundaries.md)

| ID | Material claim family | Relevant authority | Outcome and limits |
| --- | --- | --- | --- |
| BO-01 | System boundary distinguishes observer-selected system from environment | [Source](https://sebokwiki.org/wiki/System_Boundary_%28glossary%29) | Direct definition confirmed in SEBoK |
| BO-02 | Separation and limitation are distinct editorial functions of delimitation | [Source](https://sebokwiki.org/wiki/Introduction_to_System_Fundamentals) | Governing architecture of this repository, not an external normative taxonomy |
| BO-03 | System boundary is not identical to an interface across it | [Source](https://sebokwiki.org/wiki/Engineered_System_Context) | System boundary/context relationships confirmed; interface distinction specified by article |
| BO-04 | Physical, logical, mathematical, organizational and temporal perspectives differ | [Source](https://sebokwiki.org/wiki/Introduction_to_System_Fundamentals) | Examples illustrative; no fixed seven-type ontology asserted |
| BO-05 | Sharp model membership, graded membership and uncertainty about a boundary differ | [Source](https://sebokwiki.org/wiki/Concepts_of_Systems_Thinking) | Corrected conceptual distinction; source describes modeling views, not a universal fuzzy taxonomy |
| BO-06 | Real-valued f(x)=1/x excludes x=0 in the selected domain | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) | Checked algebraically; domain constraint not confused with access control |
| BO-07 | Nested subsystem boundaries and overlapping functional scopes are compatible | [Source](https://sebokwiki.org/wiki/Engineered_System_Context) | Cross-cutting contexts supported, example fictional |
| BO-08 | Changing the system of interest changes what is internal or external to the model | [Source](https://sebokwiki.org/wiki/Engineered_System_Context) | SEBoK narrow/wider system of interest distinction directly supports the example |

## Corrections committed before review decision

1. **Pigeonhole principle:** Generalized formula now explicitly permits empty bins; it assumes `k≥1` categories and every object assigned to exactly one of them.
2. **Abductive interpretation:** The article now distinguishes hypothesis generation and inference to the best explanation as distinct established uses rather than identifying every explanatory conjecture with best-explanation inference.
3. **System boundary versus interface:** Boundary is scoped delimitation; the interface is a defined form of interaction, which might cross that boundary.
4. **Sharp versus graded versus uncertain:** Graded membership is a modeling choice; uncertainty about the location of a sharp boundary is an epistemic limitation, not necessarily a graded boundary.
5. **SEBoK source precision:** The boundary article now explicitly links the system boundary glossary and the introduction to systems-engineering fundamentals.

## Numerical and logical example checks

| Example | Recomputed result |
| --- | --- |
| Four independent digit positions with ten symbols | `10^4 = 10,000` possible strings |
| Five choose three | `C(5,3)=10` |
| Three-position ordered selection from five | `P(5,3)=60` |
| 13 labeled items in 12 categories | At least one category has 2 or more |
| Sum of first n positive integers | Formula `n(n+1)/2` confirmed for n=1..100, with valid symbolic inductive step in article |
| Fibonacci with seeds 0 and 1 | `0,1,1,2,3,5,8,13` |
| Counter adding two from zero | Always even under **only** the modeled transitions |
| Affirming consequent | `H=False,R=True` is a countermodel to `(H→R),R ⊢ H` |
| Function `1/x` | Undefined at zero in ordinary real-number arithmetic |

These examples are **mathematical verification**, not a claim about empirical causes, professional ontology governance or independent expert certification.

## Status and governance

| Topic | Development | Source review | Unresolved concern |
| --- | --- | --- | --- |
| Discrete Mathematics | **Reviewed (model-assisted)** | **Core claims checked** | Mathematical breadth G-01 remains open |
| Deduction, Induction, and Abduction | **Reviewed (model-assisted)** | **Core claims checked** | Exact norms for explanatory inference depend on chosen framework |
| Boundaries | **Reviewed (model-assisted)** | **Core claims checked** | Seven example perspectives are not approved graph predicate types; G-01 and G-04 open |

**No new categories, mandatory reading sequence, formal knowledge graph or assessments** have been introduced. The twelve-area and 109-subject baseline remains unchanged. The next three articles begin in **Draft / References listed** state.

[Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md) · [Fundamentals](README.md)
