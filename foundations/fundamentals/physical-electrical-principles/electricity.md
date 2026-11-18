# Electricity

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Electricity  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave C Batch 01 technical audit](../WAVE-C-TECHNICAL-REVIEW-01.md); independent human review pending

## Electrical phenomena concern charges and fields

**Electric charge** is a physical property involved in electromagnetic interactions. **Electric current** measures the rate at which charge flows across a defined surface. **Electric potential difference** expresses energy transferred or work per unit charge between locations in the relevant electrical model. These are distinct physical quantities, even when a device display shows only one of them.

The SI unit of electric charge is the **coulomb (C)**, current is the **ampere (A)** and potential difference is the **volt (V)**. `1 A = 1 C/s` and `1 V = 1 J/C`. Real conductors and components exhibit physical phenomena that require considering material properties, geometry and operating conditions.

[OpenStax University Physics Volume 2](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance) explains how potential difference and material resistivity relate to conduction. [Units and Quantities](../mathematics-logic/units-and-quantities.md) owns general dimensional reasoning rather than all electric mechanisms.

## Current, charge and direction

For a time-dependent model, current can be expressed as

```text
I = dQ/dt
```

where `Q` is the net charge transferred across a defined surface. When current is constant over an interval, `I = ΔQ / Δt`.

If `2 C` of net charge cross the defined surface during `4 s` at a constant rate, the current magnitude is `0.5 A`. The calculation alone does not identify which charge carriers moved or their microscopic velocities.

**Conventional current direction** follows the direction a positive charge would move. In metallic conductors, charge transport commonly involves electrons moving in the opposite direction. Electrical signal propagation and individual carrier drift speed are also different phenomena. [OpenStax: Model of Conduction in Metals](https://openstax.org/books/university-physics-volume-2/pages/9-2-model-of-conduction-in-metals) explains this distinction.

## Potential difference, resistance and Ohm's relation

A potential difference can drive electrical current in a conductive arrangement, but current also depends on the material and configuration. **Resistance** expresses opposition to current in a specified relation or operating regime, while **resistivity** describes a material's properties under defined conditions.

For an **ohmic element** with constant resistance in the stated operating range:

```text
V = I R
```

where `R` is in ohms (Ω), `V` in volts and `I` in amperes. This is a model relationship, **not** a universal assertion that all devices have constant resistance or linear current–voltage behavior. Diodes, transistors, lamps and many materials may respond nonlinearly or change resistance as conditions evolve.

A `6 Ω` ideal ohmic resistor with `12 V` applied across it has `I = 12/6 = 2 A` in this model. The result does not establish current through an unknown circuit containing other elements.

## Power and electrical energy

The instantaneous electrical power transferred at a two-terminal element can be expressed, under a consistent sign convention, as:

```text
p(t) = v(t) i(t)
```

The sign depends on the selected reference directions and whether the element absorbs or delivers energy. For steady positive voltage/current under the passive sign convention, `P = VI` is absorbed power. A `12 V` drop with `2 A` entering the positive-reference terminal corresponds to `24 W` absorbed.

For an ideal resistor in the stated model, `P = I²R = V²/R`. Power is an energy **rate**, while energy over time requires integrating power. A device drawing `24 W` for `5 s` under constant conditions transfers `120 J`.

These are analytic examples, not instructions for connecting real power sources. Real electrical systems have heating, insulation, current limits and other safety constraints.

## AC, DC and signal semantics

**Direct current (DC)** refers to a unidirectional current under an appropriate definition; **alternating current (AC)** involves reversal of direction or polarity with time. Constant DC and sinusoidal AC are common idealizations, not the only waveforms possible.

**Analog versus digital** instead concerns how signals represent values. An alternating waveform can carry analog or digitally encoded information, and a nominally DC-biased signal may have transitions or ripple. AC/DC and analog/digital therefore describe different properties and should not be used interchangeably.

[Analog and Digital Signals](README.md) is the approved subject for representation across continuous and discrete signal levels, while [Waves and Frequency](README.md) owns periodicity and propagation concepts when authored.

## Electrical fields, materials and system boundaries

Charge distributions create electric fields; moving charges and changing fields relate to magnetic effects and electromagnetic propagation. A simple lumped electrical model may ignore some spatial effects that become important at higher frequencies or particular geometries.

Ground potential, reference directions and current return paths depend on actual circuit architecture and environmental conditions. An electrical connection labeled `ground` does not guarantee zero potential difference between every point in a real system.

[Electrical Circuits](electrical-circuits.md) owns circuit connections and current/voltage constraints; [Electronics](README.md) will develop active devices and implementations. Detailed electrical safety practices are outside this conceptual reference.

### References

- [OpenStax: Resistivity and Resistance](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance).
- [OpenStax: Model of Conduction in Metals](https://openstax.org/books/university-physics-volume-2/pages/9-2-model-of-conduction-in-metals).
- [BIPM: SI Brochure](https://www.bipm.org/en/publications/si-brochure).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave C Batch 01 24-group audit](../WAVE-C-TECHNICAL-REVIEW-01.md). Complete source verification, independent human expert peer review and final publication acceptance remain outstanding.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
