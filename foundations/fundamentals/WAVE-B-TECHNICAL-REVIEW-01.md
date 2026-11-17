# Wave B Technical Review: Batch 01

**Review date:** November 17, 2026  
**Scope:** Bits and Bytes; Information Theory; Data Types; Datasets, Records, Fields, and Values.  
**Method:** Re-read the four GitHub drafts, verify material claim groups against NIST, IETF, W3C, Cambridge and MIT source material, independently recompute numerical examples, inspect semantic boundaries, and fetch all distinct relative Markdown **file destinations** in the four articles.  
**Disposition:** **24 material claim groups reviewed** across four articles. The four references pass a **scoped model-assisted technical review** after the corrections described below. No independent human peer review, complete claim-by-claim source attestation, fragment/external-link certification, or publication acceptance is claimed.

## Claim-to-source ledger

### Bits and Bytes
[Reviewed article](information-data/bits-and-bytes.md)

| ID | Material claim group | Grounding and disposition |
| --- | --- | --- |
| BB-01 | Bit is binary digit; standard byte is eight bits | [NIST bit glossary](https://csrc.nist.gov/glossary/term/bit), [NIST byte glossary](https://csrc.nist.gov/glossary/term/byte); accepted under the stated modern standardized usage |
| BB-02 | Binary positional arithmetic and possible bit patterns | Independently checked `00101101₂=45` and `2^8=256`; **corrected** to say freely selectable binary positions, not necessarily probabilistically independent random values |
| BB-03 | Endianness orders bytes in a multi-byte representation | `12 34` interpreted as `0x1234=4660` versus `0x3412=13330`; byte order does not by itself specify sign, type or bit transmission order |
| BB-04 | Decimal prefixes and binary prefixes denote different powers | [NIST binary prefixes](https://physics.nist.gov/cuu/Units/binary.html); `1 kB=1000 B`, `1 KiB=1024 B` under their respective conventions |
| BB-05 | Bit rate differs from byte rate and end-to-end throughput | `8 Mb/s = 1 MB/s` as pure unit arithmetic with decimal prefixes and eight-bit bytes; protocol overhead and measurement boundary explicitly excluded |
| BB-06 | Representation width differs from Shannon entropy | Eight-bit field permits 256 patterns; constant source has 0 entropy, uniform source has 8 bits under a specified probabilistic model; cross-checked against the foundational information-theory model |

### Information Theory
[Reviewed article](information-data/information-theory.md)

| ID | Material claim group | Grounding and disposition |
| --- | --- | --- |
| IT-01 | Shannon entropy describes modeled distribution uncertainty, not semantic truth | [Cambridge Information Theory and Coding](https://www.cl.cam.ac.uk/teaching/1314/InfoTheory/); statement is correctly qualified |
| IT-02 | Self-information and entropy formulas and bit units | `I(x)=-log₂p(x)`; `H(X)=-Σp(x)log₂p(x)`, with `0 log 0=0` convention; accepted for discrete distributions |
| IT-03 | Entropy bound and example probabilities | `0≤H(X)≤log₂ m` for finite alphabet of size `m≥1`; verified `H(Bernoulli(1/4))=0.8112781245` bits, plus 0/1-bit endpoint examples |
| IT-04 | Mutual information and independence for discrete models | `I(X;Y)=H(X)-H(X\|Y)`, nonnegative and zero iff independence for well-defined discrete distributions; copying a fair bit gives 1 bit, independent fresh fair bit gives 0 |
| IT-05 | Channel capacity and coding-limit interpretation | **Corrected:** `C=maxₚ I(X;Y)` is the single-letter formula for a stated discrete memoryless channel; general channels with memory or feedback need appropriately defined capacity and rate conditions; [Cambridge course](https://www.cl.cam.ac.uk/teaching/1314/InfoTheory/) |
| IT-06 | Source coding, channel coding and evidence are separate concepts | [MIT Information Theory course](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/pages/lecture-notes/); source distribution entropy does not itself validate observations or claims |

### Data Types
[Reviewed article](information-data/data-types.md)

| ID | Material claim group | Grounding and disposition |
| --- | --- | --- |
| DT-01 | Type, value, and representation are distinct | Conceptual data-model distinction; example string `"45"` versus numeric `45` does not imply identical operations |
| DT-02 | Type systems vary by language and implementation | Fixed-width integers may have bounded ranges; mathematics' integers are not inherently fixed-width; treated as illustrative, not a universal machine hierarchy |
| DT-03 | JSON number syntax and numeric interoperability | [RFC 8259 §6](https://www.rfc-editor.org/rfc/rfc8259#section-6); syntax does not mandate arbitrary precision or an intrinsic date type |
| DT-04 | Measurement level differs from software data type | Nominal/ordinal/interval/ratio distinctions describe justified comparisons, not a mandatory programming-language taxonomy |
| DT-05 | Type checking, coercion, schema validation and real-world correctness differ | String-to-number coercion requires declared rules; valid numeric representation does not imply a correctly measured physical quantity |
| DT-06 | Nominal identifier and quantitative sample are not interchangeable | `"0007"` can preserve meaningful leading zeroes; numeric mean of identifiers has no supported interpretation without different domain assumptions |

### Datasets, Records, Fields, and Values
[Reviewed article](information-data/datasets-records-fields-and-values.md)

| ID | Material claim group | Grounding and disposition |
| --- | --- | --- |
| DR-01 | Dataset/record/field/value distinguish scope and grain | Original general decomposition; record grain is an explicit modeling decision, not a requirement for all datasets to be tables |
| DR-02 | Observation-grain versus device-grain aggregation | Recomputed `(21+22+19)/3=20.666…` °C (record-weighted) and `((21+22)/2+19)/2=20.25` °C (equal weight per identifier group) |
| DR-03 | Keys, identifiers and physical identity differ | **Corrected:** counting distinct `device_id` values gives two **identifiers**; by itself it does not prove two unique real devices |
| DR-04 | Null, absent field, empty string and zero have different potential semantics | [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) exemplifies explicit JSON null versus number 0; application semantics require further definition |
| DR-05 | Selection, grouping, aggregation and join may change cardinality or grain | Under a declared relationship, joins can multiply rows; explanatory, not a theorem asserting that every join must increase count |
| DR-06 | Record need not equal event; RDF dataset need not be tabular | [W3C RDF 1.1 Concepts §4](https://www.w3.org/TR/rdf11-concepts/#section-dataset); RDF graph is a set of triples; RDF dataset includes a default graph and possibly named graphs |

## Corrections applied before acceptance

1. **Bits and Bytes:** Replaced `n independent binary positions` with **n freely selectable positions**, separating the combinatorial count of possible bit patterns from probabilistic independence.
2. **Information Theory:** Scoped the common mutual-information capacity expression to a **discrete memoryless channel**. General channel models can require information-rate limits and additional constraints.
3. **Datasets, Records, Fields, and Values:** Clarified that two distinct `device_id` values establish two distinct **recorded identifiers**, not independently verified physical device identities.

**Data Types** required no technical correction in this scope. The generic type taxonomy remains illustrative rather than a formal repository-wide type system.

## Independently recomputed examples

| Calculation | Verified result |
| --- | --- |
| `00101101₂` interpreted unsigned | 45 |
| Eight freely selectable binary positions | 256 patterns |
| Two-byte big-endian `12 34` | 4660 |
| Two-byte little-endian `12 34` | 13330 |
| `8 Mb/s` to decimal megabytes/s, without overhead | 1 MB/s |
| `H(Bernoulli(1/4))` | 0.8112781245 bits/symbol |
| `I(X;X)` for fair binary X | 1 bit |
| `I(X;Y)` for independent fair bits | 0 bit |
| Mean of 21, 22, 19 across three observation records | 20.6666667 °C |
| Mean of grouped values (21.5 for D7; 19 for D8) | 20.25 °C |
| Distinct identifiers among D7,D7,D8 | 2, not proof of two physical devices |

The examples are stipulated toy models, not measured empirical results or estimates of any deployed system.

## Internal links and source limitations

The four articles contain **39 relative Markdown link occurrences** resolving to **20 distinct relative file destinations** within Fundamentals. Each of these 20 file destinations was reopened through GitHub; **20/20 resolved**. This check does **not** exhaustively validate anchor fragments, external web URLs, documentation on other branches, or all links across the repository.

Authoritative sources were checked at the **material claim-family** level. The full Shannon paper linked within the article is provided as historical source context; the technical review instead relied on HTML course descriptions and source-defined concepts, not a page-by-page analysis of the PDF. The review does not claim a full formal proof or validation of software implementations.

## Governing boundaries and disposition

- **Bits and Bytes** owns binary units and representation; **Information Theory** owns entropy and channel limits; **Data Types** owns type interpretation; **Datasets/Records/Fields/Values** owns information granularity.
- **Schemas**, **Classification**, **Probability and Statistics**, **Measurement**, and **Evidence** keep distinct canonical ownership.
- All four articles now qualify as **Reviewed (model-assisted)** with **Core claims checked** as their source-review state. **Verified**, independent human review, and **Published** remain unclaimed.
- 12 knowledge areas, 109 approved headings, and G-01/G-04/G-06 pending decisions remain unchanged. No assessments or new subject categories were introduced.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
