# Algorithms

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Algorithms  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Batch 01 audit](../WAVE-D-TECHNICAL-REVIEW-01.md); independent human expert review pending

## An algorithm specifies a procedure, not its implementation language

An **algorithm** is a defined, effective procedure for transforming admissible inputs or states according to explicit operations and rules, with the aim of producing an output or satisfying a specified objective. Whether it must terminate depends on the class of algorithm and task under consideration; an algorithm for a **total function** must return correctly on every valid input, while an ongoing control or streaming algorithm may be defined to operate indefinitely.

An **implementation** expresses an algorithm in a programming language or machine representation. Multiple implementations can realize the same abstract algorithm, while the same program text can behave differently when language semantics, input interpretation or environment differ.

The [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) references treat algorithmic problem formulation, correctness, efficiency and data-structure selection. [Programming Languages](../software-programming/README.md) owns language-specific realization.

## Problem contracts, inputs and outputs

A meaningful algorithm specification should clarify:

- **Input domain:** valid inputs and any preconditions.
- **Output or effect:** what result or state change is required.
- **Correctness relation:** what makes a result acceptable for a given input.
- **Operational model:** permitted primitive operations and relevant representation assumptions.
- **Termination or liveness obligation:** when a result is expected or which continuous behavior must be maintained.

These are general explanatory concerns, not a mandatory schema. A sorting algorithm might return a permutation ordered according to a declared comparison relation. It is insufficient for the output merely to be ordered if original items can be silently lost or duplicated.

[Requirements](../systems-engineering/requirements.md) owns engineered-product requirement processes; this article owns abstract computational procedure contracts.

## Determinism, nondeterminism and randomness

A **deterministic** algorithm has a determined next action given the same relevant state and input under its execution model. A **randomized** algorithm uses random choices modeled by an explicit distribution; a repeated input can yield different execution paths or outputs, with stated success probabilities.

Nondeterministic computation is also a formal theoretical model and should not automatically be described as a real program “making random choices.” Nondeterminism and randomness have distinct semantics.

An algorithm can be **correct but slow**, **fast but incorrect**, or **correct on a limited domain**. Performance alone cannot establish correctness.

## Worked example: finding the first matching element

Let the input be an indexed finite sequence `A[0..n-1]` and a target value `t`. The required output is the **smallest index** `i` such that `A[i]=t`, or `NONE` if no match exists.

```text
FIRST_MATCH(A, t):
    for i from 0 to length(A)-1:
        if A[i] equals t:
            return i
    return NONE
```

With `A=[4,9,4]` and `t=4`, the algorithm returns `0`, not `2`. The first match fulfills the specified minimal-index requirement.

Before iteration `i`, the **loop invariant** is: no earlier position `j<i` contains a match. Initially, no positions have been inspected, so the claim holds. If a tested position does not match, it remains true for the next iteration. On the first matching position, the invariant guarantees no smaller index matches. If the loop ends, every position was checked and returning NONE is justified.

This is a correctness argument for the stated equality operation and finite sequence model, not proof that equality or data retrieval from a real system is reliable.

## Termination and resource cost

For an input of length `n≥0`, the example examines at most `n` elements and then stops, under the assumption that each indexed read and equality test terminates. It therefore terminates in the finite-array model.

If every comparison has constant cost, worst-case comparison count is `n`, with a successful match in the first position requiring one comparison for nonempty inputs. Exact wall time depends on data representation, memory access and implementation.

[Complexity](complexity.md) owns asymptotic growth analysis, while [Computational Efficiency](computational-efficiency.md) will own engineering efficiency and practical resource tradeoffs. A count of abstract comparisons is not a measured CPU duration.

## Correctness, proofs, and tests

**Partial correctness** says that if a procedure terminates, its result meets a specification. **Total correctness** adds termination for every admissible input under the model. A test suite can reveal defects but finite tests do not usually prove behavior across an unbounded input domain.

Correctness arguments may use induction, invariants, preconditions and postconditions. [Deduction, Induction and Abduction](../scientific-analytical-reasoning/deduction-induction-abduction.md) owns the general logical forms. [Algorithm Design](algorithm-design.md) owns the construction of algorithms and selection of proof strategies.

Different implementations of FIRST_MATCH can use sequential or vectorized operations. A change that returns *any matching index* rather than the *smallest matching index* would change the specification even if typical tests happen to pass.

## Boundaries and applications

An algorithm can manipulate abstract values, operate physical controllers, transform datasets or coordinate distributed agents. Its admissible inputs and semantics must be explicit. An algorithm that calculates from incorrect sensor data can produce an exactly correct result for its input while still supporting an erroneous conclusion about the world.

[Data Types](../information-data/data-types.md) owns value interpretation; [State and Behavior](../systems-engineering/state-and-behavior.md) owns general system evolution; [Computability](computability.md) owns theoretical solvability.

No programming language, code runner, vendor environment, grading or learner assessment is required by this article.

### Sources

- [MIT OCW 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
- [MIT OCW 6.006: Lecture 1, Introduction](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-videos/lecture-1-introduction/).
- [MIT OCW 6.046J: Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/).

**Editorial status:** Reviewed (model-assisted) following the [Wave D Batch 01 24-family technical audit](../WAVE-D-TECHNICAL-REVIEW-01.md). Complete source verification, independent expert peer review and final publication approval remain separate outstanding gates.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
