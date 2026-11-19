# Technical, Organizational, and Physical Controls

**Candidate subject:** SF-07-03 · Security Controls & Defense Mechanisms  
**Working area:** [Security Controls & Defense Mechanisms](README.md) · Fundamentals-style directory pattern adopted; semantic area and subject taxonomy provisional  
**Artifact type:** Substantive working security-knowledge reference; not a final canonical publication or system-specific controls implementation guide  
**Development state:** Reviewed (model-assisted) · **Source-review state:** Core claims checked in [Technical Review 11](../PILOT-TECHNICAL-REVIEW-11.md), 8 material claim groups; full source verification and independent expert review pending  
**Architecture:** [Working Candidate Inventory](../SUBJECT-INVENTORY-PROPOSAL.md) · [Source/Model Crosswalk](../ESTABLISHED-MODEL-CROSSWALK.md) · [Ownership Register](../CANONICAL-OWNERSHIP-REGISTER.md)

## What a control is implemented through differs from what it achieves

A control may depend on software, people, organizational policy, physical boundaries, or a combination of all four. **Implementation category** identifies the nature and locus of a control's mechanism, responsibility or enforcement. **Functional purpose** identifies the protective effect it intends to provide. Neither determines **effectiveness** without evidence.

The working subject name uses **technical, organizational, and physical**, which is a useful broad comparison but not an exhaustive list of how standards organize controls. Human behavior, for example, can be described under organizational measures yet warrants its own meaningful distinction in some references. This article therefore covers **people** as an explicit dimension rather than silently equating people with management paperwork.

[NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) states that controls can include **administrative, technical and physical aspects**, while NIST's control families are organized by security/privacy topics rather than three exclusive implementation categories.

The final [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html) uses **four themes**: *organizational, people, physical and technological*. An [ISO/IEC JTC 1/SC 27 journal article by its three editors (December 2022, printed pp. 13–14)](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IEC%20JTC%201-SC%2027_N22755_SC27%20Journal%20Vol%202%20Issue%202%20%28update%20Dec%202022%29.pdf) identifies 37 organizational, 8 people, 14 physical, and 34 technological controls within its **93-control** edition. Those are **standard-specific chapter/theme counts**, not an observation that all real controls everywhere fit only one of four boxes. The same editorial overview explicitly says ISO/IEC 27002 also includes **attributes for alternative views** of controls. Its four chapter themes therefore should not be interpreted as forbidding cross-theme implementation dependencies.

## Four implementation perspectives

| Implementation perspective | Typical mechanism or responsibility | Representative safeguard | Important limitation |
| --- | --- | --- | --- |
| **Technical / technological** | Executable policy, cryptography, hardware-assisted enforcement, protocol or software logic | Object-level authorization check | Source code alone does not establish deployment or correctness |
| **Organizational / administrative** | Authority, rules, responsibilities, governance, oversight, contractual obligations | Defined separation of duties and privileged-access policy | A signed policy document is not evidence that it was enforced |
| **People** | Human competence, judgment, accountability, training, review, supervised operation | Independent review for a critical exception | Competence and trustworthy decisions cannot be assumed from training attendance |
| **Physical / environmental** | Physical access, barriers, power, environmental conditions, equipment protection | Controlled equipment-room access | Physical control does not necessarily restrict remote logical access |

The table is **editorial**. ISO and NIST use their terms within their own publication architecture, and historical source categories such as “management, operational, technical” are not literally the same four themes as ISO/IEC 27002:2022.

These perspectives describe **how protection is provided**, not whether the action is preventive, detective, corrective or recovery-oriented. In ISO/IEC 27002:2022, **preventive, detective and corrective are source-defined control-type attributes**; recovery remains a separate functional comparison in the adjacent working article, not an invented fourth ISO attribute value. An organizational review requirement may prevent an unsuitable change; a technical monitor may detect a bad state; a physical backup facility may support recovery.

## Multiple mechanisms cooperate in one protection requirement

Consider a fictional service whose key material can authorize software updates. Its legitimate protected interest is to ensure that only authorized, trustworthy releases are accepted.

Possible safeguards include:

1. **Organizational:** A defined authority to approve releases, including independent approval for changes that alter trusted signing material.
2. **People:** Trained approvers assess whether proposed releases are justified and whether unusual requests merit escalation.
3. **Technical:** A signing system enforces that only designated keys can sign a release, and receivers validate signatures and relevant release context.
4. **Physical:** Key-management equipment is protected against unauthorized physical access and tampering.

The four mechanisms can contribute to **one** security claim. A technically valid signature cannot guarantee the release was approved for a legitimate purpose. A restricted equipment room cannot ensure that remote credentials are protected. An internal policy cannot ensure that the service applied it to an emergency change. Training does not certify that no approver is compromised.

