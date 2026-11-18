# Wave D Technical Review: Batch 02

**Review date:** November 17, 2026  
**Scope:** Computational Data Structures; Iteration and Recursion; Concurrency and Parallelism; Synchronization; Computational Efficiency.  
**Method:** Reopened the five repository drafts; checked six material claim groups per article against MIT 6.006, MIT 6.005 and MIT 6.172 technical references; independently recomputed each worked example and checked its assumptions; checked canonical ownership; fetched every distinct article-local relative file destination in GitHub.  
**Disposition:** **30 material claim groups reviewed across five articles. All five pass scoped model-assisted technical review** after the recorded efficiency clarification. This is not exhaustive source certification, independent expert human review, actual performance benchmarking, formal model checking, or final publication acceptance.

## Claim-to-source ledger

### Computational Data Structures

[Reviewed article](computation-algorithms/computational-data-structures.md)

| ID | Material claim group | Evidence and disposition |
| --- | --- | --- |
| DS-01 | Abstract data type, concrete representation and data format are distinct | [MIT 6.005 Software Construction](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/syllabus/); the general information-format subject retains its own ownership |
| DS-02 | Arrays, lists, stacks, queues, hashing, trees and heaps differ in supported operations | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/); table explicitly illustrative, not a universal structure hierarchy |
| DS-03 | Representation invariants are correctness obligations, not storage-format guarantees | [MIT 6.005 readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/); binary min-heap parent/child rule is correctly conditional |
| DS-04 | Toy dynamic-array capacity doubles only when a write exceeds existing capacity | Recomputed eight appends with capacities 1,2,4,4,8,8,8,8 and resize-copy counts 0,1,2,0,4,0,0,0 |
| DS-05 | Aggregate copies lead to amortized constant item-copy/write cost under doubling | Seven resize copies plus eight appended writes = 15; doubling gives total fewer than 2n resize copies for n≥1, under the article's cost model; [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) |
| DS-06 | Hash lookup guarantees depend on hashing, collision resolution, load and input assumptions | MIT 6.006; cache locality and hardware effects not inferred from asymptotic class alone |

### Iteration and Recursion

[Reviewed article](computation-algorithms/iteration-and-recursion.md)

| ID | Material claim group | Evidence and disposition |
| --- | --- | --- |
| IR-01 | Iteration and recursion express repeated computation with different operational representations | [MIT 6.005 Readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/); not defined merely as syntax |
| IR-02 | Termination needs a well-founded progress argument rather than an arbitrary decrement | MIT 6.005 Recursion; decreasing nonnegative integer is one appropriate example |
| IR-03 | Recursive factorial base case and recurrence are correct on nonnegative integers | `FACT(0)=1`, `FACT(5)=5×4×3×2×1=120` verified |
| IR-04 | Iterative factorial gives same mathematical result with loop invariant | Before iteration k, `result=(k−1)!`; executing k multiplies to k!, and zero iterations return 1 |
| IR-05 | Call-stack and scalar-state claims require a chosen arithmetic/execution model | Conventional recursive call stack O(n), iterative scalar variables O(1) **in a unit-cost abstraction**; bit lengths grow, so not claimed true under arbitrary bit-space cost |
| IR-06 | Cyclic graph recursion can require visited-state tracking to terminate | [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/); a finite graph alone does not prevent naive repeated traversal around a cycle |

### Concurrency and Parallelism

[Reviewed article](computation-algorithms/concurrency-and-parallelism.md)

| ID | Material claim group | Evidence and disposition |
| --- | --- | --- |
| CP-01 | Logical concurrency can occur without simultaneous parallel execution | [MIT 6.005 Concurrency Reading](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/19-concurrency/); distinctions retain scheduling and physical-core conditions |
| CP-02 | Process, thread, task and actor refer to model-dependent execution/communication abstractions | MIT 6.005; OS-specific processes/threads retain approved operating-system ownership |
| CP-03 | Uncoordinated shared-state updates permit a lost-update interleaving | Stipulated reads of 0 by A and B followed by two writes of 1 yield final counter 1 |
| CP-04 | Race condition is broader than a language-specific data race | [MIT 6.005 Thread Safety](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/20-thread-safety/); exact data-race rules depend on the memory model |
| CP-05 | Shared-memory/message-passing designs require different correctness contracts | [MIT 6.005 Readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/); message passing not treated as automatically correct or reliable |
| CP-06 | Amdahl's idealized fixed-workload speedup is bounded by serial fraction and overhead | [MIT 6.172 Performance Engineering](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/pages/syllabus/); `1/(0.20+0.80/4)=2.5` under declared ideal assumptions |

### Synchronization

[Reviewed article](computation-algorithms/synchronization.md)

