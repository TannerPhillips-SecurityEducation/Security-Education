# Scheduling

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Scheduling  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## A scheduler allocates limited execution opportunities

**Scheduling** is the selection and allocation of execution opportunities among eligible tasks, threads or processes under a defined policy and available resources. It is related to, but different from, creating work, prioritizing goals or guaranteeing that all work finishes on time.

A scheduler may seek low response time, short average waiting time, fairness, deadline satisfaction, throughput, energy efficiency or another defined objective. Such goals can conflict. A policy is meaningful only with a workload model, arrival times, task durations, preemption assumptions and resource constraints.

[MIT Operating System Engineering](https://pdos.csail.mit.edu/6.S081/2026/schedule.html) addresses thread switching, coordination, processor resources and OS architecture. [Processes and Threads](processes-and-threads.md) owns schedulable contexts; this article owns selection criteria and measured scheduling behavior.

## State and policy

A **runnable** task is eligible to execute under the OS's rules but need not run immediately. A **blocked** task is waiting for a resource, timer, event or other condition. A **running** task currently occupies an execution resource under a chosen model.

**Preemptive scheduling** permits the system to interrupt a running task and schedule another. **Cooperative scheduling** relies on explicit yielding or blocking under relevant rules. Neither label alone determines responsiveness or fairness.

Common illustrative strategies include first-come-first-served, shortest-job-first, round-robin, priority scheduling and weighted allocation. These are not a newly approved taxonomy. A policy's actual implementation may combine selection, time slicing, aging, affinity and resource controls.

## Worked example: waiting-time tradeoff

Suppose three tasks arrive simultaneously at time zero and use a **single processor**. Their known service demands are A=4, B=3, C=2 time units. Assume no context-switch cost, no I/O blocking and nonpreemptive execution.

**First-come-first-served**, in the declared arrival/tie-break order A→B→C, produces:

| Task | Start | Finish | Waiting |
| --- | ---: | ---: | ---: |
| A | 0 | 4 | 0 |
| B | 4 | 7 | 4 |
| C | 7 | 9 | 7 |

Average waiting time is `(0+4+7)/3=11/3≈3.67` units.

**Shortest-job-first** instead runs C→B→A, giving waiting times 0, 2 and 5, for an average `7/3≈2.33` units. Under this toy workload, the second policy improves mean waiting time. It does not establish a universal best policy: true task durations may be unknown, short-task preference can cause starvation under continual arrivals, and deadlines or fairness may dominate the chosen objective.

## Response, turnaround and completion

**Waiting time** measures intervals spent eligible but not executing under a declared accounting model. **Turnaround time** usually measures submission/arrival to completion. **Response time** measures arrival to first response, which may differ from completion.

An average can conceal long tail delays for an individual task. Reporting only throughput can hide latency or starvation. A schedule that minimizes mean waiting time may still violate an urgent task's deadline.

For interactive or mixed workloads, priority and time-slice settings can affect user experience. A deadline-aware design must consider worst-case execution time, blocking, interrupt effects and resource sharing.

## Multi-core and resource interactions

On multiple processors, scheduling can assign work across cores, preserve affinity or migrate tasks. Migration may improve load balance while affecting caches, memory access and power. Lock contention and blocking dependencies also influence throughput.

A runnable task can wait while all processors are occupied; a task can also be blocked despite idle cores. Thus adding cores does not guarantee proportional speedup.

[Concurrency and Parallelism](../computation-algorithms/concurrency-and-parallelism.md) owns the general distinction between concurrent and simultaneous execution. [Computational Efficiency](../computation-algorithms/computational-efficiency.md) owns performance evaluation, while [Resource Management](resource-management.md) owns quotas and competing system resources.

## Correctness and scope

Scheduling decisions can have correctness implications when time constraints are part of a requirement. However, a real-time designation or high priority is not itself proof of meeting deadlines. The result depends on all interference and execution assumptions.

No scheduling policy, fairness metric, realtime deadline, or specific OS kernel is mandated by this reference.

### Sources

- [MIT 6.1810: Operating System Engineering](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [Operating Systems: Three Easy Pieces, official chapters on scheduling](https://research.cs.wisc.edu/wind/OSTEP/).
- [MIT Computer Systems Engineering course description](https://catalog.mit.edu/subjects/6/).

**Editorial status:** Substantive Draft. Scheduling arithmetic, policy distinctions and performance claims require a scoped technical review. No learner assessment or new subject heading is added.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
