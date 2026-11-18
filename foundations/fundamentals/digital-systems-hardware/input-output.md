# Input/Output

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Input/output  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## I/O connects computing state with devices and environments

**Input/output (I/O)** concerns the movement of information and control between a computing system and devices, external processes, other computing elements or people. An input device can report events or measurements; an output device can display information, transmit messages or drive an actuator. The same device may support both directions.

I/O is not limited to keyboards and displays. Storage controllers, network interfaces, sensors, serial ports and device control registers also participate. Their behavior depends on device-specific semantics, electrical interfaces, timing, software coordination and error conditions.

[Computing Components](computing-components.md) owns the overall hardware roles. [Buses and Interfaces](buses-and-interfaces.md) owns the interconnect contract. This article owns **how computing elements exchange data and coordinate operations with devices**.

## Registers, buffers, and transactions

A device interface may expose **status registers**, **control registers**, and **data registers or buffers**. An instruction or controller operation can read or write those locations under a defined device protocol. Some reads have side effects, such as clearing a status flag; some writes initiate a command rather than instantly completing it.

**Memory-mapped I/O** associates selected addresses with device registers or functions. A load instruction targeting such an address may cause a device transaction instead of reading ordinary memory. **Port-mapped I/O** uses a different machine-level addressing convention. Which approach is available depends on the ISA and platform.

An addressable device register is not interchangeable with normal RAM. Access width, alignment, caching, ordering, permission and side-effect rules can differ.

## Polling, interrupts, and direct memory access

**Polling** checks device state at selected times to determine whether action is needed. **Interrupts** signal a processor or controller that a condition requires attention under a defined priority and delivery model. **Direct memory access (DMA)** lets an eligible device or controller transfer data between appropriate addressable resources without the CPU individually copying every data unit.

These mechanisms can be combined. A processor might configure a DMA engine, receive an interrupt on completion and poll for errors. DMA is not a promise of zero CPU involvement, zero overhead or automatically correct memory coherence.

The [MIT Computation Structures course](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/) includes devices and interrupts in its hardware/software interface coverage. [Operating System Principles](../operating-system-principles/README.md) owns scheduling, protection and software-driver responsibilities.

## Worked example: interrupt processing budget

Suppose a hypothetical processor receives **500 device interrupts per second**, and handling each one consumes exactly **20 microseconds of processor execution time**. Ignore nested interrupts, cache effects, concurrency, scheduling and all additional device work.

```text
CPU execution time per second = 500 × 20 μs = 10,000 μs
                              = 10 ms per second
Fraction of one CPU-second    = 10 / 1000 = 0.01 = 1%
```

Under these assumptions, interrupt handling alone consumes **1% of one processor's available execution time** over the measured second. This is not a utilization measurement for a real operating system. Higher rates, different handlers, scheduling interference or missed interrupts can produce different behavior.

The calculation does not establish the end-to-end time from a physical event to the corresponding application action. That requires separate timing boundaries and a measured or justified latency model.

## Buffering, flow control and data loss

A buffer temporarily retains information when producers and consumers operate at different rates. It has finite capacity, unless the model explicitly allows unlimited growth. When a producer outpaces a consumer for long enough, the system may drop, delay, overwrite, throttle or redirect data according to its policy.

**Flow control** seeks to coordinate production and consumption under a contract. A device reporting that a buffer accepted a data item does not necessarily mean the item was processed, durably saved or acted upon.

The correct semantics of message ordering, duplicate delivery, acknowledgment and retry belong to the specific device and protocol, with specialized treatment in [Communication & Distributed Systems](../communication-distributed-systems/README.md).

## Physical and logical state boundaries

I/O can carry a validly encoded but inaccurate sensor measurement. Conversely, an output command can be acknowledged while the physical plant does not respond. These differences require distinguishing device status, physical state and observed evidence.

[Sensors and Actuators](../physical-electrical-principles/sensors-and-actuators.md) owns physical transduction. [State and Behavior](../systems-engineering/state-and-behavior.md) owns whole-system state modeling. [Human-Computer Interaction](../human-sociotechnical-systems/human-computer-interaction.md) owns the people's interpretation of resulting feedback.

I/O operations may expose errors, timeouts, invalid data, unavailable devices or permissions. A sound interface documents recoverable and unrecoverable conditions rather than implying that a successful API call guarantees real-world success.

## Architectural boundaries

The detailed software driver, operating system kernel and application interface belong to specialized software and operating-system subjects. This article does not mandate a device protocol, DMA design, interrupt controller, input modality, or training assessment.

### Sources

- [MIT 6.004 Computation Structures: Course Outline (Devices and Interrupts)](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/).
- [MIT 6.004: Devices and Interrupts, Annotated Slides](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c18/c18s1/).
- [MIT 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [NASA: Interface Management](https://www.nasa.gov/reference/6-3-interface-management/).

**Editorial status:** Substantive Draft. The interrupt-budget example and device semantics require a separate scoped claim-to-source and numerical audit. No live hardware testing, operational security activity or assessment is introduced.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
