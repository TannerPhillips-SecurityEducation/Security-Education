# Discrete Mathematics

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Discrete mathematics  
**Development status:** Reviewed (model-assisted; independent human review and final release pending)  
**Source review:** Core claims checked in [Wave A Batch 04 review](../WAVE-A-TECHNICAL-REVIEW-04.md); complete independent expert verification not claimed

## Distinct structures and countable possibilities

**Discrete mathematics** studies mathematical structures and methods built around distinguishable elements, steps, configurations, or values. Its central objects may include integers, finite sets, sequences, logical expressions, combinations, graphs, and relations. Its usefulness is not restricted to electronic computers; those are one type of system to which its general methods apply.

A **discrete model** represents a system using individually distinguishable states or elements. It may abstract a continuous phenomenon into categories or steps, but the existence of discrete states in the *model* does not prove the underlying phenomenon is intrinsically discontinuous.

For example, a room's temperature can vary continuously, while a controller may represent its condition as one of the categories `LOW`, `NORMAL`, or `HIGH`. The categories are a modeling decision. The physical conditions, sampling method, and boundary thresholds require their own explanations in [Measurement](../scientific-analytical-reasoning/measurement.md) and [Models & Abstraction](../models-abstraction/README.md).

The [MIT Mathematics for Computer Science course](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) covers proof techniques, counting, recurrence relations, graphs, states and invariants, and discrete probability. The material demonstrates how such mathematical principles support many different technical disciplines.

## Sets, sequences, and functions

A **set** represents distinct members without an intrinsic sequence order. A **sequence** assigns positions to elements, so order and repeated values can matter. A **function** associates each allowed input with one output.

Consider these representations:

```text
Set:       {a, b, c}
Sequence:  (a, b, a, c)
Function:  f(n) = 2n + 1, for n in the integers
```

The sequence has four positions and repeats `a`; the set has three members. The function specifies a mathematical mapping for all allowed integer inputs. These are different structures with different operations and constraints.

Canonical definitions of membership and relations belong in [Sets and Relations](sets-and-relations.md), while function composition belongs in [Algebra and Functions](algebra-and-functions.md). This article instead develops shared **discrete reasoning mechanisms** that operate on these structures.

## Counting and the product rule

Counting methods establish the number of possible configurations without necessarily enumerating them.

The **product rule** applies when a choice consists of a sequence of stages, with a known number of possibilities available at each stage. If there are `m` possibilities for the first stage and `n` for the second, and every first-stage choice permits exactly `n` second-stage choices, the total is `m × n`.

Suppose a system uses a four-position label, each position independently selected from ten symbols `0` through `9`. There are

```text
10 × 10 × 10 × 10 = 10,000
```

different length-four strings under those assumptions. This counts strings with leading zeros and repeated symbols. If repetitions were prohibited, the count would differ. Counting answers depend on the model's constraints, not merely on the number of available symbols.

The **addition rule** counts disjoint alternatives. If two classes of outcomes overlap, simply adding their sizes double-counts the intersection; the general two-set rule is

```text
|A ∪ B| = |A| + |B| − |A ∩ B|
```

These methods relate to the set operations defined in [Sets and Relations](sets-and-relations.md).

## Permutations, combinations, and ordering

A **permutation** selects and arranges items with ordering taken into account. A **combination** selects items without regarding their ordering as different choices.

For `n` distinct items and `k` selected positions without replacement, the number of ordered selections is

```text
P(n,k) = n! / (n−k)!
```

The number of unordered selections is

```text
C(n,k) = n! / (k! (n−k)!)
```

For example, choosing three items from five distinct candidates yields `C(5,3)=10` combinations. Arranging three distinct items chosen from the same five gives `P(5,3)=60` possible ordered sequences.

The expressions assume `0 ≤ k ≤ n` for nonnegative integers and no replacement. Repeated items, replacement, or additional constraints require different counting models.

The [MIT course readings on counting](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) treat these distinctions and their proofs as general mathematical tools.

## The pigeonhole principle

