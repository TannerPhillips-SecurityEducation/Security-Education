# Weaknesses, Vulnerabilities & Exposure

**Division:** [Security Foundations](../README.md)  
**Working area ID:** SF-04  
**Architecture status:** **Provisional area membership and naming**, within a user-approved **Fundamentals-style directory architecture**. The number and names of areas and subjects can expand or contract.  
**Current content:** **8 candidate subjects; 2 substantive articles**, both Reviewed (model-assisted); 6 without an article. Neither is source-Verified or Published.

## Scope and canonical ownership

This working area groups **weaknesses, vulnerabilities & exposure** concepts that share a security-specific explanatory purpose. Boundaries follow the [working inventory](../SUBJECT-INVENTORY-PROPOSAL.md), [ownership decisions](../OWNERSHIP-BOUNDARIES.md), and [governing architecture proposal](../ARCHITECTURE.md), not a rigid formal ontology. Generic science/technical concepts belong in [Fundamentals](../../fundamentals/README.md); security practices belong in [Operational Foundations](../../operational-foundations/README.md); product-specific implementations belong to the seven specialized domains.

The area may be renamed, split, consolidated, or relocated when stronger conceptual and source evidence justifies it. **A directory is a navigation home, not automatically a ratified subject taxonomy.**

## Subject inventory and actual articles

| ID | Proposed subject or actual article | Development and source state | Intended conceptual responsibility |
| --- | --- | --- | --- |
| SF-04-01 | Weaknesses and root causes | **Inventoried / not authored** | Distinguish general flaw classes from particular vulnerable instances. |
| SF-04-02 | [Vulnerabilities and exploitability](vulnerabilities-and-exploitability.md) | **Reviewed (model-assisted)** · Core claims checked | Describe context-dependent ways a weakness can be used to violate protection. |
| SF-04-03 | Exposure and attack surface | **Inventoried / not authored** | Describe accessible interfaces, paths, assets, and reachable opportunities. |
| SF-04-04 | Preconditions and reachability | **Inventoried / not authored** | Explain required state, authority, location, timing, and access conditions. |
| SF-04-05 | Exploitation and security violations | **Inventoried / not authored** | Distinguish attempted exploitation, successful violation of a security property, and compromise; the broader state and consequences of compromise belong to SF-11-01. |
| SF-04-06 | Severity, exploitability, and context | **Inventoried / not authored** | Separate generic severity labels from system-specific consequences and risk. |
| SF-04-07 | Weakness chains and dependency failures | **Inventoried / not authored** | Describe interacting flaws and upstream or transitive exposure. |
| SF-04-08 | [Side channels, covert channels, and unintended information leakage](side-channels-covert-channels-and-unintended-information-leakage.md) | **Reviewed (model-assisted)** · Core claims checked in [Review 05](../PILOT-TECHNICAL-REVIEW-05.md) | Distinguish leakage inferred from side effects, deliberate hidden communication and unintended disclosure; specific hardware/protocol cases remain specialized. |

**Review interpretation:** Both authored area articles now have separate scoped audits: SF-04-02 under [Review 01](../PILOT-TECHNICAL-REVIEW-01.md) and SF-04-08 under [Review 05](../PILOT-TECHNICAL-REVIEW-05.md). Both are **Reviewed (model-assisted) / Core claims checked**, not source-Verified, independently peer-reviewed, Published or confirmed as permanent canonical ownership. Remaining **Inventoried** entries are proposed coverage subjects, not failed articles.

## Development and relationships

New substantive references belong **inside this area directory**, directly under its `README.md`, following the [Fundamentals area pattern](../../fundamentals/mathematics-logic/README.md). Each article owns a coherent security-specific concept and links meaningfully to related areas and sources. Do not add a file merely to match the number of subjects in another area or the length of a Fundamentals chapter.

For development/review use [AGENTS.md](../AGENTS.md), [Development Plan](../DEVELOPMENT-PLAN.md), [Scope and Gap Review](../COVERAGE-AND-GAPS-REVIEW-03.md) and the [historical pilot register](../pilots/README.md). Substantive articles in this directory are the current working manuscript source; historical `pilots/` paths remain navigation aliases.

[Security Foundations](../README.md) · [All candidate subjects](../SUBJECT-INVENTORY-PROPOSAL.md) · [Root SOP](../../../AGENTS.md)
