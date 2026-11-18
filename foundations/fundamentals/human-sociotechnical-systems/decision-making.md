# Decision-Making

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Decision-making  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 05 audit](../WAVE-B-TECHNICAL-REVIEW-05.md); no independent human peer review

## Decisions connect goals, knowledge, alternatives and action

**Decision-making** is the process of selecting or committing to an option under some combination of goals, constraints, available information, anticipated consequences and uncertainty. A **decision rule** describes how alternatives are evaluated and selected. A **decision outcome** is what results when an option is implemented; the outcome does not prove that the reasoning was valid or that the original choice was justified.

Humans may use explicit analysis, learned experience, heuristics, consultation, organizational rules or combinations. No one method is always appropriate. A quick heuristic can be useful under time pressure and hazardous under misleading cues. A lengthy calculation may improve rigor while introducing delay, complexity, or false precision.

The [APA Dictionary's heuristic definition](https://dictionary.apa.org/heuristic) distinguishes efficient decision strategies from guaranteed-correct algorithms. [NASA Human Performance and Error](https://www.nasa.gov/reference/5-0-human-performance-and-error-vol-2/) discusses cognition and decision-related limitations in operational environments.

## What is known, assumed, valued and chosen?

A decision statement should keep four different elements apart:

| Element | Example | Limitation |
| --- | --- | --- |
| Evidence | Recorded measurements and their provenance | Data may be incomplete or inaccurate |
| Model | Estimated consequences of available options | Predictions depend on assumptions |
| Preference or objective | Minimize delays while meeting an acceptable risk threshold | Values and thresholds are not automatically empirical facts |
| Decision/action | Select one alternative and implement it | An action does not certify the model or preference |

**Uncertainty** describes limitations in what is known or predicted. **Risk** evaluates adverse possibilities in relation to consequences and objectives under a specified framework. **Preference** or value expresses what outcomes matter. Treating one as a substitute for another can conceal important disagreements.

[Evidence](../scientific-analytical-reasoning/evidence.md) owns claim-relative support; [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) owns mathematical probabilities; [Ethics and Professional Responsibilities](ethics-and-professional-responsibilities.md) owns duties and harm-related constraints.

## Heuristics, biases, and bounded reasoning

A **heuristic** is a practical strategy that can reduce cognitive and computational effort but does not guarantee correct results. Bias can arise when particular processes systematically distort judgment relative to an appropriate criterion, yet identifying a named cognitive bias after an outcome is not a complete explanation of what caused a particular person's choice.

**Framing** can alter which features of an option appear salient. **Anchoring** can make an initial number influential even when irrelevant. **Availability** can influence judgments when vivid examples are easier to recall than representative data. These are useful research concepts, not a license to label every disagreement as irrational.

The [APA Dictionary: Availability Heuristic](https://dictionary.apa.org/availability-heuristic) explains a recurring mechanism. Individual decisions depend on context, expertise, incentives and information quality.

## Worked example: expected cost under stipulated probabilities

Suppose an organization must choose between two hypothetical operating arrangements.

```text
Option A: fixed cost = 40 units
          probability of an additional 100-unit loss = 0.10

Option B: fixed cost = 55 units
          probability of an additional 100-unit loss = 0.02
```

Under the assumed probability model, linear monetary valuation, and no other consequences:

```text
Expected cost(A) = 40 + 0.10 × 100 = 50 units
Expected cost(B) = 55 + 0.02 × 100 = 57 units
```

Option A has the lower **expected cost in this toy model**. That arithmetic does not make it the uniquely correct decision for every stakeholder. A risk-averse decision maker, a safety constraint, possible catastrophic consequences, or inaccurate probabilities may change the result. Expected-value calculations do not settle values, ethics, or the legitimacy of risks imposed on others.

The parameters are invented; neither option describes a real product or incident.

## Decision thresholds, evidence and asymmetric consequences

A decision rule under uncertainty combines **information about the condition**, **action alternatives**, **objectives**, and **relative consequences**. Changing the required evidence threshold is not the same as changing the underlying ability to distinguish conditions.

In signal detection theory, a more permissive threshold can increase the hit rate and false alarm rate simultaneously; a more restrictive threshold can reduce both hit rate and false alarm rate. [Human Cognition and Perception](human-cognition-and-perception.md) owns the perceptual discrimination model, while this article owns **how action criteria reflect objectives and consequences**.

**Worked illustration:** Under a stipulated model, acting on a false alarm costs 2 units, failing to act when a true hazard is present costs 20, and the probability of the hazard given current information is p. If doing nothing costs 20p and acting costs 2(1−p), then acting has lower expected loss when 2(1−p)<20p, or **p>1/11 ≈ 0.0909**. This is a *toy* two-action expected-loss model; it omits action cost during true hazards, additional harms, prior decisions, delayed effects and estimation uncertainty. The numerical threshold is **not** a recommended alarm policy.

The model illustrates why a decision can be justified under a specific preference/risk representation while its outcome remains unfavorable, and why avoiding all false alarms is not the same as choosing the safest decision rule.

## Decision quality and outcome quality

A defensible choice can produce an unfavorable result because of genuine uncertainty, while a poorly grounded choice can appear successful by chance. **Outcome quality and decision-process quality must be assessed separately**.

Good process documentation can identify the decision's question, alternatives, assumptions, evidence, criteria, dissent, limits, designated authority, and a plan for revision. Those practices enable later scrutiny without proving the original decision optimal.

Decisions can also be distributed: one person identifies a problem, others supply information, an authorized role chooses, and a separate operator implements. This distribution requires explicit responsibilities to prevent ambiguous accountability.

## Changing decisions with new evidence

An initial decision may be reasonable under one state of knowledge and inappropriate when new observations arrive. **Revision is not inherently failure**; refusing to revise can be a failure of governance when the relevant premises have changed.

A decision log should preserve the original information set, not rewrite the past to make the decision appear inevitable. Retrospective analysis should distinguish what was knowable at the time from what became evident afterward.

[Collaboration and Communication](collaboration-and-communication.md) owns how alternatives and rationale move between people. [Organizational Structures](organizational-structures.md) owns roles and authority. [Requirements](../systems-engineering/requirements.md) owns specified system needs, not the entire psychology of choosing among them.

### Sources

- [FAA Human Factors Analysis of Safety Alerts, Signal Detection Theory, 2007](https://hf.tc.faa.gov/publications/2007-human-factors-analysis/full_text.pdf).


- [APA Dictionary: Heuristic](https://dictionary.apa.org/heuristic).
- [APA Dictionary: Availability Heuristic](https://dictionary.apa.org/availability-heuristic).
- [NASA: Human Performance and Error](https://www.nasa.gov/reference/5-0-human-performance-and-error-vol-2/).
- [NASA: Technical Risk Management](https://www.nasa.gov/reference/6-4-technical-risk-management/).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 05 technical audit](../WAVE-B-TECHNICAL-REVIEW-05.md). Complete standards verification, independent human expert review and final publication acceptance remain separate and pending.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
