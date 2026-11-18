# System Calls

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** System calls  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Operating System Principles 60-family audit](../WAVE-E-TECHNICAL-REVIEW-01.md); independent human review pending

## System calls expose controlled operating-system services

A **system call** is an interface through which an application or execution context requests an operating-system service across a defined protection or execution boundary. The service may involve files, memory mappings, processes, device operations, clocks or interprocess communication.

An application-level library call is not automatically a system call. A library function may execute entirely in user space, wrap one or several system calls, or cache results. The **application binary interface**, calling convention and kernel implementation are related but different.

[MIT 6.1810's traps material](https://pdos.csail.mit.edu/6.S081/2026/labs/traps.html) illustrates a protected system-call transition in a teaching OS. This reference owns general request/return and privilege-boundary semantics, not a prescribed POSIX or Windows interface.

## Arguments, transitions and results

A simplified request path can be expressed as:

```text
Application intent → API/library wrapper → controlled transition
                   → kernel dispatch/validation → service operation
                   → result/error → application interpretation
```

The actual path differs by operating system, processor architecture and operation. An entry mechanism must preserve or reconstruct enough execution state to return or transfer control safely. Checking that arguments are well-formed does not automatically prove the caller has authorization.

A return value may report a count, handle, error, completion status or other result according to the chosen syscall's contract. It must not be interpreted more strongly than defined.

## Worked example: short reads

Consider a hypothetical byte-reading interface modeled after common POSIX-style semantics:

```text
read(handle, buffer, requested_count)
```

The caller requests **100 bytes**. A successful call may return **40**, indicating that 40 bytes were actually read under the contract; it does **not** establish that all 100 requested bytes were supplied. If a later call returns zero, its meaning can depend on the object type and contract, such as end-of-file for a regular file.

The program must account for the actual returned count and avoid treating a short read as an automatic error or silently processing uninitialized portions of the buffer.

The example is a stipulated interface interpretation, not a statement that every I/O API has identical semantics. The [POSIX system-interface specification](https://pubs.opengroup.org/onlinepubs/9799919799/) documents one important standardized family.

## Protection, memory and caller context

A system call uses parameters interpreted in the caller's execution context, but kernel code must not assume those parameters designate valid, writable or safe memory. Depending on the OS model, address translation, permissions, copies or other checks mediate access to application buffers.

A caller may have permission to read one resource but not another. A valid file path or device identifier does not confer authority. [Memory Management](memory-management.md) owns virtual mapping/protection, and [Execution Contexts](execution-contexts.md) owns the state relevant to returning from privileged execution.

## Blocking, asynchronous operation and errors

Some syscalls can block while waiting for I/O, a lock, an event or available capacity. Others return quickly after initiating an operation. A successful submission may precede actual completion of a physical effect.

Interruptions, partial results, retry requirements and timeouts vary by operation. Retrying an operation can duplicate external effects when a previous attempt may have completed despite a lost response. [Error Handling](../software-programming/error-handling.md) owns software-level recovery decisions, while [Input/Output](../digital-systems-hardware/input-output.md) owns device exchange mechanics.

## Canonical boundaries

System calls are a privilege-mediated interface, not the entire kernel, a programming-language function system, or a network RPC. [Software Interfaces](../software-programming/software-interfaces.md) owns general software contracts; this article specializes them to OS services and protected entry/exit.

### Sources

- [MIT 6.1810: Traps and system calls](https://pdos.csail.mit.edu/6.S081/2026/labs/traps.html).
- [MIT 6.1810 Operating System Engineering](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [POSIX System Interfaces, The Open Group](https://pubs.opengroup.org/onlinepubs/9799919799/).

**Editorial status:** Reviewed (model-assisted) following the [Wave E OS 60-family technical audit](../WAVE-E-TECHNICAL-REVIEW-01.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
