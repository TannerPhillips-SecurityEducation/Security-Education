# Wave C Technical Review: Batch 03

**Review date:** November 17, 2026  
**Scope:** Sensors and Actuators; Signal Conversion; Physical Control Mechanisms; Memory and Storage; Buses and Interfaces; Input/Output; Timing and Clocks; Firmware; Hardware Abstraction.  
**Method:** Reopened nine canonical drafts, examined **54 material claim families** against JCGM VIM, NIST, MIT 6.003 and 6.004, NASA and OpenStax references; independently recomputed the stipulated examples; inspected canonical ownership and epistemic limits; corrected ambiguous timing notation; and fetched each of the **35 distinct relative Markdown file destinations** linked from the nine articles.  
**Disposition:** All nine pass **scoped model-assisted technical review** with the recorded corrections and conditions. This is **Core claims checked**, not complete source-level verification, independent human expert peer review, hardware testing, standards certification or final publication acceptance.

## Claim-to-source ledger

### Sensors and Actuators

[Reviewed article](physical-electrical-principles/sensors-and-actuators.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| SA-01 | Sensors observe a measurand and actuators influence physical conditions | [JCGM VIM](https://jcgm.bipm.org/vim/en/) and [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/); sensing indication and physical intervention remain separate |
| SA-02 | Sensing is a chain of transduction, signal conditioning and interpretation | [MIT Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/); chain is illustrative, not mandatory physical architecture |
| SA-03 | Sensitivity, operating range, resolution and measurement accuracy differ | JCGM VIM; `a=dV/dT` applies to the stipulated linear transfer function |
| SA-04 | Toy sensor `V=0.05T` V for T in °C | `T=20°C` gives `1.00V`, `1.05V` inversely gives `21°C`, `+0.01V` gives apparent `+0.2°C`; not a measured uncertainty budget |
| SA-05 | Command accepted, actual actuation and observed outcome differ | [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/); no inference from command receipt to real-world effect |
| SA-06 | Sensor presence is not a proof of observability or calibration | [MIT Feedback Control](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/); no universal sensor redundancy guarantee |

### Signal Conversion

[Reviewed article](physical-electrical-principles/signal-conversion.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| SC-01 | Conversion differs from measurement, encoding and information compression | [MIT 6.003 Signals and Systems](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/); scopes and representations explicitly separated |
| SC-02 | Sampling, quantization and encoding are conceptually separable | [MIT Lecture 22: Sampling and Quantization](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-22-sampling-and-quantization/); **dedicated source added** |
| SC-03 | Twelve-bit uniform quantizer has 4096 bins on half-open `[0,4.096 V)` | Step `4.096/4096=0.001V`; bin code for `2.500V` is `2500` under stated floor convention |
| SC-04 | Reconstruction error is dependent on the chosen bin reconstruction rule | Lower-edge estimate `2.500V`, midpoint estimate `2.5005V`; ideal midpoint error at most `0.5mV` in range |
| SC-05 | Aliasing is possible without suitable band-limitation, sampling and filtering | [MIT Sampling Lecture](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-21-sampling/); 1000 samples/s gives conventional Nyquist frequency 500Hz |
| SC-06 | DAC output and physical measurement need not equal the represented ideal value | MIT 6.003; converter width does not establish effective sensor accuracy |

### Physical Control Mechanisms

[Reviewed article](physical-electrical-principles/physical-control-mechanisms.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| PC-01 | Physical plant intervention differs from abstract control command | [MIT Feedback Control](https://ocw.mit.edu/courses/2-14-analysis-and-design-of-feedback-control-systems-spring-2014/); supplied command does not prove energy or force delivered |
| PC-02 | Saturation, inertia, loss and response delay constrain physical plants | MIT Feedback Control; listed physical mechanisms are examples, not universal taxonomy |
| PC-03 | Open-loop influence and feedback regulation are separate mechanisms | MIT Feedback Control and systems canonical reference; a sensor alone does not guarantee stable feedback |
| PC-04 | Thermal worked example conserves net modeled energy | `6000J - 2000J = 4000J`; `4000 J/(2000 J/K)=2K` change, also a 2 °C interval, not 2 °C absolute |
| PC-05 | Heat-balance model assumptions and thermodynamic grounding | [OpenStax First Law](https://openstax.org/books/university-physics-volume-2/pages/3-3-first-law-of-thermodynamics) and [Heat Transfer](https://openstax.org/books/university-physics-volume-2/pages/1-4-heat-transfer-specific-heat-and-calorimetry); **direct sources added** |
| PC-06 | Model-based stability and engineering verification remain distinct | [NASA Systems Fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/); no safety signoff or real device performance claimed |

### Memory and Storage

[Reviewed article](digital-systems-hardware/memory-and-storage.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| MS-01 | Memory and storage include different physical retention/access mechanisms | [MIT 6.004 Caches and Memory Hierarchy](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c14/c14s1/); cache and backing storage distinguished |
| MS-02 | Addressability differs from installed physical memory capacity | MIT 6.004; memory maps may include devices, holes and translations |
| MS-03 | Volatile, nonvolatile, SRAM and DRAM have different retention mechanisms | MIT 6.004; no claim of fault-free retention or unlimited endurance |
| MS-04 | Cache hit/miss and locality characterize workload-dependent behavior | MIT 6.004; hit ratio is measured over a defined access distribution |
| MS-05 | Average memory access time formula | `4ns + (1-0.9)×40ns=8ns`; separate conditional latencies 4ns hit and 44ns miss; agrees with [MIT annotated example](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c14/c14s1/) |
| MS-06 | Cache coherence does not imply persistence, and latency differs from bandwidth | MIT 6.004; physical storage bits do not determine data meaning |

### Buses and Interfaces

[Reviewed article](digital-systems-hardware/buses-and-interfaces.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| BI-01 | Bus, point-to-point link and switched fabric are different arrangements | [MIT Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/); not every interconnect is a shared bus |
| BI-02 | Address, data, control, timing and acknowledgment are separate transaction roles | [MIT Devices and Interrupts](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c18/c18s1/) and [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/); **specific MIT source added** |
| BI-03 | Contention and arbitration affect scheduling under assumptions | MIT 6.004; no universal priority/fairness promise |
| BI-04 | Ideal 32-bit accepted transfer each cycle at 100 MHz | `32bits/8×100,000,000=400,000,000 bytes/s=400MB/s` decimal; half accepted cycles → 200MB/s under the stipulation |
| BI-05 | Data width, word width, endianness and memory-mapped device semantics differ | [MIT 6.004](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/); address-mapped device is not arbitrary normal RAM |
| BI-06 | Clock domains and error reporting need explicit contracts | [MIT Sequential Logic](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c6/c6s1/); correct sampled behavior conditional on electrical/timing model |

### Input/Output

[Reviewed article](digital-systems-hardware/input-output.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| IO-01 | Hardware I/O includes registers, device operations and physical effects | [MIT 6.004 Devices and Interrupts](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c18/c18s1/); source added explicitly |
| IO-02 | Memory-mapped I/O has side effects different from ordinary RAM | MIT 6.004; valid access may initiate a transaction rather than return passive data |
| IO-03 | Polling, interrupts and DMA are different coordination mechanisms | MIT 6.004; not a claim that DMA requires no CPU configuration or coherence actions |
| IO-04 | Interrupt service budget example | `500/s ×20µs=10ms` of CPU time per second = **1%** of one CPU-second under specified non-overlap assumptions |
| IO-05 | Buffers and flow control address producer/consumer rate mismatch | MIT 6.004; finite buffers can fill; acknowledgment does not prove durable action |
| IO-06 | Device status, observed plant state and software completion differ | [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/); no universal device-driver semantics mandated |

### Timing and Clocks

[Reviewed article](digital-systems-hardware/timing-and-clocks.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| TC-01 | Periodic hardware clock, cycles and temporal measures are related but distinct | [MIT Sequential Logic](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c5/c5s1/); a clock is not global temporality |
| TC-02 | Clock rate, period and cycle count | `100MHz=10ns/cycle`; five cycles = 50ns; one million cycles = 10ms if rate constant |
| TC-03 | Setup/hold and propagation delay constrain sequential elements | MIT sequential logic; separate hold analysis required |
| TC-04 | Register-to-register setup constraint under declared skew sign convention | **Corrected** to `T≥t_CQ+t_path+t_setup+U−S`, with `S=t_capture−t_launch` and nonnegative uncertainty allowance U; no claim of complete timing signoff |
| TC-05 | Synchronization reduces but cannot eliminate all metastability risk | [MIT Synchronization and Metastability](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c6/c6s1/); **specific source added** |
| TC-06 | Hardware timing neither defines wall clock nor distributed ordering | G-04 remains open; control/system and communication areas keep existing ownership |

### Firmware

[Reviewed article](digital-systems-hardware/firmware.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| FW-01 | Firmware is executable code associated closely with hardware functions | [NIST SP 800-193](https://csrc.nist.gov/pubs/sp/800/193/final); guidance applies specifically to platform firmware as stated |
| FW-02 | Hardware, firmware, drivers and applications have different but overlapping roles | NIST SP 800-193 and MIT 6.004; no universal “always before OS” rule |
| FW-03 | Image presence, formatting, authentication, execution and physical outcome are separate | NIST platform firmware resiliency; authentication alone does not prove functional correctness |
| FW-04 | Boot, trust, protection/detection/recovery are conditional mechanisms | NIST SP 800-193; no claim that all firmware uses secure boot or a root of trust |
| FW-05 | Firmware storage capacity example | `128KiB−96KiB=32KiB`; 131072−98304=32768 bytes; fit alone does not prove deployability |
| FW-06 | Update/rollback can fail under environmental and implementation conditions | NIST SP 800-193; rollback file presence is not recovery guarantee |

### Hardware Abstraction

[Reviewed article](digital-systems-hardware/hardware-abstraction.md)

| ID | Material claim | Evidence and disposition |
| --- | --- | --- |
| HA-01 | Hardware abstraction exposes a selected contract, hiding implementation details | [MIT Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/); abstract behavior not automatically physical equivalence |
| HA-02 | ISA, device interface, HAL, driver and virtual devices are distinct possible boundaries | MIT 6.004 and [NASA Interface Management](https://www.nasa.gov/reference/6-3-interface-management/); not a prescribed fixed stack |
| HA-03 | Compatibility includes meaning, timing, ordering and faults, not just function names | NASA Interface Management; semantic obligations explicitly stated |
| HA-04 | Active-high versus active-low worked example | Logical ON→physical 1 for active-high; logical ON→physical 0 for active-low, conditional on stipulated wiring |
| HA-05 | Abstraction portability and performance have tradeoffs | MIT 6.004; not a universal portability guarantee |
| HA-06 | Emulation, virtualization and physical hardware can differ in timing/fault behavior | MIT 6.004; an accepted software response is not end-to-end physical confirmation |

## Recorded corrections and source improvements

1. **Timing and Clocks:** Corrected ambiguous setup-time inequality. With capture-minus-launch skew `S` and uncertainty `U≥0`, the illustrative constraint is `T≥t_CQ+t_path+t_setup+U−S`, with hold constraints treated separately. Added MIT 6.004 sequential logic and metastability references.
2. **Signal Conversion:** Added a direct MIT Lecture 22 Sampling and Quantization reference, distinguishing quantization from sampling.
3. **Physical Control Mechanisms:** Added direct OpenStax first-law and heat-transfer sources for the illustrative thermal balance.
4. **Input/Output and Buses and Interfaces:** Added MIT 6.004 *Devices and Interrupts* reference to support transaction and interrupt semantics.
5. **No numerical corrections were needed** in the nine toy examples after recomputation.

## Numerical verification ledger

| Example | Independently checked |
| --- | --- |
| `V=0.05T` at 20°C | 1.00V |
| 1.05V inverse of ideal sensor relation | 21°C |
| 10mV apparent change at 50mV/°C sensitivity | 0.2°C |
| 12-bit quantizer over [0,4.096V) | 4096 bins, 1mV/bin |
| Code for 2.500V in specified floor quantizer | 2500 |
| Code 2500 midpoint | 2.5005V; ideal midpoint error ≤0.5mV |
| `6000−2000` J, `C=2000J/K` | 4000J net; 2K temperature increase |
| Cache 4ns lookup, 90% hit rate, 40ns miss penalty | 8ns average |
| 32-bit word every cycle at 100MHz | 400MB/s decimal |
| 500 interrupts/s, 20µs handling each | 10ms CPU/s = 1% |
| 100MHz clock period, five cycles | 10ns period, 50ns for five cycles |
| One million cycles at 100MHz | 10ms |
| 128KiB minus 96KiB firmware image | 32KiB (32768 bytes) remaining |

All calculations are for **invented, bounded examples**, not measured device results.

## Link and source-review scope

The nine articles contain **93 relative Markdown link occurrences** resolving to **35 distinct file destinations**. Every distinct destination was reopened through GitHub: **35/35 found**. No complete check of fragment anchors, external URL availability, the entire repository graph, or semantic correctness of every cross-link is claimed.

The documented second pass evaluates **material claim groups**, not every line of a textbook, standards document or system implementation. The source-review state is **Core claims checked**. The stronger `Verified` state, independent human peer review and final `Published` acceptance remain outstanding.

## Architecture and disposition

- **Physical & Electrical Principles:** Nine of nine approved subjects now internally Reviewed, including its three Batch 03 articles.
- **Digital Systems & Hardware:** Nine of nine approved subjects internally Reviewed, including its six Batch 03 articles and the earlier Digital Logic pilot.
- **Wave C:** 18/18 authored and model-assisted Reviewed. Waves A and B remain internally Reviewed.
- **Portfolio:** **72 Reviewed (model-assisted), 0 Draft, 37 Inventoried without article**, totaling 109 approved headings.
- Approved **12 knowledge areas, 109 headings** unchanged. G-01 mathematics breadth, G-04 general temporality and G-06 AI/ML remain unresolved; no Knowledge Checks, Practical Assessments or new subject categories introduced.

[Fundamentals](README.md) · [Development Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Curriculum Plan](CURRICULUM-DEVELOPMENT-PLAN.md)
