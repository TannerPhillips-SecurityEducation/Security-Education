# Security Education

**A living technical knowledge base for Network Security Operations, Zeek, threat hunting, detection engineering, and practical education.**

This repository develops technical concepts and educational material. Documentation is organized by subject, with explicit status indicators to distinguish drafts from verified resources.

## Explore

| Section | Description |
| --- | --- |
| [Foundations](foundations/README.md) | Networking, security, systems, data, and evidence |
| [Network Security Operations](network-security-operations/README.md) | NSO, NSM, NTA, and NDR |
| [Zeek](zeek/README.md) | Learning, architecture, engineering, development, analysis |
| [Threat Hunting](threat-hunting/README.md) | Methodology, models, and investigations |
| [Detection Engineering](detection-engineering/README.md) | Detection design, validation, and refinement |
| [Technical Education](technical-education/README.md) | Learning methods, labs, and assessment |

## Foundational NSO architecture

```text
Network Activity --NSM--> Network Telemetry --NTA--> Network Evidence --NDR--> Security Action
```

- **NSM — Network Security Monitoring:** Capture & Collect; Transform & Record; Store & Retrieve.
- **NTA — Network Telemetry Analytics:** Select; Compare; Correlate; Aggregate; Calculate; Present.
- **NDR — Network Detection & Response:** Detection; Investigation; Response.

Network telemetry includes **packets, logs, metrics, and traces**. This architecture is a conceptual framework for developing and teaching network security practices.

## Editorial standards

- Mark material as **Draft**, **Under Review**, or **Validated**.
- Distinguish observation from derivation, inference, and action.
- Specify prerequisites, assumptions, and validation procedures for labs.
- Cite authoritative references where practical.
- Do not present planned work as completed implementation.

## Related repository

[Security Operations Portfolio](https://github.com/TannerPhillips-SecurityEducation/Security-Operations-Portfolio) highlights professional work and links to technical projects.

*Licensing and contribution policy are still to be defined. Public access does not automatically grant unrestricted reuse.*
