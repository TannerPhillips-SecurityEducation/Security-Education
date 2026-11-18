# Security Foundations | Pilot Technical Review 02: Risk and Control Concepts

**Review date:** November 18, 2026  
**Scope:** Two newly authored working pilots: SF-05-01 *Risk, Scenarios, and Time Horizon* and SF-07-01 *Controls, Safeguards, and Security Functions*.  
**Method:** 10 material claim groups checked, five per article; conceptual distinctions, primary publisher scope, example arithmetic, alternative explanations, relation to eight previous pilots, and the Fundamentals/Operational Foundations boundary.  
**Outcome:** Both pilots pass this **bounded model-assisted technical review**, with development state **Reviewed (model-assisted)** and source state **Core claims checked**. This is **not** full passage-by-passage source verification, independent qualified human approval, published acceptance, or ratification of the 12-area/96-candidate working taxonomy.

## SF-05-01 | Risk, Scenarios, and Time Horizon

[Risk pilot](pilots/risk-scenarios-and-time-horizon.md) · **Principal sources:** [NIST SP 800-30 Rev.1](https://csrc.nist.gov/pubs/sp/800/30/r1/final), [FIRST CVSS v4.0](https://www.first.org/cvss/user-guide), [NIST SP 800-160 Vol. 1 Rev.1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final).

| Claim | Review finding |
| --- | --- |
| Risk relative to context | Risk relates possible adverse impact to scenario, protected interest, system assumptions and horizon; it is not an intrinsic property of a named vulnerability. |
| Probability and frequency | Historical counts/rates do not automatically determine future occurrence probabilities; threat initiation, success and impact have separate conditions. |
| Model scope and expected-loss example | Under stipulated probability 0.2, fixed loss 100, otherwise zero, the expected loss is 20. This does **not** prove a one-in-five-year occurrence or replace tail-risk analysis. |
| Inherent/residual/accepted risk | These labels depend on control baselines, assumptions, evidence and accountable decision context; a deployed control is not proof of proportional risk reduction. |
| CVSS v4 non-equivalence | FIRST explicitly distinguishes CVSS Base **severity** from full organizational risk, with Threat and Environmental metrics adding context rather than an exhaustive organizational assessment. |

**Recomputed check:** `0.20 × 100 + 0.80 × 0 = 20`. The “20” is an expectation under one synthetic two-outcome distribution, not a field observation, policy threshold or recommendation.

**Cross-domain distinction:** SF-02-05 owns generalized adverse harms; SF-05-01 owns risk scenarios/time horizon; SF-05-03 owns scenario-specific consequence estimation; Operational Foundations owns performing actual assessments and treatment processes. This article must not be merged blindly with a vulnerability scoring guide.

## SF-07-01 | Controls, Safeguards, and Security Functions

[Controls pilot](pilots/controls-safeguards-and-security-functions.md) · **Principal sources:** [NIST SP 800-53 Release 5.2.0](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls), [SP 800-53A Rev.5 and 2025 minor release](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), [MITRE D3FEND FAQ](https://d3fend.mitre.org/faq/), [NIST SP 800-160v2r1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

| Claim | Review finding |
| --- | --- |
| Protection objective vs selected/implemented control | Goals, stated requirements, specifications, implemented functions, observed results and supported assurance claims are different types of statements. |
| Prevent/detect/correct/recover distinctions | These are purpose labels, not automatically exclusive implementation classes, and a classified safeguard does not imply performance under all conditions. |
| NIST 800-53 vs 800-53A | NIST 800-53 is a **control catalog**; 800-53A supplies associated **assessment procedures**. Both have Release 5.2.0 updates announced August 2025; neither proves deployment efficacy by its existence. |
| D3FEND vs measured effectiveness | MITRE explicitly says D3FEND neither prescribes, prioritizes nor characterizes the effectiveness of defensive techniques. It is a vocabulary/knowledge graph, not a conformance certificate. |
| Worked denied-request/logging example | A denied request plus a recorded log can demonstrate bounded enforcement and record-generation for tested conditions, not complete mediation, zero leakage, or human operator attribution. |

**Cyber resiliency boundary:** NIST SP 800-160 Vol.2 Rev.1 identifies **anticipate, withstand, recover, adapt** as cyber resiliency goals; these are not a universal four-step incident-response procedure. The controls pilot refers to them as engineering properties while Operational Foundations owns conducting implementation and assessment work.

## Combined publication and architecture boundaries

- **Ten pilots now have substantive articles**: the previous eight passed [Pilot Technical Review 01](PILOT-TECHNICAL-REVIEW-01.md) (40 material groups), and these two passed **10 additional material claim groups**. These are **50 checked claim groups**, not 50 fully source-Verified article sentences.
- **Ten internally reviewed pilot articles** do not constitute ten approved final canonical Security Foundations subjects. Final area count and subject count remain **working, flexible 12/96**, rather than frozen targets.
- **No substantive reviewer falsely claims** access to complete licensed standard clauses, independent expert attestation, a published organizational risk assessment, or empirical measurements of a deployed security control.
- **Remaining next coverage checks:** Security failure and resilience (SF-11); privacy and safety distinctions (SF-01-08/SF-12-08); security observation inference; original formal security-policy sources; comprehensive claim-to-passage validation and architecture ratification.

[Security Foundations](README.md) · [Pilot Register](pilots/README.md) · [Development Plan](DEVELOPMENT-PLAN.md)
