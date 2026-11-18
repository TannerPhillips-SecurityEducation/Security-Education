# Computer Architecture Models

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Subject ID:** F-06-10  
**Development status:** Draft; substantive article newly authored  
**Source review:** References listed; scoped technical review pending  
**Inventory authority:** [Model and Architecture Adjudication 01](../FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md)

## Computer architecture is an organization of responsibilities and interfaces

A **computer architecture model** describes how processing, storage, control, and communication responsibilities are organized and constrained, including the interfaces through which those elements interact. It is not automatically an implementation blueprint, a specific instruction-set architecture, or a single physical chip arrangement.

A computing system can be described at several levels: a programming abstraction; an instruction-set architecture (ISA); a microarchitecture with registers, data paths, caches and pipelines; a system-level memory and I/O organization; or a physical implementation. Different architectural views can represent the same computer. A diagram depicting CPU, memory and I/O is a useful structural abstraction, not evidence that any deployed system matches it.

[Computing Components](computing-components.md) owns individual component roles, [Processors and Instruction Sets](processors-and-instruction-sets.md) owns the ISA versus microarchitecture contract, and [Hardware Abstraction](hardware-abstraction.md) owns hiding machine details behind interfaces. This subject owns **comparative whole-computer architectural models**.

## Stored-program model and memory organization

A **stored-program computer** represents executable instructions in a machine-accessible memory and fetches instructions according to its execution semantics. In the familiar **von Neumann-style model**, a CPU, memory and I/O are connected under a shared memory arrangement in which instructions and data can be held in the same addressable storage. The concept is broader than one physical bus and does not mean every operation literally performs a sequential memory read.

A commonly contrasted **Harvard-style model** separates instruction and data address spaces or memory paths under a specified implementation. Separate paths can permit instruction and data traffic to proceed independently under relevant timing and arbitration rules. They do not automatically double application throughput, and a device may combine a Harvard-like first-level cache structure with a common lower-level memory or shared physical storage.

The terminology describes **models and engineering arrangements**, not exclusive immutable classes of modern computers. Real systems often combine multiple levels, address spaces and memory paths.

## Instruction set, microarchitecture and system architecture

An **ISA** specifies programmer-visible instructions, architectural registers, memory-addressing conventions, machine state and defined behaviors. **Microarchitecture** describes how an implementation realizes that ISA, potentially with pipelining, caching, out-of-order scheduling or other structures. **System architecture** encompasses relationships among processor complexes, memory systems, accelerators, I/O, buses and supporting control.

Two chips can execute the same ISA but exhibit very different performance, power consumption, latency, fault behavior and implementation-level side channels. An assembly instruction count is therefore not a universal measure of execution time or energy.

The separation also prevents confusion between **execution mechanism** and **architectural promise**. Speculative execution or a cache may be invisible to ordinary program semantics while still affecting timing and resource behavior.

## Memory hierarchy and locality

A **memory hierarchy** provides multiple storage levels with different capacities, costs, persistence and access times. Registers, caches, main memory and secondary storage differ in their access semantics and mechanisms; "higher" and "lower" are contextual labels, not universal numeric latencies.

**Temporal locality** means recently accessed data may be accessed again. **Spatial locality** means locations near an accessed address may soon be used. Caches can exploit such patterns but may perform poorly when access patterns are unpredictable or when synchronization causes coherence traffic.

Separate instruction and data caches do not necessarily imply entirely separate physical memory systems. Shared caches, translation structures, DMA, nonuniform memory access and coherence may influence observed behavior. [Memory and Storage](memory-and-storage.md) owns memory devices and caching mechanisms in greater detail.

## Flynn's architecture classification

**Flynn's taxonomy** classifies computational arrangements by the number of **instruction streams** and **data streams** in its model:

