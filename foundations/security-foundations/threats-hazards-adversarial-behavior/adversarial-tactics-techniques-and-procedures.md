# Adversarial Tactics, Techniques, and Procedures

**Candidate subject:** SF-03-05 · Threats, Hazards & Adversarial Behavior  
**Working area:** [Threats, Hazards & Adversarial Behavior](README.md) · Approved Fundamentals-style directory pattern; internal area/subject ownership provisional  
**Artifact type:** Substantive security-knowledge working manuscript, not an accepted permanent canonical publication  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 08](../PILOT-TECHNICAL-REVIEW-08.md), 8 article-specific material claim groups; full source-passage verification and independent expert acceptance pending  
**Architecture:** [Working candidate inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Coverage review SG-06](../COVERAGE-AND-GAPS-REVIEW-03.md)

## An objective is not the method, and the method is not an occurrence

**Tactics, techniques, and procedures (TTPs)** are a useful vocabulary for distinguishing different dimensions of adversarial behavior. A **tactic** denotes a tactical goal or purpose within a model of adversarial conduct. A **technique** denotes an abstract method by which that goal may be accomplished. A **procedure** denotes how an actor actually implements or uses one or more techniques in a concrete operation. Procedures can include tools, commands, infrastructure, timing and other details in a particular case.

The distinctions are source-grounded, not merely semantic preference. The [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/) expressly defines tactics as the *why* of an ATT&CK technique, techniques as the *how*, sub-techniques as more specific behavior, and procedures as **specific implementations** of techniques or sub-techniques. A procedure example in ATT&CK describes behavior documented through reported observations; it is not an instruction that every adversary will repeat it.

An ATT&CK technique label does **not** mean the corresponding event occurred on a particular computer. A detection rule mentioning a technique does not independently prove that the technique was used. Identifying a tactical category does not reveal the actor's ultimate political, financial or personal motive.

| Concept | Question | Illustrative interpretation | Not established |
| --- | --- | --- | --- |
| Strategic objective | Why does an actor ultimately want the result? | Obtain data for an external purpose | Proven individual motive from a protocol field |
| Tactic | What is the immediate tactical aim in ATT&CK? | Credential Access | A definite stage number in a required attack sequence |
| Technique | What general behavior serves that aim? | Accessing credential material by an operating-system method | The method's presence in one specific incident |
| Sub-technique | What more specific behavior does a technique classify? | A particular kind of credential-store access | Which tool, operator or victim was involved |
| Procedure | How a source used methods in particular conditions | A documented implementation combining multiple techniques | A universal recipe or a reliable attribution of identity |
| Event or record | What actually occurred or was observed | A process accessed a protected location | The entire actor's goal, origin, or incident history |

This table includes **strategic objective** and **event** as adjoining explanatory concepts. Those are not extra mandatory levels in ATT&CK's formal data model.

## Why behavior categories are not chronological stages

MITRE ATT&CK's [Enterprise introduction](https://attack.mitre.org/resources/enterprise-introduction/) organizes adversary behavior using **tactical objectives and techniques**. The taxonomy includes activities associated with discovery, access, persistence, command and control, collection or other goals, but the categories are **not a universal temporal program**.

A single behavior may serve multiple goals, and an adversary might repeat techniques, skip some, pursue different objectives in parallel, or act through legitimate credentials. A classification of behavior can therefore remain correct without establishing the order of the broader intrusion.

Likewise, an ATT&CK technique may be used through a variety of procedures or technological platforms, and one procedure can include **multiple** techniques. This is stated in the [MITRE ATT&CK Design and Philosophy paper, §3.4.1, printed p. 9 / PDF page index 18](https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf), **visually inspected**. That paper was revised in **March 2020**; it records the model's then-current design, not the complete technique inventory or detection coverage in November 2026. The [live ATT&CK catalog](https://attack.mitre.org/) may rename, deprecate or revise techniques and platforms.

**ATT&CK coverage is evidence-based but not exhaustive**: absence of a technique from a currently examined matrix does not prove an action is impossible or has never occurred. Nor does the existence of a technique in a matrix establish a specific organization's exposure.

## Techniques are abstractions of behavior

An abstract technique description removes implementation details to express a recurring adversarial method. That abstraction makes it useful across operating systems, identities and telemetry sources, but it also creates a danger: two concrete activities that share a category are not necessarily equivalent in consequence or detectability.

Consider the tactical objective of gaining credentials. Different techniques may obtain passwords, token material, cached secrets, configuration files or delegated privileges under very different conditions. A broad tactic tells us *why* certain methods might be relevant, not whether all such resources exist or are readable in a particular target.

