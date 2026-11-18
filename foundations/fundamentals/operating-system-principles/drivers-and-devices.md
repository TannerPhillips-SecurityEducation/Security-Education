# Drivers and Devices

**Knowledge area:** [Operating System Principles](README.md)  
**Approved subject heading:** Drivers and devices  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave E Operating System Principles 60-family audit](../WAVE-E-TECHNICAL-REVIEW-01.md); independent human review pending

## Drivers mediate operating-system requests and device behavior

A **device driver** is a software component that translates or mediates operating-system requests into device-specific operations and interprets resulting status under a defined hardware and software contract. **A device** is a physical or emulated component exposing capabilities through an interface. A driver is not necessarily inside a privileged kernel, and not every device uses the same command model.

A driver can manage configuration, data transfer, synchronization, interruptions and error recovery. Its presence does not establish that the hardware is functional or that a requested physical action completed.

[Input/Output](../digital-systems-hardware/input-output.md) owns hardware exchange mechanisms. [Buses and Interfaces](../digital-systems-hardware/buses-and-interfaces.md) owns interconnect transactions. This article owns **OS-level mediation, device state, driver lifecycle and the observable software-device contract**.

## Logical operations versus physical behavior

A generic `read` or `write` operation may map to memory-mapped registers, serialized commands, DMA descriptors or other device-specific transactions. Drivers often present a common interface while respecting different device capabilities and error conditions.

A driver can report success when a command was queued, when a device acknowledged it, or when some physical result was confirmed, depending on the contract. These statuses must not be conflated. In a sensor system, validly encoded data can still represent an inaccurate physical measurement.

[Software Interfaces](../software-programming/software-interfaces.md) owns operation contracts, while [Sensors and Actuators](../physical-electrical-principles/sensors-and-actuators.md) owns physical observation and actuation.

## Device lifecycle and interrupts

A device may be detected, initialized, configured, active, suspended, unavailable or removed, subject to its platform design. Drivers must cope with relevant transitions, including state reset, unplugging, failed initialization or changes in capability.

An **interrupt** can notify the CPU or interrupt controller of a device condition. **Polling** checks state at selected times. **DMA** can transfer data without the CPU copying each item individually, but still requires safe setup, memory visibility and completion handling.

The [MIT 6.1810 device-driver lecture schedule](https://pdos.csail.mit.edu/6.S081/2026/schedule.html) covers drivers and their relationship to interrupts. A successful interrupt handler does not itself prove that data reached the intended application.

## Worked example: queued work versus completed work

A hypothetical storage device accepts three requests labeled A, B and C. The driver receives acknowledgments that all three requests entered the device queue. Later, the device reports A and C complete but B failed.

The correct count of **accepted requests** is three. The correct count of **reported completed requests** is two. It would be incorrect to report a 100% completion rate from the acceptance acknowledgments alone.

Under this toy case, the reported completion fraction is `2/3≈66.7%`, while acceptance is `3/3=100%`. These are counts under invented status rules, **not** actual device reliability estimates.

## Resource ownership and safety

Device interactions can use shared queues, buffers, interrupts and power resources. Driver implementations need relevant locking, ordering, lifetime and cancellation rules. A driver might isolate a device from other processes through OS controls, but protection depends on mapping, permissions and hardware enforcement.

A failed driver can affect other components when they share the kernel, bus or execution context. Moving a driver to a separate process can alter fault containment without automatically guaranteeing safe behavior.

[Resource Management](resource-management.md) owns competing allocations, [Synchronization](../computation-algorithms/synchronization.md) owns coordinating concurrent state, and [Reliability and Failure](../systems-engineering/reliability-and-failure.md) owns general failure models.

## Canonical boundaries

This reference does not prescribe a device-driver API, operating system, USB/PCI architecture, programming language, hardware assembly procedure or certification. Firmware is a separate hardware-facing executable layer covered in [Firmware](../digital-systems-hardware/firmware.md).

### Sources

- [MIT 6.1810 Operating System Engineering: devices and drivers](https://pdos.csail.mit.edu/6.S081/2026/schedule.html).
- [Operating Systems: Three Easy Pieces, I/O Devices](https://research.cs.wisc.edu/wind/OSTEP/).
- [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/).

**Editorial status:** Reviewed (model-assisted) following the [Wave E OS 60-family technical audit](../WAVE-E-TECHNICAL-REVIEW-01.md). Complete source-level verification, independently performed expert review and final publication acceptance remain outstanding.

[Operating System Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
