# Collaboration and Communication

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Collaboration and communication  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave B Batch 05 audit](../WAVE-B-TECHNICAL-REVIEW-05.md); no independent human peer review

## Coordinated action depends on shared interpretation

**Communication** is the exchange or negotiation of information and meaning among participants through some medium, convention and context. **Collaboration** involves people coordinating contributions toward one or more common or compatible objectives. Communication can occur without collaboration, and collaboration requires more than the mechanical delivery of messages.

A message being sent, delivered, read, understood, agreed with and acted upon are **distinct states or claims**. They should not be collapsed into a generic “communication successful” indicator.

The [National Academies: The Science and Practice of Team Science](https://nap.nationalacademies.org/catalog/29043/the-science-and-practice-of-team-science) analyzes team processes, communication, coordination and contextual differences. [SEBoK Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration) treats collaboration as part of whole-system integration.

## Content, meaning, intention and context

A message contains **content**, but the receiver interprets it within a **context**. The sender may have an intended meaning; the receiver's interpretation may differ. Agreement about words does not guarantee agreement about responsibility, timing or what action is authorized.

For example, “the test is complete” could mean the procedure finished, results were collected, all acceptance criteria passed, anomalies were resolved, or approval was granted. Those are distinct assertions requiring a shared vocabulary or explicit qualifiers.

[Metadata](../information-data/metadata.md) owns descriptive context for recorded information. [Evidence](../scientific-analytical-reasoning/evidence.md) owns support for claims. This article concerns the people and coordination mechanisms through which those claims are exchanged and acted upon.

## Coordination requires more than channel access

Collaboration may require shared goals, compatible roles, dependencies, decision rights, sequencing, resource commitments and agreed conventions for disagreement and change. Messaging tools can support these functions but cannot automatically supply them.

| Collaboration concern | What must be clarified |
| --- | --- |
| Goal | What outcome do participants seek? |
| Contribution | Who is responsible for which work? |
| Dependency | Whose output or decision is needed by another? |
| Authority | Who can approve, reject or redirect action? |
| Handoff | What state and evidence must be supplied? |
| Disagreement | How are conflicting interpretations or priorities resolved? |

These are editorial considerations, not six new knowledge categories or a mandatory team protocol.

## Worked example: an ambiguous handoff

Suppose Team A tells Team B: `The interface update is ready.` Team B interprets this as an approved release and starts integration. Team A intended only that a draft had been prepared.

No technical error is necessary in the messaging channel. The breakdown concerns **shared meaning and operational status**. A more explicit handoff might state:

```text
Artifact: Interface specification v2
State: Draft for review
Validation evidence: Not yet available
Approver: Interface owner
Next action: Review compatibility before integration
```

Those fields are illustrative, not a repository-wide schema. They make the difference between **artifact existence**, **evaluation**, **approval** and **authorized action** visible. They do not prove that the artifact is correct or that the receiver will interpret it as intended.

[Components and Interfaces](../systems-engineering/components-and-interfaces.md) owns technical exchange contracts; [Organizational Structures](organizational-structures.md) owns decision authority and reporting relationships.

## Synchronous, asynchronous and recorded interaction

**Synchronous** communication involves participants coordinating interaction within a shared exchange interval. **Asynchronous** communication separates message production and response in time. Neither is universally superior. A conversation can resolve ambiguity quickly but leave an incomplete record; a documented handoff can be inspectable but become stale or fail to reach the right person.

Communication media may introduce delay, missing context, translation errors, accessibility barriers or loss of nonverbal cues. A team should choose mechanisms based on the task and participants, not solely convenience.

Important decisions may benefit from explicit restatement, independent confirmation of meaning, recorded rationale and change notifications. These mechanisms require suitable norms and do not guarantee that every participant has the same mental model.

## Team processes and emergent outcomes

Collaborative behavior can depend on shared expertise, trust, psychological safety, power differences, conflict resolution and learning routines. These factors are not properties of any one message. A group may produce an effective outcome through complementary knowledge, or a poor outcome despite every member understanding their individual task.

Diversity of background can reveal missing assumptions, yet differing vocabularies can also create translation challenges. Proper coordination helps preserve the contribution of minority or dissenting views rather than reducing disagreement to a performance defect.

The [National Academies’ responsible collaboration guidance](https://nap.nationalacademies.org/pubs/29488/versions/v1.0/modules/module-2.html) discusses team roles, norms and explicit agreements. This article does not prescribe one team structure or communication style.

## Boundaries and accountability

[Decision-Making](decision-making.md) owns selection among alternatives. [Human Cognition and Perception](human-cognition-and-perception.md) owns individual attention and interpretation; [Ethics and Professional Responsibilities](ethics-and-professional-responsibilities.md) owns respectful conduct and responsible information sharing.

A successful collaboration is judged relative to goals and evidence, not simply by message volume, meeting count or the absence of visible conflict. No new ontology predicate, mandatory communication platform or assessment is introduced.

### Sources

- [National Academies: The Science and Practice of Team Science](https://nap.nationalacademies.org/catalog/29043/the-science-and-practice-of-team-science).
- [National Academies: Collaborating Responsibly](https://nap.nationalacademies.org/pubs/29488/versions/v1.0/modules/module-2.html).
- [SEBoK: Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration).

**Editorial status:** Reviewed (model-assisted) following the scoped [Wave B Batch 05 technical audit](../WAVE-B-TECHNICAL-REVIEW-05.md). Complete standards verification, independent human expert review and final publication acceptance remain separate and pending.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
