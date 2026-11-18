# Complexity

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Complexity  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source review pending

## Complexity describes resource growth under a computational model

**Computational complexity** studies the resources required by algorithms or problems as a function of input size under a stated computational and cost model. Common resources include **time**, **space**, number of comparisons, communication steps and other explicit measures.

An expression such as `O(n²)` is meaningful only with context: which resource is counted, how `n` measures input size, what operations cost, and whether the bound concerns worst-case, average-case, best-case or amortized behavior.

This article owns **asymptotic analysis and resource-growth classifications**. It is distinct from system-wide [Emergence and Complexity](../systems-engineering/emergence-and-complexity.md), which concerns interacting elements, nonlinear dynamics and whole-system behavior.

The [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) course develops computational models, asymptotic analysis and resource tradeoffs. [MIT 6.045J](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/) also develops complexity classes and problem reductions.

## Input size and cost models

Input size may be measured by sequence length, number of vertices plus edges, bit length of an integer, dimensions of a matrix, or another defined measure. These are not interchangeable. An algorithm that performs `n` arithmetic operations may not run in time proportional to `n` if the operands grow in bit length and arithmetic operations are not constant-cost.

A **unit-cost model** can simplify selected operations to constant cost, while a bit-complexity model counts operations on bits or more realistic primitive units. An analysis should declare its model rather than silently applying one to every input representation.

Implementation language, hardware, caches, I/O and allocation can affect actual execution time without invalidating an asymptotic claim under its mathematical model.

## Upper, lower, and tight asymptotic bounds

For functions that are eventually nonnegative, common notation includes:

- **Big O:** `f(n)=O(g(n))` when there are constants `c>0` and `n₀` with `f(n)≤cg(n)` for all `n≥n₀`.
- **Big Omega:** `f(n)=Ω(g(n))` when there are constants `c>0` and `n₀` with `f(n)≥cg(n)` for all sufficiently large `n`.
- **Big Theta:** `f(n)=Θ(g(n))` when both applicable O and Ω bounds hold, giving a tight asymptotic bound up to positive constant factors.

An upper bound does not automatically state a matching lower bound. For example, `3n+2` is `O(n²)`, but `Θ(n)` is a more precise growth characterization for `n≥1`.

Constants, cache behavior and small inputs may matter greatly in practice even when they do not affect a stated large-`n` asymptotic class.

## Worst case, average case, and amortization

**Worst-case** analysis bounds cost over all admissible inputs of the chosen size. **Average-case** analysis requires a probability distribution over inputs or execution conditions. **Amortized** analysis distributes total cost across a sequence of operations under assumptions about the allowed sequence; it is **not** automatically an average over random inputs.

A data structure can sometimes make an individual operation expensive while bounding the total cost of many operations. A convincing amortized argument uses an accounting, aggregate, or potential method rather than an unsupported claim about what happens “on average.”

[Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns probabilistic mathematics; [Computational Data Structures](README.md) owns how implementation structures influence operation costs.

## Worked example: a divide-and-conquer recurrence

Consider a hypothetical algorithm whose exact input sizes are powers of two, with cost recurrence:

```text
T(1) = 1
T(n) = 2 T(n/2) + n   for n = 2,4,8,...
```

The two subproblems each have size `n/2`, and additional work at a level costs `n`. Expand the recurrence for `n=8`:

```text
T(2) = 2(1)+2 = 4
T(4) = 2(4)+4 = 12
T(8) = 2(12)+8 = 32
```

For powers of two, the closed form is `T(n)=n log₂(n)+n`. This follows by induction: it holds at `n=1`; substituting the form for `T(n/2)` gives `2[(n/2)log₂(n/2)+n/2]+n=nlog₂n+n`.

The asymptotic complexity under this recurrence is therefore **Θ(n log n)** for the stated domain. The recurrence does not by itself prove that any particular merge-sort implementation has those exact costs on physical hardware.

## Complexity classes and computability limits

**Decidability** concerns whether a decision problem has an algorithm that always terminates with the correct result. **Complexity classes**, such as P and NP, concern resource-bounded classes of problems under formal computational models.

P comprises decision problems decidable by a deterministic Turing machine in polynomial time. NP includes decision problems whose yes-instances have certificates verifiable in polynomial time under standard definitions, equivalently decidable by nondeterministic polynomial-time machines. **NP does not mean “not polynomial.”**

Whether P equals NP remains unresolved in the standard theory. This article neither claims a proof nor implies that a hard practical problem is NP-complete without a formal reduction and membership argument.

[Computability](computability.md) owns the theoretical existence of effective procedures; [Algorithm Design](algorithm-design.md) owns strategy construction; this article owns resource growth and class distinctions.

## Complexity versus engineering efficiency

Two procedures with the same `Θ(n log n)` growth can have different constant factors, memory locality, power demand or parallel overhead. A procedure with a worse asymptotic bound can be faster over a practical range of input sizes.

[Computational Efficiency](README.md) retains the separate approved heading for applying resource tradeoffs in actual computational systems. [Memory and Storage](../digital-systems-hardware/memory-and-storage.md) owns the physical memory hierarchy; it does not redefine mathematical asymptotic notation.

## Canonical scope

No programming language, benchmark, performance claim about a real processor, new taxonomy or assessment is introduced. Input representation and model assumptions remain explicit rather than silently equating algorithmic asymptotics with wall-clock measurements.

### Sources

- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
- [MIT 6.045J Automata, Computability and Complexity](https://ocw.mit.edu/courses/6-045j-automata-computability-and-complexity-spring-2011/).
- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/).

**Editorial status:** Substantive Draft. The recurrence, asymptotic claims and class definitions require a separate scoped source/technical audit before promotion. No Knowledge Checks or Practical Assessments are included.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
