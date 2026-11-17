# Sets and Relations

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Sets and relations  
**Development status:** Draft  
**Source review:** Core claims checked (see [pilot technical review](../PILOT-TECHNICAL-REVIEW.md)); final editorial acceptance pending

## Understanding collections and associations

A **set** is a collection of distinct elements considered as one mathematical object. Membership is the defining operation: for an element `x` and a set `A`, the expression `x ∈ A` asserts that `x` belongs to `A`. In ordinary extensional set theory, the members determine which set it is; repeated listing does not add another member, and the written order of members does not matter.

For example, `A = {2, 4, 6}` and `B = {6, 2, 4, 2}` denote the same set. By contrast, the **ordered sequence** `(2, 4, 6)` is different from `(6, 2, 4)`. An unordered collection and an ordered sequence support different kinds of reasoning, even if they mention the same values.

A set need not be a collection of numbers. It may represent possible system states, messages, components, users, or abstract objects. The mathematical notion itself is independent of any application. A set **does not** specify how its membership is stored in memory or how quickly an implementation can look up an element; those are separate computational questions.

## Basic structures

The **empty set** `∅` has no elements. If every element of `A` belongs to `B`, then `A ⊆ B`: `A` is a **subset** of `B`. Equality of sets means that each is a subset of the other.

| Operation | Expression | Meaning |
| --- | --- | --- |
| Union | `A ∪ B` | Elements in at least one of the sets |
| Intersection | `A ∩ B` | Elements in both sets |
| Difference | `A ∖ B` | Elements of A not in B |
| Cartesian product | `A × B` | Ordered pairs `(a, b)` with `a ∈ A` and `b ∈ B` |
| Power set | `P(A)` | The set of all subsets of A |

For `A = {a, b}` and `B = {1, 2}`, the Cartesian product is

```text
A × B = {(a,1), (a,2), (b,1), (b,2)}
```

The product preserves **position** in each ordered pair. If `A` and `B` are finite, the number of pairs is `|A × B| = |A| · |B|`.

## Relations as structured associations

A **binary relation from A to B** is a subset `R ⊆ A × B`. It selects which pairs of elements are associated. We write `a R b` when `(a,b) ∈ R`.

Suppose `A = {u1, u2}` is a set of abstract entities and `B = {r1, r2}` a set of abstract resources. A relation might be

```text
R = {(u1,r1), (u1,r2), (u2,r2)}
```

This asserts three associations. It says nothing, by itself, about *why* they exist, whether they are authorized, or how they are enforced. Meaning is supplied by the model interpreting the relation.

A relation **on A** is a subset of `A × A`. Such a relation can possess properties that matter across mathematics and computing:

- **Reflexive:** every `a` satisfies `a R a`.
- **Symmetric:** whenever `a R b`, also `b R a`.
- **Antisymmetric:** if `a R b` and `b R a`, then `a = b`.
- **Transitive:** if `a R b` and `b R c`, then `a R c`.

These properties are independent. In particular, **antisymmetric does not mean not symmetric**. A partial order is reflexive, antisymmetric, and transitive. An equivalence relation is reflexive, symmetric, and transitive. Equivalence partitions a set into classes of mutually equivalent elements; a partial order captures an ordering that need not compare every pair.

The subset relation `⊆` on a collection of sets provides a partial-order example. For instance, `{a} ⊆ {a,b}` and `{b} ⊆ {a,b}`, but `{a}` and `{b}` are not comparable by inclusion. In this example, distinct sets cannot include one another in both directions, illustrating *antisymmetry*, while equality of sets is symmetric. These properties should not be conflated.

## Functions and graphs: connected but different

A **function** from `A` to `B` may be represented by a binary relation in which *each element of A has exactly one corresponding element of B*. Arbitrary relations may connect one element to many, one to none, or many to one.

A directed **graph** can represent a relation on a set by drawing each element as a vertex and each related ordered pair as an edge. But the drawn picture is a **representation** of a relation, not the definition of every graph or every relationship in reality. Additional constraints can be imposed through the models we choose.

## Distinctions that prevent conceptual drift

**Membership versus subset:** `x ∈ A` concerns an element; `A ⊆ B` concerns all members of one set being members of another. The statements are not interchangeable.

**A mathematical set versus a software collection:** a software list may contain duplicates and preserve order, whereas a mathematical set has distinct elements and does not encode a sequence order.

**A relation versus its interpretation:** a set of ordered pairs is a formal structure. Labels such as *depends on*, *owns*, or *connected to* are modeled interpretations, and a real-world relationship may require time, direction, scope, or other context.

## Where this knowledge is reused

Set membership provides a foundation for classification and typed grouping; relations support dependency diagrams, graph edges, associations between data records, and definitions of functions. This does not make those applications new definitions of set theory.

Related approved areas include [Relationships](../models-abstraction/README.md), [Graph theory](README.md), [Data structures and formats](../information-data/README.md), and [Dependencies](../systems-engineering/README.md). Those links currently lead to area indexes until individual canonical articles exist.

## References and verification status

- [MIT OpenCourseWare: Mathematics for Computer Science, lecture notes](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/), especially relations and counting.
- [MIT OpenCourseWare: Mathematics for Computer Science, readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/), covering sets, relations, and proofs.
- [Open Logic Project: Sets, Logic, Computation](https://slc.openlogicproject.org/) for more formal treatment of set-theoretic and logical foundations.

**Review record:** Core mathematical definitions, the subset/partial-order distinctions, and the worked set and relation examples were checked in a second-pass technical review against the cited MIT/Open Logic material and direct example evaluation. This is a **source-checked draft**, pending final editorial acceptance; it is not a claim that every possible application of set theory has been verified.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Canonical ownership register](../CANONICAL-OWNERSHIP-REGISTER.md)
