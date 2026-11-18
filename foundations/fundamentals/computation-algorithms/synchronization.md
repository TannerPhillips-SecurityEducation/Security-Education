# Synchronization

**Knowledge area:** [Computation & Algorithms](README.md)  
**Approved subject heading:** Synchronization  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave D Batch 02 technical audit](../WAVE-D-TECHNICAL-REVIEW-02.md); independent human peer review pending

## Coordination constrains concurrent operation

**Synchronization** establishes specified relationships among concurrent computational activities, including mutual exclusion, event ordering, communication and visibility of shared state. It is not the same as concurrency itself: activities can be concurrent without appropriate synchronization, and some synchronization mechanisms can be used when physical parallelism is absent.

Synchronization is correct only relative to a defined contract and execution or memory model. A lock, barrier, queue or atomic instruction is a mechanism; its presence does not by itself prove a correct program.

[Concurrency and Parallelism](concurrency-and-parallelism.md) owns overlapping activities and interleaving models. This article owns **ordering, atomicity, synchronization invariants and progress constraints**. [Operating System Principles](../operating-system-principles/README.md) will own particular kernel and thread APIs.

The [MIT 6.005 Software Construction readings](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/) cover locks, synchronization, thread safety, and deadlock, emphasizing explicit correctness arguments.

## Mutual exclusion and critical sections

A **critical section** is a region of operations requiring coordination to preserve a stated shared-state invariant. **Mutual exclusion** ensures that no more than the allowed number of activities occupy a protected section simultaneously, under the lock contract.

For example, a mutex can protect reading and updating a shared counter, provided every relevant access follows the same locking discipline. If one activity modifies the counter outside the protocol, the intended invariant may no longer hold.

Mutual exclusion is neither sufficient for all concurrency correctness nor a guarantee of progress. It may introduce waiting, priority inversion or deadlock.

## Atomicity, visibility and ordering

An **atomic operation** has a defined indivisibility property under a particular memory or execution model. **Visibility** concerns which updates another activity can observe, and **ordering** constrains which observations and effects can be reordered.

Different languages and CPUs have different memory-order semantics. A read and write written in adjacent source-code lines are not automatically one atomic read-modify-write transaction.

A synchronization contract might provide *happens-before* relationships or comparable ordering rules; exact definitions must be taken from the chosen model. This article does not impose a specific language memory model.

## Worked example: protecting a shared count

Suppose a shared counter begins at zero and two activities each need to increment it exactly once. Under uncoordinated read-then-write operations, both may read zero and both write one.

If instead each activity performs one **linearizable atomic fetch-and-add(1)** operation with no overflow and both operations complete, the two updates can be ordered in a sequential account:

```text
Initial counter = 0
First completed atomic add: 0 → 1
Second completed atomic add: 1 → 2
Final counter = 2
```

The result is **2** under those assumptions, regardless of which activity's operation takes effect first. A mutex-protected read and write can achieve the same final counter if all accesses obey the protocol. These are **specified mechanisms**, not a claim that arbitrary increments are atomic on every architecture.

The example does not address crashes, duplicate application requests, hardware faults or counter overflow. It also does not prove fairness or bound the time each activity waits.

## Deadlock, starvation and progress

A **deadlock** can occur when activities wait in a cyclic arrangement of dependencies that none can resolve under the given rules. For example:

```text
Task A acquires lock L1, then waits for L2
Task B acquires lock L2, then waits for L1
```

If both first acquisitions succeed and neither task releases its held lock while waiting, neither proceeds. One common mitigation is a shared lock-ordering rule requiring both tasks to acquire L1 before L2. Such a policy prevents **this specific lock-order inversion** when consistently followed; it does not solve every possible deadlock mechanism.

**Starvation** means an activity may fail to make progress because resource allocation or scheduling continually favors others, even if the system as a whole continues operating. Deadlock freedom and starvation freedom are distinct guarantees.

## Barriers, queues, semaphores and condition variables

A **barrier** coordinates participants at a defined phase boundary. A **semaphore** tracks permits under its semantics, potentially controlling access to a limited-capacity resource. A **condition variable** helps activities wait for changes in predicates associated with shared state, using the chosen synchronization protocol.

A message queue can also establish communication and ordering, but the exact guarantees depend on whether messages can be lost, duplicated or reordered and how consumers acknowledge them.

These mechanisms solve different coordination problems; none is universally superior. A barrier with a missing participant can stall, and a semaphore configured with the wrong permit count can violate a resource constraint.

## Invariants and testing limitations

Synchronization design should state the invariant being protected, the operations that can affect it, the visibility model, and the progress expectations. A lock acquisition that returns success is not proof that a subsequent I/O device operation completed physically.

Tests using a limited number of thread schedules cannot generally prove that no harmful schedule exists. Model checking and formal reasoning can establish properties **of stated models**, while real implementations still require correspondence assumptions and appropriate evidence.

[Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md) owns general formal semantics. [Reliability and Failure](../systems-engineering/reliability-and-failure.md) owns failure scenarios and availability, not every concurrency invariant.

## Canonical boundaries

Synchronization as a computational mechanism differs from communication protocol agreement, physical clock synchronization and organizational coordination. [Timing and Clocks](../digital-systems-hardware/timing-and-clocks.md) owns hardware timing; [Collaboration and Communication](../human-sociotechnical-systems/collaboration-and-communication.md) owns human coordination.

No mutex API, CPU architecture, threading library, verification platform or learner assessment is mandated.

### Sources

- [MIT 6.005: Software Construction Readings, Locks and Synchronization](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/pages/readings/).
- [MIT 6.005: Thread Safety](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/20-thread-safety/).
- [MIT 6.005: Software Construction Course](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/).

**Editorial status:** Reviewed (model-assisted) following the [Wave D Batch 02 scoped 30-family technical audit](../WAVE-D-TECHNICAL-REVIEW-02.md). Exhaustive source verification, independent human expert review and final publication acceptance remain open.

[Computation & Algorithms](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
