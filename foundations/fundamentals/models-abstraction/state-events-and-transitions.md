# State, Events, and Transitions

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** State, events, and transitions  
**Development status:** Draft  
**Source review:** References listed; scoped technical acceptance pending  
**Architectural boundary:** General temporality is still an open coverage question ([G-04](../COVERAGE-GAP-DECISIONS.md)); this article does not resolve it.

## Describing conditions and changes

A **state** describes the condition of a modeled entity or system through selected properties and their values within a specified context. An **event** represents an occurrence recognized by a model. A **transition** represents a modeled change from one state to another, potentially subject to a condition, trigger, action or rule.

These are related but not interchangeable. An entity can remain in the same modeled state while an event occurs. A discrete transition may abstract an underlying continuous physical process, algorithmic step, administrative change, or formal rule. Continuous-time behavior may instead require a differential, hybrid, or other dynamical model. What counts as a separate state depends on which properties the model has selected.

The [Systems Engineering Body of Knowledge discussion of State and Behavior](https://sebokwiki.org/wiki/Concepts_of_Systems_Thinking) uses attributes to describe system states and events in its system-of-interest context. Some formalisms define events specifically as state-changing occurrences; other models allow events that leave the *selected* state variables unchanged. This article provides an explicit **general modeling vocabulary**, not one universally prescribed formal event ontology.

## State is a model of a condition

Consider a simple device with the attributes `power_mode` and `temperature`:

```text
Device X
power_mode = OFF
temperature = 21.4 °C
```

This is a modeled state description under an assumed observation context. A different model might consider only `power_mode`, or also include `firmware_version`, `voltage` and `connection_status`. The fact that one model has fewer state variables does not imply the actual device has fewer properties.

In an abstract state machine, a **state space** is the collection of possible states. A state is often represented by an element `s ∈ S`. This description does not specify whether a state is physically stored, inferred from observations, or represented symbolically.

A finite-state model has a finite set of states, but a real system's relevant behavior might require continuous-valued or higher-dimensional variables. The **finite** character belongs to the chosen model, not automatically to the underlying world.

## An event represents an occurrence

An event might be described as a message arrival, button press, scheduled clock tick, threshold indication, or other occurrence. The model must specify what qualifies as an event and how it is recognized.

A statement such as `button_pressed` is a symbolic **event description**, not the physical button press itself. The record announcing that event is also distinct from the event and may be delayed or incomplete.

Some models are **event-triggered**, allowing events to select transitions. Others use continuous-time evolution, time-stepped updates, or other dynamics. Consequently, not every state transition is defined by an externally reported discrete event, and an event does not always produce a change in the selected modeled state.

The philosophical concept of an event is contested. The [Stanford Encyclopedia of Philosophy's Events article](https://plato.stanford.edu/entries/events/) discusses differences between events, processes, objects and changes. Here we use the *modeling* notion of an occurrence while avoiding claims of a universal metaphysical ontology.

## Transitions as relations and functions

Let `S = {OFF, ON}` be the states of a simplified device, and `I = {toggle, none}` the modeled inputs.

A deterministic next-state rule could be written:

```text
T(OFF, toggle) = ON
T(ON,  toggle) = OFF
T(OFF, none)   = OFF
T(ON,  none)   = ON
```

This is a **function** `T : S × I → S`. Under its assumptions, each state/input pair has exactly one next state. A more general transition **relation** might permit several possible next states or none, depending on the model.

This example illustrates three things:

- The input symbol *toggle* has a meaning defined by the model.
- The symbol *none* is an explicitly modeled no-action input and, under this rule, does not change the state.
- A transition rule describes permitted or prescribed behavior; it does not prove a physical device follows the rule.

The [MIT finite-state-machine notes](https://computationstructures.org/lectures/fsm/fsm.html) describe transition functions, current and next state, finite-state representations, and the distinction between Moore and Mealy output rules. Their clocked electronic implementation is one **contextual realization** of a general transition model.

## Transition guards, actions, and outcomes

Some state-machine formalisms attach a **guard** to a transition: a condition that must hold for the transition to be eligible. They may also attach actions, outputs or side effects. The presence of these components depends on the formalism.

For example:

```text
State: IDLE
Input/event: start_requested
Guard: resource_available = true
Transition: IDLE -> ACTIVE
Action: begin_processing
```

If the guard does not hold, a particular model might stay in IDLE, defer the request, raise an error, or take another transition. The general word *transition* does not settle such behavior; its semantics must be specified.

**State change and observable output can differ.** An internal transition might have no externally visible effect, and a system might produce an output without changing the modeled state. It is therefore important to distinguish what the system *is modeled as*, what it *does*, and what an observer can actually *detect*.

## Event occurrence versus event record

A record such as

```text
timestamp: 14:03:12
event_type: start_requested
entity: device-x
```

does not by itself establish when the real-world event occurred, whether the timestamp was synchronized, whether a transition succeeded, or whether the subsequent system state was observed. The record indicates what its producer reported according to that system's recording semantics.

An explicit [Observation](../scientific-analytical-reasoning/observation.md) mechanism and a claim-relative [Evidence](../scientific-analytical-reasoning/evidence.md) analysis are required before drawing stronger conclusions from a record.

This matters across networks, operating systems, applications, cloud workloads and industrial controls. A log entry describing a requested state transition should not be silently recast as proof that the commanded outcome occurred.

## Time and ordering: an open boundary

A state model can use discrete steps `s0, s1, s2`, measured timestamps, a transition order, or continuous time. These represent **different temporal structures**.

An ordered transition index is not necessarily an SI-clock duration. Two distributed records with timestamps from different clocks do not automatically establish causal ordering. The distinction between **time units**, **physical timing hardware**, **modeled order**, and **distributed synchronization** is retained in the [Coverage Gap Decision Register, G-04](../COVERAGE-GAP-DECISIONS.md).

This article intentionally **does not declare the general notion of temporality complete**. It provides only the temporal assumptions required to explain states, occurrences and state transitions.

## Related canonical knowledge

[Entities and Attributes](entities-and-attributes.md) supplies modeled subjects and properties; [Sets and Relations](../mathematics-logic/sets-and-relations.md) supplies formal relations and functions; [Observation](../scientific-analytical-reasoning/observation.md) and [Evidence](../scientific-analytical-reasoning/evidence.md) distinguish records from modeled events. [Systems & Engineering](../systems-engineering/README.md) owns whole-system dynamics; [Operating System Principles](../operating-system-principles/README.md) owns process-specific states; [Communication & Distributed Systems](../communication-distributed-systems/README.md) owns replicated states and distributed ordering.

## References and editorial status

- [SEBoK: Concepts of Systems Thinking, State and Behavior](https://sebokwiki.org/wiki/Concepts_of_Systems_Thinking), general state-variable and system-behavior terminology.
- [MIT Computation Structures: Finite State Machines](https://computationstructures.org/lectures/fsm/fsm.html), transition functions and stored state in a concrete formal/physical model.
- [Stanford Encyclopedia of Philosophy: Events](https://plato.stanford.edu/entries/events/), philosophical perspectives on occurrences, objects, and change.

**Editorial state:** This is a substantive domain-agnostic draft. The two-state toggle model was checked against MIT finite-state-machine semantics and all four state/input combinations; the broader event/state distinction is qualified against SEBoK's system-specific account. General temporality G-04 remains open. A separate Wave A audit records technical acceptance and limitations.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Concept Boundary Decisions](../CONCEPT-BOUNDARY-DECISIONS.md)
