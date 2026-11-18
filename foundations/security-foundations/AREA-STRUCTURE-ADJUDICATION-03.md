# Security Foundations | Area-Structure Adjudication 03

**Decision date:** November 18, 2026  
**Explicit user specification:** Use **Fundamentals as the directory baseline**, with **uniform organization and tailored subject content**.  
**Approved structural pattern:** Division index → knowledge-area directory → area `README.md` → multiple substantive subject article files, as warranted by actual coverage.  
**Not implicitly ratified:** The **current twelve area names/identities**, **96 active candidate subjects**, permanent subject ownership, publication state or fixed inventory count. These remain working, flexible decisions.

## Rationale and operational change

The earlier Security Foundations `pilots/` structure overprotected provisional approval by storing every substantive reference in one flat directory. This was navigationally inconsistent with the already useful [Fundamentals baseline](../fundamentals/README.md). **Folder presence is not taxonomy ratification**; provisional areas can have real README indexes and substantive working articles while exact membership remains under architectural review.

We have therefore established the same **division → area → subject** layout at the user-requested structural level, with each area retaining its own security-specific purpose, scope and flexible depth.

## Current working areas and authored references

| Area | Working knowledge area | Candidate subjects | Substantive Reviewed references | Awaiting authoring |
| --- | --- | ---: | ---: | ---: |
| SF-01 | [Security Meaning & Objectives](security-meaning-objectives/README.md) | 8 | 2 | 6 |
| SF-02 | [Protected Interests, Assets & Harm](protected-interests-assets-harm/README.md) | 6 | 0 | 6 |
| SF-03 | [Threats, Hazards & Adversarial Behavior](threats-hazards-adversarial-behavior/README.md) | 7 | 1 | 6 |
| SF-04 | [Weaknesses, Vulnerabilities & Exposure](weaknesses-vulnerabilities-exposure/README.md) | 8 | 1 | 7 |
| SF-05 | [Security Risk & Uncertainty](security-risk-uncertainty/README.md) | 8 | 1 | 7 |
| SF-06 | [Trust, Identity & Authority Principles](trust-identity-authority-principles/README.md) | 9 | 1 | 8 |
| SF-07 | [Security Controls & Defense Mechanisms](security-controls-defense-mechanisms/README.md) | 8 | 1 | 7 |
| SF-08 | [Secure Design & Architecture](secure-design-architecture/README.md) | 9 | 1 | 8 |
| SF-09 | [Cryptography & Information Protection](cryptography-information-protection/README.md) | 9 | 1 | 8 |
| SF-10 | [Security Observation & Evidence](security-observation-evidence/README.md) | 8 | 1 | 7 |
| SF-11 | [Security Failure & Resilience](security-failure-resilience/README.md) | 8 | 2 | 6 |
| SF-12 | [Security Assurance, Governance & Accountability](security-assurance-governance-accountability/README.md) | 8 | 2 | 6 |
| **Total** | **12 provisional areas** | **96** | **14** | **82** |

Both numbers are current inventory observations, not a ceiling, floor, symmetry requirement or approval of the specific labels.

## Relocation map and link compatibility

The original article contents, review state and sources were preserved, with relative article-to-article links resolved from their new area locations. **Each substantive article has only one working content home.** Prior dated technical-audit links targeting `pilots/` remain valid via lightweight redirect stubs.

