# Security Foundations | Pilot Technical Review 03: Failure, Resilience, Privacy, Safety and Human Harm

**Review date:** November 18, 2026  
**Scope:** Four new substantive **working pilots**, not ratified permanent canonical subjects: SF-11-01, SF-11-04, SF-01-08, SF-12-08.  
**Method:** Scoped model-assisted technical/editorial review of **20 material claim groups** (five per article); inspected NIST/ISO/IEC/UN publisher descriptions and glossary meanings; visually inspected **page 17 (PDF page index 30)** of NIST SP800-34r1 for the RTO/RPO/MTD definitions; independently recomputed mathematical examples and checked source-version caveats.  
**Disposition:** All four pilots pass the bounded conceptual, example and primary-source-scope audit. **Reviewed (model-assisted) / Core claims checked** may be recorded for each. Full source-passage verification, independent expert acceptance, architecture ratification and final Published state are **not** claimed.

## Review ledger: five material claim groups per pilot

### SF-11-01 · Compromise and Loss of Security

**Article:** [compromise-and-loss-of-security.md](pilots/compromise-and-loss-of-security.md)  
**Primary source orientations:** [NIST compromise glossary](https://csrc.nist.gov/glossary/term/compromise); [NIST incident glossary](https://csrc.nist.gov/glossary/term/security_incident); [NIST SP 800-61r3 (2025)](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

| Group | Material claim reviewed | Finding and limit |
| --- | --- | --- |
| 01 | Compromise is source/context-dependent | NIST glossary includes distinct senses of unauthorized disclosure, policy violation, compromise judgment, and keying-material compromise. Do not replace them with one unqualified system-wide binary. |
| 02 | Threat attempt vs security violation | An attempted exploit and a demonstrated unauthorized outcome are not the same; a denied test request does not establish compromised state. |
| 03 | Evidence vs attribution | A successful protected read under an unauthorized account may substantiate a bounded property violation; a log alone does not prove human actor or intent. |
| 04 | Containment, function and trustworthy restoration | Constraining effects, restarting service, recovering data and demonstrating trusted security state require distinct evidence. |
| 05 | Incident workflow boundary | NIST SP 800-61r3 supersedes Rev.2 and guides practical risk-aligned incident response; it is an operational method, not an ontology of every compromise state. |

### SF-11-04 · Resilience, Survivability, and Robustness

**Article:** [resilience-survivability-and-robustness.md](pilots/resilience-survivability-and-robustness.md)  
**Primary source orientations:** [NIST SP800-160 Vol.2 Rev.1 (2021)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final); [NIST SP800-34 Rev.1 (2010)](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final); [NIST glossary: cyber resiliency](https://csrc.nist.gov/glossary/term/cyber_resiliency)

| Group | Material claim reviewed | Finding and limit |
| --- | --- | --- |
| 01 | Resilience goal scope | NIST SP800-160v2r1 defines anticipate, withstand, recover and adapt as cyber-resiliency goals, not four mandatory chronological incident-response steps. |
| 02 | Robustness/reliability/survivability | Distinct models of bounded disturbance, function over time, preserving critical mission and adapting under adversity. None implies protection against every attack. |
| 03 | Common-mode dependence | Replication can maintain service while retaining a shared compromised key or erroneous dependency; redundant systems do not automatically fail independently. |
| 04 | RTO vs RPO vs MTD | NIST SP800-34r1 chapter 3 page 17 distinguishes maximum resource unavailability, recoverable data point and total tolerable mission/business outage. Its procedure scope is federal contingency planning. |
| 05 | Worked recovery example | 09:40 interruption, 11:00 functional recovery means 80 minutes: within two-hour RTO. Last usable state 09:00 is 40 minutes old: misses a stipulated 15-minute RPO if there are no later recoverable changes. Neither proves trusted restoration. |

### SF-01-08 · Security, Privacy, Safety, and Reliability

**Article:** [security-privacy-safety-and-reliability.md](pilots/security-privacy-safety-and-reliability.md)  
**Primary source orientations:** [NIST Privacy Framework v1.0 final (2020)](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final); [ISO/IEC Guide51:2014](https://www.iso.org/standard/53940.html); [IEC61508-1:2010 valid edition](https://webstore.iec.ch/en/publication/5515)

| Group | Material claim reviewed | Finding and limit |
| --- | --- | --- |
| 01 | Security/privacy non-equivalence | NIST privacy risk includes authorized processing producing adverse impacts; meeting access controls does not by itself satisfy every privacy interest. |
| 02 | Current privacy framework status | NIST PF v1.0 is final (2020), while PF 1.1's public project page identifies a 2025 initial public draft and no published final as of audit. |
| 03 | Safety standard scope | ISO/IEC Guide51:2014 was reaffirmed in 2025 and addresses harm to people, property and environment; IEC61508 addresses electrical/electronic/programmable electronic functional safety, not all cybersecurity. |
| 04 | Reliability model | Under an explicitly constant-hazard exponential model R(t)=e^(-λt), λ=.01 per hour for ten hours yields e^(-.1)=0.904837..., not a probability of being secure, safe or privacy-preserving. |
| 05 | Cross-objective example | An automated-building system can be secure but privacy-invasive, reliable but unsafe, or safely shut down while temporarily unavailable; technical outcome claims require separate objectives. |

### SF-12-08 · Ethical, Human, and Societal Constraints

**Article:** [ethical-human-and-societal-constraints.md](pilots/ethical-human-and-societal-constraints.md)  
**Primary source orientations:** [UN Universal Declaration of Human Rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights); [NIST Privacy Framework v1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final); [NIST privacy-risk glossary](https://csrc.nist.gov/glossary/term/info_system_related_privacy_risks)

| Group | Material claim reviewed | Finding and limit |
| --- | --- | --- |
| 01 | Rights vs authorization | UN UDHR Articles 3/7/12/29 provide human-rights context; a valid technical permission does not by itself settle legal authority, ethics or legitimate purpose. |
| 02 | Privacy harm beyond breach | NIST explicitly includes possible discrimination, distress and other harms from authorized data processing; organizational reputational exposure is not the only affected interest. |
| 03 | Necessity/proportionality qualifiers | Necessity, proportionality, accountability and remedy are context- and jurisdiction-sensitive evaluative principles, not universal technical formulas. |
| 04 | Unequal burden vs global accuracy | Aggregate detector or authentication accuracy may conceal concentrated burdens; disparity alone does not prove its cause or legal violation. |
| 05 | Monitoring/safety worked comparisons | Collecting all personal data is not automatically justifiable for security; denying all messages to a safety interlock may create danger. Scenarios are hypothetical and do not assert local legal findings. |

## Recomputed examples and evidence boundaries

| Example | Calculation or distinction | What it does not establish |
| --- | --- | --- |
| Ideal exponential lifetime model | R(10 h)=exp(−0.01×10)=exp(−0.1)=**0.904837...** | An actual measured failure distribution or any security/privacy/safety guarantee |
| Stipulated two-hour RTO | 09:40 to 11:00 = **80 minutes**, within 120 minutes | That data freshness, identity credentials or application integrity are correct |
| Stipulated 15-minute RPO | Checkpoint 09:00 vs outage 09:40 = **40-minute** recovery-point age, too old under stated no-later-copy assumptions | That a real system has lost every intervening transaction |
| Suspected and verified compromise | Denied request vs verified unauthorized content disclosure vs restarted service | Actor identity, total system compromise, or restored trusted state |
| Authorized-but-harmful processing | Access-approved personal telemetry reused for unrelated purposes | A particular legal violation without jurisdiction and contextual evidence |
| Safety-oriented shutdown | A correctly functioning safety interlock intentionally limits service | Universal fail-closed or always-online prescription for every environment |

### Source and standards version register

- **NIST SP 800-160 Volume 2 Revision 1**: final December 2021, identifies **anticipate, withstand, recover, adapt** as cyber-resiliency engineering goals. Does not prescribe an invariant sequence of incident-response steps.
- **NIST SP 800-61 Revision 3**: final April 2025, supersedes Revision 2; incident response is an **Operational Foundations activity**.
- **NIST SP 800-34 Revision 1**: final 2010, with source-bound definitions of RTO, RPO and MTD. Page 17 of Chapter 3 was **visually inspected**; its original scope is federal-system contingency planning rather than a universally binding service contract.
- **NIST Privacy Framework**: **v1.0 final January 2020**. The public 1.1 project page still identifies an **Initial Public Draft (2025)**; do not label it final. The distinction between authorized data-processing harm and cybersecurity breach is explicitly supported by NIST privacy-risk terminology.
- **ISO/IEC Guide 51:2014**: 2014 published edition, **confirmed current in 2025**; general safety aspects and harm. **IEC 61508-1:2010** remains listed by IEC as a valid edition, while a third-edition **preview** exists. Do not treat the preview as final applicability for every evaluated product.
- **United Nations UDHR**: Articles 3 (life/security of person), 7 (equal protection), 12 (privacy) and 29 (rights limitations in defined circumstances) provide foundational **human-rights framing**, not a universal substitute for jurisdiction-specific law.

## Architecture findings

1. **Keep SF-11-01 (Compromise and Loss of Security) and SF-11-04 (Resilience, Survivability and Robustness) distinct.** One explains lost or uncertain security state, the other explains bounded continuation and restoration. Future SF-11-07 can deepen RTO/RPO/trusted restoration without duplicating operational procedures.
2. **Keep SF-01-08 and SF-12-08 distinct.** SF-01-08 compares security, privacy, safety and reliability objectives; SF-12-08 examines legitimate authority, human impacts and proportionality in choosing protection methods. They are related, not synonyms.
3. **Privacy is not reducible to CIA confidentiality.** NIST PF includes harms from authorized data processing. Safety is not reducible to high availability, and reliable processing does not guarantee justified processing.
4. **Source type is part of the claim.** NIST standards/glossary, ISO/IEC functional-safety references and UN rights instruments supply different kinds of guidance and must not be collapsed into one technical taxonomy.
5. **No forced numerical expansion.** The working inventory remains **12 proposed areas and 96 active candidate headings**, both flexible. The source crosswalk contains 30 source groups and ownership review 34 cases; those are research catalogs, not fixed quotas.
6. **Publication remains open.** Passing a scoped model-assisted audit is not a complete clause-level verification, independent expert peer review, legal opinion, verified physical safety test or final article publication.

## Pilot portfolio reconciliation

The first 10 pilots passed [Review 01](PILOT-TECHNICAL-REVIEW-01.md) (40 claim groups across eight) and [Review 02](PILOT-TECHNICAL-REVIEW-02.md) (10 claim groups across two). These **four** new pilots are separately reviewed here, covering **20 more groups**. The resulting working corpus is **14 internally Reviewed pilots / 70 scoped claim groups**, with **82 working candidate headings not yet piloted**. This does **not** mean the internal taxonomy or any canonical location has been approved.

[Security Foundations](README.md) · [Pilot Register](pilots/README.md) · [Source Crosswalk](ESTABLISHED-MODEL-CROSSWALK.md) · [Working Architecture](ARCHITECTURE.md)