Sub-techniques can refine the meaning of a technique. Yet an analyst should not assume that a technique's entire set of sub-techniques is mutually exclusive, complete in every release, or always distinguishable from available observations.

A useful conceptual representation is:

~~~text
Tactical goal
     |
     +---- Technique A ------ Sub-technique A.1
     |         |              Sub-technique A.2
     |         +---- procedure examples, if documented
     |
     +---- Technique B ------ one or more implementations
     
Evidence of actual event != automatic proof of every ancestor,
related technique, actor identity or final strategic objective
~~~

An ATT&CK label should be linked to the behavior it describes. It should never function as a shortcut that conceals missing evidence.

## What is a procedure?

A procedure is not simply “the last item in a list.” In ATT&CK, procedures describe **specific observed implementations of behavior** that can include several techniques, tools and environmental choices. A published tool's theoretical capabilities do not establish that a particular actor deployed all of them. In ATT&CK, the **Procedure Examples** field documents source-reported observed-in-the-wild uses of techniques; a locally hypothesized procedure is a useful analytic description but should not be presented as a catalog-verified observed procedure without its own evidence.

For a hypothetical, defensive incident record, imagine three observed phenomena:
1. a new session uses an existing authorized credential;
2. a process reads a configuration artifact;
3. data moves through a network connection.

The sequence alone does not prove a single malicious procedure. A legitimate administrator, automated deployment process or intruder could all produce portions of such a trace. Determining whether it forms one actor-driven procedure would require context, continuity of identity, causality, data content and independent evidence. **A procedure is an interpretation of concrete conduct**, whereas raw logs are observations or representations of it.

[Observable, Observed, and Recorded](../security-observation-evidence/observable-observed-and-recorded.md) and [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) own this evidence-to-conclusion distinction. SF-03-05 owns the behavioral vocabulary, not the forensic proof of attribution.

## ATT&CK, CAPEC, and Diamond describe different objects