| Planning ID | Historical pilot path (navigation alias) | New working article home |
| --- | --- | --- |
| SF-01-01 | [Pilot alias](pilots/security-and-insecurity.md) | [Substantive reviewed article](security-meaning-objectives/security-and-insecurity.md) |
| SF-03-01 | [Pilot alias](pilots/threat-sources-and-threat-events.md) | [Substantive reviewed article](threats-hazards-adversarial-behavior/threat-sources-and-threat-events.md) |
| SF-04-02 | [Pilot alias](pilots/vulnerabilities-and-exploitability.md) | [Substantive reviewed article](weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) |
| SF-06-09 | [Pilot alias](pilots/access-control-policy-models.md) | [Substantive reviewed article](trust-identity-authority-principles/access-control-policy-models.md) |
| SF-08-09 | [Pilot alias](pilots/information-flow-security-and-noninterference.md) | [Substantive reviewed article](secure-design-architecture/information-flow-security-and-noninterference.md) |
| SF-09-09 | [Pilot alias](pilots/cryptographic-composition-and-protocol-security.md) | [Substantive reviewed article](cryptography-information-protection/cryptographic-composition-and-protocol-security.md) |
| SF-10-02 | [Pilot alias](pilots/observable-observed-and-recorded.md) | [Substantive reviewed article](security-observation-evidence/observable-observed-and-recorded.md) |
| SF-12-01 | [Pilot alias](pilots/security-claims-and-assurance-arguments.md) | [Substantive reviewed article](security-assurance-governance-accountability/security-claims-and-assurance-arguments.md) |
| SF-05-01 | [Pilot alias](pilots/risk-scenarios-and-time-horizon.md) | [Substantive reviewed article](security-risk-uncertainty/risk-scenarios-and-time-horizon.md) |
| SF-07-01 | [Pilot alias](pilots/controls-safeguards-and-security-functions.md) | [Substantive reviewed article](security-controls-defense-mechanisms/controls-safeguards-and-security-functions.md) |
| SF-01-08 | [Pilot alias](pilots/security-privacy-safety-and-reliability.md) | [Substantive reviewed article](security-meaning-objectives/security-privacy-safety-and-reliability.md) |
| SF-11-01 | [Pilot alias](pilots/compromise-and-loss-of-security.md) | [Substantive reviewed article](security-failure-resilience/compromise-and-loss-of-security.md) |
| SF-11-04 | [Pilot alias](pilots/resilience-survivability-and-robustness.md) | [Substantive reviewed article](security-failure-resilience/resilience-survivability-and-robustness.md) |
| SF-12-08 | [Pilot alias](pilots/ethical-human-and-societal-constraints.md) | [Substantive reviewed article](security-assurance-governance-accountability/ethical-human-and-societal-constraints.md) |

### Distinguish structure approval from knowledge approval

- **Established now:** Uniform, Fundamentals-style **directory pattern**. Each provisional working area has its own README, live subject inventory, actual article links, and explicit reviewed/unwritten status.
- **Still proposed:** Membership/identity of the twelve named areas; 96 subject candidates and detailed semantic ownership. Split, merge, move, rename or add when evidence warrants.
- **Existing bounded review preserved:** The fourteen working articles remain **Reviewed (model-assisted) / Core claims checked** with their original three pilot-review records. Moving Markdown files does **not** make them Verified or Published.
- **Historical material preserved:** `pilots/README.md` remains the prior-wave review register; legacy article paths point to their new homes instead of duplicating the article bodies.
- **Future authoring:** Place substantive Markdown directly within its most appropriate area directory, and update that area's README, [development register](DEVELOPMENT-VERIFICATION-REGISTER.md) and [working ownership register](CANONICAL-OWNERSHIP-REGISTER.md) together. Use a provisional classification when genuine ownership remains unresolved.

## Review and validation

Dynamic checks must ensure every currently inventoried area has one matching README, every authored subject has one actual working area article with correct ID/frontmatter, and pilot aliases are not counted as duplicate knowledge. **No fixed expected area count or subject total** should be enforced.

The repository-wide and Security Foundations GitHub Actions workflows check local links and inventory consistency. They **do not** check external source availability, scientific truth, standards conformance, independent expert review or publication acceptance.

[Security Foundations](README.md) · [Architecture Proposal](ARCHITECTURE.md) · [Inventory](SUBJECT-INVENTORY-PROPOSAL.md) · [Development Plan](DEVELOPMENT-PLAN.md) · [Security Foundations AGENTS](AGENTS.md)
