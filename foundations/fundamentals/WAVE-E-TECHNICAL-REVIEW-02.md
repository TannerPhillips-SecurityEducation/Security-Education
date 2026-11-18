# Wave E Technical Review: Batch 02 — Communication & Distributed Systems

**Review date:** November 17, 2026  
**Scope:** Communication Models; Transmission and Signaling; Communication Channels; Protocols and Layering; Addressing and Naming; Latency and Throughput; Reliability and Ordering; Distributed State; Synchronization and Coordination.  
**Method:** Reopened all nine canonical GitHub articles, examined six material claim groups per article, checked source grounding against the [MIT Distributed Systems course](https://pdos.csail.mit.edu/6.5840/), IETF RFCs 768/9293/1034/2606/3986/5737 and original published results on linearizability and asynchronous consensus, recomputed quantitative toy examples and directly fetched all unique relative Markdown file destinations.  
**Disposition:** **54 material claim groups reviewed; all nine references pass scoped model-assisted technical review** after the recorded source and conceptual corrections. This is not full standards conformance testing, exhaustive source verification, independent human peer review or final publication acceptance.

## Claim-to-source ledger

### Communication Models
[Reviewed article](communication-distributed-systems/communication-models.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| CM-01 | Communication identifies participants, messages, channels and interpretation contracts | [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.5840/); roles can be composed or distributed |
| CM-02 | Send, intermediate acceptance, receipt, interpretation and intended effect are different claims | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html); transport acknowledgment is not application completion |
| CM-03 | Messages, byte streams and datagrams have distinct boundaries and services | [RFC 9293 §3.7](https://www.rfc-editor.org/rfc/rfc9293.html#section-3.7) versus [RFC 768](https://www.rfc-editor.org/rfc/rfc768); no TCP write/read message-boundary guarantee |
| CM-04 | Client/server, pub/sub and peer-to-peer are nonexclusive exchange patterns | MIT 6.5840; examples are not a newly approved communication taxonomy |
| CM-05 | Toy acknowledgment observation from five update requests | Four acknowledged and one missing gives **4/5=80% observed acknowledgment receipt**; this is not measured effect-completion success or general delivery probability |
| CM-06 | Timeout and partial failure create uncertainty about remote operation | MIT 6.5840; no inference of failed execution merely from missing reply |

### Transmission and Signaling
[Reviewed article](communication-distributed-systems/transmission-and-signaling.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| TS-01 | Signaling maps abstract data to physical or modeled properties | [MIT 6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/); bit values not asserted to be literally binary voltage amplitudes |
| TS-02 | Symbol rate and raw bit rate can differ | MIT 6.003; depends on distinguishable symbols, encoding and overhead |
| TS-03 | Serialization, framing and coding are different mechanisms | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html) and Signals and Systems; framing does not establish authenticity |
| TS-04 | MiB and decimal raw Mbps model | `1 MiB=1,048,576 bytes=8,388,608 bits`; at exactly 8,000,000 bits/s, ideal serialization = **1.048576 s** |
| TS-05 | Raw signaling rate is not application goodput | Packet/frame overhead, delivery errors and processing may change time; no real link benchmark claimed |
| TS-06 | Transmission medium, direction and signal quality constrain interpretation | MIT 6.003; domain-neutral mechanism, not physical-layer certification |

### Communication Channels
[Reviewed article](communication-distributed-systems/communication-channels.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| CH-01 | Physical medium, logical channel and abstract stochastic channel differ | [MIT 6.003](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) and [Information Theory](information-data/information-theory.md); not one universal channel model |
| CH-02 | Path availability, capacity and current occupancy are different quantities | [MIT 6.5840](https://pdos.csail.mit.edu/6.5840/); a possible channel does not guarantee available application service |
| CH-03 | Noise, packet loss, delay and application failure have distinct causes | [RFC 768](https://www.rfc-editor.org/rfc/rfc768); no conflation of corruption and dropped messages |
| CH-04 | Toy propagation over 200,000 meters at 200,000,000 m/s | **0.001 s = 1 ms** one-way; symmetric request/response would incur at least **2 ms** propagation under stipulated medium/path |
| CH-05 | Discrete memoryless channel capacity uses maximized mutual information per use | General [Shannon Information Theory reference](information-data/information-theory.md); not claimed for unconstrained arbitrary channels |
| CH-06 | Bandwidth measured in hertz or signal rate is not necessarily net delivered bits/s | MIT Signals and Systems and Information Theory; assumptions about encoding/coding required |

### Protocols and Layering
[Reviewed article](communication-distributed-systems/protocols-and-layering.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| PR-01 | A protocol includes syntax, legal exchange behavior, state and error rules | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html); protocol name does not establish universal version compatibility |
| PR-02 | Layering and encapsulation distribute responsibilities without physical one-layer-one-device rules | TCP/UDP and general communication architecture; model caveat retained |
| PR-03 | Syntactically valid messages can be invalid in the current protocol state | RFC 9293 state machine; parser correctness is not conformance |
| PR-04 | Toy 1000-byte payload plus 40-byte protocol overhead | Total **1040 bytes**; modeled payload fraction **1000/1040≈96.1538%** under no retransmission/extra overhead assumptions |
| PR-05 | TCP provides a reliable ordered byte stream, not preserved application-write records | **Specific reference added:** [RFC 9293 §3.7](https://www.rfc-editor.org/rfc/rfc9293.html#section-3.7) explicitly distinguishes segments from application writes and reads |
| PR-06 | Transport acknowledgments and end-to-end application persistence remain separate | RFC 9293; selected layer properties do not guarantee data provenance or durable application action |

### Addressing and Naming
[Reviewed article](communication-distributed-systems/addressing-and-naming.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| AN-01 | Namespace, name, identifier, address and authority describe different roles | [RFC 1034 DNS Concepts](https://www.rfc-editor.org/rfc/rfc1034.html) and [RFC 3986 URI](https://www.rfc-editor.org/rfc/rfc3986.html); not equivalent identifiers |
| AN-02 | Resolution may change over time, return multiple values or be stale | RFC 1034; resolution result alone does not authenticate a resource |
| AN-03 | Toy `sensor.example` resolves to changing addresses | **Source improved:** [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606.html) reserves `.example`, while [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737.html) reserves `192.0.2.0/24`; no live service asserted |
| AN-04 | URI with scheme, authority, path, query and fragment parses under declared grammar | [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html); `https://example.com/measurements?id=7#top` parsed as stated |
| AN-05 | A fragment is not automatically a network transport destination | RFC 3986; parsing and resource identity/authentication remain separate |
| AN-06 | Endpoint address, application service identifier and object identity need not coincide | RFC 1034/3986; no universal port/identifier scheme imposed |

### Latency and Throughput
[Reviewed article](communication-distributed-systems/latency-and-throughput.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| LT-01 | Latency, raw signaling rate, bandwidth, throughput and goodput differ | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html) and MIT 6.5840; reference event boundaries and useful data scope required |
| LT-02 | Serialization, propagation, queueing and processing have different contributions | [MIT Distributed Systems](https://pdos.csail.mit.edu/6.5840/); simple additive model explicitly constrained |
| LT-03 | Five-million-byte payload at 10 Mb/s decimal | `5,000,000×8=40,000,000` bits; **4.0 s** ideal serialization |
| LT-04 | Additional 20 ms one-way propagation with no other delay | Last-bit arrival **4.020 s** after transmission begins, not application completion |
| LT-05 | Ideal 40 ms RTT and 10 Mb/s bandwidth-delay product | `10,000,000×0.040=400,000` bits = **50,000 bytes**; not necessarily actual in-flight data |
| LT-06 | Mean/tail delay and observed throughput require workload-specific measurement | Article correctly avoids inferred percentiles or an unmeasured real path |

### Reliability and Ordering
[Reviewed article](communication-distributed-systems/reliability-and-ordering.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| RO-01 | Loss, corruption, duplication, ordering and application effect are distinct outcomes | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html) and [RFC 768](https://www.rfc-editor.org/rfc/rfc768); delivery guarantees scoped to service layer |
| RO-02 | Missing ACK does not prove that the original request was not performed | MIT 6.5840; partial failure and ambiguous response considered |
| RO-03 | At-most-once versus at-least-once versus exactly-once **effects** have distinct guarantees | MIT Distributed Systems; article conditions progress, durable deduplication and atomic application effects |
| RO-04 | Increment example with retry after lost acknowledgment | No dedup: **0→10→20**; stipulated atomic durable dedup: **0→10→10** |
| RO-05 | Intersection of deduplication record/effect matters after crashes | Properly states that recording the ID after non-atomic effect can still duplicate after crash |
| RO-06 | Byte-stream order does not establish global ordering over independent channels | RFC 9293 and MIT 6.5840; sequence numbers and timestamps not conflated |

### Distributed State
[Reviewed article](communication-distributed-systems/distributed-state.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| DS-01 | Replicas may disagree temporarily under some consistency contracts | [MIT 6.5840](https://pdos.csail.mit.edu/6.5840/); disagreement alone neither proves a bug nor actual truth |
| DS-02 | Linearizability and eventual convergence are different promises | **Primary result added:** [Linearizability (1990)](https://doi.org/10.1145/78969.78972); operation boundaries and real-time constraints explicit |
| DS-03 | A read after a completed write cannot legally return a previous value under a linearizable single-object model without intervening writes | Original definition of linearizability; sufficiently qualified to stated history |
| DS-04 | Toy A=5/B=5; write A=6 with delayed propagation to B | Under a stale-read-permitting asynchronous model, B can read **5**; after convergence both read **6** under additional delivery/merge assumptions |
| DS-05 | Timeouts and network partitions create partial information about remote state | MIT 6.5840; no claim of a universally consistent and available service without defined conditions |
| DS-06 | Conflict resolution and version records depend on object invariants and causal assumptions | MIT 6.5840; counter merging not generalized to bank transfer/reservation correctness |

### Synchronization and Coordination
[Reviewed article](communication-distributed-systems/synchronization-and-coordination.md)

| ID | Material claim | Grounding and finding |
| --- | --- | --- |
| SY-01 | Local memory synchronization and inter-node agreement have different failure models | [MIT 6.5840](https://pdos.csail.mit.edu/6.5840/) and [Computational Synchronization](computation-algorithms/synchronization.md); distinct canonical ownership |
| SY-02 | Logical event ordering and synchronized wall clocks are distinct | [Time, Clocks and Ordering original paper](https://lamport.org/pubs/time-clocks.pdf); event causality need not entail a single global physical clock |
| SY-03 | Leaders, membership, agreement and validity must be specified as protocol contracts | MIT 6.5840; one successful vote does not prove consensus |
| SY-04 | Three voters with any two forming a quorum yield pairwise intersections | Quorums AB, AC, BC; **each pair intersects** in at least one voter, by pigeonhole/counting reasoning |
| SY-05 | Quorum intersection alone does not guarantee no conflicting commits | Correctly requires voter/round/persistence rules; a voter approving conflicting values could invalidate safety |
| SY-06 | Asynchronous consensus progress needs additional assumptions | **Corrected and sourced:** [MIT-LCS asynchronous-consensus impossibility report](https://dspace.mit.edu/entities/publication/287e7d14-a6f3-4ab4-b21a-a98ea86c1212); fully asynchronous crash-fault model forbids an unconditional deterministic termination guarantee, not safety or all probabilistic/partially synchronous progress |

## Corrections and source improvements

1. **Protocols and Layering:** Replaced generic TCP citation with [RFC 9293 §3.7](https://www.rfc-editor.org/rfc/rfc9293.html#section-3.7), explicitly grounding the absence of one-write/one-read application message boundaries.
2. **Addressing and Naming:** Clarified that `sensor.example` uses an RFC 2606 reserved example top-level domain and `192.0.2.10`/`192.0.2.20` are documentation-only TEST-NET-1 addresses under RFC 5737. Neither is represented as a real endpoint.
3. **Distributed State:** Added the original published linearizability result as grounding for the real-time ordering condition.
4. **Synchronization and Coordination:** Replaced imprecise asynchronous-consensus wording with a bounded deterministic termination impossibility statement for the standard fully asynchronous crash-fault model; added MIT technical-report grounding and a published logical-clock reference.
5. **No numerical changes** were required. All examples are invented mathematical or contractual scenarios, not real transport captures or measurements.

## Independent numerical checks

| Stipulated example | Recomputed result |
| --- | --- |
| 4 acknowledgments of 5 requests | 80% observed receipt, not confirmed action-completion rate |
| 1 MiB on ideal 8 Mb/s raw link | 8,388,608 bits; 1.048576 s serialization |
| 200,000 m at 200,000,000 m/s | 1 ms one-way propagation, 2 ms ideal two-way propagation |
| 1000 payload bytes with 40 overhead bytes | 1040 total; payload ratio ≈96.1538% |
| 5,000,000 bytes at 10 Mb/s | 4 seconds ideal serialization; +20 ms propagation = 4.020 seconds last-bit arrival |
| 10 Mb/s × ideal 40 ms RTT | 400,000 bits / 50,000 bytes bandwidth-delay product |
| Retry of nonidempotent +10 effect | No dedup 0→10→20; correct conditional dedup 0→10→10 |
| Two-of-three voter quorum | AB∩AC={A}; AB∩BC={B}; AC∩BC={C} |
| Asynchronously replicated value A=6, B still 5 | Stale read of 5 under permitted contract; not a linearizable read after a completed write of 6 |

## Internal file verification and audit limits

The nine articles contain **80 relative Markdown-link occurrences**, resolving to **28 distinct local file destinations**. All **28 distinct paths were fetched directly through GitHub** during the audit and were found on the default branch: **28/28**. The check excludes fragment-anchor validity, automated availability of every external URL, exhaustive semantic relevance of links and the entire corpus.

The primary sources were checked at material-claim-group level: MIT 6.5840, RFCs 9293/768/1034/3986/5737/2606, the original linearizability result and the asynchronous-consensus impossibility abstract. The full original papers, every standards clause and every reference passage were **not exhaustively inspected**. Mathematical examples were recomputed, but these are not empirical performance or availability measurements.

The state **Reviewed (model-assisted)** / **Core claims checked** is appropriate for this bounded audit. It is not the stronger `Verified` source-review state, independent human peer review, standards conformance certification or final `Published` approval.

## Architecture and acceptance disposition

- All nine Communication & Distributed Systems subjects pass scoped model-assisted review, maintaining separate canonical ownership of communication roles, transmission, channels, protocols, naming, performance, delivery/ordering, replicated state and cross-node coordination.
- Along with ten audited OS subjects and the prior 90 Wave A–D subjects, the **109-heading Fundamentals corpus is now 109/109 authored and 109/109 internally Reviewed (model-assisted)**.
- The twelve approved knowledge areas and exactly 109 approved headings remain unchanged. G-01 mathematics breadth, G-04 general temporality and G-06 AI/ML are unresolved.
- No Knowledge Checks, Practical Assessments, new heading families, mandatory network protocols or vendor products were introduced.
- **Independent human expert review, complete claim-to-source verification, corpus-wide link/anchor integrity, editorial depth and seven publication completion gates remain outstanding.**

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
