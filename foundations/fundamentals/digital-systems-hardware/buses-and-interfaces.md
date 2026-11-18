# Buses and Interfaces

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Buses and interfaces  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Interconnects coordinate exchanges among hardware components

A **hardware interconnect** provides physical and logical means for hardware elements to exchange information, control, timing and sometimes power. A **bus** commonly denotes a shared communication structure connecting multiple components, while point-to-point links and switched fabrics are different interconnect arrangements.

An **interface** defines how participants present, interpret and coordinate exchanges. Its physical connectors and signal levels are only part of the contract; addresses, transactions, ordering, timing, reset, errors and ownership can matter.

[Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns general interface contracts. This article owns the **hardware-level implementation concerns**, not the definition of all system interactions.

## Address, data, control, and protocol

A simplified memory-mapped hardware transaction can distinguish:

- **Address:** selects a target register, location or address range under a defined map.
- **Data:** the information being transferred.
- **Control:** operation type and conditions such as read/write, permission or transaction attributes.
- **Handshake or acknowledgment:** signals the status of acceptance or completion under a protocol.
- **Timing:** specifies when participants sample or produce values.

These are conceptual roles rather than a guarantee of separate physical wires. Some buses multiplex address and data; serial links encode many roles into a packet or framing convention.

A receiver acknowledging a request is not necessarily the same as completing a durable write or changing a physical actuator. Protocol definitions determine the permitted inference from each acknowledgment.

## Shared communication and arbitration

When multiple requesters share a constrained interconnect, an **arbitration mechanism** selects who may use the resource under defined rules. Contention can add delay, affect fairness and bound available throughput.

A high-priority requester can be favored while another waits. Whether such behavior is acceptable depends on performance and system requirements. A bus operating correctly according to an arbitration rule may still be unsuitable for an application needing strict response deadlines.

Shared buses, point-to-point links and fabrics involve different scalability, routing, resource and failure tradeoffs. This reference does not prescribe one architecture.

## Worked example: an ideal transfer-rate ceiling

Suppose a hypothetical bus transfers a 32-bit data word during **one accepted transfer every clock cycle** at an exactly 100 MHz clock rate. Assume no wait states, control overhead, idle cycles, arbitration delays or error retransmissions.

```text
Transferred data per accepted cycle = 32 bits = 4 bytes
Accepted cycles per second          = 100,000,000
Ideal data transfer rate            = 400,000,000 bytes/s
                                    = 400 MB/s (decimal)
```

This is the **theoretical payload ceiling under the stated bus model**, not a performance claim about an actual device. If only half the cycles carry accepted words, the rate becomes 200 MB/s under the same simplifying assumptions.

Clock rate alone is not transfer rate: a protocol may require several cycles per transaction, support multiple transfers per cycle, or use multiple independent lanes.

## Order, widths, and representation

The **data width** of an interconnect and the width of a device register or ISA word need not be identical. A 64-bit value can require multiple transfers on a narrower bus, or a protocol can split a wider bus into independent logical lanes.

**Byte order** specifies ordering of multi-byte values under a chosen representation; it is not necessarily the ordering of serialized bits on a physical link. [Bits and Bytes](../information-data/bits-and-bytes.md) owns the general representation-unit mechanics.

Memory-mapped interfaces assign address ranges to registers or device functions. That does not prove the addressed resource behaves like ordinary RAM, is cacheable, or permits arbitrary unaligned reads and writes. Register semantics and side effects must be declared.

## Timing domains, electrical compatibility, and errors

Two participants may use different clocks or lack a shared clock. Their interface must manage sampling and coordination appropriately. **Clock-domain crossings** can introduce metastability and synchronization requirements, while physical connections add signal-integrity, voltage, impedance and timing constraints.

A digital packet being structurally valid does not certify delivery, integrity or authorization. Error-detection mechanisms can reject some corrupt transfers; what they detect or recover depends on the declared protocol and error model.

[Timing and Clocks](timing-and-clocks.md) owns hardware timing relationships. [Input/Output](input-output.md) owns device interaction and transfers. [Electrical Circuits](../physical-electrical-principles/electrical-circuits.md) owns the underlying electrical network behavior.

## Canonical boundaries

This article does not designate a required bus, connector, protocol version, transaction encoding, arbitration discipline or vendor platform. Domain-specific designs may extend these general principles. An electrical connection, logical address map and software API are distinct layers of interaction.

### Sources

- [MIT OpenCourseWare 6.004: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [MIT 6.004: Devices and Interrupts](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c18/c18s1/).
- [MIT OpenCourseWare 6.004: Devices and Interrupts (course materials)](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/).
- [NASA: Interface Management](https://www.nasa.gov/reference/6-3-interface-management/).

**Editorial status:** Substantive Draft. The bus bandwidth calculation and hardware-interface generalizations await scoped technical review. No hardware assembly or learner assessment is prescribed.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
