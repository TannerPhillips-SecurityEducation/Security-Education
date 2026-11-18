# Wave D Technical Review: Batch 01

**Review date:** November 17, 2026  
**Scope:** Computability; Algorithms; Algorithm Design; Complexity.  
**Method:** Reopened the four committed canonical drafts, examined six material claim groups per article using MIT OpenCourseWare 6.045J, 6.006 and 6.046J and the general Turing-machine reference, examined published MIT lecture materials for halting and algorithm-design theory, recomputed the worked examples, checked conceptual ownership, and fetched all distinct article-local relative Markdown destinations from GitHub.  
**Disposition:** **24 material claim families reviewed; four articles pass scoped model-assisted technical review** after corrections. This is not independent human peer review, a formal machine-checked proof of every statement, exhaustive source-level verification, or final publication acceptance.

## Claim-to-source ledger

### Computability
[Reviewed article](computation-algorithms/computability.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| CO-01 | Computability is relative to defined inputs, output relationships and a computational model | [MIT 6.045J syllabus](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/syllabus/); problem specification is required |
| CO-02 | Turing computation and Church–Turing thesis are not physical hardware specifications | [MIT 6.045J Lecture 6](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/d6c18e634cdf3363ecac909bd2958b8b_MIT6_045JS11_lec06.pdf); appropriately described as thesis rather than an experimentally proven universal law |
| CO-03 | Recognizer differs from a decider | **Correction committed:** recognizer must halt and accept every member; on nonmembers it can reject or diverge. Decider must halt and give the correct yes/no answer for every admitted input |
| CO-04 | Reachability over a finite explicitly represented directed graph is decidable | Original graph A→B→C, D→A traversed from A; visited A, B, C, so C reachable; visited set bounds traversal |
| CO-05 | General halting problem undecidable by a total decider under the standard model | [MIT 6.045J Lecture 6](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/d6c18e634cdf3363ecac909bd2958b8b_MIT6_045JS11_lec06.pdf); diagonal contradiction for hypothetical H and self-applied D is sound given effective encoding |
| CO-06 | Decidability, reductions, running time and physical feasibility differ | [MIT 6.045J lecture notes index](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/lecture-notes/); resource limitation is not identical to undecidability |

### Algorithms
[Reviewed article](computation-algorithms/algorithms.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| AL-01 | Abstract algorithm, implementation and problem contract are distinct | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/); input/operation/output conditions explicit |
| AL-02 | Deterministic, randomized and theoretical nondeterministic models differ | MIT 6.006 and [MIT 6.045J](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/); nondeterminism not equated with sampling randomness |
| AL-03 | FIRST_MATCH example returns smallest matching index | Recomputed `FIRST_MATCH([4,9,4],4)=0`, not 2 |
| AL-04 | Loop invariant establishes minimality at the first successful return | No previous index `j<i` matches before inspection of i; invariant maintained by checking a nonmatch |
| AL-05 | Termination and comparison count depend on finite input and constant-cost primitives | At most n comparisons; zero when `n=0`; no extrapolation to real CPU wall-time |
| AL-06 | Partial correctness, total correctness and testing have distinct meanings | MIT 6.006/6.046J; finite tests not equated with universal proof of unbounded behavior |

### Algorithm Design
[Reviewed article](computation-algorithms/algorithm-design.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| AD-01 | Design strategies require a specified optimization or output objective | [MIT 6.046J syllabus](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/syllabus/); goal constraints and proof obligation explicit |
| AD-02 | Divide-and-conquer, greedy, dynamic programming and backtracking are illustrative strategies | [MIT 6.046J course overview](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/); not ratified as a new knowledge-area taxonomy |
| AD-03 | Largest-coin greedy algorithm is not optimal for every denomination set | With unlimited `{1,3,4}`, greedy `4+1+1` uses 3 coins for 6; `3+3` uses 2 |
| AD-04 | Minimum-coin recurrence with an available unit coin is valid | `M(0)=0`; `M(a)=1+min_{c∈{1,3,4},c≤a}M(a−c)` for positive integer `a`; computed M(0..6) = [0,1,2,1,1,2,2] |
| AD-05 | Optimal-substructure recurrence plus induction can justify the result | Every term involves a smaller nonnegative amount; no unsupported extrapolation to all greedy coin systems |
| AD-06 | Correctness, asymptotic cost and implementation fit are separate criteria | [MIT 6.046J syllabus](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/syllabus/); no empirical performance claim |

### Complexity
[Reviewed article](computation-algorithms/complexity.md)

| ID | Material claim | Evidence and finding |
| --- | --- | --- |
| CX-01 | Complexity bounds require an input-size metric and cost model | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/); bit-cost and unit-cost assumptions identified |
| CX-02 | Big-O, Ω, Θ express upper, lower and tight eventual growth bounds | Definitions in article use positive constants, eventual nonnegativity, and appropriate eventual inequalities |
| CX-03 | Worst-case, average-case and amortized costs are not interchangeable | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/); amortized is not automatically input-distribution average |
| CX-04 | `T(1)=1`, `T(n)=2T(n/2)+n` for powers of two | Recomputed T(2)=4, T(4)=12, T(8)=32, T(16)=80; closed form `n log₂ n+n` gives these values |
| CX-05 | P, NP and polynomial-time certificates refer to formal complexity classes | [MIT 6.045J syllabus](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/pages/syllabus/); NP not misdefined as “not polynomial”; P versus NP remains open |
| CX-06 | Asymptotic time and actual hardware performance are different claims | MIT 6.006; constant factors, memory hierarchy and input representation can affect practice |

