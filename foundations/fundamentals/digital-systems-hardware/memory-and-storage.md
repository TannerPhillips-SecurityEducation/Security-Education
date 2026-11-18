# Memory and Storage

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Memory and storage  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Physical resources retain and retrieve represented state

**Computer memory** comprises physical arrangements that retain state available for subsequent reading or computation under defined conditions. **Storage** can refer broadly to retaining information or more narrowly to resources supporting longer-term persistence. These terms overlap; they are not a guarantee of one universal hierarchy or a fixed lifetime for recorded data.

Registers, caches, main memory, nonvolatile semiconductor storage and magnetic media differ in capacity, access latency, bandwidth, energy use, retention, cost and failure characteristics. A **memory hierarchy** organizes multiple technologies to serve different access patterns.

The [MIT 6.004 Caches and the Memory Hierarchy](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c14/c14s1/) lesson develops these tradeoffs. [Computing Components](computing-components.md) owns the broader processor/memory/I/O organization, while this article owns physical storage mechanisms, hierarchy behavior and access tradeoffs.

## Memory locations, addressability, and capacity

A hardware memory resource provides some number of **addressable locations**, each with a defined unit of access or storage. Address width, addressable unit, memory mapping and installed physical media are distinct.

A device may use byte addressing, word addressing or another scheme. A processor with a 16-bit address can express `2^16` address combinations, but those combinations are not evidence that 64 KiB of physical memory exists or that every address is writable. Some ranges may map to devices, be invalid, or require translation.

[Processors and Instruction Sets](processors-and-instruction-sets.md) owns the ISA-visible addressing model. [Bits and Bytes](../information-data/bits-and-bytes.md) owns binary units and positional representation.

## Volatility, retention, and endurance

**Volatile memory** generally requires specified power conditions to retain state. **Nonvolatile storage** can retain recorded state without continuous electrical power under its rated conditions. Neither label guarantees immunity to bit errors, physical damage, aging, finite endurance or unauthorized modification.

RAM may use different circuit mechanisms. A simplified **SRAM** cell uses a retained switching state, while **DRAM** represents information partly through capacitor charge and requires refresh under its operating model. Flash memory and magnetic media use different nonvolatile mechanisms.

Real durability also depends on controllers, error management, wear, environmental conditions, power behavior and data-management policy. A written value acknowledged by one interface may not yet be present in the intended durable medium.

## Caches and locality

A **cache** stores selected copies of information closer to a requester to reduce typical access delay. A **cache hit** retrieves an item from the cache; a **miss** requires some further operation, possibly involving another level. **Locality** describes observed tendencies of accesses to reuse recently accessed or nearby locations, subject to workload.

Typical cache design choices include line/block size, capacity, associativity, replacement policy and write behavior. These have different tradeoffs and do not ensure that every workload benefits.

**Coherence** concerns whether multiple copies of shared data satisfy a chosen consistency contract. **Persistence** concerns surviving specified failures or loss of power. A coherent cache hierarchy does not automatically provide durable storage.

## Worked example: average memory access time

Consider an idealized one-level cache that always takes 4 ns for the initial lookup, has a hit rate of 90% under a defined workload, and adds exactly 40 ns for a miss. Ignore queueing, overlap, multiple outstanding requests and other delays.

```text
Average access time = hit time + miss rate × miss penalty
                    = 4 ns + (0.10 × 40 ns)
                    = 8 ns
```

A hit takes 4 ns and a miss takes 44 ns under these assumptions. The weighted average `0.9×4 + 0.1×44 = 8 ns` agrees with the formula.

This result does **not** prove that a particular real processor or cache will exhibit 90% hits. A change in program locality, conflicts or memory configuration can alter the values. A hit ratio is measured over a defined set of accesses.

## Storage versus data meaning

Physical memory stores representations, not intrinsic semantic truths. A byte pattern may represent an integer, instruction, text or image depending on the format and consuming system.

Files, databases, retention rules and provenance belong to the approved [Information & Data](../information-data/README.md) area. Virtual memory, paging, file systems and protection policies belong to [Operating System Principles](../operating-system-principles/README.md); this article supplies the underlying physical storage mechanisms.

An operating system can offer a virtual address space larger than installed RAM or use storage to back pages. The existence of a logical address range is not the same as physical storage availability.

## Failure and performance boundaries

Latency is not bandwidth: a resource can have a low delay for one access yet limited aggregate transfer capacity. Retention is not correctness: stored bits can faithfully preserve a false observation. Capacity is not accessibility: reserved, protected or unmapped portions may be unavailable to a requester.

[Hardware Abstraction](hardware-abstraction.md) owns standardized, implementation-independent resource interfaces. [Buses and Interfaces](buses-and-interfaces.md) owns interconnect mechanisms. The choice of memory technology remains system-specific; no universal cache size or vendor architecture is mandated.

### Sources

- [MIT OpenCourseWare 6.004: Caches and the Memory Hierarchy](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c14/c14s1/).
- [MIT OpenCourseWare 6.004: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [NIST: Binary Prefixes](https://physics.nist.gov/cuu/Units/binary.html).

**Editorial status:** Substantive Draft. The cache equation and memory-technology generalizations require a separate scoped claim-to-source and numerical audit. No mandatory hardware design or assessment is introduced.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
