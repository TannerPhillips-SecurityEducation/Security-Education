# Wave H | Four Foundational Knowledge Gaps: Scoped Technical Review 01

**Review date:** November 18, 2026  
**Articles:** F-01-12/13, F-05-10, F-11-12, four newly authored references in Mathematics & Logic, Information & Data and Systems & Engineering.  
**Review scope:** **24 material claim groups**, six per article, covering canonical ownership, definitions, mathematical examples, model assumptions and core source references.  
**Disposition:** All four articles pass this bounded **model-assisted technical/editorial review** and may be promoted from Draft/References listed to **Reviewed (model-assisted) / Core claims checked**. This is **not** complete source-passage verification, qualified independent human peer review, or final Published acceptance.

## Source and claim-group ledger

### F-01-12: Calculus and Differential Equations

**Canonical article:** [mathematics-logic/calculus-and-differential-equations.md](mathematics-logic/calculus-and-differential-equations.md)  
**Knowledge area:** Mathematics & Logic  
**Sources checked for scope:** [MIT 18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/); [MIT 18.03SC Syllabus](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/)

| Claim group | Finding and limitation |
| --- | --- |
| Limits, derivatives and units | Difference-quotient derivative under a real-function limit, differentiability assumptions, and units of rate are stated. A derivative is not automatically an average or an empirical observation. |
| Integral and accumulation | Integral of r(t)=t on [0,2] is 2 under standard real Riemann integration; dimensions depend on model units. |
| ODE and initial-value model | dx/dt=−kx, x(0)=x₀ has solution x₀e^(−kt), for constant k and the declared domain; no blanket existence/uniqueness claim for all ODEs. |
| Numerical Euler step | For x₀=10, k=.2/s, h=1s, Euler yields 8 versus analytic 10e^(−.2)≈8.18730753; error correctly identified as approximation. |
| Five-second decay calculation | x(5)=10e^(−1)≈3.67879441, under the invented constant-rate model; no measured behavior asserted. |
| Canonical ownership | Mathematical calculus/differential equation theory distinguished from algebra, time representations, control mechanism and measured physical dynamics. |

### F-01-13: Stochastic Processes and Markov Models

**Canonical article:** [mathematics-logic/stochastic-processes-and-markov-models.md](mathematics-logic/stochastic-processes-and-markov-models.md)  
**Knowledge area:** Mathematics & Logic  
**Sources checked for scope:** [MIT 6.041SC syllabus and resource index](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/pages/resource-index/); [MIT lecture 17 Markov chains](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/0c7babf5725ef87aa95cf623253a68e4_MIT6_041SCF13_lec17_300k.pdf)

| Claim group | Finding and limitation |
| --- | --- |
| Indexed random variables and sample paths | Stochastic process, marginal distribution, joint dependence, sample path and index/state-space distinction are differentiated. |
| Markov condition | The conditional-state property is distinguished from time homogeneity and from any claim that a physical system lacks historical dependence. |
| Transition-matrix validity | P=[[.8,.2],[.4,.6]] nonnegative row-stochastic; p₁=(.8,.2); p₂=(.72,.28) recomputed. |
| Stationary distribution | π=(2/3,1/3) satisfies πP=π under exact rational arithmetic; article does not infer empirical convergence from stationary algebra alone. |
| Poisson counting model | Homogeneous Poisson process assumptions stated; for λ=2/min, P(N(1 min)=0)=e^(-2)≈.135335, not evidence all observed arrivals are Poisson. |
| Cross-subject boundary | Probability theory, stochastic processes, queue service disciplines and AI Markov decision processes have distinct canonical explanations. |

### F-05-10: Search and Information Retrieval