## Corrections made before acceptance

1. **Computability:** Replaced ambiguous recognizer wording with its defining guarantee: every language member must be accepted after finite steps, while nonmembers may cause rejection or nontermination. This makes the distinction from a decider precise.
2. **Computability:** Added a direct [MIT 6.045J Turing Machines / Halting Problem lecture](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/d6c18e634cdf3363ecac909bd2958b8b_MIT6_045JS11_lec06.pdf) source.
3. **Algorithm Design:** Added MIT's course outcomes as direct grounding for dynamic programming, greedy methods and invariants; corrected an inline-code formatting defect in the coin-change example before the review.
4. **No numerical correction:** The other worked results passed recomputation.

## Computed verification

| Example | Checked result |
| --- | --- |
| Explicit directed graph reachability A→B→C | C is reachable from A |
| FIRST_MATCH for `[4,9,4]`, target 4 | index 0 |
| Greedy choice for 6 with coins {1,3,4} | 4+1+1, three coins |
| Optimal choice for same target | 3+3, two coins |
| Dynamic recurrence M(0..6) | 0, 1, 2, 1, 1, 2, 2 |
| Recurrence T(1), T(2), T(4), T(8), T(16) | 1, 4, 12, 32, 80 |
| Closed form T(8)=8log₂8+8 | 32 |

The halting argument is a standard mathematical proof sketch, not a software test of an actual universal decider. Counterexamples and toy recurrences are original pedagogical constructions, not copied MIT case studies.

## Internal links and review limits

All **43 relative Markdown link occurrences** across the four articles resolve to **17 distinct local file destinations**, and **all 17 destinations were reopened successfully in GitHub**. File existence is the scope of this check: URL fragments, external link availability, entire repository graph and complete relationship semantics were not exhaustively verified.

The audit reviews material claim families using publicly accessible source descriptions and selected lecture material; it does **not** establish a source citation for every sentence, a formal machine-checked proof, or independent human expert review. Articles are eligible for **Reviewed (model-assisted)** with **Core claims checked**, not the stronger `Verified` source state or final `Published` status.

The 12 approved knowledge areas and 109 subject headings remain unchanged. No Knowledge Checks, Practical Assessments, new subject categories, or programming-environment mandates were introduced. G-01 mathematical breadth, G-04 general temporality and G-06 AI/ML remain unresolved.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