[MITRE CAPEC](https://capec.mitre.org/about/new_to_capec.html) catalogs **attack patterns**: recurrent abstractions of how certain kinds of attacks can be performed. CAPEC entries can describe prerequisites, mechanisms, consequences, execution flows and relationships to weakness classes such as CWE. MITRE's [CAPEC-versus-ATT&CK comparison](https://capec.mitre.org/about/attack_comparison.html) emphasizes CAPEC's **application weakness/attack-pattern** use and ATT&CK's **operational adversary-behavior** use; the scopes overlap but are not interchangeable. CAPEC's execution-flow steps are pattern-level possible actions, **not** a transcript of a particular incident or proof of an exploited weakness.

The [Diamond Model of Intrusion Analysis](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf) describes an *intrusion event* through **adversary, capability, infrastructure and victim**. In its Figure 1 (printed p. 9), capability and infrastructure are related to the event's other features. A Diamond event can be enriched with method/phase/time metadata; a method label by itself does not establish all four features.

The three vocabularies have different units of analysis:

| Framework | Primary explanatory unit | Useful relationship | Wrong substitution |
| --- | --- | --- | --- |
| MITRE ATT&CK | Tactic, technique, sub-technique, documented procedure | Map behavior to a tactical goal and concrete platform context | Treat tactic row as a mandatory chronology |
| MITRE CAPEC | Reusable attack pattern | Relate patterns and exploit-relevant conditions | Treat attack pattern as proof a target was exploited |
| Diamond Model | Intrusion event and its core relational features | Connect adversary, capability, infrastructure and victim in an event hypothesis | Treat a capability or IP address as proven real-world attribution |
| Unified Kill Chain | Progression model for adversarial operations | Compare stages of hypothetical or observed progression | Infer a fixed 18-step path for every intrusion |

The [Unified Kill Chain](https://www.unifiedkillchain.com/) groups progression into **Getting In, Hacking Through, and Taking It Out**. Its specific version and phases belong to that model, not to ATT&CK's tactic definitions. The fact that two frameworks describe parts of the same episode does not make their labels interchangeable or require one-to-one mapping.

## Working example: one action, several plausible classifications

Imagine an application that permits ordinary users to authenticate and view documents belonging to their own groups. A telemetry source records a successful login followed by requests that enumerate a document catalog.

**Observation:** A session requested catalog endpoints.

**Possible derived behavior:** The session explored available data or application objects.

**Tactic hypothesis:** Depending on evidence, this might be related to discovery or collection objectives in an ATT&CK context.

**Actual policy claim:** Whether access was unauthorized depends on what the user was permitted to enumerate and whether protected data was returned.

**Actor interpretation:** The same requests could arise from the application's normal search function, an administrator, an approved test or an unauthorized actor. Nothing in the HTTP requests alone proves the actor's intent or identity.

A rule that labels every catalog request “ATT&CK Discovery” without declaring its detection model is an overbroad inference. The fact that ATT&CK contains a technique does not make every superficially similar program action malicious.

## TTPs can persist while infrastructure changes

An adversary can change network endpoints or tool filenames without changing a meaningful underlying technique. Conversely, the same public utility can be used in several unrelated techniques and legitimate workflows.

For this reason, a TTP description should avoid reducing behavior to one IP address, hash, filename or port. Those artifacts can be useful observations, but they are not interchangeable with **behavioral method**. A classifying analyst must specify which invariant or sequence of effects supports the interpretation.

This also explains why models have different **stability levels**: a file hash represents a particular artifact; an ATT&CK technique groups behavior across implementations; a tactical objective is a broader purpose within ATT&CK's model. Neither abstraction inherently measures how much effort it takes an adversary to change that behavior or how reliably a defender can detect it. The [Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) is a useful heuristic for discussing relative adversary costs of changing indicators, but not a quantitative law applying to every system.

## Mapping behavior requires three separate claims

When a security narrative assigns an ATT&CK technique, three questions should be separate:

1. **Observed behavior:** Did the described behavior occur, based on a trustworthy sensor and available evidence?
2. **Model fit:** Does the behavior satisfy the technique's actual definition and platform scope, including the chosen ATT&CK release?
3. **Adversarial relevance:** Is there evidence that the activity was adversarial, and is the attributed actor/intent justified?

Answering the second question does not settle the other two. **ATT&CK coverage is neither a truth label for a telemetry record nor an identity-attribution mechanism**; the analyst must distinguish the behavior's evidence, mapping fit, and adversarial interpretation. A single documented procedure may span several mapped techniques, and a technique may be used in legitimate activity. One could correctly map a legitimate red-team exercise to a technique without asserting a malicious criminal event. An analyst might observe a suspicious artifact that fits several techniques, requiring further evidence.

Not every model entry supplies a unique detection rule. ATT&CK's observed behavior classes are not normative requirements for software, and CAPEC's attack-pattern fields are not a complete security-testing program. Procedures for performing the mapping, managing detections and conducting hunts belong to [Operational Foundations](../../operational-foundations/README.md).

## Canonical boundaries and primary sources

- [Capability, Opportunity, and Intent](capability-opportunity-and-intent.md) owns actor abilities and inferred objectives at the actor/context level. **An ATT&CK tactic is a specific tactical objective**, not the actor's final motive.
- [Adversarial and Non-Adversarial Threat Sources](adversarial-and-non-adversarial-threat-sources.md) owns source categories and the distinction between intentional and accidental threat origins.
- [Attack Paths, Stages, and Dependencies](attack-paths-stages-and-dependencies.md) owns how multiple events and transitions can be connected; one TTP does not define a full route.
- [Threat Sources and Threat Events](threat-sources-and-threat-events.md) owns the distinction between potential source and occurrence.
- [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) owns enabling conditions; a technique label does not prove exploitability.
- [Fundamentals: Models & Abstraction](../../fundamentals/models-abstraction/README.md) owns general categories and the difference between representation and reality.
- [Operational Foundations](../../operational-foundations/README.md) owns live TTP mapping, testing, hunting and response.

**Primary source starting points:** [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/), source-defined tactic/technique/sub-technique/procedure meanings; [ATT&CK Enterprise introduction](https://attack.mitre.org/resources/enterprise-introduction/), intended scope and observed behavior; [MITRE ATT&CK Design and Philosophy](https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf), §3.4.1 on procedures spanning multiple techniques; [MITRE CAPEC introduction](https://capec.mitre.org/about/new_to_capec.html), attack patterns versus weaknesses and observations; [Diamond Model of Intrusion Analysis](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), Figure 1, printed p. 9; [Unified Kill Chain](https://www.unifiedkillchain.com/), progression model and three named clusters.

**Editorial limitations:** The session and catalog examples are hypothetical. Framework names and publication references are source starting points, not proof that each taxonomy is comprehensive, current in every detail or validated against a real incident. The separate [Technical Review 08](../PILOT-TECHNICAL-REVIEW-08.md) documented eight material claim groups, ATT&CK's live tactic/technique/procedure vocabulary, the inspected MITRE 2020 design paper and CAPEC/Diamond/UKC boundary checks. Status is **Reviewed (model-assisted) / Core claims checked**; no exhaustive current ATT&CK release audit, independently verified incident mapping, complete passage-level source review, independent peer acceptance, canonical taxonomy ratification or Published status is asserted.

[Security Foundations](../README.md) · [Working area](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
