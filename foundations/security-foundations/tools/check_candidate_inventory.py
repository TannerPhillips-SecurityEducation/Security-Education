#!/usr/bin/env python3
"""Validate the *flexible* Security Foundations candidate inventory and pilot records.

This check deliberately has NO hardcoded area/subject/pilot count.
An approved DIVISION does not imply approved internal taxonomy or published content.
Does not check factual accuracy, external links, or independent source verification.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "SUBJECT-INVENTORY-PROPOSAL.md"
PILOT_INDEX = ROOT / "pilots" / "README.md"
AREA = re.compile(r"^### (SF-\d{2})\. .+? \((\d+) candidates\)\s*$")
SUBJECT = re.compile(r"^\| (SF-\d{2}-\d{2}) \| ([^|]+) \| ([^|]+) \|$")
PILOT = re.compile(r"^\| (SF-\d{2}-\d{2}) \| \[([^\]]+)\]\(([^)]+\.md)\) \| \*\*(Draft|Reviewed \(model-assisted\))\*\* \| ([^|]+) \|", re.M)

def main() -> int:
    errors: list[str] = []
    text = INVENTORY.read_text(encoding="utf-8")
    if "## Proposed subject headings" not in text or "## Established-model grounding" not in text:
        errors.append("Missing candidate inventory boundaries")
        body = text
    else:
        body = text.split("## Proposed subject headings", 1)[1].split("## Established-model grounding", 1)[0]
    counts: dict[str, int] = {}
    expected: dict[str, int] = {}
    ids: list[str] = []
    current_area = None
    for line in body.splitlines():
        m = AREA.match(line)
        if m:
            current_area = m.group(1)
            expected[current_area] = int(m.group(2))
            counts.setdefault(current_area, 0)
            continue
        m = SUBJECT.match(line)
        if not m:
            continue
        id_ = m.group(1)
        ids.append(id_)
        area = "SF-" + id_.split("-")[1]
        counts[area] = counts.get(area, 0) + 1
        if current_area != area:
            errors.append(f"{id_} belongs to {area} but appears in {current_area}")
    if not ids:
        errors.append("Candidate inventory has zero subjects")
    if len(ids) != len(set(ids)):
        errors.append("Duplicate candidate IDs")
    for area, declared in expected.items():
        if counts.get(area) != declared:
            errors.append(f"{area}: declared {declared} active subjects, found {counts.get(area)}")
    for area in set(counts) - set(expected):
        errors.append(f"{area}: has subjects without a declared area")
    pilots = PILOT_INDEX.read_text(encoding="utf-8")
    pilot_rows = PILOT.findall(pilots)
    pilot_ids = [r[0] for r in pilot_rows]
    if not pilot_rows or len(pilot_ids) != len(set(pilot_ids)):
        errors.append("Pilot index has no pilot rows or duplicate IDs")
    active = set(ids)
    for id_, title, rel, state, source_state in pilot_rows:
        if id_ not in active:
            errors.append(f"{id_}: pilot points to inactive/retired subject candidate")
        path = PILOT_INDEX.parent / rel
        if not path.is_file():
            errors.append(f"{id_}: missing pilot manuscript {rel}")
            continue
        body = path.read_text(encoding="utf-8")
        if not re.search(rf"^\*\*Candidate subject:\*\* {re.escape(id_)}", body, re.M):
            errors.append(f"{id_}: manuscript candidate ID mismatch")
        if not re.search(r"^\*\*Development state:\*\* "+re.escape(state), body, re.M):
            errors.append(f"{id_}: manuscript status inconsistent with index")
        if len(re.findall(r"^##\s+", body, re.M)) < 5:
            errors.append(f"{id_}: fewer than five substantive sections")
        if not re.search(r"^## .*?(?:source|reference)",body,re.I|re.M):
            errors.append(f"{id_}: expected source/references section absent")
    print(f"WORKING_AREAS={len(expected)}")
    print(f"WORKING_CANDIDATES={len(ids)}")
    print(f"PILOT_ARTICLES={len(pilot_rows)}")
    print(f"PILOTS_DRAFT={sum(r[3]=='Draft' for r in pilot_rows)}")
    print(f"PILOTS_REVIEWED={sum(r[3]=='Reviewed (model-assisted)' for r in pilot_rows)}")
    print(f"INVENTORY_ERRORS={len(errors)}")
    for error in errors:
        print(f"ERROR {error}")
    print("LIMIT: inventory, links, states and simple article structure only; this is not technical or source review.")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
