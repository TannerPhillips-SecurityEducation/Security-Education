# Wave B Technical Review: Batch 05

**Review date:** November 17, 2026  
**Scope:** Human Cognition and Perception; Decision-Making; Human-Computer Interaction; Usability and Accessibility; Human Error; Collaboration and Communication; Organizational Structures; Ethics and Professional Responsibilities.  
**Method:** Reopened all eight canonical GitHub drafts, inspected 48 material claim groups, compared the principal claims against publicly accessible NIST, W3C, ISO catalog, APA, HSE, National Academies, SEBoK and ACM references, recomputed the worked quantitative case, assessed non-conflation boundaries, and reopened all 24 distinct relative Markdown file destinations.  
**Disposition:** **48 material claim groups reviewed; eight articles pass scoped model-assisted technical review** after the correction documented below. This is not an exhaustive source-by-source expert review, full content review of paywalled standards or NASA PDF volumes, independent human peer review, field usability study, compliance certification, or final publication acceptance.

## Claim-to-source ledger

### Human Cognition and Perception
[Reviewed article](human-sociotechnical-systems/human-cognition-and-perception.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| HC-01 | Perception and cognition overlap but are distinct processes | [NIST Human-Centered Design](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design); article correctly separates observing signals from interpreting their meaning |
| HC-02 | Attention and interpretation depend on task, context and cues | [HSE Workload](https://www.hse.gov.uk/humanfactors/topics/workload.htm); avoids universal individual predictions |
| HC-03 | Working-memory capacity and task demands are constrained, not a fixed universal item count | HSE Workload; appropriately avoids an unsupported single-number rule |
| HC-04 | External labels and representations may reduce ambiguity yet can be stale or wrong | NIST HCD; design guidance framed as conditional, not guaranteed |
| HC-05 | Unlabeled duplicate green indicators versus role-labeled state text | Invented comparison is internally coherent; article does not claim measured superiority for every user |
| HC-06 | Cognition, HCI, observation and decision-making retain separate ownership | Canonical definitions and [SEBoK Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration); no new cognitive taxonomy imposed |

### Decision-Making
[Reviewed article](human-sociotechnical-systems/decision-making.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| DM-01 | A decision process is distinct from action and realized outcome | [NASA Technical Risk Management](https://www.nasa.gov/reference/6-4-technical-risk-management/); outcome alone does not establish process quality |
| DM-02 | Evidence, forecast/model, objective and choice are different inputs or products | [NIST HCD](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design); conceptual explanatory distinctions, not a mandated schema |
| DM-03 | Heuristics aid efficiency without guaranteeing a correct result | [APA Dictionary: Heuristic](https://dictionary.apa.org/heuristic); avoids labeling every disagreement a cognitive bias |
| DM-04 | Availability heuristic and salient examples can distort frequency judgments | [APA Dictionary: Availability Heuristic](https://dictionary.apa.org/availability-heuristic); effect is conditional, not universal |
| DM-05 | Illustrative expected costs for two alternatives | Calculated A=`40+0.10×100=50`, B=`55+0.02×100=57`; A has smaller expected cost **only under the stipulated model** |
| DM-06 | Decision quality and outcome quality can diverge under uncertainty | Evidence and model assumptions explicitly distinguished; no assertion that expected value alone decides ethics or risk acceptability |

### Human-Computer Interaction
[Reviewed article](human-sociotechnical-systems/human-computer-interaction.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| HCI-01 | HCI includes people, tasks, interfaces and use context, not just visual UI | [NIST HCD](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design); supported |
| HCI-02 | Action, response, perceived feedback and interpretation differ | NIST HCD; conceptual cycle not presented as obligatory psychometric model |
| HCI-03 | Affordance, signifier, mapping and constraints concern interaction design | General human-centered design concepts; no asserted universal standard vocabulary or conformance |
| HCI-04 | Acknowledging a command does not entail successful physical state change | Invented STOP/acknowledged/relay-ON case is logically consistent; real device behavior remains unknown |
| HCI-05 | Multi-modal and assistive interaction needs depend on users and environment | NIST HCD and [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/); alternatives are not automatically accessible |
| HCI-06 | Observed task performance must carry sample and environmental scope | NIST HCD's iterative evaluation approach; no usability trial is claimed |

### Usability and Accessibility
[Reviewed article](human-sociotechnical-systems/usability-and-accessibility.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| UA-01 | Usability is relative to specified users, goals and context | [ISO 9241-11:2018 catalog](https://www.iso.org/standard/63500.html); describes purpose and terminology, not paywalled clauses |
| UA-02 | Accessibility and usability overlap but neither entails the other | [ISO 9241-171:2025 abstract](https://www.iso.org/standard/86308.html) and NIST HCD |
| UA-03 | Effectiveness, efficiency, satisfaction and accessibility have distinct evaluation perspectives | ISO 9241-11 catalog and NIST HCD; editorial table is not a new ratified assessment taxonomy |
| UA-04 | WCAG 2.2 organizes web requirements as Perceivable, Operable, Understandable, Robust | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/); generalizing beyond applicable scope is explicitly avoided |
| UA-05 | Mouse-operable but keyboard-inaccessible Save control is a meaningful barrier | [W3C WCAG 2 at a Glance](https://www.w3.org/WAI/standards-guidelines/wcag/glance/); original illustrative case, not a completed conformance test |
| UA-06 | Automated checks and one successful modality do not prove accessibility for all users | NIST HCD/WCAG; no certification claimed |

### Human Error
[Reviewed article](human-sociotechnical-systems/human-error.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| HE-01 | Error, deviation, adverse outcome and culpability are distinct claims | [UK HSE Managing Human Failures](https://www.hse.gov.uk/humanfactors/topics/humanfail.htm); **corrected** first definition to distinguish unintended errors from deliberate violations |
| HE-02 | Intention, action and outcome can diverge | HSE guidance; heater A/B error case is stipulated, not attributed to an observed person |
| HE-03 | Slips, lapses, mistakes and violations are different explanatory classes | [HSE Managing Human Failures](https://www.hse.gov.uk/humanfactors/topics/humanfail.htm); correct that violations are intentional, while slips/lapses/mistakes are unintentional |
| HE-04 | Error-mitigation measures are conditional on workload, task and design | [HSE Workload](https://www.hse.gov.uk/humanfactors/topics/workload.htm); no assertion that confirmation dialogs universally remove errors |
| HE-05 | Unlabeled temperature units can produce semantic misinterpretation | Invented 20 °F versus 20 °C case is coherent; no unique individual fault inferred |
| HE-06 | Causal account, accountability and blame require different evidence and judgments | HSE human-factors framework; no inference of negligence from an outcome alone |

### Collaboration and Communication
[Reviewed article](human-sociotechnical-systems/collaboration-and-communication.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| CC-01 | Message transport and shared understanding are distinct | [National Academies Team Science report](https://nap.nationalacademies.org/catalog/29043/the-science-and-practice-of-team-science); context-specific communication requirements |
| CC-02 | Roles, objectives, handoffs and authority shape coordination | [National Academies: Collaborating Responsibly](https://nap.nationalacademies.org/pubs/29488/versions/v1.0/modules/module-2.html); explicit agreements are supported |
| CC-03 | Ambiguous 'ready' status can produce wrong decisions | Invented draft/review/approval handoff example is logically consistent; not a measured failure case |
| CC-04 | Synchronous and asynchronous media involve different tradeoffs | National Academies 2025 Team Science materials; not a universal ranking |
| CC-05 | Collaboration depends on environment, trust and psychological safety | National Academies 2025/2026 publications; association not converted into guaranteed causal outcome |
| CC-06 | Communication mechanisms are distinct from organization and technical interface contracts | Canonical scope retained; exemplar handoff fields are not required repository schema |

### Organizational Structures
[Reviewed article](human-sociotechnical-systems/organizational-structures.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| OS-01 | Organization involves people, responsibilities, authorities and relationships | [SEBoK Organization glossary](https://sebokwiki.org/wiki/Organization_%28glossary%29); wording consistent with referenced systems-engineering definition |
| OS-02 | Roles, people, responsibility, authority and accountability differ | [SEBoK Organizing Businesses and Enterprises](https://sebokwiki.org/wiki/Organizing_Business_and_Enterprises_to_Perform_Systems_Engineering); role allocation requires explicit context |
| OS-03 | Centralized, distributed and matrix patterns have tradeoffs | SEBoK Organizing Businesses and Enterprises; illustrative rather than exclusive structure classes |
| OS-04 | Implementing, reviewing, authorizing and operating are distinct responsibilities | Invented release governance example; no mandatory separation-of-duties policy asserted |
| OS-05 | Formal reporting and informal coordination can diverge | SEBoK organization guidance; an organization chart is not an exhaustive model of actual behavior |
| OS-06 | Organization structure affects requirements and accountable decisions | [SEBoK Human Systems Integration](https://sebokwiki.org/wiki/Human_Systems_Integration); causal results depend on assumptions |

### Ethics and Professional Responsibilities
[Reviewed article](human-sociotechnical-systems/ethics-and-professional-responsibilities.md)

| ID | Material claim | Supporting evidence and disposition |
| --- | --- | --- |
| EP-01 | Technical possibility, authorization and ethical justification are distinct | [ACM Code of Ethics](https://www.acm.org/code-of-ethics); code is computing-specific, not a universal legal doctrine |
| EP-02 | Harms, rights, privacy, fairness and professional competence can be relevant | ACM Code principles 1 and 2; details remain context-dependent |
| EP-03 | Multiple ethical lenses can give different assessments | Editorial lenses clearly declared, not a single mandated universal ethical theory |
| EP-04 | Accuracy, uncertainty, expertise and independent review constrain responsible claims | ACM Code provisions on honesty, competence, review and risk evaluation |
| EP-05 | Faster mouse task with inaccessible keyboard Save exposes a competing concern | Invented example appropriately separates limited usability observation from accessibility and ethical acceptability |
| EP-06 | Accountability and escalation remain relevant throughout a system lifecycle | ACM Code and NIST HCD; no compliance certification, legal advice or policy imposition implied |

## Corrections made before acceptance

**Human Error:** Distinguish **unintentional errors** (slips, lapses and mistakes) from **deliberate procedural violations**; an adverse outcome is not proof of either and a deliberate violation does not automatically establish malice, negligence or an unjustified action. Added the UK Health and Safety Executive as explicit grounding and revised the category section accordingly.

The remaining seven articles required **no material correction within this scoped review**. Their original worked scenarios are inventions used to teach the conceptual distinctions, not externally observed trials or studies attributed to NIST, NASA, the National Academies, SEBoK, W3C or ACM.

## Worked examples and calculation checks

| Check | Result |
| --- | --- |
| Decision-making example: Option A | Expected cost `40 + 0.1×100 = 50` units |
| Decision-making example: Option B | Expected cost `55 + 0.02×100 = 57` units |
| HCI STOP message and physical relay still ON | No logical contradiction if command acknowledgment is not state confirmation |
| Accessibility keyboard-only user cannot reach Save | A hypothesized interaction barrier, **not** a measured rate or formal WCAG conformance finding |
| Intended Heater A versus selected Heater B | Action–intention mismatch; causal explanation remains unspecified |
| Organizational 'ready to release' handoff | Under-specified approval state; a proposed clarification, not empirical evidence |

## Link verification and source limitations

The eight articles have **83 relative Markdown link occurrences** resolving to **24 distinct local file destinations**, and **all 24 file destinations were reopened successfully through GitHub**. These checks exclude fragment anchors, live external URLs, interpretation of referenced terms, and the rest of the repository's link graph.

Primary guidance checked online included NIST HCD, ISO publication catalog/abstracts, W3C WCAG, APA Dictionary entries, UK HSE public human-factors pages, National Academies publications, SEBoK and ACM public ethics material. **The full paid ISO standards and NASA's linked human-spaceflight PDF volume were not independently analyzed**, so a claim that all their text was source-verified would be unsupported. The review is at a **material claim-family level**, not an exhaustive line-by-line review.

## Architectural and acceptance boundaries

- General cognitive limits, decision-making, HCI, inclusive usability, human error, collaboration, organizational roles and professional ethics remain in **their eight existing approved canonical headings**.
- Wave A remains 26/26 internally Reviewed; Information & Data 9/9 and Systems & Engineering 11/11 remain internally Reviewed. Eight newly reviewed Human & Sociotechnical Systems articles bring the Wave B corpus to **28/28 internally Reviewed**.
- Portfolio reconciliation following this audit is **55 Reviewed (model-assisted), 0 Draft, 54 Inventoried without article = 109 approved headings**.
- G-01 mathematical breadth, G-04 general temporality and G-06 AI/ML remain separately unresolved. No Knowledge Checks, Practical Assessments, new approved areas or headings, compliance certification, or mandatory ethical code adopted.
- **Reviewed (model-assisted)** with **Core claims checked** is not **Verified**, independently human peer-reviewed or **Published**.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
