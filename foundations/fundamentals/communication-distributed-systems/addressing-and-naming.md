# Addressing and Naming

**Knowledge area:** [Communication & Distributed Systems](README.md)  
**Approved subject heading:** Addressing and naming  
**Development status:** Draft  
**Source review:** Authoritative references listed; scoped technical audit pending

## Names, identifiers and addresses describe different relationships

A **name** is a symbol used to refer to an entity or resource under a namespace. An **identifier** distinguishes a referent within some defined scope or identity system. An **address** commonly specifies a location or routing/communication reference used to reach a resource through a chosen mechanism.

One string can serve multiple purposes, but the purposes should not be conflated. A stable human-readable name may resolve to changing addresses; several names can refer to one service; one address can serve multiple named resources. A syntactically valid name is not evidence of a genuine or trustworthy entity.

[Identity and Distinction](../models-abstraction/identity-and-distinction.md) owns general referent identity; this subject owns communication naming, addressing and resolution.

## Namespace, scope and resolution

A **namespace** establishes how names are assigned and distinguished. **Resolution** transforms a name or reference into some target representation, such as one or more addresses or another identifier, under a declared authority and context.

A resolution result can be stale, unavailable, inconsistent or invalid for the current task. A successful response does not automatically establish the intended target's authenticity, availability or fitness for use.

[DNS concepts and facilities in RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) provide a concrete example of a hierarchical, distributed naming design. Other naming systems may be flat, local, content-based or application-specific. DNS is an example, **not** the universal definition of naming.

## Worked example: stable name, changing endpoint

Suppose a fictional service has the documentation name `sensor.example`. At one time its recorded destination address is `192.0.2.10`; after a service relocation it is `192.0.2.20`. These two addresses are in a documentation-only block, and the example does not describe actual deployed service records.

```text
Time A: name sensor.example → address 192.0.2.10
Time B: name sensor.example → address 192.0.2.20
```

The **name stays unchanged while the address changes**. This does not prove that the same physical device or software instance provides the service in both cases, or that a name-resolution response has been authenticated.

Multiple instances could answer for one service name. Conversely, one instance could be reachable by several names or addresses. Identity, location, and authority require separate contracts.

## URI structure versus resource identity

An illustrative URI `https://example.com/measurements?id=7#top` has scheme `https`, authority `example.com`, path `/measurements`, query `id=7` and fragment `top` under [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html).

The fragment is interpreted by the relevant client/application scheme; it is not intrinsically a network transport destination. Different URIs can identify related resources, and a URI does not itself authenticate a server. Parsing syntax and resolving meaning are different steps.

This article does not define all aspects of URI or DNS specifications; it uses them to demonstrate why name structure, resolution and authorization are separate.

## Addressing and communication endpoints

An endpoint may require additional selectors beyond a network address, such as a service identifier, port or protocol context. A port alone is not necessarily a globally unique service identity.

Addressing rules depend on layer and scope. A link-level address, routed network address and application resource identifier are distinct even if all appear as strings or byte fields.

[Protocols and Layering](protocols-and-layering.md) owns exchange layer conventions; [Communication Channels](communication-channels.md) owns possible paths and capacity. [Software Interfaces](../software-programming/software-interfaces.md) owns application-facing contract meaning.

## Temporal and security limitations

Name resolution and routing can change over time. Caching may preserve an old mapping, while a new mapping can point to a resource with different capabilities. A name-resolution step may also fail or return several candidate targets.

Such uncertainty does not imply every result is wrong; it means the guarantee must be scoped. General temporality G-04 remains unresolved and is not decided by this applied naming article.

### Sources

- [RFC 1034: Domain Names, Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html).
- [RFC 3986: URI Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.html).
- [RFC 5737: IPv4 Address Blocks Reserved for Documentation](https://www.rfc-editor.org/rfc/rfc5737.html).

**Editorial status:** Substantive Draft. URI parsing, address examples and identity claims require a separate technical/source audit. No DNS deployment, security practice or assessment is mandated.

[Communication & Distributed Systems](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
