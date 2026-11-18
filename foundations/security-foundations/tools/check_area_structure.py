#!/usr/bin/env python3
"""Dynamic Security Foundations area/README/article integrity.

Validates the user-adopted Fundamentals-style directory PATTERN while treating
all area names, subject IDs, and counts as a living working inventory. This
does not approve the proposed taxonomy, verify sources or certify publication.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INV=ROOT/"SUBJECT-INVENTORY-PROPOSAL.md"
REG=ROOT/"DEVELOPMENT-VERIFICATION-REGISTER.md"
OWNER=ROOT/"CANONICAL-OWNERSHIP-REGISTER.md"
PILOT=ROOT/"pilots/README.md"
RELOCATION=ROOT/"AREA-STRUCTURE-ADJUDICATION-03.md"  # dated evidence of original flat-pilot relocations
HISTORICAL_ROW=re.compile(r"^\| (SF-\d{2}-\d{2}) \| \[Pilot alias\]\(pilots/([^)]+\.md)\) \|", re.M)
AREA_HEAD=re.compile(r"^### (SF-\d{2})\. (.+?) \((\d+) candidates\)$")
SUBJECT=re.compile(r"^\| (SF-\d{2}-\d{2}) \| ([^|]+) \| ([^|]+) \|$")
AREA_ROW=re.compile(r"^\| (SF-\d{2}-\d{2}) \| (.+?) \| (.+?) \| (.+?) \|$")
PILOT_ROW=re.compile(r"^\| (SF-\d{2}-\d{2}) \| \[([^\]]+)\]\(([^)]+\.md)\) \| \*\*(Reviewed \(model-assisted\)|Draft)\*\* \| ([^|]+) \|")
ID_RE=re.compile(r"^\*\*Candidate subject:\*\* (SF-\d{2}-\d{2})", re.M)
LOCATION=re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
AREA_MARK=re.compile(r"^\*\*Working area ID:\*\* (SF-\d{2})\b", re.M)

def main():
    errors=[]
    src=INV.read_text(encoding="utf-8")
    if "## Proposed subject headings" not in src or "## Established-model grounding" not in src:
        raise SystemExit("ERROR: missing candidate inventory boundaries")
    src=src.split("## Proposed subject headings",1)[1].split("## Established-model grounding",1)[0]
    by_area={};declared={};current=None
    for line in src.splitlines():
        a=AREA_HEAD.match(line)
        if a:
            current=a.group(1)
            if current in by_area: errors.append(f"duplicate working area {current}")
            by_area[current]=[];declared[current]=int(a.group(3))
        s=SUBJECT.match(line)
        if s:
            id_=s.group(1)
            if current is None or not id_.startswith(current+"-"):
                errors.append(f"orphan/misplaced inventory row {id_}")
            else: by_area[current].append(id_)
    for area,ids in by_area.items():
        if len(ids)!=declared[area] or len(ids)!=len(set(ids)):
            errors.append(f"{area}: declared count/unique ID mismatch")
    all_ids={id_ for ids in by_area.values() for id_ in ids}
    active={};actual_articles={}
    for d in ROOT.iterdir():
        if not d.is_dir() or not (d/"README.md").is_file():
            continue
        readme=(d/"README.md").read_text(encoding="utf-8")
        m=AREA_MARK.search(readme)
        if not m: continue  # historical pilots or auxiliary dirs
        area=m.group(1)
        if area in active: errors.append(f"duplicate area README ID {area}")
        active[area]=d
        if area not in by_area:
            errors.append(f"unregistered provisional area {area}: {d.name}")
            continue
        rows={}
        for line in readme.splitlines():
            hit=AREA_ROW.match(line)
            if hit: rows[hit.group(1)]=(hit.group(2),hit.group(3),hit.group(4))
        if set(rows)!=set(by_area[area]):
            errors.append(f"{area}: area README IDs disagree with active working inventory")
        for id_,(label,state,scope) in rows.items():
            if "Reviewed (model-assisted)" not in state and "Draft" not in state:
                if "Inventoried" not in state:
                    errors.append(f"{id_}: invalid un-authored state: {state}")
                continue
            links=LOCATION.findall(label)
            if len(links)!=1:
                errors.append(f"{id_}: working article row requires one real article link")
                continue
            target=(d/links[0][1]).resolve()
            if target.parent!=d.resolve() or not target.is_file() or target.name=="README.md":
                errors.append(f"{id_}: missing/misplaced working article: {links[0][1]}")
                continue
            body=target.read_text(encoding="utf-8")
            id_match=ID_RE.search(body)
            if not id_match or id_match.group(1)!=id_:
                errors.append(f"{id_}: candidate-ID frontmatter mismatch")
            if not re.search(r"^\*\*Development state:\*\* (?:Reviewed \(model-assisted\)|Draft)",body,re.M):
                errors.append(f"{id_}: working article missing development review state")
            if id_ in actual_articles: errors.append(f"{id_}: duplicate substantive owner")
            actual_articles[id_]=target
        for article in d.glob("*.md"):
            if article.name=="README.md": continue
            if article not in actual_articles.values():
                errors.append(f"unregistered article in {d.name}: {article.name}")
    if set(active)!=set(by_area):
        errors.append(f"area directory IDs differ: missing={sorted(set(by_area)-set(active))}, extras={sorted(set(active)-set(by_area))}")
    if not actual_articles:
        errors.append("no actual substantive area article files found")
    # Register and historical review index must point to the substantive area file,
    # not to a legacy flat-pilot alias.
    register=REG.read_text(encoding="utf-8")
    owner=OWNER.read_text(encoding="utf-8")
    reg_rows={}
    for line in register.splitlines():
        if re.match(r"^\| SF-\d{2}-\d{2} \|",line):
            cols=[s.strip() for s in line.strip().strip("|").split("|")]
            if len(cols)>=6: reg_rows[cols[0]]=cols
    own_ids=set(re.findall(r"^\| (SF-\d{2}-\d{2}) \|",owner,re.M))
    if set(reg_rows)!=all_ids: errors.append("development register IDs differ from inventory")
    if own_ids!=all_ids: errors.append("working ownership IDs differ from inventory")
    for id_,cols in reg_rows.items():
        authored=id_ in actual_articles
        if authored:
            if "Reviewed" not in cols[3] and "Draft" not in cols[3]:
                errors.append(f"{id_}: register omits authored state")
            links=LOCATION.findall(cols[2])
            if len(links)!=1 or (ROOT/links[0][1]).resolve()!=actual_articles[id_]:
                errors.append(f"{id_}: development register article target mismatch")
        elif "Inventoried" not in cols[3]:
            errors.append(f"{id_}: un-authored register state not Inventoried")
    # Only articles actually relocated from the former flat pilots directory
    # have historical aliases. An area-first Draft may later become Reviewed
    # without ever having had a historical pilots/<filename>.md URL.
    historical_rows=HISTORICAL_ROW.findall(RELOCATION.read_text(encoding="utf-8"))
    historical_aliases=dict(historical_rows)
    if len(historical_aliases)!=len(historical_rows):
        errors.append("historical relocation record contains duplicate subject IDs")
    if set(historical_aliases)-set(actual_articles):
        errors.append("historical relocation record refers to missing area articles")
    aliases=0;pilots=0;seen_pilots=set()
    for line in PILOT.read_text(encoding="utf-8").splitlines():
        m=PILOT_ROW.match(line)
        if not m: continue
        pilots+=1
        id_,_,rel,_,_=m.groups()
        if id_ in seen_pilots:
            errors.append(f"duplicate pilot register entry: {id_}")
        seen_pilots.add(id_)
        target=(PILOT.parent/rel).resolve()
        if id_ not in actual_articles or target!=actual_articles.get(id_):
            errors.append(f"pilot register target for {id_} is not the working area article")
        if id_ in historical_aliases:
            # Preserve the *actual old path* captured by the dated relocation map,
            # not a guessed alias based on current review status or filename.
            alias=PILOT.parent/historical_aliases[id_]
            if not alias.is_file():
                errors.append(f"{id_}: documented historical pilot alias missing: {alias.name}")
            else:
                txt=alias.read_text(encoding="utf-8")
                if "Historical pilot path retained for link compatibility" not in txt:
                    errors.append(f"{id_}: former pilot path still contains substantive body")
                aliases+=1
    if seen_pilots!=set(actual_articles):
        errors.append(f"working article register differs: missing={sorted(set(actual_articles)-seen_pilots)}, extras={sorted(seen_pilots-set(actual_articles))}")
    if pilots!=len(actual_articles): errors.append(f"pilot register has {pilots} rows; {len(actual_articles)} articles exist")
    print(f"WORKING_AREA_DIRECTORIES={len(active)}")
    print(f"WORKING_CANDIDATES={len(all_ids)}")
    print(f"WORKING_SUBSTANTIVE_ARTICLES={len(actual_articles)}")
    print(f"INVENTORIED_WITHOUT_ARTICLE={len(all_ids)-len(actual_articles)}")
    print(f"HISTORICAL_NAVIGATION_ALIASES={aliases}")
    print(f"DEVELOPMENT_REGISTER_ROWS={len(reg_rows)}")
    print(f"WORKING_OWNERSHIP_ROWS={len(own_ids)}")
    print(f"AREA_STRUCTURE_ERRORS={len(errors)}")
    for e in errors: print("ERROR "+e)
    print("LIMIT: structure/identity/status only; area and subject taxonomy provisional; no factual or publication claims.")
    return 1 if errors else 0

if __name__=="__main__": sys.exit(main())
