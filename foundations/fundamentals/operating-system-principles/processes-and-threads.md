# Processes and Threads

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Processes and threads  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Operating System Principles 60-family audit](../WAVE-E-TECHNICAL-REVIEW-01.md); independent human review pending

## Execution needs ownership and scheduling context

A **process** is an OS-defined execution/resource context, commonly encompassing an address space and handles to operating resources. A **thread** is an execution path with its own instruction-progress and selected context, typically sharing portions of the containing process's resources with other threads. The exact boundaries depend on OS design.

A single process can contain several threads, and a system can have many processes. Neither concept is identical to a processor core, an algorithm, a task in a high-level runtime, or a file containing executable code.

The [MIT 6.1810 curriculum](https://pdos.csail.mit.edu/6.S081/2026/schedule.html) covers thread switching, scheduling, page tables and system calls. [Concurrency and Parallelism](../computation-algorithms/concurrency-and-parallelism.md) owns the general theory of overlapping tasks; this article owns its OS process/thread realization.

## Context and shared resources

A thread may have its own registers, program counter, stack and scheduling state, while threads in a process may share an address space, heap objects and open resources. This sharing is not a guarantee that every object is safe to modify concurrently.

Separate processes usually have OS-mediated boundaries between their address spaces, but can also establish shared-memory regions or other communication resources under defined permissions. A process boundary is a design protection mechanism, not proof of complete isolation from all timing, resource or hardware effects.

[Execution Contexts](execution-contexts.md) owns what must be preserved across execution transitions. [Memory Management](memory-management.md) owns mappings and protection.

## Process/thread state and lifecycle

Execution contexts can move among **created**, **runnable**, **running**, **waiting/blocked**, and **terminated** states in a simplified OS model. The precise labels, state machine and transitions vary. A runnable thread is eligible for scheduling but need not currently execute; a waiting thread may require an event or resource before becoming runnable.

Creating a process does not necessarily start a new physical processor, and exiting a thread need not terminate all other threads in the same process. Joining or waiting for completion is an explicit synchronization behavior, not an inevitable effect of creating a task.

## Worked example: shared versus isolated counters

Suppose two threads share one counter initially zero and each attempts a read-then-write increment. One possible interleaving reads zero twice and writes one twice, yielding **1**, not **2**. If instead the two threads use completed linearizable atomic increments, the final value is **2** under the stipulated no-overflow model.

If two separate processes each have a **private** counter initially zero and each increments its own counter once, their local results can both be **1** without representing a lost update. The apparent numerical similarity conceals different ownership.

The example does not claim all OS threads share every variable or that all processes are completely independent of shared resources. [Synchronization](../computation-algorithms/synchronization.md) owns atomicity/visibility reasoning.

## Switching, scheduling and overhead

A scheduler selects eligible execution contexts under a policy. A **context switch** preserves relevant outgoing state and establishes state for another context. It can introduce overhead, affect cache behavior and expose coordination or memory-visibility requirements.

Different execution contexts may use cooperative or preemptive scheduling. A timer interrupt can enable preemption under an OS model, but no universal timer interval or execution order follows from the existence of threads.

[Scheduling](scheduling.md) owns allocation policies and performance measures. [Kernels](kernels.md) owns privileged execution and global coordination.

## Failure and communication boundaries

A process crash may affect other processes through shared files, services or dependencies even when their address spaces are isolated. Conversely, a process can remain runnable after an individual thread fails, depending on language and OS behavior.

Interprocess communication may use pipes, shared memory, messages or other mechanisms. Actual delivery, ordering and failure guarantees belong to the relevant contract, including [Communication & Distributed Systems](../communication-distributed-systems/README.md) for separate nodes.

### Sources

- [MIT 6.1810: Thread switching](https://pdos.csail.mit.edu/6.S081/2026/homework/xv6-threads.html).
- [MIT 6.1810 Operating System Engineering](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [Operating Systems: Three Easy Pieces](https://research.cs.wisc.edu/wind/OSTEP/).

**Editorial status:** Reviewed (model-assisted) following the [Wave E OS 60-family technical audit](../WAVE-E-TECHNICAL-REVIEW-01.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
