# Security Knowledge

A domain-organized knowledge repository with a **hierarchy for navigation** and a **knowledge graph for relationships**.

**Contributor and agent SOP:** [AGENTS.md](AGENTS.md) governs evidence-led collaboration, variable knowledge structure and content depth, canonical ownership, authoring, reviews, approvals and validation across this repository. Subtree instructions refine it without overriding approved architecture.

## Foundations

- [Fundamentals](foundations/fundamentals/README.md)
- [Security Foundations](foundations/security-foundations/README.md)
- [Operational Foundations](foundations/operational-foundations/README.md)

[Foundations overview](foundations/README.md)

## Knowledge Domains

The approved navigation model is **Domain → Function → Implementation**. Functions are primary; specific technologies, platforms, operating systems, providers, and other contexts can also be found through secondary indexes and cross-domain relationships.

| Domain | Primary functional navigation |
| --- | --- |
| [Network Knowledge](network/README.md) | Network functions |
| [Endpoint Knowledge](endpoint/README.md) | Host system functions |
| [Application Knowledge](application/README.md) | Application functions |
| [Cloud Knowledge](cloud/README.md) | Cloud service functions |
| [Industrial Knowledge](industrial/README.md) | Industrial system functions |
| [IoT Knowledge](iot/README.md) | Connected-device functions and roles |
| [Identity Knowledge](identity/README.md) | Identity and access functions |

### Alternate Navigation Perspectives

- [Operating system families](endpoint/README.md#operating-system-family-indexes-secondary-navigation)
- [Application types](application/README.md#application-type-indexes-secondary-navigation)
- [Cloud providers](cloud/README.md#cloud-provider-indexes-secondary-navigation)

These indexes are maintained for discovery and learning. They should point to canonical function or implementation documents instead of replicating them.

## Publication Scope

This repository is a **technical knowledge reference**. It contains concepts, explanations, mechanisms, examples, relationships, and references. It does **not** contain **Knowledge Checks** or **Practical Assessments**. Technical verification of factual claims is still part of maintaining the reference.

## Architectural Principles

1. **One canonical home** for each documented subject.
2. **Function-first navigation** within each specialized domain.
3. **Implementation details** belong with their applicable functions, subject to approved placement.
4. **Multiple entry points** through operating systems, providers, application types, and other indexes.
5. **Knowledge graph relationships** connect subjects across domains and perspectives. A directory location is not necessarily conceptual parentage.
6. **Foundations** provides shared concepts but is not a mandatory reading sequence.
7. **Extensibility** without redefining established categories.

[Knowledge relationship conventions](RELATIONSHIPS.md)

## Related

[Security Operations Portfolio](https://github.com/TannerPhillips-SecurityEducation/Security-Operations-Portfolio)

> **Current state:** The functional navigation skeleton is established. Implementation pages, graph schema, and graph engine have not yet been created or approved.
