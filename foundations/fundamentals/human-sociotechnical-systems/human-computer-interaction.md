# Human-Computer Interaction

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Human-computer interaction  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 05 audit](../WAVE-B-TECHNICAL-REVIEW-05.md); no independent human peer review

## Interaction is a relationship between a person and a system

**Human-computer interaction (HCI)** studies and designs the ways people perceive, understand, control, and receive feedback from interactive computing systems. The system can involve software, devices, equipment, sensors, automation, physical spaces and organizational procedures. HCI is not limited to graphical user interfaces or visual aesthetics.

A user acts within a **context of use**: goals, tasks, experience, capabilities, environment and available resources affect what an interaction should accomplish. A design optimized for an expert in a quiet office may perform differently for an inexperienced operator in noise or under time pressure. Neither context is the universal standard.

[NIST Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design) describes understanding users, tasks and environments, involving people during design, evaluating iteratively, and addressing whole-system experience. [SEBoK Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration) situates human interaction within an engineered system's lifecycle.

## Action, interpretation, and feedback

An interaction can be described as a sequence of changing understandings and actions:

```text
Goal → Select action → Issue command → System response → Perceive feedback → Interpret result
```

This is an **illustrative conceptual sequence**, not a mandatory cognitive model. People may revise goals during interaction, act concurrently, consult others, or misunderstand system state. The real system may also respond asynchronously.

An **affordance** concerns opportunities for action in a given person–environment relationship; a **signifier** is a clue that communicates a possible action. The visible appearance of a control does not alone guarantee that it is operable, and a physically operable control can remain undiscoverable or ambiguous.

**Feedback** provides information about what the system accepted, is doing, completed, rejected, or failed to do. Feedback should distinguish an attempted command from the underlying change of state. A “save” animation is not automatically proof that data reached durable storage.

## Mapping, constraints, and error recovery

**Mapping** links available controls to expected outcomes. A clear mapping allows a person to anticipate what a choice will change. **Constraints** can prevent invalid actions or reduce their scope, but a restrictive design can also block legitimate work.

A system can reduce error potential through visible state, confirmation for consequential actions, undo operations where feasible, unambiguous labels, contextual help and safe recovery paths. These are candidate mechanisms, not universal design rules. Confirmation dialogs can themselves become distracting or routinely ignored.

[Human Cognition and Perception](human-cognition-and-perception.md) owns attention, memory and interpretation. [Human Error](human-error.md) owns the conditions and mechanisms of unintended action; HCI concerns designing the whole interaction rather than assigning failures solely to users.

## Worked example: command versus observed outcome

Suppose a user presses **Stop** for a remotely controlled heater.

```text
Command sent: STOP
Command acknowledged: YES
Heater relay observed: ON
```

The three statements are consistent: the controller may acknowledge receiving the command while the physical relay remains ON because of delay, a fault or a different state-reporting mechanism. An interface that displays only “Success” collapses distinct states and could mislead the operator.

An improved conceptual interface distinguishes **command accepted**, **action in progress**, and **physical state not yet confirmed**. This does not guarantee safety; it makes the interpretation of available evidence more precise. Actual implementation requires reliable sensing, defined time semantics, suitable interface language and evaluation with intended users.

[State and Behavior](../systems-engineering/state-and-behavior.md) owns the system's state semantics; [Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns exchange contracts. G-04 general temporality remains open.

## Multiple interaction modalities

Interaction may use text, graphics, auditory signals, haptics, physical controls, speech or combinations. A modality is not automatically accessible or appropriate for every task. Voice input may be impractical in a noisy area; color-only status cues may be ambiguous; a touchscreen may not suit gloved operation.

A multimodal design may provide alternatives, but alternatives must be consistent and verified. A screen reader announcing an unlabeled button as “button” does not become usable merely because speech output exists.

People may also use assistive technology, automation or delegated operators. The interaction boundary should reflect the actual task and the system of interest.

## Evaluation is context-dependent

Observing representative users attempt realistic tasks can reveal breakdowns that expert inspection misses. Evaluation can consider task completion, errors, recovery, time, comprehension, trust and subjective experience. These measures should be reported with their sample, task, and environmental assumptions. A fast interface is not necessarily safe or satisfying, and one successful demonstration does not establish universal usability.

[Usability and Accessibility](usability-and-accessibility.md) owns the corresponding outcomes and accessibility conditions. [Decision-Making](decision-making.md) owns selection among alternatives, not all interaction mechanics.

## Canonical scope

This article does not prescribe a UI framework, application platform, visual style, software architecture, or interaction protocol for this repository. It introduces no learner assessments or new knowledge-area categories.

### Sources

- [NIST: Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design).
- [SEBoK: Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration).
- [ISO 9241-11:2018, Usability: Definitions and Concepts](https://www.iso.org/standard/63500.html).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 05 technical audit](../WAVE-B-TECHNICAL-REVIEW-05.md). Complete standards verification, independent human expert review and final publication acceptance remain separate and pending.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
