# Systems and Subsystems

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Systems and subsystems  
**Development status:** Draft  
**Source review:** Core claims checked (see [pilot technical review](../PILOT-TECHNICAL-REVIEW.md)); final editorial acceptance pending

## A system is a whole defined through relationships

A **system** is a set of elements regarded as a whole because their interactions contribute to a purpose, capability, function, or observable behavior. The identity of the system is not determined only by an inventory of components: the elements' organization, interfaces, relationships, and environment affect what the system does.

In engineering, systems may include people, physical equipment, software, procedures, information, and external services. The relevant system definition depends on what is being studied or built. A running software service, a transportation network, a manufacturing process, and a scientific instrument can each be treated as a system for a specified investigation.

NASA describes a system as elements functioning together to produce a required capability, and its systems-engineering guidance emphasizes both elements and their relationships. See [NASA Systems Engineering Handbook: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).

A system can be analyzed without assuming it is physically enclosed, isolated, or owned by one organization. What counts as its environment depends on the **system of interest** and its chosen boundary.

## System of interest, boundary, and environment

The **system of interest** is the particular whole chosen for study, design, or evaluation. A **boundary** distinguishes what the model treats as inside from what it treats as outside. That boundary can mark different kinds of separation: physical enclosure, functional responsibility, information exchange, operational authority, or limits of analysis.

An **environment** consists of relevant conditions and external entities that interact with or constrain the system. A boundary is not necessarily a wall; external conditions can affect the system through explicit or unmodeled paths.

For example, a building's heating system might include heaters, sensors, control software, and wiring. The building structure and outside weather may be treated as environmental influences rather than heating-system components. If the system of interest shifts to the **whole building**, the heating system may become a subsystem of that larger system.

This shift changes the **scope of analysis**, not the physical existence of the heater.

## Subsystems and decomposition

A **subsystem** is a system that functions as a constituent of a larger system in a chosen context. Subsystem status is therefore **relative**: one whole can be a subsystem of a larger whole and still contain subsystems of its own.

```text
Building (system of interest)
├── Heating (subsystem)
│   ├── Controller
│   ├── Sensors
│   └── Actuators
├── Lighting (subsystem)
└── Access systems (subsystem)
```

This tree is one legitimate **decomposition view**, not the only correct organization of the building. A communication network, shared power supply, or emergency procedure may cross several branches. A strict folder tree is convenient for navigation, yet it cannot capture every important relationship.

Engineering decomposition separates a system into manageable elements; **composition** and **integration** explain how those elements are assembled into a working whole. A list of parts is not a complete explanation of their collective behavior.

## Components, interfaces, functions, and responsibilities

A **component** is an element distinguished within the chosen system architecture. An **interface** specifies or describes the interaction surface or contract between elements, including exchanged energy, information, materials, controls, or services.

A system's **function** describes what it does; its **structure** describes how its elements are organized; its **behavior** describes what happens under particular inputs, conditions, and time evolution. These are related perspectives but not interchangeable.

Consider a heating controller:

| View | Illustrative content |
| --- | --- |
| Function | Regulate heating toward a selected set point |
| Components | Sensor, controller, switch, heater |
| Interfaces | Temperature reading, control signal, electrical power |
| State | Controller mode, measured reading, actuator status |
| Environment | Room conditions and external temperature |
| Behavior | Controller changes output in response to sensed conditions |

A list of components alone does not demonstrate that the heating function works. Function depends on interaction and assumptions: the sensor might be misplaced, the output may be delayed, or the environment may change faster than expected.

Functional decomposition and physical/product decomposition are **different views**. One component can contribute to several functions; one function can require several components.

## Interactions, emergence, and dependencies

Systems may exhibit **emergent properties**, features of the whole arising from interactions among elements rather than simply matching the properties of any one isolated component. Stability, traffic congestion, throughput, and complex failure behavior can depend upon the structure and dynamics of the whole.

This does not imply that emergent behavior is inherently unpredictable or mysterious. It means that component facts alone may be insufficient for a claim about the assembled system without understanding interactions and constraints.

A **dependency** describes a required condition or relationship for an intended behavior. Dependencies can form chains and feedback loops. Systems engineering therefore pays attention to interface compatibility, resources, timing, failure modes, and assumptions about the environment. A change in one component can produce downstream consequences elsewhere.

The general formal treatment of relations belongs in [Sets and relations](../mathematics-logic/sets-and-relations.md). The general concepts of entities and properties belong in [Entities and attributes](../models-abstraction/entities-and-attributes.md). Systems Engineering develops how those abstractions participate in an integrated whole.

## Systems-of-systems and boundary changes

Sometimes multiple independently operable systems cooperate to provide a higher-level capability. A **system of systems** is a context-dependent engineering concept in which constituent systems retain significant operational and managerial independence; it should not simply mean any system that has subsystems. [SEBoK's discussion of Systems of Systems](https://sebokwiki.org/wiki/Systems_of_Systems_%28SoS%29) identifies operational and managerial independence as especially important distinguishing characteristics.

For example, independently managed transportation, communications, and energy systems may jointly support a city-scale operation. Modeling their coordination requires attention to governance, trust, dependencies, and separate operational lifecycles. Their interfaces and relationships cannot be reduced to a single physical containment tree.

## An illustration of why boundaries matter

Suppose a climate-control model monitors a heater that appears functional but fails to maintain room temperature. A component-only inspection may find no broken heater. A broader **system** analysis could reveal that the sensor, controller, power supply, building insulation, and ventilation conditions interact.

Different boundary choices produce different but potentially valid explanations:

- If only the heater is inside scope, insulation and ventilation may be external constraints.
- If the entire room and climate-control equipment are inside scope, heat loss and sensor placement are modeled as internal mechanisms.
- If the entire building is the system of interest, other environmental and organizational interactions become relevant.

The correct boundary is the one explicitly justified by the purpose and question, not automatically the one producing the fewest elements.

## Where this knowledge connects

[Boundaries](../models-abstraction/README.md) provides the general concept of delimitation; [Relationships](../models-abstraction/README.md) provides association; [Architecture and composition](README.md) covers design views; [Components and interfaces](README.md) covers constituent responsibilities; [State and behavior](README.md) covers dynamics; [Human & Sociotechnical Systems](../human-sociotechnical-systems/README.md) covers the role of humans and organizations.

Those broader links currently lead to existing approved area indexes until canonical articles are written.

## References and verification status

- [NASA Systems Engineering Handbook: Definitions and appendices](https://www.nasa.gov/reference/system-engineering-handbook-appendix/).
- [NASA Systems Engineering Handbook: Fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/), for whole-system properties, system elements and their relationships.
- [SEBoK: Systems of Systems](https://sebokwiki.org/wiki/Systems_of_Systems_%28SoS%29), for the independence characteristics of systems of systems.
- [SEBoK: Main reference](https://sebokwiki.org/wiki/Main_Page), for broader systems-engineering concepts.

**Review record:** The system, subsystem, boundary, interface and systems-of-systems distinctions were checked against NASA's HTML Systems Engineering Handbook and SEBoK. An obsolete NASA procedural reference and an outdated software-handbook appendix have been replaced. The building example is illustrative, not a NASA-prescribed architecture. This remains a source-checked draft pending final editorial acceptance.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Governing Architecture](../ARCHITECTURE.md)
