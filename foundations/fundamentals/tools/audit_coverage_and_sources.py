#!/usr/bin/env python3
"""Non-gating diagnostic for article traceability, graph edges and candidate gaps.

Read-only. All 116 current canonical articles are discovered from the development
register, not hardcoded. A lexical hit is not proof of sufficient knowledge and
a non-hit is not proof of an absent concept. Source hyperlinks are NOT verified
for semantic support or availability.
"""
from __future__ import annotations

import collections
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
REGISTER = ROOT / "DEVELOPMENT-VERIFICATION-REGISTER.md"
DOMAINS = ("network", "endpoint", "application", "cloud", "industrial", "iot", "identity")
CANONICAL = re.compile(r"^\| (F-\d\d-\d\d) \| ([^|]+) \| \[Reviewed article\]\(([^)]+)\) \|")
URL = re.compile(r"!?\[([^\]]+)\]\((https?://[^)\s]+)\)")
LOCAL = re.compile(r"!?\[([^\]]+)\]\(([^)\s]+)\)")
SOURCE_START = re.compile(
    r"^#{2,3}\s+(?:Sources(?: and .*)?|References(?: and .*)?|"
    r"Authoritative reference starting points|Primary reference starting points|"
    r"Sources and limitations|Canonical relationships and references|"
    r"Source orientation and applicability)\s*$", re.I)
REVIEW_LINE = re.compile(r"(?:^\*\*Source review:\*\*|\bsource-level verified\b|\bcore claims checked\b)", re.I)

# These are *probes*, not proposed automatic taxonomy additions.
# Keep technical prerequisites distinct from application/security implementations.
PROBES = (
 ("calculus_derivatives","Mathematics / Physical / Systems","calculus;derivative;differentiation;differential equation;integral"),
 ("differential_dynamics","Mathematics / Systems","differential equation;dynamical system;state-space model;state space model;ordinary differential equation"),
 ("numerical_methods","Mathematics / Computation","numerical method;numerical analysis;conditioning;convergence;floating-point error;rounding error"),
 ("optimization","Mathematics / Computation","optimization;linear programming;constrained optimization;gradient descent;objective function"),
 ("combinatorics","Mathematics / Algorithms","combinatorics;combinatorial;counting principle;permutation;combination"),
 ("queueing","Systems / Communication / OS","queueing theory;queuing theory;little's law;queue depth;utilization law"),
 ("stochastic_processes","Mathematics / Models","markov chain;markov process;stochastic process;poisson process"),
 ("formal_languages","Models / Computation / Software","formal language;context-free grammar;automata;parser;regular language"),
 ("proof_model_checking","Models / Software / Engineering","model checking;formal verification;invariant;temporal logic;proof obligation"),
 ("search_information_retrieval","Information / Computation","information retrieval;inverted index;tf-idf;bm25;full-text search;search ranking;query optimization"),
 ("search_semantics","Information / Software","regex search;fuzzy search;proximity search;field matching;full-text search;regular expression"),
 ("semantic_interoperability","Information / Software / Communication","semantic interoperability;schema evolution;semantic mapping;data contract"),
 ("complexity_emergence","Systems / Science","emergence;complex adaptive;nonlinear feedback;phase transition"),
 ("causal_modeling","Scientific Reasoning / Models","structural causal model;causal inference;causal graph;confounder;counterfactual"),
 ("signal_fourier","Physical / Mathematics","fourier transform;fourier analysis;frequency domain;spectral analysis;filter"),
 ("control_pid","Systems / Physical","PID;proportional integral derivative;closed loop;controllability;observability"),
 ("reliability_fault_tree","Systems / Engineering","fault tree;failure mode;fmea;reliability block;hazard analysis"),
 ("human_signal_detection","Human / Scientific","signal detection theory;false alarm;miss rate;decision criterion;cognitive load"),
 ("distributed_consistency","Communication / Computation","linearizability;consensus;cap theorem;partial failure;partition tolerance"),
 ("virtualization","OS / Hardware / Cloud","virtual machine;virtualization;hypervisor;containerization;namespaces"),
 ("event_oriented_models","Models / Scientific / Information","event sourcing;event-oriented;event driven;temporal model;event record"),
 ("data_quality","Information / Scientific","missing data;data quality;data validation;provenance;bias;measurement uncertainty"),
)

def normalized(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).casefold()
    for ch in ("‐","‑","‒","–","—","−"):
        text = text.replace(ch, "-")
    for ch in ("‘","’"):
        text = text.replace(ch, "'")
    return text

def clean_line(line: str) -> str:
    # Drop link text as well as URLs to avoid calling bibliographic mention a concept explanation.
    line = re.sub(r"!?\[[^\]]*\]\([^)]+\)", "", line)
    line = re.sub(r"\x60[^\x60]+\x60", "", line)
    return line

