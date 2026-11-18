#!/usr/bin/env python3
"""Validate the *current* Fundamentals inventory without freezing its subject count.

- Area inventories, tracked IDs/statuses, and canonical ownership are reconciled.
- Reviewed articles must exist. Inventoried entries must not masquerade as articles.
- Historical wave audit denominators are not treated as the current total.
Run: python3 foundations/fundamentals/tools/check_inventory.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AREAS = (
    "mathematics-logic",
    "scientific-analytical-reasoning",
    "models-abstraction",
    "physical-electrical-principles",
    "information-data",
    "digital-systems-hardware",
    "computation-algorithms",
    "software-programming",
    "operating-system-principles",
    "communication-distributed-systems",
    "systems-engineering",
    "human-sociotechnical-systems",
)
AREA_HEADER = re.compile(r"^### (\d\d)\. (.+?) \(Wave")
ROW = re.compile(r"^\| (F-\d\d-\d\d) \|")
OWNER = re.compile(r"^\| \*\*(.+?)\*\*(?: \(F-\d\d-\d\d; (?:Inventoried|Draft|Reviewed)\))? \|")
ARTICLE = re.compile(r"\[Reviewed article\]\(([^)]+)\)")
INVENTORY = re.compile(r"^## (?:Approved Subject Inventory|Subject Inventory \(versioned\))$")


def normal(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


def inventory_names(body: str) -> list[str]:
    lines = body.splitlines()
    start = next((i for i, s in enumerate(lines) if INVENTORY.match(s)), None)
    if start is None:
        raise ValueError("Area has no recognized subject inventory")
    names = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        if not line.startswith("- "):
            continue
        name = line[2:].strip()
        name = re.sub(r"\s*\(Inventoried;.*$", "", name)
        names.append(name.strip("* "))
    return names


def main() -> int:
    problems = []
    register = (ROOT / "DEVELOPMENT-VERIFICATION-REGISTER.md").read_text(encoding="utf-8")
    groups = {}
    area = None
    for line in register.splitlines():
        h = AREA_HEADER.match(line)
        if h:
            area = int(h.group(1))
            groups.setdefault(area, [])
            continue
        match = ROW.match(line)
        if match and area is not None:
            fields = [p.strip() for p in line.strip().strip("|").split("|")]
            if len(fields) < 6:
                problems.append(f"Invalid tracker row: {line[:120]}")
                continue
            groups[area].append({
                "id": fields[0], "name": fields[1],
                "canonical": fields[2], "status": fields[3].strip("* "),
                "source": fields[4].strip("* "),
            })
    ids = [r["id"] for rows in groups.values() for r in rows]
    if len(ids) != len(set(ids)):
        problems.append("Duplicate tracker ID")
    if len(groups) != len(AREAS):
        problems.append(f"Expected {len(AREAS)} known area groups, found {len(groups)}")
    reviewed = inventoried = other = 0
    for number, folder in enumerate(AREAS, 1):
        rows = groups.get(number, [])
        try:
            names = inventory_names((ROOT / folder / "README.md").read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            problems.append(f"{folder}: {error}")
            continue
        expected = [normal(r["name"]) for r in rows]
        actual = [normal(n) for n in names]
        if actual != expected:
            problems.append(f"{folder}: subject name/order mismatch: register {expected}; area README {actual}")
        for row in rows:
            if row["id"][:4] != f"F-{number:02d}":
                problems.append(f"{row['id']}: tracker ID not in area {number}")
            if row["status"] == "Reviewed":
                reviewed += 1
                m = ARTICLE.search(row["canonical"])
                if not m:
                    problems.append(f"{row['id']}: Reviewed missing canonical file link")
                elif not (ROOT / m.group(1)).is_file():
                    problems.append(f"{row['id']}: missing article {m.group(1)}")
                if row["source"] != "Core claims checked":
                    problems.append(f"{row['id']}: Reviewed article source state is {row['source']}")
            elif row["status"] == "Inventoried":
                inventoried += 1
                if "Article not authored" not in row["canonical"] or row["source"] != "Not reviewed":
                    problems.append(f"{row['id']}: Inventoried row misleadingly claims article/source review")
            elif row["status"] in {"Draft", "Scoped", "Researched", "Pilot queued"}:
                other += 1
            else:
                problems.append(f"{row['id']}: unknown development state: {row['status']!r}")
    owners = (ROOT / "CANONICAL-OWNERSHIP-REGISTER.md").read_text(encoding="utf-8")
    owner_names = [normal(m.group(1)) for line in owners.splitlines()
                   if (m := OWNER.match(line))]
    tracker_names = [normal(r["name"]) for rows in groups.values() for r in rows]
    if len(owner_names) != len(tracker_names) or sorted(owner_names) != sorted(tracker_names):
        problems.append("Ownership register names or counts do not match tracked subjects")
    main_index = (ROOT / "README.md").read_text(encoding="utf-8")
    total_match = re.search(r"^\| \*\*Total\*\* \| \*\*12 knowledge areas\*\* \| \*\*(\d+) subject headings", main_index, re.M)
    if total_match is None or int(total_match.group(1)) != len(ids):
        problems.append("Main index total does not equal tracking register total")
    print(f"KNOWLEDGE_AREAS={len(groups)}")
    print(f"CURRENT_SUBJECTS={len(ids)}")
    print(f"REVIEWED={reviewed}")
    print(f"INVENTORIED={inventoried}")
    print(f"OTHER_STATES={other}")
    print(f"OWNERSHIP_RECORDS={len(owner_names)}")
    print(f"INVENTORY_ERRORS={len(problems)}")
    for p in problems:
        print(f"ERROR {p}")
    print("LIMIT: Structural/state consistency only, not article correctness, publication approval, or independent review.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
