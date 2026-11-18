# Security Foundations | Coverage, Completeness and Canonical Boundaries Review 03

**Review date:** November 18, 2026  
**Status:** Research-backed **working coverage review**, not internal taxonomy ratification or final publication acceptance.  
**Working baseline:** 12 **proposed** knowledge areas; **96 active candidate subjects**, both **flexible** and subject to further change.  
**Manuscript evidence:** 14 substantive pilots **Reviewed (model-assisted)** under [Pilot Technical Review 01](PILOT-TECHNICAL-REVIEW-01.md) (40 material groups), [02](PILOT-TECHNICAL-REVIEW-02.md) (10 groups), and [03](PILOT-TECHNICAL-REVIEW-03.md) (20 groups). **82 active candidates remain without pilot manuscripts**; this is a development-coverage count, not proof that 82 ideas are missing from the conceptual map.  
**Authority map:** [30 source groups](ESTABLISHED-MODEL-CROSSWALK.md); [34 working ownership cases](OWNERSHIP-BOUNDARIES.md).

## 1. What the first fourteen pilots establish

Across objectives, threat events, vulnerabilities, risk, access controls, information flow, cryptographic composition, observation, assurance, compromise, resilience, privacy, safety and ethical constraints, the pilots demonstrate that Security Foundations can provide **cross-domain security meaning and mechanism boundaries** without copying general Fundamentals or importing operational procedures as canonical definitions.

Specific distinctions now covered in bounded texts include:

| Concepts that must not be conflated | Established pilot material |
| --- | --- |
| Actual insecurity / unverified security | [Security and Insecurity](pilots/security-and-insecurity.md) |
| Threat source / threat event / observed violation | [Threat Sources and Threat Events](pilots/threat-sources-and-threat-events.md) |
| Weakness / vulnerability / exploit / compromise | [Vulnerabilities and Exploitability](pilots/vulnerabilities-and-exploitability.md), [Compromise and Loss of Security](pilots/compromise-and-loss-of-security.md) |
| Severity score / organizational risk | [Risk, Scenarios, and Time Horizon](pilots/risk-scenarios-and-time-horizon.md) |
| Authentication / authorization policy / actual enforcement | [Access-Control Policy Models](pilots/access-control-policy-models.md) |
| Authorized operation / information-flow property | [Information-Flow Security and Noninterference](pilots/information-flow-security-and-noninterference.md) |
| Encryption / authenticated message / anti-replay and session security | [Cryptographic Composition and Protocol Security](pilots/cryptographic-composition-and-protocol-security.md) |
| Event / observation / record / inference | [Observable, Observed, and Recorded](pilots/observable-observed-and-recorded.md) |
| Control selected / control functioning / control effective | [Controls, Safeguards, and Security Functions](pilots/controls-safeguards-and-security-functions.md) |
| Function restored / data restored / trust restored | [Resilience, Survivability, and Robustness](pilots/resilience-survivability-and-robustness.md) |
| Privacy / confidentiality / safety / reliability / ethics | [Security, Privacy, Safety, and Reliability](pilots/security-privacy-safety-and-reliability.md), [Ethical, Human, and Societal Constraints](pilots/ethical-human-and-societal-constraints.md) |

The coverage is **initial and example-driven**, not an exhaustive technical treatment of each concept across every asset, threat model or technology.

## 2. Source-grounded remaining gaps and depth priorities

These are **editorial work packages** rather than requests to automatically grow or freeze the inventory.

