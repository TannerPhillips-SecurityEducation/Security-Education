# Synchronization and Coordination

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Synchronization and coordination  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Coordinating separate nodes requires explicit guarantees

**Distributed coordination** concerns how independent processes or nodes align selected decisions, actions or views despite message delay, reordering, partial failure and incomplete information. **Distributed synchronization** can involve coordinating event order, resource access, state updates or clock estimates under an explicit system model.

These mechanisms are not equivalent to local thread synchronization. A mutex within one process may rely on shared-memory atomic operations; a lock or lease across nodes requires communication, identity, failure detection and assumptions about time or authority.

[Synchronization](../computation-algorithms/synchronization.md) owns local computational mutual exclusion, visibility and progress; this article owns **coordination across autonomous nodes**.

## Events, clocks and causal relations

Distributed participants may have local clocks that differ in rate or phase. A timestamp value is not automatically evidence of a globally ordered event. **Clock synchronization** attempts to limit differences under a stated error model, while a **logical clock** can represent ordering information without measuring physical elapsed time.

A causal relationship such as “message sent before it was received” constrains possible event order. Two independent events without a known causal link may remain incomparable in a partial-order model.

A total ordering may be constructed for selected operations by a protocol, but it does not follow simply because every node has a hardware clock. The general temporality decision G-04 remains open.

## Leadership, membership and agreement

A coordinator or **leader** may assign work, order updates or manage membership. Leadership can change after failure; an outdated leader may still believe it is authorized if it has not learned about a transition.

**Consensus** seeks agreement among participating nodes under a particular validity, safety and liveness contract. Different consensus protocols make different assumptions about failures, communication delay and membership. A single successful vote does not establish the long-run availability or correctness of the entire system.

[MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/) studies fault-tolerant replication and coordination through specific algorithms and systems, without defining one universal approach.

## Worked example: majority quorum intersection

Suppose there are three distinguishable voters A, B and C, with a quorum defined as any set of **two** voters.

Possible quorums are `{A,B}`, `{A,C}`, and `{B,C}`. Any two of these sets intersect in at least one voter. This follows because two disjoint groups of size two would require four distinct voters, but only three exist.

```text
Q1 = {A,B}
Q2 = {B,C}
Q1 ∩ Q2 = {B}
```

**Quorum intersection is a mathematical property, not a complete consensus protocol.** Preventing conflicting decisions also requires rules for how voters handle rounds, accepted values, failures and persistence. For example, if a voter were allowed to approve two conflicting values in the same round, intersection alone would not ensure agreement.

## Leases, locks and time assumptions

A **lease** grants an authority for a bounded period under declared timing assumptions. A stale holder and a new holder can overlap in their beliefs if clocks drift, messages are delayed or expiration is interpreted inconsistently. Fencing tokens, monotonic epochs or other mechanisms can help prevent outdated actors from performing unauthorized effects, under the receiving system's contract.

A distributed lock does not automatically protect a physical or external resource unless all relevant actors honor the lock or a downstream mechanism enforces its authority. A nominal lock service can be correct while consumers misuse its guarantees.

## Safety, liveness and partial failure

**Safety** concerns not reaching forbidden conditions, such as two conflicting committed results for one defined decision. **Liveness** concerns eventual progress under stated assumptions. A design may preserve safety during a network partition by refusing some operations, at the cost of availability.

Under unconstrained asynchronous delays and failures, unconditional consensus termination guarantees are not generally available. Any claim of guaranteed progress must specify restrictions such as synchrony, eventual synchrony, failure detectors, or other enabling assumptions.

[Distributed State](distributed-state.md) owns replica consistency and state histories. [Reliability and Ordering](reliability-and-ordering.md) owns message delivery and sequencing; coordination builds on them without replacing their definitions.

## Canonical boundaries

This article does not mandate Raft, Paxos, a distributed database, wall-clock infrastructure, cloud service or any universal quorum size. It introduces no new approved category or learner assessment.

### Sources

- [MIT 6.5840: Distributed Systems](https://pdos.csail.mit.edu/6.5840/).
- [MIT 6.5840: Project and Replication Examples](https://pdos.csail.mit.edu/6.5840/project.html).
- [MIT 6.1800: Computer Systems Engineering](https://catalog.mit.edu/subjects/6/).

**Editorial status:** Substantive Draft. Quorum example, consistency guarantees and timing assumptions require separate scoped technical review. No consensus implementation is prescribed.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
