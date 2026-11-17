# Wave A Technical Review: Batch 07

**Review date:** November 17, 2026  
**Scope:** Units and Quantities; Validation and Falsification; Ontologies and Taxonomies; Schemas; Conceptual and Formal Models.  
**Method:** Reopen committed draft articles; check material claim families against authoritative SI, NIST, NASEM, NASA, W3C, JSON Schema and philosophy-of-science references; recompute worked examples; review modeling semantics; fetch and verify the distinct relative-link file targets used by the five articles.  
**Disposition:** **30 material claim groups reviewed** across five articles. Each passes a **scoped model-assisted technical review** with documented qualifications. This is **not** exhaustive source-level certification, independent human peer review, or final publication acceptance.

## Claim-to-source review ledger

### Units and Quantities

[Reviewed article](mathematics-logic/units-and-quantities.md)

| ID | Material claim group | Evidence and finding |
| --- | --- | --- |
| UQ-01 | Quantity, value, reference, unit and kind distinguished | [JCGM VIM](https://jcgm.bipm.org/vim/en/); definition is compatible with metrological vocabulary |
| UQ-02 | Physical dimensions and quantity kinds are not synonymous | [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure); torque versus energy share dimension but differ in kind |
| UQ-03 | Base SI units, derived units and decimal prefixes | BIPM SI Brochure; seven SI base units and `N = kg·m·s⁻²` checked |
| UQ-04 | Decimal and binary prefix semantics | [NIST binary prefixes](https://physics.nist.gov/cuu/Units/binary.html); `1 kB=1000 B` versus `1 KiB=1024 B` checked in defined notation |
| UQ-05 | Unit conversion including affine Celsius/Kelvin relation | BIPM SI Brochure; `2.5 km=2500 m`, `72 km/h=20 m/s`, `20 °C=293.15 K`; temperature difference `20 °C=20 K` in interval magnitude, not absolute temperature |
| UQ-06 | Dimensional consistency is necessary but insufficient for truth | Dimensional identities checked; model correctness cannot follow from dimensional consistency alone |

### Validation and Falsification

[Reviewed article](scientific-analytical-reasoning/validation-and-falsification.md)

| ID | Material claim group | Evidence and finding |
| --- | --- | --- |
| VF-01 | Empirical validation supports claims conditionally | [SEP Scientific Method](https://plato.stanford.edu/entries/scientific-method/); distinguishes evidence evaluation from certainty |
| VF-02 | Falsifiability, contrary predictions and auxiliary assumptions | [SEP Popper](https://plato.stanford.edu/entries/popper/); counterexamples require credible observational premises |
| VF-03 | Experimental claims, predictions and rival explanations | SEP Scientific Method; article appropriately qualifies test design and underdetermination |
| VF-04 | Engineering verification versus validation | [NASA Systems Engineering](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/); conformance to requirements differs from fitness for intended purpose |
| VF-05 | Reproducibility versus replicability | [National Academies](https://www.nationalacademies.org/read/25303/chapter/3); report-specific computational versus independent-study senses correctly identified |
| VF-06 | Statistical p-value semantics and universal test example | [ASA statement](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf); null-model conditional interpretation correct. Ten compliant observations alone do not prove a nonexhaustively sampled universal; a verified counterinstance can refute it under defined conditions |

### Ontologies and Taxonomies

[Reviewed article](models-abstraction/ontologies-and-taxonomies.md)

| ID | Material claim group | Evidence and finding |
| --- | --- | --- |
| OT-01 | Taxonomy, ontology and classification have distinct roles | [W3C SKOS](https://www.w3.org/TR/skos-reference/) and [OWL 2](https://www.w3.org/TR/owl2-overview/); distinctions are conceptual, not new repository category definitions |
| OT-02 | Concepts, classes, labels and instances are not interchangeable | SKOS and OWL 2; term labels do not directly establish real-world identity |
| OT-03 | Broader concept, subclass, part-of and membership differ | SKOS and OWL 2; wheel-part-of-bicycle does not mean subclass-of |
| OT-04 | Direct broader relation versus transitive closure | SKOS §8.6.6; **correction committed**: `skos:broader` is not declared transitive; `skos:broaderTransitive` captures transitive broader ancestry |
| OT-05 | OWL entailment and open-world semantics | OWL 2; non-asserted statements need not be false. Real-world accuracy not guaranteed by entailment |
| OT-06 | Navigational structures, graphs and formal semantics | SKOS/OWL; an edge symbol alone cannot determine its logical relation; no mandatory repository ontology implied |

### Schemas

[Reviewed article](models-abstraction/schemas.md)

| ID | Material claim group | Evidence and finding |
| --- | --- | --- |
| SC-01 | Schema describes representation constraints, not factual truth | [JSON Schema](https://json-schema.org/specification); conforms under specified dialect, not automatically to physical reality |
| SC-02 | Types, ranges, required fields and relationships are separate constraint forms | JSON Schema and [SHACL](https://www.w3.org/TR/shacl/); languages need not share all constraints |
| SC-03 | Illustrative three-field device record | Manual evaluation: numeric 20.5 accepted, string `"warm"` rejected by numeric requirement |
| SC-04 | JSON Schema draft 2020-12 worked example | [JSON Schema object reference](https://json-schema.org/understanding-json-schema/reference/object); `required` requires keys; `additionalProperties:false` disallows unspecified keys; `enum` restricts state |
| SC-05 | RDF graph validation versus OWL reasoning | W3C SHACL and OWL 2; shape conformance is not logical entailment or truth attestation |
| SC-06 | Schema evolution, semantic versus syntactic compatibility | Editorial explanatory distinctions, not a universal compatibility theorem; consumer behavior and versioning matter |

### Conceptual and Formal Models

[Reviewed article](models-abstraction/conceptual-and-formal-models.md)

| ID | Material claim group | Evidence and finding |
| --- | --- | --- |
| FM-01 | Conceptual versus formal representations and model–target distinction | [SEP Models in Science](https://plato.stanford.edu/entries/models-science/); purpose and assumptions remain explicit |
| FM-02 | Syntax, semantics and real-world interpretation separate | SEP Models in Science; formal well-formedness does not establish empirical accuracy |
| FM-03 | Transition-system example `(S,I,→,L)` | Two states, initial OFF, two opposing transitions; **correction committed** to explain infinite alternation under the stipulated relation |
| FM-04 | Safety, liveness, invariant and proof obligations | Formal-method concepts scoped to declared model and fairness/environment assumptions; physical truth not claimed |
| FM-05 | Many-to-one abstraction and transition preservation | Example `c2→c3` requires abstract `NORMAL→ALERT` in a transition-covering may over-approximation; mapping alone is insufficient |
| FM-06 | Formal verification distinct from empirical and engineering validation | NASA Systems Engineering and SEP; tool proof is conditional on modeling correspondence, not product acceptance |

## Recorded corrections

1. **Ontologies and Taxonomies:** Added explicit distinction between SKOS immediate `skos:broader` and the separately defined transitive superproperty `skos:broaderTransitive`. Mere adjacency in a concept hierarchy does not establish OWL subclass semantics.
2. **Conceptual and Formal Models:** Clarified that the two-state transition system permits infinite OFF/ON alternation **under the stipulated relation**, not as a claim about real physical devices.

No numerical correction was required in the dimensional-conversion examples. The JSON Schema example's `required`, `type`, `enum`, and `additionalProperties` behavior was checked against the stated dialect's published semantics; this was a spec/manual check, **not an executed validator test**.

## Calculation and semantic spot checks

| Case | Checked result |
| --- | --- |
| `2.5 km → m` | 2500 m |
| `72 km/h → m/s` | 20 m/s |
| `20 °C → K` absolute temperature | 293.15 K |
| `Δ20 °C → ΔK` temperature interval | 20 K |
| `1 KiB` and `1 kB` | 1024 bytes and 1000 bytes respectively |
| `N = kg·m·s⁻²` | Dimensional form of SI force unit |
| DeviceRecord numeric versus string temperature field | Number conforms; string conflicts with declared type |
| Two-state OFF/ON transition example | Infinite alternating sequence under total deterministic relation |
| `c2→c3`, `α(c2)=NORMAL`, `α(c3)=ALERT` | Corresponding abstract may-transition must cover `NORMAL→ALERT` for that preservation criterion |

## Internal link checks

All **distinct relative Markdown file destinations referenced within the five Batch 07 articles** were reopened via the GitHub contents API. Repeated links and links already directly in Batch 07 were not counted as distinct external targets. No missing relative file destination was identified. This check covers file destinations, **not** URL fragments, external web availability, or the complete repository's link graph.

## Scope and acceptance disposition

- **24 prior Reviewed + 5 Batch 07 Reviewed = 29 Reviewed (model-assisted)**.
- **0 remaining authored drafts**; **80 approved headings not yet authored**. Wave A authoring **26/26**; all 26 Wave A articles now internally Reviewed, with three additional Reviewed pilot articles in later waves.
- The **12 approved knowledge areas and 109 approved headings are unchanged**; no additional ontology/schema/predicate standard or mandated implementation adopted.
- **G-01** mathematical breadth, **G-04** general temporality, and **G-06** AI/ML remain open architecture decisions.
- No Knowledge Checks, Practical Assessments, scoring or graded work introduced.
- Source review is **Core claims checked**, not complete source validation **Verified**; independent human expert review and final publication acceptance remain unclaimed.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