| Review case | Existing working owner | Substantive gap and evidence needed | Proposed action |
| --- | --- | --- | --- |
| SG-01 | SF-11-07 Recovery objectives and trusted restoration | RTO/RPO/MTD appear in an existing pilot but lack their own full source-defined treatment; recovery-state assurance is not captured by clocks alone | **Develop one canonical-owner pilot**, checking NIST SP 800-34r1 and SP 800-160v2r1 separately |
| SG-02 | SF-04-08 Side/covert channels and unintended leakage | A flow-property article mentions side channels, but does not adequately model leakage channel capacity, observation mechanisms or covert cooperation; never assume a model proves a real leak | **Develop separate weakness/leakage pilot** and compare with formal SF-08-09 |
| SG-03 | SF-10-08 Evidence/causality/attribution limitations | Several pilots contain bounded inferences, but the canonical security-evidence synthesis, evidence provenance, correlated observations and uncertainty are not authored | **Develop security-evidence pilot** with counterexamples and attribution limits |
| SG-04 | SF-12-05 Compliance vs effective security | Sources distinguish standards, control catalogs, tests and assurance, but the positive and negative cases for conformity without effective protection deserve coherent reference treatment | **Develop assurance/governance pilot**, avoid making compliance a simple yes/no security badge |
| SG-05 | SF-09-07 Key lifecycle and failures | Protocol pilot covers key/context binding; full rotation, compromise, storage, destruction, agility and post-quantum migration conditions remain beyond that scope | **Deepen via dedicated candidate pilot**, maintain FIPS/KEM/signature distinctions |
| SG-06 | SF-03-05/06 Adversarial TTPs and attack dependencies | Model crosswalk identifies ATT&CK tactics, CAPEC patterns, Diamond intrusion events and Unified Kill Chain progression, but no substantive canonical pair comparison exists yet | **Build behavior-vs-event-vs-progression pilot(s)** without imposing a fixed attack timeline |
| SG-07 | SF-02-05 Adverse outcomes, consequences and harm | After consolidating SF-02-06, coverage of affected interests, harm classes and time-dependent consequences needs a direct owner article rather than incidental mention in risk or privacy pilots | **Develop a consolidated harm pilot** and verify it need not split again |
| SG-08 | SF-07-04 defense in depth / SF-11-05 redundancy/diversity | Existing controls/resilience pilots discuss common-mode dependency but leave separate security goals versus implementation diversity insufficiently differentiated | **Depth and overlap review** before merging or adding subjects |
| SG-09 | SF-12-08 and SF-01-08 privacy/safety/human rights | New pilots define objective and ethical boundaries; full privacy threat analysis and functional safety engineering belong to specialized contexts/operational methods | **Keep current canonical boundaries**; integrate domain examples incrementally |
| SG-10 | All remaining models and source claims | Citation presence does not prove claim-to-source passage support, actual implementation, or standards version fidelity | **Create article-level source-verification ledger** and qualified review evidence, not an automatic Published state |

## 3. Consolidation tests to revisit when evidence grows

**The permission to contract is essential.** Potential duplicate ownership should be tested against actual prose, not titles:

- **SF-01-07** (accountability, attribution, non-repudiation), **SF-10-08** (evidentiary attribution limits), and **SF-12-04** (governance accountability) may overlap in terminology but concern **security claim**, **epistemic evidence** and **responsibility** respectively. Do not merge without demonstrated duplicate definitions.
- **SF-07-04** (defense in depth) versus **SF-11-05** (redundancy/common-mode failure): the former concerns safeguard layering, the latter system failure dependency and survivability. Distinct until evidence shows otherwise.
- **SF-08-03** (isolation/segmentation/containment design) versus **SF-11-03** (damage propagation and blast radius): structural protective mechanism versus resulting scope of damage.
- **SF-02-05** (general harm) versus **SF-05-03** (risk-scenario consequence estimation): actual affected interests and outcomes versus conditional estimates under a specific scenario/horizon.

The two historical consolidations **SF-02-06 → SF-02-05** and **SF-03-08 → SF-03-03 + SF-10-08** remain mapped in [Adjudication 02](ARCHITECTURE-ADJUDICATION-02.md). No additional merge or split is adopted by this review.

## 4. Current version and source caveats

- **NIST Privacy Framework 1.0** is a final 2020 publication. The 2025 Privacy Framework 1.1 **Initial Public Draft** remains distinguished from a final edition, per NIST's [project status](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11).
- **NIST SP 800-160v2r1 (2021)** provides cyber-resiliency goals, not a substitute for **NIST SP 800-61r3 (2025)** incident-response activities.
- **NIST SP 800-34r1** supplies the RTO/RPO/MTD distinction from a federal contingency-planning context; data recovery and trusted restoration are not equivalent.
- **ISO/IEC Guide 51:2014** was confirmed current in 2025; **IEC 61508-1:2010** remains listed as valid while later-edition work is presented as a preview in the IEC webstore.
- **RFC 9846 (2026)** supersedes RFC 8446 as current TLS 1.3; **ISO/IEC 15408-1:2026** supersedes the 2022 Part 1 edition. The earlier pilot audits and source crosswalk retain these source-version corrections.

## 5. Next execution and acceptance gates

1. Select the **highest-distinction** unpiloted subject cases, especially SG-01 to SG-04, for deep articles with formal definitions, assumptions, counterexamples and source citations.
2. Inspect original standards, model publications and relevant clauses, not merely the vendor or publisher's table of contents. Maintain source-version context and evidentiary limits.
3. Reconcile each new pilot against the proposed working ownership register, the Fundamentals general concept and Operational Foundations practice boundary. Cross-domain links are added **when real domain content develops**, never to fill a link quota.
4. Keep **architecture approval**, **model-assisted Reviewed**, **source-level Verified**, **independent expert acceptance**, and **Published** as distinct states.
5. Expand, consolidate or relocate area/subject headings whenever source evidence and prose support it, maintaining old-to-new mappings. **Twelve and ninety-six are currently useful snapshots, not targets.**

**No new heading, area, permanent canonical location, assessments or publication state is adopted by this review.**

[Security Foundations](README.md) · [Development Plan](DEVELOPMENT-PLAN.md) · [Pilot Register](pilots/README.md) · [Source Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md)
