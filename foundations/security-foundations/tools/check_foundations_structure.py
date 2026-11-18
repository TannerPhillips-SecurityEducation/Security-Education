#!/usr/bin/env python3
"""Security Foundations source-tree and pilot integrity check.

This verifies a *versioned working proposal*; it does not approve the number of
areas, subjects, article taxonomy, technical correctness or publication.
The counts are discovered from the current repository rather than hardcoded.
Run from anywhere: python3 foundations/security-foundations/tools/check_foundations_structure.py
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "SUBJECT-INVENTORY-PROPOSAL.md"
CROSS = ROOT / "ESTABLISHED-MODEL-CROSSWALK.md"
BOUNDS = ROOT / "OWNERSHIP-BOUNDARIES.md"
PILOTS = ROOT / "pilots" / "README.md"
INDEX = ROOT / "README.md"

ACTIVE_ROW = re.compile(r"^\| (SF-\d\d-\d\d) \| ([^|]+) \| ([^|]+) \|$")
AREA = re.compile(r"^### SF-(\d\d)\. (.+?) \((\d+) candidates\)$")
PILOT_ROW = re.compile(
    r"^\| (SF-\d\d-\d\d) \| \[([^\]]+)\]\(([^)]+\.md)\) \| (.*?) \| (.*?) \|")
SOURCE = re.compile(r"^\| (R-\d\d) [^|]+ \|")
BOUNDARY = re.compile(r"^\| (B-\d\d):")
MD_LINK = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
FRAGMENT_RE = re.compile(r"[^\w\s-]", re.UNICODE)


def markdown_slugs(body: str) -> set[str]:
    seen = collections.Counter()
    result = set()
    for line in body.splitlines():
        m = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?\s*$", line)
        if m is None:
            continue
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip().lower()
        title = title.replace("**", "").replace("\x60", "")
        title = FRAGMENT_RE.sub("", title)
        slug = re.sub(r"\s+", "-", title)
        duplicate = seen[slug]
        if duplicate:
            result.add(f"{slug}-{duplicate}")
        else:
            result.add(slug)
        seen[slug] += 1
    return result


def main() -> int:
    issues = []
    raw = INV.read_text(encoding="utf-8")
    if "## Proposed subject headings" not in raw or "## Established-model grounding" not in raw:
        issues.append("Missing candidate inventory section boundaries")
        active_section = ""
    else:
        active_section = raw.split("## Proposed subject headings", 1)[1].split("## Established-model grounding", 1)[0]
    counts = {}
    active = {}
    area = None
    for line in active_section.splitlines():
        h = AREA.match(line)
        if h:
            area = h.group(1)
            if area in counts:
                issues.append(f"Duplicate area SF-{area}")
            counts[area] = {"expected": int(h.group(3)), "name": h.group(2), "ids": []}
        m = ACTIVE_ROW.match(line)
        if m:
            id_, name, scope = m.groups()
            if id_ in active:
                issues.append(f"Duplicate active subject ID {id_}")
            active[id_] = (name.strip(), scope.strip())
            if area is None:
                issues.append(f"Subject outside area {id_}")
            else:
                counts[area]["ids"].append(id_)
                if not id_.startswith(f"SF-{area}-"):
                    issues.append(f"{id_} belongs under incorrect area SF-{area}")
    for number, area_data in counts.items():
        if area_data["expected"] != len(area_data["ids"]):
            issues.append(f"SF-{number} area count mismatch: header {area_data['expected']}, rows {len(area_data['ids'])}")
    if len(counts) != 12:
        # We check against this documented snapshot while keeping the script adaptive:
        # a later approved area-count revision updates this navigation constraint.
        if "12 proposed areas" in INDEX.read_text(encoding="utf-8").lower():
            issues.append(f"README still describes 12 areas but found {len(counts)}")
    cross = CROSS.read_text(encoding="utf-8")
    source_refs = SOURCE.findall(cross)
    if len(source_refs) != len(set(source_refs)):
        issues.append("Duplicate model/source R-IDs")
    btext = BOUNDS.read_text(encoding="utf-8")
    boundary_refs = BOUNDARY.findall(btext)
    if len(boundary_refs) != len(set(boundary_refs)):
        issues.append("Duplicate boundary B-IDs")
    ptext = PILOTS.read_text(encoding="utf-8")
    pilot_rows = [PILOT_ROW.match(line) for line in ptext.splitlines()]
    pilot_rows = [x for x in pilot_rows if x]
    pilot_ids = set()
    for m in pilot_rows:
        id_, title, rel, status, source = m.groups()
        if id_ in pilot_ids:
            issues.append(f"Repeated pilot {id_}")
        pilot_ids.add(id_)
        if id_ not in active:
            issues.append(f"Pilot {id_} not in active candidate inventory")
        target = PILOTS.parent / rel
        if not target.is_file():
            issues.append(f"Missing pilot article {rel}")
            continue
        body = target.read_text(encoding="utf-8")
        if f"**Candidate subject:** {id_}" not in body:
            issues.append(f"Pilot candidate ID mismatch in {rel}")
        if "Reviewed" in status and "Reviewed" not in body.split("## ", 1)[0]:
            issues.append(f"Reviewed pilot {id_} lacks matching article frontmatter")
        if "Published" in status:
            issues.append(f"Pilot {id_} improperly marked Published without architecture ratification")
    paths = list(ROOT.rglob("*.md"))
    broken = []
    fragments = 0
    for path in paths:
        body = path.read_text(encoding="utf-8")
        for href in MD_LINK.findall(body):
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if " " in href:
                # A URL with spaces is not unambiguously a simple Markdown file link.
                continue
            raw_path, _, frag = href.partition("#")
            if not raw_path:
                continue
            target = (path.parent / unquote(raw_path)).resolve()
            if not target.is_file():
                broken.append(f"{path.relative_to(ROOT)} -> {href}")
            elif frag:
                fragments += 1
                if unquote(frag).lower() not in markdown_slugs(target.read_text(encoding="utf-8")):
                    issues.append(f"Unresolved heading fragment {path.relative_to(ROOT)} -> {href}")
    if broken:
        issues.extend(f"Broken internal link {x}" for x in broken)
    index = INDEX.read_text(encoding="utf-8")
    declared = re.search(r"\*\*(\d+) active candidate", index)
    if declared and int(declared.group(1)) != len(active):
        issues.append(f"README declares {declared.group(1)} candidates but has {len(active)} active")
    print(f"CANDIDATE_AREAS={len(counts)}")
    print(f"ACTIVE_CANDIDATE_SUBJECTS={len(active)}")
    print(f"MODEL_SOURCE_GROUPS={len(source_refs)}")
    print(f"OWNERSHIP_BOUNDARIES={len(boundary_refs)}")
    print(f"PILOT_MANUSCRIPTS={len(pilot_rows)}")
    print(f"SECURITY_FOUNDATIONS_MARKDOWN_FILES={len(paths)}")
    print(f"INTERNAL_FILE_ERRORS={len(broken)}")
    print(f"CHECKED_HEADING_FRAGMENTS={fragments}")
    print(f"STRUCTURE_ERRORS={len(issues)}")
    print("LIMITATIONS: No external links fetched, no model correctness proof, no source-passage check, no taxonomy ratification or human publication acceptance.")
    for issue in issues:
        print("ERROR", issue)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
