# Relationships

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Relationships  
**Development status:** Reviewed (model-assisted; not independently human-accepted)  
**Source review:** Core claims checked in [Wave A Technical Review, Batch 02](../WAVE-A-TECHNICAL-REVIEW-02.md); full independent validation not claimed

## Relationships make modeled entities meaningful in context

A **relationship** is an association described between two or more participant roles, subjects, or values within a specified model or context. In some cases the same subject can occupy multiple roles, so the participants need not be distinct individuals. A relationship may express containment, dependency, similarity, ordering, communication, ownership, spatial position, causation, or another interpreted association. These meanings must not be treated as interchangeable merely because they can all be drawn with a line or arrow.

The central conceptual distinction is between a relationship **as interpreted meaning** and the formal structure used to represent it. A mathematical binary relation is a set of ordered pairs; a conceptual relationship is an interpretation that can require scope, roles, evidence, conditions, and change over time.

The formal mathematics belongs in [Sets and Relations](../mathematics-logic/sets-and-relations.md). This article owns the **domain-agnostic conceptual semantics** of associations among modeled entities.

## Relata, roles, direction, and meaning

The entities or values that participate in a relationship are often called its **relata**. A model must identify participants and what roles they play.

Consider the statement:

```text
sensor-1  -- measures -->  temperature-room-2
```

The arrow can be understood as a modeled direction from measuring instrument to measured property. It does not assert that the property measures the sensor, and it does not establish that every sensor reading is accurate. The relationship label conveys the intended meaning. The actual measurement mechanism requires a distinct explanation in [Measurement](../scientific-analytical-reasoning/measurement.md).

An explicit relationship description should usually clarify these facets when relevant:

| Facet | Concern |
| --- | --- |
| **Participants** | Which entities, types, values or roles participate? |
| **Relation meaning** | What kind of association is asserted? |
| **Direction** | Does the association distinguish source and target roles? |
| **Multiplicity** | How many participants can or must satisfy it? |
| **Scope and conditions** | Under what assumptions or circumstances does it hold? |
| **Time or change** | Is the association stable, observed at a time, or valid during an interval? |
| **Support or origin** | Is it stipulated, inferred, measured, asserted or directly observed? |

These are **explanatory considerations**, not seven newly ratified graph predicates or a mandatory metadata schema.

## Binary, n-ary, and contextual relationships

A **binary** relation involves ordered pairs in a formal model. A **ternary** relation involves triples, and a relationship with `n` roles is called **n-ary**. In philosophical discussions, relations are conventionally distinguished from unary properties; in set-theoretic and computational formalisms, unary predicates can also be treated as unary relations. The convention must be specified. Some associations cannot be accurately represented without additional context.

For instance:

```text
operator-3  assigned_to  system-7
```

This might be true today but false last month, or might hold only for a specific responsibility. A richer conceptual model could describe:

```text
Assignment(
  operator = operator-3,
  system = system-7,
  role = maintainer,
  valid_from = 2026-11-01
)
```

This is an illustrative **relation instance with attributes**. It avoids treating one timeless edge as the complete meaning of a time-sensitive responsibility. A different schema may represent the same information differently.

Time-based validity does not mean this article has defined general temporality. That broader foundational scope remains open under [G-04](../COVERAGE-GAP-DECISIONS.md).

## Multiplicity, constraints, and cardinality

A relationship's **cardinality** describes permitted or required numbers of participating instances. One-to-one, one-to-many, and many-to-many are familiar abstractions, but precise constraints depend on the model's vocabulary and whether the relationship is optional.

For example, a model might stipulate that each measurement record references **exactly one** observed device, while a device can have **zero or many** measurement records. That is a **schema constraint**, not a statement proven by observing any arbitrary collection of records.

The ability to represent a relationship does not establish that all its instances exist, satisfy constraints, or reflect reality. Those are validation and evidential questions.

A relationship can also have **roles** rather than unnamed endpoints. In a purchase model, the buyer and seller are both persons or organizations but perform different roles. Direction or role names prevent the meaning from collapsing into a vague assertion that the two subjects are merely connected.

## Distinguishing common relationship kinds

Several relationship types appear frequently in technical models, but they have different consequences.

**Classification / kind-of:** Saying an instance or subtype belongs to a category is different from saying it physically contains another thing. Category membership, subtype relations, and identity need explicit logical rules.

**Part-of:** Describes composition or inclusion of a component in a larger whole under a defined scope. This may be physical, functional or organizational; not every part relation is transitive under every contextual interpretation.

**Depends-on:** Expresses a required condition, resource, or association for some capability or outcome. Dependency direction must be explicit: `A depends on B` is not the same as `B depends on A`.

**Uses or communicates-with:** Describes an interaction or capability. It does not automatically imply hierarchy, ownership or trust.

