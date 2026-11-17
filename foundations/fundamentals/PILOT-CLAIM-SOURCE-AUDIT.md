# Fundamentals: Pilot Claim-to-Source Acceptance Audit

**Status:** Internal model-assisted editorial and technical verification record, v0.2 (2026-11-17)  
**Scope:** Six pilot reference drafts, fifty material claim groups.  
**Outcome:** Pass for **model-assisted technical/editorial calibration**. External human peer-review and final publication acceptance **have not** occurred.  
**Baseline:** Twelve approved areas, 109 subject headings, no knowledge checks or practical assessments.

## Audit methodology

Reopened the six live GitHub files; compared the material claim families below with their cited normative, academic or government sources; recalculated all mathematical, UTF-8 and logic examples; checked their canonical-ownership distinctions; and reviewed relative links. An **editorial illustration** is evaluated for conceptual soundness and disclosed as such, rather than falsely attributed to a standard. This is a **scoped** audit of material claim families, not a legal guarantee of correctness or independent human expert certification.

**Verified examples:** (a) `{2,4,6}` equals `{6,2,4,2}` in set theory; (b) 2×2 Cartesian product contains four pairs; (c) UTF-8 `A: 41`, `é: C3 A9`, `€: E2 82 AC`, decomposed `e + ◌́: 65 CC 81`, with NFC equality; (d) four AND/OR/XOR/NAND rows and all four half-adder cases. These were recalculated with independent Python operations.

## Source-linked material claim groups

### Sets and Relations

[Current pilot reference](mathematics-logic/sets-and-relations.md)

| ID | Material claim group | Source evidence | Result / qualification |
| --- | --- | --- | --- |
| S-01 | Extensional set membership, duplicate and order invariance | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions) | Set example calculated |
| S-02 | Empty sets, subsets, union/intersection/difference/power set | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions) | Conventional definitions supported |
| S-03 | Cartesian product and ordered pair count | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions) | 2×2=4 checked |
| S-04 | Binary relation as subset A×B | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions) | Direct definition |
| S-05 | Reflexivity, symmetry, antisymmetry, transitivity | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions), [W](https://mathworld.wolfram.com/PartialOrder.html) | Scope and antisymmetry checked |
| S-06 | Partial orders vs equivalence relations | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions), [W](https://mathworld.wolfram.com/PartialOrder.html) | Correct criteria, incomparable subsets |
| S-07 | Functions as single-valued total relations | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions) | Function coverage supported |
| S-08 | Graph representation vs semantic interpretation | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions) | Illustration explicitly distinguished |

### Observation

[Current pilot reference](scientific-analytical-reasoning/observation.md)

