# Fundamentals | Coverage & Source Triage 02

**Review date:** November 18, 2026  
**Scope:** 116 canonical Fundamentals articles in the twelve existing knowledge areas, with source/coverage diagnostics and targeted direct article reading.  
**Purpose:** Decide whether remaining knowledge gaps require **new canonical subjects**, more depth in existing subjects, source-passage checking, or only future cross-links.  
**Status:** Adopted as a **working architecture disposition**. All article-writing and technical-review outcomes remain separate. The subject count is **not fixed**.

## 1. Evidence and diagnostic limits

[Corpus-wide diagnostic](tools/audit_coverage_and_sources.py) inspected 116 articles from the [Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md). The [successful GitHub Actions run](https://github.com/TannerPhillips-SecurityEducation/Security-Education/actions/runs/44289211075) reported:

| Diagnostic | Observation | Correct interpretation |
| --- | ---: | --- |
| Canonical subject articles scanned | 116 | Current inventory snapshot, not immutable denominator |
| Articles with zero external source URLs | 0 | Every article has at least one reference URL, not that sources support every claim |
| Articles with zero detected inline source links | 20 | Candidate claim-to-source traceability weakness; some citations may be embedded in bibliographies or missed by parser |
| Total external link occurrences in subject articles | 666 | Citation and navigation links mixed; not 666 independently verified sources |
| Unique external hostnames | 44 | Diversity of domains, not independent corroboration |
| Articles directly linking to specialized-domain paths | 2 | Low explicit inter-domain navigation **at this snapshot**, not evidence of conceptual absence |

**Linking policy:** Specialized-domain cross-links will be added **as the relevant domain knowledge is developed**. Do not elevate present link counts into a content-completion gate or force 116 articles to add decorative domain links. Canonical terms and meaning take precedence; link correctness and discoverability are maintenance responsibilities.

**Lexical diagnostic:** The scan looked for 22 concept families in non-bibliographic, non-code prose. It found **no exact candidate phrase matches** for: differential/dynamical systems, queueing theory, stochastic processes, and search/information retrieval. This is a *screening signal only*. The scanner strips inline code spans and links and has incomplete synonyms; direct article inspection is required before adjudicating a knowledge gap.

## 2. Source-grounded adjudication

| Case | Candidate knowledge | Current evidence and boundary | Disposition |
| --- | --- | --- | --- |
| CG-11 | **Calculus and Differential Equations** | [Algebra and Functions](mathematics-logic/algebra-and-functions.md) explains functions and transformations, while [Feedback and Control](systems-engineering/feedback-and-control.md) uses time-response concepts. No standalone canonical account of limits, derivatives, integrals, differential equations, initial conditions, and dynamic solutions is established. [MIT 18.03](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) treats these as substantial mathematical prerequisites to physical and engineering models. | **Add Mathematics & Logic subject**, separate from elementary algebra and physical controllers |
| CG-12 | **Stochastic Processes and Markov Models** | [Probability and Statistics](mathematics-logic/probability-and-statistics.md) treats random variables and distributions but not an explicit canonical account of indexed random variables, trajectories, transitions, Markov assumptions and Poisson arrival processes. [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/pages/resource-index/) distinguishes Poisson processes and Markov chains. | **Add Mathematics & Logic subject**, preserving Probability and Statistics as prerequisite owner |
| CG-13 | **Queueing and Service-System Models** | [Latency and Throughput](communication-distributed-systems/latency-and-throughput.md) defines communication delay/rate, while [Computational Efficiency](computation-algorithms/computational-efficiency.md) covers resource costs. A general model of arrivals, service, utilization, waiting, stability and Little's law has no adequate canonical treatment. [MIT Queues: Theory and Applications](https://ocw.mit.edu/courses/15-072j-queues-theory-and-applications-spring-2006/pages/readings/) covers queueing networks across many contexts. | **Add Systems & Engineering subject**, not a network-only topic |
| CG-14 | **Search and Information Retrieval** | [Databases and Queries](information-data/databases-and-queries.md) explains structured selection, joins and aggregation. It does not develop full-text retrieval, inverted indexes, lexical matching, regex, tolerant/fuzzy and positional search, ranking, relevance and evaluation. [Stanford Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/) treats these as a coherent and substantial field. | **Add Information & Data subject**, with clear boundaries around structured database queries and search engine implementations |
| CG-15 | **Numerical Methods and Optimization** | Prior G-02: [Algorithm Design](computation-algorithms/algorithm-design.md), [Algebra and Functions](mathematics-logic/algebra-and-functions.md) and [Computational Efficiency](computation-algorithms/computational-efficiency.md) provide plausible existing ownership, but conditioning, convergence, error analysis and numerical approximation may need more depth. | **Defer additional heading**, perform direct depth/source checks first; broad mention does not prove coverage |
| CG-16 | **Scientific model validation, data quality and reliability** | Prior G-07/G-09 and existing measurement, evidence, data provenance, verification/validation and reliability articles have established conceptual owners. | **Deepen existing articles** based on claim-level findings, do not create redundant subjects |
| CG-17 | **Cross-domain links for all seven specialized domains** | Two currently detected direct links reflect current repository documentation maturity and editorial priorities. | **Incremental links only** as substantive specialist articles appear; do not call a low link count a knowledge deficit |

## 3. Current inventory change: four distinctly owned subjects

The four **new** names receive provisional administrative IDs under existing areas, in a documented versioned inventory change. Their eventual content is **not** Reviewed merely because 116 earlier articles passed model-assisted review.

| Tracking ID | Subject | Distinctive responsibility | Not owned here |
| --- | --- | --- | --- |
| F-01-12 | Calculus and Differential Equations | Limits, rates/accumulation, ODEs, initial conditions, dynamic solution models | Algebraic function notation, physical plant implementation or controller tuning |
| F-01-13 | Stochastic Processes and Markov Models | Time/space-indexed random variables, conditional transitions, trajectories, Markov and Poisson models | General probability axioms, security-specific risk scenarios or specific stochastic services |
| F-05-10 | Search and Information Retrieval | Search matching, indexing, lexical/positional retrieval, ranking and relevance evaluation | Relational schema, general query algebra, specific SIEM products or vendor search syntax |
| F-11-12 | Queueing and Service-System Models | Arrivals, departures, occupancy, utilization, waiting, service discipline and stability | Particular router queues, OS schedulers or cloud managed queues |

**Current working inventory after adoption:** **120 subjects across the same twelve knowledge areas**: 116 existing scoped Reviewed (model-assisted) and four newly Inventoried with articles not yet written. There is no guarantee this count will remain 120.

## 4. Conceptual placement and dependencies

- **Calculus** supplies mathematics for models of continuous change; **Temporal Concepts and Models** describes time representations, while **Feedback and Control** applies dynamical ideas to systems. Neither timekeeping nor a controller law is a generic definition of a derivative.
- **Stochastic Processes** extends random-variable theory with dependence over an index (often time); **Markov assumptions** concern the modeled conditional dependence structure, not a claim that all future events forget their history.
- **Queueing systems** apply mathematical stochastic/deterministic arrival and service models to a general system boundary, and make occupancy, utilization and delay explicit. A queueing model can apply to servers, ports, manufacturing lines, people or computational tasks.
- **Information retrieval** supplies a distinct search/query lens over collections; structured relational queries and document retrieval can be combined but should retain separately owned general definitions.

## 5. Editorial and publication controls

1. Create one substantive canonical article for each new subject only after checking source definitions and the scope above.
2. Add new subject headings to the four area indexes, ownership register and development tracker. Never fabricate an article path while it does not yet exist.
3. Source verification is **claim-relative**, not determined by whether a URL appears inline or in a bibliography. For each consequential technical claim, identify a precise reference section and its applicability.
4. Preserve the earlier 116/116 Reviewed state as a **historical denominator**. Newly Inventoried content must progress through Draft and scoped Reviewed with separate evidence. No transfer of review status by association.
5. Maintain cross-domain references **incrementally as the specific application content develops**, as directed for this repository. No compulsory quota for outbound domain links.
6. Do not introduce Knowledge Checks, Practical Assessments or a forced graph schema.

## 6. Sources

- [MIT OpenCourseWare 18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/).
- [MIT OpenCourseWare 6.041SC Probabilistic Systems and Applied Probability](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/pages/resource-index/).
- [MIT Queues: Theory and Applications](https://ocw.mit.edu/courses/15-072j-queues-theory-and-applications-spring-2006/pages/readings/).
- [Stanford Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/).

These are established reference sources for curricular and conceptual scope, not blanket passage-level verification of all future articles.

[Fundamentals index](README.md) · [Gaps and decisions](COVERAGE-GAP-DECISIONS.md) · [Development register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Governing architecture](ARCHITECTURE.md)