**Canonical article:** [information-data/search-and-information-retrieval.md](information-data/search-and-information-retrieval.md)  
**Knowledge area:** Information & Data  
**Sources checked for scope:** [Stanford Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/); [Stanford Boolean retrieval online chapter](https://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html); [Stanford IR evaluation chapter](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html)

| Claim group | Finding and limitation |
| --- | --- |
| Semantic distinctions | Information need, query syntax/semantics, matching, indexing, result, ranking and relevance are distinct units of description. |
| Search-family types | Exact field, full text, Boolean, regex, fuzzy, proximity, ranking and semantic matching are nonexclusive families, with implementation caveats. |
| Inverted and positional indexes | Postings lists return terms to documents; positional indexes enable ordered phrase/proximity constraints with stated tokenizer and normalization rules. |
| Toy corpus exact matching | D1 'red fox near hill', D2 'red hills contain foxes', D3 'fox red near river'; exact fox postings D1/D3, red postings D1/D2/D3; Boolean AND D1/D3; ordered phrase 'red fox' D1 only. |
| Precision and recall calculations | Three relevant among four retrieved gives precision 3/4=.75; three retrieved relevant among six relevant in scope gives recall 3/6=.5; relevance truth not conflated. |
| Ownership and evidence | Retrieval is distinct from relational queries, graph queries, source truth and application-specific search syntax; no assumption that any named search implementation is adopted. |

### F-11-12: Queueing and Service-System Models

**Canonical article:** [systems-engineering/queueing-and-service-system-models.md](systems-engineering/queueing-and-service-system-models.md)  
**Knowledge area:** Systems & Engineering  
**Sources checked for scope:** [MIT Queues Theory and Applications](https://ocw.mit.edu/courses/15-072j-queues-theory-and-applications-spring-2006/pages/readings/); [MIT M/M/1 model note](https://live.ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/927056a1af54772a587fd84ad4951e71_MIT2_854F16_Mm1Queue.pdf)

| Claim group | Finding and limitation |
| --- | --- |
| Boundary and accounting | Arrival, departure, occupancy, waiting-only time and total time in system separated, with service discipline, admission and loss conditions explicit. |
| Utilization and capacity | ρ=λ/μ is conditional on simple server model; λ close to μ can increase delay under many stochastic models, not an automatic universal waiting prediction. |
| Little's law | For stable matching boundaries, L=λW; λ=5 requests/s and W=.4s gives L=2 items average, not exactly 2 at every instant. |
| M/M/1 formula and conditions | Poisson arrivals/exponential services/one server with λ<μ; MIT note gives Wsystem=1/(μ−λ) and Lsystem=λ/(μ−λ); system values not confused with queue-only values. |
| M/M/1 worked numbers | At λ=5/s and μ=6/s, nominal ρ=5/6≈.8333, Wsystem=1s, Lsystem=5; a different model from the preceding .4s illustration. |
| Noninterchangeable disciplines | Queueing generality maintained across networking, endpoint execution, databases, manufacturing and service desks; no network vendor or workflow chosen. |

## Independent example recomputation

| Example | Recomputed result | Qualification |
| --- | --- | --- |
| Derivative of f(t)=t² | f'(t)=2t; at t=3 derivative=6 | Exact real-variable model, not observed system |
| Integral of t over 0…2 | 2 | Standard integral under given limits |
| Exponential decay x(0)=10, k=.2/s | x(1)=10e^(−.2)≈8.18730753; x(5)=10e^(−1)≈3.67879441 | Constant k and exact ideal ODE |
| Euler h=1s on x'=−.2x | First step x₁=8 | Different from exact x(1) due to discretization |
| Two-state Markov chain after one and two steps | p₁=(.8,.2), p₂=(.72,.28) | Chosen row-stochastic P, initial state A |
| Two-state stationary distribution | π=(2/3,1/3) | Algebraic stationarity only, not a finite empirical convergence test |
| Poisson rate 2/min, zero events in 1 minute | e^(−2)≈.1353353 | Homogeneous Poisson model assumed, not diagnosed from observations |
| Inverted-index toy corpus | Exact 'red' AND 'fox' yields D1/D3; phrase 'red fox' yields D1 | Lowercase whitespace tokenization, no stemming or fuzzy matching |
| Precision/recall toy evaluation | Precision 3/4=.75; recall 3/6=.5 | Relevance judgments and collection defined by stipulation |
| Little's law | λ=5/s, W=.4s ⇒ L=2 | Stable, consistently bounded system, long-run average |
| M/M/1 model | λ=5/s, μ=6/s ⇒ ρ=5/6, Wsystem=1s, Lsystem=5 | Steady-state M/M/1 assumptions; not same service model as prior illustration |

## Source confidence and limitations

1. **Differential equations:** MIT 18.03SC distinguishes introductory calculus prerequisites, ordinary differential equations, exact and numerical solution approaches and physical modeling. This establishes topical grounding and supports the worked idealized examples; it is not evidence that an arbitrary measured system follows a particular ODE.
2. **Stochastic processes:** The MIT 6.041SC resource index identifies Poisson processes and Markov-chain units. The Markov transition example was checked by direct calculation. One lecture document is a teaching reference, not an assertion that every real transition is Markovian.
3. **Information retrieval:** The Stanford textbook and its HTML directory provide source-backed chapters covering Boolean retrieval, postings, proximity, ranked retrieval and relevance evaluation. Some individual Stanford page fetches timed out through the web reader, although the HTML directory lists the section files; full external URL reachability and paragraph-level citation review remain open.
4. **Queueing:** The MIT OCW M/M/1 note was inspected visually on its first page as well as through parsed content. It explicitly distinguishes queue-only from system-wide waiting/occupancy and gives Wsystem=1/(μ−λ) and Lsystem=λ/(μ−λ). The model assumptions must not be transferred to arbitrary nonstationary, lossy or multi-server systems.
5. **Cross-domain navigation:** No arbitrary quota for links to specialized domains is adopted. Cross-links remain incremental as related technical descriptions and applications develop.
6. **Remaining knowledge gaps:** The separate [Coverage & Source Triage 02](COVERAGE-AND-SOURCE-TRIAGE-02.md) retains numerical methods/optimization and source/depth checks as open candidates. Neither is declared resolved merely by these four articles.

## Repository review state

The current subject count is **120** within twelve existing knowledge areas: the original **116 Reviewed (model-assisted)** under Waves A–G plus **four additional Reviewed** under this Wave H audit. **Core claims checked** does not equal complete material claim-to-passage verification; **Published** and independent qualified human acceptance remain unachieved.

The subject count is a versioned snapshot rather than a cap or target. No Knowledge Checks, Practical Assessments, mandatory vendor tools, new knowledge-area taxonomy, or graph engine were introduced.

[Fundamentals index](README.md) · [Development register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Coverage triage](COVERAGE-AND-SOURCE-TRIAGE-02.md)
