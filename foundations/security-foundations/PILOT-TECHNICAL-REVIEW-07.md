# Security Foundations | Technical Review 07: Stakeholders, Assets, Criticality, Harm, and Protection Priorities

**Review date:** November 18, 2026  
**Scope:** Five substantive area-first Draft manuscripts in [Protected Interests, Assets & Harm](protected-interests-assets-harm/README.md): **SF-02-01**, **SF-02-02**, **SF-02-04**, **SF-02-05**, **SF-02-07**. **30 material claim groups**, six per article, audited separately after Draft Batch 07. **SF-02-03 remains Inventoried without an article** and is not included in this audit.  
**Method:** Separate model-assisted claim-led review of the drafted articles, including verification against official publication records; visual inspection of NIST SP 800-160 Vol. 1 Rev. 1 Chapter 3 §3.7 and Figures 7–8, FIPS 199's information-type and information-system categorization; inspection of NIST CSF 2.0 GV.OC outcomes, Privacy Framework and relevant NIST glossary definitions; logical truth-table enumeration; worked Pareto comparison; source-scope counterexamples; and corrections to overbroad or ambiguous claims.  
**Disposition:** The five **corrected** area manuscripts pass this **bounded model-assisted technical review**. They may advance to **Reviewed (model-assisted) / Core claims checked**, **not** Source-Verified, independently expert-reviewed, architecturally ratified or Published. The six previous reviews remain historical and retain their own original scope.

## 1. SF-02-01 | Stakeholders and Protection Needs

