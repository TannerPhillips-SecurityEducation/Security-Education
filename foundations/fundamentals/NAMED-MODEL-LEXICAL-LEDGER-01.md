# Named Foundational Models: Lexical Presence Ledger 01

**Date:** November 18, 2026  
**Corpus examined:** 109 currently tracked canonical Fundamentals articles in 12 existing knowledge areas. The 109 count is **a versioned snapshot, not a fixed quota**.  
**Reproducible script:** [audit_named_models.py](tools/audit_named_models.py)  
**GitHub Actions evidence:** [Successful run 44279824463](https://github.com/TannerPhillips-SecurityEducation/Security-Education/actions/runs/44279824463)  
**Result:** **77 candidate names searched; 38 matched at least one article; 39 had no exact lexical match.** Of the 38 matched names, 36 matched within the candidate's expected area (other areas may still be valid). This is **not** a score of conceptual completeness.

## Limits of the method

This Python scanner searches candidate spellings and aliases in Markdown text outside fenced code blocks. It normalizes common Unicode dash/apostrophe variants. It includes prose, link labels and citations. **A name appearing in a file does not prove the explanation is sufficient, technically correct, or properly sourced. A name not appearing does not prove the model or underlying idea is absent.** Example: a voltage-current relationship can be explained without the phrase “Ohm's law”; conversely, a source list can mention a framework without teaching it. Candidate selection is an editorial sample, not an exhaustive list of all important models.

The ledger contains historical observations from the cited workflow run and **will not automatically update** as articles change. Run the scanner to obtain the current status; a new historical ledger may be committed after a later audit.

## Area-level lexical counts

| Area | Names sampled | Mentioned anywhere | Mentioned within intended area |
| --- | ---: | ---: | ---: |
| Mathematics & Logic | 6 | 5 | 5 |
| Scientific & Analytical Reasoning | 6 | 5 | 5 |
| Models & Abstraction | 7 | 3 | 3 |
| Physical & Electrical Principles | 6 | 2 | 2 |
| Information & Data | 5 | 4 | 4 |
| Digital Systems & Hardware | 6 | 2 | 2 |
| Computation & Algorithms | 7 | 4 | 4 |
| Software & Programming | 7 | 3 | 3 |
| Operating System Principles | 5 | 4 | 4 |
| Communication & Distributed Systems | 8 | 4 | 3 |
| Systems & Engineering | 7 | 2 | 1 |
| Human & Sociotechnical Systems | 7 | 0 | 0 |
| **Total** | **77** | **38** | **36** |

## Named-model ledger

| Diagnostic ID | Expected area | Model, framework, architecture, or relevant foundation | Source class | Article hits anywhere | Hits in expected area | Up to four matching article basenames |
| --- | --- | --- | --- | ---: | ---: | --- |
| M001 | Mathematics & Logic | Linear algebra | mathematical foundation | 1 | 1 | algebra-and-functions |
| M002 | Mathematics & Logic | Graph theory | mathematical foundation | 10 | 2 | graph-theory,sets-and-relations,causality-and-correlation,abstraction |
| M003 | Mathematics & Logic | Bayesian inference | inferential model | 1 | 1 | probability-and-statistics |
| M004 | Mathematics & Logic | Markov models | stochastic model | 0 | 0 | No lexical match |
| M005 | Mathematics & Logic | Proof systems | formal reasoning | 2 | 1 | boolean-and-predicate-logic,deduction-induction-abduction |
| M006 | Mathematics & Logic | Topology | mathematical foundation | 7 | 2 | discrete-mathematics,graph-theory,boundaries,electrical-circuits |
| M007 | Scientific & Analytical Reasoning | Scientific method | methodological framework | 1 | 1 | validation-and-falsification |
| M008 | Scientific & Analytical Reasoning | Experimental design | methodological framework | 3 | 3 | deduction-induction-abduction,hypotheses-and-experiments,validation-and-falsification |
| M009 | Scientific & Analytical Reasoning | Causal graphs / structural causal models | explanatory formal model | 1 | 1 | causality-and-correlation |
| M010 | Scientific & Analytical Reasoning | VIM metrology vocabulary | terminology standard | 4 | 1 | units-and-quantities,measurement,sensors-and-actuators,signal-conversion |
| M011 | Scientific & Analytical Reasoning | GUM measurement uncertainty | measurement framework | 0 | 0 | No lexical match |
| M012 | Scientific & Analytical Reasoning | Bayesian updating | inferential model | 1 | 1 | evidence |
| M013 | Models & Abstraction | Finite-state machines | state transition model | 2 | 1 | state-events-and-transitions,digital-logic |
| M014 | Models & Abstraction | Petri nets | concurrent system model | 0 | 0 | No lexical match |
| M015 | Models & Abstraction | UML | modeling language | 0 | 0 | No lexical match |
| M016 | Models & Abstraction | SysML | modeling language | 0 | 0 | No lexical match |
| M017 | Models & Abstraction | Formal verification / model checking | formal method | 3 | 1 | conceptual-and-formal-models,concurrency-and-parallelism,synchronization |
| M018 | Models & Abstraction | RDF and OWL | semantic representation standards | 10 | 6 | classification,entities-and-attributes,identity-and-distinction,ontologies-and-taxonomies |
| M019 | Models & Abstraction | Abstract interpretation | formal analysis framework | 0 | 0 | No lexical match |
| M020 | Physical & Electrical Principles | Ohm's law | physical law | 0 | 0 | No lexical match |
| M021 | Physical & Electrical Principles | Kirchhoff's circuit laws | physical law | 2 | 2 | electrical-circuits,electronics |
| M022 | Physical & Electrical Principles | Maxwell's equations | physical theory | 0 | 0 | No lexical match |
| M023 | Physical & Electrical Principles | Fourier analysis | mathematical signal model | 0 | 0 | No lexical match |
| M024 | Physical & Electrical Principles | Nyquist-Shannon sampling theorem | theorem | 2 | 2 | analog-and-digital-signals,signal-conversion |
| M025 | Physical & Electrical Principles | PID control | control model | 0 | 0 | No lexical match |
| M026 | Information & Data | Shannon entropy and channel capacity | information-theoretic model | 4 | 2 | signal-conversion,bits-and-bytes,information-theory,communication-channels |
| M027 | Information & Data | Relational data model | data model | 3 | 2 | schemas,databases-and-queries,datasets-records-fields-and-values |
| M028 | Information & Data | Entity-relationship model | data model | 0 | 0 | No lexical match |
| M029 | Information & Data | W3C PROV provenance | provenance model / standard | 2 | 2 | data-provenance-and-lifecycle,metadata |
| M030 | Information & Data | Data lifecycle model | lifecycle model | 1 | 1 | data-provenance-and-lifecycle |
| M031 | Digital Systems & Hardware | Von Neumann architecture | computer architecture | 0 | 0 | No lexical match |
| M032 | Digital Systems & Hardware | Harvard architecture | computer architecture | 0 | 0 | No lexical match |
| M033 | Digital Systems & Hardware | Flynn taxonomy | architecture taxonomy | 0 | 0 | No lexical match |
| M034 | Digital Systems & Hardware | Memory hierarchy | computer architecture | 4 | 2 | memory-and-storage,processors-and-instruction-sets,complexity,computational-data-structures |
| M035 | Digital Systems & Hardware | Instruction-set architecture | computer architecture | 3 | 3 | computing-components,hardware-abstraction,processors-and-instruction-sets |
| M036 | Digital Systems & Hardware | Cache coherence models | memory model | 0 | 0 | No lexical match |
| M037 | Computation & Algorithms | Turing machines | computability model | 2 | 2 | complexity,computability |
| M038 | Computation & Algorithms | Church-Turing thesis | computability thesis | 1 | 1 | computability |
| M039 | Computation & Algorithms | Lambda calculus | computability formalism | 0 | 0 | No lexical match |
| M040 | Computation & Algorithms | Asymptotic complexity | analytical model | 3 | 3 | complexity,computational-data-structures,iteration-and-recursion |
| M041 | Computation & Algorithms | Actor model | concurrency model | 1 | 1 | concurrency-and-parallelism |
| M042 | Computation & Algorithms | Communicating sequential processes | concurrency model | 0 | 0 | No lexical match |
| M043 | Computation & Algorithms | Random-access machine model | computational cost model | 0 | 0 | No lexical match |
| M044 | Software & Programming | Type systems | formal programming model | 2 | 1 | data-types,programming-languages |
| M045 | Software & Programming | Design by contract | design principle | 3 | 2 | iteration-and-recursion,error-handling,software-interfaces |
| M046 | Software & Programming | Model-view-controller | software architecture | 0 | 0 | No lexical match |
| M047 | Software & Programming | Software V-model | engineering lifecycle model | 0 | 0 | No lexical match |
| M048 | Software & Programming | SOLID principles | design heuristic | 0 | 0 | No lexical match |
| M049 | Software & Programming | Testing pyramid | testing heuristic | 0 | 0 | No lexical match |
| M050 | Software & Programming | Language operational semantics | language semantic model | 1 | 1 | syntax-and-semantics |
| M051 | Operating System Principles | Monolithic versus microkernel | operating system architecture | 1 | 1 | kernels |
| M052 | Operating System Principles | Virtual memory model | operating system abstraction | 2 | 1 | memory-and-storage,memory-management |
| M053 | Operating System Principles | Copy-on-write | memory-management mechanism | 1 | 1 | memory-management |
| M054 | Operating System Principles | POSIX interface model | interface standard | 2 | 2 | filesystems,system-calls |
| M055 | Operating System Principles | Process lifecycle models | execution-state model | 0 | 0 | No lexical match |
| M056 | Communication & Distributed Systems | OSI reference model | communication reference architecture | 0 | 0 | No lexical match |
| M057 | Communication & Distributed Systems | Internet protocol suite layers | communication architecture | 0 | 0 | No lexical match |
| M058 | Communication & Distributed Systems | Shannon-Weaver communication model | communication model | 0 | 0 | No lexical match |
| M059 | Communication & Distributed Systems | CAP theorem | distributed consistency theorem | 0 | 0 | No lexical match |
| M060 | Communication & Distributed Systems | FLP impossibility | distributed computing result | 1 | 1 | synchronization-and-coordination |
| M061 | Communication & Distributed Systems | Happens-before relation | distributed ordering model | 1 | 0 | synchronization |
| M062 | Communication & Distributed Systems | Linearizability | consistency model | 3 | 1 | synchronization,processes-and-threads,distributed-state |
| M063 | Communication & Distributed Systems | Paxos or Raft consensus | distributed algorithm | 1 | 1 | synchronization-and-coordination |
| M064 | Systems & Engineering | ISO IEC IEEE 42010 architecture descriptions | architecture description standard | 0 | 0 | No lexical match |
| M065 | Systems & Engineering | ISO IEC IEEE 15288 system lifecycle | engineering process standard | 0 | 0 | No lexical match |
| M066 | Systems & Engineering | Model-based systems engineering | engineering approach | 0 | 0 | No lexical match |
| M067 | Systems & Engineering | Systems engineering V-model | engineering lifecycle model | 0 | 0 | No lexical match |
| M068 | Systems & Engineering | Reliability block diagrams | reliability model | 1 | 1 | reliability-and-failure |
| M069 | Systems & Engineering | STPA hazard analysis | safety-analysis method | 0 | 0 | No lexical match |
| M070 | Systems & Engineering | Systems thinking | systems approach | 1 | 0 | state-events-and-transitions |
| M071 | Human & Sociotechnical Systems | Norman seven stages of action | interaction model | 0 | 0 | No lexical match |
| M072 | Human & Sociotechnical Systems | Cognitive load theory | cognitive model | 0 | 0 | No lexical match |
| M073 | Human & Sociotechnical Systems | Signal detection theory | decision model | 0 | 0 | No lexical match |
| M074 | Human & Sociotechnical Systems | Swiss cheese model | safety/human-error model | 0 | 0 | No lexical match |
| M075 | Human & Sociotechnical Systems | Fitts's law | human-performance model | 0 | 0 | No lexical match |
| M076 | Human & Sociotechnical Systems | Hick-Hyman law | human-performance model | 0 | 0 | No lexical match |
| M077 | Human & Sociotechnical Systems | Sociotechnical systems theory | sociotechnical model | 0 | 0 | No lexical match |

## Rules for interpretation and follow-up

1. Distinguish **(a) named, (b) explained, (c) demonstrated with conditions and examples, (d) source checked, (e) independently reviewed**. These are separate evidence states.
2. First read the expected canonical article and nearby related articles. Search synonyms, equations and mechanisms before calling a model absent.
3. Verify the external model's actual purpose, authority, version, assumptions and limits. Do not import its taxonomy as an automatic Fundamentals taxonomy.
4. Decide on **deeper treatment**, an **additional subject**, a **split**, a **merge**, or **cross-references only**. The living inventory may expand or contract after justified governance decisions.
5. Avoid automatic additions for model-specific practices, vendor architectures, implementation details or optional heuristics. A named model does not necessarily deserve its own heading.

[Fundamentals architecture](ARCHITECTURE.md#living-subject-inventory-and-versioned-change-control) · [Main index](README.md)
