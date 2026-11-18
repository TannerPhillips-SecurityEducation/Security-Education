# Matter and Energy

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Matter and energy  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source audit pending

## Physical systems contain material and exchange energy

**Matter** refers to physical material and its constituents, whose properties and interactions are described by models appropriate to the scale being studied. **Energy** is a physical quantity used to characterize the capacity of physical systems to undergo or produce changes through work, heat transfer and other processes. Energy is **not a material substance or a synonym for electricity**.

An engineered system may contain solids, fluids, gases, electronic components and material interfaces. The behavior of an element depends on its structure, composition, environment and interactions, not simply on its name or location in a component inventory.

The [OpenStax University Physics discussion of work](https://openstax.org/books/university-physics-volume-1/pages/7-1-work) treats energy transfers associated with applied forces and displacements; the [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure) establishes the relevant units. These sources provide foundational mechanics and metrology, not a universal physical ontology adopted by this repository.

## Materials, states, properties and mechanisms

Physical descriptions may involve **mass**, density, volume, temperature, mechanical strength, thermal conductivity, electrical conductivity, and other properties. Which properties matter depends on purpose. A copper conductor, ceramic insulator and cooling fluid can participate in the same technical system with quite different physical roles.

The **state of a material** refers to its relevant physical condition under a model. A particular material can change temperature, phase, deformation or charge distribution while retaining some other attributes. Some transitions can alter performance, damage a component or make a previously valid engineering assumption false.

The general definitions of [Entities and Attributes](../models-abstraction/entities-and-attributes.md) and [State, Events, and Transitions](../models-abstraction/state-events-and-transitions.md) remain in Models & Abstraction. This article owns the physical mechanisms and their constraints.

## Energy, work and power are separate quantities

In a simplified mechanics model, **work** transfers energy when a force acts through a displacement. For a constant force and displacement vector:

```text
W = F · d = |F| |d| cos(θ)
```

where θ is the angle between force and displacement. Work can be positive, negative or zero, depending on their orientation. Work and energy share the SI derived unit **joule (J)**. **Power** is the rate of energy transfer or work, with the watt `1 W = 1 J/s`. The symbols are context-dependent: `W` is also the symbol of the watt unit, so distinguish a work variable from a unit symbol.

If a constant force of `10 N` acts parallel to a displacement of `3 m` in the stipulated model, the work is `30 J`. If the same `30 J` is transferred uniformly over `5 s`, the mean transfer power is `30/5 = 6 W`. The example assumes all values, alignments and system boundaries exactly as stated; it is not an instrument reading.

[Units and Quantities](../mathematics-logic/units-and-quantities.md) owns the general quantity calculus and unit conventions. [Measurement](../scientific-analytical-reasoning/measurement.md) owns measurement uncertainty.

## Conservation does not mean absence of change

Conservation laws express constraints on permitted physical changes under specified models and boundaries. In an **isolated system**, total energy is conserved under the applicable physical theory. When an engineered system exchanges energy with its surroundings, its internal energy can increase or decrease without violating conservation.

A heating element converts supplied electrical energy into thermal energy and may also produce light or other effects. An electrical motor can convert electrical input into mechanical output while also transferring energy as heat and sound. These are examples of **energy transformation**, not disappearance of energy.

The boundaries of a physical system are therefore crucial. Measuring only useful output and ignoring losses is not a complete energy balance. A highly efficient component under one load is not necessarily efficient across all environmental conditions.

## Heat, temperature and thermal behavior

**Temperature** is a physical quantity associated with thermal state; **heat** is energy transferred because of a temperature difference, in thermodynamic usage. They are not interchangeable. A temperature reading does not alone specify the total thermal energy of an object, which also depends on material properties and amount of matter.

Thermal transfer may occur through conduction, convection or radiation, with different governing conditions. A device can dissipate heat during normal operation but fail under insufficient cooling even if its digital logic is correct. Material limits, environment and thermal paths belong to the physical reality that constrains all hardware designs.

The exact thermal model requires appropriate properties, boundary conditions and measurements; this article does not impose one constitutive law on every material.

## Work example: physical constraints on a computing device

Suppose a fictional electronic assembly consumes `20 W` of electrical power for `60 s`. Under a constant-power assumption, it receives `20×60=1200 J` of electrical energy in that interval. This does **not** prove that all 1200 J becomes internal stored heat: energy can leave through mechanical work, radiation, conducted or convected heat, or other channels.

Evaluating temperature rise needs additional information about cooling, heat capacities, geometry, ambient conditions and power history. An energy accounting equation alone does not predict a safe operating temperature.

## Canonical boundaries and relationships

[Electricity](electricity.md) owns charge, current and potential difference. [Electrical Circuits](electrical-circuits.md) owns interconnected lumped-element behavior. [Computing Components](../digital-systems-hardware/computing-components.md) owns the role of hardware elements in digital systems. General [Feedback and Control](../systems-engineering/feedback-and-control.md) owns regulation rather than all physical processes by which energy moves.

**Matter and Energy** remains a domain-independent physical foundation. It creates no new subject heading, mandatory material classification, experimental assessment or safety-certification claim.

### References

- [OpenStax University Physics Volume 1: Work](https://openstax.org/books/university-physics-volume-1/pages/7-1-work).
- [OpenStax University Physics Volume 1: Chapter 7 Summary](https://openstax.org/books/university-physics-volume-1/pages/7-summary).
- [BIPM: The International System of Units (SI Brochure)](https://www.bipm.org/en/publications/si-brochure).

**Editorial status:** Substantive Draft with stipulated physical calculations. A separate technical and source audit is required before internal review-state promotion. Independent human acceptance and final publication remain pending.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
