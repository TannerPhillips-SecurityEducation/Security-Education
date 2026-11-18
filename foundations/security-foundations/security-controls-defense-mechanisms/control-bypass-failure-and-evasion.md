# Control Bypass, Failure, and Evasion

**Candidate subject:** SF-07-06 · Security Controls & Defense Mechanisms  
**Working area:** [Security Controls & Defense Mechanisms](README.md) · Approved Fundamentals-style directory pattern; individual subject ownership provisional  
**Artifact:** Substantive working reference, not a canonical publication or a guide to attacking real systems  
**Development state:** Draft · **Source-review state:** References listed; primary-source scopes consulted; separate claim-led Technical Review 09 pending  
**Architecture:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Coverage review SG-08](../COVERAGE-AND-GAPS-REVIEW-03.md)

## A control can be present without providing its claimed protection

A security control may be correctly installed and visible in an inventory while the intended security property is still violated. Explaining that outcome requires distinguishing **bypass**, **failure**, **evasion**, **misconfiguration**, and **non-coverage** rather than treating every adverse event as an attack on the control itself.

- **Bypass:** an operation reaches an effect through a route or operating condition that avoids the expected safeguard's mediation or constraint. It may be intentional or accidental.
- **Failure:** a control is unable to provide its specified protective function under the actual conditions. Failure can arise from a fault, an incorrect dependency, a design flaw, or deliberate interference.
- **Evasion:** activity is deliberately adapted to reduce its chance of being detected, classified, examined or acted upon by a defensive mechanism. Evasion is commonly relevant to sensors and analytic controls.
- **Misconfiguration:** the deployed settings, policy or integration differ from the requirements needed for the control's intended function. A misconfigured safeguard may still execute its own configured rules correctly while failing the *intended* protection.
- **Coverage gap:** the modeled control does not apply to an operation, state, path or interface in the asserted protection scope. This may have been an explicit design choice, an unrecognized omission, or an inherent limitation of the control.

These are **editorial analytical distinctions**, not an approved universal threat or failure taxonomy. One case may satisfy several descriptions. The security proposition must identify which mechanism is relevant and what evidence supports it.

