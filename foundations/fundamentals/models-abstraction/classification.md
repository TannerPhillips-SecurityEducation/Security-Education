# Classification

**Knowledge area:** [Models & Abstraction](README.md)  
**Approved subject heading:** Classification  
**Development status:** Reviewed (model-assisted)  
**Source review:** Core claims checked; [Wave A Batch 06 audit](../WAVE-A-TECHNICAL-REVIEW-06.md); no independent human review

## Classification makes distinctions according to criteria

**Classification** is the grouping or assignment of subjects to categories according to selected attributes, relationships, rules, or other criteria. It may describe observed properties, express a stipulated conceptual organization, or support a decision. Its results are only as meaningful as the classification criteria and underlying information.

The concept is **domain-independent**: physical substances, biological organisms, documents, system components, mathematical objects, and events can all be classified. A classification scheme should specify the **universe of subjects**, the basis for distinguishing them, the categories, and which assignments count as valid.

Classifying an object does not necessarily establish its identity, value, causal history, or fitness for a particular purpose. A category membership statement can be true while the reason for the observed property remains unknown.

This article owns the **general classification mechanism**. It does not define a new taxonomy of security threats, an application-specific machine-learning classifier, or an unapproved knowledge-graph predicate system.

## Entities, attributes, classes, and instances

A **class** or **category** collects subjects satisfying a specified rule or sharing some modeled property. An **instance** is a particular subject to which category membership may apply.

Consider three modeled devices:

```text
Device A: portable, powered
Device B: stationary, powered
Device C: portable, unpowered
```

A classification criterion **mobility** places A and C into `Portable` and B into `Stationary`. A different criterion **power state** places A and B into `Powered` and C into `Unpowered`.

The categories answer different questions, so their assignments must not be collapsed into a single absolute classification of the device. These two **facets** can coexist.

General entities and properties are defined under [Entities and Attributes](entities-and-attributes.md). [Identity and Distinction](identity-and-distinction.md) governs sameness; two devices belonging to the same category are not necessarily the same device.

## Exhaustive, exclusive, and overlapping categories

A classification scheme may be designed as a **partition** of its universe: its classes are collectively exhaustive and pairwise disjoint.

- **Exhaustive:** Every subject in the defined universe belongs to at least one of the classes.
- **Mutually exclusive:** No subject in the defined universe belongs to more than one class.
- **Partition:** Both properties hold, and normally each class of the partition is nonempty.

Many useful classification schemes **do not** form partitions. A document might simultaneously be technical, historical and introductory. A resource could have several functional roles. A category assignment may be partial if the necessary data are missing.

For a universe `U={A,B,C}`, a partition could be `Portable={A,C}` and `Stationary={B}` if the model's mobility categories are valid for all these subjects and no subject satisfies both. A second facet, power status, provides a different partition.

The [MIT Mathematics for Computer Science material](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/) supplies set membership, partitions and equivalence relations as formal foundations.

## Membership, uncertainty, and graded classification

Under a crisp set-based criterion, membership is a yes/no property under the specified interpretation. For example, `temperature ≥ 30 °C` defines a precise threshold **over a reported numerical value**.

That does not prove the physical temperature was measured without error, nor that the chosen threshold denotes a natural physical discontinuity. The classification can be precise even if the measurement is uncertain.

Other schemes allow **graded membership**, such as a fuzzy-set model in which a subject has a degree of membership between zero and one. A fuzzy membership degree is **not automatically** the probability that an uncertain subject belongs to the class. Probability models uncertainty about outcomes or propositions under assumptions; fuzzy sets model degrees of membership under chosen semantics.

A scheme may also allow **Unknown** or **Unclassified** when evidence is insufficient. This is a state of knowledge about classification, not necessarily an additional property of the underlying entity. The distinction is developed in [Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md).

## Categories, taxonomies, and ontologies

A **taxonomy** organizes categories according to an intended hierarchy, usually broader/narrower or specialized/general relationships. An **ontology** may formalize kinds, properties, constraints, and logical relationships in a more expressive representation.

Classification is the act of assigning or grouping subjects according to criteria; a taxonomy or ontology can provide the conceptual structures those assignments use. None of the three terms is a synonym for a directory tree.

