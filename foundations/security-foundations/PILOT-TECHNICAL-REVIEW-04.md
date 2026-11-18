# Security Foundations | Pilot Technical Review 04: Evidentiary Inference, Trusted Recovery, and Security Effectiveness

**Review date:** November 18, 2026  
**Scope:** Three substantive area-first working manuscripts: **SF-10-08**, **SF-11-07**, and **SF-12-05**; eighteen material claim groups (six per article).  
**Method:** Separate model-assisted claim-led second pass after Draft authoring. Compared claim scope with publisher originals, inspected a source passage and rendered page where necessary, recalculated examples, challenged alternative explanations, and corrected inaccuracies or overgeneralizations before status promotion.  
**Disposition:** All three revised manuscripts pass the **scoped model-assisted review** recorded here. Eligible status: **Reviewed (model-assisted) / Core claims checked**. This is **not** complete clause-by-clause source verification, independent human peer review, taxonomy ratification, empirical system testing, professional legal advice, or final publication acceptance.

## 1. SF-10-08 | Evidentiary Confidence, Causality, and Attribution Limits

**Manuscript:** [Evidentiary Confidence, Causality, and Attribution Limits](security-observation-evidence/evidentiary-confidence-causality-and-attribution-limits.md)  
**Source orientation:** [W3C PROV-DM, Recommendation, 2013](https://www.w3.org/TR/prov-dm/) §§2, 5.3.2; [NIST SP 800-86, final, 2006](https://csrc.nist.gov/pubs/sp/800/86/final), publisher scope statement; [NIST SP 800-61 Rev. 3, 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final), incident-response context.

| Group | Material claim or test | Second-pass finding and boundary |
| --- | --- | --- |
| 10-01 | A record, observation, security interpretation, and attribution are distinct | **Supported as an editorial epistemic separation.** SP 800-86 addresses forensic examination of multiple data sources from an IT, not law-enforcement, perspective. Neither existence of a record nor the source's discussion alone establishes a real event's truth. |
| 10-02 | Provenance explains lineage but not truth | **Supported with qualification.** W3C PROV-DM defines entity/activity/agent relationships and `wasAttributedTo` in a provenance vocabulary. That relation is **not** automatically forensic attribution of a packet to a human adversary; the article now states the distinction explicitly. |
| 10-03 | Observation coverage, negative findings, and corroboration are conditional | **Conceptual review passed.** Absence of a log is weak evidence of absence if collection/retention/query coverage is unknown; shared dependencies undermine any assumption of independent corroboration. The article does **not** claim NIST defines a universal negative-evidence theorem. |
| 10-04 | Bayesian detector example and base-rate reasoning | **Recomputed.** 10,000 opportunities × 1% prevalence = 100 target cases; 100 × 90% sensitivity = 90 true alerts; 9,900 × 5% false-positive rate = 495 false alerts; PPV = 90/585 = **0.153846… (~15.4%)**. An error-rate model is **not proof of probability calibration**. Removed the unearned “calibrated” description and defined the M/A symbols. |
| 10-05 | Temporal ordering and statistical correlation do not uniquely establish causation | **Qualified.** The deployment/DNS/authentication diagram is a constructed possible common-cause explanation, not measured incident evidence. Clock errors, hidden common causes and selection effects remain possible. |
| 10-06 | Attribution requires specifying the entity and identity-binding level | **Supported as a bounded reasoning requirement.** IP, device, process, account, credential and human are different referents. PROV-DM's agent relation, a security event, and a human intent inference cannot be collapsed. NIST SP 800-61 Rev. 3 governs operational incident-response context rather than certifying identities. |

**Corrections recorded:** (a) replaced unjustified “calibrated” detector label; (b) explicitly defined modeled conditional event symbols; (c) distinguished checksum evidence from authenticated integrity and underlying truth; (d) separated PROV agent attribution from forensic human attribution. The 10,000-opportunity example remains invented and is not an empirical estimate of any real detector.

## 2. SF-11-07 | Recovery Objectives and Trusted Restoration

**Manuscript:** [Recovery Objectives and Trusted Restoration](security-failure-resilience/recovery-objectives-and-trusted-restoration.md)  
**Source orientation:** [NIST SP 800-34 Rev. 1, final updated 2010](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final), Chapter 3 §3.2.1 **printed p. 17 / PDF page index 30**, visually inspected; [NIST SP 800-184, final 2016](https://csrc.nist.gov/pubs/sp/800/184/final), recovery-planning abstract; [NIST SP 800-160 Volume 2 Rev. 1, final 2021](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), resilience engineering abstract.

| Group | Material claim or test | Second-pass finding and boundary |
| --- | --- | --- |
| 11-01 | Cyber-resiliency goals include anticipate, withstand, recover, adapt | **Supported by NIST SP 800-160v2r1** as goals/engineering capabilities rather than an ordered incident-response procedure. |
| 11-02 | Functional recovery and trusted restoration are different | **Defensible editorial synthesis** of protection and recovery requirements. A process answering requests does not itself prove clean authority, secure dependencies or acceptable data state. The specific six-dimension recovery decomposition is editorial, **not** a NIST-defined taxonomy. |
| 11-03 | RTO, RPO and MTD are non-equivalent | **Verified against the rendered NIST SP 800-34r1 Chapter 3 p. 17.** RTO concerns system-resource unavailability; MTD concerns mission/business-process disruption; RPO concerns the data point recoverable after disruption. The resource RTO should normally be shorter than MTD because business reprocessing may consume time. Edited the article to make that distinction explicit. |
| 11-04 | Modeled example: RTO and RPO windows | **Recomputed.** 09:40 to 10:50 = **70 minutes** (within 120 minutes); 09:30 to 09:40 = **10 minutes** (within 15 minutes), assuming recoverable valid required data and identical time conventions. Neither result establishes full business-process recovery, absence of malicious changes or exact transaction loss. |
| 11-05 | Backup-byte integrity is not compromise-free source integrity | **Supported as a qualified threat-model distinction.** Matching a digest or verifying a signature is not a proof that the signed/matching content was safe, complete, correct or created before a compromise. Correct use depends on key trust and chronology. |
| 11-06 | Recovery planning, trust evaluation and operational incident response have different owners | **Boundary supported.** NIST SP 800-184 concerns actionable recovery planning, while SP 800-160v2r1 addresses general cyber-resiliency engineering. Recovery execution, forensics and incident command belong to Operational Foundations; this article explains security-specific recovery claims. |

**Corrections recorded:** clarified resource RTO versus process MTD, added a primary-source page location and normal RTO/MTD constraint, made example timing arithmetic explicit, and bounded any RPO inference to complete/trustworthy recoverable data. **Not claimed:** that all source clauses were checked, that a backup is clean, or that any production environment meets its objectives.

## 3. SF-12-05 | Compliance and Effective Security

**Manuscript:** [Compliance and Effective Security](security-assurance-governance-accountability/compliance-and-effective-security.md)  
**Source orientation:** [NIST CSF 2.0, final 2024](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), outcome framework abstract; [NIST CSF FAQs](https://www.nist.gov/cyberframework/faqs), certification statement; [NIST SP 800-53 Rev. 5, Release 5.2.0](https://csrc.nist.gov/news/2025/nist-releases-revision-to-sp-800-53-controls), control catalog; [NIST SP 800-53A Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), assessment methodology; [NIST assessment-method glossary](https://csrc.nist.gov/glossary/term/assessment_method).

| Group | Material claim or test | Second-pass finding and boundary |
| --- | --- | --- |
| 12-01 | Compliance and effective protection ask different questions | **Defensible conceptual separation.** Compliance is rule-set-bound conformity; evidence of compliance is a separate determination. A conformity outcome requires scope, authority, version, timing and criterion. Corrected the draft's phrasing that treated compliance itself as necessarily already “demonstrated.” |
| 12-02 | NIST CSF 2.0 and certification | **Checked against official CSF FAQ.** NIST does **not** offer certification or endorsement of CSF-related implementations, products or services. CSF describes outcomes and resources, not a mandated universal control implementation. |
| 12-03 | Control catalog versus assessed control versus effectiveness | **Supported by publisher scopes.** SP 800-53 describes controls; SP 800-53A describes customizable assessment methodology/procedures. The NIST glossary attributes **examine, interview, test** to SP 800-53A Rev. 5. Official NIST pages identify **Release 5.2.0 (August 2025)** updates to both. |
| 12-04 | Neither bounded conformity nor bounded protection entails the other | **Logic reviewed.** The article's C and P predicates are explicitly editorial; without an additional premise connecting assessed baseline/scope to the protection goal/threat environment, neither universal implication follows. Added the missing converse non-implication for symmetry of the reasoning, **not** as a claim from NIST notation. |
| 12-05 | Sample-based 90-day log-retention example | **Qualified.** An assessor examining selected timestamps/configuration may support a bounded report about Application A, but samples alone do not prove *all* records meet retention criteria. Refined the example to distinguish reported conformity and actual adequacy of evidence; Application B's untested path is a separate broader protection concern. |
| 12-06 | Assessment coverage and time-limited claims | **Conceptual review passed.** “All assessed controls passed” does not entail complete threat coverage. Changed deployments can invalidate the applicability of historical evidence without making that historical finding retroactively false. The article does not purport to determine legal compliance for a real organization. |

**Corrections recorded:** separated conformity from evidence of conformity; expressed *both* non-implications; replaced “full assessment coverage” overclaim with a completed-assessment description; bounded the sample-based retention conclusion and its summary.

## 4. Calculations, source treatment, and remaining uncertainty

| Check | Result | Scope limitation |
| --- | --- | --- |
| Detector prevalence and base rate | 100 target cases, 90 true alerts, 495 false alerts, 585 total alerts; **90/585 ≈ 15.3846%** | Expected counts from explicitly hypothetical conditional rates; not real-world detector calibration or prevalence |
| Recovery timing | **70 min** from outage to stipulated function; **10 min** from checkpoint to outage | Model assumes comparable clocks, recoverable valid data, and an explicit service-level start/end; MTD and trust are not certified |
| Conformity logic | A countermodel exists in each direction (passes assessed retention; lacks other protection / protects against tested threat; misses independent obligation) | Editorial conceptual notation rather than a normative NIST equation |
| Evidence identity claim | Account login ≠ verified human actor; PROV agent-ascription ≠ forensic actor identity | Requires additional contextual identity evidence |
| Source edition | SP 800-34r1 (2010 updated), SP 800-184 (2016), SP 800-160v2r1 (2021), SP 800-86 (2006), SP 800-61r3 (2025), CSF 2.0 (2024), SP 800-53/53A 5.2.0 (2025), W3C PROV-DM (2013) | Those are source editions visibly checked; dates may change in future. Current official landing pages were used, not a guarantee of permanent currency |

**Review method and evidence limits:** The concrete RTO/RPO/MTD source passage on printed p. 17 of SP 800-34r1 was inspected in rendered PDF view. The public W3C PROV-DM recommendation's entities/activities/agents and attribution sections, NIST CSF certification FAQ, NIST SP 800-53A assessment-method glossary, and official standards landing-page descriptions/edition notes were checked in HTML. Mathematical and logical examples were recalculated. The remaining discussion is a **scoped review**, not complete crosswalked clause-by-clause verification of every article sentence or licensed publication.

### Outcome and process correction

- **Article status:** SF-10-08, SF-11-07 and SF-12-05 transition from **Draft** to **Reviewed (model-assisted)** only in the same reconciled change set that records this review.
- **Source-review status:** From **References listed** to **Core claims checked** for these bounded groups; **not Source-Verified**.
- **Architecture/publication:** No new subject/area approval, independent expert acceptance or Published claim.
- **Standing workflow correction:** After authoring a batch, the **next authoring-related execution should be its technical Review**, with corrections and register reconciliation, before beginning additional Draft work. If a review is blocked, leave the article Draft and report the actual blocker.

[Security Foundations](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Historical and Working Article Index](pilots/README.md) · [Working Ownership](CANONICAL-OWNERSHIP-REGISTER.md)
