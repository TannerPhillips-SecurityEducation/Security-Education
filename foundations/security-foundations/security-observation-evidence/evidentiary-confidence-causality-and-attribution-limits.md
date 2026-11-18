# Evidentiary Confidence, Causality, and Attribution Limits

**Candidate subject:** SF-10-08 · Security Observation & Evidence  
**Working area:** [Security Observation & Evidence](README.md) · The Fundamentals-style directory pattern is adopted; subject ownership remains provisional  
**Artifact type:** Substantive working reference, not an approved canonical publication  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Pilot Technical Review 04](../PILOT-TECHNICAL-REVIEW-04.md), six bounded material claim groups; full source verification and independent expert acceptance pending  
**Architecture:** [Security Foundations proposal](../ARCHITECTURE.md) · [Working inventory](../SUBJECT-INVENTORY-PROPOSAL.md)

## What evidence can establish

Security evidence is information relevant to a specific proposition about a system, event, security property, or actor. **Evidentiary confidence** describes how strongly particular evidence supports a proposition *under stated assumptions*. It is neither an intrinsic quality of a log line nor a universal numerical score. **Causal inference** asks whether one event or condition contributed to another, rather than merely preceding or accompanying it. **Attribution** assigns an action, artifact, or effect to an entity at a declared level of identity.

A record, a security interpretation, a causal explanation, and an attribution claim are distinct objects. Observing an outbound connection can support a claim about a network exchange. It does not, without additional evidence, establish that its purpose was exfiltration, that the host was compromised, or that a named person initiated it.

The foundational distinction is developed in [Observable, Observed, and Recorded](observable-observed-and-recorded.md). The present subject addresses what conclusions records may justify after collection. Evidence collection and incident investigation procedures belong in [Operational Foundations](../../operational-foundations/README.md).

## The unit of a claim determines its evidence requirements

A useful investigation can distinguish several increasingly demanding propositions about the same apparent event.

| Claim | Example proposition | What could support it | What remains unproven |
| --- | --- | --- | --- |
| Representation | A file contains an authentication-success record | Inspecting the retained file and its integrity | Whether authentication actually succeeded |
| Observation | A particular sensor observed an apparent authentication response | Sensor configuration, collection path, trustworthy timing | Whether the sensor parsed or associated the exchange correctly |
| System behavior | The service accepted a particular credential or session | Server state, protocol trace, application evidence | Which human, if any, controlled the credential |
| Security interpretation | The access was unauthorized or violated a policy | Actual applicable policy, identities and permissions, time-specific state | Whether an intentional attacker caused the violation |
| Causal explanation | A particular action caused a later security-relevant outcome | Mechanistic evidence, alternative-hypothesis analysis, temporal constraints | Exclusive cause or general applicability beyond this case |
| Attribution | A particular account, device, process, organization, or person performed the act | Identity-binding and continuity evidence appropriate to that entity type | Attribution at a stronger level than the evidence reaches |

These are not a mandated universal ladder: a direct attestation might support one level without all intermediate logs. Nevertheless, **moving to a stronger proposition requires a new justification**, not a new adjective attached to the same artifact.

Evidence is claim-relative. A comparison against a trustworthy prior checksum can reveal accidental byte changes, but its resistance to deliberate substitution depends on the integrity mechanism and the trustworthiness of the reference value. Even a cryptographically authenticated digest cannot show that the original bytes accurately described reality. Likewise, authenticated logging can support origin of a record without establishing truth of the event text, completeness of the record stream, or correctness of the sender.

## Confidence depends on assumptions and competing explanations

Evidence quality has several independent dimensions:

- **Provenance and integrity:** Who or what created the data, which transformations occurred, and whether the retained representation changed.
- **Observability and coverage:** Whether the relevant activity was within sensor reach, enabled, retained, and successfully parsed; missing evidence is not automatically evidence of absence.
- **Time and identity binding:** Clock synchronization, correlation keys, session reuse, address translation, shared credentials, and the difference between logical identities and humans.
- **Diagnosticity:** How differently the evidence would be expected under competing explanations; an observation common to benign and malicious activity may be weak evidence for either.
- **Independence:** Whether apparently corroborating records actually arise from independent capture paths, or share one sensor, clock, parser, data source, or mistaken assumption.
- **Reproducibility and challenge:** Whether another analyst can examine source material and meaningfully test the claim or an alternative explanation.

