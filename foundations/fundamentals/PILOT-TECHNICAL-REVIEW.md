# Fundamentals: Six-Pilot Technical and Editorial Review

**Review edition:** v0.1 (historical second-pass review; superseded for current status by [50-Claim-Family Acceptance Audit](PILOT-CLAIM-SOURCE-AUDIT.md))  
**Review scope:** Six substantive pilot references approved in the [Curriculum Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md)  
**Status at v0.1:** Second-pass technical/editorial source check completed. At the time these articles were drafts. The later [scoped audit](PILOT-CLAIM-SOURCE-AUDIT.md) supports their current **Reviewed (model-assisted)** state; independent human peer-review and complete corpus validation remain outstanding.  
**Approved baseline preserved:** 12 knowledge areas, 109 subject headings.  
**Excluded:** Knowledge Checks, Practical Assessments, quizzes, graded exercises.

## Purpose and standards

This review examines the **actual GitHub article content** against source material and the [governing Fundamentals architecture](ARCHITECTURE.md). It does not replace direct source verification with an author's confidence, and it does not treat the appearance of a reference list as comprehensive verification.

The six editorial gates for every canonical entry remain: **definition and scope, distinctions, mechanisms, relationships, explanatory examples, references**. The seven wider Fundamentals completion gates are separate. A pass at this six-article calibration stage **does not** mean Fundamentals is complete.

## Review method

1. Reopened the six committed Markdown documents rather than using only older summaries.
2. Compared core technical claims with primary or authoritative sources: MIT OpenCourseWare, Unicode Consortium, RFC Editor, W3C RDF specifications, NIST, NASA's HTML Systems Engineering Handbook, SEBoK, and the Stanford Encyclopedia of Philosophy.
3. Programmatically checked illustrative set equality, binary gate and half-adder truth tables, UTF-8 examples, and Unicode normalization.
4. Inspected internal Markdown references and resolved the distinct relative destinations through GitHub.
5. Corrected substantiated errors, misleading word choices, and stale or inaccessible cited documents.
6. Preserved canonical subject scope, existing filenames, and all approved area identities.

**Limitations:** This is a model-assisted second-pass review, **not a separate human expert sign-off**. Source pages were inspected for the supported claims and topics, but external sources were not subjected to a full scholarly peer review; not every statement can be elevated to a universal formal theorem. Selected MIT course landing pages describe lecture coverage; an uninspected lecture PDF is **not** being represented as individually audited.

## Article-level findings and corrections

| Article | Checked concepts and examples | Corrections recorded | Current editorial outcome |
| --- | --- | --- | --- |
| [Sets and Relations](mathematics-logic/sets-and-relations.md) | Extensional sets, membership, subset, binary relations, reflexive/symmetric/antisymmetric/transitive properties, functions, partial order | Added an explicit antisymmetry contrast; mathematically checked set equality and ordered-pair example | **Source-checked draft** |
| [Observation](scientific-analytical-reasoning/observation.md) | Observation vs measurement vs record vs evidence, sampling limitations, evidence interpretation | Clarified secondary observation of a record and corrected the false implication that a sample above a threshold establishes the occurrence or time of a threshold crossing | **Source-checked draft** |
| [Entities and Attributes](models-abstraction/entities-and-attributes.md) | General model entities, attributes, types, identifiers, state, RDF graph representation | Specified the permitted RDF 1.1 subject, predicate, and object categories while retaining RDF as an illustrative implementation rather than a universal ontology | **Source-checked draft** |
| [Symbols and Encoding](information-data/symbols-and-encoding.md) | Code points vs scalar values vs glyphs, UTF-8 mapping, normalization, serialization vs meaning | Clarified that not every code point is an assigned character; that UTF-8 encodes Unicode scalar values; and added Unicode normalization annex as a direct source | **Source-checked draft** |
| [Systems and Subsystems](systems-engineering/systems-and-subsystems.md) | System vs subsystem, boundaries, composition, function, behavior, systems-of-systems independence | Replaced an obsolete NASA procedural requirement citation and older software-handbook reference with NASA's accessible Systems Engineering Handbook and SEBoK; added direct SoS independence reference | **Source-checked draft** |
| [Digital Logic](digital-systems-hardware/digital-logic.md) | Boolean vs electronic logic, combinational/sequential behavior, gate truth tables, half-adder, clocking and metastability | Clarified the meaning of Boolean expression and added a focused MIT synchronization/metastability reference; truth tables checked for all four binary input pairs | **Source-checked draft** |

### Examples audited computationally

**Sets:** `{2,4,6} = {6,2,4,2}` after mathematical set interpretation; the 2×2 Cartesian-product example contains four ordered pairs.

