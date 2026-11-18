# Temporal Concepts and Models

**Knowledge area:** [Models & Abstraction](README.md)  
**Subject ID:** F-03-11  
**Development status:** Reviewed (model-assisted; independent human acceptance not claimed)  
**Source review:** Core claims checked; [Wave F 42-family scoped technical audit](../WAVE-F-TECHNICAL-REVIEW-01.md); comprehensive source-level verification not claimed  
**Inventory authority:** [Model and Architecture Adjudication 01](../FUNDAMENTAL-MODEL-ARCHITECTURE-ADJUDICATION-01.md)

## Time and temporal representation are not the same thing

**Temporality** concerns the temporal properties and relationships of occurrences, conditions and changes, including **instants, intervals, durations, succession, order, concurrency, and persistence**. A **temporal model** specifies how some of those concepts are represented and what inferences the representation permits. It does not prove which temporal theory completely describes physical reality.

An event may occur in the world, may become observable, may be observed, and may later be recorded with a timestamp. Those are distinct occurrences and times. A timestamp is **data produced under a clock and recording convention**, not the event itself or an unconditionally accurate report of the time it occurred.

[State, Events, and Transitions](state-events-and-transitions.md) owns the general meaning of conditions, occurrences and modeled changes. This article owns the **general temporal vocabulary and relationships**. [Units and Quantities](../mathematics-logic/units-and-quantities.md) owns time as a measurable quantity; [Timing and Clocks](../digital-systems-hardware/timing-and-clocks.md) owns mechanisms that represent or measure it.

## Instants, intervals and durations

An **instant** is a location in an adopted time model; a **duration** is a measure or amount of elapsed time between specified temporal positions under a chosen time scale. An **interval** is a temporal extent represented by start and end bounds and a convention for including or excluding endpoints. A civil-date string, a point on a monotonic clock, and an abstract instant are not the same data type.

In a linearly ordered numerical model, an interval can be represented as `[a,b)`, meaning `a≤t<b`. This **half-open interval** includes its start and excludes its end. For numeric instants measured in seconds on the same consistent scale, its length is `b−a`. That arithmetic does not automatically establish the observed elapsed duration of a process if the numbers came from unsynchronized or non-monotonic clock sources.

Half-open intervals are convenient because adjacent intervals `[a,b)` and `[b,c)` share no included instant, even though they meet at a boundary. Other models may use closed, open, or unbounded intervals. Endpoint conventions must be explicit.

## Temporal order need not be total

A **total order** compares every pair of distinct elements. A **partial order** is reflexive, antisymmetric and transitive, but may leave some pairs incomparable. For strict orders, irreflexivity replaces reflexivity and distinct events may remain incomparable.

In distributed systems, the **happened-before** relation is typically a strict *partial order* based on local event order, message transmission/receipt and transitivity. Two events can be concurrent in this causal-order model, meaning neither is established as preceding the other. Concurrency does not mean that their physical times are identical.

**Physical time**, **recorded time**, **logical time** and **causal order** are different conceptual commitments. [Synchronization and Coordination](../communication-distributed-systems/synchronization-and-coordination.md) owns particular distributed clock and consensus mechanisms; general ordering stays here.

## Interval relations and temporal reasoning

Temporal relationships between intervals include **before**, **meets**, **overlaps**, **during**, **starts**, **finishes** and **equals**, plus the inverses of the asymmetric relationships. In Allen's interval algebra, a set of thirteen basic relations describes how two proper intervals with distinct start/end instants can be related under a linear time model. This is one representation, not a claim that every physical or computational process must use exactly these categories.

For example, in an abstract time scale:

```text
A = [10, 20)
B = [15, 25)
A ∩ B = [15, 20)
```

The intervals overlap on `[15,20)`, a five-unit extent, and neither contains the other. That result assumes a common ordered coordinate system and consistent units. If the bounds were read from unrelated, inaccurate clocks, a comparison of the recorded numbers would not by itself establish a genuine temporal overlap.

