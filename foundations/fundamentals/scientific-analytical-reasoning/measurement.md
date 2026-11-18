# Measurement

**Knowledge area:** [Scientific & Analytical Reasoning](README.md)  
**Approved subject heading:** Measurement  
**Development status:** Reviewed (model-assisted; not independently human-accepted)  
**Source review:** Core claims checked in [Wave A Technical Review, Batch 02](../WAVE-A-TECHNICAL-REVIEW-02.md); full independent validation not claimed

## Measurement connects quantities to defensible values

A **measurement** is an experimental process of obtaining one or more quantity values reasonably attributable to a quantity. This definition follows the [International Vocabulary of Metrology (VIM 2.1)](https://jcgm.bipm.org/vim/en/2.1.html). The key point is that a number displayed by an instrument is not automatically a complete measurement result.

A measurement requires a sufficiently specified **measurand**, an intended quantity to be measured, a procedure and suitable conditions. The intended quantity might be the length of a particular rod at a specified temperature, an electrical potential difference under a defined load, or the temperature of a selected material at a particular location and time.

Specifying *which* quantity is being measured determines the meaning of the outcome. The phrase “the temperature was 25 °C” is incomplete if the relevant question concerns different locations, intervals, devices, surfaces, or quantities.

The [VIM 2.3 definition of measurand](https://jcgm.bipm.org/vim/en/2.3.html) explicitly calls attention to the description of the property and the phenomenon carrying it.

## A measurement procedure has several interdependent parts

A useful analytical decomposition includes:

| Element | Function |
| --- | --- |
| **Measurand** | The quantity intended to be measured |
| **Measurement method** | The general physical or computational principle used |
| **Measurement procedure** | Specific operations, instruments, conditions and calculation steps |
| **Measurement system** | Instruments, standards, sensors and associated apparatus |
| **Calibration and reference** | Establishes relationships between indications and quantity values under conditions |
| **Measurement result** | Estimated quantity value(s) and relevant contextual information |
| **Measurement uncertainty** | Quantifies dispersion of quantity values attributed to the measurand |

These terms are not interchangeable. The list is a **reference-oriented explanation**, not an assertion that every measurement requires exactly seven software fields.

For example, a thermistor may change electrical resistance with temperature. The electrical response is a physical transduction mechanism. Interpreting the response as temperature requires a model or calibration and a sufficiently specified measurand. Those distinct mechanisms belong respectively in [Physical & Electrical Principles](../physical-electrical-principles/README.md) and this measurement reference.

## Indication, measured value, and result

An instrument may display an **indication**, such as `8.3 cm`. The display is a representation, not by itself a complete account of the measurand or measurement quality.

A **measured quantity value** is a quantity value representing a measurement result. The [VIM 2.10 entry](https://jcgm.bipm.org/vim/en/2.10.html) warns that the everyday phrase *measured value* can be confused with the instrument indication.

A **measurement result** may include a representative measured quantity value, uncertainty and other information about conditions and interpretation. The [VIM 2.9 definition](https://jcgm.bipm.org/vim/en/2.9.html) emphasizes the set of values attributed to the measurand and relevant information.

A result such as `(8.3 ± 0.5) cm` is incomplete if the meaning of the `±` term is not stated. It might represent a standard uncertainty, an expanded uncertainty with a coverage factor, a tolerance, or some other quantity. Those are fundamentally different claims.

## Accuracy, precision, uncertainty, and error

In measurement science, **accuracy** describes closeness of agreement between a measured quantity value and a true quantity value of the measurand. It is a qualitative concept in VIM and should not automatically be replaced by one numerical “accuracy percentage.”

**Precision** concerns closeness of agreement between indications or measured quantity values obtained by replicate measurements under specified conditions. Repeatability and reproducibility are distinct types of precision conditions.

**Measurement uncertainty** is a non-negative parameter characterizing dispersion of quantity values attributed to the measurand, based on the information used. It is not simply the amount by which a particular reading is wrong.

**Error** is a measured value minus a reference quantity value under a chosen convention; systematic and random errors involve different mechanisms.

NIST's [Measurement Uncertainty guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) and the VIM distinguish these concepts. They should not be merged with *numerical precision* of a floating-point representation, which concerns a different kind of representational limitation.

A measuring instrument can be precise but biased, giving tightly clustered values offset from a suitable reference. Another can be less repeatable but approximately centered on a reference. A set of close readings does not by itself establish that a result is accurate.

## Calibration and metrological traceability

**Calibration** establishes, under specified conditions, a relationship between values given by measurement standards and corresponding indications, including their uncertainties, then uses that information to establish a relationship for obtaining a measurement result from an indication. Calibration is not the same as simply changing an instrument setting to eliminate an offset.

**Metrological traceability** is a **property of the measurement result**: it can be related to an appropriate reference through a documented unbroken chain of calibrations, with each contributing to uncertainty. It is not merely a property bestowed on an instrument because it carries a sticker. The [VIM 2.41 definition](https://jcgm.bipm.org/vim/en/2.41.html) also cautions that traceability alone does not guarantee adequate uncertainty or absence of mistakes.

NIST's [Metrological Traceability policy and FAQ](https://www.nist.gov/metrology/metrological-traceability) explicitly emphasizes this distinction. A measurement can depend upon conditions, methods, references and uncertainty even when the instrument was calibrated previously.

## JCGM GUM: evaluating and combining measurement uncertainty

The [Guide to the Expression of Uncertainty in Measurement (GUM), JCGM 100:2008](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e) is an established framework for expressing uncertainty in **measurement results**, not simply reporting an instrument's display precision. The JCGM publication suite includes [GUM-6:2020](https://www.bipm.org/en/doi/10.59161/JCGMGUM-6-2020) on measurement models and a **2026 amendment to JCGM 100** addressing nonlinearity in measurement models. Authors must identify which version and approximation they are using.

A **measurement model** relates an output measurand Y to input quantities X₁,…,Xₙ under a chosen model, often written Y=f(X₁,…,Xₙ). Each input has a value estimate and associated uncertainty. The GUM distinguishes **Type A evaluation**, commonly based on statistical analysis of observations, from **Type B evaluation**, based on other information such as calibration certificates, manufacturer specifications or prior data. A/B is a distinction between **evaluation methods**, not a separation into random versus systematic error types.

For sufficiently regular functions and appropriate first-order propagation assumptions, the output **combined standard uncertainty** depends on input standard uncertainties and their covariance. For a linear sum Y=X+Z, the exact variance under ordinary finite-variance random-variable modeling is

Var(Y) = Var(X) + Var(Z) + 2 Cov(X,Z).

When estimates are appropriately modeled with uncorrelated input uncertainties, this reduces to uᶜ(Y)=√[u(X)²+u(Z)²]. Correlations cannot be ignored when sharing calibration references, sensors or common physical effects.

**Worked illustration:** Two input estimates are 10.0 and 4.0 units, each with standard uncertainties 0.2 and 0.3 units, assumed uncorrelated. The sum is **14.0 units**, and the combined standard uncertainty is **√(0.2²+0.3²)=√0.13≈0.3606 units**. Adding the uncertainties directly would describe a different model or bound. A reported expanded uncertainty U=k·uᶜ requires a justified coverage factor and probability distribution assumptions. It is not automatically a 95% guarantee.

**Interpretation:** A numerical uncertainty budget concerns a specified **measurand, model and measurement procedure**. It does not prove the sensor's readings are authentic, the instrument has no bias, or the physical process is stable. A conformity decision near a threshold requires a separate declared decision rule, not merely a central reading exceeding the limit.

## An explanatory threshold example

Suppose a properly specified liquid-level measurement reports a representative value `8.3 cm`, with an associated interval from `7.8 cm` to `8.8 cm` under stated uncertainty conventions. The operational threshold is `8.0 cm`.

The representative value exceeds the threshold, but the stated interval includes values **below and above** the threshold. Without a decision rule, probability model, or additional observations, it would be unjustified to claim that the measurand is certainly above the threshold.

By contrast, a raw indication of `8.3` without stated units, calibration, uncertainty or subject does not even identify a comparable measurand adequately.

The interval is a **hypothetical illustration**, not a universal confidence interval or proof of a particular coverage probability. Measurements, estimated uncertainty intervals and decisions about risk need explicit assumptions.

## Measurement versus observation and evidence

An **observation** may be qualitative, such as noticing a color change. A **measurement** is a specific quantitative activity producing values reasonably attributable to a quantity. A **record** is a representation of a measurement or other event. **Evidence** concerns the information's relationship to a particular claim.

These concepts can participate in a workflow without being synonymous:

```text
Selected measurand and procedure
         ↓
Observation / instrument indications
         ↓
Calibration, calculation and evaluation
         ↓
Measurement result with uncertainty
         ↓
Possible evidence for a specified claim
```

The figure is an explanatory possibility. A measurement may involve multiple instruments, computed models and correlated variables; information can serve as evidence without itself being a measurement. A record of a result can also omit critical conditions.

An instrument that samples once per second cannot, from a single sample, generally establish the exact time of a threshold crossing between samples. This limitation connects to [Observation](observation.md), [Evidence](evidence.md), and the still-open general-temporality coverage question [G-04](../COVERAGE-GAP-DECISIONS.md).

## Relationships across Fundamentals

[Numbers and Numerical Systems](../mathematics-logic/numbers-and-numerical-systems.md) explains numerical representations; [Units and Quantities](../mathematics-logic/README.md) covers dimensional expression; [Probability and Statistics](../mathematics-logic/README.md) supplies mathematical distributions; [Sensors and Actuators](../physical-electrical-principles/README.md) covers physical transduction. [Data Provenance and Lifecycle](../information-data/README.md) covers record history.

## Authoritative reference starting points

- [JCGM 100:2008, Guide to the Expression of Uncertainty in Measurement](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e).
- [JCGM publications, including the 2026 nonlinearity amendment and GUM suite](https://www.bipm.org/en/committees/jc/jcgm/publications).
- [JCGM GUM-6:2020, Developing and Using Measurement Models](https://www.bipm.org/en/doi/10.59161/JCGMGUM-6-2020).


- [JCGM VIM 2.1: Measurement](https://jcgm.bipm.org/vim/en/2.1.html).
- [JCGM VIM 2.3: Measurand](https://jcgm.bipm.org/vim/en/2.3.html).
- [JCGM VIM 2.9: Measurement Result](https://jcgm.bipm.org/vim/en/2.9.html).
- [JCGM VIM 2.10: Measured Quantity Value](https://jcgm.bipm.org/vim/en/2.10.html).
- [JCGM VIM 2.13: Measurement Accuracy](https://jcgm.bipm.org/vim/en/2.13.html).
- [JCGM VIM 2.15: Measurement Precision](https://jcgm.bipm.org/vim/en/2.15.html).
- [JCGM VIM 2.26: Measurement Uncertainty](https://jcgm.bipm.org/vim/en/2.26.html).
- [JCGM VIM 2.39: Calibration](https://jcgm.bipm.org/vim/en/2.39.html).
- [JCGM VIM 2.41: Metrological Traceability](https://jcgm.bipm.org/vim/en/2.41.html).
- [NIST: Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty).
- [NIST: Metrological Traceability](https://www.nist.gov/metrology/metrological-traceability).

**Review record:** Core terms were cross-checked against VIM3 entries for measurement, measurand, result, accuracy, precision, uncertainty, calibration and traceability. The threshold example was checked for the stated logical comparison and is explicitly hypothetical, not a confidence/coverage guarantee. This article passed the scoped model-assisted review described in the Wave A Batch 02 audit; it has not undergone independent human acceptance.

[Scientific & Analytical Reasoning](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
