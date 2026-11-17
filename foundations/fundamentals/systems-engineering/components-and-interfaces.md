# Components and Interfaces

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Components and interfaces  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 03 audit](../WAVE-B-TECHNICAL-REVIEW-03.md); no independent human peer review

## Constituents become a system through interaction

A **component** is an element distinguished within a system for a specified function, responsibility, or structural role. An **interface** describes the boundary across which elements interact, including the conditions and conventions governing exchanges. An inventory of components is not a specification of how the assembled system works.

Components may be physical assemblies, software services, human roles, procedures, or mixed arrangements. Their granularity depends on the chosen system of interest. A device that is treated as one component in a building may itself contain several components when examined as a subsystem. **Component membership is relative to a decomposition**, not an immutable classification of an object.

[Systems and Subsystems](systems-and-subsystems.md) owns the concept of a composed whole and its boundary. This article develops individual constituents, their assigned responsibilities, and the interaction contracts needed to integrate them.

## Responsibility, function, and implementation

A **function** describes what an element or system is expected to do. **Responsibility** identifies what an element is accountable for within a chosen design. **Implementation** describes how an allocated function is realized. They may not map one-to-one:

- A single component can perform several functions.
- A single function can require several cooperating components.
- One responsibility may be shared or reassigned under another architecture.
- A component may exist for structural, safety, service, or organizational reasons beyond the primary function.

For a hypothetical climate-control system, temperature sensing, deciding on an output, and delivering heat are distinct functions. A temperature sensor, controller, and actuator/heater are candidate components, but a different design could redistribute these responsibilities. **The functional decomposition does not prove the physical decomposition.**

NASA's [Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/) distinguishes system requirements and functions from the design elements ultimately chosen to realize them.

## Interfaces define interactions across boundaries

An interface may describe transfer of **information, material, energy, control, or services**, and can be specified at multiple levels. A physical connector might specify geometry, tolerances, voltage, and permitted loads. A logical interface might specify message types, permitted operations, units, sequencing, and error responses. A human-system interface may specify controls, indications, and procedures.

An interface description is meaningful only with its **direction, endpoints, scope, operating conditions, and relevant assumptions**.

| Interface facet | Example within a hypothetical heating system |
| --- | --- |
| Provider and consumer | Sensor provides a reading; controller consumes it |
| Exchanged quantity | Reported temperature |
| Representation | Number accompanied by degrees Celsius |
| Update condition | A reading provided when sampled |
| Invalid input | Missing, malformed, or out-of-range measurement |
| Expected behavior | Controller applies a documented handling rule |
| Physical coupling | Power and signaling paths compatible with equipment |

These are illustrative interface concerns, not a mandated universal interface-document schema. NASA's [Interface Management](https://www.nasa.gov/reference/6-3-interface-management/) describes the identification, documentation, compatibility, and control of internal and external interfaces.

## Connection is not compatibility

Two components can be connected without being able to operate together. **Syntactic compatibility** asks whether the exchanged representations meet the declared format or signature. **Semantic compatibility** asks whether the producer and consumer interpret the exchange consistently. **Behavioral compatibility** concerns timing, order, state, error handling, and other interaction expectations.

Suppose a sensor emits the numerical value `68`, believing it denotes degrees Fahrenheit, while a controller interprets `68` as degrees Celsius. The interface may carry a syntactically valid number while violating the intended physical semantics. Converted correctly, `68 °F = 20 °C`; interpreting it as `68 °C` changes the asserted physical condition dramatically.

This example demonstrates that **agreement about a data type is not enough**. [Units and Quantities](../mathematics-logic/units-and-quantities.md) owns conversion mathematics, [Data Types](../information-data/data-types.md) owns type semantics, and [Schemas](../models-abstraction/schemas.md) owns declared representation constraints.

## Contracts, assumptions, and failure

An **interface contract** states conditions under which interacting parties may rely on specified behavior. A contract can include preconditions, allowed inputs, output guarantees, error handling, resource limits, and environmental constraints. The term *contract* does not require a particular programming-language feature or legal agreement.

A contract statement is a model or specification, not evidence that an implementation satisfies it. Interface testing can expose mismatches, while a successful test under selected conditions does not guarantee compatibility under every conceivable condition.

Interface failure can arise from broken connections, incompatible units, stale assumptions, resource exhaustion, timing differences, unsupported versions, or ambiguous ownership. Some failures are local; others affect downstream components through **Dependencies**. One incompatible interface can prevent a whole system from satisfying a requirement even when both individual components work in isolation.

## Internal versus external interfaces

Whether an interface is **internal** or **external** depends on the system boundary under consideration. A controller-to-sensor exchange may be internal to a heating system but external to the controller when the controller is itself the system of interest.

A subsystem boundary can hide implementation details and expose a smaller set of contracts to its environment. Such **encapsulation** can reduce coupling but does not ensure that every external influence is mediated or that undocumented side effects are absent.

The same real-world relationship can appear in multiple model views. A wiring diagram can represent an electrical interface; a functional diagram may represent an exchange of sensor readings. These diagrams are not necessarily interchangeable.

## Canonical boundaries and applications

[Architecture and Composition](architecture-and-composition.md) owns system-wide organization and design views. [Dependencies](dependencies.md) owns necessary relationships and propagation assumptions. [State and Behavior](state-and-behavior.md) owns system evolution under inputs. [Relationships](../models-abstraction/relationships.md) owns the general concept of association. Specialized hardware connectors, software APIs, industrial interfaces, and communication protocols extend these concepts in their respective knowledge domains.

No interface specification format, API standard, new taxonomy, or assessment activity is adopted by this reference.

### Sources

- [NASA: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).
- [NASA: Logical Decomposition](https://www.nasa.gov/reference/4-3-logical-decomposition/).
- [NASA: Interface Management](https://www.nasa.gov/reference/6-3-interface-management/).
- [SEBoK: System Requirements Definition](https://sebokwiki.org/wiki/System_Requirements).

**Editorial status:** Reviewed (model-assisted) following the [Wave B Batch 03 scoped 24-family technical review](../WAVE-B-TECHNICAL-REVIEW-03.md). Complete source verification, independent human expert peer review and final publication approval remain separate outstanding gates.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
