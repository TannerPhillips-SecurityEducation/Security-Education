# Digital Systems & Hardware

**Division:** [Fundamentals](../README.md)  
**Architecture status:** Approved subject area  
**Content status:** All 9 approved subjects authored; 3 Reviewed (model-assisted), 6 Draft; independent human review and final publication acceptance pending  
**Governing architecture:** [Fundamentals Knowledge Architecture](../ARCHITECTURE.md)

## Scope

Components and mechanisms by which physical hardware represents information and executes digital operations.

## Approved Subject Inventory

- Digital logic
- Computing components
- Processors and instruction sets
- Memory and storage
- Buses and interfaces
- Input/output
- Timing and clocks
- Firmware
- Hardware abstraction

## Canonical reference articles

| Approved subject | Canonical reference | Development state |
| --- | --- | --- |
| Digital logic | [Digital Logic](digital-logic.md) | Reviewed (model-assisted) |
| Computing components | [Computing Components](computing-components.md) | Reviewed (model-assisted) |
| Processors and instruction sets | [Processors And Instruction Sets](processors-and-instruction-sets.md) | Reviewed (model-assisted) |
| Memory and storage | [Memory And Storage](memory-and-storage.md) | Draft |
| Buses and interfaces | [Buses And Interfaces](buses-and-interfaces.md) | Draft |
| Input/output | [Input/Output](input-output.md) | Draft |
| Timing and clocks | [Timing And Clocks](timing-and-clocks.md) | Draft |
| Firmware | [Firmware](firmware.md) | Draft |
| Hardware abstraction | [Hardware Abstraction](hardware-abstraction.md) | Draft |

## Technical review and canonical boundaries

**Wave C authoring coverage: 9/9.** The earlier [Wave C Batch 01](../WAVE-C-TECHNICAL-REVIEW-01.md) and [Wave C Batch 02](../WAVE-C-TECHNICAL-REVIEW-02.md) audits establish scoped model-assisted review for their corresponding articles. The **nine newly authored Batch 03 articles across both Wave C areas remain Draft**, awaiting a separate scoped technical/source review.

This area distinguishes logical switching, hardware roles, ISA contracts, physical memory, interconnects, I/O, clocks, firmware, and abstraction. Operating-system memory management, device drivers and other software mechanisms retain separate ownership. Hardware timing does not settle the general-temporality decision G-04.

This area is a **navigation discipline**, not a new universal ontology or a mandate for any particular vendor, electrical implementation, chip architecture, operating system or data format. The original 12-area/109-heading approved architecture is unchanged. G-01, G-04 and G-06 remain unresolved scope questions; no Knowledge Checks or Practical Assessments are introduced.

[Fundamentals](../README.md) · [Knowledge relationships](../../../RELATIONSHIPS.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