The **pigeonhole principle** states that placing more than `n` objects into `n` categories requires at least one category to contain more than one object. More generally, assigning `N` objects to `k ≥ 1` categories means that at least one category contains at least `⌈N/k⌉` objects, assuming each object is assigned to exactly one category. Individual categories **may be empty**; the conclusion does not require every category to contain an object.

If 13 labeled events must each be classified into one of 12 months, at least one month category must contain at least two events. This conclusion follows from counting, not from observations of which month received them.

The principle is powerful because it proves an **existence claim** without identifying a particular category. It therefore does not tell us which month had at least two events.

## Mathematical induction and invariants

**Mathematical induction** is a deductive proof technique, not the same as empirical inductive inference from repeated observations. A typical proof over nonnegative integers establishes a **base case**, then demonstrates that if the claim holds for `n`, it holds for `n+1`.

Consider the claim that for every integer `n ≥ 1`,

```text
1 + 2 + ··· + n = n(n+1)/2
```

The base case `n=1` gives `1=1(2)/2`. Assume the formula holds for `n`. Adding `n+1` to both sides gives

```text
n(n+1)/2 + (n+1) = (n+1)(n+2)/2
```

which is precisely the formula for `n+1`. Under the induction principle this proves the identity for all `n≥1`.

An **invariant** is a property maintained across specified transitions. Proving that an invariant holds initially and is preserved by every allowed transition can establish system-level claims without enumerating all possible executions.

For example, an abstract counter defined to increment by exactly two from zero preserves the property *the counter is even*. This proof assumes that **only** the specified transitions occur; an uncontrolled external update would violate the model's premises.

The MIT [lecture notes for Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/) distinguish mathematical induction from state-machine invariants. Their [course readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) separately include induction, recurrences, graphs, and counting techniques.

## Recurrences and recursive definition

A **recurrence relation** expresses a term of a sequence using one or more previous terms. For example,

```text
a₀ = 0
a₁ = 1
aₙ = aₙ₋₁ + aₙ₋₂, for n ≥ 2
```

defines the Fibonacci sequence. The initial conditions are essential: the recurrence alone does not determine a unique sequence. Recurrences describe **mathematical dependencies between terms**. They do not necessarily prescribe a particular implementation strategy or memory layout.

An algorithm may compute recurrence terms iteratively, recursively with repeated work, or with memoization. Those performance and implementation distinctions belong in [Computation & Algorithms](../computation-algorithms/README.md).

## Discrete structure versus continuous model

Continuous quantities can be represented with discrete samples or categories. A discrete mathematical model can also describe an indefinitely large set, such as all integers. **Discrete is not synonymous with finite**, nor is it synonymous with binary.

The integer set is infinite and discrete. The real interval `[0,1]` is continuous in the ordinary real topology. A computer may approximate real-valued quantities through finite encodings; that implementation limit is distinct from the mathematical structure.

This distinction preserves the boundary between [Mathematics & Logic](README.md), [Physical & Electrical Principles](../physical-electrical-principles/README.md), and [Digital Systems & Hardware](../digital-systems-hardware/README.md).

## Related canonical concepts

[Numbers and Numerical Systems](numbers-and-numerical-systems.md) provides number domains, [Sets and Relations](sets-and-relations.md) provides membership, [Boolean and Predicate Logic](boolean-and-predicate-logic.md) provides formal implication, [State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) explains modeled change, and [Algorithms](../computation-algorithms/README.md) explains computation.

### References

- [MIT OpenCourseWare: Mathematics for Computer Science, 2024](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/).
- [MIT course lecture-note index](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/), including induction, counting, recurrences, and state machines.
- [MIT course readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/), including counting rules and proof techniques.

**Review note:** The counting, pigeonhole, recurrence, induction and discrete-versus-continuous distinctions have been checked against MIT's source index and directly recalculated illustrative values. The revised generalized pigeonhole statement allows empty categories. The Batch 04 claim audit documents model-assisted review; G-01 mathematics breadth remains separately open.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
