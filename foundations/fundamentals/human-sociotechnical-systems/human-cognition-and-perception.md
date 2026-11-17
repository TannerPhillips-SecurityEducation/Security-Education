# Human Cognition and Perception

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Human cognition and perception  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 05 audit](../WAVE-B-TECHNICAL-REVIEW-05.md); no independent human peer review

## People perceive, interpret, and remember through limited processes

**Perception** concerns how sensory information is selected and interpreted into experienced or recognized features of the environment. **Cognition** encompasses mental activities such as attention, learning, memory, comprehension, reasoning, and problem solving. These processes are related but not identical: a visible indicator may be perceived without its intended operational meaning being understood.

A human operator is neither a passive sensor nor an infallible processor of information. What is noticed and remembered depends on task demands, context, prior knowledge, expectations, signal quality, environmental distractions, and individual circumstances. **Variation across people and situations is a basic design consideration**, not evidence that one cognitive profile is the universal human baseline.

[NASA Human Performance and Error](https://www.nasa.gov/reference/5-0-human-performance-and-error-vol-2/) addresses attention, perception, memory, workload, and performance within engineered systems. [SEBoK Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration) situates human capabilities within system design and operation.

## Sensation, perception, attention, and interpretation

A sensory signal and its interpretation are distinct. A display can emit a red light, but its color does not intrinsically mean emergency, stop, or defective state. Meaning depends on an interface convention and a person's ability to perceive and interpret it.

**Attention** selects or prioritizes portions of available information; it is affected by competing demands and task context. A low-salience indication can be missed, while a conspicuous but irrelevant warning can capture attention. Neither an observed miss nor a correct response alone demonstrates the entire cognitive mechanism responsible.

**Situation awareness** is a model-dependent understanding of relevant conditions and possible consequences in a dynamic task. It should not be equated with merely viewing a dashboard. A person may recognize individual readings yet misunderstand their combined implications.

## Working memory and external representations

Human **working memory** supports temporary maintenance and manipulation of information during ongoing tasks; it is limited, but the amount and form of what can be maintained vary with material, expertise, strategies, and task demands. It is inaccurate to prescribe a universal fixed number of information items for every person and context.

External representations such as labels, diagrams, checklists, persistent status displays, and written procedures can reduce demands on memory when they are accurate, accessible, and appropriately designed. They can also create new errors if stale, cluttered, ambiguous, or inconsistent with the underlying system.

[Metadata](../information-data/metadata.md) describes recorded context. [Human-Computer Interaction](human-computer-interaction.md) owns the interaction mechanisms through which information is presented and acted upon.

## Worked example: two ways to present state

Suppose an operator must distinguish a controller's current state and a pending requested action.

```text
Interface A:
  Green light
  Green light

Interface B:
  Current state: ON
  Requested action: OFF
```

Assume the two lights in Interface A have no documented labels or distinct positions. Their meaning cannot be reliably inferred from color alone, even for a person who perceives green easily. Interface B communicates two roles explicitly in this toy example, though it still requires understandable text, legibility, and updated values.

This example does **not** establish experimentally that Interface B is faster or safer for every user. Such conclusions would require evaluation with representative participants and realistic tasks. It illustrates the distinction between sensing a cue and knowing what the cue denotes.

## Cognitive workload and task design

**Workload** concerns task demands relative to available human resources and capabilities under a given model. Both excessive demands and insufficient engagement can degrade performance under some conditions, but the relationships are contextual, not universal equations.

Time pressure, frequent interruptions, unclear priorities, unfamiliar terminology, and poorly timed alerts can affect performance. A design response may simplify presentation, support progressive disclosure, provide state history, or make recovery possible. Such measures require evaluation rather than assumption that fewer controls or fewer messages are always better.

Human differences may involve visual, auditory, motor, cognitive, linguistic, situational or experience-related factors. The correct engineering response is not to infer individual ability from a demographic label or a diagnosis; it is to consider documented requirements and observed task performance.

## Knowledge, inference, and neighboring subjects

Perception produces information available for judgment, but a perceived state is not always the physical state. A displayed measurement may be outdated or incorrect. [Observation](../scientific-analytical-reasoning/observation.md) owns the general epistemic acquisition problem; [Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md) owns knowledge limits.

[Decision-Making](decision-making.md) owns choosing among alternatives under criteria and uncertainty. [Human Error](human-error.md) owns undesired departures in human-system activity and contributing conditions. [Usability and Accessibility](usability-and-accessibility.md) owns evaluation of inclusive and effective use, rather than claiming every cognitive challenge is a user defect.

### Sources

- [NASA: Human Performance and Error](https://www.nasa.gov/reference/5-0-human-performance-and-error-vol-2/).
- [SEBoK: Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration).
- [NIST: Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 05 technical audit](../WAVE-B-TECHNICAL-REVIEW-05.md). Complete standards verification, independent human expert review and final publication acceptance remain separate and pending.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
