# Wave D Software & Programming Technical Review: Batches 03–04

**Review date:** November 17, 2026  
**Scope:** Programming Languages; Syntax and Semantics; Programming Paradigms; Compilation and Interpretation; Runtime Environments; Modules and Dependencies; Software Interfaces; Error Handling; Testing and Software Lifecycle.  
**Method:** Reopened nine GitHub draft articles, checked six material claim groups per article against MIT 6.035 Computer Language Engineering, MIT 6.005 Software Construction, and appropriate systems-engineering sources; recomputed the invented examples; corrected version representation and integer-domain test coverage; and verified the internal Markdown file destinations linked by the nine articles.  
**Disposition:** **54 material claim groups reviewed across nine articles; all nine pass a scoped model-assisted technical review after the recorded corrections.** This does not establish exhaustive sentence-level source verification, implementation conformance, independently performed human expert peer review, certification, or final publication acceptance.

## Claim-to-source ledger

### Programming Languages

[Reviewed article](software-programming/programming-languages.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| PL-01 | A language has rules for expressing programs, distinct from a particular implementation | [MIT 6.035 Computer Language Engineering](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/); correct language/implementation distinction |
| PL-02 | Syntax, static semantics, dynamic semantics and execution environment answer different questions | [MIT 6.035 lecture notes](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/pages/lecture-notes/); the article does not impose one theory for all languages |
| PL-03 | Types, names, scope and object lifetime can differ | [MIT 6.005 Static Checking](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/01-static-checking/); no ungrounded universal memory model |
| PL-04 | Toy integer addition versus string concatenation illustrates language-dependent semantics | Numeric `1+2=3`; stipulated string concatenation `"1"+"2"="12"`; not a universal operator rule |
| PL-05 | Static or dynamic checks detect only violations within their chosen rules and scope | MIT 6.005; a syntactically valid program need not fulfill the user's intended goal |
| PL-06 | Language, compiler, runtime, and paradigm choices have separate roles | MIT 6.035; not a vendor or language endorsement |

### Syntax and Semantics

[Reviewed article](software-programming/syntax-and-semantics.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| SS-01 | Syntax constrains valid forms; semantics describes interpretation | [MIT 6.005 Regular Expressions and Grammars](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/17-regex-grammars/); accepted |
| SS-02 | Tokens, grammar productions, parse tree and abstract syntax tree differ | [MIT 6.035 lecture notes](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/pages/lecture-notes/); AST may omit source punctuation |
| SS-03 | Simplified expression grammar gives `*` tighter grouping than `+` | For `2+3*4`, grammar groups `2+(3*4)`; independently computed 14 |
| SS-04 | Parenthesized alternative `(2+3)*4` evaluates to 20 | Arithmetic checked; result depends on given interpretation |
| SS-05 | Static rules versus dynamic evaluation and operational/denotational approaches differ | MIT 6.035 semantic analysis/IR lectures; concept examples not a fixed semantic formalism |
| SS-06 | Language meaning differs from programmer intent or real-world correctness | [MIT 6.005 Specifications](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/06-specifications/); syntactic or semantic correctness alone is not product validation |

### Programming Paradigms

[Reviewed article](software-programming/programming-paradigms.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| PP-01 | Programming paradigms describe expression/organization styles, not mutually exclusive language classes | [MIT 6.005 Software Construction](https://ocw.mit.edu/ans7870/6/6.005/s16/); accepted |
| PP-02 | Imperative and declarative views can coexist in software | MIT 6.005; not a binary classification mandate |
| PP-03 | Functional expression and purity are conditional semantic notions | [MIT 6.005 Map/Filter/Reduce](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/25-map-filter-reduce/); I/O and mutable state may still occur in a functional program |
| PP-04 | Objects, constraints, and event-driven styles may coexist | MIT Software Construction; no claim that event handlers require distinct hardware threads |
| PP-05 | Even-square-sum example across imperative and functional pseudocode | Even inputs [2,4]; squares [4,16]; sum **20** both ways under exact integer arithmetic |
| PP-06 | Paradigm choice alone does not establish performance, safety or correctness | MIT 6.005; costs and coupling remain implementation-dependent |

### Compilation and Interpretation

[Reviewed article](software-programming/compilation-and-interpretation.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| CI-01 | Translation and interpretation can be combined | [MIT 6.035](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/); language not intrinsically “compiled-only” or “interpreted-only” |
| CI-02 | Parsing, static checks, IR, optimization, code generation and loading are distinct stages | [MIT 6.035 lecture notes](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/pages/lecture-notes/); pipeline clearly illustrative rather than universal |
| CI-03 | Observable semantics constrain legal optimizations | MIT 6.035 optimization lectures; side effects, rounding, overflow and ordering require attention |
| CI-04 | Toy constant folding under exact arithmetic and no effects | `3*4+2=14`; replacement by literal `14` is valid under stipulated semantics |
| CI-05 | AST interpretation, bytecode VMs and JIT compilation are nonexclusive mechanisms | MIT 6.035; runtime implementation choices not a language definition |
| CI-06 | Successful compilation does not prove complete semantic correctness, deployment compatibility or termination | [MIT 6.005 Specifications](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/06-specifications/); epistemic limit retained |

### Runtime Environments

[Reviewed article](software-programming/runtime-environments.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| RE-01 | Runtime environment comprises execution support and surrounding resources | [MIT 6.005 readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/); not a required stack |
| RE-02 | Language semantics and environmental availability are distinct | MIT 6.005 and [MIT 6.035](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/); resource and configuration conditions explicit |
| RE-03 | Call stack, heap and lifetime are commonly related but implementation-specific | MIT 6.035 code generation material; no universal heap/stack requirement |
| RE-04 | Toy configuration influences output under same computation | `BASE=10→12`, `BASE=20→22`; missing/invalid BASE has no defined result without an error contract |
| RE-05 | Static and dynamic linking do not determine presence/absence of all runtime dependencies | MIT 6.035; version string alone does not prove compatibility |
| RE-06 | Reproducibility claims require source, dependencies, input, environment and scope | MIT 6.005; container/VM use not equated with universal deterministic replay |

### Modules and Dependencies

[Reviewed article](software-programming/modules-and-dependencies.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| MD-01 | Module, import, package, build-time and run-time dependencies have different semantics | [MIT 6.005 Interfaces](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/14-interfaces/index.html); distinct organization/contract concepts |
| MD-02 | Public surface and internal representation are separate | MIT 6.005 Interfaces; matching names do not ensure semantic compatibility |
| MD-03 | A→B, A→C, B→C is a dependency graph, not automatically a run order | Graph notation explicitly interpreted; initialization semantics and dependency cycles remain conditional |
| MD-04 | Stipulated version constraints have an intersection | `[2.0,3.0) ∩ [2.5,4.0) = [2.5,3.0)` for lexicographically ordered (major,minor) tuples |
| MD-05 | Versions 2.7, 2.4 and 3.1 under the intersection | 2.7 permitted; 2.4 violates B; 3.1 violates A. **Correction:** version comparison is tuple-based rather than decimal fraction |
| MD-06 | Constraint satisfaction or a lockfile does not prove runtime/API compatibility or reproducible deployment | MIT 6.005 Interfaces; scope qualified correctly |

### Software Interfaces

[Reviewed article](software-programming/software-interfaces.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| SI-01 | Interface includes admissible inputs, guarantees, errors, effects and observables | [MIT 6.005 Specifications](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/06-specifications/); contracts not merely names and types |
| SI-02 | Preconditions, postconditions and side effects impose different obligations | MIT Specifications; specific source added to article |
| SI-03 | Fahrenheit-to-Celsius toy contract is unit-sensitive | `(68−32)×5/9=20` °C. Returning 68 violates stipulated postcondition; interpreting input as °C violates caller's input meaning |
| SI-04 | Interface equivalence can hold across different representations if observables align | [MIT 6.005 Interfaces](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/14-interfaces/index.html); representation independence conditional |
| SI-05 | Acknowledgment versus actual completion and idempotency are distinct | MIT Specifications; repeated requests not automatically safe |
| SI-06 | Interface version labels alone cannot establish backward compatibility | MIT 6.005; additions may break strict consumers |

### Error Handling

[Reviewed article](software-programming/error-handling.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| EH-01 | Defect, contract error condition, exception and system failure differ | [MIT 6.005 Specifications](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/06-specifications/); terminology scoped to conventions |
| EH-02 | Invalid input differs from unavailable dependency and code defect | MIT 6.005; distinctions conditional on the stated precondition |
| EH-03 | Return value, exception and structured result have different reporting contracts | MIT Specifications/Exceptions; null and zero can be legitimate success values |
| EH-04 | Toy integer parsing of `"23"` and `"three"` | Under defined decimal integer format, 23 succeeds; “three” fails. Error result must distinguish invalid input from numeric zero |
| EH-05 | Cleanup, rollback and external effects depend on transaction guarantees | MIT 6.005; rollback/compensation cannot be assumed to undo every external action |
| EH-06 | Timeout, retry and idempotency depend on the operation's effect | MIT Specifications; missing response does not establish no operation occurred |

### Testing and Software Lifecycle

[Reviewed article](software-programming/testing-and-software-lifecycle.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| TS-01 | Test cases need inputs, expected outcome and relevant conditions | [MIT 6.005 Testing](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/03-testing/); a program merely running is not proof of correctness |
| TS-02 | Unit, integration, end-to-end and regression tests have different scopes | MIT 6.005 Testing; test labels are not graded learner assessment categories |
| TS-03 | Score predicate integer domain and boundary tests | For integers −1,0,1,100,101 outcomes are F,T,T,T,F as stipulated |
| TS-04 | Noninteger type guard is separately necessary | **Added:** 0.5 and text `"50"` must return false under the integer-only contract; the examples were verified |
| TS-05 | Coverage, test doubles and version control do not guarantee full correctness | MIT 6.005 Testing/Version Control; independent environment or human acceptance not implied |
| TS-06 | Software lifecycle includes iterative revision, not mandatory waterfall | [NASA Product Realization](https://www.nasa.gov/reference/5-0-product-realization/) and MIT 6.005; no development methodology mandated |

## Corrections and improvements committed

1. **Modules and Dependencies:** Version ranges explicitly use lexicographically ordered `(major,minor)` integer tuples. This prevents mistaking version 2.10 for a decimal number less than 2.9; the toy convention is **not** a universal semantic-version compatibility guarantee.
2. **Testing and Software Lifecycle:** Added noninteger inputs 0.5 and text `"50"` to the illustrative valid-score boundary tests, making the integer-only contract check explicit.
3. **Software Interfaces:** Added direct MIT specifications and interfaces sources to strengthen precondition/postcondition and representation-independence grounding.
4. **No other material numerical correction was necessary.** Original examples remain invented and are not attributed as published empirical findings from MIT or NASA.

## Independent recomputation of example outputs

| Example | Verified result |
| --- | --- |
| Numeric addition versus concatenation under stipulated semantics | `1+2=3`; `"1"+"2"="12"` |
| Grammar grouping `2+3*4` versus `(2+3)*4` | 14 versus 20 |
| Sum of squared even values among [1,2,3,4] | 20 |
| Pure exact integer constant folding `3*4+2` | 14 |
| Runtime configuration BASE=10 / BASE=20 | 12 / 22 |
| Software dependency intersection | `[2.5,3.0)`; permits 2.7, excludes 2.4 and 3.1 |
| Fahrenheit-to-Celsius input 68 | 20 °C |
| Integer-only score range [0,100] | −1 F, 0 T, 1 T, 100 T, 101 F, 0.5 F, text "50" F |
| Integer parse `"23"` versus `"three"` | valid 23 versus invalid-format result |

These are checks of **stipulated language and data contracts**, not execution of nine production software implementations.

## Internal link verification

All **102 relative Markdown-link occurrences** from the nine source articles resolve to **37 distinct local file destinations**; all **37 were reopened successfully through GitHub**. Link checks concern file destinations, **not** individual fragment anchors, external website availability, complete repository-wide links or source relevance beyond this scoped audit.

## Scope and acceptance disposition

- All nine Software & Programming articles now qualify as **Reviewed (model-assisted)** with the source-review state **Core claims checked**.
- The original **12 approved knowledge areas** and **109 approved subject headings** remain unchanged.
- **Wave D is 18/18 authored and internally Reviewed**: nine Computation & Algorithms, nine Software & Programming.
- The post-audit corpus totals are **90 Reviewed, zero Draft, 19 Inventoried without articles**, pending Wave E authoring.
- G-01 mathematics breadth, G-04 general temporality and G-06 AI/ML remain open. No Knowledge Checks, Practical Assessments, new headings or required implementation tools introduced.
- **Complete source verification, independent human peer review and final publication acceptance remain outstanding.**

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
