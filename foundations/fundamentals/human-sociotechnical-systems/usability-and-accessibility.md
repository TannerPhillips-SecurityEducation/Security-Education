# Usability and Accessibility

**Knowledge area:** [Human & Sociotechnical Systems](README.md)  
**Approved subject heading:** Usability and accessibility  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source technical review pending

## Useful is not the same as usable or accessible

**Usability** concerns how effectively, efficiently and satisfactorily **specified users** achieve **specified goals** in a **specified context of use**, following the conceptual framework of [ISO 9241-11:2018](https://www.iso.org/standard/63500.html). **Accessibility** concerns whether people with diverse abilities and circumstances can perceive, understand, navigate, and operate a system or content, including when using appropriate assistive technologies.

Usability and accessibility overlap but are not synonyms. A technically accessible interface can still be confusing or inefficient; an interface that works smoothly for one selected group can exclude other users. Neither property is an inherent yes/no attribute of an entire system independent of tasks, users and environment.

[NIST Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design) emphasizes context, representative users and iterative evaluation. [ISO 9241-171:2025](https://www.iso.org/standard/86308.html) concerns software accessibility for a wide range of abilities; its detailed paid standard text is not reproduced here.

## Effectiveness, efficiency, satisfaction, and barriers

**Effectiveness** addresses whether users achieve intended goals accurately and completely. **Efficiency** relates resources used to the outcomes achieved. **Satisfaction** addresses users' responses to the experience in its relevant context. Different metrics may conflict or improve independently.

| Concern | Possible observation | Why interpretation is limited |
| --- | --- | --- |
| Effectiveness | Tasks completed correctly | Choice of tasks and users changes results |
| Efficiency | Time, effort, steps or resources used | Fast completion can conceal mistakes |
| Satisfaction | Reported experience | Responses depend on context and expectations |
| Accessibility | Whether essential functions can be used with different interaction needs | One successful modality does not establish universal accessibility |

These are **evaluation perspectives**, not newly approved knowledge-area branches. A task might be ineffective because of absent functionality, confusing interface structure, poor documentation, environmental conditions, or an accessibility barrier.

## Web accessibility versus general accessibility

The [W3C Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) organizes web-content requirements around four principles: **Perceivable, Operable, Understandable, and Robust**. WCAG 2.2 provides testable success criteria within its defined scope; it is not a complete universal standard for every industrial control, physical device, or organizational process.

Examples of accessibility-related mechanisms include text alternatives for meaningful images, keyboard access, adequate text contrast, understandable focus order, captions for relevant media, visible focus, and clear instructions. Their technical requirements depend on the applicable criteria and system context.

Accessibility cannot be reduced to a single color contrast ratio or automated checklist. Automated tools can detect some violations but cannot independently determine whether all interactions are understandable, meaningful, or usable with assistive technologies.

## Worked example: a keyboard access barrier

Consider an invented settings interface with a Save control that can be activated with a mouse but is unreachable from keyboard navigation.

A user operating only a keyboard may enter the required information but cannot complete the Save task. The interface may look visually clear while still excluding that interaction path. Adding a correctly labeled keyboard-operable Save control and an appropriate focus order addresses **candidate barriers**, but it does not itself establish full accessibility of the application.

The example is a conceptual comparison; it has not been tested with real participants, assistive technologies, or a formal WCAG conformance procedure. A defensible claim would specify applicable success criteria, supported technology environments and the evidence collected.

[Human-Computer Interaction](human-computer-interaction.md) owns the interaction mechanisms; [Human Cognition and Perception](human-cognition-and-perception.md) owns attention and interpretation.

## Inclusive design and variation

People's requirements can differ with sensory, motor, cognitive, linguistic, environmental, technological or temporary circumstances. Some disabilities are invisible; different people with superficially similar needs may prefer different accommodations.

An inclusive design process considers variation without treating everyone as interchangeable or inferring an individual's capability from a diagnostic or demographic label. Allowing adjustable text size, alternative input, clear semantics and recoverable actions can improve access, but each measure still needs evaluation in its context.

A system that meets one published accessibility level does not automatically meet every user need. Similarly, a prototype that satisfies one group's preference does not establish fitness for every group.

## Requirements and lifecycle responsibilities

Usability and accessibility goals should be expressed in requirements and checked in realistic contexts. An assertion like “the system shall be accessible” is insufficiently testable unless its scope, standard/version, applicable criteria, users, technology and evaluation method are stated.

A revision may introduce new barriers even if functionality remains available to mouse users. Accessibility review should therefore occur throughout design, testing, deployment and change management rather than only at launch.

[Requirements](../systems-engineering/requirements.md) owns the system's specified criteria; [Verification and Validation](../systems-engineering/verification-and-validation.md) owns conformance and intended-use evidence. Neither replaces specialist accessibility evaluation.

### Sources

- [ISO 9241-11:2018: Usability, Definitions and Concepts](https://www.iso.org/standard/63500.html).
- [ISO 9241-171:2025: Software Accessibility](https://www.iso.org/standard/86308.html).
- [W3C WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/).
- [NIST Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design).

**Editorial status:** Substantive Draft. The keyboard barrier is illustrative; full technical/source review remains pending. No accessibility compliance certification or new curriculum category is asserted.

[Human & Sociotechnical Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