**Same-as versus equivalent-to:** Numerical identity means one and the same referent. Equivalence means indistinguishability *under a selected relation or criterion*, and can hold between distinct subjects. Two identifiers matching by string do not automatically prove referential identity; an equivalence relation is not necessarily the identity relation.

**Evidence-for or supports:** Expresses a claim-relative evidential or inferential relationship. It is not logically equivalent to the claim itself being true. See [Evidence](../scientific-analytical-reasoning/evidence.md).

**Causes:** A causal assertion requires stronger justification than mere co-occurrence or statistical correlation. See [Causality and Correlation](../scientific-analytical-reasoning/README.md).

These phrases illustrate distinctions worth preserving. The repository has **not approved a closed, formal relationship-predicate vocabulary**, and this article does not establish one by listing them.

## Relations are not necessarily symmetric or transitive

The mathematics of relations provides useful properties, but a conceptual relationship does not inherit a property merely from its label or visualization.

For example:

```text
A --depends-on--> B
B --depends-on--> C
```

Whether `A` should also be considered dependent on `C` depends on the chosen meaning of dependency. It might mean an immediate dependency, in which case the assertion may be absent, or a transitive reachability relation, in which case indirect dependency may be derived.

Likewise, if `A` communicates with `B`, the communication may be directional and asymmetric. A directed arrow does not become bidirectional because both endpoints are present in one diagram.

The formal criteria for **symmetric**, **antisymmetric**, **reflexive**, and **transitive** relations belong to [Sets and Relations](../mathematics-logic/sets-and-relations.md). Conceptual models must specify which, if any, apply to their interpreted predicates.

## A knowledge graph is a representation, not the world itself

A **knowledge graph** commonly uses nodes and edges or structured assertions to describe entities and their relationships. Its usefulness depends on definitions of nodes, predicates, scope and interpretation.

The W3C [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) specification provides one precise graph-based representation using **subject-predicate-object** triples. In RDF 1.1, subjects are IRIs or blank nodes, predicates are IRIs, and objects may be IRIs, literals, or blank nodes. Those are constraints of **RDF 1.1**, not requirements on every graph model or every relationship in existence.

For example, a conceptual representation might say:

```text
sensor-1 -- located_in --> room-2
sensor-1 -- measures   --> temperature-room-2
```

A graph could encode these two assertions with typed predicates. But the graph does not, from its mere existence, prove sensor calibration, the physical location at a particular moment, or the quality of the underlying evidence.

**Navigation hierarchy versus conceptual relationships** is a critical distinction for this repository. Placing a concept in a folder is a way of finding its canonical article; it is not automatically an `is-a` or `part-of` assertion. See the [Governing Fundamentals Architecture](../ARCHITECTURE.md) and [Repository Relationship Conventions](../../../RELATIONSHIPS.md).

## A worked conceptual example

Imagine a system that has a pump, control software, a tank, and a level sensor.

```text
level-sensor -- observes --> tank-level
controller   -- receives --> sensor-report
controller   -- issues   --> pump-command
pump         -- moves    --> liquid
```

Each association has different semantics. Observing a tank-level property does not establish that the sensor's indication is correct; issuing a command does not prove the pump executed it; and moving liquid does not by itself establish the resulting level after all environmental effects.

A useful model may add timing, uncertainty, failure conditions, and evidence links, but those additions must be justified by the question being studied. **An edge is an assertion, not a complete explanation.**

## Canonical relationships to other areas

[Entities and Attributes](entities-and-attributes.md) develops modeled participants and properties; [Sets and Relations](../mathematics-logic/sets-and-relations.md) provides mathematical structure; [Systems and Subsystems](../systems-engineering/systems-and-subsystems.md) describes composition; [State, Events, and Transitions](state-events-and-transitions.md) describes modeled change; [Evidence](../scientific-analytical-reasoning/evidence.md) describes claim-relative support.

## Reference starting points

- [W3C: RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/), subject/predicate/object triple structure and graph interpretation.
- [W3C: RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/), readable examples of directed and typed assertions.
- [Stanford Encyclopedia of Philosophy: Relations](https://plato.stanford.edu/entries/relations/), philosophical and logical perspectives on relational structures.
- [Stanford Encyclopedia of Philosophy: Identity](https://plato.stanford.edu/entries/identity/), numerical identity and its distinction from qualitative equivalence.
- [MIT OpenCourseWare: Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/), binary relations and mathematical properties.

**Review record:** The general participant/role distinctions, cardinality, relation arity, identity versus equivalence, and RDF 1.1 triple constraints were checked against W3C and Stanford Encyclopedia of Philosophy sources. Seven descriptive facets and the pump example remain editorial illustrations, not ratified graph predicates. This article passed the scoped model-assisted review documented in the Wave A Batch 02 audit; independent human publication acceptance remains outstanding.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
