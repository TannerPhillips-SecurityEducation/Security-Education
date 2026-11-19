# Security Foundations | Technical Review 11: Control Functions, Implementation, Compensation, and Effectiveness

**Review date:** November 19, 2026  
**Scope:** Four new substantive area-first Drafts: [SF-07-02](security-controls-defense-mechanisms/preventive-detective-corrective-and-recovery-controls.md), [SF-07-03](security-controls-defense-mechanisms/technical-organizational-and-physical-controls.md), [SF-07-07](security-controls-defense-mechanisms/compensating-controls-and-residual-exposure.md), and [SF-07-08](security-controls-defense-mechanisms/control-effectiveness-and-costs.md). **32 bounded material claim groups**, eight per manuscript, assessed after Draft Batch 11 rather than inherited from prior reviews.  
**Method:** Separate source-led, model-assisted technical review; official ISO publication record and the ISO/IEC 27002:2022 editors' account in the SC 27 Journal; NIST SP 800-53, 53A, 53B (and their release status), SP 800-55 Volumes 1–2 and CSRC glossary source scopes. Relevant publisher-hosted PDF pages were **visually inspected**: ISO SC 27 Journal pp. 13–14 (PDF indexes 14–15), NIST SP 800-53B p. 12 (PDF index 25), NIST SP 800-55v1 pp. 17–18 (PDF indexes 24–25). Recomputed toy measurement quantities and tested conceptual counterexamples. Applied corrections to each draft before promoting it.  
**Disposition:** The **corrected** four manuscripts pass the scoped **Reviewed (model-assisted) / Core claims checked** gate. This is **not** a claim of complete source-passage verification, independent qualified human review, deployed-control testing, compliance certification, final taxonomic acceptance or publication.

## 1. SF-07-02 | Preventive, Detective, Corrective, and Recovery Controls

