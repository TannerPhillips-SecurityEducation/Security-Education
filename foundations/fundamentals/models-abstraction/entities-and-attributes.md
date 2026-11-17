# Entities and Attributes

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Entities and attributes  
**Development status:** Reviewed (model-assisted; not an independently accepted final publication)  
**Source review:** Core claims checked in [50-claim-family audit](../PILOT-CLAIM-SOURCE-AUDIT.md); independent external expert review not performed

## What a model chooses to distinguish

An **entity** is something a model treats as an individually distinguishable subject of description. An entity might represent a physical object, a person, an organization, a software component, a process, an event, an abstract number, or another subject selected for analysis. This is a modeling convention, not an assertion that every domain agrees on one universal inventory of things.

An **attribute** is a property used to describe an entity. Within a particular model an attribute has a meaning, an applicable value or range of values, and sometimes a measurement procedure, timestamp, or source. For a modeled device, possible attributes include mass, power state, location, identifier, and firmware version. Some are relatively stable; others can change.

A model does not need to describe every property of an entity. It selects those relevant to a purpose, while deliberately excluding other detail. That selection is part of [abstraction](README.md), and it should be explicit when omitted properties affect interpretation.

## A minimal conceptual structure

Consider a system model of two heating devices, `h1` and `h2`. Their descriptions might be represented as:

```text
Entity h1
  type: Heater
  rated_power: 1200 W
  mode: off

Entity h2
  type: Heater
  rated_power: 800 W
  mode: on
```

Here `Heater` is a **type or class** in the model, while `h1` and `h2` denote two instances. The attribute `rated_power` is a property that takes a quantity value, and `mode` is a variable state attribute.

This example implies assumptions about what counts as a distinct heater, which power rating is relevant, and what the allowed modes are. A different model might use components or assemblies as its primary entities and therefore assign attributes at another level.

| Distinction | Meaning |
| --- | --- |
| Entity | Subject being distinguished |
| Type or class | Category or declared kind of subjects |
| Attribute | Property relevant to that subject |
| Value | A particular description or measurement of a property |
| Identifier | Name, label, or token used to refer to an entity within some scope |
| Relationship | Association involving one or more entities |
| Schema | Rules constraining how such descriptions are represented |

These concepts are connected but not interchangeable. A property like *temperature* is not the value `23 °C`; a device with label `h1` is not identical to the string `h1`; and a type is not automatically one of its instances.

## Attributes, values, and state

The model may describe an attribute as a function from a set of entities to a domain of allowed values. If `E` contains the modeled devices, then `mode: E → {on, off}` assigns a mode to each applicable entity at a particular modeled instant. In a time-varying description, the result may also depend on time:

```text
mode(entity, time) -> value
```

Not every attribute is mandatory, single-valued, static, or directly measured. A property may be optional, multivalued, derived from another property, or uncertain. The schema and modeling assumptions determine how such cases are expressed.

**State** is a condition of an entity or system characterized by selected properties at a time or within a model context. An **event** is an occurrence, and a **transition** describes a change. A value recorded today should not silently be treated as the object's value yesterday. See the approved heading [State, events, and transitions](README.md).

## Identity and identifier are different

A model needs criteria for deciding when two observations refer to the **same entity**. That is an identity question. A serial number, hostname, row ID, or other token may help identify the intended entity, but the identifier is a **representation** that works within a particular assignment policy and scope.

An identifier might be reassigned or mistyped; two data sources may use different identifiers for the same thing; and a single logical service may retain identity through hardware replacement. Thus, *entity identity* cannot universally be reduced to *identifier string equality*.

The canonical general treatment of sameness and distinction belongs in [Identity and distinction](README.md). Authentication, proofing, and access enforcement are specialized security topics, not prerequisites for defining a model entity.

## Attributes versus relationships

An attribute can sometimes be represented as a relation between an entity and a value. But ordinary conceptual models often distinguish an **intrinsic or descriptive property** from an **association between distinct entities** because those differences affect cardinality and change semantics.

For example:

```text
h1 -- rated_power --> 1200 W
h1 -- located_in --> room-2
```

A statement about `rated_power` relates a device to a quantity. A statement about `located_in` relates the device to another modeled entity. Both can be represented as directed, labeled edges in an information model, but the interpretation of their objects and constraints matters.

The W3C [RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/) specification formalizes one graph-based representation: **subject, predicate, object** triples, with properties represented by predicates. In RDF, subjects are IRIs or blank nodes, predicates are IRIs, and objects may be IRIs, blank nodes, or literals. RDF is a useful implementation example, **not** the definition of entity or attribute in every conceptual modeling method.

## Mechanisms and limitations of modeling

When designing entity descriptions, a modeler must decide the **boundary** of the entity, the **granularity** of its parts, the properties worth recording, and the circumstances in which those properties are valid. Missing values, stale observations, uncertain measurements, and changes over time should not be silently transformed into certain facts.

A good model makes its choices inspectable: which entities exist in its universe of discourse, what makes them distinguishable, which attributes are applicable, how values are established, and which relationships connect the entities.

A practical model may evolve without the underlying object changing. Adding a `maintenance_status` attribute is a **model or schema change**; a heater switching from off to on is an **entity state change**. Their distinction is essential for sound data interpretation.

## Connections to the broader knowledge base

[Sets and relations](../mathematics-logic/sets-and-relations.md) supplies the formal language of membership and association. [Data types and datasets](../information-data/README.md) covers represented values and records. [Schemas](README.md) constrains descriptions, while [Systems and subsystems](../systems-engineering/README.md) develops composition and boundaries of systems.

Links without individual article targets intentionally lead to existing approved area indexes until substantive concept articles exist.

## References and verification status

- [W3C: RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/), for graph-based assertions, resources, and properties.
- [W3C: RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/), for illustrative triples and descriptions.
- [NASA Systems Engineering Handbook: definitions and architecture](https://www.nasa.gov/reference/system-engineering-handbook-appendix/), for relationships among system elements, attributes, and interfaces within engineering models.

**Review record:** The distinction between modeled entities, attributes, values, identifiers, and RDF graph statements was checked against W3C RDF 1.1 and NASA's systems-engineering definitions. The heater example is illustrative and does not claim that every model uses exactly this schema. The article passed the model-assisted scoped acceptance audit; independent human publication approval remains outstanding.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Canonical ownership register](../CANONICAL-OWNERSHIP-REGISTER.md)
