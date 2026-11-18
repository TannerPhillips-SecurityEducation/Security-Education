# Observable, Observed, and Recorded

**Candidate subject:** SF-10-02 · Security Observation & Evidence  
**Artifact type:** Working article pilot; not an approved canonical subject path  
**Development state:** Draft · **Source review:** References listed; scoped technical audit pending  
**Architecture:** [Candidate inventory v0.3](../SUBJECT-INVENTORY-PROPOSAL.md) · [Source crosswalk](../ESTABLISHED-MODEL-CROSSWALK.md)

## Reality, observation and records are different epistemic objects

Security analysis often begins with **events and conditions** in the world. Some aspects may be observable by an available instrument, some are actually observed, and selected aspects may be recorded. Those are not equivalent stages of certainty.

- **Observable:** A property or occurrence that could, in principle, be made available to an observer under a defined sensor position, mechanism, precision and operating condition.
- **Observed:** Information actually obtained by an observer or measurement process from some accessible phenomenon.
- **Recorded:** A representation of an observation or asserted occurrence retained in a storage or communication medium.

An event can occur without being observable to the deployed system. It can be observable but missed by a sensor. It can be observed without being permanently recorded. A record can also be created by a process that did **not** actually sense the event it purports to describe, including a simulation, mistaken inference, faulty instrument or deliberate fabrication.

```text
World / Network / System Activity
                │
      potentially observable
                ↓
       Observable Properties
                │  sensor and conditions
                ↓
       Actual Observations
                │  processing, selection and storage
                ↓
       Recorded Representations
                │  context and inference
                ↓
       Security Evidence / Claims
```

The flow is a **conceptual explanation**, not a formal proof of all real observation architectures or a claim that every security system must have five named processing stages.

[Fundamentals: Observation](../../fundamentals/scientific-analytical-reasoning/observation.md) owns the general epistemology of observation; [Fundamentals: Data Provenance and Lifecycle](../../fundamentals/information-data/data-provenance-and-lifecycle.md) owns the general derivation/history model. This Security Foundations pilot owns **security-specific significance and limits of inference** from available observations and records.

## The event and the event record are not identical

An **event** is an occurrence or state-changing condition relative to a defined model. An **event record** is an artifact containing selected data that some producer has associated with the occurrence. A record may be a factual representation of an observation, a derived classification, a generated notification or an assertion made by some agent.

A log entry can include timestamps, source and destination labels, action types, status codes, principal identifiers and other fields. Those fields are meaningful only under the **producer's schema, measurement conditions, time conventions, data transformations and trust assumptions**.

The field `user=alice` is not independent proof that a particular human named Alice performed an action. It may represent a claimed login name, authenticated account, session owner, software configuration or another mapping. The interpretation must be justified.

Likewise, an event classification in a detection record might reflect a rule's criteria, not independent proof of malicious intent.

## Visibility boundaries and missingness

**Visibility** refers to the scope of relevant activity and properties that a system can make available for security observation under defined conditions. It depends on placement, sensor capability, access, retention, sampling, processing and adversarial interference.

A sensor placed on one network link cannot automatically observe every flow in the environment. An endpoint logger may omit actions not instrumented by its collection mechanism. A cloud audit service may collect only events exposed by the configured service and permissions. A security program's visibility is therefore a *bounded property*, not a synonym for "logging enabled."

**Missing data** has multiple possible meanings:

| Condition | Example | What the absence does not prove |
| --- | --- | --- |
| Event did not occur | No attempted access in the chosen interval | Nothing about other intervals |
| Event outside observation scope | Activity on unmonitored path | That the activity was benign |
| Sensor failed or was disabled | Dropped packets, disabled logging | That no relevant event occurred |
| Event was observed but filtered | Sampling removed a record | That the observation is unimportant |
| Event record expired | Retention threshold passed | That the event never happened |
| Search omitted a match | Wrong index, schema or filter | That no matching record exists |

A claim of “no attacks occurred” requires a much stronger basis than “no alerts appeared.”

## Telemetry, indicators and detections occupy different semantic levels

**Telemetry** comprises recorded or transmitted data about system activity, such as packet captures, event logs, metrics and traces. A **signal** is a property or pattern with possible significance under some analytical or detection model. An **indicator** is information used to support a hypothesis about a condition or activity.

A **detection** is the result of applying some rule, method or judgment to available information. An **alert** is a notification or output artifact representing a detection condition under a system's design. An alert may be accurate relative to its rule while the resulting security inference is wrong.

For example, an alert indicating `failed_authentication_count > 20` might truthfully report an elevated count. It does not independently demonstrate attempted compromise or rule out legitimate automation, stale credentials, retries or sensor duplication.

