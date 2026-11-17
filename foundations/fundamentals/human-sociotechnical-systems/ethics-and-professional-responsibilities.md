# Ethics and Professional Responsibilities

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Ethics and professional responsibilities  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source technical review pending

## Technical capability and justified action are different

**Ethics** concerns reasoned evaluation of how actions affect people, communities, institutions and other things of value, including duties, harms, rights, fairness and consequences. **Professional responsibility** concerns obligations attached to the exercise of specialized skill, organizational authority, public trust and applicable standards of conduct.

An action can be technically possible, organizationally authorized, legally permitted and still ethically questionable. Conversely, a professional may face genuine conflicts among duties that cannot be resolved by a single maxim or calculation.

The [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) emphasizes societal well-being, avoidance of harm, honesty, fairness, privacy, competence and professional review in computing. It is a profession-specific reference, **not** a universal substitute for all cultural, legal, engineering or philosophical approaches to ethics.

## Stakeholders and effects

A **stakeholder** is a person, group or organization with a relevant interest, responsibility or exposure to the system or decision. Relevant stakeholders may include users, nonusers affected by system operation, maintainers, operators, owners, regulators, surrounding communities and future recipients of consequences.

Identifying a stakeholder does not settle how interests should be weighed, whether a demand is justified, or who has decision authority. Evaluating effects requires distinguishing evidence about likely outcomes from normative judgments about which outcomes are acceptable.

**Harm** can concern physical safety, privacy, exclusion, economic loss, diminished autonomy, environmental effects or other adverse consequences. Its likelihood, severity, scope and reversibility may vary. The same design choice can create benefits for some people and costs for others.

## Several ethical lenses, no imposed universal doctrine

Professional reasoning can consider:

| Perspective | Guiding concern |
| --- | --- |
| Consequences | What benefits, harms and risks could follow? |
| Duties and constraints | Which obligations or prohibitions apply? |
| Rights and autonomy | Whose legitimate choices and protections are at stake? |
| Fairness | Who receives benefits, burdens and opportunities for appeal? |
| Professional integrity | Are claims accurate, competence sufficient and conflicts disclosed? |

These are **explanatory perspectives**, not newly ratified categories, a hierarchy of values, or one mandatory ethical theory for this knowledge repository. Ethical arguments need explicit premises, context and defensible conclusions.

[Decision-Making](decision-making.md) owns selection mechanisms under uncertainty; [Evidence](../scientific-analytical-reasoning/evidence.md) owns support for factual claims. Neither alone determines moral acceptability.

## Honesty, uncertainty, and informed reliance

A professional should distinguish confirmed results, assumptions, model outputs, missing data, and unsupported claims. Representing a prototype test as proof of production readiness misleads decision makers even if the test truly passed.

Competence includes recognizing the boundaries of one's training and arranging additional review or specialist input when needed. A confident presentation does not establish that a person or organization has the expertise to manage a particular risk.

**Transparency** is not the indiscriminate publication of all information. Personal privacy, confidentiality, security, intellectual-property obligations, informed consent and legitimate public scrutiny can pull in different directions. Responsible disclosure needs context-specific judgment and applicable rules.

## Worked example: accessible capability and a release decision

Suppose a fictional service is updated to complete a user task in two steps instead of five for mouse users. During testing, reviewers find that the final control cannot be activated by keyboard alone.

The shorter mouse path is a positive usability observation within its tested scope, but it does not establish overall accessibility or justify ignoring the exclusion of keyboard-only users.

Possible actions include delaying deployment, repairing the interaction, providing an effective interim alternative, communicating limits, or adopting a risk-governed phased rollout. The ethically defensible choice depends on who is affected, how consequential the task is, the alternatives available, the evidence, applicable obligations and the authority to accept residual risks.

**Neither a faster completion metric nor a formal approval automatically settles the ethical question.** The example is invented and does not describe a particular organization, product or compliance finding.

[Usability and Accessibility](usability-and-accessibility.md) owns inclusive-use mechanisms and evaluation. [Requirements](../systems-engineering/requirements.md) owns specified system criteria. [Organizational Structures](organizational-structures.md) owns decision rights and governance arrangements.

## Conflicts, escalation and accountability

A professional may confront conflicts among employer instructions, stakeholder interests, professional standards, and harms to people outside the immediate project. A responsible process makes conflicts explicit, seeks evidence, records reasoned objections and uses appropriate review or escalation mechanisms.

Accountability includes the ability to explain decisions, identify who authorized them, correct errors and learn from consequences. It does not require pretending that every adverse outcome was foreseeable, nor should it permit avoidable harms to be dismissed as merely technical details.

A code of ethics can guide conduct but cannot guarantee good outcomes. Its language and enforcement differ across professions and jurisdictions. This article does not provide individualized legal advice or declare a binding policy for readers.

## Public trust and lifecycle implications

Ethical duties do not end at initial implementation. Monitoring, correction, accessibility maintenance, privacy, informed communications, impact review and responsible retirement can matter throughout the system lifecycle.

[System Lifecycle](../systems-engineering/system-lifecycle.md) owns engineered-system evolution; [Collaboration and Communication](collaboration-and-communication.md) owns information exchange; [Human Error](human-error.md) owns error conditions without reducing causal analysis to blame.

### Sources

- [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics).
- [SEBoK: Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration).
- [NIST: Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design).
- [W3C: Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/).

**Editorial status:** Substantive Draft. Normative distinctions and the invented accessibility case require a dedicated source/technical review. No required ethical theory, compliance certification, policy enforcement or assessment is instituted.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