Models of event histories may additionally distinguish **event time** (the time assigned to the occurrence), **observation or ingestion time**, and **processing or record time**. The assignment rules vary by system and must be documented rather than inferred from generic column names.

## Clocks, timestamps and uncertainty

A **clock** maps physical or modeled progression to a reading. A **timestamp** associates a record with a represented time under a clock, time scale, epoch, calendar and formatting convention. Its precision (number of representable digits or units) is distinct from its accuracy, offset, synchronization uncertainty and delay.

Civil time must account for time zones and calendar rules; a formatted local timestamp without an offset or zone may be ambiguous across clock changes. For measuring elapsed durations in software, a monotonic clock is generally preferable to a civil wall-clock reading that can be adjusted or discontinuously changed. Even a monotonic clock has resolution, rate and implementation limitations.

An apparently high-resolution timestamp is not evidence of nanosecond accuracy. The sensing path, transport, buffering, queuing and recording mechanism can delay or perturb the time assigned to the original event.

## Worked example: apparent timestamp reversal

Assume device A sends a message and device B subsequently receives that same message. The causal relation is **send-before-receive**. Yet imagine the following recorded wall-clock values:

```text
Event                 Recorded clock reading
A sends               12:00:00.200
B receives            12:00:00.150
```

The receiver's recorded reading is **50 milliseconds earlier** than the sender's. This is not evidence that the message arrived before it was sent. The clock readings could be offset, or a record could have been delayed or incorrectly assigned a timestamp. To explain the difference, one would need synchronized-clock evidence, event-identification evidence and the recording semantics.

If a model guarantees that these are a matched send and receive, their **causal** ordering holds even though the raw readings sort in the opposite order. If we only see two uncorrelated records, even the matching send/receive interpretation is an inference, not an established fact.

## Temporal models, state and persistence

A system's state may be described as of an **instant**, across an **interval**, or as a sequence of events that update selected variables. **Temporal validity** (when a statement should be regarded as true in the modeled world) differs from **recording time** (when a database learned or stored it). The distinction matters in retrospective analysis, configuration histories and systems that receive late information.

A formal transition system can express legal sequences without specifying how much real time passes between transitions. Timed automata, temporal logic and hybrid dynamical systems add distinct clocks, constraints or time-dependent behavior. This article does not replace those specific formalisms.

## Canonical boundaries and sources

- [State, Events, and Transitions](state-events-and-transitions.md) owns change semantics, event/state distinctions and transition rules.
- [Measurement](../scientific-analytical-reasoning/measurement.md) owns measured quantities and uncertainty; [Units and Quantities](../mathematics-logic/units-and-quantities.md) owns dimensional units.
- [Timing and Clocks](../digital-systems-hardware/timing-and-clocks.md) owns hardware timing mechanisms, rather than the abstract temporal theory.
- [Synchronization and Coordination](../communication-distributed-systems/synchronization-and-coordination.md) owns distributed coordination and logical-clock implementations.
- [Data Provenance and Lifecycle](../information-data/data-provenance-and-lifecycle.md) owns source and transformation histories in records.

### Primary reference starting points

- [Allen, Maintaining Knowledge About Temporal Intervals (1983)](https://doi.org/10.1145/182.358434), interval-algebra formalism and temporal constraint reasoning.
- [Lamport, Time, Clocks, and the Ordering of Events in a Distributed System (1978)](https://lamport.org/pubs/time-clocks.pdf), causal event ordering, logical clocks and their distinction from physical clocks.
- [BIPM International System of Units](https://www.bipm.org/en/measurement-units/), time as a measured physical quantity.
- [NIST Time and Frequency Division](https://www.nist.gov/pml/time-and-frequency-division), physical timekeeping and clock-system references.

A chosen time scale and data model determine which interval/order calculations are meaningful. This article does not settle the philosophy or physics of time, nor establish operational timestamp accuracy in any deployed system.

**Editorial status:** Reviewed (model-assisted) under the [Wave F scoped technical review](../WAVE-F-TECHNICAL-REVIEW-01.md). Full source-passage verification, independent expert review and final publication acceptance remain open.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
