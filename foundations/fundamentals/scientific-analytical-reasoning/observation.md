# Observation

**Knowledge area:** [Scientific & Analytical Reasoning](README.md)  
**Approved subject heading:** Observation  
**Development status:** Draft  
**Source review:** Core claims checked (see [pilot technical review](../PILOT-TECHNICAL-REVIEW.md)); final editorial acceptance pending

## How something becomes observable

**Observation** is the acquisition or recognition of information about a phenomenon, entity, event, or condition by an observer or an observing system. It is an encounter with a selected aspect of something, not a complete or infallible copy of reality.

Observation may be **direct** through the human senses or **instrument-mediated** through sensors or scientific instruments. Inspecting an existing record is a **secondary observation of the record**, not a fresh direct observation of the original event. The same event may generate several observations at different granularities, and different observers may attend to different aspects of it.

A camera can register changes in illumination; a temperature probe responds to a physical property; a computer can record messages it receives. Each observes through a particular mechanism and within an observable range. None automatically captures every relevant property of the observed subject.

This is why the questions *what was observed?*, *how?*, *from where?*, and *under what limitations?* are fundamental to reasoning.

## The anatomy of an observation

A useful conceptual decomposition identifies several distinct elements:

| Element | Role |
| --- | --- |
| **Subject or phenomenon** | What the observation concerns |
| **Observer** | Person, instrument, or system collecting an indication |
| **Observation mechanism** | Sensing, acquisition, inspection, recording, or other means |
| **Selection and scope** | What is visible, sampled, included, and excluded |
| **Context** | Conditions, place, time representation, configuration, and assumptions |
| **Observation result** | An indication, report, value, signal, image, or record |
| **Limitations** | Noise, loss, coverage gaps, bias, uncertainty, and possible errors |

These are **explanatory facets**, not a newly ratified schema or ontology for all observations. Real procedures can combine or subdivide them.

For example, a device measuring temperature may have a thermistor as part of its mechanism. Its output depends on the sensor's physical behavior, calibration, sampling, the thermal contact with the subject, and ambient influences. The number displayed by the device is an indication under those conditions, not a universally complete statement about the subject.

## Observation, measurement, record, and evidence

These four terms should not be collapsed.

**Observation** concerns acquiring or noticing information about a phenomenon.

**Measurement** is a more specific experimental process that determines one or more quantity values reasonably attributable to a specified measurand. Its interpretation depends on a procedure, reference and uncertainty. An observation may be qualitative and need not constitute a measurement. NIST's [measurement uncertainty guidance](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) explains the role of the measured quantity, reference, and instrument.

**Record** is a representation of an observation or some other occurrence. It might contain a timestamp, value, code, image, or description. Records can omit context or be transformed after acquisition. Their structure and provenance belong under [Information & Data](../information-data/README.md).

**Evidence** is information considered in relation to a claim. An observation or record may be used as evidence, but its relevance and strength depend on the question, conditions, reliability, and reasoning. A recorded occurrence does not validate any particular interpretation by itself.

The relationship can be illustrated without equating the concepts:

```text
Phenomenon
    |
  observed through a mechanism
    v
Observation result
    |
  may be represented as
    v
Record
    |
  interpreted in relation to a claim
    v
Potential evidence
```

This is a possible reasoning path, not a mandatory processing pipeline. Some evidence is not observational; observations can be retained without being used to support a particular claim.

## Observation is selective and mediated

Observations have limits even when their instruments function correctly. A sample excludes unobserved points; a sensor only responds within certain conditions; a model can influence which phenomena are selected or recognized.

For instance, a system that checks a process every 60 seconds cannot generally determine whether an event occurring and ending between two samples happened, unless another mechanism recorded it. Increasing the sampling rate may improve temporal coverage, but it does not remove every bias or instrument limitation.

The philosophy of science calls attention to the influence of concepts, assumptions, and instruments upon the production and interpretation of empirical results. The [Stanford Encyclopedia of Philosophy's discussion of theory and observation](https://plato.stanford.edu/entries/science-theory-observation/) treats this as a substantive issue, not a reason to dismiss observations entirely.

The disciplined response is to make the mechanism, assumptions, and uncertainties inspectable.

## Worked illustration: an observed threshold crossing

Consider a hypothetical sensor sampling a liquid level once per second and reporting a value above a configured threshold. An observation record might contain:

```text
observed_at: 12:00:04
sensor_id: S-17
level_reading: 8.3
unit: cm
threshold: 8.0
```

Assuming the sensor and timestamp reporting behave as specified, the record indicates that the **reported sampled value** was above the configured threshold. It does **not**, without earlier observations or other evidence, establish that a crossing actually occurred during the observed interval, when any crossing took place, whether the reading was calibrated, why the level changed, or whether the subject was physically unsafe.

An investigator could later compare other sensor values or measurements, but those subsequent calculations and interpretations are not themselves identical to the initial observation.

## Cross-cutting relationships

[Measurement](README.md) supplies quantitative procedures; [Evidence](README.md) addresses support for claims; [Sensors and actuators](../physical-electrical-principles/README.md) and [Signal conversion](../physical-electrical-principles/README.md) explain physical acquisition; [Data provenance and lifecycle](../information-data/README.md) explains a record's history; [State, events, and transitions](../models-abstraction/README.md) explains modeled conditions and occurrences.

All links above point to approved area indexes because most individual canonical articles are not yet written. A directory location is a navigation choice, not a claim of ontological parentage.

## References and verification status

- [Stanford Encyclopedia of Philosophy: Theory and Observation in Science](https://plato.stanford.edu/entries/science-theory-observation/), substantive revision January 2026, on theory, observational instruments, and empirical evidence.
- [NIST: Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty), for the measurement process and its limitations.
- [Stanford Encyclopedia of Philosophy: Evidence](https://plato.stanford.edu/entries/evidence/), for the distinction between observations and their epistemic support.

**Review record:** The distinction between observation, measurement, record, and evidence was checked against the cited philosophy-of-science and NIST resources. The seven explanatory facets are an original editorial decomposition, **not** a standardized ontology. The sampling example has been corrected so a threshold reading is not mistaken for evidence of a crossing. This remains a source-checked draft pending final editorial acceptance.

[Scientific & Analytical Reasoning](README.md) · [Fundamentals](../README.md) · [Concept boundary decisions](../CONCEPT-BOUNDARY-DECISIONS.md)