The W3C [Simple Knowledge Organization System (SKOS)](https://www.w3.org/TR/skos-reference/) provides a standardized representation for concepts, labels, broader/narrower and related links, concept schemes and collections. The [OWL 2 Overview](https://www.w3.org/TR/owl2-overview/) describes a more formal ontology language with classes, properties, individuals and logical semantics.

**SKOS broader/narrower links are not automatically OWL subclass axioms.** A navigational or thesaurus hierarchy can represent conceptual organization without committing to every logical consequence of a strict class-subsumption relationship. [Ontologies and Taxonomies](ontologies-and-taxonomies.md) develops this distinction further.

No repository-specific SKOS or OWL implementation is hereby introduced or approved. These standards are reference examples of distinct ways to represent knowledge.

## Single-label, multi-label, hierarchical and faceted classification

Some systems assign **exactly one category** from an approved set, while others permit several labels.

| Classification design | Meaning | Illustration |
| --- | --- | --- |
| Single-label | One label from the chosen class set | Exactly one lifecycle stage |
| Multi-label | Multiple labels may apply simultaneously | A document may be both technical and introductory |
| Hierarchical | Categories are organized by stated broader/narrower relations | Instrument → Sensor → Temperature Sensor |
| Faceted | Independent dimensions of categorization are combined | Mobility and power status |
| Partial | A category may remain unknown or unassigned | Missing measurement value |
| Graded | Membership has a defined degree | Fuzzy model of “warm” |

These are **illustrative classification approaches**, not six additional knowledge areas or a mandated formal schema.

A **hierarchical** classification need not be a strict mathematical tree if categories have multiple parents. A **faceted** scheme may allow combinations that are invalid for a particular domain, in which case additional constraints are necessary.

## Rule-based and learned classification are different implementations

A **rule-based classifier** assigns categories through explicit criteria, such as numerical thresholds or logical predicates. A **statistically learned classifier** uses training data and an estimation procedure to learn a mapping or decision boundary. Both realize classification, but they have distinct development and validation concerns.

For example:

```text
Rule:
    if reported_temperature >= 30:
        label = HIGH
    else:
        label = NOT_HIGH
```

This rule defines classification by a reported value. It does not claim that all physically meaningful temperatures have a natural division at 30 or that the sensor always reports correctly.

A trained machine-learning system may produce scores or probability estimates, but those outputs do not make *classification itself* synonymous with AI or guarantee calibrated confidence. The unresolved [AI/ML coverage decision G-06](../COVERAGE-GAP-DECISIONS.md) remains separate from the general foundational concept.

## Classification quality and the role of evidence

Classification requires more than choosing labels. A defensible classification includes an identifiable rule, a valid scope, and enough evidence to justify applying it to the subject.

Different failure modes should be kept distinct:

- **Bad definition:** A category lacks a coherent criterion.
- **Insufficient information:** The category is well defined, but evidence does not determine membership.
- **Measurement error:** The recorded attribute does not accurately describe the subject.
- **Rule error:** The assignment procedure fails to follow the stated criterion.
- **Semantic mismatch:** The assigned label carries a different meaning to the consumer.
- **Scope mismatch:** A scheme designed for one population or context is applied to another without justification.

An erroneous classification does not necessarily mean the subject changed, or that its identity was incorrectly established. The error may be in observation, representation, mapping, or inference.

[Observation](../scientific-analytical-reasoning/observation.md), [Evidence](../scientific-analytical-reasoning/evidence.md), [Measurement](../scientific-analytical-reasoning/measurement.md) and [Schemas](schemas.md) cover neighboring concepts.

## Worked example: two independent facets

Under the stipulated three-device universe:

| Device | Mobility class | Power-state class |
| --- | --- | --- |
| A | Portable | Powered |
| B | Stationary | Powered |
| C | Portable | Unpowered |

From this model, `Portable={A,C}`, `Powered={A,B}`, so their intersection is `Portable ∩ Powered={A}`. This is a set-theoretic result based on the stated assignments.

It is not evidence that those are all actual devices or that the supplied properties were measured correctly. If C's power status were unknown, the scheme should preserve that uncertainty instead of silently treating C as unpowered.

The example illustrates **canonical ownership separation**: Mathematics & Logic defines set operations, Models & Abstraction defines category meaning and membership rules, and Information & Data describes how records encode the assignments.

## Relationships and references

[Sets and Relations](../mathematics-logic/sets-and-relations.md) supplies membership and partitions. [Entities and Attributes](entities-and-attributes.md) supplies subjects and properties. [Identity and Distinction](identity-and-distinction.md) separates reference from category membership. [Relationships](relationships.md) develops associations, while [Boundaries](boundaries.md) develops inclusion/exclusion and scope limits.

### Sources

- [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/), lightweight concept schemes, broader/narrower and related concept relations.
- [W3C OWL 2 Overview](https://www.w3.org/TR/owl2-overview/), formal classes, properties, individuals and logical semantics.
- [MIT Mathematics for Computer Science Readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/), sets and equivalence classes.

**Editorial status:** Reviewed (model-assisted) following the scoped [Batch 06 technical audit](../WAVE-A-TECHNICAL-REVIEW-06.md). Not independently human peer reviewed, fully verified, or published.

[Models & Abstraction](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
