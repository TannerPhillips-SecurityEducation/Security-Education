#!/usr/bin/env python3
"""Dynamic, non-gating architecture/content coverage inventory.

This reports file presence and development labels, not conceptual completeness,
source correctness, human review, publication or an immutable coverage target.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DOMAINS=("network","endpoint","application","cloud","industrial","iot","identity")
FUNDAMENTALS=ROOT/"foundations"/"fundamentals"
SECURITY=ROOT/"foundations"/"security-foundations"
OPS=ROOT/"foundations"/"operational-foundations"

def canonical_articles():
    p=FUNDAMENTALS/"DEVELOPMENT-VERIFICATION-REGISTER.md"
    r=p.read_text(encoding="utf-8")
    rows=re.findall(r"^\| (F-\d\d-\d\d) \| ([^|]+) \| \[Reviewed article\]\(([^)]+)\) \| ([^|]+) \|",r,re.M)
    return rows

def security_candidates():
    t=(SECURITY/"SUBJECT-INVENTORY-PROPOSAL.md").read_text(encoding="utf-8")
    body=t.split("## Proposed subject headings",1)[1].split("## Established-model grounding",1)[0]
    return re.findall(r"^\| (SF-\d\d-\d\d) \|",body,re.M)

def pilot_rows():
    t=(SECURITY/"pilots/README.md").read_text(encoding="utf-8")
    return re.findall(r"^\| (SF-\d\d-\d\d) \| \[[^\]]+\]\(([^)]+)\) \| \*\*(.*?)\*\* \|",t,re.M)

def main():
    refs=canonical_articles();candidates=security_candidates();pilots=pilot_rows()
    md_files=list(ROOT.rglob("*.md"))
    print(f"MARKDOWN_FILES={len(md_files)}")
    print(f"FOUNDATIONS_DIVISIONS={sum((p/'README.md').is_file() for p in (FUNDAMENTALS,SECURITY,OPS))}")
    print(f"FUNDAMENTALS_CANONICAL_REGISTER_ROWS={len(refs)}")
    print(f"FUNDAMENTALS_REGISTER_IDS_UNIQUE={len({r[0] for r in refs})}")
    print(f"FUNDAMENTALS_REGISTER_ARTICLE_PATHS_PRESENT={sum((FUNDAMENTALS/r[2]).is_file() for r in refs)}")
    print(f"SECURITY_WORKING_SUBJECT_CANDIDATES={len(candidates)}")
    print(f"SECURITY_CANDIDATE_IDS_UNIQUE={len(set(candidates))}")
    area_index_files=[p for p in SECURITY.glob("*/README.md") if "**Working area ID:**" in p.read_text(encoding="utf-8")]
    real_area_articles=[p for d in area_index_files for p in d.glob("*.md") if p.name != "README.md"]
    print(f"SECURITY_WORKING_AREA_DIRECTORIES={len(area_index_files)}")
    print(f"SECURITY_SUBSTANTIVE_AREA_ARTICLES={len(real_area_articles)}")
    print(f"SECURITY_HISTORICAL_PILOT_REVIEW_LINKS={len(pilots)}")
    print(f"SECURITY_INVENTORIED_UNAUTHORED={len(candidates)-len(real_area_articles)}")
    print(f"SECURITY_PILOT_ARTICLES={len(pilots)}")  # historical review register; do not count aliases as substantive files
    print(f"SECURITY_PILOTS_REVIEWED_MODEL_ASSISTED={sum('Reviewed' in r[2] for r in pilots)}")
    print(f"SECURITY_CANDIDATES_WITHOUT_PILOT={len(set(candidates)-{r[0] for r in pilots})}")
    print(f"OPERATIONAL_SUBSTANTIVE_ARTICLES={len([p for p in OPS.glob('*.md') if p.name not in {'README.md','AGENTS.md'}])}")
    print(f"SPECIALIZED_DOMAINS={len(DOMAINS)}")
    for d in DOMAINS:
        root=ROOT/d
        nav=list(root.glob("*/README.md"))
        body=[p for p in root.rglob("*.md") if p.name not in {"README.md","AGENTS.md"}]
        print(f"DOMAIN_{d.upper()}_NAV_INDEXES={len(nav)}")
        print(f"DOMAIN_{d.upper()}_SUBSTANTIVE_ARTICLES={len(body)}")
    print("LIMIT: A missing pilot is not necessarily a knowledge gap; file counts are not scientific completeness.")
    print("LIMIT: No publication, source passage, safety, security efficacy, or qualified human review is asserted.")

if __name__=="__main__": main()
