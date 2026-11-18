# Processors and Instruction Sets

**Knowledge area:** [Digital Systems & Hardware](README.md)  
**Approved subject heading:** Processors and instruction sets  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source review pending

## Instruction sets define programmer-visible machine behavior

An **instruction-set architecture (ISA)** defines a machine-level interface for executing instructions: relevant operations, architectural registers, operand representations, addressing conventions, state updates, and control-flow semantics. A **processor microarchitecture** is an implementation of those architectural behaviors using concrete datapaths, control mechanisms, memories, timing and physical hardware.

The two are not synonyms. Different processor implementations can support the same ISA while differing in pipelines, cache organizations, execution order, power use and performance. Conversely, a hardware implementation may support more than one execution mode or software-visible interface.

The [MIT Computation Structures course](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) develops instructional examples of machine architecture, the stored-program model, datapaths and processor design. Its teaching instruction set and word widths are examples, not the universal structure of all processors.

## Architectural state and implementation state

**Architectural state** consists of values whose behavior is defined by the machine-level contract, such as selected general-purpose registers, a program counter and defined status values. **Microarchitectural state** can include pipeline buffers, speculative execution structures, cache state and internal scheduling information that need not be directly visible through ordinary ISA instructions.

A program's correct architectural result does not require that the hardware execute its instruction effects in the simplest textbook sequence. A processor can fetch, decode, execute and retire or commit instructions using overlapping stages if externally visible behavior follows the relevant contract.

A separate concept is **privilege**: some processor instructions or state changes may be restricted to certain execution modes. The boundaries of privilege depend on the ISA and operating environment, not solely on the physical circuitry.

## Instructions and operands

An ISA can specify operations such as arithmetic, logic, comparison, memory load/store, branch, control transfer and system-related operations. Which are provided, and how operands are encoded, varies among ISAs.

An instruction might obtain operands from registers, an immediate constant, or memory under defined addressing rules. A load reads an accessible value from a specified memory location into architectural state; a store makes a specified value available at a chosen memory location according to the architecture's memory and ordering semantics.

The distinction between **operation semantics** and **instruction encoding** matters: two different bit patterns can sometimes express related operations, and the same pattern can mean different operations under different ISA definitions.

[Bits and Bytes](../information-data/bits-and-bytes.md) owns raw binary representation; [Data Types](../information-data/data-types.md) owns value interpretation. [Computing Components](computing-components.md) owns the system hardware roles, not every ISA rule.

## Worked example: arithmetic under a declared eight-bit ISA

Consider a toy processor with an eight-bit unsigned general-purpose register, a hypothetical ADD operation, and **modulo-256 arithmetic** with wraparound. Let the register initially hold `250`, and execute `ADD register, 10`.

```text
Mathematical sum: 250 + 10 = 260
Modulo-256 result: 260 mod 256 = 4
Register after ADD: 4
```

The final architectural register value is **4** under the stipulated rule. If the same mathematical operation instead used an ISA's saturating arithmetic rule, the result might be `255`. If the ISA signaled an exception or retained a wider result, other behavior could follow. None of these alternatives is determined solely by the phrase *eight-bit processor*.

This example is a deliberately simple architectural contract, not a claim about a named real CPU or an observed register value. The possibility of overflow underscores the importance of operand interpretation, result width and status behavior.

## Addressing and instruction memory

A stored-program system makes instructions available in a representation accessible to a processor. A **program counter** or equivalent architectural mechanism identifies the next instruction according to defined control-flow rules. Branches may change which instruction is selected next; exceptions, interrupts and privilege transfers may alter control flow in other ways.

The number of address bits does not by itself establish physical memory capacity or imply that every address is valid. Byte-addressed and word-addressed architectures can use the same address width while referring to different sized units.

[Memory and Storage](README.md) and [Buses and Interfaces](README.md) remain separate approved headings for physical memory and interconnect mechanisms. Their not-yet-authored status does not make the ISA the canonical owner of those physical details.

## Performance and execution are different quantities

Processor **clock frequency** specifies a clock or timing rate in a relevant design. **Instruction throughput** concerns architectural instructions completed per unit time under a given workload. **Latency** concerns the elapsed duration of an operation under stated measurement boundaries.

These quantities are not inherently proportional. A processor can complete more than one instruction per cycle in some designs, stall for multiple cycles in others, or execute operations without one synchronous system-wide clock. Cache misses, branch behavior, dependency chains and power limits affect performance.

A correct ISA description can coexist with vastly different microarchitectural performance. Timing, energy consumption and heat removal are properties of implementation and environment, not automatically of an ISA instruction's abstract mathematical effect.

## ISA, operating systems and software contracts

The ISA is one boundary between machine-level software and hardware. An **application binary interface (ABI)** may add conventions for calling functions, register usage and binary layout, while an operating system defines services, process models and access policies. A compatible ISA does not automatically imply compatible ABIs, operating-system environments or applications.

[Hardware Abstraction](README.md) will develop the specialized mechanisms hiding hardware details. [System Calls](../operating-system-principles/README.md) belongs to the separately approved operating-system area, not to all processors universally.

## Canonical boundaries and references

[Digital Logic](digital-logic.md) owns gates and sequential functions; [State and Behavior](../systems-engineering/state-and-behavior.md) owns whole-system behavioral modeling. The processor article owns architecture-visible instruction behavior and its relation to implementation.

No specific ISA, chip vendor, assembler, emulator, assessment, or new knowledge category is mandated.

### Sources

- [MIT OCW 6.004: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [MIT OCW 6.004: Designing an Instruction Set](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c9/c9s1/).
- [MIT OCW 6.004: Caches and the Memory Hierarchy](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c14/c14s1/).
- [NIST: Binary Prefixes](https://physics.nist.gov/cuu/Units/binary.html).

**Editorial status:** Substantive Draft. The unsigned-register example, ISA and microarchitecture claims require a separately documented scoped technical/source review. No platform adoption or learner assessment introduced.

[Digital Systems & Hardware](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
