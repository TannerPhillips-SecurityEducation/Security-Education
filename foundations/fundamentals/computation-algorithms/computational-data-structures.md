# Computational Data Structures

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Computational data structures  
**Development status:** Draft  
**Source review:** Authoritative references listed; separate scoped technical audit pending

## Data organization determines the cost of operations

A **computational data structure** organizes values and relationships to support specified operations with particular correctness and resource properties. A structure is selected not only by the kind of information it holds, but also by the operations a procedure must perform: lookup, insertion, deletion, traversal, update, and others.

An **abstract data type (ADT)** defines a logical collection of values and its permitted operations, without requiring one representation. A **representation or implementation** realizes those operations through concrete storage and algorithms. Several structures can implement the same ADT with different complexity and physical performance.

[Data Structures and Formats](../information-data/data-structures-and-formats.md) owns general representation and serialization. This article owns **computational operations, invariants, and cost tradeoffs**. [Data Types](../information-data/data-types.md) owns value domains, while [Memory and Storage](../digital-systems-hardware/memory-and-storage.md) owns the underlying physical hierarchy.

## Operations and their governing assumptions

Common computational structures include arrays, linked structures, stacks, queues, hash tables, search trees, heaps, and graph representations. These are **illustrative structures**, not a new approved heading hierarchy.

| Structure or representation | Useful modeled operation | Important qualification |
| --- | --- | --- |
| Indexed contiguous array | Direct index access | Inserting at front can shift many elements |
| Linked sequence | Local insertion with a known node | Finding a particular index can require traversal |
| Stack | Push/pop at one end | Does not offer unrestricted random lookup by stack semantics |
| Queue | Add at one end, remove at another | Performance depends on the actual representation |
| Hash table | Expected efficient key lookup under assumptions | Collisions and adversarial distributions affect cost |
| Balanced search tree | Ordered key operations | Balancing imposes invariants and update work |
| Heap | Access to highest-priority element | Not necessarily sorted by arbitrary index |

The [MIT 6.006 Introduction to Algorithms syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/) includes dynamic arrays, hash tables, heaps and balanced search trees, along with algorithmic analysis.

No row should be read as a universal performance guarantee independent of input size, representation, cost model, hardware or implementation.

## Representation invariants

A **representation invariant** states conditions that must hold for the data representation to satisfy its intended abstract contract. For a binary min-heap stored in an array, one such invariant is that every parent's key is no greater than the keys of its children.

If a structure violates its invariant, an operation that assumes the invariant can return incorrect results even if the structure still occupies valid memory. Conversely, an implementation can preserve its invariant while the input values are semantically wrong.

Operations must preserve stated invariants under their preconditions. Correctness follows from those conditions and proofs or checks, not from the structure's familiar name.

## Worked example: growing a dynamic array

Consider an idealized dynamic array with initial capacity one, containing zero items. Whenever a new append would exceed capacity, the implementation allocates a new array with **twice the current capacity**, copies all existing items, and then writes the new item.

For eight appends:

| Append number | Capacity after append | Existing items copied by resize |
| ---: | ---: | ---: |
| 1 | 1 | 0 |
| 2 | 2 | 1 |
| 3 | 4 | 2 |
| 4 | 4 | 0 |
| 5 | 8 | 4 |
| 6 | 8 | 0 |
| 7 | 8 | 0 |
| 8 | 8 | 0 |

The example performs **eight ordinary item writes and seven resize copies**, totaling fifteen modeled item write/copy operations. An individual resize can take linear time in the number of stored items, but the total copying across repeated doubling grows geometrically rather than quadratically.

Over a sequence of `n` appends under this capacity policy, the cumulative resize-copy count is less than `2n` for `n≥1`; counting one item write per append gives fewer than `3n` item writes/copies. Thus appending has **amortized O(1)** modeled item-operation cost under these assumptions, although a particular append can be **O(n)**.

This is a mathematical representation model; actual memory allocation, element construction and copying can have different costs.

## Hashing, collisions and distribution assumptions

A **hash function** maps a key to a hash value used to guide placement or lookup. Different keys can produce the same hash value, a **collision**. A hash table requires a collision-resolution strategy and rules for key equality.

An expected constant-time lookup claim usually depends on bounded load, a suitable key distribution or hashing assumptions, and a specific implementation. A deliberate collision-heavy input can degrade certain table implementations. A cryptographic hash's security properties and a hash table's expected lookup behavior are separate topics.

The choice between a hash table and an ordered tree may depend on whether the consumer needs sorted traversal, range queries, exact-match lookup, stable iteration or predictable worst-case operations.

## Memory layout and physical effects

A contiguous array can support efficient sequential access due to locality, while pointer-linked structures may require scattered memory reads. This is an implementation consideration, not a theorem that every array is faster than every linked structure for every workload.

Real performance depends on cache hierarchy, allocation overhead, branch behavior, concurrency, memory pressure and language runtime. [Computational Efficiency](computational-efficiency.md) owns evaluation of these practical constraints; [Complexity](complexity.md) owns formal asymptotic bounds.

## Canonical boundaries

The shape of a record is not the same as its computational structure; a JSON array is an exchange representation, not a guarantee that the consumer uses an actual contiguous dynamic array. Similarly, a graph's mathematical structure does not prescribe one adjacency representation or traversal algorithm.

[Algorithms](algorithms.md) owns general procedure contracts; [Algorithm Design](algorithm-design.md) owns strategy selection; [Iteration and Recursion](iteration-and-recursion.md) owns repeatable execution mechanisms.

### Sources

- [MIT 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/).
- [MIT 6.006: Syllabus and data-structure topics](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/).
- [MIT 6.005: Software Construction, Readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).

**Editorial status:** Substantive Draft. Doubling-array arithmetic, complexity bounds and invariants require a dedicated scoped technical and source review. No assessments, implementation mandates or new category are introduced.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
