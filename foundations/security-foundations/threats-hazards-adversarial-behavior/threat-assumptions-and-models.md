# Threat Assumptions and Models

**Candidate subject:** SF-03-07 · Threats, Hazards & Adversarial Behavior  
**Working area:** [Threats, Hazards & Adversarial Behavior](README.md) · Fundamentals-style directory architecture adopted; individual subject ownership remains provisional  
**Artifact type:** Substantive security-knowledge working reference, not an operational modeling workshop or final canonical publication  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 10](../PILOT-TECHNICAL-REVIEW-10.md), 11 scoped material claim groups; full source verification and independent expert acceptance pending  
**Architecture:** [Working subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Established Model Crosswalk](../ESTABLISHED-MODEL-CROSSWALK.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)

## A threat model represents possibilities and assumptions, not the threat itself

A **threat model** is an intentionally scoped representation of a system, its protected interests, potential threats, relevant actors and conditions, controls, assumptions and unknowns. It helps explain **how and under what conditions security could fail**. It does not itself prove that an attack occurred, that all real threats have been enumerated, or that the represented system is secure.

A **threat assumption** is a proposition a model treats as true, possible, excluded, fixed or variable for its declared boundary. A **threat hypothesis** proposes that a source, event, mechanism or condition might hold. A **threat assessment** characterizes the available evidence and uncertainty associated with a selected threat context. An observed **threat event** is distinct from all three.