Detection engineering, threat hunting, alert triage and investigative decisions are **Operational Foundations** activities; the meaning and limitations of detection evidence belong here.

## Provenance, integrity and trustworthy interpretation

A useful security record has a **source**, a relevant **time/context**, a **producer**, a **schema**, a **transformation history** and assumptions about integrity and completeness. Some of these may be absent or uncertain. Integrity-protected storage can help establish that a representation was not altered after a point of protection, but cannot by itself prove that the original observation was true.

A signed log may prove that a key signed the represented bytes under the signature algorithm's assumptions. Whether the signer was authorized, whether the sensor was calibrated, whether timestamps were reliable, and whether logs were complete are separate questions.

Evidence can support a claim only relative to what it actually observes. The [NIST SP 800-53 control catalog](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls) includes audit and accountability controls, but inclusion in a catalog is not a demonstration of log quality, coverage or forensic authenticity.

## Worked example: one action, three records

Suppose an authorized user successfully downloads a private document, and the following invented records are retained:

```text
Network record:
  time=10:00:00.100  src=clientA  dst=service  bytes_out=1200

Service record:
  time=10:00:00.160  principal=acct42  action=read  object=doc7  status=success

Detection record:
  time=10:00:00.300  rule=large_download  alert=true
```

**What is observable?** Selected connection activity, service-level authorization/read events, and rule outputs from the instrumented systems. The records show that **the producers asserted** those fields under their own collection semantics.

**What can be inferred?** The service log supports a hypothesis that an account-related read succeeded, if its schema and integrity are reliable. The network record may be consistent with the corresponding transfer if the endpoints, times and accounting directions are reconciled.

**What remains unknown?** Whether the transmitted bytes were exactly document 7, whether one particular human operated account 42, whether the reading was legitimate under every applicable policy, whether copies were made outside observation scope, whether timestamps share an accurate clock, and whether the detection rule's label corresponds to a truly "large" download.

**What should not be conflated?** An alert is a recorded detection result, not the underlying event; a log field is a representation, not independent evidence of identity, and a timestamp is not automatic proof of causal ordering.

All values are invented; the example is about evidence limits, not a real-world event.

## Classification and uncertainty

Benign, anomalous, suspicious and malicious can be useful terms for interpreting observations, but they have **distinct evidentiary meanings**. Unknown is a legitimate state of knowledge. An **anomaly** indicates deviation from a chosen baseline or expectation; it does not, by itself, prove intent or a security violation.

**False positives** and **false negatives** depend on an explicit target condition, the decision rule and ground truth or a defensible reference. Different sensors can have different observation scope, and agreement between two correlated sensors is not always independent corroboration.

A security classification can be revised as additional evidence arrives. That revision is not a retroactive change in what was originally recorded, unless the record itself was wrong or altered.

## Related knowledge and references

- [Threat Sources and Threat Events](threat-sources-and-threat-events.md), potential causes, event conditions and hypotheses.
- [Security and Insecurity](security-and-insecurity.md), protected interests and assessable claims.
- [Vulnerabilities and Exploitability](vulnerabilities-and-exploitability.md), mechanisms enabling security violations.
- [Fundamentals: State, Events and Transitions](../../fundamentals/models-abstraction/state-events-and-transitions.md), general event/change definitions.
- [Fundamentals: Temporal Concepts and Models](../../fundamentals/models-abstraction/temporal-concepts-and-models.md), instants, timestamps, causal order and timing uncertainty.
- [Fundamentals: Information Retrieval](../../fundamentals/information-data/search-and-information-retrieval.md), why a failed search does not prove record absence.
- [Network Knowledge](../../../network/README.md), [Endpoint Knowledge](../../../endpoint/README.md) and [Cloud Knowledge](../../../cloud/README.md), concrete telemetry/collection functions.
- [Operational Foundations](../../operational-foundations/README.md), practical investigation and response methods.

**Source starting points:** [NIST SP 800-53 Rev.5, Release 5.2.0](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls); [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final) (older reference, check revisions before operational guidance); [RFC 5424 Syslog](https://www.rfc-editor.org/info/rfc5424/); [W3C PROV-DM](https://www.w3.org/TR/prov-dm/), general provenance framework.

**Editorial limits:** This is a conceptual model of security visibility and evidence. Logging semantics, measurement quality, integrity, timestamp correctness and claims about real actors must be independently validated. No universal security event taxonomy or sensor design is mandated. Full primary-source review and independent expert acceptance remain open.

[Security Foundations](../README.md) · [Pilot Register](README.md)