**UTF-8:** `A` → `41`; `é` (`U+00E9`) → `C3 A9`; `€` (`U+20AC`) → `E2 82 AC`; `e` + combining acute (`U+0065 U+0301`) → `65 CC 81`. NFC of both forms of `é` yields the precomposed form.

**Logic:** For `(A,B) = (0,0),(0,1),(1,0),(1,1)`, gate outputs were recomputed for AND, OR, XOR and NAND. Half-adder `sum = A XOR B`, `carry = A AND B` passed all four cases.

These computational checks substantiate **the example values**. They do not validate every broader interpretive or engineering assertion.

## Source quality and claim-to-source audit

| Knowledge area | Principal source(s) checked | What they support | Limits |
| --- | --- | --- | --- |
| Mathematics & Logic | [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/resources/lecture-notes/); [Open Logic Project](https://slc.openlogicproject.org/) | Formal mathematics, relations, proof and sets as curriculum subjects | The lecture listing and source index were checked; not every lecture PDF was separately analyzed |
| Scientific Reasoning | [Stanford Encyclopedia: Theory and Observation](https://plato.stanford.edu/entries/science-theory-observation/); [Evidence](https://plato.stanford.edu/entries/evidence/); [NIST Measurement Uncertainty](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) | Theory-laden observations, epistemic evidence, quantitative measurement and calibration | The article's seven-part observation anatomy remains an **editorial construct**, not an external standardized schema |
| Models & Abstraction | [W3C RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/); [RDF Primer](https://www.w3.org/TR/rdf11-primer/) | RDF triples and the role of resources and properties | RDF is a concrete graph representation, not a universal definition of entities or attributes |
| Information & Data | [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629); [Unicode Technical Introduction](https://www.unicode.org/standard/principles.html); [UAX #15](https://www.unicode.org/reports/tr15/) | UTF-8 encoding, Unicode representation and normalization | A current-version landing page and technical annex may evolve; cite particular standard versions when a claim depends on version-specific behavior |
| Systems Engineering | [NASA Systems Engineering Handbook, Fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/); [NASA Handbook appendix](https://www.nasa.gov/reference/system-engineering-handbook-appendix/); [SEBoK Systems of Systems](https://sebokwiki.org/wiki/Systems_of_Systems_%28SoS%29) | Whole-system functions and relationships, system definitions, operational and managerial SoS independence | NASA requirements revision 7123.1B was explicitly marked obsolete and has been removed as a principal reference |
| Digital Hardware | [MIT Computation Structures lecture index](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/); [MIT Synchronization & Metastability](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/resources/mit6_004s09_lec07/) | Digital abstraction, combinational/sequential logic, timing, and metastability as distinct hardware concepts | Electrical behavior is technology-dependent; no ungrounded universal voltage or timing values are asserted |

## Cross-article architectural consistency

- **Formal concept vs implementation:** Mathematical logic is not the same as electronic gates or software condition evaluation.
- **Entity vs identifier:** A symbolic identifier does not define all identity criteria for its referent.
- **Observation vs evidence:** A reading or record does not prove an interpretation of the cause or event history.
- **System vs component:** Components participate in system-level functions through interactions, not just physical containment.
- **Symbol vs meaning:** Encoded bytes do not determine semantic meaning without an interpretation.
- **Relationships:** These articles link to existing approved area indexes or real draft canonical pages. The repository navigation is not being presented as a formal knowledge-graph ontology.

## Remaining review and publication decisions

**Pilot review disposition:** All six articles have undergone a second-pass source check and received corrections. They remain **Draft**, because a separate final editorial/acceptance gate has not been recorded and the broader source-to-claim audit may be strengthened where more precision is required.

For progress tracking, use **Core claims checked** as an intermediate source-review state, distinct from **Verified**. The latter is reserved for a complete, documented claim-to-source check and final technical acceptance. Do not silently promote a draft to *Published* because this review report exists.

**Open global architecture questions:** G-01 mathematical breadth, G-04 general temporality, and G-06 AI/ML remain unresolved. None requires rewriting these six pilot definitions before the scope decision, but future material should link to the decisions when applicable.

**Next production gate:** Conduct the final human/editorial acceptance of the six source-checked drafts, then apply the calibrated standard to remaining subjects in development waves A–E. The six-part editorial contract and seven-completion-gate architecture remain unchanged.

## Follow-up tracking

- [Development & Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md)
- [Fundamentals Index](README.md)
- [Curriculum Development Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
- [Canonical Ownership Register](CANONICAL-OWNERSHIP-REGISTER.md)
- [Concept Boundary Decisions](CONCEPT-BOUNDARY-DECISIONS.md)

**Review completed for six pilots; Fundamentals as a whole remains incomplete.**
