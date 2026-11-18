# Electrical Circuits

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Electrical circuits  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source audit pending

## Connections and element behavior determine circuit outcomes

An **electrical circuit** is an arrangement of connected electrical elements and paths described for the purpose of understanding charge flow, potential differences, energy transfer, and physical behavior. A **circuit diagram** represents selected components and connections; it is not proof of how a constructed device is wired or whether the real components meet their models.

Common analysis terms include **node** (electrically connected reference region under ideal-wire assumptions), **branch** (an element or defined connecting path), and **loop** (a closed path through the circuit graph). Circuit elements may be modeled as resistors, capacitors, inductors, sources, switches and other ideal or nonideal devices.

[Electricity](electricity.md) owns electrical quantities; this article owns relationships imposed by interconnected elements. [Electronics](README.md) will develop specialized devices and active circuit mechanisms.

## Ideal versus physical elements

A model may represent an ideal resistor through `v=iR`, a capacitor through `i=C,dv/dt`, or an inductor through `v=L,di/dt` under stated passive sign conventions. These relations are local device models with assumptions about linearity, time variation and applicability.

Real components can have parasitic resistance, capacitance, inductance, thermal limits, finite response times and frequency-dependent behavior. Their practical behavior may require detailed distributed or electromagnetic models.

A circuit model should declare its values, reference directions, polarity, source properties and conditions before deriving results. A simulated network can be internally consistent while failing to represent a real assembly.

## Kirchhoff constraints and when they apply

**Kirchhoff's current law (KCL)** expresses charge conservation in a circuit node model: the algebraic sum of currents into/out of a node is zero when charge accumulation at that modeled node is negligible or appropriately accounted for.

**Kirchhoff's voltage law (KVL)** expresses the loop relationship of modeled potential differences under the circuit's assumptions. Its familiar sum-of-voltages-equals-zero form is straightforward for lumped quasi-static circuits. In arrangements with significant time-varying magnetic flux linkage, induced electromagnetic fields require a more careful formulation, so applying KVL without assumptions can be misleading.

The [OpenStax University Physics circuits chapter](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel) treats ideal resistor networks, source potentials and the resulting current/voltage relations. [Graph Theory](../mathematics-logic/graph-theory.md) owns the mathematical structure of paths and cycles rather than circuit physics.

## Series and parallel are connection properties

Two ideal resistive elements **in series** carry the same current when no additional connection branches at their shared node. Under the usual linear ohmic assumptions, `R_series=R1+R2`. Two ideal resistors **in parallel** share the same potential difference when their terminals connect to the same two ideal nodes; then

```text
1 / R_parallel = 1 / R1 + 1 / R2
```

for positive finite resistances. The physical distance between parts is not enough to establish series or parallel topology.

## Worked example: ideal parallel branches

Suppose an ideal `12 V` source is connected across two ideal resistors, one `4 Ω` and the other `6 Ω`, with negligible wire resistance and all positive values as stated.

```text
  12 V source
      |
      +---[ 4 Ω ]---+
      |             |
      +---[ 6 Ω ]---+
      |             |
      +-------------+
```

The equivalent resistance is:

```text
R_eq = (1/4 + 1/6)^(-1) Ω = (5/12)^(-1) Ω = 12/5 Ω = 2.4 Ω
I_total = 12 V / 2.4 Ω = 5 A
I_4Ω = 12/4 = 3 A
I_6Ω = 12/6 = 2 A
```

KCL is satisfied at the junction: `3 A + 2 A = 5 A`. Total resistor power absorption is `P=VI=12×5=60 W`, consisting of `36 W` in the 4 Ω branch and `24 W` in the 6 Ω branch. These are **hypothetical equations**, not directions to construct a real power circuit.

## Energy storage and time-dependent circuits

Capacitors store energy in electric fields, and inductors store energy in magnetic fields. Unlike a simple steady resistive model, networks with capacitors and inductors can respond over time to changes, requiring initial conditions and appropriate differential equations.

For a linear ideal capacitor, `E_C=½ C V²`; for a linear ideal inductor, `E_L=½ L I²`. These formulae are conditional on element models, not measured energy values for arbitrary devices. Real components have losses, limits and coupling.

The general system behavior and feedback concepts belong respectively to [State and Behavior](../systems-engineering/state-and-behavior.md) and [Feedback and Control](../systems-engineering/feedback-and-control.md). The general placement of time and temporality remains open under G-04; circuits retain applied temporal mechanisms within their approved area.

## Circuits versus electronics and digital logic

An electrical circuit can carry power, implement analog processing, or realize digital operations, depending on its devices and design. **Electronics** focuses on devices and circuits used to control or process electrical signals, often with nonlinear semiconductor elements. **Digital Logic** develops physical switching circuits that implement Boolean and sequential logical behavior.

The labels do not make three isolated physical domains. A processor is a digital system implemented through electronic devices assembled in electrical circuits. Canonical references separate general concepts to avoid treating every digital gate as a complete circuit theory.

[Digital Logic](../digital-systems-hardware/digital-logic.md) retains its specialized foundational ownership, while [Computing Components](../digital-systems-hardware/computing-components.md) develops integrated hardware roles.

### References

- [OpenStax: Resistors in Series and Parallel](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel).
- [OpenStax: Resistivity and Resistance](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance).
- [MIT OpenCourseWare: Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).

**Editorial status:** Substantive Draft with a verified-on-paper ideal parallel-circuit example. The conceptual claims, model assumptions and numeric results require a separate scoped technical audit before Reviewed status.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
