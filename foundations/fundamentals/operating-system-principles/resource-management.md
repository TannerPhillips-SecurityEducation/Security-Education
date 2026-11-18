# Resource Management

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Resource management  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Operating System Principles 60-family audit](../WAVE-E-TECHNICAL-REVIEW-01.md); independent human review pending

## Operating systems allocate constrained shared resources

**Resource management** concerns allocating, accounting for, limiting and reclaiming computing resources under an operating-system model. Resources can include CPU time, memory, storage capacity, I/O bandwidth, handles, device access and other shared capacities.

**Allocation** is a decision to assign resource access or capacity. **Accounting** records selected usage. **Quota or limit** constrains permitted consumption, while **reservation** expresses a commitment of capacity under a contract. These are different states: a declared reservation does not necessarily mean the resource is currently being used.

This subject owns OS-level resource control and policy; [Scheduling](scheduling.md) owns which runnable execution contexts receive processing opportunities, [Memory Management](memory-management.md) owns memory-specific mechanisms, and [Computational Efficiency](../computation-algorithms/computational-efficiency.md) owns performance assessment.

## Ownership, isolation and sharing

An operating system can allocate resources to processes, users, groups, containers or other entities under a defined policy. Resource ownership may be exclusive, shared, time-divided or virtualized.

Isolation helps prevent one consumer from improperly affecting another, but no single resource limit proves complete isolation. Shared caches, I/O paths and hardware may introduce interference. A system can satisfy memory quotas while still failing due to CPU saturation or a shared storage bottleneck.

A resource may have several capacity measures, such as total storage bytes, I/O operations per second and network transfer rate. Comparing them requires consistent quantities and measurement boundaries.

## Worked example: competing reservation requests

Suppose a hypothetical pool has **10 indivisible resource units** available at a particular instant. Three independent clients request exclusive reservations of 4, 5 and 3 units. The total requested capacity is `4+5+3=12`, exceeding the available pool by **2 units**.

All three cannot simultaneously receive their complete requested allocations under this model. One valid admission decision could accept the 4-unit and 5-unit requests, reserving 9 units and leaving one unreserved. Another policy could select a different subset.

The arithmetic proves **infeasibility of admitting all three simultaneously**, not which selection is ethically or operationally best. Priorities, fairness, duration and consequences require explicit policy.

If the resource were shareable or overcommitted under different rules, the capacity model would need revision. The example is invented and not a physical memory measurement.

## Fairness, starvation and priority

Fairness can be defined through equal shares, weighted shares, waiting-time bounds or other criteria. Equal allocation does not automatically serve different workload requirements equally. A high-priority task can receive more resources while lower-priority tasks wait, which may be appropriate under some constraints and lead to starvation under others.

**Deadlock** can arise when resource holders wait for resources held by each other under unreleasable conditions. **Starvation** concerns failure of a particular request to make progress despite other progress. These require separate analysis and countermeasures.

[Dependencies](../systems-engineering/dependencies.md) owns conditional reliance models, and [Synchronization](../computation-algorithms/synchronization.md) owns mutual exclusion and progress conditions.

## Monitoring, limits and failure handling

An OS may account for current usage, historical activity, allocated capacity or peak demand. Those metrics are not equivalent. A program may reserve 1 GiB of virtual address space without currently using 1 GiB of physical memory.

Resource exhaustion can produce allocation failure, request delay, throttling, reclamation or termination, depending on the resource and policy. Retrying an unsuccessful request without understanding the capacity condition may aggravate overload.

Monitoring a reported counter does not prove that usage is measured accurately or that the measurement's scope matches a contractual limit. [Measurement](../scientific-analytical-reasoning/measurement.md) owns quantitative measurement concepts.

## Canonical boundaries

Resource management is not a general moral theory of allocation, a package-management process or a guaranteed method of optimizing all workloads. This article imposes no OS-specific control mechanism, quota unit or policy, and introduces no graded assessment.

### Sources

- [MIT 6.1810 Operating System Engineering](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [Operating Systems: Three Easy Pieces](https://research.cs.wisc.edu/wind/OSTEP/).
- [MIT 6.1800 Computer Systems Engineering overview](https://catalog.mit.edu/subjects/6/).

**Editorial status:** Reviewed (model-assisted) following the [Wave E OS 60-family technical audit](../WAVE-E-TECHNICAL-REVIEW-01.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
