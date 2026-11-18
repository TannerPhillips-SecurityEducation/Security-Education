# Iteration and Recursion

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Iteration and recursion  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Batch 02 technical audit](../WAVE-D-TECHNICAL-REVIEW-02.md); independent human peer review pending

## Repeated computation can be expressed in different forms

**Iteration** performs a step or sequence of steps repeatedly according to a loop condition or other progression rule. **Recursion** defines a computation in terms of one or more applications of a related computation, usually on smaller or simpler subproblems.

Iteration and recursion can often express the same mathematical function, but their cost and operational behavior depend on the execution model. A recursive mathematical definition is not automatically a stack-using procedure, and iterative code is not automatically memory-efficient or correct.

[Algorithms](algorithms.md) owns general input-output contracts. This article owns **repeated execution, base conditions, progress, termination and recursive/iterative equivalence**. [Programming Languages](../software-programming/README.md) owns language-specific loops and calls.

The [MIT 6.005 Software Construction readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/) explicitly cover recursion, recursive data types and representation invariants.

## Iteration: state, condition and invariant

A loop can be described using an initial state, a guard or continuation condition, a body that transforms state, and an eventual exit or ongoing behavior. A **loop invariant** is a property intended to hold before and after every iteration for all reachable states.

A loop that stops when a counter reaches a bound must also ensure the counter makes appropriate progress. Merely containing an exit condition does not prove that the condition will ever become true.

For continuous systems, an algorithm may be intentionally ongoing. Then the relevant obligation might be liveness, responsiveness, bounded resource use or graceful termination on a stop signal rather than eventual completion of every possible execution.

## Recursion: base cases and decreasing measures

A recursive definition or function uses a **base case** for simple inputs and one or more **recursive cases** for reducing the problem. A termination argument typically identifies a **well-founded measure**, such as a nonnegative integer that strictly decreases on every recursive path until a base case is reached.

A recursive call that reduces one argument while increasing another may still terminate if an appropriate well-founded measure decreases. It is therefore overly restrictive to require “the numerical input always decreases” for every recursive algorithm.

Some recursive definitions describe infinite or lazy structures without immediate termination. A proof obligation must match the defined behavior.

## Worked example: factorial by iteration and recursion

For nonnegative integers, define factorial by `0!=1` and `n!=n×(n−1)!` for positive `n`.

A recursive procedure is:

```text
FACT(n):
    require n is a nonnegative integer
    if n == 0:
        return 1
    return n * FACT(n-1)
```

An iterative alternative is:

```text
FACT_ITER(n):
    require n is a nonnegative integer
    result = 1
    for k from 1 through n:
        result = result * k
    return result
```

For `n=5`, both produce `5×4×3×2×1 = 120`, under exact integer arithmetic. For `n=0`, the loop has no iterations and returns one.

The recursive version terminates because the positive argument decreases by one until it reaches zero; the iterative version terminates because its bounded counter reaches the end. An implementation with fixed-width arithmetic may overflow even if the mathematical procedure is correct.

## Invariants and induction

For the iterative version, a useful invariant before iteration `k` is that `result=(k−1)!`. Initially at `k=1`, `result=1=0!`; multiplying by `k` produces `k!`, establishing the invariant for the next iteration. On completion, the result is `n!`.

For the recursive version, mathematical induction can establish that `FACT(n)` returns `n!` when exact multiplication and the stated precondition apply. The proof's base case is zero, and the inductive step depends on correctness at `n−1`.

These proofs concern defined procedures and mathematical models. They do not establish that a particular compiler, processor or machine has unbounded integer precision.

[Deduction, Induction, and Abduction](../scientific-analytical-reasoning/deduction-induction-abduction.md) owns general logical inference, and [Algorithm Design](algorithm-design.md) owns how to construct proof strategies for procedures.

## Operational differences: stack and tail calls

Ordinary recursive implementations may retain stack frames for outstanding calls, with stack depth proportional to recursion depth. A naive recursive factorial may use **O(n)** call-stack space under a conventional call-stack model, while the iterative example can use **O(1)** additional scalar state under an idealized exact-arithmetic cost model.

However, exact integer values grow in bit length, so full bit-space complexity cannot automatically be treated as constant. Some language implementations optimize certain tail calls, but **tail-call optimization is not universally guaranteed**.

An iterative implementation may simulate recursion with an explicit stack; thus replacing recursion by iteration does not automatically remove memory cost when the problem's structure still requires suspended state.

## Trees, graphs and cycles

Recursive procedures naturally express traversal of recursive structures such as trees. Graph traversal over cyclic data, however, requires attention to repeated visits; blindly recursing along every edge may never terminate.

A visited set or carefully designed traversal policy can preserve termination on finite graphs. A tree-shaped mathematical description does not itself guarantee the real data contains no cycles.

[Graph Theory](../mathematics-logic/graph-theory.md) owns formal trees and graphs; [Computational Data Structures](computational-data-structures.md) owns their computational representations.

## Canonical boundaries

Iteration and recursion are mechanisms of repeated computation, not separate human learning strategies, mathematical proof systems or programming paradigms. Their specific syntax varies across programming languages.

This article introduces no required programming language, algorithm-assessment exercise, or extension to the 109 approved headings.

### Sources

- [MIT 6.005 Software Construction: Recursion and Recursive Data Types](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).
- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
- [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/).

**Editorial status:** Reviewed (model-assisted) following the [Wave D Batch 02 scoped 30-family technical audit](../WAVE-D-TECHNICAL-REVIEW-02.md). Exhaustive source verification, independent human expert review and final publication acceptance remain open.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
