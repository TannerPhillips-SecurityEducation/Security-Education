# Electronics

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Electronics  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source review pending

## Controlling electrical behavior using devices and circuits

**Electronics** concerns devices and arrangements that control or process electrical signals and energy through their electrical characteristics. Electronic systems may amplify, switch, rectify, regulate, detect, generate or transform signals. The term covers analog, digital and mixed-signal arrangements, not only computers.

Electronics builds on [Electricity](electricity.md), which owns charge, current, potential difference, and resistance, and [Electrical Circuits](electrical-circuits.md), which owns connected-element constraints such as Kirchhoff's rules. This article owns general electronic device behavior, operating regions, biasing, amplification and switching. [Digital Logic](../digital-systems-hardware/digital-logic.md) owns the specialized realization of Boolean and sequential functions in digital hardware.

## Passive, nonlinear and active behavior

A resistor, capacitor or inductor may be described by an ideal lumped-element model, but an actual device can exhibit temperature dependence, limits, leakage, losses and parasitics. Other components have nonlinear electrical characteristics.

A **diode** is a two-terminal device whose current–voltage relationship generally depends on polarity, temperature and device characteristics. A **transistor** can be used to control current or voltage through another electrical input, enabling switching and amplification. A device classification is useful for discussing behavior, but neither a diode nor transistor has one universally exact operating equation.

**Biasing** establishes an operating condition around which device behavior can be analyzed. In a small-signal model, a nonlinear device may be approximated locally by a linear relationship for sufficiently small changes; that approximation need not remain valid at large inputs.

The [MIT 6.004 Computation Structures course](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) covers CMOS switching and digital abstraction. For foundational semiconductor and solid-state behavior, see [OpenStax University Physics Volume 3: Semiconductor Devices](https://openstax.org/books/university-physics-volume-3/pages/9-7-semiconductor-devices).

## Signals, power and operating limits

Electronic devices interact with physical voltages and currents, not abstract Boolean values directly. A digital input commonly has **specified ranges** interpreted as logical low or high, with thresholds, noise margins and undefined regions depending on the implementation. Analog circuits may represent an input quantity by a varying voltage or current over an operating range.

Power supply constraints, thermal dissipation, frequency response, bandwidth, input/output impedance and overload behavior can all matter. A circuit could produce the expected logical result under one input condition but fail when the supply changes or an output is overloaded.

[Analog and Digital Signals](analog-and-digital-signals.md) owns the distinction between signal representation types. [Matter and Energy](matter-and-energy.md) owns the physical energy balance, and [Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns general interaction contracts.

## Worked example: ideal half-wave rectification

Consider an **ideal diode model**, an ideal alternating input voltage, and a resistive load with a suitable return path. Assume the diode conducts without voltage drop for the positive polarity and blocks all current for the reverse polarity.

| Input voltage | Ideal diode state | Load voltage |
| ---: | --- | ---: |
| +5 V | Conducting | +5 V |
| 0 V | Boundary / zero applied drive | 0 V |
| −5 V | Blocking | 0 V |

The arrangement can be represented by `v_out(t) = max(0, v_in(t))` for the specified reference orientation and ideal model. It **does not** mean a real semiconductor diode always turns on without a voltage drop or blocks without leakage. Real behavior depends on its I–V characteristics, temperature, reverse-voltage limits, source and load, and circuit arrangement.

If the load is an ideal 1 kΩ resistor, the +5 V condition gives `I = 5 V / 1000 Ω = 0.005 A = 5 mA` and `P = VI = 25 mW`. The −5 V condition carries zero load current **only in the ideal blocking model**.

The example demonstrates a nonlinear transfer mechanism; it does not instruct the assembly or testing of mains-connected equipment.

## Amplification, switching and feedback are distinct

**Amplification** increases a selected signal measure under a specified gain model. Energy for the increased signal power comes from the circuit's power supply, not from creating energy. **Switching** selects or changes a conduction state based on inputs and operating conditions. A single transistor may serve in either role depending on its bias and circuit.

**Feedback** can regulate amplifier gain, linearity, distortion or stability under a particular closed-loop model. Its correctness is not assured by the mere presence of a loop. [Feedback and Control](../systems-engineering/feedback-and-control.md) owns the general theory of regulation and closed-loop behavior.

## Electronics versus system organization

A board's microcontroller, power stage and sensor inputs may all contain electronic circuits, yet their system responsibilities differ. An electrical schematic shows chosen connectivity; a logical diagram shows intended information transformations; a firmware interface defines software-visible behavior. None substitutes completely for the others.

[Computing Components](../digital-systems-hardware/computing-components.md) owns hardware subsystem roles. [Sensors and Actuators](README.md) is a separate approved physical subject reserved for transduction and action mechanisms. Electronics does not establish a new hardware architecture, vendor preference, or compliance standard.

### Sources

- [MIT OpenCourseWare: Computation Structures, CMOS and Digital Abstraction](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [OpenStax University Physics Volume 3: Semiconductor Devices](https://openstax.org/books/university-physics-volume-3/pages/9-7-semiconductor-devices).
- [OpenStax University Physics Volume 2: Resistors in Series and Parallel](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel).

**Editorial status:** Substantive Draft. The idealized rectifier example and semiconductor generalizations require a scoped independent second-pass technical review. No learner assessments, wiring instructions, or new subject categories are introduced.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
