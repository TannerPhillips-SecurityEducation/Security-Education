# Algorithm Design

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Algorithm design  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Batch 01 audit](../WAVE-D-TECHNICAL-REVIEW-01.md); independent human expert review pending

## Designing an algorithm means selecting and justifying a strategy

**Algorithm design** concerns constructing a computational procedure that meets a clearly stated problem specification, under relevant correctness, resource, and implementation constraints. It includes selecting representations, decomposing the problem, identifying invariants, developing a procedure, and evaluating evidence that the procedure meets its purpose.

An algorithm can be described precisely without saying how it was invented. Conversely, naming a design strategy such as “greedy” or “dynamic programming” does not prove that applying it to a particular problem is correct.

[Algorithms](algorithms.md) owns the general specification and execution concepts. This article owns **construction strategies, correctness arguments, competing designs, and their conditional suitability**.

The [MIT 6.046J Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/) course develops divide-and-conquer, greedy methods, dynamic programming, incremental improvements, and analysis of their assumptions.

## Problem definition precedes strategy

A candidate design begins with a problem statement: which inputs are admitted, what counts as a valid output, and which constraints apply? An optimization problem additionally specifies an objective and feasible alternatives.

For example, “choose coins to make an amount” is ambiguous until the allowed denominations, available quantities, objective, and representable amounts are known. Minimizing coin count differs from minimizing weight, transaction cost, or resource usage.

Some problems can be simplified by restricting the input domain; however, a solution correct under a restriction must not be advertised as correct for the unrestricted problem.

## Illustrative strategy families

| Strategy | Central construction idea | Typical proof question |
| --- | --- | --- |
| Exhaustive search | Examine admissible candidates systematically | Does the search cover all feasible candidates? |
| Divide and conquer | Split a problem into smaller subproblems and combine solutions | Do subproblem solutions combine into a valid whole? |
| Greedy choice | Select a locally preferred alternative at each stage | Does local choice preserve access to a global optimum? |
| Dynamic programming | Reuse solutions to overlapping subproblems | Is the recurrence valid and are base conditions correct? |
| Backtracking | Explore partial solutions and abandon infeasible branches | Can any pruned branch contain a valid solution? |

These are explanatory families, not new approved knowledge categories. Practical algorithms often combine approaches or employ specialized methods that do not fit neatly into one row.

## Worked example: when a greedy choice fails

Suppose unlimited coins with denominations `{1,3,4}` must sum to `6`, with the **objective of using as few coins as possible**.

A largest-denomination-first greedy procedure chooses `4`, then `1`, then `1`: a valid representation using **three coins**. Another feasible representation is `3+3=6`, using **two coins**. Since no allowed single coin has denomination 6, two coins are optimal.

```text
Greedy: 4 + 1 + 1 = 6  (3 coins)
Better: 3 + 3     = 6  (2 coins)
```

The counterexample proves that this greedy rule is **not universally optimal** for arbitrary coin systems. It does not prove that greedy algorithms always fail or that all coin systems require dynamic programming. A locally optimal choice needs a problem-specific argument.

## Constructing a recurrence

Define `M(a)` as the minimum number of coins needed to make nonnegative integer amount `a` under unlimited availability of the three denominations. A valid recurrence is:

```text
M(0) = 0
M(a) = 1 + min{M(a-c) : c in {1,3,4}, c <= a}
```

For positive integer amounts, the denomination 1 guarantees all subproblems in this toy problem are feasible. The recurrence relies on **optimal substructure**: an optimal solution's remaining coins after the first selection must solve the remaining amount optimally. Otherwise a better remainder would improve the whole solution.

Compute the values:

| Amount `a` | `M(a)` | One optimal representation |
| ---: | ---: | --- |
| 0 | 0 | No coins |
| 1 | 1 | 1 |
| 2 | 2 | 1+1 |
| 3 | 1 | 3 |
| 4 | 1 | 4 |
| 5 | 2 | 4+1 |
| 6 | 2 | 3+3 |

This table is derived from the specified recurrence, not a numerical experiment on a real payment system.

## Correctness and invariants

A **correctness argument** must match the algorithm's actual contract and use stated premises. For dynamic programming, proving the recurrence correct and establishing base cases are distinct from selecting an efficient evaluation order.

Induction can justify `M(a)` over increasing amounts because every recursive case refers to a strictly smaller nonnegative amount. An implementation may compute results bottom-up in a table or top-down with memoization. Both can implement the same mathematical recurrence under appropriate conditions.

[Deduction, Induction, and Abduction](../scientific-analytical-reasoning/deduction-induction-abduction.md) owns general inferential forms, and [Iteration and Recursion](README.md) owns the specialized computational mechanisms when authored.

## Choosing a design under constraints

Correctness is necessary, but designs also differ in time, space, latency, predictability, parallelizability, understandability and maintenance burden. One algorithm can be mathematically optimal for comparison count yet poor when memory accesses dominate runtime. Another can perform well on common workloads but have an unacceptable worst-case delay.

Design decisions therefore need a **cost model and intended environment**. [Complexity](complexity.md) owns asymptotic resource growth; [Computational Efficiency](README.md) owns practical resource tradeoffs; [Computational Data Structures](README.md) owns operation cost under a representation.

The existence of one successful example is not a correctness proof for an unbounded input domain. Counterexamples are powerful for rejecting a universal claim, while establishing a universal positive claim generally requires a more complete argument.

## Scope and references

This article does not prescribe a programming language, optimization library, contest methodology or a new universal algorithm-design taxonomy. It concerns general computing principles reusable across all seven specialized knowledge domains.

### Sources

- [MIT 6.046J: Design and Analysis of Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/).
- [MIT 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
- [MIT 6.046J: Lecture Videos](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/lecture-videos/).
- [MIT 6.046J: Syllabus and course outcomes](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/pages/syllabus/).

**Editorial status:** Reviewed (model-assisted) following the [Wave D Batch 01 24-family technical audit](../WAVE-D-TECHNICAL-REVIEW-01.md). Complete source verification, independent expert peer review and final publication approval remain separate outstanding gates.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
