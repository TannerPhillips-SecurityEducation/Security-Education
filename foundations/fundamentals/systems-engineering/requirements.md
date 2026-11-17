# Requirements

**Knowledge area:** [Systems & Engineering](README.md)  
**Approved subject heading:** Requirements  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped claim-to-source audit pending

## Requirements state what a system must satisfy

A **requirement** expresses a necessary condition, capability, constraint, or performance expectation for a specified system, product, service, or element. It is a statement about what must hold under defined circumstances, not proof that the condition has been achieved. Requirements help connect stakeholder purposes to architecture, engineering choices, interfaces, integration and acceptance.

A requirement should identify an appropriate **subject**, a **condition or behavior**, relevant **operating context**, and a sufficiently clear **criterion for evaluation**. Required wording depends on the organization's established specification conventions. The [NASA Technical Requirements Definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/) process uses explicit “shall” statements and traceability, while stressing communication with stakeholders and validation of the requirements themselves.

## Needs, expectations, requirements and solutions

A **stakeholder need** describes an outcome valued by the people or organizations affected. A **system requirement** translates that need into conditions the system of interest must fulfill. A **design solution** identifies a possible means of satisfying those conditions.

For a hypothetical heating system:

```text
Stakeholder need:
  Maintain a comfortable room temperature.

System requirement:
  When valid measured temperature is at or below 18 °C,
  the controller shall request heating, while in automatic mode.

Possible design:
  A particular controller, sensor and actuator arrangement.
```

The requirement introduces explicit conditions but does not fully specify comfort, sensor validity, response time or the system's behavior during failures. Those would require further definitions or separate requirements. The design is one possible realization; it is **not logically entailed** by the need.

[Architecture and Composition](architecture-and-composition.md) owns design organization. [State and Behavior](state-and-behavior.md) owns the operational state model. [Components and Interfaces](components-and-interfaces.md) owns interaction contracts.

## Requirements have different purposes

Requirements can address function, performance, external interface, environmental conditions, maintainability, safety, accessibility, resource limits or other relevant qualities. Their meaning should follow the system and stakeholder context rather than a universal label scheme.

| Illustrative concern | Example focus |
| --- | --- |
| Functional | What capability is required? |
| Performance | How much, how often, how quickly? |
| Interface | What may the system exchange, with whom, and under what contract? |
| Constraint | What physical, legal, resource or design boundaries apply? |
| Quality | What reliability, usability or maintainability criteria must be satisfied? |

These are **illustrative concerns**, not five new approved subcategories or an exhaustive taxonomy. A statement can span multiple concerns and may need decomposition for precise evaluation.

## Well-formed and verifiable statements

A useful requirement is unambiguous within its defined context, feasible in principle, necessary to a stated purpose, consistent with other requirements, and evaluable through a defined procedure. Ambiguous modifiers such as *fast*, *secure*, *efficient* or *user-friendly* are insufficient by themselves when the desired level is not defined.

Compare:

```text
Ambiguous:
  The system shall respond quickly.

More evaluable, hypothetical:
  After receiving a valid input in automatic mode,
  the controller shall issue a command within 200 ms,
  as measured from input acceptance to command output.
```

The revised statement supplies a measured event pair and threshold but still depends on defining *valid input*, acceptable timing instrumentation and test conditions. **Writing a testable sentence does not demonstrate compliance.** The 200 ms value is invented for explanation, not a broadly applicable engineering target.

Multiple linked requirements may need separate tests to avoid one statement hiding independent acceptance conditions.

## Traceability and allocation

**Traceability** records relationships among stakeholder needs, requirements, architecture elements, tests, changes and evidence. An allocation assigns a requirement to an element or function expected to fulfill it. A relation may be one-to-many or many-to-one, and tracing links alone do not establish causal truth or completed verification.

An explanatory trace might be:

```text
Need N1
   ↓ informs
Requirement R1
   ↓ allocated to
Controller function F1
   ↓ evaluated by
Verification procedure V1
   ↓ produces
Evidence record E1
```

Every arrow has a **specific declared meaning**. This is a conceptual trace, not a new approved knowledge-graph predicate vocabulary. A requirement may need multiple verification procedures and evidence records. A test record can show a result without proving that the initial need was correctly understood.

[Dependencies](dependencies.md) owns conditional reliance. [Evidence](../scientific-analytical-reasoning/evidence.md) owns claim-relative support.

## Conflicts, changes and baselines

Requirements often conflict with one another or compete for constrained resources. Short response times, low energy use, reliability, accessibility and cost may require trade studies. A requirement should not be changed silently to match a preferred implementation.

A **baseline** identifies an approved set of requirements at a specified revision for a governed purpose. Change management assesses reasons, impacts, approvals, dependent elements and evidence affected by a revision. Version identity enables comparisons but does not guarantee requirements are correct or complete.

Requirements can be revised as knowledge changes; formalization does not freeze reality. [System Lifecycle](system-lifecycle.md) develops evolution and change management as a system-level concern.

## Verification versus requirements validation

**Requirements validation** evaluates whether the specified set adequately reflects stakeholder needs, intended use and constraints. **Product verification** evaluates whether an implemented system satisfies the specified requirements. A product can pass a technically precise requirement that does not address the actual need.

The separate [Verification and Validation](verification-and-validation.md) article develops evidence methods, acceptance interpretation and limits. [Validation and Falsification](../scientific-analytical-reasoning/validation-and-falsification.md) owns the broader epistemology of empirical claim criticism, not engineering requirements ownership.

### Sources

- [NASA: Technical Requirements Definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/).
- [SEBoK: System Requirements Definition](https://sebokwiki.org/wiki/System_Requirements).
- [NASA: Requirements Management](https://www.nasa.gov/reference/6-2-requirements-management/).

**Editorial status:** Substantive Draft. The hypothetical thermostat requirement, traceability example and semantic distinctions require their own scoped technical review. No new assessment, safety mandate or formal schema is ratified.

[Systems & Engineering](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