| ID | Material claim group | Evidence and disposition |
| --- | --- | --- |
| SY-01 | Synchronization includes mutual exclusion, order and visibility constraints | [MIT 6.005 Locks and Synchronization](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/23-locks/); distinct from merely having concurrent execution |
| SY-02 | A protected critical section must preserve a specific shared invariant | MIT 6.005 Thread Safety/Locks; one mutex does not prove all program correctness or progress |
| SY-03 | Atomicity and memory visibility/ordering depend on language and hardware contracts | MIT 6.005 Locks; no universal assertion that adjacent source operations are one atomic transaction |
| SY-04 | Two completed linearizable atomic increments produce a final counter of 2 | Starting at 0, with no overflow/failure and each operation applied exactly once, 0→1→2 regardless of which operation linearizes first |
| SY-05 | Opposite lock acquisition order can deadlock; ordered acquisition addresses that case | A acquires L1/waits L2, B acquires L2/waits L1, neither releases; common L1-before-L2 ordering prevents the **specific** inversion if followed |
| SY-06 | Deadlock freedom, starvation freedom and safe data access are different properties | [MIT 6.005 Locks and Synchronization](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/23-locks/); finite thread tests do not prove absence of every adverse schedule |

### Computational Efficiency

[Reviewed article](computation-algorithms/computational-efficiency.md)

| ID | Material claim group | Evidence and disposition |
| --- | --- | --- |
| CE-01 | Efficiency is relative to equivalent work and declared resource objective | [MIT 6.172 Performance Engineering](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/pages/syllabus/); changing correctness conditions is not a valid speedup |
| CE-02 | Latency, throughput, memory, communication and energy answer different questions | MIT 6.172; scope, workload, measurement methodology and resource boundaries remain explicit |
| CE-03 | Crossover example at n=100 | `n²=10,000`, `50n log₂n≈33,219.28`; A is lower under stipulated formulas |
| CE-04 | Crossover example at n=1000 | `n²=1,000,000`, `50n log₂n≈498,289.21`; B is lower under stipulated formulas |
| CE-05 | Asymptotic eventual superiority differs from measured implementation performance | **Clarified:** `50nlog₂n=o(n²)` so B is mathematically lower for sufficiently large n in this model; no real system speed guarantee follows |
| CE-06 | Fixed-workload bottleneck/parallelism example | `1/(0.20+0.80/4)=2.5`, not 4, given no overhead; profiling results are evidence for a workload, not an end-to-end speedup proof |

## Corrections and qualifications

1. **Computational Efficiency:** Corrected the distinction between an analytically certain *eventual* crossover for the stipulated functions and the absent evidence for any real application's performance. Under these formulas, B eventually beats A for all sufficiently large positive integer input sizes.
2. **No other numerical correction** was necessary. Source descriptions and model boundaries were checked at the material claim-group level.
3. The five articles' original dynamic-array, factorial, concurrent-update, lock-order and crossover examples are **invented pedagogical models**, not MIT empirical case studies or recorded benchmarking results.

## Executed numerical checks

| Example | Checked result |
| --- | --- |
| Dynamic array, eight appends, initial capacity one and doubling | Resize-copy counts 0,1,2,0,4,0,0,0; total 7 |
| Dynamic array, item writes plus copies | 8+7=15 modeled operations |
| Factorial 5, recursive and iterative exact arithmetic | 120 for each |
| Two unsynchronized increments both read initial 0 | Possible final counter 1 |
| Two completed linearizable atomic increments | Final counter 2 |
| Amdahl 20% serial, 80% parallel, four processors | 2.5× ideal fixed-workload speedup |
| Cost A(100) and B(100) | 10,000 and ≈33,219.28 |
| Cost A(1000) and B(1000) | 1,000,000 and ≈498,289.21 |

## Internal links and source limits

The five articles reference **55 local relative Markdown link occurrences**, mapping to **28 distinct file destinations**, all **28 of which were successfully reopened through GitHub**. This confirms file targets, not URL-fragment validity, external-link availability or corpus-wide relationship correctness.

Primary technical grounding includes MIT OpenCourseWare 6.005's software construction and synchronization material, 6.006's algorithms/data structures curriculum, and 6.172's performance-engineering course. The audit is a bounded **model-assisted claim-family review**, not exhaustive source inspection, source-level `Verified`, human peer review or final publication approval.

## Architecture and disposition

- **Computation & Algorithms** now has **nine of nine approved subjects authored and internally Reviewed** after this Batch 02 audit.
- The distinction between computational data structures, mathematical complexity, practical efficiency, repeated computation, concurrency and synchronization is preserved. General information formats and OS-specific mechanisms retain separate ownership.
- No change to **12 approved knowledge areas**, **109 approved subject headings**, unresolved G-01 mathematical breadth, G-04 general temporality or G-06 AI/ML decisions.
- No Knowledge Checks, Practical Assessments, new formal ontology predicates or mandatory programming environments have been introduced.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
