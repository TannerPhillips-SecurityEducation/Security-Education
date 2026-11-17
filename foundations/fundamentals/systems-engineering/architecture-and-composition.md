# Architecture and Composition

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Architecture and composition  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 03 audit](../WAVE-B-TECHNICAL-REVIEW-03.md); no independent human peer review

## Architecture organizes how a system works as a whole

**System architecture** expresses fundamental concepts and organizing relationships of a system in its environment, including how elements fit together, how functions are allocated, and which principles or constraints govern design and evolution. **Composition** concerns assembling or relating constituent elements to form a working whole. **Decomposition** concerns identifying constituent elements or functions within that whole.

An architecture is not merely a diagram, a bill of materials, or a hierarchy. Different architectural descriptions may emphasize structure, function, behavior, information exchanges, deployment, or people. A drawing is a *representation of* an architecture, not necessarily the whole architecture itself.

The [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) describes architecture, requirements allocation, system boundaries, and technical tradeoffs. [SEBoK System Architecture Design Definition](https://sebokwiki.org/wiki/System_Architecture_Design_Definition) distinguishes related functional, logical, and physical viewpoints.

## Decomposition and composition are related but not inverses

**Decomposition** can separate a system into elements for understanding, assigning responsibilities, or implementing a design. **Composition** concerns whether and how those elements interact and integrate to produce the required behavior. The operations are not automatically reversible.

Consider a building climate-control system:

```text
Functional view:
  Measure conditions -> Determine action -> Deliver heating

Candidate physical view:
  Sensor -> Controller -> Switch -> Heater
```

This mapping is illustrative, not mandatory. The same function may be performed by multiple components, or several functions by one component. A component tree may hide shared power, operator actions, environmental influences, and cross-branch control signals. **Reassembling the correct parts without compatible interfaces does not establish correct system behavior.**

[Components and Interfaces](components-and-interfaces.md) develops responsibilities and interaction contracts. [Systems and Subsystems](systems-and-subsystems.md) develops boundary-relative decomposition.

## Multiple architectural views

A view selects certain concerns to support decisions. Different views may emphasize:

| View | Representative concern | Important limitation |
| --- | --- | --- |
| Functional | What transformations or capabilities are required? | Functions are not necessarily physical components |
| Logical | How are roles, responsibilities, and interactions organized? | Logical grouping need not determine deployment |
| Physical | Which assemblies, locations, or resources realize the design? | Physical proximity need not imply functional dependency |
| Behavioral | What sequences and state changes are permitted? | A trace may omit unmodeled conditions |
| Operational | How do users, operators, and environment interact with the system? | Intended procedures may differ from actual usage |

These are useful **illustrative views**, not five additional knowledge areas or an obligatory repository modeling framework. Views may overlap and can be combined or split for a given project. Consistency and traceability between views matter more than forcing all concerns into one diagram.

NASA's [Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/) emphasizes functional analysis, requirements allocation, interfaces, and iterations across architectural alternatives.

## Architecture constrains possible compositions

Architecture can impose **allocation**, **interaction**, **capacity**, **resource**, **safety**, **performance**, or **lifecycle** constraints. It may also express conventions such as separation of concerns, redundancy, modular replacement, or controlled shared services.

A constraint should be stated precisely enough to evaluate. For example, “the sensor shall provide temperature in degrees Celsius” is an interface requirement. “The controller shall produce a heating command within 200 ms of a valid input” is an illustrative behavioral/performance requirement. Neither can be inferred solely from the presence of an edge in an architecture diagram.

**Architectural tradeoffs** involve comparing alternatives relative to intended outcomes and assumptions. Increasing redundancy can improve some failure scenarios while increasing component count, power demand, maintenance, or common-mode risks. A design choice is not inherently optimal without criteria and evidence.

## Worked comparison: two heating designs

Suppose Design A has one temperature sensor driving one controller and one heater. Design B adds a second sensor and a reconciliation function.

| Concern | Design A | Design B |
| --- | --- | --- |
| Sensing path | One reported temperature | Two reported temperatures |
| Integration | Fewer interactions | Requires comparison/reconciliation |
| Fault tolerance | Sensor failure may remove the only reading | May tolerate some single-sensor faults under defined assumptions |
| New failure modes | Single-sensor dependence | Sensor disagreement, common power faults, reconciliation mistakes |

**Design B is not automatically more reliable.** Its benefit depends on sensor independence, calibration, placement, reconciliation logic, environmental conditions, and operational policies. Merely counting components cannot decide.

The example shows that architecture is evaluated against **behavior and requirements**, not visual complexity or diagram symmetry.

## Composition, integration, and verification

An **architectural model** expresses intended relationships. **Integration** realizes connections among actual system elements. **Verification** checks whether specified requirements are satisfied under a defined method and scope. **Validation** addresses fitness for intended use and stakeholder needs. These are related but separate.

A component could individually satisfy its specification while the composed system violates an end-to-end timing constraint. Conversely, an architecture that appears coherent on paper can include an interface whose interpretation is ambiguous or unimplemented.

[Conceptual and Formal Models](../models-abstraction/conceptual-and-formal-models.md) owns general formalization and model-to-target relationships. [Verification and Validation](verification-and-validation.md) is the separate canonical Systems & Engineering subject; this architecture article does not redefine it.

## Changes to architecture

An architecture is subject to evolution. Adding a component can affect resource allocation, compatibility, operational responsibilities, and failure paths. An architectural decision record can preserve rationale, alternatives, assumptions, and rejected options, but a record alone is not proof that a decision was correct.

Architectural descriptions must identify the relevant **system of interest**, boundary, version, and intended use when those distinctions affect interpretation. Detailed formal change-control methods belong to the approved [System Lifecycle](system-lifecycle.md) subject and later specialized knowledge domains.

## Boundaries and references

This reference does not prescribe a particular architecture-description language, vendor product, design pattern, or formal ontology. [Dependencies](dependencies.md) develops necessary relationships and propagation; [State and Behavior](state-and-behavior.md) develops permitted behavior of integrated systems. Architecture uses these concepts without absorbing their definitions.

### Sources

- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).
- [NASA: Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/).
- [NASA: System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/).
- [SEBoK: System Architecture Design Definition](https://sebokwiki.org/wiki/System_Architecture_Design_Definition).

**Editorial status:** Reviewed (model-assisted) following the [Wave B Batch 03 scoped 24-family technical review](../WAVE-B-TECHNICAL-REVIEW-03.md). Complete source verification, independent human expert peer review and final publication approval remain separate outstanding gates.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
