# Identity and Distinction

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Identity and distinction  
**Development status:** Draft  
**Source review:** References listed; scoped technical acceptance pending

## Distinction allows entities to be counted and understood

**Distinction** is the recognition or specification of difference between subjects, properties, states, or representations. **Identity** concerns whether two references, descriptions, or appearances concern **the very same entity** under an established model or interpretation.

The first conceptual act is often to choose what counts as a subject of attention. A model that distinguishes a system from its environment also needs criteria for whether observations before and after a change refer to the same system. These are interconnected questions but not synonyms: **distinguishing two things** is not the same as knowing all their properties, and **identifying the same thing** is not necessarily equivalent to matching its name or appearance.

This article uses identity in a broad logical and modeling sense. **Authentication, identity proofing, credential issuance, access control and directory services are security-specific mechanisms**, whose canonical details belong in Security Foundations and specialized [Identity Knowledge](../../../identity/README.md).

## Numerical identity and qualitative similarity

The [Stanford Encyclopedia of Philosophy's treatment of Identity](https://plato.stanford.edu/entries/identity/) distinguishes **numerical identity** from **qualitative identity** or similarity. Qualitative similarity may hold to a degree; numerical identity is the all-or-nothing claim that the referents are one and the same thing.

**Numerical identity** holds when two expressions refer to **one and the same thing**, often written `a = b`. It is not a matter of degree. If `a` and `b` denote the same entity under an interpretation, numerical identity holds.

**Qualitative similarity** concerns sharing properties. Two separate devices may be the same model, have matching specifications and exhibit the same temperature, yet remain two numerically distinct entities. Similarity may be partial or extensive depending on which properties matter.

For example:

```text
Device A: model T7, reading 24 °C
Device B: model T7, reading 24 °C
```

The matching values do not by themselves entail that the two records describe the same device. They could describe two devices or one device observed through different systems. Additional assumptions and evidence are required to decide referential identity.

## Formal equality and equivalence

In standard classical logic, the identity relation is **reflexive** (`a=a`), **symmetric** (if `a=b` then `b=a`), and **transitive** (if `a=b` and `b=c` then `a=c`). It is an equivalence relation, but **not every equivalence relation is identity**.

For example, let `x ~ y` mean two integers have the same remainder when divided by 3. Then `4 ~ 7`, although `4 ≠ 7`. Equivalence groups things according to a specified relation; identity asserts numerical sameness.

The [Stanford Encyclopedia of Philosophy: Identity](https://plato.stanford.edu/entries/identity/) discusses the indiscernibility of identicals: within a given interpretation, anything true of an entity is true of itself even if several names refer to it. Its **converse**, the proposed identity of indiscernibles, is philosophically contested when limited to ordinary qualitative properties. We should not assert that matching every observed attribute proves numerical identity.

The formal definitions of equivalence relations belong in [Sets and Relations](../mathematics-logic/sets-and-relations.md), while [Boolean and Predicate Logic](../mathematics-logic/boolean-and-predicate-logic.md) covers identity statements in logical language.

## Identity criteria and a universe of discourse

Identifying a subject depends on **what kind of entity the model recognizes** and **which identity criteria it adopts**. The same object can be represented at different granularities: a physical computer, a virtual machine, a running service or a user-facing application may have distinct persistence conditions.

Suppose a logical service migrates from one host to another. A service-level model may treat it as the same service because its service identity and contractual role persist; a hardware inventory model treats the original and new machines as different entities. These are not contradictory if the models clearly specify their units of identity.

An identification criterion might involve provenance, continuity, structure, function, historical tracking, or a stipulated unique key. Such criteria are not automatically infallible; they are assumptions and procedures to be evaluated.

**The universe of discourse** identifies which kinds of subjects can be mentioned. Identifiers and identity rules must be interpreted within that universe, and a category change might require revisiting what counts as the same object.

## Identifiers and references are representations

An **identifier** is a name, token or structured value used to refer to an entity within some scope. It may be unique under a defined assignment scheme; that uniqueness does not automatically make it immutable, globally meaningful or sufficient to prove referential identity.

A record may contain:

```text
host_id = 0042
host_name = node-a
host_address = 192.0.2.10
```

The three values may refer to related aspects of one managed host, but only under the record producer's scope and interpretation. A hostname can be rebound, a network address can change, and an administrative identifier could be reused after retirement.

A *numeric-looking* identifier such as `0042` may not be an ordinary quantity. Removing leading zeros can erase meaningful formatting or alter a key; see [Numbers and Numerical Systems](../mathematics-logic/numbers-and-numerical-systems.md) and [Symbols and Encoding](../information-data/symbols-and-encoding.md).

W3C's [RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/) describes IRIs as identifiers and discusses the referents/resources they denote in RDF interpretations. It does not assert that an arbitrary identifier string, disconnected from assignment and interpretation, guarantees real-world identity. An IRI and its referent are not the same kind of thing.

## Identity through change

An entity can undergo changes in properties without necessarily becoming a different entity. A device may be moved, repaired, or renamed. What *counts* as persistence depends on the kind of entity and the relevant criteria.

The philosophical study of **identity over time** distinguishes identity at a time and persistence across time, and debates whether persistence is explained through continuation, temporal parts, or other accounts. See [Stanford Encyclopedia: Identity Over Time](https://plato.stanford.edu/entries/identity-time/).

A technical model can specify a practical persistence convention without claiming to settle those philosophical debates. For example, replacing one failed sensor might preserve the identity of the **measurement system** while changing the identity of one component. A device-level inventory would need a different update.

The general concept of **temporality** remains an open architectural coverage question [G-04](../COVERAGE-GAP-DECISIONS.md). This article discusses identity *under stated temporal assumptions* and does not establish a complete theory of time.

## Identity, classification and boundaries

**Classification** groups subjects by common criteria or categories. Membership in the same class does not make distinct instances identical.

**Boundaries** delimit what a model includes and excludes. They influence what counts as a single system, part, subsystem, or entity, but the boundary itself does not automatically establish the identity criteria of everything it contains.

**Relationships** can connect subjects with associations such as same-role-as, connected-to, part-of, or refers-to. None should automatically be interpreted as **numerical identity** without explicit semantics. A folder hierarchy has no inherent authority to decide whether two concepts are identical.

The corresponding canonical subject discussions are [Entities and Attributes](entities-and-attributes.md), [Relationships](relationships.md), and the approved subject [Boundaries](README.md).

## A worked representation reconciliation

Suppose two telemetry records report:

```text
Record 1: host_name = node-a, host_address = 192.0.2.10
Record 2: host_name = node-a, host_address = 192.0.2.21
```

Several interpretations remain possible: one host changed address; two hosts temporarily shared a name; a name was reused; or one record is stale. Matching hostname alone does not decide which interpretation is true.

If a separate, reliable host lifecycle record demonstrates that the same managed host was assigned both addresses at different times, the two observations can be associated with one modeled host identity under that registry's rules. But the identity inference depends on that additional evidence and the trustworthiness of its source.

This example demonstrates the difference between **identifier equality**, **contextual identity attribution**, and **independent evidence**, without turning Identity and Distinction into an authentication workflow.

## Related technical concepts and references

[Sets and Relations](../mathematics-logic/sets-and-relations.md) formalizes equality and equivalence; [Boolean and Predicate Logic](../mathematics-logic/boolean-and-predicate-logic.md) treats truth-valued identity assertions; [Entities and Attributes](entities-and-attributes.md) develops modeled subjects and properties; [State, Events and Transitions](state-events-and-transitions.md) treats change; [Evidence](../scientific-analytical-reasoning/evidence.md) explains attribution of support to claims.

### Sources

- [Stanford Encyclopedia of Philosophy: Identity](https://plato.stanford.edu/entries/identity/), revised October 2026, for numerical identity and qualitative similarity.
- [Stanford Encyclopedia of Philosophy: Identity Over Time](https://plato.stanford.edu/entries/identity-time/), for diachronic identity debates.
- [Stanford Encyclopedia of Philosophy: Identity of Indiscernibles](https://plato.stanford.edu/entries/identity-indiscernible/), for the distinct and contested converse to the indiscernibility of identicals.
- [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/), for IRIs, referents, RDF terms and resource statements.

**Editorial review note:** Numerical identity, equivalence modulo three, identity-through-change qualifications and the difference between IRI/identifier and referent were checked against the cited SEP and W3C sources. Service migration and telemetry examples remain editorial illustrations; the G-04 time question is still open. Batch 03 records model-assisted scope review without external human publication approval.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
