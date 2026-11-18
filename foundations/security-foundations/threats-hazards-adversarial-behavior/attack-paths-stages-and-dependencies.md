# Attack Paths, Stages, and Dependencies

**Candidate subject:** SF-03-06 · Threats, Hazards & Adversarial Behavior  
**Working area:** [Threats, Hazards & Adversarial Behavior](README.md) · Fundamentals-style directory adopted; working area and subject semantics remain provisional  
**Artifact type:** Substantive security-knowledge reference, not an approved canonical publication or operational attack playbook  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 08](../PILOT-TECHNICAL-REVIEW-08.md), 9 article-specific material claim groups; full source-passage verification and independent expert acceptance pending  
**Architecture:** [Subject inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [SG-06 coverage finding](../COVERAGE-AND-GAPS-REVIEW-03.md) · [Working ownership register](../CANONICAL-OWNERSHIP-REGISTER.md)

## An attack is not necessarily a linear story

A security event may form part of a larger effort, but a sequence of observations does not automatically establish a single actor, an intentional plan, or a successful attack. An **attack path** is a hypothesized or demonstrated series of state transitions and enabling conditions through which an adversarial objective could be approached or achieved. A **stage** is a coarse conceptual grouping of activity within a chosen progression model. A **dependency** is a prerequisite or relationship governing whether a transition, capability or objective can be realized.

A path is a **relationship among conditions and actions**, not simply a chronological list of logs. A stage label is a model's explanatory device, not an objective timestamp or a law of nature. Dependencies can include reachability, privilege, identity trust, access to data, vulnerable state, environmental conditions or the cooperation of multiple services.

[NIST SP 800-30 Revision 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Chapter 3 Task 2-2 (printed p. 31), describes threat events crossing system boundaries and functional dependencies, including events defined through adversarial tactics, techniques and procedures (TTPs). It recognizes that multiple sources can initiate the same event type and one source can initiate multiple events. Its risk-assessment example structures do not make all intrusion activity follow one universal chain.

## Necessary states, transitions, and possible outcomes

An abstract attack-state model can be represented by a directed graph

\[
G=(V,E),
\]

where \(V\) represents **security-relevant system and actor states** and \(E\) represents **modeled state transitions**. A transition \(e:u\rightarrow v\) may require a guard condition \(g_e(s)\), representing some property of the current state \(s\).

For example, a transition from “account can access public data” to “account can access restricted data” might require some combination of authorization changes, a credential issue, an application flaw, or a policy exception. Those are **alternative mechanisms** that should not be flattened into one generic “privilege escalation” event without evidence.

A more precise model needs:
- **State variables:** privileges, trust relationships, relevant data custody, policy/configuration version and active sessions.
- **Transition conditions:** privileges, reachable resources, environmental events and applicable security rules.
- **Alternative branches:** different authorized or unauthorized ways to obtain the same effect.
- **Success conditions:** the specific security property or adversarial goal being evaluated.
- **Evidence map:** which changes or attempts could actually be observed at a given sensor or record source.
- **Time and continuity:** which transitions must precede others, which may overlap, and which records truly refer to the same actor or session.

The graph is an **authored abstraction**. It does not establish that a transition is exploitable, occurred in the world, or belongs to a named adversarial campaign. A path may be **logically permitted by a specified model**, **feasible under a real configuration**, **observed in part**, or **contradicted by reliable evidence**. These are separate evidential claims. One feasible modeled path does not prove that a real actor knows or attempts it.

## Feasibility is not probability, and a path is not proof

Let \(P=(e_1,\ldots,e_k)\) be a proposed path. Its feasibility can be described informally as requiring that the precondition for each transition be satisfied in the state reached by the preceding transition.

\[
\operatorname{Feasible}(P,s_0)
\Rightarrow
\bigwedge_{i=1}^{k} g_{e_i}(s_{i-1}),
\]

where \(s_{i-1}\) is the state before transition \(e_i\). This is **a necessary-condition implication within the constructed model**, not a sufficient test of exploitation. It requires **the guards to hold in the evolving states actually reached**, plus a valid transition relation. Checking every guard against one initial configuration snapshot would be incorrect. The notation itself does not establish that the model's edges are executable on a deployed system.

Even if every guard is satisfied in the model and the transitions are defined, there may be no evidence that the actor selected this path, that an event occurred, or that an observed action was unauthorized. Model feasibility, environmental reachability and **observed traversal** are distinct claim levels. A configuration snapshot can support a precondition claim, but cannot prove the state was identical during an earlier incident.

A proposed path also need not yield a meaningful **probability of success**. Multiplying individually guessed probabilities such as “70% chance at step A × 50% at step B” is unjustified if steps share dependencies, the attacker can retry, or probabilities are conditional on earlier states. Probabilistic risk modeling belongs to [Security Risk & Uncertainty](../security-risk-uncertainty/README.md).

## AND requirements and OR alternatives

The same target outcome may depend on several necessary conditions or on one of multiple alternative routes.

A conceptual security property might require that an unauthorized path remain unavailable unless two prerequisites are simultaneously present:

\[
\operatorname{PathAvailable}=R\land C,
\]

where \(R\) means a relevant protected interface is reachable and \(C\) means the actor possesses some usable credential or enabling state. This **does not assert that every attack involves a credential**, and neither variable is a general statement about legal authorization.

If there are two alternative paths,

\[
\operatorname{AnyPath}=P_A\lor P_B.
\]

For the constructed model, blocking \(P_A\) does not eliminate \(P_B\). Equally, a control common to both branches can be a shared dependency whose compromise or failure affects both. These Boolean expressions describe logical structure, not event frequencies, empirically complete coverage, or bypass instructions. In particular, **blocking the represented Route A only eliminates the represented Route A**. To claim the goal itself is prevented, all feasible alternative routes and any shared state transitions in the declared boundary must be considered.

~~~text
                     Modeled objective
                      /           \
                     / OR          \
                Route A          Route B
                 /  \              /  \
             pre A1 pre A2     pre B1 pre B2
                 AND              AND
                     \           /
                      \         /
                possibly shared service
                   or trust dependency
~~~

The diagram is intentionally abstract. It is not a recipe for accessing a particular real system or a verified threat graph. An organization may reduce reachable paths by changing legitimate controls, but efficacy requires evidence about *every* path in the claimed coverage scope.

## An observed order is not always a causal order

A log sequence ordered by timestamp is not automatically a faithful sequence of actions. Device clocks may differ, data may be buffered or retried, and log collection may record receipt time rather than event occurrence time. Independently initiated actions can overlap.

A **temporal sequence** says events appear in an order. A **causal explanation** says some event or state enabled or produced another under specified assumptions. A **stage mapping** says the activity resembles one of the categories in a chosen model. Those are distinct claims.

For example, an event timestamped after a suspected credential theft might be causally unrelated. A login can succeed without the visible earlier failed-login events having contributed to its success. An access to one resource does not automatically imply earlier compromise of every intermediate system.

The [Diamond Model of Intrusion Analysis](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), printed p. 9 (**Figure 1, PDF index 8, visually inspected**), defines a modeled intrusion **event** with adversary, capability, infrastructure and victim. The four core features and optional meta-features help relate event hypotheses, even when particular features remain unknown; recording a diamond does not independently prove all four features. Its activity-thread and activity-group concepts relate events at higher levels. This is an analyst's explanatory event-relationship framework; a graph of related events is not by itself proof of shared human authorship.

## A progression model has its own unit of analysis

Several published models give different views:

| Model | Main representation | What it explains | What it must not be turned into |
| --- | --- | --- | --- |
| [MITRE ATT&CK](https://attack.mitre.org/resources/faq/) | Tactical goals and behavioral methods | The reason/method categories for observed or hypothetical adversarial actions | Required chronological phases of every intrusion |
| [Unified Kill Chain](https://www.unifiedkillchain.com/) | Progression phases grouped as Getting In, Hacking Through and Taking It Out | Where different actions fit within a model of adversarial progression | Universal evidence that all phases occurred in order |
| [Diamond Model](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf) | Intrusion event and linked events/activity threads | Actors, victim, capability and infrastructure relations with time/phase metadata | Automatic attribution or unique historical reconstruction |
| [MITRE CAPEC](https://capec.mitre.org/about/new_to_capec.html) | Reusable attack patterns with prerequisites and execution-flow descriptions | Common design abstractions of adversarial methods | Proof that one system was exploited or all patterns apply |

The **Unified Kill Chain** is helpful in distinguishing high-level movement **into**, **through**, and **out of** an environment, but its publication-specific number and arrangement of phases are properties of the **UKC model**, not universal causal laws. A defender may observe an activity consistent with one phase while missing other phases because an adversary started from an existing credential, because coverage is partial, or because no broader intrusion occurred.

ATT&CK tactic names also do not substitute for actual stage transitions. A behavior mapped to *Discovery* could occur before or after actions classified as *Persistence* in some episodes. The model's labels are not temporal assertions.

## Repetition, branching, convergence and incomplete histories

An adversarial episode can contain:
- **repeated actions:** several attempts toward the same purpose, perhaps with different parameters;
- **branching:** multiple methods considered or attempted;
- **convergence:** different paths producing the same capability or observed result;
- **loops:** revisiting a state after recovery, failed action or changed authorization;
- **parallel activity:** multiple actors, hosts or processes interacting concurrently;
- **missing observations:** events outside the collection vantage, retention period or available evidence.

A model restricted to a directed acyclic graph (DAG) may be useful for a particular planning problem, but it is **not universally adequate** when actions can repeat or system state can return to a prior condition. A time-expanded DAG can sometimes encode repeated state transitions, at the cost of more nodes and assumptions, without claiming the real intrusion was acyclic.

A chain in which every stage is assumed to have happened because a later stage was observed is a reconstruction error. Observation of data transfer does not prove initial exploitation. A credential may have been legitimately issued, stolen or misconfigured. Hypotheses must retain those alternatives.

## Worked example: an incomplete three-event account history

Consider a fabricated case in which telemetry records:

| Approximate observation | Narrow claim supportable if records are valid | Unknown or alternative |
| --- | --- | --- |
| 09:10 | An account authenticated to a service | Who controlled it, whether use was legitimate |
| 09:18 | A process associated with the session requested a set of resources | Whether the resources were protected or enumerated for an unauthorized purpose |
| 09:27 | A network endpoint transmitted bytes | Whether those bytes were sensitive, related to the earlier requests, or exfiltrated |

A storyteller could construct a linear “initial access → discovery → exfiltration” narrative. The records do **not** by themselves establish those classifications, causality, intent or shared actor identity. A legitimate report export can produce similar artifacts. The network flow may be unrelated to the session. Timing alone may be unreliable.

To assess the **hypothesized** chain, additional evidence would be needed about authorization, object identity, actual content, processes, session continuity, data lineage and sensor reliability. The example therefore distinguishes **possible path**, **observed activity** and **causally justified reconstruction**.

This is not a real investigation, attack recipe or assertion that a named model has exactly three stages.

## Defenders need a coverage claim, not a colorful timeline

Understanding attack paths can support rigorous defensive questions: which prerequisites are actually necessary, which trust boundaries prevent unauthorized transitions, which alternate routes remain possible, and what observations would substantiate an intervention's effectiveness?

A layer described as “preventing lateral movement” needs a defined adversarial capability, route, reachable assets, authorization state and control behavior. Installing a firewall does not establish that every alternate identity or software path is blocked; the security claim must be tied to actual coverage.

[Controls, Safeguards, and Security Functions](../security-controls-defense-mechanisms/controls-safeguards-and-security-functions.md) owns the conceptual distinction between a listed control, deployed mechanism and achieved protection. Detailed engineering and operation of attack-graph analysis, hunting, response or attack simulation belong to [Operational Foundations](../../operational-foundations/README.md).

## Cross-domain relationships, primary sources and review limits

- [Adversarial Tactics, Techniques, and Procedures](adversarial-tactics-techniques-and-procedures.md) owns tactic/method vocabulary; path models own transitions and dependencies that can connect behaviors.
- [Capability, Opportunity, and Intent](capability-opportunity-and-intent.md) owns the actor- and circumstance-relative requirements for possible action.
- [Adversarial and Non-Adversarial Threat Sources](adversarial-and-non-adversarial-threat-sources.md) owns intentional versus non-intentional origins.
- [Threat Sources and Threat Events](threat-sources-and-threat-events.md) owns what counts as a potential source or occurrence.
- [Vulnerabilities and Exploitability](../weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) owns enabling weaknesses; a route alone need not contain an exploitable software bug.
- [Evidentiary Confidence, Causality, and Attribution Limits](../security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md) owns what records prove about causal links and identities.
- [Value, Criticality, and Dependencies](../protected-interests-assets-harm/value-criticality-and-dependencies.md) owns why system dependencies matter to protected interests.
- [Fundamentals: State, Events and Transitions](../../fundamentals/models-abstraction/state-events-and-transitions.md) and [Fundamentals: Graph Theory](../../fundamentals/mathematics-logic/graph-theory.md) own general mathematical structure.
- [Operational Foundations](../../operational-foundations/README.md) owns procedures for threat modeling, technical analysis and defensive validation.

**Primary source starting points:** [NIST SP 800-30 Rev. 1 (final 2012)](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Chapter 3 Tasks 2-1/2-2, relevant threat-event dependencies and Appendix E; [MITRE ATT&CK FAQ](https://attack.mitre.org/resources/faq/) and [Enterprise introduction](https://attack.mitre.org/resources/enterprise-introduction/) for behavior categories rather than fixed chronology; [MITRE CAPEC](https://capec.mitre.org/about/new_to_capec.html), pattern prerequisites/execution flow; [Diamond Model](https://securityandtechnology.org/wp-content/uploads/2020/07/diamond.pdf), Figure 1 printed p. 9 plus activity-thread relationship; [Unified Kill Chain](https://www.unifiedkillchain.com/), source-specific progression framing.

**Editorial limitations:** The formal graph, transition guards, AND/OR constraints and all examples are authored models, not measured paths, exploitation instructions, attack-likelihood calculations or proofs about a live incident. The cited progression frameworks have different purposes and are not translated one-to-one. The separate [Technical Review 08](../PILOT-TECHNICAL-REVIEW-08.md) checked nine material claim groups, including guarded transitions, two-path logic, model-versus-reality boundaries and the original Diamond/UKC/ATT&CK source distinctions. This manuscript is **Reviewed (model-assisted) / Core claims checked**, not a verified live attack graph, empirically calibrated threat likelihood, forensic reconstruction, full source-passage verification, independent expert acceptance, fixed taxonomy or Published article.

[Security Foundations](../README.md) · [Working area](README.md) · [Development register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
