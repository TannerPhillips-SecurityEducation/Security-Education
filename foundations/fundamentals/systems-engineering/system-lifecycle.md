# System Lifecycle

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** System lifecycle  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source audit pending

## Systems evolve from concept through retirement

A **system lifecycle** describes a system's evolution from initial conception through development, realization, utilization, support and retirement, according to a specified model. A **lifecycle model** organizes stages, activities, decisions and relationships to help manage that evolution. It is not an immutable law that every system must pass through the same number of sequential stages.

The [SEBoK Life Cycle Models](https://sebokwiki.org/wiki/Life_Cycle_Models) reference distinguishes lifecycle models from project schedules and notes that stages can overlap or repeat. [NASA Program/Project Life Cycle](https://www.nasa.gov/reference/3-0-nasa-program-project-life-cycle/) illustrates one organization-specific model, not a universal set of phases for all physical, computational and social systems.

A system may comprise elements with different lifetimes. Equipment can be replaced while an overall service persists; a software module may be revised repeatedly before the larger system retires. **Lifecycle identity and configuration identity are not identical.**

## System lifecycle versus project lifecycle

A **project lifecycle** concerns governance of a bounded initiative, its milestones, deliverables and decisions. A **system lifecycle** concerns the evolving system or service, including use and support beyond a particular delivery project.

A project may construct one system, modify several systems, or end while a system remains operational. Several projects may participate in one system's evolution. Treating a project closing date as proof that an operational system is retired would therefore be mistaken.

Lifecycle descriptions should specify their **system of interest**, scope, boundary, revisions and the model being applied. [Systems and Subsystems](systems-and-subsystems.md) owns boundary-relative whole/part definitions.

## Stages and processes are different

A **stage** identifies a period or state of maturity in a chosen lifecycle model. A **process** is a set of activities used to accomplish an objective; processes such as requirements management, verification, configuration management and risk analysis can recur across stages.

An illustrative sequence is:

```text
Conceive ↔ Define ↔ Design ↔ Realize ↔ Operate/Support ↔ Retire
```

The two-way arrows communicate possible iteration or return to earlier work, **not** a formal transition system or a requirement that each stage follows the prior one in strict order. Utilization, maintenance and redesign may overlap. An existing system may enter a new development effort while continuing to serve users.

No exact stage names or count are being ratified as the only valid taxonomy for Fundamentals.

## Lifecycle decisions and evidence

A meaningful lifecycle transition may depend on entrance/exit criteria, stakeholder decisions, operational readiness, safety conditions, documentation, resources and evidence. For example, a readiness decision might require evidence that defined interfaces function under specified conditions and that identified severe hazards are addressed.

A decision record should distinguish **evidence**, **remaining risk**, **authority**, **date/scope**, and **approved action**. An approval is a governance decision, not proof that all uncertainties have been removed.

**Configuration management** preserves identification and control of the system's designed or realized arrangements. **Change impact analysis** considers how alterations affect requirements, dependent elements, evidence and users. [Requirements](requirements.md), [Dependencies](dependencies.md), and [Verification and Validation](verification-and-validation.md) retain their own canonical mechanisms.

## Worked example: controlled revision

Suppose a fictional sensor service has release `v1` supporting values in degrees Celsius with an explicit unit field. A proposed `v2` adds an optional diagnostic field, while retaining the earlier required fields and values.

A simplistic backward-compatible reader may ignore the new field, but compatibility is **not proved** by the word “optional.” The actual v1 parser could reject unknown properties, or the new producer might change ordering, precision, field meaning or timing.

A meaningful change analysis therefore includes:

| Question | Evidence needed |
| --- | --- |
| Does v1 parse v2 output? | Tested instances under declared schema and reader rules |
| Are earlier meanings preserved? | Field semantics, units and conversion assumptions |
| Does operational behavior remain acceptable? | Representative integration and regression evidence |
| Can the change be reverted? | Configuration, data migration and state-recovery procedures |
| Have stakeholders accepted changed risks? | Recorded decision and criteria |

This invented example highlights that **syntactic**, **semantic** and **behavioral** compatibility are different. Version labels and passed tests are evidence within scope, not universal guarantees.

## Maintenance, support and retirement

Support may include monitoring, repair, calibration, updates, training, replacement, logistics and operational documentation. These activities have their own costs, risks and dependencies. A system that functions during initial acceptance may later degrade because of changing environmental conditions, worn components, new interfaces, changing users or evolving requirements.

**Retirement** may include shutting down services, preserving required records, disposing of equipment, transferring responsibilities, revoking access, or confirming that dependent systems are not left unsupported. These are contextual concerns, not one universal decommissioning checklist.

Data copies, backups, replicas and derivative products may outlive the originating operational system. [Data Provenance and Lifecycle](../information-data/data-provenance-and-lifecycle.md) owns information history and retention, while this article owns the whole system's evolution and retirement decisions.

## Adaptation and governance boundaries

A lifecycle model helps organize decision-making but cannot ensure technical correctness. A phase gate may be satisfied administratively while underlying performance remains unproven; a system can also require continued support even after a project formally closes.

Feedback from operations can inform requirements and redesign. Scientific evidence can invalidate assumptions that were reasonable when a baseline was approved. A mature system therefore requires some method for documenting changed knowledge and revising decisions, but the exact governance mechanism depends on the organization.

**G-04 general temporality** remains open; this article treats temporal progression only as applied to system engineering, not as canonical ownership of time, simultaneity or universal temporal logic.

### Sources

- [SEBoK: Life Cycle Models](https://sebokwiki.org/wiki/Life_Cycle_Models).
- [SEBoK: Life Cycle Concepts](https://sebokwiki.org/wiki/Life_Cycle_Concepts).
- [NASA: Program/Project Life Cycle](https://www.nasa.gov/reference/3-0-nasa-program-project-life-cycle/).
- [NASA: Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/).

**Editorial status:** Substantive Draft. The versioning example and stage/process distinctions require scoped technical source review. No new lifecycle taxonomy, mandatory project process or assessment is introduced.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
