# Computing Components

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Computing components  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave C Batch 01 technical audit](../WAVE-C-TECHNICAL-REVIEW-01.md); independent human review pending

## Digital systems combine specialized hardware responsibilities

A **computing component** is a physical or hardware-described constituent of a computing system that contributes processing, storage, communication, input/output, control or support capabilities. The identity of a component depends on the system boundary and architectural view. A chip may be one component in a board and a collection of many interacting subcomponents when studied internally.

A computing system is not simply a CPU. Instructions, state, memory, interconnects, peripherals, clocks and power delivery interact to realize observable behavior. The [MIT OpenCourseWare Computation Structures course](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) develops shared digital-architecture concepts from gates to instruction sets and memory systems.

[Systems and Subsystems](../systems-engineering/systems-and-subsystems.md) owns whole-system analysis; [Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns generic constituent and contract concepts. This reference owns their **computing-hardware manifestations**.

## A model of hardware roles

A simplified stored-program design might contain:

```text
           +-----------------------+
           | Processor / Control   |
           | Registers + datapath  |
           +------------+----------+
                        |
                    Interconnect
             +----------+-----------+
             |                      |
          Memory               Input/Output
             |                      |
       Program + data        External devices
```

These boxes express roles rather than requirements that they be separate chips or use one universal bus. A microcontroller may integrate processor, memory and peripherals on one die. A distributed device may place components on several boards or machines. A GPU or other accelerator may perform substantial processing without conforming to the simplest CPU-centered picture.

[MIT OCW's stored-program and processor architecture material](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c9/c9s1/) illustrates a specific teaching computer. Its bit widths, registers and instruction sequences are examples of a design, not universal values for all computers.

## Processor, datapath and control

A **processor** executes instructions under a defined instruction-set architecture and hardware implementation. A **datapath** includes elements that move and transform values such as registers, arithmetic/logic units and internal routes; **control** coordinates operations according to instruction and state semantics.

A common instructional account uses *fetch*, *decode*, *execute* and *commit or write-back*. This is a **logical decomposition of instruction effects**, not proof that every modern processor executes every instruction in that exact sequence or within one clock cycle. Pipelines, speculative execution, asynchronous operations and specialized processors can overlap or reorganize work.

[Processors and Instruction Sets](README.md) will own the detailed ISA-versus-microarchitecture distinction, including instruction encoding, register models and execution semantics. [Digital Logic](digital-logic.md) owns gates and sequential switching mechanisms.

## Memory, storage and data persistence

**Registers**, caches, main memory and persistent storage support different locality, capacity, speed, endurance and persistence characteristics. A simple hierarchy often places small processor-near storage ahead of larger slower resources, but the exact arrangement is design-specific.

**Volatile** storage generally loses its retained contents when the required power conditions are absent; **nonvolatile** storage can retain information without continuous power under specified conditions. Neither designation by itself guarantees permanent retention, zero faults, security or unrestricted rewrite endurance.

The approved [Memory and Storage](README.md) subject will develop its canonical mechanics. [Bits and Bytes](../information-data/bits-and-bytes.md) owns the binary units and [Data Types](../information-data/data-types.md) owns interpretation, not memory-device physics.

## Interconnects and input/output

An **interconnect** enables exchange among system elements. It can carry addresses, data, control signals and power depending on the design. A **bus** is one common shared interconnection arrangement, but not every system communication path is a bus.

**Input/output (I/O)** provides paths between computing elements and external devices or contexts. Interfaces may be memory-mapped, port-mapped or organized under other architectural rules. Such mechanisms have ordering, timing, encoding and fault behavior that must be specified.

[Buses and Interfaces](README.md) and [Input/Output](README.md) are separate approved subjects reserved for detailed ownership. A physical connector's shape does not alone define the semantics of a digital message.

## Worked example: addressable capacity is not installed memory

Suppose an idealized machine has `16` address bits and a *byte-addressed* address space with all `2^16` address values defined:

```text
Address combinations = 2^16 = 65,536
Addressed byte locations = 65,536 bytes = 64 KiB
```

That is a calculation about the **specified address space**, not a claim that the machine necessarily contains 64 KiB of installed physical memory. Some addresses may map to I/O, be reserved, be unmapped, or be translated to other locations.

If instead the same bit-width addresses indexed 16-bit words, the corresponding total representable byte span under a dense two-byte-word model would be `2×65,536 = 131,072 bytes = 128 KiB`. Address width alone does not determine unit of addressability.

The result also does not establish that all combinations are usable, that reads are equally fast, or that software can access the whole space.

## Performance and physical constraints

Processor frequency, instruction throughput, memory latency, bus bandwidth, data locality, power delivery and cooling interact. More clock cycles per second do not automatically guarantee proportionally greater task performance. A workload stalled on memory access or I/O may not benefit substantially from higher core frequency.

Hardware consumes energy, dissipates heat and is limited by electrical and physical constraints. [Matter and Energy](../physical-electrical-principles/matter-and-energy.md), [Electricity](../physical-electrical-principles/electricity.md), and [Electrical Circuits](../physical-electrical-principles/electrical-circuits.md) own the foundational physical mechanisms. This article joins them to hardware organization without redefining their governing physics.

## Canonical boundaries

[Timing and Clocks](README.md) will own cycles, clock domains and hardware timing, while general temporality G-04 remains an open architectural decision. [Hardware Abstraction](README.md) will own machine-facing abstraction layers. Specialized processors, storage architectures and peripheral implementations remain extensions rather than new Fundamentals categories.

No mandated processor architecture, vendor product, bus standard, assessment or additional subject heading is introduced.

### References

- [MIT OpenCourseWare: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [MIT OCW: Stored-Program/Processor Architecture](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c9/c9s1/).
- [NIST: Binary Prefixes](https://physics.nist.gov/cuu/Units/binary.html).
- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave C Batch 01 24-group audit](../WAVE-C-TECHNICAL-REVIEW-01.md). Complete source verification, independent human expert peer review and final publication acceptance remain outstanding.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
