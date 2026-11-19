# Dependencies

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Dependencies  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 03 audit](../WAVE-B-TECHNICAL-REVIEW-03.md); no independent human peer review

## A dependency is a qualified reliance relationship

A **dependency** is a relationship in which the availability, behavior, validity, or performance of one element relies on another condition, element, resource, or outcome under stated assumptions. Dependencies matter because elements rarely produce their intended contribution in complete isolation.

A dependency assertion should specify **what depends on what**, **for which purpose**, and **under which conditions**. It is not inherently a physical connection, causal edge, ownership relationship, software package import, temporal ordering, or mathematical implication. Several different relations can be modeled with similar arrows while having different meanings.

[Relationships](../models-abstraction/relationships.md) owns the general notion of associations. [Graph Theory](../mathematics-logic/graph-theory.md) owns directed graphs and connectivity. This article owns *system-level reliance*, propagation assumptions, and the consequences for engineering design and operation.

## Direction and conditions

Consider a hypothetical system in which a recorder requires both a sensor feed and a storage service:

```text
Recorder -> requires -> Sensor feed
Recorder -> requires -> Storage service
Storage service -> requires -> Power
```

Here `A -> requires -> B` means that A's intended operation depends on B under the modeled operating mode. The direction is declared; it is not a claim that the arrow is a data-flow direction. If power is unavailable, storage might be unavailable and the recorder might fail to record, **provided those stated requirements and failure assumptions actually apply**.

A graph edge by itself cannot justify a specific failure probability, causal mechanism, or real-world occurrence. An unmodeled battery, cache, alternate path, or degraded mode could change the dependency relation.

## Hard, conditional, and substitutable reliance

Dependency descriptions may distinguish different conditions:

| Illustrative pattern | Meaning |
| --- | --- |
| Necessary under a mode | Without B, A cannot fulfill a stated function in that mode |
| Conditional | A requires B only if a particular operation or environment is selected |
| Substitutable | A requires one of several acceptable alternatives, rather than a particular single resource |
| Performance-affecting | Reduced B capability degrades A, without necessarily making A fully unavailable |
| Shared resource | A and C rely on the same B, creating a possible correlated failure path |

These are **editorial distinctions**, not a mandated formal taxonomy. Whether a dependency is necessary must be justified by the chosen behavioral model and context.

If a recorder can write to either storage service B or C, the requirement may be `B OR C`, not `B AND C`. Drawing two unlabeled arrows could conceal that decisive difference.

## A dependency graph is not necessarily a failure model

Dependency graphs can help identify candidate points of failure, change impact and coupling. They do not automatically predict how failure propagates.

For example, suppose A requires B, and B requires C. If C becomes unavailable and there is no alternative to C, B may be unable to function, and A may in turn be unable to perform its required task. That is a **conditional propagation scenario**. It does not establish the probability of failure, the time to failure, or the absence of fallback resources.

The same graph may represent planned tasks, supply relationships, service prerequisites, or runtime resource requirements. The meaning of every edge and the definition of a node must travel with the model.

## From dependency edges to failure conditions

A reliance graph answers *which components are required for a stated function*. A failure model adds a different question: *which combinations of component states make that function unavailable?* The second question requires an explicit success criterion, operating mode, time boundary, fallback behavior, and assumptions about how faults affect services.

Consider a hypothetical recorder that needs a sensor `S` and at least one of two interchangeable storage services `B` or `C`. Define each variable as **true when the corresponding service fulfills its required function at a sampled instant**. Assume storage can switch immediately and correctly, with no buffer loss, switching delay, degraded mode, or additional hidden prerequisites. Then:

```text
Required success:      Recorder_up = S AND (B OR C)
Corresponding failure: Recorder_down = NOT S OR (NOT B AND NOT C)
```

This follows by De Morgan's laws. The recorder can tolerate loss of **one** storage service but not loss of the sensor or of **both** storage services. A different operating contract, such as requiring both stores for synchronous replication, would produce a different expression even if an unlabeled dependency drawing used the same three component names. In fault-tree terms, the top failure is an OR of sensor failure and the AND of both storage failures; this is **modeled event logic**, not an observed outage.

### A numerical example, and why dependence matters

Suppose the events `S_down`, `B_down`, and `C_down` refer to **the same hypothetical instant**, with probabilities `0.02`, `0.10`, and `0.10`. If these three down-state events are mutually independent, then:

```text
P(B_down AND C_down) = 0.10 × 0.10 = 0.01
P(Recorder_up)        = (1 - 0.02) × (1 - 0.01) = 0.9702
P(Recorder_down)      = 1 - 0.9702 = 0.0298 = 2.98%
```

