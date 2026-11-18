# Wave C Technical Review: Batch 01

**Review date:** November 17, 2026  
**Scope:** Matter and Energy; Electricity; Electrical Circuits; Computing Components.  
**Method:** Reopened the four authored articles, checked material claim families against BIPM SI material, OpenStax University Physics, MIT Computation Structures and NIST prefix guidance, recomputed physical/electrical/address examples, inspected canonical ownership boundaries, and reopened the articles' distinct relative file destinations through GitHub.  
**Disposition:** **24 material claim groups reviewed; four references pass scoped model-assisted technical review.** This is not independently commissioned human expert peer review, comprehensive standards certification, a physical laboratory evaluation, full source-level verification or final publication acceptance.

## Claim-to-source ledger

### Matter and Energy
[Reviewed article](physical-electrical-principles/matter-and-energy.md)

| ID | Material claim | Evidence / finding |
| --- | --- | --- |
| ME-01 | Matter/material attributes depend on a physical description and chosen scale | [OpenStax University Physics](https://openstax.org/books/university-physics-volume-1/pages/7-1-work); article distinguishes physical properties from a universal material taxonomy |
| ME-02 | Force–displacement work is a dot product, and can be positive, negative or zero | [OpenStax Work §7.1](https://openstax.org/books/university-physics-volume-1/pages/7-1-work); constant-force expression is appropriately scoped |
| ME-03 | Energy/work in joules and power in watts are distinct quantities | [BIPM SI Brochure](https://www.bipm.org/en/publications/si-brochure); `J=N·m`, `W=J/s`; symbols require context |
| ME-04 | Force of 10 N through 3 m parallel displacement | Independently recomputed 30 J; 30 J transferred uniformly over 5 s yields mean power 6 W |
| ME-05 | Isolated-system conservation differs from energy balance across an open boundary | Source concepts and boundary caveat retained; heat, work, radiation and other transfers are not equated |
| ME-06 | Electronic assembly receiving 20 W over 60 s | Recomputed input energy 1200 J; explicitly not a prediction that 1200 J becomes stored heat or determines temperature rise |

### Electricity
[Reviewed article](physical-electrical-principles/electricity.md)

| ID | Material claim | Evidence / finding |
| --- | --- | --- |
| EL-01 | Charge, current, potential difference, resistance and resistivity are distinct | [OpenStax Resistivity and Resistance](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance); [BIPM SI](https://www.bipm.org/en/publications/si-brochure) |
| EL-02 | Current is net charge transfer rate with declared surface/direction | [OpenStax Conduction in Metals](https://openstax.org/books/university-physics-volume-2/pages/9-2-model-of-conduction-in-metals); `2 C/4 s=0.5 A` confirmed |
| EL-03 | Conventional current and electron drift direction differ in metallic conductors | OpenStax conduction section; no claim that all charge transport always involves electrons only |
| EL-04 | Ohm's law is conditional on an ohmic element/operating regime | [OpenStax Resistivity](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance); `12 V/6 Ω=2 A` under assumptions |
| EL-05 | Electrical power `p=vi` requires sign convention; energy integrates power | 12 V × 2 A = 24 W absorbed under passive sign convention; at constant 24 W over 5 s = 120 J |
| EL-06 | AC/DC refers to temporal polarity/current behavior; analog/digital refers to representation | Editorial conceptual distinction is scoped and does not treat waveforms or hardware as universally ideal |

### Electrical Circuits
[Reviewed article](physical-electrical-principles/electrical-circuits.md)

| ID | Material claim | Evidence / finding |
| --- | --- | --- |
| EC-01 | A circuit model selects nodes, branches, paths and component behavior | [OpenStax Series and Parallel](https://openstax.org/books/university-physics-volume-2/pages/10-2-resistors-in-series-and-parallel); diagram is a model rather than a tested physical assembly |
| EC-02 | Idealized R, C and L device relations require stated operating assumptions | Mathematical review of `v=iR`, `i=C(dv/dt)`, `v=L(di/dt)`; derivative notation was repaired during initial authoring and independently rechecked |
| EC-03 | KCL and familiar lumped/quasi-static KVL need explicit physical assumptions | [OpenStax Kirchhoff's Rules](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules); **added dedicated source** during this audit |
| EC-04 | Series and parallel topology determine shared current and voltage | OpenStax Series/Parallel; physical proximity alone is insufficient |
| EC-05 | Parallel 4 Ω and 6 Ω resistors across ideal 12 V source | `R_eq=2.4 Ω`, `I_total=5 A`, branches 3 A and 2 A; KCL consistent; powers 36 W and 24 W sum to 60 W |
| EC-06 | Capacitive/inductive storage requires dynamic initial-condition models | Ideal energy expressions `E_C=½CV²`, `E_L=½LI²` are explicitly conditional, not empirical device ratings |

### Computing Components
[Reviewed article](digital-systems-hardware/computing-components.md)

| ID | Material claim | Evidence / finding |
| --- | --- | --- |
| CC-01 | Computing hardware comprises cooperating processing, memory, I/O and interconnect roles | [MIT 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/); roles not mandated separate chips |
| CC-02 | Processor instruction-set semantics differ from specific datapath/control implementation | [MIT 6.004 Designing an Instruction Set](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c9/c9s1/); fetch/decode/execute stages are illustrative, not one-cycle universal physical sequences |
| CC-03 | Registers, caches, RAM and persistent storage occupy different hierarchy/retention roles | [MIT 6.004](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/); volatility does not guarantee reliability or infinite retention |
| CC-04 | Buses, interconnects and I/O exchange information under declared interface semantics | MIT 6.004; does not treat every connection as a shared bus |
| CC-05 | Addressable capacity depends on both width and addressable unit | `2^16=65,536` addresses; byte-addressed gives 64 KiB; two-byte word-addressed gives 128 KiB under dense mapping |
| CC-06 | Address width does not prove installed memory; frequency does not by itself determine throughput | MIT 6.004 and model caveats; memory-mapped I/O, reservations and performance bottlenecks remain possible |

## Corrections and acceptance qualifications

1. **Electrical Circuits source grounding:** Added a direct [OpenStax Kirchhoff's Rules](https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules) reference. The previously authored KCL/KVL material now has a dedicated source rather than only a related series/parallel reference.
2. **Derivative notation:** Confirmed the earlier authoring correction from malformed capacitor/inductor expressions to `i=C(dv/dt)` and `v=L(di/dt)`. This correction was already committed before this scoped review.
3. **No numerical correction:** Recomputed all material worked examples under their explicitly hypothetical parameters and found no mismatches. The article examples are inventions, not measured physical systems.

## Numerical evidence ledger

| Calculation | Independently computed result |
| --- | --- |
| 10 N parallel to 3 m displacement | 30 J work |
| 30 J over 5 s | 6 W mean power |
| 20 W for 60 s | 1200 J input energy |
| 2 C through a surface in 4 s | 0.5 A mean current |
| 12 V across ideal 6 Ω resistor | 2 A |
| 12 V and 2 A under passive sign convention | 24 W absorbed |
| 24 W constant over 5 s | 120 J |
| Ideal parallel 4 Ω and 6 Ω | `R_eq=2.4 Ω`; 3 A + 2 A = 5 A |
| Power in ideal 4 Ω / 6 Ω branches | 36 W / 24 W; total 60 W |
| 16-bit, byte-addressed space | 65,536 bytes = 64 KiB |
| 16-bit, 2-byte-word-addressed space | 131,072 bytes = 128 KiB |

## Internal link and source limitations

The four articles had **50 relative Markdown-link occurrences** resolving to **20 distinct relative file destinations**. The 20 file destinations were reopened through GitHub and **20/20 resolved**. This check excludes URL-fragment validity, complete external URL checks, and every other link in the repository.

Material claims were checked against the cited public sources and examples against their explicit assumptions. This does not amount to independent laboratory measurement, comprehensive inspection of every PDF/textbook page, paid standards conformance, or expert human peer review. **Reviewed (model-assisted)** corresponds to **Core claims checked**, not the stronger `Verified` source state or `Published` acceptance.

## Architectural limits and disposition

- **Matter and Energy** owns foundational material/energy constraints; **Electricity** owns electrical quantities and carriers; **Electrical Circuits** owns interconnected element behavior; **Computing Components** owns integrated digital hardware roles.
- Existing canonical ownership of measurement, units, graphs, state, digital logic, and general systems engineering is preserved.
- These four articles are promoted to **Reviewed (model-assisted)** after their scope-specific audit. They are not independently human accepted or published.
- The **12 approved knowledge areas** and **109 approved subject headings** remain unchanged. G-01 mathematical breadth, G-04 general temporality, G-06 AI/ML remain open. No Knowledge Checks, Practical Assessments or mandatory implementation standard is introduced.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