| ID | Material claim group | Source evidence | Result / qualification |
| --- | --- | --- | --- |
| O-01 | Observation reports mediated by concepts and instruments | [O](https://plato.stanford.edu/entries/science-theory-observation/) | Source explains observational limitations |
| O-02 | Direct observation vs observing a previous record | [O](https://plato.stanford.edu/entries/science-theory-observation/) | Interpretive distinction explicit |
| O-03 | Seven-facet observation anatomy | Editorial example / logical consequence | Original explanatory model, not a standard |
| O-04 | Measurement process, measurand and uncertainty | [N](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) | NIST supports |
| O-05 | Record distinct from claim-relative evidence | [E](https://plato.stanford.edu/entries/evidence/), [O](https://plato.stanford.edu/entries/science-theory-observation/) | Epistemic scope made explicit |
| O-06 | Periodic sampling misses unrecorded events | [N](https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty) | Logical conditional example |
| O-07 | Reading above threshold does not prove crossing time | Editorial example / logical consequence | Counterexample verified |
| O-08 | Observer selection and theory dependence | [O](https://plato.stanford.edu/entries/science-theory-observation/) | SEP directly addresses |

### Entities and Attributes

[Current pilot reference](models-abstraction/entities-and-attributes.md)

| ID | Material claim group | Source evidence | Result / qualification |
| --- | --- | --- | --- |
| E-01 | Entities/attributes are model-scoped notions | [R](https://www.w3.org/TR/rdf11-concepts/), [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | Editorial abstraction, not universal ontology |
| E-02 | Type vs instance and property vs value | [P](https://www.w3.org/TR/rdf11-primer/) | Illustrative heater model |
| E-03 | Attributes can be functions varying over time | [M](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions) | Assumptions specified |
| E-04 | State/event/transition concept distinction | [T](https://computationstructures.org/lectures/fsm/fsm.html) | Conceptual modeling supported |
| E-05 | Identity vs identifier string | [R](https://www.w3.org/TR/rdf11-concepts/) | Referent vs IRI distinction |
| E-06 | Attribute/property vs inter-entity relation | [R](https://www.w3.org/TR/rdf11-concepts/) | RDF supports both as predicates |
| E-07 | RDF 1.1 subject/predicate/object allowed categories | [R](https://www.w3.org/TR/rdf11-concepts/) | Normative syntax matched |
| E-08 | Model boundary vs state change | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | Engineering modeling perspective |

### Symbols and Encoding

[Current pilot reference](information-data/symbols-and-encoding.md)

| ID | Material claim group | Source evidence | Result / qualification |
| --- | --- | --- | --- |
| S-01 | Encoding convention distinct from interpretation | [U](https://www.unicode.org/standard/principles.html), [F](https://www.rfc-editor.org/rfc/rfc3629) | Representation/meaning separated |
| S-02 | Code points and scalar values; surrogates excluded | [F](https://www.rfc-editor.org/rfc/rfc3629), [U](https://www.unicode.org/standard/principles.html) | Verified with Unicode/RFC |
| S-03 | UTF-8 one to four bytes, ASCII compatibility | [F](https://www.rfc-editor.org/rfc/rfc3629) | RFC encoding ranges |
| S-04 | A, é, € byte values | [F](https://www.rfc-editor.org/rfc/rfc3629) | Python UTF-8 values match |
| S-05 | Composed vs decomposed é canonical equivalence | [Z](https://www.unicode.org/reports/tr15/) | Python NFC match |
| S-06 | Code point vs grapheme cluster | [G](https://www.unicode.org/reports/tr29/) | Normative segmentation annex |
| S-07 | JSON unicode escaping vs byte encoding | [J](https://www.rfc-editor.org/rfc/rfc8259) | JSON syntax checked |
| S-08 | Malformed UTF-8 vs decoder policy | [F](https://www.rfc-editor.org/rfc/rfc3629) | RFC validation, no false guarantees |

### Systems and Subsystems

[Current pilot reference](systems-engineering/systems-and-subsystems.md)

| ID | Material claim group | Source evidence | Result / qualification |
| --- | --- | --- | --- |
| S-01 | System as cooperating whole with required capability | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | NASA direct definition |
| S-02 | Elements include hardware, software, people and process | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | NASA direct definition |
| S-03 | Boundary and system of interest depend on inquiry | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | Illustrative context qualified |
| S-04 | Subsystem relative to larger chosen system | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | Systems perspective |
| S-05 | Components, interfaces, function and behavior | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | Related but distinct views |
| S-06 | Functional vs physical decomposition | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | Different view purposes |
| S-07 | Emergent/dependency outcomes exceed isolated component inventory | [A](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/), [S](https://sebokwiki.org/wiki/Systems_of_Systems_%28SoS%29) | NASA and SEBoK support |
| S-08 | System of systems constituent managerial/operational independence | [S](https://sebokwiki.org/wiki/Systems_of_Systems_%28SoS%29) | Explicit SoS distinction |
| S-09 | Building example illustrates boundaries; not prescriptive | Editorial example / logical consequence | Original illustrative model |

### Digital Logic

[Current pilot reference](digital-systems-hardware/digital-logic.md)

| ID | Material claim group | Source evidence | Result / qualification |
| --- | --- | --- | --- |
| D-01 | Formal Boolean truth vs electrical signal realization | [C](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/), [D](https://computationstructures.org/notes/sequential_logic/notes.html) | MIT digital abstraction |
| D-02 | Binary signal ranges not fixed universal 0/1 V | [C](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/) | Technology-relative physical representation |
| D-03 | Combinational logic vs stateful sequential circuits | [D](https://computationstructures.org/notes/sequential_logic/notes.html) | Direct MIT note |
| D-04 | AND, OR, XOR, NAND tables and functional completeness | [C](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/) | Truth tables recomputed |
| D-05 | Half adder sum XOR, carry AND | [C](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/) | 4 combinations recomputed |
| D-06 | Latch vs edge-triggered flip-flop | [D](https://computationstructures.org/notes/sequential_logic/notes.html) | Direct text describes distinction |
| D-07 | Finite-state machine current/next state functions | [T](https://computationstructures.org/lectures/fsm/fsm.html) | MIT finite state lecture |
| D-08 | Setup/hold, propagation and metastability | [D](https://computationstructures.org/notes/sequential_logic/notes.html), [T](https://computationstructures.org/lectures/fsm/fsm.html) | Physical timing supported |
| D-09 | Clock rate not equal to useful throughput | [C](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/lecture-notes/) | Architecture/performance qualification |

## Source quality and reviewed boundaries

**Normative references:** [RDF 1.1 Concepts](https://www.w3.org/TR/rdf11-concepts/), [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629), [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259), Unicode [UAX #15](https://www.unicode.org/reports/tr15/) and [UAX #29](https://www.unicode.org/reports/tr29/). These support narrowly specified data-model, encoding, JSON and normalization claims.

**Primary educational/engineering sources:** [MIT Computation Structures](https://computationstructures.org/notes/sequential_logic/notes.html), [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/), [SEBoK Systems of Systems](https://sebokwiki.org/wiki/Systems_of_Systems_%28SoS%29), [Mathematics LibreTexts](https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_%28Schilling_Nachtergaele_and_Lankham%29/13%3A_Appendices/13.01%3A_The_Language_of_Sets_and_Functions), and [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/science-theory-observation/). These support the corresponding conceptual and engineering explanations; they do **not** prescribe this repository's twelve-area taxonomy.

**Editorial constructs:** Seven-facet observation anatomy, heater/building illustrations, and canonical ownership routing are author-designed explanatory choices, not source-defined scientific standards. Uncertainty about general temporality and AI/ML placement remains open in the [coverage gap register](COVERAGE-GAP-DECISIONS.md).

## Corrections carried forward from prior technical review

- A single above-threshold sample was previously conflated with evidence of crossing; this was corrected.
- A stale NASA requirements reference was replaced with the current accessible systems-engineering handbook.
- Unicode scalar values, code points, and grapheme clusters were distinguished and better sourced.
- RDF node constraints, formal antisymmetry, Boolean vs electronic logic, and sequential timing were clarified.
- All revised references preserve the approved subject inventory and cross-domain canonical ownership model.

## Disposition and next gate

**Claim-family audit:** 50 / 50 examined, with source pointers or explicit editorial classification. No remaining *identified* material contradiction prevents using the six articles as the **reviewed authoring baseline**.

**Development status:** Each pilot may advance from **Draft** to **Reviewed (model-assisted)**, with its review evidence linked here. This is not a claim of independent human endorsement.

**Source-review status:** Retain **Core claims checked** in the tracking register rather than claim fully independent expert verification. The facts have been reviewed within this scoped audit but a separate human technical approval remains unavailable.

**Publication status:** Do not label the six pilots a final externally validated or peer-reviewed release. Broader Fundamentals still has 103 approved headings without canonical articles and three unresolved architectural scope decisions (G-01, G-04, G-06).

**Next work:** Expand Wave A using this accepted internal writing-and-review standard. New articles start as drafts and must undergo a similar source/links review.

[Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Previous Pilot Review](PILOT-TECHNICAL-REVIEW.md) · [Fundamentals](README.md)
