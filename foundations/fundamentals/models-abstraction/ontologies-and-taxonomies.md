# Ontologies and Taxonomies

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Ontologies and taxonomies  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Different representations answer different questions

An **ontology** is a structured account of what kinds of entities, properties, and relationships are represented in a domain, often with explicitly defined semantics and constraints. In computational contexts, an ontology can be formalized so that specified logical consequences can be derived. A **taxonomy** organizes concepts or categories using an intended classification structure, frequently broader/narrower or general/specialized relations.

Neither is synonymous with a folder tree, a schema, a statistical classifier, or a knowledge graph. A taxonomy may be one component of an ontology, and an ontology need not contain a single rooted hierarchy.

[Classification](classification.md) owns the act of assigning members to categories; this article owns conceptual structures, category relationships, and their interpretations. [Schemas](schemas.md) owns constraints on admissible data or representations.

## Distinguishing concepts, classes, and instances

A **concept** is a unit of meaning within a vocabulary or knowledge organization scheme. A **class** in a formal ontology has semantics for membership; an **individual** or **instance** is an entity that can belong to one or more classes. A term or textual label denotes a concept or class but is not the concept or class itself.

For example:

```text
Concept scheme:
  Sensor (broader concept)
    Temperature sensor (narrower concept)

Instance statements:
  device-17 is described as a temperature sensor
  device-17 measures ambient temperature
```

The first arrangement can serve navigation or retrieval; the second makes claims about a particular modeled device. Treating the broader/narrower link as logical subset membership requires an additional semantic commitment.

A classification system may assign multiple classes to one instance. Membership alone does not establish individual identity: two sensors in the same class remain distinct devices.

## Taxonomies and types of hierarchy

Different hierarchies express different relations:

- **Subtype / subclass:** every instance of the narrower class is also an instance of the broader class, under the relevant semantics.
- **Broader / narrower concept:** a concept-organization relationship that is not necessarily formal subclass inclusion.
- **Part / whole:** composition or containment, not class subsumption.
- **Instance / class:** a membership relation, not a kind-of hierarchy.
- **Dependency / prerequisite:** an ordering or reliance relation, not membership or containment.

Confusing these creates invalid inferences. If `Wheel part-of Bicycle`, a wheel is not therefore a subclass of bicycle. If `Bicycle subclass-of Vehicle`, instances of Bicycle are instances of Vehicle under the stated model.

The [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/) defines properties for concept schemes, labels and semantic relations. **SKOS broader/narrower assertions must not automatically be treated as OWL `rdfs:subClassOf` axioms**; SKOS does not, by default, impose that equivalence.

## Formal ontology languages and inference

An ontology representation can declare classes, properties, individuals, property restrictions, and relationships. In [OWL 2](https://www.w3.org/TR/owl2-overview/), logical semantics support automated entailment under a particular formal interpretation. A reasoner may infer that an individual belongs to a superclass when the ontology entails that conclusion. This is a consequence **of axioms**, not independent confirmation that the real individual has the claimed property.

Axioms can also produce inconsistency. Whether inconsistency is surfaced, and which inferences are available, depends on the chosen logic, profile and reasoner capabilities. Not all representations called ontologies have OWL expressiveness or entailment semantics.

### The open-world distinction

OWL typically follows an **open-world assumption**: a fact that is not stated or entailed is not thereby false. By contrast, many validation and database workflows intentionally assess a record against a closed list of required fields. **Logical entailment and data validation are different operations.**

For example, an ontology may not infer that `device-17` lacks a serial number solely because no serial number triple was supplied. A record schema may still reject an incoming record missing a mandatory serial-number field. The apparent difference is not a contradiction; the representation and validation goals differ.

## Ontology, taxonomy, controlled vocabulary, and graph

| Structure | Governing function | What it does not automatically guarantee |
| --- | --- | --- |
| Controlled vocabulary | Stabilize terms and intended labels | Formal class semantics |
| Taxonomy | Organize concepts by chosen relations | Complete ontology or unique tree |
| Ontology | Declare kinds, relationships and potentially logical constraints | Correctness of domain assumptions |
| Knowledge graph | Represent entities or concepts and connected statements | One particular logic, ontology or truth of claims |
| Schema | Specify permitted/required representation structure | Correctness of domain semantics or measurements |

These are **distinctions among existing practices**, not new repository knowledge-area categories or an adopted modeling stack.

## Example: two incompatible interpretations of a link

A catalog contains `Instrument → Sensor → Temperature Sensor`. If arrows mean *broader than*, they organize terms for navigation. If they mean *superclass of* under a formal class model, the inference `every temperature sensor is a sensor` is intended. If an arrow is actually a *contains* relation, that inference is invalid.

A rigorous representation must specify the semantics of the arrow. Mere graph shape cannot settle the matter. The same caution applies to a curriculum knowledge graph: a navigational dependency is not automatically a logical prerequisite, causal dependence, or subclass relation.

## Identity, boundaries, and revisions

An ontology's domain of discourse, naming and identification rules, relationship semantics, version, and consistency assumptions should be explicit when they matter. A change in meaning can break consumers even if text labels remain unchanged. Two equivalent labels do not prove two entities identical, and two different labels may denote the same concept in a particular scheme.

[Identity and Distinction](identity-and-distinction.md) governs identity, [Relationships](relationships.md) governs general relation mechanisms, and [Boundaries](boundaries.md) governs delimitation. The broader [Conceptual and Formal Models](conceptual-and-formal-models.md) article concerns modeling assumptions and logical interpretation.

## Architectural limits

This reference **does not ratify** a repository-specific ontology language, formal graph predicate list, knowledge graph engine, or additional knowledge area. The approved subject headings remain intact. Examples using SKOS or OWL demonstrate possibilities rather than requiring either for Security Education.

### Sources

- [W3C SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/).
- [W3C OWL 2 Web Ontology Language Overview](https://www.w3.org/TR/owl2-overview/).
- [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/).
- [Stanford Encyclopedia of Philosophy: Ontology](https://plato.stanford.edu/entries/ontology/).

**Editorial status:** Substantive draft; example inferences and sources require a dedicated scoped claim-to-source review.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
