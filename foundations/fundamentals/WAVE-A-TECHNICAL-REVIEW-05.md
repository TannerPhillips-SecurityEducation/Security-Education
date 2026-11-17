# Wave A Technical Review: Batch 05

**Review date:** November 17, 2026  
**Scope:** Graph Theory, Causality and Correlation, Abstraction.  
**Method:** Reopened the three GitHub article drafts, inspected MIT/SEP/NASA source pages, checked mathematical and conditional-probability examples independently, and corrected identified technical issues.  
**Outcome:** **24 material claim families reviewed, 3 articles pass scoped model-assisted review.** Independent human expert sign-off and final publication acceptance are not asserted.

## Source grounding and limitations

This review uses [MIT Mathematics for Computer Science readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/), [Stanford Encyclopedia: Causal Models](https://plato.stanford.edu/entries/causal-models/), [Stanford Encyclopedia: Models in Science](https://plato.stanford.edu/entries/models-science/), and [NASA Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/). Model claims and worked examples are classified separately from source-defined mathematical theorems. The review checks **material claim families** rather than asserting every incidental statement has received independent human peer review.

## Claim-to-source review ledger

### Graph Theory

[Reviewed reference](mathematics-logic/graph-theory.md)

| Claim ID | Material claim | Evidence | Review finding |
| --- | --- | --- | --- |
| GT-01 | Simple undirected graph defined by vertices and unordered edges | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | The four-vertex, four-edge example is not a complete graph; corrected K₄ to six edges. |
| GT-02 | Directed vs undirected edge semantics | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | Directed ordered pairs do not imply reverse reachability; graph structure does not assert real-world meaning. |
| GT-03 | Degree and handshake lemma, with loop qualification | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/) | Degree vector [2,2,3,1], sum 8=2×4 independently calculated. |
| GT-04 | Paths, cycles and connected components | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | A–B–C–A is a cycle and A–C–D has two edges; formal convention stated. |
| GT-05 | Tree criterion: connected, acyclic, n−1 edges for nonempty finite tree | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | Removing A–B leaves connected acyclic graph with four vertices, three edges; n−1 alone insufficient. |
| GT-06 | DAG admits topological ordering, potentially nonunique | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) | A,C/B,C and C,D admit A,B,C,D or B,A,C,D. |
| GT-07 | Fewest hops distinct from minimum weighted path cost | [Source](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) | A→C direct 5 vs A→B→C cost 1+1=2; checked. |
| GT-08 | Graph relationships are selected representations, not observations of truth | [Source](https://plato.stanford.edu/entries/models-science/) | General model/target distinction; this is interpretive guidance, not a graph theorem. |

### Causality and Correlation

[Reviewed reference](scientific-analytical-reasoning/causality-and-correlation.md)

| Claim ID | Material claim | Evidence | Review finding |
| --- | --- | --- | --- |
| CC-01 | Correlation describes statistical association, not sufficient evidence of causation | [Source](https://plato.stanford.edu/entries/causal-models/) | Claim is appropriately limited to model interpretations. |
| CC-02 | Pearson coefficient measures linear association with finite nonzero variance | [Source](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm) | Definitions qualified for sample r and population rho; numerator/denominator context explicit. |
| CC-03 | Zero Pearson correlation need not imply independence | [Source](https://plato.stanford.edu/entries/causal-models/) | X in {-2,-1,1,2}, Y=X² gives covariance 0 yet deterministic dependence. |
| CC-04 | Common cause can produce association without direct causal edge | [Source](https://plato.stanford.edu/entries/causal-models/) | Rain/umbrella/wet example states conditional independence assumption. |
| CC-05 | Weather example conditional probabilities under model assumptions | [Source](https://plato.stanford.edu/entries/causal-models/) | Recomputed P(U,W)=0.37, P(W|U)=0.74, P(W|not U)=0.26. |
| CC-06 | Observational conditioning distinct from an intervention distribution | [Source](https://plato.stanford.edu/entries/causal-models/) | P(Y|X=x) versus P(Y|do(X=x)) are not interchangeable without model assumptions. |
| CC-07 | Confounder, mediator and collider are different causal patterns | [Source](https://plato.stanford.edu/entries/causal-models/) | Causal DAG semantics explained without promising conditioning is always harmless. |
| CC-08 | Counterfactual claims require assumptions beyond an observed event record | [Source](https://plato.stanford.edu/entries/causal-models/) | Individual counterfactual distinct from observed association; temporal scope G-04 remains open. |

### Abstraction

[Reviewed reference](models-abstraction/abstraction.md)

| Claim ID | Material claim | Evidence | Review finding |
| --- | --- | --- | --- |
| AB-01 | Abstraction selects relevant aspects of a target while omitting others | [Source](https://plato.stanford.edu/entries/models-science/) | SEP emphasizes model/target representation and purpose. |
| AB-02 | Target, selection, representation, interpretation are editorial facets | [Source](https://plato.stanford.edu/entries/models-science/) | Declared original decomposition, not standard metadata schema. |
| AB-03 | Multiple functional/physical/state models may represent one system | [Source](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | NASA system-engineering views support multiple levels; illustrative sequence not literal pipeline. |
| AB-04 | Abstraction versus idealization distinction is useful but contested | [Source](https://plato.stanford.edu/entries/models-science/) | Omission distinguished from false/simplifying assumption with caveat. |
| AB-05 | Classification, generalization and encapsulation are distinct mechanisms | [Source](https://plato.stanford.edu/entries/models-science/) | Editorial distinctions reasonable; specialized mechanisms remain in their canonical areas. |
| AB-06 | Concrete-to-abstract many-to-one map loses recoverable detail | [Source](https://plato.stanford.edu/entries/models-science/) | Threshold mapping t=17.9 LOW, 18 NORMAL, 28.9 NORMAL, 30 HIGH evaluated. |
| AB-07 | Many-to-one state mapping alone does not guarantee sound transition abstraction | [Source](https://plato.stanford.edu/entries/models-science/) | Corrected claim: sound over-approximation depends on appropriately defined transition semantics. |
| AB-08 | Telemetry summarization loses time/calibration/uncertainty context | [Source](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | Original worked example; suppression of attributes makes certain inferences unsupported. |

## Corrections made before acceptance

1. **Graph Theory:** The example with four vertices and four edges was incorrectly labeled complete. A complete simple four-vertex graph has six edges. Corrected the label and clarified that `n−1` edges alone do not make a graph a tree.
2. **Causality and Correlation:** Explicitly distinguished sample `r` from population `ρ`, qualified the zero-correlation counterexample with finite moments and nondegeneracy, and made the common-cause assumptions clear.
3. **Abstraction:** Clarified that an arbitrary many-to-one state mapping does **not** automatically establish a sound over-approximation of transition behavior. Context and validation remain required.

## Independently computed example results

| Example | Calculated value |
| --- | --- |
| Example graph `V={A,B,C,D}` with four undirected edges | Degrees A=2, B=2, C=3, D=1, total 8 = twice four edges |
| Complete simple undirected graph on four vertices, `K₄` | `4×3/2 = 6` edges |
| Delete A-B from original graph | Connected, acyclic graph with four vertices and three edges |
| Weighted path A→C versus A→B→C | Costs 5 and 2, respectively |
| `P(Umbrella, Wet)` under stated toy weather model | `0.37` |
| `P(Wet \| Umbrella)` | `0.74` |
| `P(Wet \| No umbrella)` | `0.26` |
| Example symmetric `X={-2,-1,1,2}` and `Y=X²` | Zero covariance despite deterministic dependence |
| Abstract class `α(17.9), α(18), α(28.9), α(30)` | LOW, NORMAL, NORMAL, HIGH |

These computations verify **the illustrative numbers**, not causal identification for actual weather data or any particular security or industrial system.

## Architectural and publication boundaries

- **Graph Theory** owns graph structures; causal DAG arrows describe assumed causes, not generic mathematical edges.
- **Causality and Correlation** owns the interpretation of association, intervention, counterfactuals and confounding; it does not redefine probability mathematics.
- **Abstraction** owns selective modeling and interpretation; a simplified record does not preserve evidence or semantics by default.
- G-01 mathematical breadth and topology, G-04 general temporality, and G-06 AI/ML remain explicit unresolved placement/scope questions.
- No additional knowledge area, graph predicate schema, classroom assessment or mandatory reading sequence is created.

## Acceptance disposition

All three are **Reviewed (model-assisted)** and **Core claims checked**, with evidence linked above and specific corrections committed to their respective articles. This does **not** constitute independent human expert verification or final publication approval. Those review states remain separate in the [Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md).

[Fundamentals Index](README.md) · [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