def body_parts(raw: str) -> tuple[str,str]:
    body, bibliography = [], []
    in_fence, in_reference = False, False
    for line in raw.splitlines():
        if re.match(r"^\s*(?:\x60{3,}|~{3,})",line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if SOURCE_START.match(line.strip()):
            in_reference=True
        (bibliography if in_reference else body).append(line)
    return "\n".join(body), "\n".join(bibliography)

def matches(body: str, terms: list[str]) -> bool:
    b = normalized(body)
    for term in terms:
        t = normalized(term)
        pattern = r"(?<![a-z0-9_])" + re.escape(t).replace(r"\ ","[ -]+").replace(r"\-","[ -]+") + r"(?![a-z0-9_])"
        if re.search(pattern,b):
            return True
    return False

def main() -> None:
    reg = REGISTER.read_text(encoding="utf-8")
    subject_rows = [(a,b.strip(),c) for a,b,c in CANONICAL.findall(reg)]
    if not subject_rows or len({x[0] for x in subject_rows}) != len(subject_rows):
        raise SystemExit("Unresolved or duplicate subject rows")
    docs=[]
    for id_, name, rel in subject_rows:
        path=ROOT/rel
        raw=path.read_text(encoding="utf-8")
        body, bibliography=body_parts(raw)
        # bibliography *can* start late, but this is a heuristic that must not be
        # interpreted as proof of source placement.
        external_body=URL.findall(body)
        external_biblio=URL.findall(bibliography)
        external_all=URL.findall(raw)
        internal=LOCAL.findall(raw)
        domains=set()
        for label, href in internal:
            if href.startswith(("http://","https://")):
                continue
            resolved=(path.parent / href.split("#")[0]).resolve()
            for domain in DOMAINS:
                try:
                    resolved.relative_to(REPO/domain)
                    domains.add(domain)
                except ValueError: pass
        headings=sum(bool(re.match(r"^##\s+",ln)) for ln in raw.splitlines())
        example=bool(re.search(r"^#{2,3}\s+.*(?:worked|example|illustrat|demonstrat)",raw,re.I|re.M))
        docs.append({"id":id_,"name":name,"path":rel,"raw":raw,
                     "body":clean_line(body),"body_raw":body, "bib":bibliography,
                     "body_words":len(re.findall(r"\b[\w'-]+\b",body)),
                     "all_sources":len(external_all), "bib_sources":len(external_biblio),
                     "inline_sources":len(external_body),"unique_source_hosts":len(set(urlsplit(u).hostname for _,u in external_all)),
                     "external_domains":set(urlsplit(u).hostname for _,u in external_all),
                     "domain_links":domains,"headings":headings,"worked":example})
    print(f"ARTICLES_ANALYZED={len(docs)}")
    print(f"AREA_COUNT={len({d['path'].split('/')[0] for d in docs})}")
    print(f"ARTICLES_WITH_ZERO_EXTERNAL_SOURCES={sum(d['all_sources']==0 for d in docs)}")
    print(f"ARTICLES_WITH_ZERO_INLINE_SOURCE_LINKS={sum(d['inline_sources']==0 for d in docs)}")
    print(f"ARTICLES_WITH_ZERO_BIBLIOGRAPHIC_LINKS={sum(d['bib_sources']==0 for d in docs)}")
    print(f"ARTICLES_WITH_WORKED_HEADING={sum(d['worked'] for d in docs)}")
    print(f"ARTICLES_WITH_SPECIALIZED_DOMAIN_LINK={sum(bool(d['domain_links']) for d in docs)}")
    print(f"TOTAL_EXTERNAL_LINK_OCCURRENCES={sum(d['all_sources'] for d in docs)}")
    print(f"TOTAL_INLINE_SOURCE_LINK_OCCURRENCES={sum(d['inline_sources'] for d in docs)}")
    print(f"UNIQUE_EXTERNAL_SOURCE_HOSTS={len(set.union(set(),*(d['external_domains'] for d in docs)))}")
    for domain in DOMAINS:
        print(f"SPECIALIZED_DOMAIN_{domain.upper()}_LINKED_FROM_ARTICLES={sum(domain in d['domain_links'] for d in docs)}")
    print("LOW_TRACEABILITY_ARTICLES: id | path | inline links | bibliography links | headings | words")
    for d in docs:
        if d["inline_sources"] <= 1:
            print(f"LOWTRACE | {d['id']} | {d['path']} | {d['inline_sources']} | {d['bib_sources']} | {d['headings']} | {d['body_words']}")
    print("PROBE: topic | intended areas | articles_with_nonbibliographic_text_match | sample article IDs")
    for name, areas, spec in PROBES:
        terms=spec.split(";")
        found=[d for d in docs if matches(d["body"],terms)]
        print(f"PROBE | {name} | {areas} | {len(found)} | {','.join(d['id'] for d in found[:12])}")
    print("EXTERNAL_HOSTS: host | occurrences")
    counter=collections.Counter(urlsplit(url).hostname for d in docs for _,url in URL.findall(d['raw']))
    for host,n in counter.most_common(22):
        print(f"HOST | {host} | {n}")
    print("LIMITATIONS=Source count is not evidence of support. Link presence is not conceptual dependency correctness. Probes are nonexhaustive and are not gap verdicts. Some inline citations may be missed by simplistic Markdown parsing.")
    print("END_COVERAGE_AUDIT")

if __name__ == "__main__":
    main()