The [W3C PROV Data Model](https://www.w3.org/TR/prov-dm/) describes general provenance relations among entities, activities, and agents. It is useful for modeling lineage, but a provenance graph is not by itself a truth certificate. PROV-DM's formal relation `wasAttributedTo` associates a provenance entity with an agent; this must not be equated automatically with forensic attribution of a network event to a human adversary. [NIST SP 800-86 (2006)](https://csrc.nist.gov/pubs/sp/800/86/final) discusses acquiring, examining, analyzing, and reporting digital evidence and explicitly scopes its guidance to IT forensics rather than legal advice.

A security conclusion should preserve three things together: the proposition, the supporting evidence, and the assumptions/limitations that determine its strength. Labeling a finding “high confidence” without specifying the claim and its basis does little to distinguish evidence from opinion.

## Worked example: a high-performing alert can still be weak evidence

Consider a **hypothetical** binary detector with stipulated conditional error rates applied to 10,000 comparable opportunities. No calibration experiment has been performed or implied. Suppose the target condition truly holds in 1% of opportunities, the detector alerts for 90% of target cases (sensitivity), and it also alerts for 5% of non-target cases (false-positive rate). These figures are assumptions for illustration, not measurements.

| Modeled outcome | Calculation | Expected count |
| --- | ---: | ---: |
| Actual target condition | 10,000 × 0.01 | 100 |
| True alerts | 100 × 0.90 | 90 |
| Non-target condition | 10,000 − 100 | 9,900 |
| False alerts | 9,900 × 0.05 | 495 |
| All alerts | 90 + 495 | 585 |

Let **M** denote the stipulated target condition and **A** denote an alert. For an alert drawn from this population, the modeled positive predictive value is:

\[
P(M\mid A)=\frac{P(A\mid M)P(M)}{P(A\mid M)P(M)+P(A\mid \neg M)P(\neg M)}
=\frac{0.90(0.01)}{0.90(0.01)+0.05(0.99)}
\approx 0.1538.
\]

Only about **15.4% of alerts** correspond to the stipulated target condition under these assumptions, despite 90% sensitivity. The result is not a universal probability of maliciousness. If prevalence, detector behavior, event dependence, or the meaning of the target class changes, the calculation changes. For several correlated detections, multiplying their probabilities as though they were independent would generally be unjustified.

The exercise demonstrates why “the detector fired” and “the hypothesis is supported strongly” are different statements. It also illustrates a concept from [Fundamentals: Evidence](../../fundamentals/scientific-analytical-reasoning/evidence.md): evidence strength depends on the proposition and the competing explanations, not just the existence of a record.

## Sequence, correlation, and cause

An event occurring before another satisfies a *possible* temporal condition for certain causal hypotheses, but does not establish causation. Two observations can covary because one affects the other, because both depend on an unobserved common cause, because the measurement process couples them, or by coincidence.

Imagine a service deployment that simultaneously changes DNS queries and causes authentication failures. A network monitor records the DNS increase first and authentication failures shortly afterward. The shared deployment is a plausible common cause. Without additional mechanism-level evidence, neither “DNS caused authentication failure” nor “an attacker used DNS to cause the failure” follows from ordering alone.

```text
                Configuration deployment
                     /          \
                    v            v
          DNS query pattern   Authentication failures
                    `--------------`  correlated observations
```

This diagram is a **hypothetical causal explanation**, not evidence about a real incident. Rival explanations need not be equally likely; they must be assessed rather than ignored. A time series can help exclude impossible orderings when clocks and event semantics are trustworthy, but correlation alone does not identify a unique causal path.

## Attribution must name the level of identity

“Source” can refer to a packet address, endpoint, application process, authenticated principal, credential holder, administrative organization, or human being. Those are **not interchangeable**:

- A source IP address can identify a network endpoint from one vantage point and time, while network address translation, proxies, spoofing, shared hosts, and dynamic allocation complicate stronger attributions.
- A verified application signature can help bind software artifacts to a signing key; it does not prove which person initiated a runtime action.
- A successful login can support use of an account or credential; it does not prove the legitimate owner performed the action.
- A threat-intelligence campaign label or behavior-pattern match can support a hypothesis about a group or technique but is not a forensic identity proof.

Attribution may be **unknown**, or justified only at the process/device/account level. Intent hypotheses about a threat source belong to the [Threats, Hazards & Adversarial Behavior](../threats-hazards-adversarial-behavior/README.md) area; evidentiary limits remain here. The previous SF-03-08 planning label was divided between these responsibilities, as recorded in [Architecture Adjudication 02](../ARCHITECTURE-ADJUDICATION-02.md).

A strong claim about *which computer exchanged packets* and a weak claim about *which person controlled it* can coexist without contradiction.

## Absence, contradiction, and evolving interpretations

When a search returns no matching log, alternative explanations include no occurrence, missing collection, dropped events, retention expiry, time-range mismatch, parsing error, and querying the wrong dataset. Negative evidence becomes informative only after establishing that the relevant event would probably have been observed and retained under the hypothesized conditions.

Conflicting records can indicate tampering, clock skew, partial coverage, duplicate event identifiers, or genuine differences in sensor vantage. Disagreement should be resolved through testable provenance and observation models; a majority vote among dependent sensors is not automatically stronger evidence.

When new observations arrive, investigators may revise an interpretation while preserving the original record and the revision history. The [NIST SP 800-61 Revision 3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final) supplies current incident-response context; it does not make an alert, an incident designation, or a forensic theory self-validating.

## Relationships, boundaries, and source scope

- [Observable, Observed, and Recorded](observable-observed-and-recorded.md) owns the distinction between reality, sensed phenomena, and retained representations.
- [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) owns arguments that bind a security claim to evidence.
- [Threat Sources and Threat Events](../threats-hazards-adversarial-behavior/threat-sources-and-threat-events.md) owns the difference between potential causes and occurrences.
- [Compromise and Loss of Security](../security-failure-resilience/compromise-and-loss-of-security.md) owns conditional claims of lost security properties.
- [Fundamentals: Temporal Concepts and Models](../../fundamentals/models-abstraction/temporal-concepts-and-models.md) owns general time and ordering structures.
- [Security Risk & Uncertainty](../security-risk-uncertainty/README.md) owns scenario and likelihood uncertainty, not the present subject's evidence-to-claim inference.
- [Operational Foundations](../../operational-foundations/README.md) owns actual monitoring, triage, investigation, forensic processing, and response activities.

**Primary source starting points:** [NIST SP 800-86, Guide to Integrating Forensic Techniques into Incident Response (2006)](https://csrc.nist.gov/pubs/sp/800/86/final), forensic data-source and interpretation scope; [NIST SP 800-61 Rev. 3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final), current incident-response context; [W3C PROV-DM (2013)](https://www.w3.org/TR/prov-dm/), formal provenance vocabulary; [NIST SP 800-92 (2006)](https://csrc.nist.gov/pubs/sp/800/92/final), historical log-management reference rather than current prescriptive incident-response guidance.

**Editorial limitation:** The causal diagram and detector counts are authored examples, not source experiments. The cited sources inform bounded evidence, provenance, and operations; they do not directly establish the example's assumed probabilities, prove any attribution, or validate a specific monitoring system. The exact meaning of confidence remains tied to a declared proposition and evidence method. The separate [Review 04](../PILOT-TECHNICAL-REVIEW-04.md) checked six claim groups and recalculated the hypothetical example. Complete source-passage verification, independent expert acceptance and taxonomy ratification remain outstanding.

[Security Foundations](../README.md) · [Working area](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