The [NIST threat-modeling glossary](https://csrc.nist.gov/glossary/term/threat_modeling), citing SP 800-53 Rev. 5, describes modeling attack and defense aspects of a particular logical entity. [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) provides risk-assessment framing around threat sources, events, vulnerabilities, impacts, assumptions and uncertainty. These sources are informative within their defined scope; **they do not establish one complete, universal ontology of threat models**.

The [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) describes several modeling approaches for security requirements, system understanding and response decisions. Methodologies differ, and the choice of model should follow the question being examined.

This subject owns the **security-specific concepts of model scope, abstraction, assumptions and validity**, including their relationship to *threat hunting models*. The actual activity of building, facilitating, maintaining or executing a model belongs to [Operational Foundations](../../operational-foundations/README.md).

## Threat Models and Threat Hunting Models are distinct

**Threat Models** and **Threat Hunting Models** can be peers that use some of the same underlying representations, without being the same kind of model.

A **Threat Model** primarily represents potential threats to a scoped system or protected interest, including the system conditions under which an adverse event or violation could occur. A **Threat Hunting Model** primarily represents how a defender can reason about, search for, and assess possible adversarial activity using hypotheses, relevant behaviors, observations, available telemetry, analytics and evidentiary limits. **These two labels distinguish model purpose in this repository. They are not asserted to be disjoint standard-defined types formally enumerated by NIST, MITRE or OWASP.**

This contrast describes **primary analytical purpose**, not a compulsory forward-looking-versus-backward-looking split. A threat model may be updated using real incident evidence, and a hunting model can hypothesize activity not yet observed.

| Dimension | Threat Model | Threat Hunting Model |
| --- | --- | --- |
| **Primary question** | What could go wrong, to which protected interest, and under what assumptions? | What adversarial behavior might be present or have occurred, and what evidence could discriminate it from alternatives? |
| **Scope** | System architecture, stakeholders, resources, boundaries and threat conditions | Hunt terrain, behaviors, time horizon, data sources, expected traces and gaps |
| **Assumptions** | Trust, access, exposure, dependencies, plausible actors and controls | Sensor coverage, telemetry fidelity, behavior observability, baseline and analytic validity |
| **Representation** | Data flows, attack trees, abuse cases, security requirements and assumptions | Behavioral hypotheses, analytic logic, evidence relationships, alternative explanations and hunt context |
| **Expected contribution** | Expose plausible adverse paths and the protection requirements or design gaps they imply | Direct the search for relevant activity and establish which inferences observations support or fail to support |
| **Uncertainty** | Omitted system paths, unmodeled actors and unknown exploitability | Missing data, false positives, false negatives, temporal gaps, causality and intent ambiguity |
| **Primary repository home** | Security Foundations concepts, with modeling practice in Operational Foundations | Hunting-model concepts and practice in Operational Foundations; shared underlying security vocabulary links here |

The distinction is **not** that a Threat Model has no evidence or a Threat Hunting Model has no hypothetical reasoning. Both require explicit assumptions, controlled abstractions and appropriate evidence.

### A hunting model is not automatically a procedure

The expression *threat hunting model* may refer to a **behavioral model**, **analytic hypothesis model**, **evidence/observation model**, or a broader **hunting methodology/framework**. A model of expected adversarial behavior and evidence is not equivalent to a prescribed chronological workflow for the hunter.

MITRE's [TTP-Based Hunting](https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf), a technical report dated **March 2019** and distributed with a 2020 copyright, explicitly connects a malicious-activity model, hypotheses, abstract analytics and data requirements to collection-gap assessment, implemented analytics, and hunt investigation. **MITRE calls the whole arrangement a *hunting methodology***; the reusable model of adversarial activity and evidence is a *component within that method*. Calling the broader arrangement a “Threat Hunting Model” here must not erase the distinction between **representation** and **operational execution**. Its **Figure 3, printed p. 10 / PDF page index 11**, was visually inspected while developing this article. This is **one published methodology**, not a requirement that every hunt follow exactly the same stages.

MITRE's [TTP-Based Threat Hunting and Detection Engineering Training](https://attack.mitre.org/resources/learn-more-about-attack/training/threat-hunting/) separately presents hypothesis development, data requirements, visibility gaps, analytics, and hunts. The [MITRE Cyber Analytics Repository glossary](https://car.mitre.org/resources/glossary/) distinguishes hypotheses describing **expected observable behavior** from the analytic implementation that attempts to identify it.

A hunting model can be built from ATT&CK techniques, Diamond intrusion-event relations, Unified Kill Chain progression, or another justified behavior/evidence framework. It still needs to explain which **observable traces** follow from a hypothesis, what telemetry is actually available, and what **alternative benign causes** could produce the same observations.

## Distinct models can share frameworks without sharing conclusions

| Shared framework | In a Threat Model | In a Threat Hunting Model |
| --- | --- | --- |
| **MITRE ATT&CK** | Describes potential methods and relevant actor capabilities under selected system assumptions | Helps organize expected adversarial behaviors, analytics, required telemetry and hypothesis testing |
| **Diamond Model** | Relates hypothesized adversary, capability, infrastructure and victim in a potential intrusion event | Relates observed or inferred intrusion-event features and tests connections among events |
| **Unified Kill Chain** | Organizes possible attack progression and dependency conditions | Gives contextual hypotheses about where observed behaviors may relate in a broader episode |
| **Attack trees / paths** | Represents alternative actions and preconditions that could reach an objective | Provides competing behavioral paths to examine through recorded evidence |
| **STRIDE** | Prompts examination of possible security-property violations during design | May suggest behaviors worth investigating, but is not itself a complete hunt-analytics model |

The rows describe **possible reuse**, not a one-to-one standard mapping. The Diamond Model can have unobserved vertices. ATT&CK labels tactical objectives rather than ordering every attack chronologically. An attack tree can describe a feasible route without establishing its execution. Reusing the same model vocabulary does not automatically transfer **system completeness** or **evidentiary confidence** from one application to another.

The actual work of formulating a hunt hypothesis, selecting telemetry, querying, analyzing, documenting evidence and refining detections belongs to [Operational Foundations](../../operational-foundations/README.md), not to a new duplicate definition of ATT&CK in this article.

## Anatomy of a security threat-model claim

A model needs to say which part of reality it is intended to approximate.

| Facet | Model meaning | Common unsupported leap |
| --- | --- | --- |
| **System boundary** | Components, actors, interfaces and dependencies included | The diagram contains every possible interaction |
| **Protected interests** | Confidentiality, integrity, privacy, safety, availability or other valued conditions | Technical requirements exhaust all human consequences |
| **Actors / threat sources** | Relevant intentional, accidental and environmental sources | All actors' intentions are directly observable |
| **Policy and legitimacy** | Expected and prohibited actions, trust and exception conditions | Authentication alone proves an action was authorized |
| **Threat mechanisms** | Hypothesized paths, attacks, misuse, hazards and adverse events | Listing a threat proves it occurred |
| **System state and time** | Configuration, operating mode, privilege, recovery and temporal horizon | One snapshot describes the system's whole lifetime |
| **Controls and dependencies** | Protective functions and what they rely upon | Control inventory proves protection effectiveness |
| **Observation and evidence** | What sensors can observe, retain and substantiate | No records means no relevant activity occurred |
| **Exclusions and unknowns** | Deliberately omitted conditions versus unresolved facts | Out-of-scope means benign or impossible |
| **Validity conditions** | Assumptions and evidence under which conclusions apply | A consistent diagram is a complete real-world model |

This is an **editorial decomposition**, not a claim that NIST, OWASP or MITRE defines these as one obligatory ten-field schema.

## Assumptions are first-class security dependencies

Examples of assumptions include:
- “The public API is the only route through which a tenant can read private documents.”
- “Administrative operations require an independent authorization decision.”
- “The telemetry system records every relevant resource read during the modeled period.”
- “A supplier cannot replace executable code without verified authorization.”
- “An emergency operating mode preserves the same access restrictions.”
- “An adversarial source controls a user account but not the service runtime.”

Each is **conditional**, not a permanent fact. A scheduled export worker, privileged support interface, backup restore path, supplier update, or failover mode may invalidate one or more assumptions. Even a well-documented assumption can be false.

A useful model exposes the dependency: *Protection objective G depends on assumptions A1 through An, relevant controls, and a faithful relationship between modeled and deployed states.* That is stronger than an opaque statement that the architecture has already been “threat modeled.”

### Model scope: included, excluded, and unknown

Distinguish:
1. **Included:** the candidate path or source was explicitly modeled.
2. **Excluded:** the path or source was deliberately omitted within a declared boundary.
3. **Unknown:** the existence, relevance, reachability or evidentiary support of the path has not been established.

Excluded is not synonymous with impossible, and unknown does not mean malicious. A model may use a **closed-world assumption** for a bounded verification claim, but that assumption needs its own justification before someone asserts that every real interface or state was included.

## A model result is not automatically a result about reality

Let \(M\) be a chosen model, \(A\) its assumptions, \(G\) the modeled security goal, and \(S\) the real system within a particular context. For a **formal model with defined semantics and a valid proof or exhaustive check** of the relevant property, the conclusion might be expressed as

\[
M,A \models G.
\]

An **informal** architectural diagram may motivate a reasoned claim but does not establish this logical entailment merely by being consistent, detailed, or reviewed.

This means the represented model under its assumptions entails the property. It does **not** automatically show

\[
S \models G.
\]

To carry the claim to the real system, an analyst must justify the model-to-system **abstraction relation**, implementation fidelity, relevant environmental assumptions, and coverage sufficient for the particular property.

An overapproximating model may admit possible but unreachable behaviors; a counterexample in it can therefore be spurious. An underapproximating model may omit a real adverse path and thereby give false confidence in the absence of violations. **The direction and soundness of the abstraction relation matter**: a proof about all possible behaviors needs a justification that the real behaviors relevant to that property are represented, while an apparent counterexample still needs validation against concrete state and transition semantics. Whether the model is being used to prove **absence**, demonstrate **possibility**, or explain an **observed** event changes what evidence and guarantees are appropriate.

A complete search of a finite abstract state graph does not establish that the chosen graph represented all real system states. Conversely, an abstract counterexample does not on its own prove practical exploitation.

### The hunting-model analogue

Let \(H\) be a hypothesis about adversarial behavior, \(D\) the telemetry available, and \(O\) the observation that an analytic produces. A hunting model may derive expected observables conditional on \(H\) and declared sensor/behavior assumptions. But observing \(O\) does not logically establish \(H\) when benign alternatives can also produce \(O\).

For example, **repeated failed authentication attempts** can arise from hostile guessing, stale service credentials or user mistakes. Finding that pattern can justify deeper investigation, but not automatic actor attribution or a proven attack. Likewise, failing to observe it is not a proof of absence if sensors, retention or query scope are incomplete.

The distinction is the security-specific application of general inference: **expected evidence given a hypothesis is not equivalent to certainty about the hypothesis given the evidence**.

### Worked inference counterexample: a hunt analytic with an imperfect discriminator

Assume a purely hypothetical hunt population in which the proposed adversarial behavior has a **2% prior frequency**, an analytic matches **80%** of cases when that hypothesis is true, and it also matches **10%** of cases when it is false. These percentages are invented, **not** measured detection performance or a prevalence claim about threats.

\[
P(H\mid O)=\frac{P(O\mid H)P(H)}{P(O\mid H)P(H)+P(O\mid\neg H)P(\neg H)}
=\frac{0.80\times 0.02}{0.80\times0.02+0.10\times0.98}
=\frac{0.016}{0.114}\approx0.14035.
\]

Thus, **only about 14.04% of matching cases would satisfy this hypothesis under the stated model**, even though the analytic matches 80% when the hypothesis is true. Other threat prevalence, logging coverage, sensor dependence, alternative behaviors or selection of hunt terrain could change the result. This is an illustration of conditional inference, not a recommendation for using one positive predictive value to classify actual incidents. For individual cases, data lineage, system authorization, behavior context and corroborating evidence still matter.

## Comparing model classes without conflating their units

| Source or model | What it principally represents | What it does not prove |
| --- | --- | --- |
| [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Conditional risk-assessment factors: sources, events, vulnerabilities, impacts and uncertainty | An assessment scenario is an actual incident |
| [STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) | Prompts for classes of design threats | Every privacy, safety or abuse threat is represented |
| [OWASP abuse cases](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | Unwanted use and effects of expected features | A hypothetical abuse case proves an attack |
| [Attack trees](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | Goals, conjunctive prerequisites and alternative routes | A path is reachable or an actor used it |
| [MITRE ATT&CK](https://attack.mitre.org/resources/faq/) | Tactics, techniques, sub-techniques and reported procedures | A behavior label proves personal identity or a mandatory timeline |
| [MITRE CAPEC](https://capec.mitre.org/about/new_to_capec.html) | Reusable attack patterns and prerequisites | A specific weakness was exploited |
| [Diamond Model](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf) | Intrusion event and relationships among four event features | Every modeled feature is directly observed |
| [Unified Kill Chain](https://www.unifiedkillchain.com/) | Attack progression perspective | Every observed episode includes all stages |
| [MITRE TTP-Based Hunting](https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf) | Behavioral characterization linked to hypotheses, analytics, data and hunt execution | The predicted behavior is present or the analytic is complete |

Different models can be related without sharing a single **unit of analysis**, guarantee, representation or operational procedure.

The [W3C Threat Modeling Guide, Group Note Draft of June 23, 2026](https://www.w3.org/TR/threat-modeling-guide/) explicitly includes security, privacy, misuse/abuse and dependency threats in the scope of specification modeling. The publisher states that **Group Note Drafts are not endorsed by W3C or its members**; this is **a draft work in progress**, not a W3C Recommendation or universal norm.

## Draft standards and source-status boundaries

The official publication record for [NIST SP 800-154, Guide to Data-Centric System Threat Modeling](https://csrc.nist.gov/pubs/sp/800/154/ipd) still marks that document as an **Initial Public Draft published in March 2016**. Its January 2025 planning note expresses intent to finalize it, **not evidence that it has been finalized**. NIST SP 800-30 Rev. 1 (2012) is a final document with a different risk-assessment purpose.

The MITRE TTP-Based Hunting report is a **published methodology**, not an approval of its exact phases as mandatory. **Figure 3 (printed p. 10 / PDF index 11) was visually re-inspected for this review**, and its V diagram places malicious-activity characterization, hypotheses and data requirements alongside analytic implementation and hunt execution; this supports the distinction between a model and the activities that use it. OWASP Cheat Sheets are community-maintained guidance. ATT&CK is a living adversary-behavior knowledge base. A meaningful model comparison identifies actual versions, scopes and intended units rather than silently upgrading any source to a normative standard.

## Worked example: the model that overlooked an export path

Consider a fictional multi-tenant document service:

~~~text
Tenant --> Public API --> Object authorization --> Document store
                        |
                        +--> Audit event
~~~

A design threat model assumes that every document read passes the public API's object-authorization check. It concludes that correctly enforced tenant checks prevent cross-tenant reads for the **modeled routes**.

The real system also has a **scheduled export worker** that reads the same store under a service identity and separately defined export policy. The worker was omitted from the original diagram.

**Threat-model correction:** The modeled access-path inventory was incomplete. An independent policy boundary may apply to exports. Its adequacy is an open protection question; omission by itself is not proof that the worker is vulnerable.

**Threat-hunting-model consequence:** A hypothesis about cross-tenant access through an export workflow needs a **behavioral prediction**, such as records of export invocations and document-to-tenant access relationships. Analysts must determine which events are observable and retained, whether normal authorized exports produce similar traces, and what evidence could distinguish the hypotheses.

These are **linked but distinct analyses**. A threat model identifies a possible gap; a hunting model determines what observations could help assess whether the hypothesized activity occurred. Neither alone proves that anyone exploited the worker or that any tenant suffered harm.

| Claim | Supportable interpretation | Remaining uncertainty |
| --- | --- | --- |
| Public API has a policy check | One modeled route is explicitly mediated | Other real routes and modes |
| An export worker exists | Model scope omitted a relevant workflow | Whether its policy is safe |
| A hunt query found an export event | A record indicates activity at the export boundary | Actual content, policy legitimacy and actor intent |
| No export events appeared | Nothing matched the available records and search constraints | Sensor coverage, retention, hidden paths and actual absence |
| Exported data crossed a tenant boundary | Potential security-policy issue given valid event/content and tenant context | Whether it was authorized, harmful or adversarial |

This example is hypothetical and not an operational investigation.

## What each model can improve in the other

Threat models can supply **protected interests, candidate adverse paths, trust assumptions and expected attacker capabilities** for hunting hypotheses. Hunting evidence can, in turn, reveal **unmodeled interfaces, unexpected behaviors, misleading assumptions and actual control coverage gaps** that warrant revising a threat model.

This is a **feedback relationship**, not a claim that the models are interchangeable or that one must always precede the other. A hunt can originate from an incident report or anomaly without a completed system threat model. A threat model can improve a design before any production telemetry exists.

The [MITRE Cyber Analytics Repository glossary](https://car.mitre.org/resources/glossary/) distinguishes analytic hypotheses, observable behavior and analytic implementations. That separation is essential to prevent an abstract model from being mistaken for a verified detection.

## Canonical relationships and primary sources

- [SF-03-01, Threat Sources and Threat Events](threat-sources-and-threat-events.md): source-versus-occurrence distinction.
- [SF-03-02, Adversarial and Non-Adversarial Threat Sources](adversarial-and-non-adversarial-threat-sources.md): intentional versus non-intentional sources.
- [SF-03-03, Capability, Opportunity, and Intent](capability-opportunity-and-intent.md): actor ability, circumstances, targeting and hypothetical goals.
- [SF-03-04, Attacks, Deception, Abuse, and Misuse](attacks-deception-abuse-and-misuse.md): particular kinds of adverse conduct and abuse of legitimate workflows.
- [SF-03-05, Adversarial Tactics, Techniques, and Procedures](adversarial-tactics-techniques-and-procedures.md): tactic/technique/procedure meanings.
- [SF-03-06, Attack Paths, Stages, and Dependencies](attack-paths-stages-and-dependencies.md): state transitions, alternative paths and progression assumptions.
- [SF-10-08, Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md): evidence and inference strength.
- [SF-07-05, Control Placement and Coverage](../security-controls-defense-mechanisms/control-placement-and-coverage.md): whether an actual control covers the hypothesized path.
- [Operational Foundations](../../operational-foundations/README.md): **distinct Threat Hunting Models**, hunt hypotheses, analytics, investigations, and applied system threat-modeling practices.
- [Fundamentals](../../fundamentals/README.md): general models, abstraction, logic, state and evidence.

### Primary source starting points

- [NIST threat modeling glossary](https://csrc.nist.gov/glossary/term/threat_modeling), source-attributed to SP 800-53 Rev. 5; [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), risk factors, events and assumptions.
- [NIST SP 800-154](https://csrc.nist.gov/pubs/sp/800/154/ipd), **Initial Public Draft**, not finalized security-modeling requirements.
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html), complementary modeling approaches and their limits.
- [W3C Threat Modeling Guide](https://www.w3.org/TR/threat-modeling-guide/), **Group Note Draft, June 23, 2026**, broad specification-level threat, harm, misuse and dependency scope.
- [MITRE TTP-Based Hunting](https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf), report dated **March 2019**, Figure 3 printed p. 10 / PDF index 11, visually inspected for behavior/hypothesis/data/analytic/hunt distinctions.
- [MITRE TTP-Based Hunting and Detection Engineering Training](https://attack.mitre.org/resources/learn-more-about-attack/training/threat-hunting/), MITRE-maintained operational workflow modules.
- [MITRE Cyber Analytics Repository glossary](https://car.mitre.org/resources/glossary/), observable TTPs, analytic hypotheses and implementation distinctions.

**Editorial limitations:** Threat Models and Threat Hunting Models are recognized as separate, related model categories, but this article does **not** ratify a new internal knowledge-area label, grant operational methodology ownership to Security Foundations, or imply that hunting is only one fixed MITRE process. The equations and fictional system are explanatory models; they do not establish deployed-state correctness, actual attacker intent or detection effectiveness. The [separate Technical Review 10](../PILOT-TECHNICAL-REVIEW-10.md) checks eleven claim groups, including MITRE's hunting model-versus-methodology distinction, original source statuses, formal abstraction limits and the independently recomputed Bayesian counterexample. This manuscript is **Reviewed (model-assisted) / Core claims checked**, not Source-Verified, independently expert-approved, canonical-ratified or Published.

[Security Foundations](../README.md) · [Working area](README.md) · [Development and Verification Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