[NIST SP 800-160 Vol. 1 Rev. 1 (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) Appendix **E.9 Defense in Depth** discusses avoiding a single point of failure by coordinating multiple barriers along loss scenarios. It does not promise that one named defensive technique can stop all adverse behavior. [NIST SP 800-160 Vol. 2 Rev. 1 (2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) explicitly includes analytic monitoring, coordinated protection, segmentation, diversity and other distinct resilience techniques. Their performance must still be justified in a declared system.

## Failure of what, at which boundary?

"Security failed" can mean several different things:

| Claim level | Example | What remains unproven |
| --- | --- | --- |
| Requirement failure | Unauthorized data was disclosed under the intended policy | Which component or actor caused it |
| Design failure | A critical path was never mediated by an authorization control | That the implemented rule itself malfunctioned |
| Implementation failure | An authorization check returns an incorrect decision | Whether its deployment ever exercised the faulty condition |
| Configuration failure | A policy grants broader access than intended | That users actually abused the granted authority |
| Operational/dependency failure | A shared identity service or policy store becomes unavailable | That all protected resources lost confidentiality |
| Detection failure | A relevant event was observable but the detector missed it under its coverage assumptions | That the event's actor identity or intent is known |
| Evidentiary failure | Missing or corrupt records prevent a confident reconstruction | That no security violation occurred |

Each claim has a different **observation and proof obligation**. A legitimate user who receives data under an overly permissive policy may have passed every authentication check; the root problem may lie in the specification of authorization or resource ownership, not the credential mechanism.

[Controls, Safeguards, and Security Functions](controls-safeguards-and-security-functions.md) owns the distinction between selected control and claimed effect. [Compromise and Loss of Security](../security-failure-resilience/compromise-and-loss-of-security.md) owns what it means for a protected state to have been compromised. This article owns **mechanisms by which controls cease to constrain or observe behavior as claimed**.

## Bypass and evasion require different analyses

A bypass route need not defeat the cryptography or software logic inside a control. Suppose a hypothetical user-facing API correctly enforces document authorization, while an internal maintenance service exposes the same data under a separate authorization rule. If the internal service can be misused by a subject not intended to have access, the original API check has not failed; the claimed **system-wide mediation** is incomplete.

By contrast, an evasion scenario may involve behavior that traverses a detector's observable path but is not classified as suspicious under its current model. That can occur through different content representations, contextual differences, gaps in protocol parsing, timing, or incorrect assumptions about what "normal" behavior means. **An unclassified observation is not evidence of benign intent**, nor is it necessarily evidence of a deliberate evasion attempt.

A real analyst should keep distinct:
- **absence of sensor coverage**;
- **sensor observed something but did not preserve it**;
- **record was preserved but no detection was configured**;
- **detector executed and did not match**;
- **detection matched but the alert was suppressed or never delivered**;
- **alert was delivered but no effective action followed**.

These stages have different failure modes and different evidence. Neither a lack of alerts nor a single negative test establishes that no adversary acted.

[Observable, Observed, and Recorded](../security-observation-evidence/observable-observed-and-recorded.md) owns what collection and recording can prove. [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) owns confidence in the conclusions, including whether deliberate evasion can be inferred.

## Protective failure, fail-open and fail-closed are contextual

A component's unavailable or degraded state can be handled by:
- **failing open:** allowing a designated operation to proceed without the normal restricting decision;
- **failing closed:** rejecting or stopping a designated operation when the expected authorization or safety condition cannot be established;
- **degraded safe mode:** providing a smaller, independently justified set of essential functions while maintaining selected protection conditions.

These phrases only make sense when tied to **which action, protection property and consequence** are at issue. "Always fail closed" can produce unacceptable safety or availability harm in some systems; "always fail open" can expose confidential information or cause unauthorized control. A safe physical shutdown can reduce one kind of harm while violating an ordinary service-availability target.

[NIST SP 800-160 Vol. 1 Rev. 1](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf), Appendix E, names **Protective Failure**, **Protective Recovery** and **Continuous Protection** as separate principles. The presence of one mode or a management override does not establish that all protection conditions survive a transition.

[Graceful Degradation and Safe Failure](../security-failure-resilience/README.md) is a **currently Inventoried candidate** for the general consequence and fallback-state meanings. This article instead asks how a particular safeguard's **protective claim** can fail in those states, without creating a second full resilience owner.

## Worked case: a protective check during partial outage

Imagine a fictional service that checks whether an employee may approve a payment. Its authorization policy is held in a shared repository.

**Normal state:** The service asks the policy engine whether the employee can approve the specific transaction. Denials and permits are recorded.

**Fault state A:** The policy engine is temporarily unreachable. The application refuses all requests. This may preserve the no-unauthorized-approval property, but it can interrupt critical legitimate approvals.

**Fault state B:** The application temporarily permits all requests to keep transactions flowing. Availability improves, but the original authorization guarantee is absent in this mode.

**Fault state C:** The application enters a constrained recovery mode allowing only a separately approved, low-risk operation with a distinct verified policy path. This may preserve important service functionality while meeting the declared authorization constraints, but those claims require evidence.

The three cases are **invented designs**, not recommended implementation patterns. Neither A nor B can be declared universally correct without knowing the stakeholder needs, safety constraints, economic consequences and legal obligations. Case C is not automatically safe just because it sounds cautious.

The example demonstrates why evaluating a control solely in its normal operating state can miss a more consequential security loss scenario.

## The detector that did not alert

Suppose a telemetry platform saw an unusual event but issued no alert. At least four distinct hypotheses can explain the absence:

1. the event was in the raw collection scope but outside configured detection logic;
2. the relevant data was filtered, delayed or expired before the rule evaluated it;
3. the rule's assumptions or input parsing did not match the actual event representation;
4. a decision policy correctly excluded the behavior because it was an authorized activity, under the system's intended detection scope.

Without evidence, the analyst should not assert "the attacker evaded detection" or "the detector malfunctioned." Those are **causal and actor-intent claims**. Similarly, an alert alone does not establish maliciousness or actual damage.

[MITRE ATT&CK's Defense Evasion tactic](https://attack.mitre.org/tactics/TA0005/) is a *behavioral objective category* describing adversarial methods intended to avoid detection or defensive controls. Assigning such a tactic to a live event requires evidence of the behavior and relevant adversarial context, not merely the absence of a matching rule.

[MITRE D3FEND](https://d3fend.mitre.org/faq/) provides relationships among defensive countermeasure techniques but **does not prescribe a choice or quantify effectiveness**. A catalog label cannot settle whether the actual behavior fell outside sensor coverage or bypassed a deployed decision.

## Controls can be undermined by shared dependencies

Imagine two independent-looking sensors that both send events to one collection queue. A failure of the queue removes the recording path for both, even if both sensors continue collecting raw signals. An attacker can also affect the same policy database used by several downstream enforcement components.

An assertion that "we have two security controls" is insufficient to establish independent defenses. The controls may share:
- credentials, secrets and administrative roles;
- policy decision sources or configuration distribution;
- telemetry ingestion, time services and event retention;
- power, networking, DNS and cloud management planes;
- vulnerable code, libraries or supplier dependencies.

These dependencies need their own failure analysis. [Redundancy, Diversity, and Common-Mode Failure](../security-failure-resilience/redundancy-diversity-and-common-mode-failure.md) owns the reliability/security implications of correlated losses; [Defense in Depth and Diversity](defense-in-depth-and-diversity.md) owns the coordinated layering of protection.

## Control evaluation is not evidence of universal security

A meaningful effectiveness assertion should state which **control function** was expected, what **conditions** were tested, what the **observed outcome** was, and which **unmodeled cases** remain.

For example:
- "The object-level authorization control rejected an unauthorized request to this endpoint under configuration X" is a bounded observation.
- "The entire application is immune to unauthorized reads" requires independent coverage across all relevant object paths, identities, configurations, and time horizons.
- "The event was not detected in three replay tests" supports a narrower negative finding under those test conditions, not proof of general undetectability.

[NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) defines control-assessment procedures and methods. **Examine**, **interview** and **test** have different evidence roles; none can provide guarantees outside its specified assessment objective and depth. The SP 800-53 control catalog and SP 800-53A assessment procedures remain distinct publications.

## Canonical relations and sources

- [Control Placement and Coverage](control-placement-and-coverage.md) owns where a safeguard is intended to apply; this article owns bypass and failure mechanisms affecting its actual contribution.
- [Defense in Depth and Diversity](defense-in-depth-and-diversity.md) owns coordinated barriers and defense dependence.
- [Controls, Safeguards, and Security Functions](controls-safeguards-and-security-functions.md) owns the difference between design intent, deployed control, and measured effect.
- [Resilience, Survivability, and Robustness](../security-failure-resilience/resilience-survivability-and-robustness.md) owns the system's capacity to withstand, recover and adapt.
- [Information-Flow Security and Noninterference](../secure-design-architecture/information-flow-security-and-noninterference.md) owns whether restricted information can influence an unauthorized observer, beyond access checks.
- [Security Risk & Uncertainty](../security-risk-uncertainty/README.md) owns uncertain likelihood and consequence estimates; [Operational Foundations](../../operational-foundations/README.md) owns operational control engineering and testing.

**Primary source starting points:**
- [NIST SP 800-160 Vol. 1 Rev. 1 (final 2022)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf), Appendix E (Continuous Protection, Defense in Depth, Protective Failure and Protective Recovery), E.9 printed p. 88/PDF index 103. Source illustrations do not mandate universal fail-open/closed behavior.
- [NIST SP 800-160 Vol. 2 Rev. 1 (final 2021)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v2r1.pdf), resilience principles and coordinated protection, layering and partitioning (Appendix D §§D.5.2.3–D.5.2.5, printed pp. 125–126).
- [NIST SP 800-53 Rev. 5 / Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), catalogued safeguards; [SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), independent assessment-method vocabulary.
- [MITRE ATT&CK: Defense Evasion](https://attack.mitre.org/tactics/TA0005/), adversarial tactic meaning, not proof of intent in a specific telemetry record.
- [MITRE D3FEND FAQ](https://d3fend.mitre.org/faq/), nonprescriptive countermeasure categories and explicit effectiveness limitation.

**Editorial limitations:** All incidents and architectures above are hypothetical and avoid practical exploitation directions. The meaning of bypass, evasion and failure is scoped to modeled requirements and observations, not a universal approved taxonomy. This is **Draft / References listed**, requiring a separate technical Review 09 with claim-source checks, counterexamples and coverage/owner-boundary validation before Reviewed promotion. No source-Verified, independently approved or Published state is asserted.

[Security Foundations](../README.md) · [Area index](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
