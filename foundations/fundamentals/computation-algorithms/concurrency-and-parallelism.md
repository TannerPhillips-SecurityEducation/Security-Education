# Concurrency and Parallelism

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Concurrency and parallelism  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Batch 02 technical audit](../WAVE-D-TECHNICAL-REVIEW-02.md); independent human peer review pending

## Multiple activities can overlap without executing simultaneously

**Concurrency** concerns systems in which multiple computational activities are in progress over an interval and may interact, coordinate or interleave. **Parallelism** concerns actual execution of multiple operations at the same time on distinct execution resources. A concurrent design may execute on one processor by interleaving tasks; a parallel implementation may exploit multiple cores or other simultaneous hardware execution resources.

These terms are related but not interchangeable. A program can have concurrent tasks that never run simultaneously, and an implementation can process data in parallel while presenting a single logical task.

The [MIT 6.005 Software Construction readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/) distinguish shared-memory concurrency, message passing, interleavings, and race conditions. [Computing Components](../digital-systems-hardware/computing-components.md) owns physical execution resources, while this subject owns computational activities and their possible overlap.

## Processes, tasks, threads and actors are model-dependent

A **task** is an activity or unit of computational work identified by the chosen model. A **thread** is one execution context in a particular programming or operating environment. A **process** commonly owns an isolation and resource context in an operating system. An **actor** is a computational abstraction that communicates through messages under an actor-model contract.

These terms do not form a universal hierarchy. Some runtimes schedule lightweight tasks on a smaller set of OS threads, and distributed services can communicate without sharing memory. The operating-system-specific mechanics belong in [Processes and Threads](../operating-system-principles/README.md), while the algorithmic problem of coordinating logically concurrent activities belongs here.

Concurrency also does not imply nondeterminism in every observable result. A correctly synchronized concurrent system may produce deterministic outputs under its contract even when internal scheduling differs.

## Interleavings and shared state

An **interleaving** describes one ordering of operations from concurrent activities consistent with their individual order constraints. Distinct interleavings can produce different results when operations interact through mutable shared state.

Consider two tasks intending to increment a shared integer counter initially equal to zero. Suppose each increment is implemented as a separate read and write:

```text
Task A: read counter → localA; write localA+1
Task B: read counter → localB; write localB+1
```

One possible interleaving is:

```text
A reads 0
B reads 0
A writes 1
B writes 1
Final shared counter = 1
```

Two increments were requested, but one update was lost. The example assumes independent read and write steps with no coordination; it does not describe how any particular language or CPU guarantees visibility and ordering. If an implementation uses one atomic increment operation, the same interleaving argument does not apply.

[Synchronization](synchronization.md) owns the mechanisms establishing appropriate atomicity, ordering and visibility.

## Race conditions and data races

A **race condition** occurs when correctness depends on timing or ordering of events that the design does not adequately constrain. A **data race** has a more specific meaning in many language memory models, commonly involving conflicting unsynchronized accesses to shared memory; the exact rules depend on the language.

It is therefore inaccurate to equate every race condition with a data race or every variable accessed by two tasks with a bug. Immutable data, explicitly ordered communication or correct synchronization can permit safe concurrent use.

An execution that appears correct in repeated tests does not prove the absence of harmful alternative interleavings. Controlled scheduling, model checking and stress tests can expose some cases, but exhaustive guarantees require a suitable formal model and evidence.

## Message passing and shared memory

**Shared-memory coordination** allows activities to read and modify agreed shared state, requiring a contract for atomic operations and visibility. **Message passing** communicates values or events through channels, queues or other means; it can reduce shared mutable state but introduces ordering, delivery, buffering and failure questions.

Neither is automatically safe or faster. A message-passing system can deadlock on waits or lose messages under certain conditions. A shared-memory system can be correct when synchronization and ownership are justified.

[Data Provenance and Lifecycle](../information-data/data-provenance-and-lifecycle.md) owns recorded lineage; [Communication & Distributed Systems](../communication-distributed-systems/README.md) owns networked delivery and distributed partial-failure mechanisms.

## Parallel speedup and its limits

Suppose a toy computation takes one normalized time unit and has an **80% perfectly parallelizable portion** and a **20% irreducibly serial portion**. With four equally capable processors, negligible overhead and no resource contention, Amdahl's fixed-workload model predicts:

```text
S(4) = 1 / (0.20 + 0.80/4)
     = 1 / 0.40
     = 2.5
```

The expected ideal speedup is **2.5×** under the assumptions, not 4×. Synchronization, communication, memory contention, scheduling and workload imbalance can further limit actual performance. Different models and workloads can change the prediction; the speedup formula is not a benchmark of real hardware.

[Complexity](complexity.md) owns asymptotic resource bounds; [Computational Efficiency](computational-efficiency.md) owns measured and modeled engineering performance.

## Correctness and performance obligations

A concurrent algorithm can preserve a correct final value but fail a responsiveness or fairness requirement. A parallel algorithm can produce faster results but use more memory, energy or coordination work. Correctness conditions and performance claims must therefore be separately stated.

Some computations require preserving causal or program order; others permit reordering if externally observable behavior remains within the contract. An implementation detail such as a particular instruction interleaving should not be confused with the system's promised semantics.

### Sources

- [MIT 6.005 Software Construction: Readings on Concurrency and Thread Safety](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).
- [MIT 6.005: Thread Safety](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/20-thread-safety/).
- [MIT 6.172: Performance Engineering of Software Systems](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/).

**Editorial status:** Reviewed (model-assisted) following the [Wave D Batch 02 scoped 30-family technical audit](../WAVE-D-TECHNICAL-REVIEW-02.md). Exhaustive source verification, independent human expert review and final publication acceptance remain open.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
