# Distributed State

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Distributed state  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Communication & Distributed Systems 54-family audit](../WAVE-E-TECHNICAL-REVIEW-02.md); independent human review pending

## Multiple nodes do not automatically share one instantaneous view

**Distributed state** concerns information and behavior maintained across separate processes or systems that communicate through channels and can experience delay, partial failure, reordering or temporary disconnection. A **replica** maintains a copy or representation of some shared logical state under a replication contract.

Two replicas can temporarily disagree without either storage system necessarily being defective, depending on what consistency guarantees the system promises. Conversely, agreement between replicas does not establish that the underlying data describe the real world accurately.

[State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) owns abstract state and change, [Data Provenance and Lifecycle](../information-data/data-provenance-and-lifecycle.md) owns lineage and recorded history, and this article owns **replication, partially observed updates and consistency contracts**.

## Replication, consistency and availability

Replication can support continued access or resilience in selected failure scenarios, but introduces coordination and conflict questions. Copies may be updated synchronously, asynchronously or by another mechanism. The required latency, availability and consistency guarantees depend on the protocol and failure assumptions.

**Consistency** describes permitted relationships among operation histories and observations. It is not a single universal scale: a system might promise linearizable operations, causal consistency, eventual convergence or other defined properties.

**Linearizability** requires each completed operation to appear at a single point between its invocation and response, consistent with real-time ordering for the specified object/history. **Eventual convergence** can describe replicas that become consistent once updates stop and appropriate delivery/merge assumptions hold. These are different models with different constraints.

The [MIT 6.5840 Distributed Systems course](https://pdos.csail.mit.edu/6.5840/) focuses on replication, fault tolerance and consistency using specific case studies.

## Worked example: stale read

Suppose replicas A and B initially report a value of **5**. A processes an update to **6**, but the updated state has not yet reached B. Immediately afterward, a reader asking B receives **5**.

```text
Initial:  A=5  B=5
Update at A: A=6  B=5
Read at B: 5
After propagation: A=6  B=6
```

Under an asynchronous replication contract permitting stale reads, these observations may be allowed. Under a properly implemented linearizable read/write contract for that object, a read that begins after a completed write of 6 cannot validly return the earlier value 5. The distinction requires defined operation boundaries and system guarantees.

A name of a consistency model does not replace evidence that an implementation satisfies it.

## Partial failure and uncertainty

Nodes may remain operational while communication between them fails. A caller that times out cannot always distinguish a crashed recipient from a slow recipient or an unreachable path. Network partitions and independent recoveries complicate agreement about recent operations.

A distributed system must decide which operations remain possible, which can be delayed and which guarantees must be preserved under the assumed faults. Vague claims that a system is “always consistent and always available” have no meaning without precise definitions and failure conditions.

[Communication Channels](communication-channels.md) owns path limitations, [Reliability and Ordering](reliability-and-ordering.md) owns message-delivery semantics, and [Synchronization and Coordination](synchronization-and-coordination.md) owns agreement mechanisms.

## Versioning, conflicts and merge semantics

Updates can arrive in different orders. A version counter or timestamp may help identify selected ordering relationships but does not automatically supply a total causally correct history across all nodes.

For a **counter**, a merge function may combine increments under a suitable conflict-free data structure. For a bank transfer or reservation, arbitrary merging can violate conservation or resource limits. A conflict strategy must match the meaning of the data and its required invariants.

A replicated state machine uses agreed operation ordering and deterministic application of state transitions under selected conditions. This is a powerful pattern, not a proof that every replica's external effects are duplicated safely.

## Canonical boundaries

Distributed state is distinct from database format, local OS process state, a network address and a hardware clock. G-04 general temporality remains a separate unresolved scope decision; this article describes temporal relationships only as required by distributed-state contracts.

No particular database, replication technology, cloud vendor, consensus algorithm or learner assessment is mandated.

### Sources

- [MIT 6.5840: Distributed Systems](https://pdos.csail.mit.edu/6.5840/).
- [Linearizability: A Correctness Condition for Concurrent Objects (original published result)](https://doi.org/10.1145/78969.78972).
- [MIT 6.5840: Course Project Ideas and Consistency Models](https://pdos.csail.mit.edu/6.5840/project.html).
- [MIT 6.1800: Computer Systems Engineering](https://catalog.mit.edu/subjects/6/).

**Editorial status:** Reviewed (model-assisted) following the [Wave E Communication & Distributed Systems 54-family technical audit](../WAVE-E-TECHNICAL-REVIEW-02.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
