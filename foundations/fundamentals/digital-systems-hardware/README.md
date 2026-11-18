# Digital Systems & Hardware

**Division:** [Fundamentals](../README.md)  
**Architecture status:** Approved subject area  
**Content status:** Three of nine headings authored (two Reviewed model-assisted; one Draft); six not yet authored  
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
| Processors and instruction sets | [Processors and Instruction Sets](processors-and-instruction-sets.md) | Draft |
| Memory and storage | Not authored | Inventoried |
| Buses and interfaces | Not authored | Inventoried |
| Input/output | Not authored | Inventoried |
| Timing and clocks | Not authored | Inventoried |
| Firmware | Not authored | Inventoried |
| Hardware abstraction | Not authored | Inventoried |

## Technical review and canonical boundaries

[Digital Logic](digital-logic.md) passed the [six-pilot claim-to-source review](../PILOT-CLAIM-SOURCE-AUDIT.md). [Computing Components](computing-components.md) passed the [Wave C Batch 01 technical audit](../WAVE-C-TECHNICAL-REVIEW-01.md). Both are internally Reviewed (model-assisted). [Processors and Instruction Sets](processors-and-instruction-sets.md) is a substantive Wave C Batch 02 **Draft** awaiting its own technical audit.

The subjects distinguish physically implemented logic, overall hardware roles, and the software-visible instruction-set contract. An ISA is not synonymous with a microarchitecture, and an address space's capacity is not proof of installed memory. The remaining six headings retain separate canonical scope when authored.

[Bits and Bytes](../information-data/bits-and-bytes.md) owns binary units, [Data Types](../information-data/data-types.md) owns value interpretation, [Electrical Circuits](../physical-electrical-principles/electrical-circuits.md) owns circuit physics, and [State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) owns general state semantics.

General time and temporality G-04 remain an unresolved architectural decision; a future article on Timing and Clocks does not settle that decision by default. G-01 and G-06 also remain open.

No assessments, new approved subjects, mandated CPU architecture or publication acceptance are introduced.

[Fundamentals](../README.md) · [Knowledge relationships](../../../RELATIONSHIPS.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
