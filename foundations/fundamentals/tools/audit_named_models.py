#!/usr/bin/env python3
"""Diagnostic only: find named foundational models in canonical article prose.

This is a lexical presence scan, NOT a validation of conceptual coverage,
model correctness, or citation support. A nonmatch is not proof of a gap.
Run from repository root or anywhere:
  python3 foundations/fundamentals/tools/audit_named_models.py
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AREAS = {
    "mathematics-logic": "math",
    "scientific-analytical-reasoning": "science",
    "models-abstraction": "models",
    "physical-electrical-principles": "physical",
    "information-data": "information",
    "digital-systems-hardware": "hardware",
    "computation-algorithms": "computation",
    "software-programming": "software",
    "operating-system-principles": "os",
    "communication-distributed-systems": "communications",
    "systems-engineering": "systems",
    "human-sociotechnical-systems": "human",
}
CATALOG = json.loads(r'''[{"id":"M001","area":"math","name":"Linear algebra","kind":"mathematical foundation","aliases":["linear algebra","vector space","eigenvalue"]},{"id":"M002","area":"math","name":"Graph theory","kind":"mathematical foundation","aliases":["graph theory","graph traversal"]},{"id":"M003","area":"math","name":"Bayesian inference","kind":"inferential model","aliases":["Bayesian inference","Bayes theorem","Bayes' theorem"]},{"id":"M004","area":"math","name":"Markov models","kind":"stochastic model","aliases":["Markov chain","Markov model","Markov process"]},{"id":"M005","area":"math","name":"Proof systems","kind":"formal reasoning","aliases":["proof system","proof calculus","natural deduction"]},{"id":"M006","area":"math","name":"Topology","kind":"mathematical foundation","aliases":["topology","topological space"]},{"id":"M007","area":"science","name":"Scientific method","kind":"methodological framework","aliases":["scientific method","hypothetico-deductive"]},{"id":"M008","area":"science","name":"Experimental design","kind":"methodological framework","aliases":["experimental design","randomized controlled","controlled experiment"]},{"id":"M009","area":"science","name":"Causal graphs / structural causal models","kind":"explanatory formal model","aliases":["causal graph","causal DAG","structural causal model"]},{"id":"M010","area":"science","name":"VIM metrology vocabulary","kind":"terminology standard","aliases":["international vocabulary of metrology","JCGM 200","VIM3"]},{"id":"M011","area":"science","name":"GUM measurement uncertainty","kind":"measurement framework","aliases":["guide to the expression of uncertainty","JCGM 100","GUM 1995"]},{"id":"M012","area":"science","name":"Bayesian updating","kind":"inferential model","aliases":["Bayesian updating","Bayes update","Bayesian inference"]},{"id":"M013","area":"models","name":"Finite-state machines","kind":"state transition model","aliases":["finite-state machine","finite state machine","finite automaton"]},{"id":"M014","area":"models","name":"Petri nets","kind":"concurrent system model","aliases":["Petri net"]},{"id":"M015","area":"models","name":"UML","kind":"modeling language","aliases":["Unified Modeling Language","UML"]},{"id":"M016","area":"models","name":"SysML","kind":"modeling language","aliases":["Systems Modeling Language","SysML"]},{"id":"M017","area":"models","name":"Formal verification / model checking","kind":"formal method","aliases":["model checking","formal verification"]},{"id":"M018","area":"models","name":"RDF and OWL","kind":"semantic representation standards","aliases":["RDF","OWL","resource description framework"]},{"id":"M019","area":"models","name":"Abstract interpretation","kind":"formal analysis framework","aliases":["abstract interpretation"]},{"id":"M020","area":"physical","name":"Ohm's law","kind":"physical law","aliases":["Ohm's law","Ohm law"]},{"id":"M021","area":"physical","name":"Kirchhoff's circuit laws","kind":"physical law","aliases":["Kirchhoff"]},{"id":"M022","area":"physical","name":"Maxwell's equations","kind":"physical theory","aliases":["Maxwell's equations","Maxwell equations"]},{"id":"M023","area":"physical","name":"Fourier analysis","kind":"mathematical signal model","aliases":["Fourier transform","Fourier analysis","Fourier series"]},{"id":"M024","area":"physical","name":"Nyquist-Shannon sampling theorem","kind":"theorem","aliases":["Nyquist","sampling theorem"]},{"id":"M025","area":"physical","name":"PID control","kind":"control model","aliases":["PID controller","proportional-integral-derivative"]},{"id":"M026","area":"information","name":"Shannon entropy and channel capacity","kind":"information-theoretic model","aliases":["Shannon entropy","Shannon information","channel capacity"]},{"id":"M027","area":"information","name":"Relational data model","kind":"data model","aliases":["relational model","relational database"]},{"id":"M028","area":"information","name":"Entity-relationship model","kind":"data model","aliases":["entity-relationship model","entity relationship diagram","ER diagram"]},{"id":"M029","area":"information","name":"W3C PROV provenance","kind":"provenance model / standard","aliases":["PROV-O","PROV-DM","W3C PROV"]},{"id":"M030","area":"information","name":"Data lifecycle model","kind":"lifecycle model","aliases":["data lifecycle","data life cycle"]},{"id":"M031","area":"hardware","name":"Von Neumann architecture","kind":"computer architecture","aliases":["von Neumann"]},{"id":"M032","area":"hardware","name":"Harvard architecture","kind":"computer architecture","aliases":["Harvard architecture"]},{"id":"M033","area":"hardware","name":"Flynn taxonomy","kind":"architecture taxonomy","aliases":["Flynn taxonomy","SISD","SIMD","MISD","MIMD"]},{"id":"M034","area":"hardware","name":"Memory hierarchy","kind":"computer architecture","aliases":["memory hierarchy","cache hierarchy"]},{"id":"M035","area":"hardware","name":"Instruction-set architecture","kind":"computer architecture","aliases":["instruction set architecture","ISA boundary"]},{"id":"M036","area":"hardware","name":"Cache coherence models","kind":"memory model","aliases":["cache coherence","coherence protocol"]},{"id":"M037","area":"computation","name":"Turing machines","kind":"computability model","aliases":["Turing machine"]},{"id":"M038","area":"computation","name":"Church-Turing thesis","kind":"computability thesis","aliases":["Church-Turing thesis","Church Turing thesis"]},{"id":"M039","area":"computation","name":"Lambda calculus","kind":"computability formalism","aliases":["lambda calculus"]},{"id":"M040","area":"computation","name":"Asymptotic complexity","kind":"analytical model","aliases":["Big O","big-O","O(n)","asymptotic complexity"]},{"id":"M041","area":"computation","name":"Actor model","kind":"concurrency model","aliases":["actor model"]},{"id":"M042","area":"computation","name":"Communicating sequential processes","kind":"concurrency model","aliases":["communicating sequential processes","Hoare CSP"]},{"id":"M043","area":"computation","name":"Random-access machine model","kind":"computational cost model","aliases":["random access machine","RAM model"]},{"id":"M044","area":"software","name":"Type systems","kind":"formal programming model","aliases":["type system"]},{"id":"M045","area":"software","name":"Design by contract","kind":"design principle","aliases":["design by contract","precondition","postcondition"]},{"id":"M046","area":"software","name":"Model-view-controller","kind":"software architecture","aliases":["model-view-controller","MVC"]},{"id":"M047","area":"software","name":"Software V-model","kind":"engineering lifecycle model","aliases":["V-model","V model"]},{"id":"M048","area":"software","name":"SOLID principles","kind":"design heuristic","aliases":["SOLID principles","single responsibility principle"]},{"id":"M049","area":"software","name":"Testing pyramid","kind":"testing heuristic","aliases":["testing pyramid","test pyramid"]},{"id":"M050","area":"software","name":"Language operational semantics","kind":"language semantic model","aliases":["operational semantics","denotational semantics"]},{"id":"M051","area":"os","name":"Monolithic versus microkernel","kind":"operating system architecture","aliases":["microkernel","monolithic kernel"]},{"id":"M052","area":"os","name":"Virtual memory model","kind":"operating system abstraction","aliases":["virtual memory"]},{"id":"M053","area":"os","name":"Copy-on-write","kind":"memory-management mechanism","aliases":["copy-on-write","copy on write"]},{"id":"M054","area":"os","name":"POSIX interface model","kind":"interface standard","aliases":["POSIX"]},{"id":"M055","area":"os","name":"Process lifecycle models","kind":"execution-state model","aliases":["process lifecycle","process state model"]},{"id":"M056","area":"communications","name":"OSI reference model","kind":"communication reference architecture","aliases":["OSI model","OSI reference model","seven-layer"]},{"id":"M057","area":"communications","name":"Internet protocol suite layers","kind":"communication architecture","aliases":["Internet protocol suite","TCP/IP model","TCP/IP layering"]},{"id":"M058","area":"communications","name":"Shannon-Weaver communication model","kind":"communication model","aliases":["Shannon-Weaver","Shannon Weaver"]},{"id":"M059","area":"communications","name":"CAP theorem","kind":"distributed consistency theorem","aliases":["CAP theorem","Brewer's theorem"]},{"id":"M060","area":"communications","name":"FLP impossibility","kind":"distributed computing result","aliases":["FLP impossibility","Fischer-Lynch-Paterson","asynchronous consensus impossibility"]},{"id":"M061","area":"communications","name":"Happens-before relation","kind":"distributed ordering model","aliases":["happens-before","happened-before","happened before"]},{"id":"M062","area":"communications","name":"Linearizability","kind":"consistency model","aliases":["linearizability","linearizable"]},{"id":"M063","area":"communications","name":"Paxos or Raft consensus","kind":"distributed algorithm","aliases":["Paxos","Raft consensus","Raft algorithm"]},{"id":"M064","area":"systems","name":"ISO IEC IEEE 42010 architecture descriptions","kind":"architecture description standard","aliases":["ISO/IEC/IEEE 42010","ISO 42010","IEEE 42010"]},{"id":"M065","area":"systems","name":"ISO IEC IEEE 15288 system lifecycle","kind":"engineering process standard","aliases":["ISO/IEC/IEEE 15288","ISO 15288","IEEE 15288"]},{"id":"M066","area":"systems","name":"Model-based systems engineering","kind":"engineering approach","aliases":["model-based systems engineering","MBSE"]},{"id":"M067","area":"systems","name":"Systems engineering V-model","kind":"engineering lifecycle model","aliases":["V-model","V model"]},{"id":"M068","area":"systems","name":"Reliability block diagrams","kind":"reliability model","aliases":["reliability block diagram","RBD model"]},{"id":"M069","area":"systems","name":"STPA hazard analysis","kind":"safety-analysis method","aliases":["system-theoretic process analysis","STPA"]},{"id":"M070","area":"systems","name":"Systems thinking","kind":"systems approach","aliases":["systems thinking"]},{"id":"M071","area":"human","name":"Norman seven stages of action","kind":"interaction model","aliases":["seven stages of action","seven stages of action cycle","Norman's seven"]},{"id":"M072","area":"human","name":"Cognitive load theory","kind":"cognitive model","aliases":["cognitive load theory"]},{"id":"M073","area":"human","name":"Signal detection theory","kind":"decision model","aliases":["signal detection theory","signal detection"]},{"id":"M074","area":"human","name":"Swiss cheese model","kind":"safety/human-error model","aliases":["Swiss cheese model"]},{"id":"M075","area":"human","name":"Fitts's law","kind":"human-performance model","aliases":["Fitts's law","Fitts law"]},{"id":"M076","area":"human","name":"Hick-Hyman law","kind":"human-performance model","aliases":["Hick-Hyman","Hick's law","Hick law"]},{"id":"M077","area":"human","name":"Sociotechnical systems theory","kind":"sociotechnical model","aliases":["sociotechnical systems theory","socio-technical systems","social and technical subsystems"]}]''')

def strip_fences(md: str) -> str:
    output = []
    fence = None
    for line in md.splitlines():
        marker = re.match(r"^[ \t]{0,3}(" + chr(96) + r"{3,}|~{3,})", line)
        if marker:
            hit = marker.group(1)[0]
            if fence is None:
                fence = hit
            elif fence == hit:
                fence = None
            continue
        if fence is None:
            output.append(line)
    return "\n".join(output)

def normalize(text: str) -> str:
    """Fold typographical variants without equating arbitrary concepts."""
    text = unicodedata.normalize("NFKC", text).casefold()
    for char in ("\u2010", "\u2011", "\u2012", "\u2013", "\u2014", "\u2212"):
        text = text.replace(char, "-")
    for char in ("\u2018", "\u2019", "\u02bc"):
        text = text.replace(char, "'")
    return text

def matches(body: str, aliases: list[str]) -> bool:
    body = normalize(body)
    for alias in aliases:
        term = normalize(alias)
        # Match hyphenated compound words even when written with spaces.
        escaped = re.escape(term).replace(r"\ ", r"[ -]+").replace(r"\-", r"[ -]+")
        needle = r"(?<![a-z0-9_])" + escaped + r"(?![a-z0-9_])"
        if re.search(needle, body):
            return True
    return False

def main() -> None:
    corpus = {}
    for directory, area in AREAS.items():
        subdir = ROOT / directory
        assert subdir.is_dir(), f"Expected approved area directory: {directory}"
        for path in sorted(subdir.glob("*.md")):
            if path.name == "README.md":
                continue
            corpus[path.relative_to(ROOT).as_posix()] = {
                "area": area,
                "body": strip_fences(path.read_text(encoding="utf-8")),
            }
    observations = []
    for item in CATALOG:
        found = [p for p, record in corpus.items() if matches(record["body"], item["aliases"])]
        found_here = [p for p in found if corpus[p]["area"] == item["area"]]
        observations.append((item, found, found_here))
    positive = sum(bool(found) for _, found, _ in observations)
    local = sum(bool(found_here) for _, _, found_here in observations)
    print(f"ARTICLES_SCANNED={len(corpus)}")
    print(f"AREAS_SCANNED={len(AREAS)}")
    print(f"NAMED_MODELS_SCANNED={len(CATALOG)}")
    print(f"MENTIONED_SOMEWHERE={positive}")
    print(f"MENTIONED_IN_EXPECTED_AREA={local}")
    print(f"NO_LEXICAL_MENTION={len(CATALOG)-positive}")
    print("INTERPRETATION=Lexical evidence only; no mention does not prove missing treatment; mention does not prove substantive, correct, or source-verified explanation.")
    print("ID | AREA | NAME | TYPE | ARTICLE_HITS | AREA_HITS | EXAMPLE_ARTICLES")
    for item, found, found_here in observations:
        titles = ",".join(p.removesuffix(".md").split("/")[-1] for p in found[:4])
        print(f"{item['id']} | {item['area']} | {item['name']} | {item['kind']} | {len(found)} | {len(found_here)} | {titles}")
    print("END_MODEL_AUDIT")
if __name__ == "__main__":
    main()
