# Boundaries

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Boundaries  
**Development status:** Reviewed (model-assisted; human expert review and final release pending)  
**Source review:** Core claims checked in [Wave A Batch 04 review](../WAVE-A-TECHNICAL-REVIEW-04.md); independent expert verification not claimed

## A boundary both separates and limits

A **boundary** is a delimitation that distinguishes one modeled region, whole, entity, scope, or condition from what is outside it. Boundaries have two related but distinct functions:

1. **Separation:** they distinguish inside from outside, one subject from another, one category from another, or one state regime from another.
2. **Limitation:** they define the extent, permissible range, responsibility, reach, or operating conditions within which a description or mechanism is intended to apply.

These functions often coincide, but not every boundary is a physical barrier. A system's boundary may be specified by an observer to make an analysis coherent; a mathematical domain constraint may limit where a function is defined; an organizational boundary may delimit responsibility; and a physical enclosure may separate environments while permitting exchanges through designed interfaces.

The [SEBoK definition of system boundary](https://sebokwiki.org/wiki/System_Boundary_%28glossary%29) describes a distinction made by an observer between system and environment. Its [Introduction to Systems Engineering Fundamentals](https://sebokwiki.org/wiki/Introduction_to_System_Fundamentals) explains why analyzing a system of interest requires considering both its elements and their interaction with the environment.

This article develops **domain-agnostic delimitation**, not network segmentation, access control, or any other security-specific implementation.

## Boundary, entity, system, and environment

An **entity** is a modeled subject. A **boundary** helps determine the extent of the subject in a chosen analysis. The **environment** is relevant context that falls outside the selected subject, even when it influences behavior inside it.

For example, a model of a **temperature sensor** may include the sensing element, its local electronics, and its output signal. The measured fluid may remain outside that sensor's boundary even though the sensor interacts with it.

A broader **measurement system** might include the sensor, calibration model, sampling software, and storage for indications. The same sensing component is internal to this wider system, and the environment is now defined differently.

The chosen boundary thus changes which elements are **internal** or **external** to the analysis, not necessarily the physical location of anything.

[Entities and Attributes](entities-and-attributes.md) develops what is distinguished; [Systems and Subsystems](../systems-engineering/systems-and-subsystems.md) explains how a system-of-interest boundary shapes decomposition and environmental context.

## Boundary and interface are different

An **interface** is a defined surface, relationship, or contract through which parts of a system, or a system and its environment, interact. A system may have one, several, or no **explicitly modeled interfaces across its chosen boundary**. The boundary distinguishes a scope; the interface describes an interaction within or across a scope.

Consider a container with an inlet and an outlet. Its physical wall separates the interior from its surroundings. The inlet and outlet are designed interfaces across that boundary. The wall and openings help define where material can pass, but the existence of an interface does not erase the distinction between interior and exterior.

For a software component, the boundary may be logical rather than physical. A callable API describes an interface that permits selected interactions with functions or data maintained within a component's abstraction. Whether those interactions are authorized is a **separate security question** and does not follow from the mere existence of the interface.

A boundary is therefore not automatically impermeable, and an interface is not automatically trustworthy.

## Types of delimitation

Boundaries can be studied in several overlapping ways.

| Perspective | Example | Principal distinction |
| --- | --- | --- |
| **Physical** | Surface of a vessel | Material or spatial separation |
| **Conceptual** | Scope of a definition or model | What the concept includes and excludes |
| **Mathematical** | Domain where `1/x` is defined | Permitted values and constraints |
| **Computational** | Process address-space model | Distinct execution or resource contexts |
| **Functional** | Responsibility of a subsystem | Which functions and exchanges are assigned |
| **Organizational** | Authority to modify a component | Responsibility and governance |
| **Temporal** | Period to which a report applies | Validity interval under defined time assumptions |

These are **illustrative boundary perspectives**, not seven new approved navigation areas or a formal ontology. The same modeled system may have several different boundaries for different purposes, and they need not align.

For example, a physically shared machine can host several computational execution contexts with distinct logical boundaries. Conversely, one logical service can span multiple physical machines.

## Sharp, graded, and context-dependent boundaries

A boundary may be modeled as **sharp** when membership is defined unambiguously under the model. For example, an integer `x` either belongs to the mathematical set `{1,2,3}` or it does not.

In other cases, membership may be **graded** under a chosen fuzzy or threshold-based model, or the *location of a sharp boundary* may be **uncertain** because observations are incomplete. These are different conditions: uncertainty about a boundary is not the same as deliberately assigning graded membership. The physical edge of a fog bank, the effective range of a sensor, or an organization's informal influence may not admit one precise cutoff without an additional convention.

A **threshold** can define a sharp classification boundary over a continuous measured variable, such as:

```text
if reported_temperature ≥ 30 °C:
    category = HIGH
else:
    category = NOT_HIGH
```

The model has specified a classification threshold of 30 °C. It has **not** proven that the real world's physical state changes discontinuously at precisely that value, nor that a noisy measurement is always classified correctly.

This is a boundary in a **decision model**, not necessarily a physical wall or a causal phase change.

## Boundaries as limitations

Boundaries also **limit** what statements or operations apply. Consider a real-valued function:

```text
f(x) = 1/x
domain: x ∈ ℝ and x ≠ 0
```

The excluded value is a **domain limitation**: the function is not defined at zero within the chosen real-valued rule. This is not equivalent to physical separation or a prohibition enforced by software. An implementation must specify how it behaves when given an invalid input.

Likewise, a scientific result may apply only within a calibrated range. Extrapolating beyond that range requires justification, even if a numerical formula can still be evaluated.

A system boundary can limit a **claim's scope**. If a report says that all observed components behaved normally, its justification depends on whether the observation boundary covered all components relevant to the claim. Coverage is an evidential limitation, not proof about unobserved components.

The difference between boundary and measured extent matters across [Measurement](../scientific-analytical-reasoning/measurement.md), [Observation](../scientific-analytical-reasoning/observation.md), and [Evidence](../scientific-analytical-reasoning/evidence.md).

## Nested and overlapping boundaries

A system may have subsystems with **nested boundaries**, but useful models can also contain **overlapping scopes**. A component can contribute to multiple functions, and a physical device can participate in more than one operational context.

For example:

```text
Building boundary
  ├── Climate-control functional scope
  ├── Electrical-power functional scope
  └── Monitoring functional scope
```

The same sensor may be involved in climate control and monitoring, while shared electrical infrastructure supports both. The scopes overlap even when a simple tree lists separate responsibilities.

A folder hierarchy can supply navigation, but it cannot completely represent these overlapping relationships. Consequently, our [Knowledge Relationship Conventions](../../../RELATIONSHIPS.md) require explicit links, and do not treat folder placement as an automatic formal `is-a` or `part-of` statement.

## The role of assumptions in defining a boundary

A defensible boundary decision should declare:

- **What** is included and excluded;
- **why** that distinction serves the question at hand;
- **which interactions** cross the boundary;
- **which constraints** or limiting conditions apply;
- **what remains unknown or unobserved** because of that scope.

This is a useful editorial practice, not a mandatory five-field metadata schema.

A boundary choice can be revised as the model or question changes. Revising scope does not necessarily mean the original physical entity has changed. It does mean that two analyses with different boundaries may need explicit reconciliation before their conclusions can be compared.

## Worked illustration: changing the system of interest

Suppose the observed room temperature differs from a controller's set point.

**Narrow boundary:** The controller is the system of interest. The sensor, heater and room are external participants. The analysis emphasizes commands and controller inputs.

**Intermediate boundary:** Controller, sensor and heater belong to one climate-control system. The room remains its environment. Interactions include measurements, control signals and heat transfer.

**Wider boundary:** The building and its HVAC equipment form the system of interest. Insulation, air exchange and room-to-room coupling are now internal mechanisms. Outside weather remains environmental.

Each boundary produces a different useful decomposition. None proves a cause merely by drawing a box. What can be inferred depends on the available observations, mechanisms and assumptions.

The [SEBoK account of engineered system context](https://sebokwiki.org/wiki/Engineered_System_Context) stresses the importance of wider systems, environmental influences, and selecting the system-of-interest boundary to match the analysis.

## Relationships and unresolved questions

[Entities and Attributes](entities-and-attributes.md) explains what is distinguished; [Identity and Distinction](identity-and-distinction.md) explains persistence and sameness; [Relationships](relationships.md) explains interactions across or within boundaries; [Systems and Subsystems](../systems-engineering/systems-and-subsystems.md) explains composition; [State, Events and Transitions](state-events-and-transitions.md) explains modeled conditions and change.

This article mentions spatial and temporal boundary perspectives but **does not resolve** the G-01 mathematical-geometry/topology coverage decision or G-04 general temporality. Specialized security boundaries belong in their appropriate security and domain references, not as the organizing principle here.

### References

- [SEBoK: System Boundary (glossary)](https://sebokwiki.org/wiki/System_Boundary_%28glossary%29).
- [SEBoK: Introduction to System Fundamentals](https://sebokwiki.org/wiki/Introduction_to_System_Fundamentals).
- [SEBoK: Engineered System Context](https://sebokwiki.org/wiki/Engineered_System_Context).
- [NASA Systems Engineering Handbook: Fundamentals of Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).

**Review note:** System boundary, system of interest, and engineered context were checked against SEBoK's glossary and contextual references. Separation and limitation remain the approved governing conceptual framing. Sharp-versus-graded membership is now explicitly distinguished from uncertainty about a boundary. These are editorial distinctions and examples, not a ratified ontology; the Batch 04 audit records a scoped model-assisted review, not independent human acceptance.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