**A security objective may be distributed across organizational, human, technical and physical dependencies.** Declaring it “technical” because its visible enforcement happens in software would obscure important necessary conditions.

~~~text
Protected interest: trustworthy software release
                    |
      +-------------+-------------+
      |             |             |
 Organization     Human         Technical
 authority        review        signature validation
      |             |             |
      +-------------+-------------+
                    |
               Physical
           key/device protection

    Jointly useful safeguards, not an automatic proof
    that every unauthorized release is impossible
~~~

This diagram is a relationship sketch, not an assurance case about a real build system.

## Classification is orthogonal to control function

A control described as **technical** may operate preventively, detectively, correctively or in a recovery mode. It can serve multiple purposes simultaneously. Similarly, an organizational approval process might prevent a prohibited action, detect deviations in later reviews, and trigger remedial changes.

| Control example | Implementation form | Possible functions under stated conditions |
| --- | --- | --- |
| Identity-based access policy | Organizational authority plus technical enforcement | Prevention; sometimes detection through denied-access records |
| Camera and response staff | Physical sensor, technology, people and organizational rules | Observation and detection; containment if personnel intervene |
| Key rotation procedure | Policy, people, technical service and key storage | Correction/reduction of future exposure; recovery support for compromised keys |
| Independent transaction verification | Human responsibility and technological records | Prevention of unauthorized finalization; detection of erroneous proposals |
| Standby recovery facility | Physical site, technical replication, organizational activation | Recovery and continuity, not necessarily prevention of compromise |

These are conditional assignments. For example, a *camera* alone records imagery but does not reliably prevent a physical breach; deterrence or immediate intervention would require additional conditions. A standby service can retain the same insecure configuration as the primary service.

[Preventive, Detective, Corrective, and Recovery Controls](preventive-detective-corrective-and-recovery-controls.md) owns the **function axis**. This subject owns the **implementation and responsibility axis**. They should not be collapsed into a single hierarchical taxonomy.

## A three-axis characterization

For a selected safeguard \(c\), an explanatory profile can keep three aspects independent:

\[
\operatorname{Profile}(c)=
\bigl(
\operatorname{Implementation}(c),
\operatorname{Function}(c),
\operatorname{ProtectedProperties}(c)
\bigr).
\]

The expression is an **authored conceptual tuple**, not a NIST- or ISO-mandated machine-readable schema. Its components may hold **sets** of applicable labels rather than one forced value; the tuple deliberately does not assert that a real-world control implements only one function or medium.

The first component might include **people and technology**; the second might include **prevent and detect**; the third might include **integrity and availability**. None of the values establishes that the control has been configured, evaluated, or found effective.

For a specific protection scenario, a fourth element, **evidenced scope and outcome**, is necessary to claim actual security performance. The tuple intentionally avoids presenting product names or type labels as evidence.

### Counterexample: category completeness does not prove security

Assume a company lists 20 technological controls, 15 organizational controls, 8 people controls, and 5 physical controls, all within its own invented inventory. These totals show the inventory's **classification**, not whether any single protected operation is mediated.

Even if each control existed and worked somewhere, an unreviewed privileged-export path might bypass all relevant authorization checks. The count cannot prove:
- that each necessary boundary is covered;
- that the policies are mutually consistent;
- that shared dependencies are trustworthy;
- that controls satisfy their specified purposes;
- that actual incidents were prevented.

The example counts are fictitious and do not correspond to ISO/IEC 27002 or a specific enterprise.

## Human judgment is not an unconditional security guarantee

People can detect ambiguities a rigid classifier misses, but can also be deceived, overburdened or exposed to poorly designed responsibilities. Organizational oversight can enable security while simultaneously producing unnecessary delays or violating privacy.

A “two-person approval” is only meaningfully independent when the approval authority, evidence, incentives and identity paths are sufficiently distinct for the relevant attack/failure model. Two people who rely on the same false document can agree and still make a wrong decision. This is conceptually analogous to the common-mode concern in [Redundancy, Diversity, and Common-Mode Failure](../security-failure-resilience/redundancy-diversity-and-common-mode-failure.md), though it does not reduce people to component reliability statistics.

An organization's responsibility for a control can also be **shared with an external provider**. A cloud provider may physically secure infrastructure while the customer sets application authorization. Saying a control is “physical” does not identify which party owns, operates or verifies it.

[Ethical, Human, and Societal Constraints](../security-assurance-governance-accountability/ethical-human-and-societal-constraints.md) owns the legitimacy of authority and burden. This article addresses how control responsibilities and mechanisms are composed.

## When a control is inherited, shared or external

[NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [SP 800-53B](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final) describe controls and organization-level selection/tailoring. A system may inherit controls supplied by an organization or common control provider; this does not mean the system has verified the inherited protection for its own context.

For example, a cloud data center's physical perimeter may be operated by the provider, while tenant isolation and user-to-object authorization require distinct technical decisions. If a customer has no access to provider cameras or staff records, the appropriate **assurance evidence** differs from the evidence available for its own application checks.

**Ownership, operation, implementation and assessment authority are separate relationships.** A documented shared-responsibility diagram may identify obligations but does not substitute for confirming fulfillment.

[Controls, Safeguards, and Security Functions](controls-safeguards-and-security-functions.md) owns the generic mechanism/requirement distinction, while [Control Placement and Coverage](control-placement-and-coverage.md) owns where the control mediates relevant paths.

## Physical control and logical control can constrain each other

Physical access can permit software reconfiguration; software can command physical devices; and operators may use organizational permissions to trigger both. A physical control that protects a network switch might be effective against local cable tampering but not a compromised remote management identity.

Similarly, an electronic door controller might check technical credentials to enforce a **physical** access boundary under an **organizational** access policy. Classifying the entire system as exactly one category loses important dependencies.

A strong claim is more precise: under specified conditions, a stated subset of unauthorized persons could not use a particular entrance, based on a tested enforcement path, operational staffing and exception process. That does not imply no person could enter by any other route or that all information behind the door is confidential.

## Assessing context instead of declaring a winning category

[NIST SP 800-53A Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) provides assessment procedures, including **examine, interview and test**, for selected controls. A technical-control test may produce executable results; an organizational requirement may need document and process evidence; a physical control may need observation or inspection.

No assessment method alone establishes complete protection. The assessment objective, relevant scope, expected behavior, actual result and independent trust assumptions must be declared. [Control Effectiveness and Costs](control-effectiveness-and-costs.md) owns how to interpret measures and justify resources rather than merely counting category members.

Detailed responsibility assignment, compliance evaluation and operation are work practices assigned to [Operational Foundations](../../operational-foundations/README.md), not to this conceptual knowledge article.

## Canonical boundaries and primary source scope

- [Preventive, Detective, Corrective, and Recovery Controls](preventive-detective-corrective-and-recovery-controls.md): functional intent, not implementation categories.
- [Compensating Controls and Residual Exposure](compensating-controls-and-residual-exposure.md): substitute control relationships and what protection is left unsatisfied.
- [Control Effectiveness and Costs](control-effectiveness-and-costs.md): evidenced adequacy, efficiency and cost tradeoffs.
- [Defense in Depth and Diversity](defense-in-depth-and-diversity.md): coordinated independent-ish protective layers under bounded scenarios.
- [Redundancy, Diversity, and Common-Mode Failure](../security-failure-resilience/redundancy-diversity-and-common-mode-failure.md): failure dependencies of replicated functions.
- [Security Claims and Assurance Arguments](../security-assurance-governance-accountability/security-claims-and-assurance-arguments.md): claim-to-evidence chain.
- [Operational Foundations](../../operational-foundations/README.md): control implementation, assessment, assignment and governance execution.

### Primary sources and edition boundaries

- [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html), final edition 3 (corrected March 2022); [ISO/IEC SC 27 editors' 2022 overview](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IEC%20JTC%201-SC%2027_N22755_SC27%20Journal%20Vol%202%20Issue%202%20%28update%20Dec%202022%29.pdf), printed pp. 13–14 (**PDF indexes 14–15**, visually inspected), confirms the **four source-specific themes** and their **37/8/14/34 control counts**, and identifies five configurable metadata attributes. This is not an analysis of every full-standard clause.
- [NIST SP 800-53 Rev. 5, Release 5.2.0](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), organizational, administrative, technical and physical control aspects with topic-based control families.
- [NIST SP 800-53B](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final), source-specific federal baselines, control tailoring and common/shared controls; 2025 Release 5.2.0 changed version consistency but **not** federal baseline membership.
- [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), assessment procedures, not validation by control-category label.
- [NIST SP 800-12 Rev. 1](https://csrc.nist.gov/pubs/sp/800/12/r1/final), broad information-security principles; its older management/operational/technical framing is distinct from ISO/IEC 27002:2022 themes.

**Editorial limitations:** The example system and multi-valued tuple are editorial constructions; ISO theme counts are edition-scoped, not universal safeguards. [Technical Review 11](../PILOT-TECHNICAL-REVIEW-11.md) documents eight material claim groups and visually inspected ISO editors' journal pages. The state is **Reviewed (model-assisted) / Core claims checked**, not full ISO standard-clause verification, independent expert acceptance, deployment assurance, permanent taxonomy approval or Published.

[Security Foundations](../README.md) · [Area](README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
