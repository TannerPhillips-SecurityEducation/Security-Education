# Kernels

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Kernels  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Operating System Principles 60-family audit](../WAVE-E-TECHNICAL-REVIEW-01.md); independent human review pending

## A kernel coordinates protected operating-system mechanisms

An **operating-system kernel** is a core software component that manages selected resources, execution, protection boundaries, and hardware interaction under an operating-system design. Its responsibilities vary: a monolithic kernel may implement broad services within privileged space, while a microkernel may keep a smaller privileged core and delegate additional services to other processes.

A **privilege level** constrains which hardware operations a running execution context can perform. Merely calling a function `kernel` does not grant hardware privilege, and privileged execution does not establish correctness. The operating system also includes components outside the kernel, such as system services, utilities and management software.

The [MIT 6.1810 Operating System Engineering course](https://pdos.csail.mit.edu/6.S081/2026/schedule.html) treats traps, kernel design, memory protection, file systems, interrupts and scheduling as related but distinct mechanisms. [Systems and Subsystems](../systems-engineering/systems-and-subsystems.md) owns general system boundaries; this subject owns their operating-system kernel realization.

## Privilege boundaries and mediation

A typical protected system distinguishes less-privileged application execution from a privileged context allowed to manage page tables, device control or selected global resources. A **trap** or similar controlled transition can transfer execution to an authorized handler, preserving enough state to resume or report an outcome.

Kernel-mediated interfaces enable policy enforcement, but a request crossing a boundary does not mean it is authorized. The handler must interpret the request, validate relevant inputs and select permitted effects under the OS model.

A separate **hypervisor** may manage virtualization at another privilege boundary; that does not make all kernels hypervisors. [System Calls](system-calls.md) owns application-to-kernel request semantics and [Hardware Abstraction](../digital-systems-hardware/hardware-abstraction.md) owns the lower-level interface boundary.

## Architecture choices and responsibility allocation

A kernel can use different internal arrangements:

| Design concern | Illustrative alternative | Important limit |
| --- | --- | --- |
| Service location | More services privileged versus more user-space services | Not a proof of security or reliability by itself |
| Resource policy | Centralized allocator versus delegated control | Resource ownership must still be defined |
| Device mediation | Kernel drivers versus service-mediated drivers | Fault isolation depends on actual boundary and implementation |
| Scheduling | Kernel-selected runnable work versus cooperative arrangements | Fairness, latency and progress need separate definitions |

These are architectural tradeoffs, **not** four newly approved types of kernel. A particular design can mix approaches.

## Worked example: privileged request versus physical effect

Imagine an application asks an OS to send 100 bytes to a device. The request crosses a defined privileged boundary and is accepted, and the kernel copies 100 bytes into a device queue. This establishes **queue acceptance** in the model, not necessarily physical transmission, remote delivery or durable storage.

If a caller lacks required access permissions, the kernel can reject the request even though the bytes and target address were structurally valid. A privilege transition enables controlled execution; it is not evidence that the operation must succeed.

The number 100 is an invented illustrative input. Actual transfer results depend on the contract, buffer capacity, device status and conditions.

## Concurrency, failures and evidence

Kernels often mediate simultaneous or interleaved activity. Their internal state may require locking, atomic operations, ordering guarantees and interrupt coordination. A bug in privileged code can have effects beyond the initiating application; nevertheless, consequences depend on OS architecture and protection mechanisms.

A kernel may support recovery or restart for some failures but not others. Observing a successful syscall return verifies only the result guaranteed by that syscall under its specified contract. [Reliability and Failure](../systems-engineering/reliability-and-failure.md) owns the general failure model, while [Synchronization](../computation-algorithms/synchronization.md) owns general concurrent coordination.

## Canonical boundaries

The kernel is not synonymous with an operating system, an ISA, a bootloader, a file system or a process. [System Initialization](system-initialization.md) owns boot and startup transitions; [Resource Management](resource-management.md) owns OS allocation and limits; [Drivers and Devices](drivers-and-devices.md) owns device-facing mediation.

### Sources

- [MIT 6.1810 Operating System Engineering, Fall 2026](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [MIT 6.1810 OS overview](https://pdos.csail.mit.edu/6.S081/2026/overview.html).
- [Operating Systems: Three Easy Pieces, official chapter index](https://research.cs.wisc.edu/wind/OSTEP/).

**Editorial status:** Reviewed (model-assisted) following the [Wave E OS 60-family technical audit](../WAVE-E-TECHNICAL-REVIEW-01.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