**Article:** [Stakeholders and Protection Needs](protected-interests-assets-harm/stakeholders-and-protection-needs.md)  
**Source basis:** [NIST SP 800-160 Vol. 1 Rev. 1 (final November 2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), §3.7 printed pp. 25–27 and Figure 7, visually inspected at PDF page indexes 40–42; [NIST CSF 2.0](https://csrc.nist.gov/Projects/Cybersecurity-Framework/Filters), GV.OC-01–04; [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final).

| ID | Material claim or assumption | Review finding, correction, and limit |
| --- | --- | --- |
| 07-01-01 | Protection needs originate in stakeholder interests, not chosen controls | **Pass.** SP 800-160v1r1 §3.7 says protection needs follow asset, loss context, type and consequence, and may be determined without first naming a particular cause or condition. Added the explicit *before threat/cause selection* distinction. This is security-engineering guidance, not the whole of human rights or legal authorization. |
| 07-01-02 | Stakeholder, system and trades are distinct perspectives | **Pass.** NIST Figure 7 (printed p. 25/PDF index 40) connects the three input perspectives to security requirements and policies. The article's explanatory chain is *editorial traceability*, not a verbatim NIST process. |
| 07-01-03 | Stakeholders and technical principals are not equivalent | **Pass with clarification.** A technical principal may represent a machine or service and need not correspond to a human or affected person. A bystander or beneficiary may have protection interests without holding any principal. Corrected the article's identity distinction; no NIST source is claimed to define its exact role table. |
| 07-01-04 | Protection needs and verifiable requirements differ | **Pass.** SP 800-160 §3.7's note on requirements and Appendix H activities support traceability and verification-method requirements. A technically tested mechanism can fail to capture a legitimate stakeholder need. Wording was changed from implying a mandatory universal field schema to optional components of sufficiently precise needs. |
| 07-01-05 | Organizational context includes internal and external stakeholder expectations | **Pass.** NIST CSF 2.0 **GV.OC-01** covers mission, **GV.OC-02** stakeholder expectations, **GV.OC-03** applicable obligations, and **GV.OC-04** critical services/capabilities expected by stakeholders. They are framework *outcomes* rather than exhaustive organizational stakeholder categories or certification of compliance. |
| 07-01-06 | Healthcare scheduling example preserves competing interests without inventing findings | **Pass.** The hypothetical example correctly separates data integrity, timely availability, access needs, confidentiality and privacy. No measurements, legal conclusion, patient outcomes or clinical guidance are asserted. SF-12-08 retains normative authority/harm judgments; Operational Foundations retains requirements-elicitation procedures. |

**Corrections recorded:** (a) located and qualified the three NIST perspectives and cause-independent protection-needs determination; (b) clarified machine/service principals versus people and decision authority; (c) avoided presenting a list of useful need-description attributes as a compulsory universal schema.

## 2. SF-02-02 | Assets, Resources, and Protected Interests

**Article:** [Assets, Resources, and Protected Interests](protected-interests-assets-harm/assets-resources-and-protected-interests.md)  
**Source basis:** [NIST SP 800-160v1r1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), Figure 8 printed p. 26 (PDF index 41); [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final), printed pp. 3–4 (PDF indexes 6–7); [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final).

| ID | Material claim or assumption | Review finding, correction, and limit |
| --- | --- | --- |
| 07-02-01 | Asset/resource/protected-interest refer to different relationships | **Pass.** A server can be a valuable resource while continued care, integrity or privacy is the interest motivating its protection. This is an editorial explanatory distinction, not an internationally uniform legal definition of assets or rights. |
| 07-02-02 | Figure 8 includes people and multiple loss forms | **Pass after clarification.** The inspected Figure 8 explicitly lists **humans** under asset types and loss forms such as correctness, ownership, control, trust and time. Added the qualification that a systems-engineering *asset type* does not create legal ownership over a person or reduce dignity and rights to prices. |
| 07-02-03 | System assets can be unknown to stakeholders | **Pass.** §3.7 describes stakeholder assets versus design-determined system assets whose existence is typically unknown to stakeholders. The payment ledger/keys/queue relationship is a hypothetical illustration, not a NIST-declared mandatory architecture. |
| 07-02-04 | Asset significance changes with boundaries and dependencies | **Pass.** An identity system can be internal to the complete platform but external to one application, without logical contradiction. The source supports contextual asset interpretation, not a universal one-to-one mapping from asset name to protection property. |
| 07-02-05 | FIPS 199 is potential-impact categorization, not price or actual risk | **Pass with concrete source nuance.** In FIPS 199, a **system's high-water mark is taken separately for each confidentiality, integrity and availability objective** across resident information types. *Not applicable* may appear for confidentiality of an **information type**, but not any of the **information-system** security objectives; inspected printed pp. 3–4. Added these limits to prevent treating system categorization as a universal price/risk score. |
| 07-02-06 | Low-cost gateway may support high-consequence functions | **Pass as a hypothetical counterexample.** The invented $120 gateway shows that replacement price is not criticality or measured human harm. The scenario neither proves injury nor rules out independent safety safeguards. SF-02-04 owns inherited criticality; SF-02-05 owns effects of loss. |

**Corrections recorded:** (a) clearly separated NIST Figure 8's word *humans* from legal/moral property claims; (b) specified FIPS 199's **per-objective** high-water mark and information-type-versus-system applicability of *not applicable*.

## 3. SF-02-04 | Value, Criticality, and Dependencies

**Article:** [Value, Criticality, and Dependencies](protected-interests-assets-harm/value-criticality-and-dependencies.md)  
**Source basis:** [NIST SP 800-160v1r1 §3.7](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final); [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final); [NIST CSF 2.0 GV.OC](https://csrc.nist.gov/Projects/Cybersecurity-Framework/Filters); Boolean models are original illustrative mathematics, *not source equations*.

| ID | Material claim or assumption | Review finding, correction, and limit |
| --- | --- | --- |
| 07-04-01 | Value, criticality and dependency are context-relative and different | **Pass.** A low-price component can be essential to a critical service, whereas a costly component can be replaceable. NIST §3.7 supports temporal, state-relative assessment; the manuscript's definitions are editorial simplifications, not NIST's sole glossary definitions. |
| 07-04-02 | Necessary inputs do not imply probabilistically independent failures | **Pass after correction.** The draft had called two conjunctive inputs “independent prerequisites.” Corrected to **jointly necessary prerequisites** and explicitly disclaimed statistical independence. A logical gate does not supply joint probabilities. |
| 07-04-03 | Shared dependency and redundant branches Boolean expression | **Pass by exhaustive enumeration.** The defined model \(S=C\land(A\lor B)\) implies \(\neg S=\neg C\lor(\neg A\land\neg B)\). All **eight** Boolean assignments of A, B and C produced matching complements. The minimal failure cut sets are **{\(\neg C\)}** and **{\(\neg A,\neg B\)}** within this model. No real failure frequencies or independence are inferred. |
| 07-04-04 | Integrity and authorization dependencies can matter without an outage | **Pass.** A responsive application can still rely on compromised identity/policy state. The article correctly limits an availability-only truth table and describes why evidence for system *security* requires additional properties. |
| 07-04-05 | Alternative paths remove some single-point dependencies | **Pass.** \(A\lor B\) can survive A's loss when B is functioning and required shared control C survives. Geographic dispersion alone does not establish independent failure mechanisms; the corrected article states this explicitly. |
| 07-04-06 | FIPS 199 high-water mark does not compute all risk or worth | **Pass with correction.** Added its per-objective, information-system scope, not one generic high/medium/low valuation of stakeholders. Probability estimates, accepted tradeoffs and actual BIA procedures remain in Security Risk & Uncertainty / Operational Foundations. |

**Independent truth-table summary:**

| A | B | C | \(C\land(A\lor B)\) | \(\neg C\lor(\neg A\land\neg B)\) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |

The fifth column is the **loss condition**, not another expression for service availability. All eight rows satisfy \(\mathrm{Loss}=\neg S\). This truth table validates the *formulation* but cannot validate a physical architecture that may admit degraded modes, imperfect failover, common causes or temporal changes.

## 4. SF-02-05 | Adverse Outcomes, Consequences, and Harm

**Article:** [Adverse Outcomes, Consequences, and Harm](protected-interests-assets-harm/adverse-outcomes-consequences-and-harm.md)  
**Source basis:** [NIST SP 800-160v1r1 Figure 8](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final); [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final); [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final); [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final); [NIST Problematic Data Action glossary](https://csrc.nist.gov/glossary/term/problematic_data_action); [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html).

| ID | Material claim or assumption | Review finding, correction, and limit |
| --- | --- | --- |
| 07-05-01 | Event, outcome, consequence and harm are conceptually different | **Pass.** An observed event need not cause harm; a consequence can vary across affected stakeholders; causal evidence and normative evaluation are additional obligations. The terms form an editorial comparison, not an asserted universal standards hierarchy. |
| 07-05-02 | Asset loss has effects on the asset and on those who value it | **Pass.** Inspected NIST SP 800-160v1r1 Figure 8, printed p. 26/PDF index 41, and the subsequent distinction between effects on the asset and effects on stakeholders. This does not convert the listed asset classes into an exhaustive harm ontology. |
| 07-05-03 | Source-defined safety harm and privacy harms have different scope | **Pass.** ISO/IEC Guide 51:2014 (published, confirmed 2025) concerns safety aspects for **people, property and environment**, not every privacy, reputation or socioeconomic harm. NIST Privacy Framework 1.0 addresses problematic data processing and individual impact beyond a confidentiality breach. Neither definition is imported as a universally exhaustive class. |
| 07-05-04 | Problematic data action signals potential, not proven harm | **Pass with correction.** NIST's source-attributed glossary defines an action that **could** cause adverse effects for individuals. It need not establish a realized injury. The article now explicitly separates privacy-event/problematic-data-action claims from independently evidenced actual harm. |
| 07-05-05 | Realized harm is not equivalent to observed or substantiated harm | **Pass after material epistemic correction.** The Draft had called realized harm an effect “shown to have occurred,” improperly merging reality with evidence. The revised text distinguishes **actual occurrence**, **availability of observations**, **evidential support** and **risk uncertainty**. Lack of evidence is not proof that no one was harmed. |
| 07-05-06 | Impact categorization and risk estimates are not evidence of consequences already experienced | **Pass.** FIPS 199 categories express *potential* adverse effects in the U.S. federal information-system context. SP 800-30 Rev. 1 concerns future/uncertain risk estimates. The hypothetical corrupted-appointment record is not a documented missed visit or demonstrated injury. SF-02-05 retains general harm; SF-05-03 remains the separate owner of scenario-consequence estimation. |

**Corrections recorded:** (a) separated actual harm from what is demonstrably recorded; (b) tightened NIST's *could cause* problematic-data-action definition; (c) clarified multiple consequence dimensions; (d) preserved FIPS 199 potential-impact and ISO safety-specific scope.

## 5. SF-02-07 | Protection Priorities and Constraints

**Article:** [Protection Priorities and Constraints](protected-interests-assets-harm/protection-priorities-and-constraints.md)  
**Source basis:** [NIST SP 800-160v1r1 §3.7](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final); [NIST CSF 2.0 GV.OC](https://csrc.nist.gov/Projects/Cybersecurity-Framework/Filters); [NIST Privacy Framework 1.0](https://csrc.nist.gov/pubs/cswp/10/nist-privacy-framework-version-10/final); [ISO/IEC Guide 51:2014](https://www.iso.org/standard/53940.html); [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final). Feasible-set and Pareto notation are authored mathematical illustrations.

| ID | Material claim or assumption | Review finding, correction, and limit |
| --- | --- | --- |
| 07-07-01 | Priority, constraint, preference and tradeoff are distinct | **Pass.** NIST §3.7 explicitly identifies stakeholder, system and engineering *trades* perspectives and allows protection needs to be determined before a threat-specific assessment. The article does not imply that all alternatives require sacrificing one desired objective. |
| 07-07-02 | Stakeholder needs and obligations constrain feasible protection designs | **Pass.** CSF 2.0 GV.OC-01–04 describes mission, stakeholders, obligations and essential services. These are organizational outcomes, not unqualified permission for one stakeholder to override other people's rights, or an assertion that all objectives have one natural ranking. |
| 07-07-03 | Formal feasible-set model is scoped to explicit requirements | **Pass with limitation.** \(\mathcal{F}=\{x\in\mathcal X:g_i(x)\le b_i,\ \forall i\}\) describes constraints representable as functions/thresholds. It is **not** a complete test of legal legitimacy, proportionality or subjective welfare. The revised article notes that a purported “hard” constraint may itself be improperly specified. |
| 07-07-04 | Pareto dominance is a partial order relative to modeled criteria | **Pass.** If delay and retention are both to be minimized after meeting hard conditions, B=(6 seconds,14 days) strictly dominates A=(8 seconds,30 days). B and C=(4 seconds,21 days) do **not** dominate one another. Added the independently checked three-alternative table. Rankings change if criteria or feasibility changes. |
| 07-07-05 | Security, privacy and safety tradeoffs need separate objective/authority analysis | **Pass.** A safe shutdown may interrupt availability; richer monitoring may increase privacy burdens. An effective detection/control mechanism alone does not prove proportionality or lawful use. The invented emergency-alert case has no measured coverage or legal applicability. |
| 07-07-06 | Context changes invalidate the applicability of a priority, not its historical occurrence | **Pass.** Changes in service, stakeholders, law, architecture, hazards and dependencies can change the feasible set or objectives. The article leaves actual prioritization workflows to Operational Foundations and legitimacy to SF-12-08. No universal numerical formula for human rights or harm is claimed. |

**Independently checked Pareto comparison:**

| Design | Delay (s) ↓ | Identifiable-data retention (days) ↓ | Conclusion under just these modeled criteria |
| --- | ---: | ---: | --- |
| A | 8 | 30 | Dominated by B |
| B | 6 | 14 | Dominates A; trades off against C |
| C | 4 | 21 | Faster than B but higher retention |

These values are invented and conditional on otherwise feasible alternatives. Shorter retention is treated as preferable for the *illustrative privacy objective* only after honoring any applicable retention obligation. The table proves no fact about deployed emergency notification systems.

## Corrections, bounded acceptance and source record

| Article | Material corrections | Remaining evidence gate |
| --- | --- | --- |
| SF-02-01 | NIST Figure 7 source and cause-independent protection needs; machine/service principal distinction; non-mandatory need-description fields | Confirm additional requirements traceability and actual stakeholder applicability in a concrete context |
| SF-02-02 | People-as-asset category caveat; precise FIPS 199 per-objective high-water mark and NA scope | Source-to-claim passage-level coverage and concrete system categorization |
| SF-02-04 | Logical necessity vs statistical independence; eight-assignment Boolean check; per-objective FIPS 199 scope | Empirical dependency modeling, failover evidence and any probability assumptions |
| SF-02-05 | Reality vs observability of harm; problematic-data-action potential vs realized harm; consequence dimensions | Causal/impact evidence in actual cases; cross-jurisdiction legal and ethical applicability |
| SF-02-07 | Correct treatment of feasibility and constrained tradeoffs; nondominated options plus numeric counterexample; model incompleteness | Actual stakeholder requirements, legal obligations, effectiveness and independent decision authorization |

**Specific inspected primary-source locations:**
- **NIST SP 800-160 Vol. 1 Rev. 1, §3.7, printed pp. 25–27**, PDF page indexes **40–42**, including Figures 7–8 and the distinction between asset loss and effects on valuing stakeholders. [Publisher record](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final).
- **FIPS 199, printed pp. 3–4**, PDF indexes **6–7**, describing potential impact, information-type security categories, per-objective high-water-mark information-system categories, and limits on “not applicable.” [Publisher record](https://csrc.nist.gov/pubs/fips/199/final).
- **NIST CSF 2.0 GV.OC-01–04** in official [CSF current outcomes and examples](https://csrc.nist.gov/Projects/Cybersecurity-Framework/Filters), used as organizational-context scope, not certification evidence.
- **NIST Privacy Framework 1.0 final (January 2020)** and [NIST problematic data action glossary](https://csrc.nist.gov/glossary/term/problematic_data_action), used to distinguish possible problematic processing from observed harms. The official [Privacy Framework 1.1 project](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11) still lists a 2025 Initial Public Draft as of this review; 1.1 is **not silently treated as a published final**.
- **ISO/IEC Guide 51:2014**, official [ISO publication record](https://www.iso.org/standard/53940.html), indicates publication in 2014 and confirmation in 2025. The official scope is safety for people, property and the environment, not a universal cybersecurity risk-metric standard.

**Not performed:** Complete clause-by-clause verification of every source-to-claim relationship, independent expert peer review, measurement of real affected people, a deployed-system audit, legal/safety certification, review of every version of every cited standard, or approval of the working 12-area/96-candidate internal taxonomy.

**State transition justified:** All five manuscripts may change **Draft → Reviewed (model-assisted)** and **References listed → Core claims checked**, with **this separate review** as the supporting article-specific record. Historical Reviews 01–06 retain **117 prior material claim groups**; this review adds **30**, totaling **147 recorded material claim groups across 25 Reviewed working manuscripts**. SF-02-03 stays Inventoried without an authored article and is not approved by this review.

[Security Foundations](README.md) · [Working manuscript index](pilots/README.md) · [Development register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Working ownership](CANONICAL-OWNERSHIP-REGISTER.md)
