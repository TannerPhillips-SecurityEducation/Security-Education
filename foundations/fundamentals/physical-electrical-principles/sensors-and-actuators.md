# Sensors and Actuators

**Knowledge area:** [Physical & Electrical Principles](README.md)  
**Approved subject heading:** Sensors and actuators  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave C Batch 03 audit](../WAVE-C-TECHNICAL-REVIEW-03.md); independent human review pending

## Connecting observable conditions with physical intervention

A **sensor** is a device or arrangement that responds to a measurand or physical condition and produces a usable indication or signal. An **actuator** receives an input or command and influences a physical process, for example by applying motion, force, heat, light, pressure, or another effect. Their roles can be combined in an instrument, but **observing a condition and changing it are different functions**.

The physical quantity being measured, the signal representing it, and a later interpreted numerical value must be distinguished. A temperature probe may produce an electrical signal from which a controller estimates temperature. The signal is not itself a proof of the environment's true temperature. Likewise, a controller issuing a heater command does not prove that heat was produced.

[Measurement](../scientific-analytical-reasoning/measurement.md) owns measurement procedures and uncertainty. [Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns general responsibilities and contracts. This article owns the physical sensing and actuation mechanisms at their interface with system behavior.

## Transduction and signal chains

A **transducer** converts one form of physical quantity or signal into another under a specified transfer relationship. Many sensors use transduction, such as converting displacement, pressure, light, or thermal effects to an electrical output. An actuator can perform conversion in the other direction, for example an electrical drive producing motion.

A sensing chain might be described as:

```text
Physical condition
  → sensing element
  → signal conditioning
  → conversion and representation
  → reported measurement
```

Every stage may introduce effects such as noise, drift, nonlinearity, finite response time, saturation, or quantization. The number of boxes in this diagram is illustrative, not a required component architecture. Some devices deliver a directly interpretable mechanical indication, while others produce complex digital records.

The [JCGM International Vocabulary of Metrology](https://jcgm.bipm.org/vim/en/) gives technical meanings to measurands, measuring instruments, sensitivity and measurement uncertainty. [Signal Conversion](signal-conversion.md) owns analog-to-digital and digital-to-analog conversion and their limits.

## Sensitivity, range, resolution, and accuracy

**Sensitivity** describes how a sensor indication changes with a relevant change in the input quantity under a specified model. **Range** is the set of input conditions for which specified behavior is intended. **Resolution** distinguishes how finely an output can represent or resolve changes. **Accuracy** and **measurement uncertainty** concern closeness and defensibility of measurement results, not simply the number of displayed digits.

For a linear model `y=a x+b`, the sensitivity is `a=dy/dx` in the modeled range. An actual device may have hysteresis, offset, drift, calibration error and temperature dependence, invalidating constant sensitivity outside the relevant conditions.

A sensor that reports to a thousandth of a degree is not necessarily accurate to a thousandth of a degree. A high sampling rate is also not the same as high physical accuracy.

## Worked example: a stipulated linear temperature sensor

Consider a *hypothetical* sensor with a linear transfer function over 0–100 °C:

```text
V_out = (0.05 V/°C) × T
```

At a true modeled temperature of 20 °C, the ideal output is `1.00 V`. If a reading is `1.05 V`, inverse conversion yields `21 °C` under the **ideal transfer function**. That computation does not establish whether the underlying temperature is 21 °C: offset, noise, calibration and wiring can influence the voltage.

Suppose a separate, stipulated signal perturbation of `+0.01 V` occurs at the sensor output, with no other errors. This corresponds to an apparent temperature change of `0.01/0.05=0.2 °C` under the idealized sensitivity. This is **error propagation within a toy model**, not an empirically measured uncertainty bound.

## Actuation, command, effect, and confirmation

An actuator's physical output depends on drive power, permitted motion, mechanical load, environment and device health. A motor can be commanded to rotate while mechanically jammed; a valve can be ordered closed while its position sensor or linkage is faulty. **Command accepted**, **actuation attempted**, **physical effect observed** and **desired process outcome achieved** are separate claims.

Actuators may have mechanical limits, thermal constraints, saturation, friction, dead zones and response delays. Their actual operation can affect human safety and system reliability; any implementation must be evaluated according to relevant engineering requirements rather than inferred from a schematic.

[State and Behavior](../systems-engineering/state-and-behavior.md) owns modeling of response to inputs. [Physical Control Mechanisms](physical-control-mechanisms.md) develops physical regulation, energy transfer and interventions in the plant.

## Observability, closed loops, and sensor limitations

Sensors can provide feedback for a control system, yet having a sensor does not guarantee that every internal state is observable. A temperature reading at one location may not describe the whole room. An actuator position measurement may not establish delivered force or successful end-to-end behavior.

Redundancy can help under particular independence and voting assumptions, but adding a second sensor can introduce disagreement, common-cause failure or calibration differences. Detection and diagnosis depend on the chosen sensing and system model.

This subject is foundational and does not mandate one sensor vendor, device category hierarchy, safety circuit or calibration interval.

### Sources

- [JCGM: International Vocabulary of Metrology](https://jcgm.bipm.org/vim/en/).
- [NIST: Engineering Metrology and Measurement](https://www.nist.gov/pml).
- [MIT OpenCourseWare: Analysis and Design of Feedback Control Systems](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/).
- [NASA: Interface Management](https://www.nasa.gov/reference/6-3-interface-management/).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave C Batch 03 54-family technical review](../WAVE-C-TECHNICAL-REVIEW-03.md). Full source verification, independent human peer review and final publication acceptance remain separate outstanding gates.

[Physical & Electrical Principles](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
