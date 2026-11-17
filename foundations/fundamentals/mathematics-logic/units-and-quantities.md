# Units and Quantities

**Knowledge area:** [Mathematics & Logic](README.md)  
**Approved subject heading:** Units and quantities  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Quantities express magnitudes of specified kinds

A **quantity** is a property of a phenomenon, body, or substance whose magnitude can be expressed as a number and a reference. A reference may be a measurement unit, a measurement procedure, a reference material, or a combination. The **quantity value** is the number and reference used to express that magnitude: for example, `5 m` denotes a value of length, while the number `5` by itself does not specify a length.

A **unit** is a conventionally defined and adopted reference with which other quantities of the same kind can be compared to express their ratios as numbers. A **quantity kind** describes what may be meaningfully compared: length and width are quantities of the same kind; length and mass are not. A **dimension** instead expresses dependence on base quantities in a chosen system. Different kinds of quantities can share a dimension: energy and torque both have dimension `M L² T⁻²`, but are not generally interchangeable physical concepts.

The [International Vocabulary of Metrology (VIM)](https://jcgm.bipm.org/vim/en/) separates quantity, quantity value, quantity kind, system of quantities, unit, and dimension. The [SI Brochure](https://www.bipm.org/en/publications/si-brochure) defines the International System of Units, including accepted conventions for unit symbols and prefixes.

## Dimension, unit, and representation are different

A physical dimension indicates the algebraic structure of a kind of quantity, not its particular unit. A unit supplies a comparison reference; the number is the magnitude expressed relative to that reference.

| Statement | Interpretation |
| --- | --- |
| `2 m` | A length quantity value with unit metre |
| `200 cm` | The same length expressed in a different unit |
| `2` | A number; the physical quantity kind is unspecified |
| `2 m/s` | A speed quantity value with derived unit |
| `2 m/s²` | An acceleration quantity value; it is not speed |

In a quantity calculus, speed may be expressed as `v = d/t`, with dimension `L T⁻¹`. If distance is `120 m` and elapsed duration is `30 s`, the average speed is `4 m/s`. The numerical calculation and dimensional calculation must both be valid.

**Dimensionless** does not mean meaningless or necessarily unit-free in every communicative sense. Plane angle, ratios, refractive index, and a count can be dimension one under the SI system but retain different kinds, conventional units, or contextual semantics.

## SI units, derived units, and prefixes

The SI defines seven base units: second (s), metre (m), kilogram (kg), ampere (A), kelvin (K), mole (mol), and candela (cd). Other SI units are products of powers of base units. For example, the coherent SI unit of force is the newton, `N = kg·m·s⁻²`.

Prefixes multiply units by defined powers of ten: `1 km = 1000 m`; `1 ms = 0.001 s`. Prefix symbol case matters. The [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure) is the normative source for SI spelling and symbols.

Computing contexts also use binary prefixes, defined separately: `1 KiB = 1024 bytes` whereas `1 kB = 1000 bytes` under SI-prefix usage. A **byte** is conventionally eight bits in contemporary computing standards, but the size and encoding meaning of a data representation must be defined in its own context. The [NIST binary prefixes reference](https://physics.nist.gov/cuu/Units/binary.html) discusses the distinct prefixes.

## Conversions must preserve the quantity

A unit conversion reexpresses the same quantity value by applying a valid relation between units. For multiplicative conversions:

```text
2.5 km × (1000 m / 1 km) = 2500 m
72 km/h × (1000 m / 1 km) × (1 h / 3600 s) = 20 m/s
```

Temperature requires particular care. Temperature **values** on the Celsius and Kelvin scales obey `t/°C = T/K − 273.15`, while temperature **intervals** have the same magnitude in °C and K. Thus 20 °C equals 293.15 K, but a temperature increase of 20 °C corresponds to an increase of 20 K, not 293.15 K. Neither a bare multiplication rule nor a naive cancellation of units captures every affine-scale conversion.

Logarithmic levels, calendar units with varying durations, currencies, and other conventional or contextual references may require additional definitions, not simply a scalar factor. Their semantics must be established before converting.

## Dimensional analysis: necessary but not sufficient

An equation asserting equality of physical quantities normally requires dimensional consistency. For example, `distance = speed × duration` has dimensions `L = (L T⁻¹) × T`. By contrast, adding `5 m + 3 s` is not a meaningful physical sum in ordinary quantity calculus.

Dimensional consistency **does not prove an equation is physically correct**. Both `d = v t` and `d = 2 v t` have consistent dimensions; only appropriate definitions, evidence, and assumptions can justify one for a given model. Dimension analysis also does not by itself distinguish all quantity kinds sharing dimensions.

## Accuracy, precision, resolution, and uncertainty

The number of printed digits does not establish measurement accuracy. Instrument resolution, uncertainty, significant digits, calibration and method limitations must be considered as measurement issues. If `L = 2.000 m` is reported, the trailing zeros communicate formatting or claimed precision only within a stated recording convention. They are not evidence of a trustworthy uncertainty budget.

[Measurement](../scientific-analytical-reasoning/measurement.md) owns measurement procedures, calibration and metrological uncertainty. [Numbers and Numerical Systems](numbers-and-numerical-systems.md) owns arithmetic and numeric representation. [Schemas](../models-abstraction/schemas.md) owns declared constraints on recorded units and values.

## Computational representations and unit safety

Storing `speed: 20` without documenting `m/s` or `km/h` leaves an ambiguity. A system may preserve quantity semantics by recording units explicitly, enforcing typed quantity interfaces, or making units part of a well-documented schema. These mechanisms reduce certain errors but do not prove the underlying measurement or sensor is correct.

Consider two records: `{value: 20, unit: "m/s"}` and `{value: 72, unit: "km/h"}`. Under the stipulated conversion, both encode equal speed values. Comparing raw numeric fields alone would produce a false distinction.

## Boundaries and applications

Quantity calculus is domain-independent. It underpins physical sensing, engineering design, computing capacity, network rates, environmental measurements, and data reporting. Time **as a measured duration** and SI unit belongs here; the more general question of temporality, ordering, simultaneity, or modeled event time remains open under [G-04](../COVERAGE-GAP-DECISIONS.md#g-04-time-temporality-clocks).

### Sources

- [BIPM, The International System of Units (SI Brochure)](https://www.bipm.org/en/publications/si-brochure).
- [JCGM, International Vocabulary of Metrology](https://jcgm.bipm.org/vim/en/).
- [NIST, Binary Prefixes](https://physics.nist.gov/cuu/Units/binary.html).
- [NIST, Guide for the Use of the International System of Units](https://physics.nist.gov/cuu/pdf/sp811.pdf).

**Editorial status:** Substantive draft; examples are explanatory calculations requiring a separate scoped technical and source audit before Reviewed status. G-01 and G-04 decisions are unchanged.

[Mathematics & Logic](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
