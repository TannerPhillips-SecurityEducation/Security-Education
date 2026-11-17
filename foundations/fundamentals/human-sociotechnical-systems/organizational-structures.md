# Organizational Structures

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Organizational structures  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 05 audit](../WAVE-B-TECHNICAL-REVIEW-05.md); no independent human peer review

## An organization arranges roles, authority and relationships

An **organization** is a purposeful arrangement of people, responsibilities, authorities, processes, resources and relationships. **Organizational structure** describes how that arrangement allocates coordination and decision-making responsibilities. It is not simply an organizational chart, a legal entity, or a collection of individuals.

Structures may be formalized through reporting lines and documented roles, or operate partly through informal expertise, trust and coordination. A chart can state who reports to whom while omitting who has the relevant technical knowledge, who actually influences decisions, or how work moves across teams.

[SEBoK: Organizing Businesses and Enterprises to Perform Systems Engineering](https://sebokwiki.org/wiki/Organizing_Business_and_Enterprises_to_Perform_Systems_Engineering) treats organizational design as contingent on goals, stakeholder needs, capabilities and environmental context. Its definitions are engineering references, not an obligation to use one management structure.

## Roles, people, responsibility, authority and accountability

A **person** is not the same thing as a **role**. One person may hold several roles; a role can be assigned to different people over time. **Responsibility** concerns assigned duties or work. **Authority** concerns permissions to make binding decisions or take actions. **Accountability** concerns obligations to explain, answer for and remedy outcomes under specified governance arrangements.

These terms have organization-dependent definitions. Writing someone's name beside an activity does not automatically grant the authority to approve or override it.

For a hypothetical system update:

| Role | Illustrative responsibility |
| --- | --- |
| Specification owner | Maintain interface requirements |
| Implementer | Develop the requested change |
| Reviewer | Evaluate evidence and record concerns |
| Authorizer | Approve or reject deployment under governing criteria |
| Operator | Execute the authorized change |

The roles can overlap under some governance systems. When conflicts of interest or high consequences matter, separating duties may improve independent scrutiny, but division can also produce delay or ambiguous handoffs. A structure must be assessed against actual objectives.

## Centralized, distributed and matrix arrangements

**Centralized authority** concentrates selected decisions. **Distributed authority** delegates selected decisions to different roles or units. A **matrix arrangement** can assign people or work to overlapping functional and project relationships.

These are illustrative patterns, not exclusive categories. A largely centralized organization may delegate technical decisions, and a decentralized group may still share strict legal or financial controls.

Tradeoffs include speed, consistency, local knowledge, resilience, coordination effort, conflict, and transparency. Neither centralization nor decentralization is inherently safer, more equitable, or more effective in every context.

## Worked example: an authorization ambiguity

Suppose Team A owns an interface specification and Team B maintains a system that consumes it. A developer implements a format change, and an operations colleague receives the message: `Ready to release`.

The phrase can mean the implementation was completed, the change was reviewed, or deployment was authorized. Without a defined decision authority and evidence standard, Team B might act on a message that was not approval.

A more explicit process identifies the specification owner, change reviewer, person authorized to accept compatibility risk, and operator responsible for deployment. It should also identify the relevant revision and acceptance evidence. The improved arrangement is a **governance proposal**, not proof that every release will succeed or that the hierarchy is optimal.

[Collaboration and Communication](collaboration-and-communication.md) owns handoff meaning and shared interpretation. [Requirements](../systems-engineering/requirements.md) owns specification criteria; [Verification and Validation](../systems-engineering/verification-and-validation.md) owns engineering evidence.

## Formal structure and actual behavior

People may rely on informal networks because formal processes are inaccessible, too slow, incomplete or misunderstood. Such workarounds can be helpful in one context and dangerous in another. The existence of an informal path is evidence of actual coordination behavior, not automatically of misconduct.

An organization can also experience **goal conflict**. A team rewarded for speed may optimize delivery time at the expense of reliability if quality and risk ownership are poorly defined. The effect is conditional on incentives and operating conditions, not inevitable merely because a metric exists.

Human-system integration includes ensuring that operational duties, training, resources and feedback align with technical designs. [SEBoK Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration) emphasizes humans and organizational context throughout a system's lifecycle.

## Change, governance, and adaptation

A structure may evolve as systems, people, budgets, legal duties or external conditions change. Changes in authority should not be inferred solely from title changes. Clear delegation, documented interfaces and review pathways make responsibilities more inspectable, yet documentation can become stale.

Governance requires mechanisms for correcting errors, questioning decisions, resolving conflicts and addressing people affected by outcomes. An escalation path that cannot be used in practice is not equivalent to effective accountability.

[Human Error](human-error.md) addresses deviations and contributing conditions, not simply rule violations. [Ethics and Professional Responsibilities](ethics-and-professional-responsibilities.md) owns duties and harm-related constraints when authority is exercised.

## Canonical boundaries

Organizational structures differ from system-component topology, communication protocols, formal graph relations and professional ethics. [Architecture and Composition](../systems-engineering/architecture-and-composition.md) explains general system-wide organization, while this subject owns the **human authority and responsibility arrangements**.

No organizational chart template, management doctrine, mandatory governance model, universal role taxonomy or assessment is introduced.

### Sources

- [SEBoK: Organizing Businesses and Enterprises to Perform Systems Engineering](https://sebokwiki.org/wiki/Organizing_Business_and_Enterprises_to_Perform_Systems_Engineering).
- [SEBoK: Organization (glossary)](https://sebokwiki.org/wiki/Organization_%28glossary%29).
- [SEBoK: Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration).
- [National Academies: Collaborating Responsibly](https://nap.nationalacademies.org/pubs/29488/versions/v1.0/modules/module-2.html).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 05 technical audit](../WAVE-B-TECHNICAL-REVIEW-05.md). Complete standards verification, independent human expert review and final publication acceptance remain separate and pending.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
