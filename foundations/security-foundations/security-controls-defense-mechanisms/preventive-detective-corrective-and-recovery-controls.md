# Preventive, Detective, Corrective, and Recovery Controls

**Candidate subject:** SF-07-02 · Security Controls & Defense Mechanisms  
**Working area:** [Security Controls & Defense Mechanisms](README.md) · Fundamentals-style area directory adopted; subject taxonomy and semantic ownership provisional  
**Artifact:** Substantive cross-domain working reference, not a published catalog or operational control runbook  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 11](../PILOT-TECHNICAL-REVIEW-11.md), 8 material claim groups; full source verification and independent expert review pending  
**Authority:** [Working Inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md) · [Ownership Register](../CANONICAL-OWNERSHIP-REGISTER.md)

## Security controls differ by intended effect, not merely by product name

A **security control** is a safeguard or countermeasure selected to satisfy a specified protection requirement. A useful functional classification asks **what protective effect the control is expected to provide relative to an unwanted event, state or consequence**.

Four frequently discussed functions are **prevention**, **detection**, **correction** and **recovery**. They are not naturally mutually exclusive and do not form one inevitable chronological security process. The same mechanism can serve several functions in different conditions, and a control that operates after an unwanted event can still prevent a *later* loss.

The [NIST security glossary](https://csrc.nist.gov/glossary/term/security) describes protective measures involving deterrence, avoidance, prevention, detection, recovery and correction in the context of sustaining an organization's mission. The NIST entry aggregates multiple source-attributed definitions; it does **not** make this article's four labels an exhaustive, ratified NIST ontology.

The editors of [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html) describe the standard's **control-type attributes** as preventive, detective and corrective in their [ISO/IEC JTC 1/SC 27 editorial overview](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IEC%20JTC%201-SC%2027_N22755_SC27%20Journal%20Vol%202%20Issue%202%20%28update%20Dec%202022%29.pdf). **Recovery** is a useful additional *functional lens* in this working subject, not a claim that ISO/IEC 27002 includes it as a fourth member of that attribute's three-value set. The original journal is an editor-authored overview, **not** the full paid standard text or an independent certification.

## The functional anatomy of a safeguard

| Function | Typical protective intent | Possible example | What the label does **not** establish |
| --- | --- | --- | --- |
| **Preventive** | Prevent a forbidden transition or make it less likely to succeed | An authorization check rejects a read inconsistent with object policy | The check mediates every relevant route, or is correct |
| **Detective** | Reveal an event, condition, deviation or possible violation | A monitor records an integrity mismatch and issues a signal | The event is malicious, or anyone responded |
| **Corrective** | Remove or limit an identified wrong condition, remediate its cause, or prevent recurrence | Fix a configuration error and replace an incorrectly authorized token | Prior consequences have been reversed |
| **Recovery** | Restore a required function, data state or acceptable service after disruption | Restore service from a verified recoverable state | Restored state is trustworthy, complete, or identical to its previous state |

These examples are **possible functions**, not source-defined placement rules. The classification must identify the protected property and its scope. Restoring an application can satisfy an availability objective while leaving confidentiality or integrity uncertain. A control may prevent a *second* event while addressing the first event's underlying weakness. Whether it is *corrective* for the first failure depends on the particular unwanted state and whether the change actually remediates it.

The [CISA Cyber Resilience Review Controls Management resource guide](https://www.cisa.gov/sites/default/files/publications/CRR_Resource_Guide-CM_0.pdf) is cited as historical context for control management. **Its underlying PDF could not be independently retrieved for this review**, so no specific CISA-defined classification is relied upon as a verified authority here. *Compensating* in the [NIST glossary](https://csrc.nist.gov/glossary/term/compensating_controls) instead refers to a baseline-control substitution relationship, which is distinct from event-timing function. Source-specific labels must not be conflated.

## Event time and consequence time do not define one universal sequence

A typical causal sketch is:

~~~text
Potential adverse action or condition
                |
                v
         Preventive barrier
          /             \
     Effective       Not effective / not applicable
         |                  |
    Action blocked     Adverse event may occur
                            |
                  Detection opportunity
                            |
                Correction or containment
                            |
                    Recovery if needed
~~~

This is **an illustrative relationship**, not a complete life cycle. Prevention may be continuously active before, during and after related actions. A detective mechanism may identify a *precursor* early enough to support intervention and prevent an ultimate consequence. Correction may occur before service restoration, after it, or not at all. Recovery may require preserving evidence and using a safer but degraded mode.

**Distinguish the event being prevented from the consequence being prevented.** A sensor detecting a prohibited write after it occurred cannot prevent *that write*. If the alert leads to prompt isolation before further data propagation, the same detection-and-response chain may prevent *additional loss*. Claims of prevention need to say which event or harm did not occur and under what evidence.

## Prevention: blocking a specific forbidden transition

Prevention depends on a rule, an enforcement point, authoritative context and available decision information. A correctly implemented authorization check can prevent a protected read via one API endpoint. It does not automatically prevent reads through backup restoration, an administrative channel, an internal worker or an improperly delegated token.

A preventive claim is therefore conditional:

\[
\operatorname{Prevented}(a,p,s,t)
\]

means, in this authored notation, that action \(a\) was actually blocked on path \(p\) in system state \(s\) at time \(t\) under the stated protection policy. It is **not** a formal NIST predicate or proof that all paths were covered.

An administrative policy can have preventive intent yet be ineffective without enforcement. A physical lock can prevent one unauthorized entrance but not an identity-based data disclosure over a network. The relevant **implementation medium** is separate from the **preventive function**.

[Control Placement and Coverage](control-placement-and-coverage.md) owns paths, boundaries and system states where a safeguard applies, not the general preventive/detective classification maintained here.

## Detection: observation and judgment are different

Detection can depend on the physical or logical vantage, telemetry, parsing, retention, analytic conditions, alert transport, and whether a decision-maker actually receives and understands the result.

Distinguish **observable**, **observed**, **recorded**, **classified**, **reported**, and **acted upon**. A security event that did not produce an alert may have been outside the sensor's view, dropped during collection, omitted by a rule, correctly excluded as benign, or suppressed after a valid match. **Absence of an alert does not prove absence of an event.**

Consider an integrity monitor that notices a file has changed. The monitor may make a correct *detective* observation while leaving unknown who changed the file, whether the change was authorized, why it occurred, and whether any harm followed. A later system action that restores an authorized version is distinct from the detection itself.

[Observable, Observed, and Recorded](../security-observation-evidence/observable-observed-and-recorded.md) owns the epistemic stages; [Control Bypass, Failure, and Evasion](control-bypass-failure-and-evasion.md) owns the mechanisms by which they break down.

## Correction and recovery: fixing a cause is not identical to restoring function

Correction can address a defective state, configuration, rule, credential or missing safeguard. Recovery focuses on getting a necessary function, information state, or operational capability back within acceptable conditions.

Imagine a fictitious service that stopped because a shared policy store became unavailable. A standby system might restore its ability to process requests without correcting the underlying dependency. Conversely, repairing the policy store may eliminate a fault but not recover all queued legitimate requests or a lost transaction.

A *correction without recovery* and a *recovery without root-cause correction* are both conceptually possible. They may overlap when a single intervention both removes the fault and restores acceptable service.

Trust matters: an operational service that responds again is **not necessarily trusted** after a security compromise. [Recovery Objectives and Trusted Restoration](../security-failure-resilience/recovery-objectives-and-trusted-restoration.md) owns recovery states, RTO/RPO and restoration assurance. **SF-07-02 owns control function, not the operational restoration procedure.**

## One control, several functions

An illustrative signed-software-update design might:

1. **Prevent** unauthorized installation when a signature check rejects a package.
2. **Detect** an unexpected change when periodic integrity verification observes inconsistent bytes.
3. **Correct** an erroneous configuration or patch the verification component that enabled the defect.
4. **Recover** a trustworthy operating state from verified known-good material after a disruption.

These are different **claims**, even if they share a component. The signature check does not prove the signing authority itself is uncompromised. The periodic monitor may not see every change. A reinstall from untrusted media may restore function but not integrity.

**Function is conditional on deployment, path, state, threats, and evidence.** A control named “endpoint protection” has no unique function without specifying which of these effects it provides under particular conditions.

### Worked quantitative counterexample: a chain is not four independent guarantees

In a **fictional** dataset of 1,000 genuinely relevant events, suppose exactly 80% become observable and retained, exactly 80% **of that observed subset** produce an actionable signal, and exactly 60% **of that signaled subset** lead to a timely corrective action. These are sequential *conditional* fractions, not independent failure probabilities. These rates are **stipulated conditional proportions**, not measured effectiveness or attack probabilities.

\[
1000 \times 0.80 \times 0.80 \times 0.60=384.
\]

Under these assumptions, **384 of the 1,000 relevant events** reach timely action through the specific detection-response chain. That is **38.4% chain yield**, not “38.4% of attacks prevented.” It assumes nothing about what happened in unobserved cases, the severity of events, any false-positive rate, or the quality of correction. The multiplication is legitimate for these **explicit sequential conditional fractions**, without asserting that sensor, rule and human-response events are statistically independent.

An apparently excellent “80% detection coverage” number would not describe the entire outcome chain. Likewise, receiving a corrective instruction does not prove that a compromised system returned to a trustworthy state.

## Adjacent taxonomies should not be confused

A functional **control type** is not the same as the NIST CSF 2.0 organizational functions **Govern, Identify, Protect, Detect, Respond, Recover**. The latter group outcomes for cybersecurity-risk management, rather than asserting that every individual security control fits exactly one function in the present article's list.

It is also not identical to an **implementation category** (technical, organizational, human or physical), a **security objective** (confidentiality, integrity, availability, privacy or safety), a **control family** (such as Access Control), or an **assessment finding** (“tested and effective in configuration X”).

A single authentication mechanism can be technological in implementation, preventive against certain impersonation attempts, supportive of integrity and privacy, and subject to assessment under several different conditions. These are not conflicting labels; they answer **different questions**.

## Canonical relationships and primary source scope

- [Controls, Safeguards, and Security Functions](controls-safeguards-and-security-functions.md) owns the general safeguard/control/requirement distinction.
- [Technical, Organizational, and Physical Controls](technical-organizational-and-physical-controls.md) owns implementation and responsibility categories.
- [Compensating Controls and Residual Exposure](compensating-controls-and-residual-exposure.md) owns substitution/tailoring relations, not a new event-timing control function.
- [Control Effectiveness and Costs](control-effectiveness-and-costs.md) owns evidence-backed performance measurement and resource tradeoffs.
- [Defense in Depth and Diversity](defense-in-depth-and-diversity.md) owns coordinated safeguards.
- [Control Placement and Coverage](control-placement-and-coverage.md) owns path, state and temporal coverage.
- [Adverse Outcomes, Consequences, and Harm](../protected-interests-assets-harm/adverse-outcomes-consequences-and-harm.md) owns real and possible harms.
- [Operational Foundations](../../operational-foundations/README.md) owns selection, application, validation, monitoring, and restoration procedures.

### Primary sources and status

- [NIST CSRC security glossary](https://csrc.nist.gov/glossary/term/security), CNSSI 4009 and NIST-source definitions containing prevention/detection/correction/recovery and other measures, understood in their attributed contexts.
- [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html), final edition 3, 2022; [ISO/IEC SC 27 editors' overview](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IEC%20JTC%201-SC%2027_N22755_SC27%20Journal%20Vol%202%20Issue%202%20%28update%20Dec%202022%29.pdf) identifies **preventive, detective, corrective** as type attributes, not recovery as a fourth of those particular values.
- [CISA CRR Supplemental Resource Guide: Controls Management](https://www.cisa.gov/sites/default/files/publications/CRR_Resource_Guide-CM_0.pdf), historical reference **not source-page verified** because the publisher PDF was unavailable in this review. Its detailed categories are not used as verified evidence.
- [NIST SP 800-53 Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), control catalog; [NIST SP 800-53A Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), separately scoped assessment.

**Draft limitations:** The working comparison is neither exhaustive nor mutually exclusive. [Technical Review 11](../PILOT-TECHNICAL-REVIEW-11.md) documents eight material claim groups, source-specific ISO control types and a verified conditional-chain calculation, with the unavailable CISA source explicitly unverified. This is **Reviewed (model-assisted) / Core claims checked**, not a deployed-system test, complete source-to-passage verification, independent human review, permanent canonical approval or Published status.

[Security Foundations](../README.md) · [Area](README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