| Class | Instruction streams | Data streams | Interpretation under the model |
| --- | --- | --- | --- |
| SISD | Single | Single | One instruction stream operates on one data stream |
| SIMD | Single | Multiple | A common instruction operation is applied to multiple data elements |
| MISD | Multiple | Single | Multiple instruction streams applied to one data stream, a less common and interpretation-sensitive class |
| MIMD | Multiple | Multiple | Multiple instruction streams operate on multiple data streams |

A modern device can combine multiple forms: a multicore processor may have MIMD parallelism while individual cores execute SIMD vector instructions. Flynn's classification is an abstraction for discussing parallel organization, not a full performance benchmark or an assertion that one device fits a single class at all relevant scales.

[Concurrency and Parallelism](../computation-algorithms/concurrency-and-parallelism.md) owns the computational difference between overlapping and parallel work; this subject owns machine organization that may enable those behaviors.

## Pipelining and parallel structures

A **pipeline** divides work into stages that may operate on different items concurrently. After filling, a pipeline may improve the rate of completed work without reducing the latency of one item and sometimes increases it due to stage overhead. Hazards, stalls, branch effects and shared-resource contention can prevent ideal throughput.

**Superscalar**, vector, multicore, heterogeneous and accelerator organizations have different instruction, data and scheduling responsibilities. These are not synonyms for concurrency at the software level. A processor capable of issuing several instructions does not guarantee that an arbitrary program contains enough independent work to exploit that capacity.

## Worked example: shared versus separate transfer paths

Consider an idealized instruction/data fetch phase requiring **four instruction transfers** and **two data transfers**. Assume every transfer occupies exactly one slot, with no caches, stalls, prefetching or reuse.

```text
Shared single-transfer path:  4 + 2 = 6 occupied transfer slots
Two independent paths:       max(4,2) = 4 minimum time slots
```

The first model serializes all transfers. The second can schedule instruction transfers and data transfers concurrently, giving a lower bound of four slots on the combined transfer phase under the assumed identical per-path slot duration.

**This does not establish** that Harvard organization yields a 1.5× speedup for an actual program. The instruction execution pipeline, dependency ordering, memory access times, contention, caching and measured workload may dominate. Nor does it establish that a modern von Neumann-style stored-program computer has only one physical path. The model demonstrates a **possible structural bandwidth constraint**, not a universal benchmark.

## Architectural boundaries and dependencies

- [Digital Logic](digital-logic.md) owns gates and state elements; the architectural model does not replace Boolean circuit analysis.
- [Processors and Instruction Sets](processors-and-instruction-sets.md) owns ISA semantics and processor implementation distinctions.
- [Memory and Storage](memory-and-storage.md) owns memory technologies, hierarchy and storage properties.
- [Buses and Interfaces](buses-and-interfaces.md) owns specific interconnection semantics; [Input/Output](input-output.md) owns device interaction.
- [Operating System Principles](../operating-system-principles/README.md) covers process, memory and privilege abstractions implemented atop hardware.
- [Architecture and Composition](../systems-engineering/architecture-and-composition.md) owns general architectural views, composition and system boundaries.
- [Algorithms](../computation-algorithms/algorithms.md) owns computational procedures, not the physical organization of their implementations.

## Authoritative source starting points

- [MIT OpenCourseWare 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/), stored-program organization, instruction sets, pipelining and architecture.
- [MIT OCW 6.004: Designing an Instruction Set](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c9/), structural and implementation-level models.
- [UC Berkeley CS61C: Flynn's Taxonomy](https://notes.cs61c.org/content/parallel-dlp/), distinguishing SISD, SIMD, MISD and MIMD by instruction/data streams.
- [ACM/IEEE-CS/AAAI CS2023 Knowledge Areas](https://csed.acm.org/knowledge-areas/), *Architecture and Organization* as a computing knowledge domain; curricular grouping is not a mandatory hardware taxonomy.

Specific historical names and classification schemes are presented as useful models with assumptions, not a complete classification of all present and future computer designs.

**Editorial status:** Draft. Technical claims and toy calculations require a separate scoped acceptance audit.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
