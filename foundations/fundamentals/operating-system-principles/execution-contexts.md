# Execution Contexts

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Execution contexts  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Execution depends on preserved state and available authority

An **execution context** is the collection of state and conditions required to interpret and continue a computation at a chosen boundary. It may include register values, instruction location, stack, address-space association, privilege state, scheduler status, thread-local information and available resources.

A context is a *model-relative* concept: a user-level coroutine, OS thread and privileged trap handler preserve different sets of state. A **context switch** establishes another execution context, but it does not necessarily switch processes, change address spaces or move to a different CPU.

[Processes and Threads](processes-and-threads.md) owns OS execution entities. [Kernels](kernels.md) owns privilege mediation; this subject owns the state needed to suspend, restore, interrupt and safely continue execution.

## Registers, stacks and address spaces

A processor execution path uses some architectural registers and control state as defined by its ISA. A stack may hold call frames, return addresses or local execution information under a particular calling convention. OS management may also associate a context with mappings, permissions and resources.

An interrupt or syscall can require saving enough context to resume interrupted work after servicing an event. What must be saved depends on the ABI, hardware and conventions. **Not every register is necessarily saved by every transition.**

A thread switch inside the same process may preserve the address-space association, while a process switch often changes it. Some OS designs avoid a full address-space switch on particular paths, so no universal cost follows from the term.

## Running, ready and waiting are different conditions

A scheduler can select among runnable contexts, while blocked contexts wait for I/O, synchronization or other events. A context that is saved in memory is not automatically runnable: the conditions under which execution may resume matter.

A suspended thread may retain application state while another thread changes shared memory. Resuming the first thread need not recreate the state of the entire world at the time of suspension.

[Scheduling](scheduling.md) owns policy for selecting work; [Synchronization](../computation-algorithms/synchronization.md) owns ordering and visibility constraints.

## Worked example: accounting for switches

Suppose two tasks, A and B, require 3 ms and 4 ms of CPU execution respectively. A single processor runs A completely, performs exactly **one context switch taking 0.2 ms**, and then runs B completely. Assume no initial dispatch overhead, interruptions or additional waiting.

```text
A execution        = 3.0 ms
A→B context switch = 0.2 ms
B execution        = 4.0 ms
Total modeled time = 7.2 ms
```

The 0.2 ms is a **stipulated modeled cost**, not a measurement of a real OS. A different ordering, more preemptions, multiple CPUs, cache effects or other overhead can change the total. CPU work alone sums to 7.0 ms; the added 0.2 ms is switch overhead in this case.

## Interrupt contexts and reentrancy

An interrupt handler can execute in a special context that differs from ordinary user process execution. It may have limits on what operations can block, allocate or acquire locks under the OS model. A handler running at high privilege does not mean that ordinary application assumptions remain valid.

**Reentrancy** concerns whether a routine can safely be invoked again while a previous invocation is active under a specified environment. A function can be thread-safe for one use while not safe to call in interrupt context because of the different constraints.

A software signal or callback is not necessarily equivalent to a physical hardware interrupt. [System Calls](system-calls.md) owns deliberate protected service requests, distinct from asynchronous hardware events.

## Correctness and boundaries

Context preservation must respect calling conventions, permission boundaries and object lifetime. A saved instruction location and stack pointer may be insufficient if a shared resource was removed, an address mapping changed, or the computation's assumptions no longer hold.

[Runtime Environments](../software-programming/runtime-environments.md) owns language/runtime support, not OS context transitions. [Timing and Clocks](../digital-systems-hardware/timing-and-clocks.md) owns hardware timing implementation.

### Sources

- [MIT 6.1810: Thread switching](https://pdos.csail.mit.edu/6.S081/2026/homework/xv6-threads.html).
- [MIT 6.1810: Traps](https://pdos.csail.mit.edu/6.S081/2026/labs/traps.html).
- [Operating Systems: Three Easy Pieces](https://research.cs.wisc.edu/wind/OSTEP/).

**Editorial status:** Substantive Draft. Context, interrupt and switching-cost claims require separate scoped technical review. No platform mandate or learner assessment.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