Without backup storage C, the same assumptions instead give `P(down) = 1 - (0.98 × 0.90) = 0.118 = 11.8%`. The modeled redundancy reduces point-in-time unavailability from **11.8% to 2.98%** under those assumptions.

Now retain the same *marginal* 10% storage unavailability rates but suppose B and C **always fail together**, while their joint outage remains independent of sensor unavailability. The intersection `P(B_down AND C_down)` is then `0.10`, **not** `0.01`. Recorder unavailability returns to `1 - (0.98 × 0.90) = 11.8%`. The graph still shows two storage alternatives; its apparent redundancy does not remove their shared failure mode.

This calculation is **not measured device reliability**, a mission-duration failure probability, or an availability forecast. It is a same-instant Boolean event model with explicitly assigned probabilities. For arbitrary storage dependence, `P(B_down AND C_down)` must be established rather than replaced by a product. A delayed or imperfect switchover, restoration process, overload during failover, or correlated sensor failure requires a richer model.

The [NASA *Fault Tree Handbook with Aerospace Applications*, version 1.1 (August 2002), Chapters 4 and 6](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf) distinguishes AND/OR event gates and gives the general inclusion-exclusion formula `P(A OR B)=P(A)+P(B)-P(A AND B)`; replacing the intersection with a product requires independence. [Reliability and Failure](reliability-and-failure.md) owns duration-dependent reliability and repair/availability interpretations. [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns the underlying probability rules.

## Cycles and ordering

A directed cycle in a dependency graph can signal a potential design challenge, but **not every cycle is invalid**. Cyclic dependencies can represent mutual coordination, coupled physical feedback, recursive function calls or circular prerequisite constraints; the consequences depend on system semantics.

A scheduling prerequisite model with a strict “must finish before” relation cannot contain a feasible directed cycle when every task must eventually finish. A feedback control loop, by contrast, is intentionally cyclic and may be appropriate or even necessary.

A **directed acyclic graph (DAG)** admits a topological order, but that graph property alone does not establish that a real system can be constructed or that a schedule has enough capacity. [Graph Theory](../mathematics-logic/graph-theory.md) owns the formal theorems; [Feedback and Control](feedback-and-control.md) is the separate approved subject for purposeful feedback mechanisms.

## Critical paths require an explicit interpretation

For a simplified task network, let task A take 2 units of time, task B take 3 units after A, task C take 5 units after A, and task D take 4 units after **both** B and C.

```text
A(2) -> B(3) --+
  |             +-> D(4)
  +----> C(5) --+
```

Under the assumptions that tasks start as early as permitted, have fixed durations, no resource constraints, and all listed dependencies are finish-to-start constraints, the completion time is `2 + max(3,5) + 4 = 11` time units. The longest prerequisite path is A→C→D with duration 11; A→B→D has duration 9.

This is a **toy critical-path calculation**, not a universal formula for system reliability or a prediction of actual project duration. Resource contention, uncertain durations and additional dependencies can change the schedule.

## Change impact, coupling, and risk

A change to a highly depended-upon component can affect multiple consumers. Possible impacts include incompatible interface contracts, version conflicts, lost functionality, altered timing or unexpected resource demand. **Transitive reachability** in a dependency graph identifies possible affected paths, not guaranteed disruption.

Two consumers sharing a dependency may experience correlated interruptions. Simply duplicating consumers does not remove a shared upstream risk. Likewise, modular decomposition may reduce some types of coupling but cannot eliminate physical resource requirements or every organizational dependency.

[Components and Interfaces](components-and-interfaces.md) owns interaction contracts; [Architecture and Composition](architecture-and-composition.md) owns whole-system organization. [Reliability and Failure](reliability-and-failure.md) develops failure and reliability interpretations under its own approved heading.

## Boundaries and references

Dependencies apply across physical, computational, organizational, and mixed systems. Contextual dependency management for software packages, network infrastructure, cloud services, manufacturing supply chains or security control systems belongs in specialized knowledge domains.

No universal dependency-predicate vocabulary, scheduling engine, risk score, or new taxonomy is approved by this article.

### Sources

- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).
- [NASA: Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/).
- [SEBoK: Requirements Management](https://sebokwiki.org/wiki/Requirements_Management).
- [MIT Mathematics for Computer Science readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/).

**Editorial status:** Reviewed (model-assisted) following the [Wave B Batch 03 scoped 24-family technical review](../WAVE-B-TECHNICAL-REVIEW-03.md). Complete source verification, independent human expert peer review and final publication approval remain separate outstanding gates.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