**Manuscript:** [Preventive, Detective, Corrective, and Recovery Controls](security-controls-defense-mechanisms/preventive-detective-corrective-and-recovery-controls.md)  
**Primary source orientation:** [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html) and the [editors' SC 27 Journal explanation](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IEC%20JTC%201-SC%2027_N22755_SC27%20Journal%20Vol%202%20Issue%202%20%28update%20Dec%202022%29.pdf); [NIST security glossary](https://csrc.nist.gov/glossary/term/security); [NIST compensating-controls glossary](https://csrc.nist.gov/glossary/term/compensating_controls); NIST [800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) / [53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

| ID | Material claim checked | Technical finding and limitation |
| --- | --- | --- |
| 11-02-01 | Preventive, detective, corrective, recovery are distinct functional lenses | **Pass.** Their objects are, respectively, attempted loss/transition, observation or classification, correction of the unwanted state/cause, and restoration of desired capability. This is a **working analytical comparison**, not a single normative four-value NIST or ISO class set. |
| 11-02-02 | ISO/IEC 27002:2022 control *types* are preventive, detective, corrective | **Pass with explicit version distinction.** The final 2022 ISO edition and editors' account in SC 27 Journal pp. 13–14 define five control metadata attributes, including a **three-valued control type**. Recovery is **not** a fourth source-defined value of that attribute. |
| 11-02-03 | NIST's security glossary includes broader protection terms | **Pass with caveat.** NIST's glossary lists multiple source-attributed meanings, including prevention, detection, correction and recovery as well as deterrence and avoidance. This is not evidence of a universal exclusive taxonomy. |
| 11-02-04 | A function label is scenario- and property-relative | **Pass.** An integrity detector may prevent *later propagation* without preventing the original write. Restoring availability does not by itself repair confidentiality or prove trusted state. Added tighter language about the event/cause being corrected. |
| 11-02-05 | Sequential detection-response yields are conditional, not independent | **Independently recomputed.** With exactly 1,000 events, 80% observable/recorded, 80% of those signaled, and 60% of those actioned: \(1000\times .8\times .8\times .6=384\) timely actions and **38.4% observed chain yield**. These are sequential **conditional proportions**; no independence assumption is needed, and no prevention probability is established. |
| 11-02-06 | No alert is insufficient evidence of no incident | **Pass.** An absent alert could reflect non-observability, collection failure, rule fit, suppressed reporting or event non-occurrence. The source's function classification does not independently identify malicious intent or measurement coverage. |
| 11-02-07 | Compensating is a different dimension from function | **Pass.** The [NIST compensating-controls glossary](https://csrc.nist.gov/glossary/term/compensating_controls) defines source-scoped substitution relationships, not a special event-timing stage. A substitute may itself be preventive/detective/etc. |
| 11-02-08 | CISA CRR resource guide is an independently verified source here | **Not established; corrected.** The referenced historical [CISA CRR Controls Management PDF](https://www.cisa.gov/sites/default/files/publications/CRR_Resource_Guide-CM_0.pdf) could not be retrieved (publisher returned forbidden). **Removed the positive claim** that it verified a particular four-type control classification, retained it only as an unverified historical starting point, and grounded the substitution distinction in NIST instead. |

**Corrections:** Explicit conditional denominators for the 384-case chain; corrected the linguistic distinction between correcting a cause and preventing later events; refused to elevate inaccessible CISA material into source-verified evidence; preserved recovery as a working separate concept rather than a misattributed ISO control-type attribute.

## 2. SF-07-03 | Technical, Organizational, and Physical Controls

**Manuscript:** [Technical, Organizational, and Physical Controls](security-controls-defense-mechanisms/technical-organizational-and-physical-controls.md)  
**Primary source orientation:** [ISO/IEC 27002:2022 (edition 3, corrected March 2022)](https://www.iso.org/standard/75652.html); [ISO/IEC SC 27 editors' journal](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IEC%20JTC%201-SC%2027_N22755_SC27%20Journal%20Vol%202%20Issue%202%20%28update%20Dec%202022%29.pdf) pp. 13–14, visually inspected; [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [800-53B](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final) and [800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

| ID | Material claim checked | Technical finding and limitation |
| --- | --- | --- |
| 11-03-01 | How a control is implemented is independent of its intended protective function | **Pass.** A control may have organizational authority, human execution, physical boundaries and technical enforcement, and may deliver prevention/detection/recovery functions under particular circumstances. A supplier/product name does not settle either classification. |
| 11-03-02 | ISO/IEC 27002:2022 uses four implementation *themes* | **Pass.** The source editors enumerate **37 organizational, 8 people, 14 physical and 34 technological** controls, a total of **93**, visually verified in their 2022 journal at printed p. 13 (PDF index 14). These are ISO theme counts, not counts of every real safeguard. |
| 11-03-03 | ISO includes attribute-based alternative views as well as themes | **Pass after source clarification.** Printed p. 14 (PDF index 15) explicitly describes **five attributes per control** permitting customizable views. Added the distinction to avoid treating chapter themes as one exclusive implementation mechanism per deployed safeguard. |
| 11-03-04 | The article's three-axis tuple is a standards-mandated schema | **Not source-backed; explicitly limited.** The illustrative \(\operatorname{Profile}(c)=(\mathrm{Implementation},\mathrm{Function},\mathrm{ProtectedProperties})\) is **editorial**. Components may be multi-valued; it is not an ISO/NIST data specification, effectiveness test or proof of completeness. |
| 11-03-05 | NIST topic-based control families are not ISO implementation themes | **Pass.** NIST SP 800-53's administrative, technical and physical facets can coexist in one topic-based control family. An old **management/operational/technical** grouping is not an exact translation of ISO's four themes. |
| 11-03-06 | Human review and organizational procedure guarantee trust by themselves | **Counterexample passes.** Two approvers may both rely on a forged artifact or shared identity state. Human processes and physical protections create useful independent opportunities only when their **actual trust dependencies** differ. No human behavior is measured in the invented model. |
| 11-03-07 | Ownership and inherited services are distinct from implemented assurance | **Pass.** The existence of an organizational policy or third-party responsibility map does not establish that a service enforces correct authorization. Shared-responsibility and assessment claims require context-specific evidence. |
| 11-03-08 | NIST 53/53A/53B publication functions are interchangeable | **Pass by separation.** SP 800-53 catalogs controls; 53B provides federal baselines/tailoring; 53A provides assessment procedures. NIST **Release 5.2.0 (August 2025)** left the SP 800-53B baseline membership unchanged; it did update parts of 53/53A. |

**Corrections:** Source-scoped ISO themes/attribute counts and visually checked page locations; explicitly multi-valued, editorial tuple; separated NIST control functions from ISO categories. The example release-signing architecture remains hypothetical, without a verified deployment assurance claim.

## 3. SF-07-07 | Compensating Controls and Residual Exposure

**Manuscript:** [Compensating Controls and Residual Exposure](security-controls-defense-mechanisms/compensating-controls-and-residual-exposure.md)  
**Primary source orientation:** [NIST SP 800-53B, Chapter 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf), printed p. 12 (PDF index 25), visually inspected; [NIST glossary for compensating controls](https://csrc.nist.gov/glossary/term/compensating_controls); [NIST SP 800-53B Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final) and [SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

| ID | Material claim checked | Technical finding and limitation |
| --- | --- | --- |
| 11-07-01 | Compensating means substituting a specified baseline requirement with comparable protection | **Pass.** NIST 53B, Chapter 2 printed p. 12, says compensating controls are used *in lieu of* selected baseline controls where the baseline item cannot be implemented but needed protection remains. It requires **equivalent or comparable protection**, rationale and risk treatment, not simply one more protective device. |
| 11-07-02 | A substitute may be justified by technical feasibility, mission or cost constraints | **Pass with bound.** The source explicitly allows context-dependent substitution but does **not** authorize bypassing applicable requirements. A documented justification and suitability of alternative controls are essential. |
| 11-07-03 | One or many controls might be needed to satisfy a baseline need | **Pass.** NIST 53B footnote 35 expressly allows **multiple compensating controls** to provide equivalent protection. Added the precise source emphasis rather than assuming every substitute is one-to-one. |
| 11-07-04 | NIST's glossary has another digital-identity meaning | **Pass after correction.** The NIST glossary includes a distinct SP 800-63-4 **xAL-specific** alternative-control definition with privacy, usability, risk and user-population concerns. It cannot be silently treated as merely another instance of arbitrary baseline substitution. |
| 11-07-05 | After-the-fact audit can universally substitute for independent preventive payment approval | **Counterexample passes.** An audit can report an unauthorized payment after it executes, but cannot by itself ensure **pre-execution** second-person approval. NIST describes audit/training/screening as possible compensating controls in some separation-of-duties contexts, not as proof they preserve every pre-execution requirement. |
| 11-07-06 | Residual modeled exposure is identical to measured residual risk | **Pass after clarification.** The authored set expression \(\mathcal E(C)=\mathcal L\setminus\mathcal P(C)\) is only **modeled scenario non-prevention**. It excludes unmodeled paths and does not represent loss-severity mitigation, detection, recovery, probabilities or human consequences without additional mechanisms. |
| 11-07-07 | Alternative controls can share failure dependencies | **Pass.** A supposedly independent compensating system may depend on the same misconfigured identity or incomplete telemetry as the original. Comparable protection is property-, path-, timing- and trust-assumption-relative. |
| 11-07-08 | 2025 SP 800-53B release changed the baseline text verified in the 2020 PDF | **Version checked.** NIST's current publication record states **Release 5.2.0 (August 27, 2025) changed no baseline members** and harmonized version numbers. The inspected source PDF is the original 2020 text, not a clause-by-clause independent diff of every later supplemental format. |

**Corrections:** More precise NIST glossary source families; source-page verification and edition caveat; multiple substitutes and scoping; excluded the stronger inference that modeled exposure subtraction is a risk score or comprehensive harm calculation.

## 4. SF-07-08 | Control Effectiveness and Costs

**Manuscript:** [Control Effectiveness and Costs](security-controls-defense-mechanisms/control-effectiveness-and-costs.md)  
**Primary source orientation:** [NIST SP 800-55 Volume 1 (final December 2024)](https://csrc.nist.gov/pubs/sp/800/55/v1/final), **§3.3, printed pp. 17–18 (PDF indexes 24–25)** visually inspected; [Volume 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final); [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) versus [SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final); [MITRE D3FEND FAQ](https://d3fend.mitre.org/faq/).

| ID | Material claim checked | Technical finding and limitation |
| --- | --- | --- |
| 11-08-01 | Selecting, implementing, assessing and measuring control effectiveness are different activities | **Pass.** 53 catalogs controls, 53A supplies assessment methods, and 55v1/55v2 guide selection and program use of measures. A selected control or passing narrow test is not evidence of comprehensive protection. |
| 11-08-02 | NIST 800-55v1 recognizes implementation/effectiveness/efficiency/impact measures | **Pass, visually verified** at §3.3 (printed pp. 17–18 / PDF indexes 24–25). The labels describe different observations and cannot be replaced by one undifferentiated activity count. |
| 11-08-03 | “Efficiency” in NIST 800-55 is identical to generic resource-cost ratio | **Not supported; corrected.** Section **3.3.3** emphasizes **timeliness and speed of useful feedback/resolution**, while §3.3.4 **impact** discusses cost savings, expenditures and cost-effectiveness. The manuscript now distinguishes general engineering efficiency from the narrower NIST measurement term. |
| 11-08-04 | The illustrative 10,000-case confusion matrix sums correctly | **Independently recomputed.** TP=80, FN=20, FP=495, TN=9,405; row totals 100/9,900 and column totals 575/9,425. Grand total is **10,000**. No sampled-world ground truth is claimed. |
| 11-08-05 | Recall, false-positive rate and precision are calculated consistently | **Pass with recomputation.** Recall \(80/(80+20)=.80\); false-positive rate \(495/(495+9405)=.05\); precision \(80/(80+495)=80/575=0.1391304348\), or **13.91%**. A high recall score therefore need not imply high alert precision in this constructed population. |
| 11-08-06 | Statistical independence of cases is required for arithmetic counts | **Incorrect premise; corrected.** Confusion-matrix rates for a specified dataset are **descriptive counts**. Independence matters when estimating uncertainty or generalizing to a different population, not merely for \(80/575\). Removed unjustified “independent cases” wording. |
| 11-08-07 | Positive expected net monetary benefit automatically establishes acceptable control | **Counterexample passes.** The fictional \(\mathbb E[L_{\rm without}]-\mathbb E[L_{\rm with}]-C\) requires a shared horizon and credible counterfactual; a positive $40,000 model result cannot by itself authorize illegitimate privacy burden or satisfy a hard security requirement. |
| 11-08-08 | Two detectors' reported coverage can always be added | **Pass by set counterexample.** Two sensors each identifying the same 80 of 100 cases need not cover 160 distinct cases. Shared inputs and common causes require an explicit intersection/union model. The control effectiveness owner stays distinct from defense depth, placement, resilience and risk acceptance. |

**Corrections:** NIST source-specific efficiency versus impact; original edition page locations; removed a mathematically unnecessary independence assumption; separated observed measurement from causal attribution. The confusion matrix and financial case remain hypothetical, not product performance or procurement advice.

## Independent calculations and countermodels

### Conditional detection-action chain

For **1,000 hypothesized relevant events**, assume 80% are observable and retained, 80% **conditional on that subset** produce an actionable signal, and 60% **conditional on the signaled subset** get timely action:

\[
1000(0.80)(0.80)(0.60)=384.
\]

The yield is \(384/1000=38.4\%\). **This is not 38.4% of threats prevented.** It does not require independence across collection, detection, or response because the quantities were stipulated as sequential conditional proportions.

### Detection confusion matrix

| Ground truth | Alert | No alert | Total |
| --- | ---: | ---: | ---: |
| Relevant condition | 80 | 20 | 100 |
| Other condition | 495 | 9,405 | 9,900 |
| **Total** | **575** | **9,425** | **10,000** |

The derived quantities are:

\[
\operatorname{Recall}=\frac{80}{100}=0.8,\quad
\operatorname{FPR}=\frac{495}{9900}=0.05,\quad
\operatorname{Precision}=\frac{80}{575}\approx0.1391304348.
\]

The *positive predictive value* depends on the ground-truth prevalence and the conditional match rates. These figures are invented and do not establish field efficacy or incident probability.

### Compensating-control property counterexample

An authorization obligation that **requires independent approval before an irreversible disbursement** is not guaranteed by a log reviewed tomorrow, even if the log's integrity is perfect. The log may help with detection and subsequent correction, but the original event has already occurred. Comparable protection must be justified relative to the actual requirement and the authorized decision context, not a vague label.

### Three axes, one unknown outcome

A control can be **technological** (medium), **preventive** (intended function), and **compensating** (relationship to a selected baseline requirement) without any independently demonstrated *effectiveness*. Conversely, a human process may be preventive and a technical system may be detective. These are orthogonal analytical descriptions, not one imposed ISO taxonomy.

## Source verification boundary and outcome

**Primary pages actually inspected:** ISO/IEC SC 27 editors' journal pp. 13–14 (PDF indexes 14–15); NIST SP 800-53B original printed p. 12 (PDF index 25); NIST SP 800-55v1 printed pp. 17–18 (PDF indexes 24–25). NIST publisher pages were checked for Release 5.2.0, the 2024 final 800-55 volumes, and the original published editions. No paid full-text ISO/IEC 27002 clauses were independently inspected; the source is the **editors' publicly available official journal and ISO publication metadata**, not a claim of complete standard text review.

**Sources not fully examined:** The CISA Controls Management PDF is inaccessible through the available retrieval source; no specific classification from it is represented as verified. Detailed clauses and all relevant cross-references across NIST 53/53A/53B and ISO have **not** been exhaustively checked. Real deployment effectiveness, financial losses, ethical legitimacy, observed human performance and external expert acceptance are out of scope.

**State transition justified:** Each corrected SF-07-02/03/07/08 article advances **Draft → Reviewed (model-assisted)** and **References listed → Core claims checked** with its own eight claim groups in this ledger. Earlier Reviews 01–10 covered **230** bounded claim groups across **35** Reviewed working manuscripts. Review 11 adds **32**, giving **262 scoped groups across 39 Reviewed articles**, with **0 Draft** and **57 Inventoried without article** within the provisional 96-candidate inventory. Structural CI success does not validate the technical truth of every sentence.

**Administrative transition:** Following this review, **pause new Security Foundations content drafting**. Existing articles and their source/review states remain intact. Shift work to a **repository-wide administrative editorial pass** for readability, explanatory depth, relationships, navigation and faithful source/claim communication. This administrative work is not a new Security Foundations authoring wave and does not silently change the ratification or publication gates.

[Security Foundations](README.md) · [Working Article Register](pilots/README.md) · [Development/Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Working Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md)
